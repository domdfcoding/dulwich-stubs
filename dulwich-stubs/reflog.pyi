# reflog.py -- Parsing and writing reflog files
# Copyright (C) 2015 Jelmer Vernooij and others.
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

from collections import namedtuple
from dulwich.objects import ZERO_SHA as ZERO_SHA, format_timezone as format_timezone, parse_timezone as parse_timezone
from typing import Any, IO, Iterator, Tuple

Entry = namedtuple('Entry', ['old_sha', 'new_sha', 'committer', 'timestamp', 'timezone', 'message'])

def format_reflog_line(old_sha: Any, new_sha: Any, committer: Any, timestamp: Any, timezone: Any, message: Any) -> bytes: ...
def parse_reflog_line(line: Any) -> Tuple[Any, Any, Any, Any, Any, Any]: ...
def read_reflog(f: IO) -> Iterator[Entry]: ...
