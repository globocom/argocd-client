# coding: utf-8
# Copyright (c) 2020, Globo (https://github.com/globocom)
# License: BSD-3-Clause

"""
    Consolidate Services

    Description of all APIs  # noqa: E501

    The version of the OpenAPI document: version not set
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import argocd_client
from argocd_client.models.application_application_sync_request import ApplicationApplicationSyncRequest  # noqa: E501
from argocd_client.rest import ApiException

class TestApplicationApplicationSyncRequest(unittest.TestCase):
    """ApplicationApplicationSyncRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApplicationApplicationSyncRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = argocd_client.models.application_application_sync_request.ApplicationApplicationSyncRequest()  # noqa: E501
        if include_optional :
            return ApplicationApplicationSyncRequest(
                dry_run = True, 
                infos = [
                    argocd_client.models.v1alpha1_info.v1alpha1Info(
                        name = '0', 
                        value = '0', )
                    ], 
                manifests = [
                    '0'
                    ], 
                name = '0', 
                prune = True, 
                resources = [
                    argocd_client.models.v1alpha1_sync_operation_resource.v1alpha1SyncOperationResource(
                        group = '0', 
                        kind = '0', 
                        name = '0', 
                        namespace = '0', )
                    ], 
                retry_strategy = argocd_client.models.v1alpha1_retry_strategy.v1alpha1RetryStrategy(
                    backoff = argocd_client.models.backoff_is_a_backoff_strategy_to_use_within_retry_strategy.Backoff is a backoff strategy to use within retryStrategy(
                        duration = '0', 
                        factor = '0', 
                        max_duration = '0', ), 
                    limit = '0', ), 
                revision = '0', 
                strategy = argocd_client.models.sync_strategy_controls_the_manner_in_which_a_sync_is_performed.SyncStrategy controls the manner in which a sync is performed(
                    apply = argocd_client.models.sync_strategy_apply_uses_`kubectl_apply`_to_perform_the_apply.SyncStrategyApply uses `kubectl apply` to perform the apply(
                        force = True, ), 
                    hook = argocd_client.models.v1alpha1_sync_strategy_hook.v1alpha1SyncStrategyHook(
                        sync_strategy_apply = argocd_client.models.sync_strategy_apply_uses_`kubectl_apply`_to_perform_the_apply.SyncStrategyApply uses `kubectl apply` to perform the apply(
                            force = True, ), ), )
            )
        else :
            return ApplicationApplicationSyncRequest(
        )

    def testApplicationApplicationSyncRequest(self):
        """Test ApplicationApplicationSyncRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
