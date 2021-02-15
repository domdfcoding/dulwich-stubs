# mailmap.py -- Mailmap reader
# Copyright (C) 2018 Jelmer Vernooij <jelmer@jelmer.uk>
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
from typing import IO, Any, Iterator, Optional

def parse_identity(text: Any): ...
def read_mailmap(f: IO) -> Iterator[Any]: ...

class Mailmap:

	def __init__(
			self,
			map: Optional[Any] = ...,  # noqa: A002
			) -> None: ...

	def add_entry(self, canonical_identity: Any, from_identity: Optional[Any] = ...) -> None: ...
	def lookup(self, identity: Any): ...

	@classmethod
	def from_path(cls, path: Any): ...
