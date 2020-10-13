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
from argocd_client.models.v1alpha1_backoff import V1alpha1Backoff  # noqa: E501
from argocd_client.rest import ApiException

class TestV1alpha1Backoff(unittest.TestCase):
    """V1alpha1Backoff unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1alpha1Backoff
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = argocd_client.models.v1alpha1_backoff.V1alpha1Backoff()  # noqa: E501
        if include_optional :
            return V1alpha1Backoff(
                duration = '0', 
                factor = '0', 
                max_duration = '0'
            )
        else :
            return V1alpha1Backoff(
        )

    def testV1alpha1Backoff(self):
        """Test V1alpha1Backoff"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
