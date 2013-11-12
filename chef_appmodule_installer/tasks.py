#/*******************************************************************************
# * Copyright (c) 2013 GigaSpaces Technologies Ltd. All rights reserved
# *
# * Licensed under the Apache License, Version 2.0 (the "License");
# * you may not use this file except in compliance with the License.
# * You may obtain a copy of the License at
# *
# *       http://www.apache.org/licenses/LICENSE-2.0
# *
# * Unless required by applicable law or agreed to in writing, software
# * distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.
# *******************************************************************************/

"""
Celery tasks for running recipes through chef-client.

This file implements the AppModule.installer interface, where for each of tasks, we check that chef is configured
and run the relevant runlist using the chef_client module.
"""

from cosmo.events import send_event, get_cosmo_properties
from cosmo.celery import celery
from chef_client_common.chef_client import run_chef


@celery.task
def deploy(chef_deploy_runlist=None, chef_attributes=None, **kwargs):
    run_chef(chef_deploy_runlist, chef_attributes, **kwargs)


@celery.task
def undeploy(chef_undeploy_runlist=None, chef_attributes=None, **kwargs):
    run_chef(chef_undeploy_runlist, chef_attributes, **kwargs)


@celery.task
def start(__cloudify_id, policy_service, chef_start_runlist=None, chef_attributes=None, **kwargs):
    run_chef(chef_start_runlist, chef_attributes, **kwargs)
    host = get_cosmo_properties()['ip']
    send_event(__cloudify_id, host, policy_service, "state", "running")


@celery.task
def stop(chef_stop_runlist=None, chef_attributes=None, **kwargs):
    run_chef(chef_stop_runlist, chef_attributes, **kwargs)
