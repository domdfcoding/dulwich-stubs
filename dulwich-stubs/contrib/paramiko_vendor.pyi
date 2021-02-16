# paramiko_vendor.py -- paramiko implementation of the SSHVendor interface
# Copyright (C) 2013 Aaron O'Mullan <aaron.omullan@friendco.de>
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

class _ParamikoWrapper:
	client: Any = ...
	channel: Any = ...

	def __init__(self, client: Any, channel: Any) -> None: ...

	@property
	def stderr(self) -> Any: ...

	def can_read(self) -> Any: ...
	def write(self, data: Any) -> Any: ...
	def read(self, n: Optional[int] = ...) -> bytes: ...
	def close(self) -> None: ...

class ParamikoSSHVendor:
	kwargs: Any = ...

	def __init__(self, **kwargs: Any) -> None: ...

	def run_command(
			self,
			host: Any,
			command: Any,
			username: Optional[Any] = ...,
			port: Optional[Any] = ...,
			password: Optional[Any] = ...,
			pkey: Optional[Any] = ...,
			key_filename: Optional[Any] = ...,
			**kwargs: Any
			) -> _ParamikoWrapper: ...
