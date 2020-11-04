# Copyright (C) 2017 Jelmer Vernooij <jelmer@jelmer.uk>
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

from dulwich.config import Config
from dulwich.repo import Repo
from typing import Any, BinaryIO, Iterable, List, Optional, Union

def translate(pat: bytes) -> bytes: ...
def read_ignore_patterns(f: BinaryIO) -> Iterable[bytes]: ...
def match_pattern(path: bytes, pattern: bytes, ignorecase: bool = ...) -> bool: ...

class Pattern:
	pattern: Any = ...
	ignorecase: Any = ...
	is_exclude: bool = ...
	def __init__(self, pattern: bytes, ignorecase: bool = ...) -> None: ...
	def __bytes__(self) -> bytes: ...
	def __eq__(self, other: object) -> bool: ...
	def match(self, path: bytes) -> bool: ...

class IgnoreFilter:
	def __init__(
		self, patterns: Iterable[bytes], ignorecase: bool = ..., path: Any = ...
	) -> None: ...
	def append_pattern(self, pattern: bytes) -> None: ...
	def find_matching(self, path: Union[bytes, str]) -> Iterable[Pattern]: ...
	def is_ignored(self, path: bytes) -> Optional[bool]: ...
	@classmethod
	def from_path(cls: Any, path: Any, ignorecase: bool = ...) -> IgnoreFilter: ...

class IgnoreFilterStack:
	def __init__(self, filters: Any) -> None: ...
	def is_ignored(self, path: str) -> Optional[bool]: ...

def default_user_ignore_filter_path(config: Config) -> str: ...

class IgnoreFilterManager:
	def __init__(
			self,
			top_path: str,
			global_filters: List[IgnoreFilter],
			ignorecase: bool,
	) -> None: ...
	def find_matching(self, path: str) -> Iterable[Pattern]: ...
	def is_ignored(self, path: str) -> Optional[bool]: ...
	@classmethod
	def from_repo(cls: Any, repo: Repo) -> IgnoreFilterManager: ...
