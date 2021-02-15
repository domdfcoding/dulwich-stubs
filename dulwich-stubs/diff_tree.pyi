# diff_tree.py -- Utilities for diffing files and trees.
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
from typing import Any, Iterable, Iterator, NamedTuple, Optional, Tuple

# this package
from dulwich.object_store import BaseObjectStore
from dulwich.objects import TreeEntry

CHANGE_ADD: str
CHANGE_MODIFY: str
CHANGE_DELETE: str
CHANGE_RENAME: str
CHANGE_COPY: str
CHANGE_UNCHANGED: str
RENAME_CHANGE_TYPES: Tuple[str, str]
RENAME_THRESHOLD: int
MAX_FILES: int
REWRITE_THRESHOLD: None

class TreeChange(NamedTuple):
	type: Any  # noqa: A003
	old: Any
	new: Any

	@classmethod
	def add(cls, new: Any) -> TreeChange: ...

	@classmethod
	def delete(cls, old: Any) -> TreeChange: ...

def walk_trees(
		store: BaseObjectStore,
		tree1_id: Optional[Any],
		tree2_id: Optional[Any],
		prune_identical: bool = ...,
		) -> Iterator[Tuple[TreeEntry, TreeEntry]]: ...

def tree_changes(
		store: BaseObjectStore,
		tree1_id: Any,
		tree2_id: Any,
		want_unchanged: bool = ...,
		rename_detector: Optional[Any] = ...,
		include_trees: bool = ...,
		change_type_same: bool = ...,
		) -> Iterator[TreeChange]: ...

def tree_changes_for_merge(
		store: BaseObjectStore,
		parent_tree_ids: Iterable[Any],
		tree_id: Any,
		rename_detector: Optional[RenameDetector] = ...,
		) -> Iterator[TreeChange]: ...

class RenameDetector:

	def __init__(
			self,
			store: Any,
			rename_threshold: Any = ...,
			max_files: Any = ...,
			rewrite_threshold: Any = ...,
			find_copies_harder: bool = ...,
			) -> None: ...

	def changes_with_renames(
			self,
			tree1_id: Any,
			tree2_id: Any,
			want_unchanged: bool = ...,
			include_trees: bool = ...,
			): ...
