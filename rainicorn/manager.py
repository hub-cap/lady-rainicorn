# vim: tabstop=4 shiftwidth=4 softtabstop=4
# -*- coding: utf-8 -*-

# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
from rainicorn.openstack.common import periodic_task
from rainicorn.openstack.common import log as logging

LOG = logging.getLogger(__name__)


class Manager(periodic_task.PeriodicTasks):

    @periodic_task.periodic_task(ticks_between_runs=1)
    def emote(self, context):
        LOG.info(u'글쎄.. 뭐가 있었을까? 아! 우리 완전히 다 벗고 상추밭 미친듯이 뛰어다닌 거 기억 나? (Giggle) 그 농부 아저씨 완전 맛이 갔었지!')