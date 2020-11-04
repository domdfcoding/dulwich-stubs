# objectspec.py -- Object specification
# Copyright (C) 2014 Jelmer Vernooij <jelmer@jelmer.uk>
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

from typing import Any, Iterator, Tuple

from dulwich.repo import Repo

from dulwich.refs import RefsContainer

from dulwich.objects import Commit


def to_bytes(text: Any) -> bytes: ...
def parse_object(repo: Repo, objectish: Any): ...
def parse_tree(repo: Any, treeish: Any): ...
def parse_ref(container: RefsContainer, refspec: bytes) -> bytes: ...
def parse_reftuple(lh_container: RefsContainer, rh_container: RefsContainer, refspec: bytes, force: bool = ...) -> Tuple[bytes, bytes]: ...
def parse_reftuples(lh_container: RefsContainer, rh_container: RefsContainer, refspecs: bytes, force: bool = ...) -> Tuple[bytes, bytes]: ...
def parse_refs(container: RefsContainer, refspecs: Any): ...
def parse_commit_range(repo: Repo, committishs: Any) -> Iterator[Commit]: ...

class AmbiguousShortId(Exception):
    prefix: Any = ...
    options: Any = ...
    def __init__(self, prefix: Any, options: Any) -> None: ...

def scan_for_short_id(object_store: Any, prefix: Any): ...
def parse_commit(repo: Repo, committish: Any) -> Commit: ...
