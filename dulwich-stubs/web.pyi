# web.py -- WSGI smart-http server
# Copyright (C) 2010 Google, Inc.
# Copyright (C) 2012 Jelmer Vernooij <jelmer@jelmer.uk>
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
import sys
from logging import Logger
from types import TracebackType
from typing import IO, Any, AnyStr, Callable, Dict, Iterator, List, Match, Optional, Pattern, Tuple, Type, Union
from wsgiref.simple_server import ServerHandler, WSGIRequestHandler, WSGIServer

# this package
from dulwich.repo import BaseRepo
from dulwich.server import Handler

logger: Logger
HTTP_OK: str
HTTP_NOT_FOUND: str
HTTP_FORBIDDEN: str
HTTP_ERROR: str

def date_time_string(timestamp: Optional[float] = ...) -> str: ...
def url_prefix(mat: Match[str]) -> str: ...
def get_repo(backend: Any, mat: Match[str]) -> BaseRepo: ...
def send_file(req: HTTPGitRequest, f: IO, content_type: Optional[str]) -> Iterator[AnyStr]: ...
def get_text_file(req: HTTPGitRequest, backend: Any, mat: Match[str]) -> Iterator[AnyStr]: ...
def get_loose_object(req: HTTPGitRequest, backend: Any, mat: Match[str]) -> Iterator[Any]: ...
def get_pack_file(req: HTTPGitRequest, backend: Any, mat: Match[str]) -> Iterator[AnyStr]: ...
def get_idx_file(req: HTTPGitRequest, backend: Any, mat: Match[str]) -> Iterator[AnyStr]: ...
def get_info_refs(req: HTTPGitRequest, backend: Any, mat: Match[str]) -> Iterator[AnyStr]: ...
def get_info_packs(req: HTTPGitRequest, backend: Any, mat: Match[str]) -> Iterator[AnyStr]: ...

class _LengthLimitedFile:

	def __init__(
			self,
			input: Any,  # noqa: A002
			max_bytes: Any,
			) -> None: ...

	def read(self, size: int = ...) -> Any: ...

def handle_service_request(req: HTTPGitRequest, backend: Any, mat: Match[str]) -> Iterator[AnyStr]: ...

class HTTPGitRequest:
	environ: Any = ...
	dumb: bool = ...
	handlers: Optional[Any] = ...

	def __init__(
			self,
			environ: Dict[str, Any],
			start_response: Any,
			dumb: bool = ...,
			handlers: Optional[Any] = ...,
			) -> None: ...

	def add_header(self, name: str, value: str) -> None: ...

	def respond(
			self,
			status: str = ...,
			content_type: Optional[str] = ...,
			headers: Optional[List[Tuple[str, str]]] = ...,
			) -> Any: ...

	def not_found(self, message: str) -> bytes: ...
	def forbidden(self, message: str) -> bytes: ...
	def error(self, message: str) -> bytes: ...
	def nocache(self) -> None: ...
	def cache_forever(self) -> None: ...

class HTTPGitApplication:
	services: Dict[Tuple[str, Pattern[str]], Callable[[HTTPGitRequest, Any, Match[str]], Iterator[AnyStr]]] = ...
	backend: Any = ...
	dumb: bool = ...
	handlers: Dict[bytes, Type[Handler]] = ...
	fallback_app: Any = ...

	def __init__(
			self,
			backend: Any,
			dumb: bool = ...,
			handlers: Optional[Any] = ...,
			fallback_app: Optional[Any] = ...,
			) -> None: ...

	def __call__(
			self,
			environ: Dict[str, Any],
			start_response: Any,
			) -> Callable[[HTTPGitRequest, Any, Match[str]], Iterator[AnyStr]]: ...

class GunzipFilter:
	app: Any = ...

	def __init__(self, application: Any) -> None: ...
	def __call__(self, environ: Dict[str, Any], start_response: Any): ...

class LimitedInputFilter:
	app: Any = ...

	def __init__(self, application: Any) -> None: ...
	def __call__(self, environ: Dict[str, Any], start_response: Any): ...

def make_wsgi_chain(
		backend: Any,
		dumb: bool = ...,
		handlers: Optional[Any] = ...,
		fallback_app: Optional[Any] = ...,
		) -> LimitedInputFilter: ...

_SysExcInfoType = Union[Tuple[type, BaseException, Optional[TracebackType]], Tuple[None, None, None]]

if sys.version_info >= (3, 5):
	_ExcInfoType = Union[None, bool, _SysExcInfoType, BaseException]
else:
	_ExcInfoType = Union[None, bool, _SysExcInfoType]

class ServerHandlerLogger(ServerHandler):
	def log_exception(self, exc_info: Any) -> None: ...

	def log_message(
			self,
			format: Any,  # noqa: A002
			*args: Any,  # noqa: A002
			) -> None: ...

	def log_error(self, *args: Any) -> None: ...

class WSGIRequestHandlerLogger(WSGIRequestHandler):
	def log_exception(self, exc_info: _ExcInfoType) -> None: ...

	def log_message(
			self,
			format: Any,  # noqa: A002
			*args: Any,
			) -> None: ...

	def log_error(self, *args: Any) -> None: ...

	raw_requestline: Any = ...

	def handle(self) -> None: ...

class WSGIServerLogger(WSGIServer):
	def handle_error(self, request: Any, client_address: Any) -> None: ...

def main(argv: List[str] = ...) -> None: ...
