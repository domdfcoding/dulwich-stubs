# stdlib
import collections
import os
import stat
import struct
import sys
from typing import TYPE_CHECKING, Any, BinaryIO, Callable, Dict, Iterable, Iterator, List, Optional, Tuple

if TYPE_CHECKING:
	from dulwich.object_store import BaseObjectStore

# this package
from dulwich.file import GitFile
from dulwich.objects import S_IFGITLINK, S_ISGITLINK, Blob, Tree, hex_to_sha, sha_to_hex
from dulwich.pack import SHA1Reader, SHA1Writer



def build_index_from_tree(
		root_path,
		index_path,
		object_store,
		tree_id,
		honor_filemode=True,
		validate_path_element=validate_path_element_default
		):
	"""Generate and materialize index from a tree

    Args:
      tree_id: Tree to materialize
      root_path: Target dir for materialized index files
      index_path: Target path for generated index
      object_store: Non-empty object store holding tree contents
      honor_filemode: An optional flag to honor core.filemode setting in
        config file, default is core.filemode=True, change executable bit
      validate_path_element: Function to validate path elements to check
        out; default just refuses .git and .. directories.

    Note: existing index is wiped and contents are not merged
        in a working dir. Suitable only for fresh clones.
    """

	index = Index(index_path)
	if not isinstance(root_path, bytes):
		root_path = os.fsencode(root_path)

	for entry in object_store.iter_tree_contents(tree_id):
		if not validate_path(entry.path, validate_path_element):
			continue
		full_path = _tree_to_fs_path(root_path, entry.path)

		if not os.path.exists(os.path.dirname(full_path)):
			os.makedirs(os.path.dirname(full_path))

		# TODO(jelmer): Merge new index into working tree
		if S_ISGITLINK(entry.mode):
			if not os.path.isdir(full_path):
				os.mkdir(full_path)
			st = os.lstat(full_path)
			# TODO(jelmer): record and return submodule paths
		else:
			obj = object_store[entry.sha]
			st = build_file_from_blob(obj, entry.mode, full_path, honor_filemode=honor_filemode)

		# Add file to index
		if not honor_filemode or S_ISGITLINK(entry.mode):
			# we can not use tuple slicing to build a new tuple,
			# because on windows that will convert the times to
			# longs, which causes errors further along
			st_tuple = (
					entry.mode,
					st.st_ino,
					st.st_dev,
					st.st_nlink,
					st.st_uid,
					st.st_gid,
					st.st_size,
					st.st_atime,
					st.st_mtime,
					st.st_ctime
					)
			st = st.__class__(st_tuple)
		index[entry.path] = index_entry_from_stat(st, entry.sha, 0)

	index.write()


def blob_from_path_and_mode(fs_path, mode, tree_encoding='utf-8'):
	"""Create a blob from a path and a stat object.

    Args:
      fs_path: Full file system path to file
      st: A stat object
    Returns: A `Blob` object
    """
	assert isinstance(fs_path, bytes)
	blob = Blob()
	if stat.S_ISLNK(mode):
		if sys.platform == 'win32':
			# os.readlink on Python3 on Windows requires a unicode string.
			fs_path = os.fsdecode(fs_path)
			blob.data = os.readlink(fs_path).encode(tree_encoding)
		else:
			blob.data = os.readlink(fs_path)
	else:
		with open(fs_path, 'rb') as f:
			blob.data = f.read()
	return blob


def blob_from_path_and_stat(fs_path, st, tree_encoding='utf-8'):
	"""Create a blob from a path and a stat object.

    Args:
      fs_path: Full file system path to file
      st: A stat object
    Returns: A `Blob` object
    """
	return blob_from_path_and_mode(fs_path, st.st_mode, tree_encoding)


def read_submodule_head(path):
	"""Read the head commit of a submodule.

    Args:
      path: path to the submodule
    Returns: HEAD sha, None if not a valid head/repository
    """
	# this package
	from dulwich.errors import NotGitRepository
	from dulwich.repo import Repo

	# Repo currently expects a "str", so decode if necessary.
	# TODO(jelmer): Perhaps move this into Repo() ?
	if not isinstance(path, str):
		path = os.fsdecode(path)
	try:
		repo = Repo(path)
	except NotGitRepository:
		return None
	try:
		return repo.head()
	except KeyError:
		return None



def get_unstaged_changes(index: Index, root_path, filter_blob_callback=None):
	"""Walk through an index and check for differences against working tree.

    Args:
      index: index to check
      root_path: path in which to find files
    Returns: iterator over paths with unstaged changes
    """
	# For each entry in the index check the sha1 & ensure not staged
	if not isinstance(root_path, bytes):
		root_path = os.fsencode(root_path)

	for tree_path, entry in index.iteritems():
		full_path = _tree_to_fs_path(root_path, tree_path)
		try:
			st = os.lstat(full_path)
			if stat.S_ISDIR(st.st_mode):
				if _has_directory_changed(tree_path, entry):
					yield tree_path
				continue

			if not stat.S_ISREG(st.st_mode) and not stat.S_ISLNK(st.st_mode):
				continue

			blob = blob_from_path_and_stat(full_path, st)

			if filter_blob_callback is not None:
				blob = filter_blob_callback(blob, tree_path)
		except FileNotFoundError:
			# The file was removed, so we assume that counts as
			# different from whatever file used to exist.
			yield tree_path
		else:
			if blob.id != entry.sha:
				yield tree_path


os_sep_bytes = os.sep.encode('ascii')


def index_entry_from_path(path, object_store=None):
	"""Create an index from a filesystem path.

    This returns an index value for files, symlinks
    and tree references. for directories and
    non-existant files it returns None

    Args:
      path: Path to create an index entry for
      object_store: Optional object store to
        save new blobs in
    Returns: An index entry; None for directories
    """
	assert isinstance(path, bytes)
	st = os.lstat(path)
	if stat.S_ISDIR(st.st_mode):
		if os.path.exists(os.path.join(path, b'.git')):
			head = read_submodule_head(path)
			if head is None:
				return None
			return index_entry_from_stat(st, head, 0, mode=S_IFGITLINK)
		return None

	if stat.S_ISREG(st.st_mode) or stat.S_ISLNK(st.st_mode):
		blob = blob_from_path_and_stat(path, st)
		if object_store is not None:
			object_store.add_object(blob)
		return index_entry_from_stat(st, blob.id, 0)

	return None


def iter_fresh_entries(paths, root_path, object_store: Optional['BaseObjectStore'] = None):
	"""Iterate over current versions of index entries on disk.

    Args:
      paths: Paths to iterate over
      root_path: Root path to access from
      store: Optional store to save new blobs in
    Returns: Iterator over path, index_entry
    """
	for path in paths:
		p = _tree_to_fs_path(root_path, path)
		try:
			entry = index_entry_from_path(p, object_store=object_store)
		except (FileNotFoundError, IsADirectoryError):
			entry = None
		yield path, entry


def iter_fresh_blobs(index, root_path):
	"""Iterate over versions of blobs on disk referenced by index.

    Don't use this function; it removes missing entries from index.

    Args:
      index: Index file
      root_path: Root path to access from
      include_deleted: Include deleted entries with sha and
        mode set to None
    Returns: Iterator over path, sha, mode
    """
	# stdlib
	import warnings
	warnings.warn(PendingDeprecationWarning, "Use iter_fresh_objects instead.")
	for entry in iter_fresh_objects(index, root_path, include_deleted=True):
		if entry[1] is None:
			del index[entry[0]]
		else:
			yield entry


def iter_fresh_objects(paths, root_path, include_deleted=False, object_store=None):
	"""Iterate over versions of objecs on disk referenced by index.

    Args:
      root_path: Root path to access from
      include_deleted: Include deleted entries with sha and
        mode set to None
      object_store: Optional object store to report new items to
    Returns: Iterator over path, sha, mode
    """
	for path, entry in iter_fresh_entries(paths, root_path, object_store=object_store):
		if entry is None:
			if include_deleted:
				yield path, None, None
		else:
			entry = IndexEntry(*entry)
			yield path, entry.sha, cleanup_mode(entry.mode)

