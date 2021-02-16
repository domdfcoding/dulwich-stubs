# index.py -- File parser/writer for the git index file
# Copyright (C) 2008-2013 Jelmer Vernooij <jelmer@jelmer.uk>
#
# Dulwich is dual-licensed under the Apache License, Version 2.0 and the GNU
# General Public License by the Free Software Foundation; version 2.0
# or (at your option) any later version. You can redistribute it and/or
# modify it under the terms of either of these two licenses.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# You should have received a copy of the licenses; if not, see
# <http://www.gnu.org/licenses/> for a copy of the GNU General Public License
# and <http://www.apache.org/licenses/LICENSE-2.0> for a copy of the Apache
# License, Version 2.0.
#

# stdlib
from collections import namedtuple
from typing import IO, Any, BinaryIO, Callable, Dict, Iterable, Iterator, List, Optional, Tuple, TypeVar, Union

# this package
from dulwich.object_store import BaseObjectStore

IndexEntry = namedtuple(
		"IndexEntry",
		["ctime", "mtime", "dev", "ino", "mode", "uid", "gid", "size", "sha", "flags"],
		)

FLAG_STAGEMASK: int
FLAG_VALID: int
FLAG_EXTENDED: int
DEFAULT_VERSION: int

def pathsplit(path: bytes) -> Tuple[bytes, bytes]: ...
def pathjoin(*args: bytes): ...
def read_cache_time(f: IO) -> Tuple[Any, ...]: ...
def write_cache_time(f: IO, t: Union[int, float, Tuple[int, int]]) -> None: ...
def read_cache_entry(f: IO) -> Tuple[Any, Any, Any, Any, Any, Any, Any, Any, Any]: ...
def write_cache_entry(f: IO, entry: Tuple[Any, Any, Any, Any, Any, Any, Any, Any, Any, Any, Any]) -> None: ...
def read_index(f: BinaryIO) -> Any: ...
def read_index_dict(f: IO): ...
def write_index(f: BinaryIO, entries: List[Any], version: Optional[int] = ...) -> Any: ...
def write_index_dict(f: BinaryIO, entries: Dict[bytes, IndexEntry], version: Optional[int] = ...) -> None: ...
def cleanup_mode(mode: int) -> int: ...

_F = TypeVar("_F", str, bytes)

class Index:
	def __init__(self, filename: _F) -> None: ...

	@property
	def path(self) -> _F: ...

	def write(self) -> None: ...
	def read(self) -> None: ...
	def __len__(self) -> int: ...
	def __getitem__(self, name: bytes) -> IndexEntry: ...
	def __iter__(self) -> Iterator[bytes]: ...
	def get_sha1(self, path: bytes) -> bytes: ...
	def get_mode(self, path: bytes) -> int: ...
	def iterobjects(self) -> Iterable[Tuple[bytes, bytes, int]]: ...
	def iterblobs(self) -> Iterable[Tuple[bytes, bytes, int]]: ...
	def clear(self) -> None: ...
	def __setitem__(self, name: Any, x: Any) -> None: ...
	def __delitem__(self, name: Any) -> None: ...
	def iteritems(self): ...
	def items(self): ...
	def update(self, entries: Any) -> None: ...
	def changes_from_tree(self, object_store: Any, tree: Any, want_unchanged: bool = ...): ...
	def commit(self, object_store: Any): ...

def commit_tree(object_store: BaseObjectStore, blobs: Iterable[Tuple[bytes, bytes, int]]) -> bytes: ...
def commit_index(object_store: BaseObjectStore, index: Index) -> bytes: ...

_changes_from_tree_iter = Iterable[Tuple[
	Tuple[Optional[bytes], Optional[bytes]],
	Tuple[Optional[int], Optional[int]],
	Tuple[Optional[bytes], Optional[bytes]]
	]]

def changes_from_tree(
		names: Iterable[bytes],
		lookup_entry: Callable[[bytes], Tuple[bytes, int]],
		object_store: BaseObjectStore,
		tree: Optional[bytes],
		want_unchanged: Any = ...,
		) -> _changes_from_tree_iter: ...

def index_entry_from_stat(stat_val: Any, hex_sha: bytes, flags: int, mode: Optional[int] = ...) -> Any: ...

def build_file_from_blob(
		blob: Any,
		mode: Any,
		target_path: Any,
		honor_filemode: bool = ...,
		tree_encoding: str = ...,
		): ...

INVALID_DOTNAMES: Tuple[bytes, bytes, bytes, bytes]

def validate_path_element_default(element: Any) -> bool: ...
def validate_path_element_ntfs(element: Any) -> bool: ...
def validate_path(path: Any, element_validator: Any = ...) -> bool: ...

def build_index_from_tree(
		root_path: Any,
		index_path: Any,
		object_store: Any,
		tree_id: Any,
		honor_filemode: bool = ...,
		validate_path_element: Any = ...,
		) -> None: ...

def blob_from_path_and_mode(fs_path: Any, mode: Any, tree_encoding: str = ...): ...
def blob_from_path_and_stat(fs_path: Any, st: Any, tree_encoding: str = ...): ...
def read_submodule_head(path: Any): ...
def get_unstaged_changes(index: Index, root_path: Any, filter_blob_callback: Any = ...) -> Any: ...

os_sep_bytes: Any

def index_entry_from_path(path: Any, object_store: Optional[Any] = ...): ...
def iter_fresh_entries(paths: Any, root_path: Any, object_store: Optional[BaseObjectStore] = ...) -> Any: ...
def iter_fresh_blobs(index: Any, root_path: Any) -> None: ...

def iter_fresh_objects(
		paths: Any,
		root_path: Any,
		include_deleted: bool = ...,
		object_store: Optional[Any] = ...,
		) -> None: ...

def refresh_index(index: Any, root_path: Any) -> None: ...
