# stdlib
from collections import OrderedDict
from collections.abc import MutableMapping
from typing import Any, AnyStr, BinaryIO, Iterable, Iterator, List, Optional, Tuple, Union

SENTINAL: object

def lower_key(key: Union[bytes, str, Iterable, Any]): ...

class CaseInsensitiveDict(OrderedDict):

	@classmethod
	def make(cls, dict_in: Optional[Union[CaseInsensitiveDict, MutableMapping]] = ...): ...

	def __setitem__(self, key: Any, value: Any, **kwargs: Any) -> None: ...
	def __getitem__(self, item: Any): ...
	def get(self, key: Any, default: Any = ...): ...
	def setdefault(self, key: Any, default: Any = ...): ...

class Config:
	def get(self, section: Tuple[Any, ...], name: Union[str, bytes]) -> Any: ...

	def get_boolean(
			self,
			section: Tuple[Any, ...],
			name: Union[str, bytes],
			default: Optional[bool] = ...,
			) -> bool: ...

	def set(  # noqa: A003  # pylint: disable=redefined-builtin
		self,
		section: Tuple[Any, ...],
		name: Union[str, bytes],
		value: Any,
		) -> None: ...

	def iteritems(
			self,
			section: Tuple[Any, ...],
			) -> Iterator[Tuple[Union[str, bytes], Any]]: ...

	def itersections(self) -> Iterator[Tuple]: ...
	def has_section(self, name: Union[str, bytes]) -> bool: ...

class ConfigDict(Config, MutableMapping):
	encoding: str = ...

	def __init__(
			self,
			values: Optional[Any] = ...,
			encoding: Optional[str] = ...,
			) -> None: ...

	def __eq__(self, other: Any) -> Any: ...
	def __getitem__(self, key: Any): ...
	def __setitem__(self, key: Any, value: Any): ...
	def __delitem__(self, key: Any): ...
	def __iter__(self) -> Any: ...
	def __len__(self): ...
	def get(self, section: Any, name: Any): ...  # type: ignore

	def set(  # noqa: A003  # pylint: disable=redefined-builtin
		self,
		section: Any,
		name: Any,
		value: Any,
		) -> None: ...

	def iteritems(self, section: Any): ...
	def itersections(self): ...

class ConfigFile(ConfigDict):
	path: Any = ...

	def __init__(
			self,
			values: Optional[Any] = ...,
			encoding: Optional[str] = ...,
			) -> None: ...

	@classmethod
	def from_file(cls: Any, f: BinaryIO) -> ConfigFile: ...

	# 		with GitFile(path, 'rb') as f:

	# 			ret = cls.from_file(f)
	# 			ret.path = path
	# 			return ret

	@classmethod
	def from_path(cls: Any, path: Any) -> ConfigFile: ...

	def write_to_path(self, path: Any = ...) -> None: ...

	# 		if path is None:

	# 			path = self.path
	# 		with GitFile(path, 'wb') as f:
	# 			self.write_to_file(f)

	def write_to_file(self, f: BinaryIO) -> None: ...

def get_xdg_config_home_path(*path_segments: AnyStr) -> AnyStr: ...

class StackedConfig(Config):
	backends: Any = ...
	writable: Any = ...

	def __init__(self, backends: Any, writable: Optional[Any] = ...) -> None: ...

	# 		self.backends = backends
	# 		self.writable = writable

	@classmethod
	def default(cls) -> "StackedConfig": ...

	@classmethod
	def default_backends(cls) -> List[ConfigFile]: ...

	def get(self, section: Any, name: Any): ...

	def set(  # noqa: A003  # pylint: disable=redefined-builtin
			self,
			section: Any,
			name: Any,
			value: Any,
			): ...

def parse_submodules(config: ConfigFile) -> Iterator[Tuple[Any, Any, Any]]: ...
