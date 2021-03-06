# walk.py -- General implementation of walking commits and their contents.
# Copyright (C) 2010 Google, Inc.
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
from typing import Any, Callable, Iterable, Iterator, List, Optional, Set, Tuple, Type, Union

# this package
from dulwich.diff_tree import RenameDetector, TreeChange
from dulwich.object_store import BaseObjectStore
from dulwich.objects import Commit

ORDER_DATE: str
ORDER_TOPO: str
ALL_ORDERS: Tuple[str, str]

class WalkEntry:
	commit: Commit = ...

	def __init__(self, walker: Any, commit: Commit) -> None: ...
	def changes(self, path_prefix: Optional[str] = ...) -> Union[List[TreeChange], List[List[TreeChange]]]: ...
	def __repr__(self) -> str: ...

class _CommitTimeQueue:
	def __init__(self, walker: Any) -> None: ...
	def next(self) -> None: ...  # noqa: A003  # pylint: disable=redefined-builtin
	def __next__(self) -> None: ...

class Walker:
	store: BaseObjectStore = ...
	include: Iterable[Union[str, bytes]] = ...
	excluded: Set[Union[str, bytes]] = ...
	order: str = ...
	reverse: bool = ...
	max_entries: Optional[int] = ...
	paths: Optional[Set[Union[str, bytes]]] = ...
	rename_detector: RenameDetector = ...
	get_parents: Any = ...
	follow: bool = ...
	since: float = ...
	until: float = ...

	def __init__(
			self,
			store: BaseObjectStore,
			include: Iterable[Union[str, bytes]],
			exclude: Optional[Iterable[Union[str, bytes]]] = ...,
			order: str = ...,
			reverse: bool = ...,
			max_entries: Optional[int] = ...,
			paths: Optional[Iterable[Union[str, bytes]]] = ...,
			rename_detector: Optional[RenameDetector] = ...,
			follow: bool = ...,
			since: Optional[float] = ...,
			until: Optional[float] = ...,
			get_parents: Callable[[Any], Any] = ...,
			queue_cls: Type = ...,
			): ...

	def __iter__(self) -> Iterator[WalkEntry]: ...
