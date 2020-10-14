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
    def __init__(self, stderr_lines: Optional[Any] = ...) -> None: ...
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
