from dulwich.objects import S_ISGITLINK as S_ISGITLINK, TreeEntry as TreeEntry
from typing import Any, Optional

CHANGE_ADD: str
CHANGE_MODIFY: str
CHANGE_DELETE: str
CHANGE_RENAME: str
CHANGE_COPY: str
CHANGE_UNCHANGED: str
RENAME_CHANGE_TYPES: Any
RENAME_THRESHOLD: int
MAX_FILES: int
REWRITE_THRESHOLD: Any

class TreeChange:
    @classmethod
    def add(cls, new: Any): ...
    @classmethod
    def delete(cls, old: Any): ...

def walk_trees(store: Any, tree1_id: Any, tree2_id: Any, prune_identical: bool = ...) -> None: ...
def tree_changes(store: Any, tree1_id: Any, tree2_id: Any, want_unchanged: bool = ..., rename_detector: Optional[Any] = ..., include_trees: bool = ..., change_type_same: bool = ...) -> None: ...
def tree_changes_for_merge(store: Any, parent_tree_ids: Any, tree_id: Any, rename_detector: Optional[Any] = ...): ...

class RenameDetector:
    def __init__(self, store: Any, rename_threshold: Any = ..., max_files: Any = ..., rewrite_threshold: Any = ..., find_copies_harder: bool = ...) -> None: ...
    def changes_with_renames(self, tree1_id: Any, tree2_id: Any, want_unchanged: bool = ..., include_trees: bool = ...): ...
