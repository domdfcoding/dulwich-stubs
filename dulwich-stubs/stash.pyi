# stash.py
# Copyright (C) 2018 Jelmer Vernooij <jelmer@samba.org>
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
from typing import Any, AnyStr, List, Optional

# this package
from dulwich.reflog import Entry

DEFAULT_STASH_REF: bytes

class Stash:
	def __init__(self, repo: Any, ref: bytes = ...) -> None: ...
	def stashes(self) -> List[Entry]: ...
	@classmethod
	def from_repo(cls, repo: Any) -> "Stash": ...
	def drop(self, index: int) -> None: ...
	def pop(self, index: int) -> None: ...
	def push(
		self,
		committer: Optional[AnyStr] = ...,
		author: Optional[AnyStr] = ...,
		message: Optional[AnyStr] = ...,
	) -> AnyStr: ...
	def __getitem__(self, index: int) -> Entry: ...
	def __len__(self) -> int: ...
