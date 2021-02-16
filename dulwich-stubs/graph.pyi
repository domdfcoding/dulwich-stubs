#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
# Copyright (c) 2020 Kevin B. Hendricks, Stratford Ontario Canada
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

# stdlib
from typing import AnyStr, List, Union

# this package
from dulwich.repo import Repo

def find_merge_base(repo: Repo, commit_ids: List[Union[str, bytes]]): ...
def find_octopus_base(repo: Repo, commit_ids: AnyStr) -> List[AnyStr]: ...
def can_fast_forward(repo: Repo, c1: Union[str, bytes], c2: Union[str, bytes]): ...
