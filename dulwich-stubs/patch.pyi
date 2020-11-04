# patch.py -- For dealing with packed-style patches.
# Copyright (C) 2009-2013 Jelmer Vernooij <jelmer@jelmer.uk>
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
from email.message import Message

from dulwich.objects import Commit
from typing import Any, IO, Optional, Tuple

FIRST_FEW_BYTES: int

def write_commit_patch(
	f: Any,
	commit: Commit,
	contents: Any,
	progress: Tuple,
	version: Optional[Any] = ...,
	encoding: Optional[Any] = ...,
) -> None: ...
def get_summary(commit: Commit) -> str: ...
def unified_diff(
	a: Any,
	b: Any,
	fromfile: str = ...,
	tofile: str = ...,
	fromfiledate: str = ...,
	tofiledate: str = ...,
	n: int = ...,
	lineterm: str = ...,
	tree_encoding: str = ...,
	output_encoding: str = ...,
) -> None: ...
def is_binary(content: Any) -> bytes: ...
def shortid(hexsha: Any) -> bytes: ...
def patch_filename(p: Any, root: Any) -> bytes: ...
def write_object_diff(
	f: IO, store: Any, old_file: Any, new_file: Any, diff_binary: bool = ...
): ...
def gen_diff_header(paths: Any, modes: Any, shas: Any) -> None: ...
def write_blob_diff(f: IO, old_file: Any, new_file: Any): ...
def write_tree_diff(
	f: IO, store: Any, old_tree: Any, new_tree: Any, diff_binary: bool = ...
) -> None: ...
def git_am_patch_split(f: IO, encoding: Optional[Any] = ...): ...
def parse_patch_message(msg: Message, encoding: Optional[str] = ...): ...
