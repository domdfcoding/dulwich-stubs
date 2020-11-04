# greenthreads.py -- Utility module for querying an ObjectStore with gevent
# Copyright (C) 2013 eNovance SAS <licensing@enovance.com>
#
# Author: Fabien Boucher <fabien.boucher@enovance.com>
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

from dulwich.object_store import MissingObjectFinder as MissingObjectFinder, ObjectStoreIterator as ObjectStoreIterator
from dulwich.objects import Commit as Commit, Tag as Tag
from typing import Any, Optional

class GreenThreadsMissingObjectFinder(MissingObjectFinder):
    object_store: Any = ...
    sha_done: Any = ...
    objects_to_send: Any = ...
    progress: Any = ...
    def __init__(self, object_store: Any, haves: Any, wants: Any, progress: Optional[Any] = ..., get_tagged: Optional[Any] = ..., concurrency: int = ..., get_parents: Optional[Any] = ...) -> None: ...

class GreenThreadsObjectStoreIterator(ObjectStoreIterator):
    finder: Any = ...
    p: Any = ...
    def __init__(self, store: Any, shas: Any, finder: Any, concurrency: int = ...) -> None: ...
    def retrieve(self, args: Any): ...
    def __iter__(self) -> Any: ...
    def __len__(self): ...
