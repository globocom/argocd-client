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

import argocd_client
from argocd_client.api.session_service_api import SessionServiceApi  # noqa: E501
from argocd_client.rest import ApiException


class TestSessionServiceApi(unittest.TestCase):
    """SessionServiceApi unit test stubs"""

    def setUp(self):
        self.api = argocd_client.api.session_service_api.SessionServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_mixin11(self):
        """Test case for create_mixin11

        Create a new JWT for authentication and set a cookie if using HTTP.  # noqa: E501
        """
        pass

    def test_delete_mixin11(self):
        """Test case for delete_mixin11

        Delete an existing JWT cookie if using HTTP.  # noqa: E501
        """
        pass

    def test_get_user_info(self):
        """Test case for get_user_info

        Get the current user's info  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
