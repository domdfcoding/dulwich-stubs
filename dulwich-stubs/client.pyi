# stdlib
from typing import Any, Iterable, List, Optional, Tuple, Union

# this package
import dulwich.contrib.paramiko_vendor
from dulwich.config import ConfigDict
from dulwich.errors import SendPackError

class InvalidWants(Exception):
	def __init__(self, wants: Any) -> None: ...

class HTTPUnauthorized(Exception):
	www_authenticate: Any = ...

	def __init__(self, www_authenticate: Any, url: Any) -> None: ...

COMMON_CAPABILITIES: List[bytes]
UPLOAD_CAPABILITIES: List[bytes]
RECEIVE_CAPABILITIES: List[bytes]

class ReportStatusParser:
	def __init__(self) -> None: ...
	def check(self) -> SendPackError: ...
	def handle_packet(self, pkt: Any) -> None: ...

def read_pkt_refs(proto: Any): ...

class FetchPackResult:
	refs: Any = ...
	symrefs: Any = ...
	agent: Any = ...
	new_shallow: Any = ...
	new_unshallow: Any = ...

	def __init__(
			self,
			refs: Any,
			symrefs: Any,
			agent: Any,
			new_shallow: Optional[Any] = ...,
			new_unshallow: Optional[Any] = ...
			) -> None: ...

	def __eq__(self, other: Any) -> Any: ...
	def __contains__(self, name: Any): ...
	def __getitem__(self, name: Any): ...
	def __len__(self): ...
	def __iter__(self) -> Any: ...
	def __getattribute__(self, name: Any): ...

class SendPackResult:
	refs: Any = ...
	agent: Any = ...
	ref_status: Any = ...

	def __init__(self, refs: Any, agent: Optional[Any] = ..., ref_status: Optional[Any] = ...) -> None: ...
	def __eq__(self, other: Any) -> Any: ...
	def __contains__(self, name: Any): ...
	def __getitem__(self, name: Any): ...
	def __len__(self): ...
	def __iter__(self) -> Any: ...
	def __getattribute__(self, name: Any): ...

class GitClient:

	def __init__(
			self,
			thin_packs: bool = ...,
			report_activity: Optional[Any] = ...,
			quiet: bool = ...,
			include_tags: bool = ...
			) -> None: ...

	def get_url(self, path: Any) -> str: ...

	@classmethod
	def from_parsedurl(cls, parsedurl: Any, **kwargs: Any) -> GitClient: ...

	def send_pack(
			self,
			path: Any,
			update_refs: Any,
			generate_pack_data: Any,
			progress: Optional[Any] = ...
			) -> SendPackResult: ...

	def fetch(
			self,
			path: Any,
			target: Any,
			determine_wants: Optional[Any] = ...,
			progress: Optional[Any] = ...,
			depth: Optional[Any] = ...
			): ...

	def fetch_pack(
			self,
			path: Any,
			determine_wants: Any,
			graph_walker: Any,
			pack_data: Any,
			progress: Optional[Any] = ...,
			depth: Optional[Any] = ...
			) -> FetchPackResult: ...

	def get_refs(self, path: bytes) -> None: ...

def check_wants(wants: Any, refs: Any) -> None: ...

class TraditionalGitClient(GitClient):
	DEFAULT_ENCODING: str = ...

	def __init__(self, path_encoding: Any = ..., **kwargs: Any) -> None: ...

	def send_pack(
			self,
			path: Any,
			update_refs: Any,
			generate_pack_data: Any,
			progress: Optional[Any] = ...
			) -> SendPackResult: ...

	def fetch_pack(
			self,
			path: Any,
			determine_wants: Any,
			graph_walker: Any,
			pack_data: Any,
			progress: Optional[Any] = ...,
			depth: Optional[Any] = ...
			) -> FetchPackResult: ...

	def get_refs(self, path: Any): ...

	def archive(
			self,
			path: Any,
			committish: Any,
			write_data: Any,
			progress: Optional[Any] = ...,
			write_error: Optional[Any] = ...,
			format: Optional[Any] = ...,  # noqa: A002  # pylint: disable=redefined-builtin
			subdirs: Optional[Any] = ...,
			prefix: Optional[Any] = ...
			) -> None: ...

class TCPGitClient(TraditionalGitClient):
	def __init__(self, host: Any, port: Optional[Any] = ..., **kwargs: Any) -> None: ...

	@classmethod
	def from_parsedurl(cls, parsedurl: Any, **kwargs: Any): ...

	def get_url(self, path: Any): ...

class SubprocessWrapper:
	proc: Any = ...
	read: Any = ...
	write: Any = ...

	def __init__(self, proc: Any) -> None: ...

	@property
	def stderr(self): ...

	def can_read(self): ...
	def close(self) -> None: ...

def find_git_command(): ...

class SubprocessGitClient(TraditionalGitClient):

	@classmethod
	def from_parsedurl(cls, parsedurl: Any, **kwargs: Any): ...

	git_command: Any = ...

class LocalGitClient(GitClient):

	def __init__(
			self,
			thin_packs: bool = ...,
			report_activity: Optional[Any] = ...,
			config: Optional[Any] = ...
			) -> None: ...

	def get_url(self, path: Any): ...

	@classmethod
	def from_parsedurl(cls, parsedurl: Any, **kwargs: Any): ...

	def send_pack(
			self,
			path: Any,
			update_refs: Any,
			generate_pack_data: Any,
			progress: Optional[Any] = ...
			) -> SendPackResult: ...

	def fetch(
			self,
			path: Any,
			target: Any,
			determine_wants: Optional[Any] = ...,
			progress: Optional[Any] = ...,
			depth: Optional[Any] = ...
			): ...

	def fetch_pack(
			self,
			path: Any,
			determine_wants: Any,
			graph_walker: Any,
			pack_data: Any,
			progress: Optional[Any] = ...,
			depth: Optional[Any] = ...
			) -> FetchPackResult: ...

	def get_refs(self, path: Any): ...

default_local_git_client_cls = LocalGitClient

class SSHVendor:

	def connect_ssh(
			self,
			host: Any,
			command: Any,
			username: Optional[Any] = ...,
			port: Optional[Any] = ...,
			password: Optional[Any] = ...,
			key_filename: Optional[Any] = ...
			): ...

	def run_command(
			self,
			host: Any,
			command: Any,
			username: Optional[Any] = ...,
			port: Optional[Any] = ...,
			password: Optional[Any] = ...,
			key_filename: Optional[Any] = ...
			) -> None: ...

class StrangeHostname(Exception):
	def __init__(self, hostname: Any) -> None: ...

class SubprocessSSHVendor(SSHVendor):

	def run_command(
			self,
			host: Any,
			command: Any,
			username: Optional[Any] = ...,
			port: Optional[Any] = ...,
			password: Optional[Any] = ...,
			key_filename: Optional[Any] = ...
			): ...

class PLinkSSHVendor(SSHVendor):

	def run_command(
			self,
			host: Any,
			command: Any,
			username: Optional[Any] = ...,
			port: Optional[Any] = ...,
			password: Optional[Any] = ...,
			key_filename: Optional[Any] = ...
			): ...

def ParamikoSSHVendor(**kwargs: Any) -> dulwich.contrib.paramiko_vendor.ParamikoSSHVendor: ...

get_ssh_vendor = SubprocessSSHVendor

class SSHGitClient(TraditionalGitClient):
	host: Any = ...
	port: Any = ...
	username: Any = ...
	password: Any = ...
	key_filename: Any = ...
	alternative_paths: Any = ...
	ssh_vendor: Any = ...

	def __init__(
			self,
			host: Any,
			port: Optional[Any] = ...,
			username: Optional[Any] = ...,
			vendor: Optional[Any] = ...,
			config: Optional[Any] = ...,
			password: Optional[Any] = ...,
			key_filename: Optional[Any] = ...,
			**kwargs: Any
			) -> None: ...

	def get_url(self, path: Any): ...

	@classmethod
	def from_parsedurl(cls, parsedurl: Any, **kwargs: Any): ...

def default_user_agent_string() -> str: ...

def default_urllib3_manager(
		config: ConfigDict,
		pool_manager_cls: Optional[Any] = ...,
		proxy_manager_cls: Optional[Any] = ...,
		**override_kwargs: Any
		): ...

class HttpGitClient(GitClient):
	dumb: Any = ...
	pool_manager: Any = ...

	def __init__(
			self,
			base_url: Any,
			dumb: Optional[Any] = ...,
			pool_manager: Optional[Any] = ...,
			config: Optional[Any] = ...,
			username: Optional[Any] = ...,
			password: Optional[Any] = ...,
			**kwargs: Any
			) -> None: ...

	def get_url(self, path: Any): ...

	@classmethod
	def from_parsedurl(cls, parsedurl: Any, **kwargs: Any): ...

	def send_pack(
			self,
			path: bytes,
			update_refs: Any,
			generate_pack_data: Any,
			progress: Optional[Any] = ...
			) -> SendPackResult: ...

	def fetch_pack(
			self,
			path: Any,
			determine_wants: Any,
			graph_walker: Any,
			pack_data: Any,
			progress: Optional[Any] = ...,
			depth: Optional[Any] = ...
			) -> FetchPackResult: ...

	def get_refs(self, path: Any): ...

def get_transport_and_path_from_url(
		url: Any,
		config: Optional[Any] = ...,
		*,
		thin_packs: Any = ...,
		report_activity: Any = ...
		) -> Tuple[GitClient, Any]: ...

def parse_rsync_url(location: str) -> Tuple[Any, Any, Any]: ...

def get_transport_and_path(
		location: Any,
		*,
		config: Any = ...,
		thin_packs: Any = ...,
		report_activity: Any = ...,
		) -> Tuple[GitClient, Any]: ...

DEFAULT_GIT_CREDENTIALS_PATHS: List[str]

def get_credentials_from_store(
		scheme: Any,
		hostname: Any,
		username: Optional[Any] = ...,
		fnames: Iterable[Union[str, bytes]] = ...,
		): ...
