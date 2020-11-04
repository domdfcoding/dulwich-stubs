# stdlib
from typing import Any, Iterator, Optional


class ChunkedBytesIO:
	contents: Any = ...
	pos: Any = ...
	def __init__(self, contents: Any) -> None: ...
	def read(self, maxbytes: Optional[Any] = ...) -> bytes: ...

def tar_stream(
		store: Any,
		tree: Any,
		mtime: Any,
		prefix: bytes = ...,
		format: str = ...,
) -> Iterator[bytes]: ...
