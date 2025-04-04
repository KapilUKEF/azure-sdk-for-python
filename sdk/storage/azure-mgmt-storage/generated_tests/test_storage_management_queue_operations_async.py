# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.storage.aio import StorageManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestStorageManagementQueueOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(StorageManagementClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_queue_create(self, resource_group):
        response = await self.client.queue.create(
            resource_group_name=resource_group.name,
            account_name="str",
            queue_name="str",
            queue={"approximateMessageCount": 0, "id": "str", "metadata": {"str": "str"}, "name": "str", "type": "str"},
            api_version="2024-01-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_queue_update(self, resource_group):
        response = await self.client.queue.update(
            resource_group_name=resource_group.name,
            account_name="str",
            queue_name="str",
            queue={"approximateMessageCount": 0, "id": "str", "metadata": {"str": "str"}, "name": "str", "type": "str"},
            api_version="2024-01-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_queue_get(self, resource_group):
        response = await self.client.queue.get(
            resource_group_name=resource_group.name,
            account_name="str",
            queue_name="str",
            api_version="2024-01-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_queue_delete(self, resource_group):
        response = await self.client.queue.delete(
            resource_group_name=resource_group.name,
            account_name="str",
            queue_name="str",
            api_version="2024-01-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_queue_list(self, resource_group):
        response = self.client.queue.list(
            resource_group_name=resource_group.name,
            account_name="str",
            api_version="2024-01-01",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
