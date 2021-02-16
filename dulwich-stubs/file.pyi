# file.py -- Safe access to git files
# Copyright (C) 2010 Google, Inc.
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
import sys
from typing import IO, Any, Set, Tuple, TypeVar, Union

# StrPath and AnyPath can be used in places where a
# path can be used instead of a string, starting with Python 3.6.
if sys.version_info >= (3, 6):
	# stdlib
	from os import PathLike

	StrPath = Union[str, PathLike[str]]
	BytesPath = Union[bytes, PathLike[bytes]]
	AnyPath = Union[str, bytes, PathLike[str], PathLike[bytes]]
else:
	StrPath = str
	BytesPath = bytes
	AnyPath = Union[str, bytes]

def ensure_dir_exists(dirname: AnyPath) -> None: ...

def GitFile(
		filename: Union[str, bytes],
		mode: str = ...,
		bufsize: int = ...,
		) -> Union[_GitFile, IO]: ...

class FileLocked(Exception):
	filename: Any = ...
	lockfilename: Any = ...

	def __init__(self, filename: Any, lockfilename: Any) -> None: ...

_G = TypeVar("_G", bound="_GitFile")

class _GitFile:
	PROXY_PROPERTIES: Set[str] = ...
	PROXY_METHODS: Tuple[str, ...] = ...

	def __init__(self, filename: Union[str, bytes], mode: str, bufsize: int) -> None: ...
	def abort(self) -> None: ...
	def close(self) -> None: ...
	def __enter__(self: _G) -> _G: ...
	def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None: ...
	def __getattr__(self, name: Any): ...
