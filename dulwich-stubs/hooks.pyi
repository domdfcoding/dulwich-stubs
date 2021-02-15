# hooks.py -- for dealing with git hooks
# Copyright (C) 2012-2013 Jelmer Vernooij and others.
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
from typing import Any, Optional

class Hook:
	def execute(self, *args: Any, **kwargs: Any): ...

class ShellHook(Hook):
	name: Any = ...
	filepath: Any = ...
	numparam: Any = ...
	pre_exec_callback: Any = ...
	post_exec_callback: Any = ...
	cwd: Any = ...

	def __init__(
			self,
			name: Any,
			path: Any,
			numparam: Any,
			pre_exec_callback: Optional[Any] = ...,
			post_exec_callback: Optional[Any] = ...,
			cwd: Optional[Any] = ...,
			) -> None: ...

class PreCommitShellHook(ShellHook):
	def __init__(self, controldir: Any) -> None: ...

class PostCommitShellHook(ShellHook):
	def __init__(self, controldir: Any) -> None: ...

class CommitMsgShellHook(ShellHook):
	def __init__(self, controldir: Any): ...

class PostReceiveShellHook(ShellHook):
	controldir: Any = ...

	def __init__(self, controldir: Any) -> None: ...
	def execute(self, client_refs: Any): ...  # type: ignore
