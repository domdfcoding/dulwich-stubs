# refs.py -- For dealing with git refs
# Copyright (C) 2008-2013 Jelmer Vernooij <jelmer@jelmer.uk>
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
from typing import IO, Any, AnyStr, Dict, Optional, Set

SYMREF: bytes
LOCAL_BRANCH_PREFIX: bytes
LOCAL_TAG_PREFIX: bytes
BAD_REF_CHARS: Set[bytes]
ANNOTATED_TAG_SUFFIX: bytes

def parse_symref_value(contents: bytes) -> bytes: ...
def check_ref_format(refname: bytes) -> bool: ...

class RefsContainer:
	def __init__(self, logger: Optional[Any] = ...) -> None: ...

	def set_symbolic_ref(
			self,
			name: Any,
			other: Any,
			committer: Optional[Any] = ...,
			timestamp: Optional[Any] = ...,
			timezone: Optional[Any] = ...,
			message: Optional[Any] = ...,
			) -> None: ...

	def get_packed_refs(self) -> Dict: ...
	def get_peeled(self, name: Any): ...

	def import_refs(
			self,
			base: Any,
			other: Any,
			committer: Optional[Any] = ...,
			timestamp: Optional[Any] = ...,
			timezone: Optional[Any] = ...,
			message: Optional[Any] = ...,
			prune: bool = ...,
			) -> None: ...

	def allkeys(self) -> None: ...
	def __iter__(self) -> Any: ...
	def keys(self, base: Optional[Any] = ...): ...
	def subkeys(self, base: Any): ...
	def as_dict(self, base: Optional[Any] = ...) -> Dict: ...
	def read_ref(self, refname: Any): ...
	def read_loose_ref(self, name: Any) -> None: ...
	def follow(self, name: Any): ...
	def __contains__(self, refname: Any): ...
	def __getitem__(self, name: Any): ...

	def set_if_equals(
			self,
			name: Any,
			old_ref: Any,
			new_ref: Any,
			committer: Optional[Any] = ...,
			timestamp: Optional[Any] = ...,
			timezone: Optional[Any] = ...,
			message: Optional[Any] = ...,
			) -> bool: ...

	def add_if_new(self, name: Any, ref: Any): ...
	def __setitem__(self, name: Any, ref: Any) -> None: ...

	def remove_if_equals(
			self,
			name: Any,
			old_ref: Any,
			committer: Optional[Any] = ...,
			timestamp: Optional[Any] = ...,
			timezone: Optional[Any] = ...,
			message: Optional[Any] = ...,
			) -> bool: ...

	def __delitem__(self, name: Any) -> None: ...
	def get_symrefs(self): ...
	def watch(self) -> None: ...

class _DictRefsWatcher:
	def __init__(self, refs: Any) -> None: ...

	queue: Any = ...

	def __enter__(self): ...
	def __next__(self): ...
	def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any): ...

class DictRefsContainer(RefsContainer):
	def __init__(self, refs: Any, logger: Optional[Any] = ...) -> None: ...
	def allkeys(self): ...
	def read_loose_ref(self, name: Any) -> Optional[Any]: ...
	def get_packed_refs(self): ...
	def watch(self): ...

	def set_symbolic_ref(
			self,
			name: Any,
			other: Any,
			committer: Optional[Any] = ...,
			timestamp: Optional[Any] = ...,
			timezone: Optional[Any] = ...,
			message: Optional[Any] = ...,
			) -> None: ...

	def set_if_equals(
			self,
			name: Any,
			old_ref: Any,
			new_ref: Any,
			committer: Optional[Any] = ...,
			timestamp: Optional[Any] = ...,
			timezone: Optional[Any] = ...,
			message: Optional[Any] = ...,
			) -> bool: ...

	def add_if_new(
			self,
			name: Any,
			ref: Any,
			committer: Optional[Any] = ...,
			timestamp: Optional[Any] = ...,
			timezone: Optional[Any] = ...,
			message: Optional[Any] = ...,
			) -> bool: ...

	def remove_if_equals(
			self,
			name: Any,
			old_ref: Any,
			committer: Optional[Any] = ...,
			timestamp: Optional[Any] = ...,
			timezone: Optional[Any] = ...,
			message: Optional[Any] = ...,
			): ...

	def get_peeled(self, name: Any): ...

class InfoRefsContainer(RefsContainer):
	def __init__(self, f: Any) -> None: ...
	def allkeys(self): ...
	def read_loose_ref(self, name: Any): ...
	def get_packed_refs(self) -> Dict[AnyStr, AnyStr]: ...
	def get_peeled(self, name: Any): ...

class _InotifyRefsWatcher:
	path: Any = ...
	manager: Any = ...
	notifier: Any = ...
	queue: Any = ...

	def __init__(self, path: Any) -> None: ...
	def __next__(self): ...
	def __enter__(self): ...
	def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any): ...

class DiskRefsContainer(RefsContainer):
	path: Any = ...
	worktree_path: Any = ...

	def __init__(self, path: Any, worktree_path: Optional[Any] = ..., logger: Optional[Any] = ...) -> None: ...
	def subkeys(self, base: Any): ...
	def allkeys(self): ...
	def refpath(self, name: Any): ...
	def get_packed_refs(self): ...
	def get_peeled(self, name: Any): ...
	def read_loose_ref(self, name: Any): ...

	def set_symbolic_ref(
			self,
			name: Any,
			other: Any,
			committer: Optional[Any] = ...,
			timestamp: Optional[Any] = ...,
			timezone: Optional[Any] = ...,
			message: Optional[Any] = ...,
			) -> None: ...

	def set_if_equals(
			self,
			name: Any,
			old_ref: Any,
			new_ref: Any,
			committer: Optional[Any] = ...,
			timestamp: Optional[Any] = ...,
			timezone: Optional[Any] = ...,
			message: Optional[Any] = ...,
			): ...

	def add_if_new(
			self,
			name: Any,
			ref: Any,
			committer: Optional[Any] = ...,
			timestamp: Optional[Any] = ...,
			timezone: Optional[Any] = ...,
			message: Optional[Any] = ...,
			): ...

	def remove_if_equals(
			self,
			name: Any,
			old_ref: Any,
			committer: Optional[Any] = ...,
			timestamp: Optional[Any] = ...,
			timezone: Optional[Any] = ...,
			message: Optional[Any] = ...,
			): ...

	def watch(self): ...

def read_packed_refs(f: IO[bytes]) -> None: ...
def read_packed_refs_with_peeled(f: IO[bytes]) -> None: ...
def write_packed_refs(f: IO[bytes], packed_refs: Any, peeled_refs: Optional[Any] = ...) -> None: ...
def read_info_refs(f: Any): ...
def write_info_refs(refs: Any, store: Any) -> None: ...
def is_local_branch(x: Any): ...
def strip_peeled_refs(refs: Any) -> Dict: ...
