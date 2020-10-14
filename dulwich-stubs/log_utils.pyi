import logging
from typing import Any

getLogger = logging.getLogger

class _NullHandler(logging.Handler):
    def emit(self, record: Any) -> None: ...

def default_logging_config() -> None: ...
def remove_null_handler() -> None: ...
