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
from argocd_client.models.v1alpha1_resource_networking_info import V1alpha1ResourceNetworkingInfo  # noqa: E501
from argocd_client.rest import ApiException

class TestV1alpha1ResourceNetworkingInfo(unittest.TestCase):
    """V1alpha1ResourceNetworkingInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1alpha1ResourceNetworkingInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = argocd_client.models.v1alpha1_resource_networking_info.V1alpha1ResourceNetworkingInfo()  # noqa: E501
        if include_optional :
            return V1alpha1ResourceNetworkingInfo(
                external_ur_ls = [
                    '0'
                    ], 
                ingress = [
                    argocd_client.models.v1_load_balancer_ingress.v1LoadBalancerIngress(
                        hostname = '0', 
                        ip = '0', )
                    ], 
                labels = {
                    'key' : '0'
                    }, 
                target_labels = {
                    'key' : '0'
                    }, 
                target_refs = [
                    argocd_client.models.resource_ref_includes_fields_which_unique_identify_resource.ResourceRef includes fields which unique identify resource(
                        group = '0', 
                        kind = '0', 
                        name = '0', 
                        namespace = '0', 
                        uid = '0', 
                        version = '0', )
                    ]
            )
        else :
            return V1alpha1ResourceNetworkingInfo(
        )

    def testV1alpha1ResourceNetworkingInfo(self):
        """Test V1alpha1ResourceNetworkingInfo"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
