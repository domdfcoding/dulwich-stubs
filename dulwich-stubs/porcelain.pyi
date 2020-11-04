# porcelain.py -- Porcelain-like layer on top of Dulwich
# Copyright (C) 2013 Jelmer Vernooij <jelmer@jelmer.uk>
#
# Dulwich is dual-licensed under the Apache License, Version 2.0 and the GNU
# General Public License as public by the Free Software Foundation; version 2.0
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
import os
from collections import namedtuple
from io import RawIOBase
from typing import Any, Optional, Tuple, Union

# this package
from dulwich.repo import BaseRepo, Repo

GitStatus = namedtuple("GitStatus", "staged unstaged untracked")

class NoneStream(RawIOBase):
	def read(self, size: int = ...): ...
	def readall(self): ...
	def readinto(self, b: Any): ...
	def write(self, b: Any): ...

default_bytes_out_stream: Any
default_bytes_err_stream: Any
DEFAULT_ENCODING: str

class Error(Exception):
	inner: Any = ...
	def __init__(self, msg: Any, inner: Optional[Any] = ...) -> None: ...

class RemoteExists(Error): ...

def open_repo(path_or_repo: Any) -> BaseRepo: ...
def open_repo_closing(path_or_repo: Union[str, os.PathLike, Repo]) -> Repo: ...
def path_to_tree_path(repopath: Any, path: Any, tree_encoding: Any = ...): ...

class DivergedBranches(Error): ...

def check_diverged(repo: Repo, current_sha: Any, new_sha: Any) -> None: ...
def archive(
	repo: Any, committish: Optional[Any] = ..., outstream: Any = ..., errstream: Any = ...
) -> None: ...
def update_server_info(repo: str = ...) -> None: ...
def symbolic_ref(repo: str, ref_name: Any, force: bool = ...) -> None: ...
def commit(
	repo: str = ...,
	message: Optional[Any] = ...,
	author: Optional[Any] = ...,
	committer: Optional[Any] = ...,
	encoding: Optional[Any] = ...,
): ...
def commit_tree(
	repo: str,
	tree: Any,
	message: Optional[Any] = ...,
	author: Optional[Any] = ...,
	committer: Optional[Any] = ...,
): ...
def init(path: str = ..., bare: bool = ...): ...
def clone(
	source: Any,
	target: Optional[Any] = ...,
	bare: bool = ...,
	checkout: Optional[Any] = ...,
	errstream: Any = ...,
	outstream: Optional[Any] = ...,
	origin: bytes = ...,
	depth: Optional[Any] = ...,
	**kwargs: Any
): ...
def add(repo: str = ..., paths: Optional[Any] = ...): ...
def clean(repo: str = ..., target_dir: Optional[Any] = ...) -> None: ...
def remove(repo: str = ..., paths: Optional[Any] = ..., cached: bool = ...) -> None: ...

rm = remove

def commit_decode(commit: Any, contents: Any, default_encoding: Any = ...): ...
def commit_encode(commit: Any, contents: Any, default_encoding: Any = ...): ...
def print_commit(commit: Any, decode: Any, outstream: Any = ...) -> None: ...
def print_tag(tag: Any, decode: Any, outstream: Any = ...) -> None: ...
def show_blob(repo: Any, blob: Any, decode: Any, outstream: Any = ...) -> None: ...
def show_commit(repo: Any, commit: Any, decode: Any, outstream: Any = ...) -> None: ...
def show_tree(repo: Any, tree: Any, decode: Any, outstream: Any = ...) -> None: ...
def show_tag(repo: Any, tag: Any, decode: Any, outstream: Any = ...) -> None: ...
def show_object(repo: Any, obj: Any, decode: Any, outstream: Any): ...
def print_name_status(changes: Any) -> None: ...
def log(
	repo: str = ...,
	paths: Optional[Any] = ...,
	outstream: Any = ...,
	max_entries: Optional[Any] = ...,
	reverse: bool = ...,
	name_status: bool = ...,
): ...
def show(
	repo: str = ...,
	objects: Optional[Any] = ...,
	outstream: Any = ...,
	default_encoding: Any = ...,
): ...
def diff_tree(
	repo: Any, old_tree: Any, new_tree: Any, outstream: Any = ...
) -> None: ...
def rev_list(repo: Any, commits: Any, outstream: Any = ...) -> None: ...
def tag(*args: Any, **kwargs: Any): ...
def tag_create(
	repo: Any,
	tag: Any,
	author: Optional[Any] = ...,
	message: Optional[Any] = ...,
	annotated: bool = ...,
	objectish: str = ...,
	tag_time: Optional[Any] = ...,
	tag_timezone: Optional[Any] = ...,
	sign: bool = ...,
) -> None: ...
def list_tags(*args: Any, **kwargs: Any): ...
def tag_list(repo: Any, outstream: Any = ...): ...
def tag_delete(repo: Any, name: Any) -> None: ...
def reset(repo: Any, mode: Any, treeish: str = ...) -> None: ...
def get_remote_repo(
	repo: Repo, remote_location: Optional[Union[str, bytes]] = ...
) -> Tuple[Optional[str], str]: ...
def push(
	repo: Any,
	remote_location: Optional[Any] = ...,
	refspecs: Optional[Any] = ...,
	outstream: Any = ...,
	errstream: Any = ...,
	force: bool = ...,
	**kwargs: Any
): ...
def pull(
	repo: Any,
	remote_location: Optional[Any] = ...,
	refspecs: Optional[Any] = ...,
	outstream: Any = ...,
	errstream: Any = ...,
	fast_forward: bool = ...,
	force: bool = ...,
	**kwargs: Any
): ...
def status(repo: Union[str, Repo] = ..., ignored: bool = ...): ...
def get_untracked_paths(frompath: Any, basepath: Any, index: Any) -> None: ...
def get_tree_changes(repo: Any): ...
def daemon(
	path: str = ..., address: Optional[Any] = ..., port: Optional[Any] = ...
) -> None: ...
def web_daemon(
	path: str = ..., address: Optional[Any] = ..., port: Optional[Any] = ...
) -> None: ...
def upload_pack(
	path: str = ..., inf: Optional[Any] = ..., outf: Optional[Any] = ...
): ...
def receive_pack(
	path: str = ..., inf: Optional[Any] = ..., outf: Optional[Any] = ...
): ...
def branch_delete(repo: Any, name: Any) -> None: ...
def branch_create(
	repo: Any, name: Any, objectish: Optional[Any] = ..., force: bool = ...
) -> None: ...
def branch_list(repo: Any): ...
def active_branch(repo: Any): ...
def get_branch_remote(repo: Any): ...
def fetch(
	repo: Any,
	remote_location: Optional[Any] = ...,
	outstream: Any = ...,
	errstream: Any = ...,
	message: Optional[Any] = ...,
	depth: Optional[Any] = ...,
	prune: bool = ...,
	prune_tags: bool = ...,
	force: bool = ...,
	**kwargs: Any
): ...
def ls_remote(remote: Any, config: Optional[Any] = ..., **kwargs: Any): ...
def repack(repo: Any) -> None: ...
def pack_objects(
	repo: Any,
	object_ids: Any,
	packf: Any,
	idxf: Any,
	delta_window_size: Optional[Any] = ...,
) -> None: ...
def ls_tree(
	repo: Any,
	treeish: bytes = ...,
	outstream: Any = ...,
	recursive: bool = ...,
	name_only: bool = ...,
) -> None: ...
def remote_add(repo: Any, name: Any, url: Any) -> None: ...
def check_ignore(repo: Any, paths: Any, no_index: bool = ...) -> None: ...
def update_head(
	repo: Any, target: Any, detached: bool = ..., new_branch: Optional[Any] = ...
) -> None: ...
def check_mailmap(repo: Any, contact: Any): ...
def fsck(repo: Any) -> None: ...
def stash_list(repo: Any): ...
def stash_push(repo: Any) -> None: ...
def stash_pop(repo: Any) -> None: ...
def ls_files(repo: Any): ...
def describe(repo: Any): ...
def get_object_by_path(repo: Any, path: Any, committish: Optional[Any] = ...): ...
def write_tree(repo: Any): ...
