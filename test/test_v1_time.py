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
from argocd_client.models.v1_time import V1Time  # noqa: E501
from argocd_client.rest import ApiException

class TestV1Time(unittest.TestCase):
    """V1Time unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1Time
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = argocd_client.models.v1_time.V1Time()  # noqa: E501
        if include_optional :
            return V1Time(
                nanos = 56, 
                seconds = '0'
            )
        else :
            return V1Time(
        )

    def testV1Time(self):
        """Test V1Time"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
