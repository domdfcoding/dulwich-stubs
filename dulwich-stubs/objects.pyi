# objects.py -- Access to base git objects
# Copyright (C) 2007 James Westby <jw+debian@jameswestby.net>
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
from typing import Any, AnyStr, NamedTuple, Optional, Tuple, Type, Union

# this package
from dulwich.errors import FileFormatException

ZERO_SHA: bytes
S_IFGITLINK: int
MAX_TIME: int
BEGIN_PGP_SIGNATURE: bytes

class EmptyFileException(FileFormatException): ...

def S_ISGITLINK(m: Any) -> bool: ...
def sha_to_hex(sha: Any) -> bytes: ...
def hex_to_sha(hex: Any) -> bytes: ...  # noqa: A002  # pylint: disable=redefined-builtin
def valid_hexsha(hex: Any) -> bool: ...  # noqa: A002  # pylint: disable=redefined-builtin

def hex_to_filename(
		path: AnyStr,
		hex: AnyStr,  # noqa: A002  # pylint: disable=redefined-builtin
		) -> AnyStr: ...

def filename_to_hex(filename: Any) -> bytes: ...
def object_header(num_type: int, length: int) -> bytes: ...
def serializable_property(name: str, docstring: Optional[str] = ...) -> property: ...
def object_class(

		type: Union[bytes, int],  # noqa: A002  # pylint: disable=redefined-builtin
		) -> Optional[Type[ShaFile]]: ...

def check_hexsha(

		hex: Any,  # noqa: A002  # pylint: disable=redefined-builtin
		error_msg: Any,
		) -> None: ...

def check_identity(identity: bytes, error_msg: Any) -> None: ...
def check_time(time_seconds: float) -> None: ...
def git_line(*items: Any) -> bytes: ...

class FixedSha:
	def __init__(self, hexsha: Any) -> None: ...
	def digest(self) -> bytes: ...
	def hexdigest(self) -> str: ...

class ShaFile:
	type_name: Optional[bytes] = ...
	type_num: Optional[int] = ...

	def as_legacy_object_chunks(self, compression_level: int = ...) -> None: ...
	def as_legacy_object(self, compression_level: int = ...): ...
	def as_raw_chunks(self): ...
	def as_raw_string(self) -> bytes: ...
	def __bytes__(self) -> bytes: ...
	def __hash__(self) -> int: ...
	def as_pretty_string(self) -> bytes: ...
	def set_raw_string(self, text: bytes, sha: Optional[Any] = ...) -> None: ...
	def set_raw_chunks(self, chunks: Any, sha: Optional[Any] = ...) -> None: ...
	def __init__(self) -> None: ...

	@classmethod
	def from_path(cls, path: Any): ...

	@classmethod
	def from_file(cls, f: Any): ...

	@staticmethod
	def from_raw_string(type_num: Any, string: Any, sha: Optional[Any] = ...): ...

	@staticmethod
	def from_raw_chunks(type_num: Any, chunks: Any, sha: Optional[Any] = ...): ...

	@classmethod
	def from_string(cls, string: Any): ...

	def check(self) -> None: ...
	def raw_length(self): ...
	def sha(self): ...
	def copy(self): ...

	@property
	def id(self): ...  # noqa: A003  # pylint: disable=redefined-builtin

	def get_type(self): ...

	def set_type(
			self,
			type: Any,  # noqa: A002  # pylint: disable=redefined-builtin
			) -> None: ...

	type: Any = ...  # noqa: A003  # pylint: disable=redefined-builtin

	def __ne__(self, other: Any) -> Any: ...
	def __eq__(self, other: Any) -> Any: ...
	def __lt__(self, other: Any) -> Any: ...
	def __le__(self, other: Any) -> Any: ...
	def __cmp__(self, other: Any): ...

class Blob(ShaFile):
	type_name: bytes = ...
	type_num: int = ...

	def __init__(self) -> None: ...

	data: Any = ...
	chunked: Any = ...

	@classmethod
	def from_path(cls, path: Any): ...

	def check(self) -> None: ...
	def splitlines(self): ...

class Tag(ShaFile):
	type_name: bytes = ...
	type_num: int = ...

	def __init__(self) -> None: ...

	@classmethod
	def from_path(cls, filename: Any): ...

	def check(self) -> None: ...

	object: Any = ...  # noqa: A003  # pylint: disable=redefined-builtin
	name: Any = ...
	tagger: Any = ...
	tag_time: Any = ...
	tag_timezone: Any = ...
	message: Any = ...
	signature: Any = ...

class TreeEntry(NamedTuple):
	path: bytes
	mode: Any
	sha: bytes

	def in_path(self, path: Any): ...

def parse_tree(text: Any, strict: bool = ...) -> None: ...
def serialize_tree(items: Any) -> None: ...
def sorted_tree_items(entries: Any, name_order: Any) -> None: ...
def key_entry(entry: Any): ...
def key_entry_name_order(entry: Any): ...
def pretty_format_tree_entry(name: Any, mode: Any, hexsha: Any, encoding: str = ...): ...

class Tree(ShaFile):
	type_name: bytes = ...
	type_num: int = ...

	def __init__(self) -> None: ...

	@classmethod
	def from_path(cls, filename: Any): ...

	def __contains__(self, name: Any): ...
	def __getitem__(self, name: Any): ...
	def __setitem__(self, name: Any, value: Any) -> None: ...
	def __delitem__(self, name: Any) -> None: ...
	def __len__(self): ...
	def __iter__(self) -> Any: ...
	def add(self, name: Any, mode: Any, hexsha: Any) -> None: ...
	def iteritems(self, name_order: bool = ...): ...
	def items(self): ...
	def check(self) -> None: ...
	def as_pretty_string(self): ...
	def lookup_path(self, lookup_obj: Any, path: Any): ...

def parse_timezone(text: Any): ...
def format_timezone(offset: Any, unnecessary_negative_timezone: bool = ...): ...
def parse_time_entry(value: bytes): ...
def parse_commit(chunks: Any): ...

class Commit(ShaFile):
	type_name: bytes = ...
	type_num: int = ...

	def __init__(self) -> None: ...

	@classmethod
	def from_path(cls, path: Any) -> Commit: ...

	def check(self) -> None: ...

	tree: Any = ...
	parents: Any = ...
	extra: Any = ...
	author: Any = ...
	committer: Any = ...
	message: Any = ...
	commit_time: Any = ...
	commit_timezone: Any = ...
	author_time: Any = ...
	author_timezone: Any = ...
	encoding: Any = ...
	mergetag: Any = ...
	gpgsig: Any = ...


OBJECT_CLASSES: Tuple[Type[Commit], Type[Tree], Type[Blob], Type[Tag]]

cls: Type[ShaFile]
del cls
