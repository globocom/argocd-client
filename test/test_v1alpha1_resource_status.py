# coding: utf-8

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
from argocd_client.models.v1alpha1_resource_status import V1alpha1ResourceStatus  # noqa: E501
from argocd_client.rest import ApiException

class TestV1alpha1ResourceStatus(unittest.TestCase):
    """V1alpha1ResourceStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1alpha1ResourceStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = argocd_client.models.v1alpha1_resource_status.V1alpha1ResourceStatus()  # noqa: E501
        if include_optional :
            return V1alpha1ResourceStatus(
                group = '0', 
                health = argocd_client.models.v1alpha1_health_status.v1alpha1HealthStatus(
                    message = '0', 
                    status = '0', ), 
                hook = True, 
                kind = '0', 
                name = '0', 
                namespace = '0', 
                requires_pruning = True, 
                status = '0', 
                version = '0'
            )
        else :
            return V1alpha1ResourceStatus(
        )

    def testV1alpha1ResourceStatus(self):
        """Test V1alpha1ResourceStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()