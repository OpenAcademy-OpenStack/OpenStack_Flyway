# -*- coding: utf-8 -*-

#    Copyright (C) 2012 eBay, Inc. All Rights Reserved.
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

from taskflow import task
import keystoneclient.v2_0.client as ksclient
from common import config
from oslo.config import cfg


class UserTenantMigrateTask(task.Task):
    """
    Task to migrate to a particular tenant (project) of a particular user
    from the source cloud to the target cloud.
    """
    def execute(self, user_id, tenant_id):
        keystone = ksclient.Client(username=cfg.CONF.SOURCE.os_username,
                                   password=cfg.CONF.SOURCE.os_password,
                                   auth_url=cfg.CONF.SOURCE.os_auth_url,
                                   tenant_name=cfg.CONF.SOURCE.os_tenant_name)
        users = keystone.users
        print keystone.tokens
        print keystone.auth_token

        #Below script has auth error...
        print users.list()
        print 'Executing UserMigrateTask'
