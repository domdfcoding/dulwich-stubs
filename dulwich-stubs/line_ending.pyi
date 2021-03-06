# line_ending.py -- Line ending conversion functions
# Copyright (C) 2018-2018 Boris Feld <boris.feld@comet.ml>
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
from typing import Any, Callable, Optional

CRLF: bytes
LF: bytes

def convert_crlf_to_lf(text_hunk: bytes) -> bytes: ...
def convert_lf_to_crlf(text_hunk: bytes) -> bytes: ...
def get_checkout_filter(core_eol: Any, core_autocrlf: Any, git_attributes: Any): ...
def get_checkin_filter(core_eol: Any, core_autocrlf: Any, git_attributes: Any): ...
def get_checkout_filter_autocrlf(core_autocrlf: bytes) -> Optional[Callable[[bytes], bytes]]: ...
def get_checkin_filter_autocrlf(core_autocrlf: bytes) -> Optional[Callable[[bytes], bytes]]: ...

class BlobNormalizer:
	config_stack: Any = ...
	gitattributes: Any = ...
	fallback_read_filter: Any = ...
	fallback_write_filter: Any = ...

	def __init__(self, config_stack: Any, gitattributes: Any) -> None: ...
	def checkin_normalize(self, blob: Any, tree_path: Any): ...
	def checkout_normalize(self, blob: Any, tree_path: Any): ...

def normalize_blob(blob: Any, conversion: Any, binary_detection: Any): ...
