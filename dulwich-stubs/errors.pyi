# errors.py -- errors for dulwich
# Copyright (C) 2007 James Westby <jw+debian@jameswestby.net>
# Copyright (C) 2009-2012 Jelmer Vernooij <jelmer@jelmer.uk>
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

class ChecksumMismatch(Exception):
	expected: Any = ...
	got: Any = ...
	extra: Any = ...

	def __init__(self, expected: Any, got: Any, extra: Optional[Any] = ...) -> None: ...

class WrongObjectException(Exception):

	def __init__(self, sha: Any, *args: Any, **kwargs: Any) -> None: ...

class NotCommitError(WrongObjectException):
	type_name: str = ...

class NotTreeError(WrongObjectException):
	type_name: str = ...

class NotTagError(WrongObjectException):
	type_name: str = ...

class NotBlobError(WrongObjectException):
	type_name: str = ...

class MissingCommitError(Exception):
	sha: Any = ...

	def __init__(self, sha: Any, *args: Any, **kwargs: Any) -> None: ...

class ObjectMissing(Exception):

	def __init__(self, sha: Any, *args: Any, **kwargs: Any) -> None: ...

class ApplyDeltaError(Exception):

	def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class NotGitRepository(Exception):

	def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class GitProtocolError(Exception):

	def __init__(self, *args: Any, **kwargs: Any) -> None: ...
	def __eq__(self, other: Any) -> Any: ...

class SendPackError(GitProtocolError): ...

class UpdateRefsError(GitProtocolError):
	ref_status: Any = ...

	def __init__(self, *args: Any, **kwargs: Any) -> None: ...

class HangupException(GitProtocolError):
	stderr_lines: Any = ...

	def __init__(self, stderr_lines: Optional[bytes] = ...) -> None: ...
	def __eq__(self, other: Any) -> Any: ...

class UnexpectedCommandError(GitProtocolError):

	def __init__(self, command: Any) -> None: ...

class FileFormatException(Exception): ...

class PackedRefsException(FileFormatException): ...

class ObjectFormatException(FileFormatException): ...

class NoIndexPresent(Exception): ...

class CommitError(Exception): ...

class RefFormatError(Exception): ...

class HookError(Exception): ...
