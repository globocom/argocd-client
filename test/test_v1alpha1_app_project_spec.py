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
from argocd_client.models.v1alpha1_app_project_spec import V1alpha1AppProjectSpec  # noqa: E501
from argocd_client.rest import ApiException

class TestV1alpha1AppProjectSpec(unittest.TestCase):
    """V1alpha1AppProjectSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1alpha1AppProjectSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = argocd_client.models.v1alpha1_app_project_spec.V1alpha1AppProjectSpec()  # noqa: E501
        if include_optional :
            return V1alpha1AppProjectSpec(
                cluster_resource_blacklist = [
                    argocd_client.models.group_kind_specifies_a_group_and_a_kind,_but_does_not_force_a_version/__this_is_useful_for_identifying
concepts_during_lookup_stages_without_having_partially_valid_types.GroupKind specifies a Group and a Kind, but does not force a version.  This is useful for identifying
concepts during lookup stages without having partially valid types(
                        group = '0', 
                        kind = '0', )
                    ], 
                cluster_resource_whitelist = [
                    argocd_client.models.group_kind_specifies_a_group_and_a_kind,_but_does_not_force_a_version/__this_is_useful_for_identifying
concepts_during_lookup_stages_without_having_partially_valid_types.GroupKind specifies a Group and a Kind, but does not force a version.  This is useful for identifying
concepts during lookup stages without having partially valid types(
                        group = '0', 
                        kind = '0', )
                    ], 
                description = '0', 
                destinations = [
                    argocd_client.models.application_destination_contains_deployment_destination_information.ApplicationDestination contains deployment destination information(
                        name = '0', 
                        namespace = '0', 
                        server = '0', )
                    ], 
                namespace_resource_blacklist = [
                    argocd_client.models.group_kind_specifies_a_group_and_a_kind,_but_does_not_force_a_version/__this_is_useful_for_identifying
concepts_during_lookup_stages_without_having_partially_valid_types.GroupKind specifies a Group and a Kind, but does not force a version.  This is useful for identifying
concepts during lookup stages without having partially valid types(
                        group = '0', 
                        kind = '0', )
                    ], 
                namespace_resource_whitelist = [
                    argocd_client.models.group_kind_specifies_a_group_and_a_kind,_but_does_not_force_a_version/__this_is_useful_for_identifying
concepts_during_lookup_stages_without_having_partially_valid_types.GroupKind specifies a Group and a Kind, but does not force a version.  This is useful for identifying
concepts during lookup stages without having partially valid types(
                        group = '0', 
                        kind = '0', )
                    ], 
                orphaned_resources = argocd_client.models.orphaned_resources_monitor_settings_holds_settings_of_orphaned_resources_monitoring.OrphanedResourcesMonitorSettings holds settings of orphaned resources monitoring(
                    ignore = [
                        argocd_client.models.v1alpha1_orphaned_resource_key.v1alpha1OrphanedResourceKey(
                            group = '0', 
                            kind = '0', 
                            name = '0', )
                        ], 
                    warn = True, ), 
                roles = [
                    argocd_client.models.project_role_represents_a_role_that_has_access_to_a_project.ProjectRole represents a role that has access to a project(
                        description = '0', 
                        groups = [
                            '0'
                            ], 
                        jwt_tokens = [
                            argocd_client.models.jwt_token_holds_the_issued_at_and_expires_at_values_of_a_token.JWTToken holds the issuedAt and expiresAt values of a token(
                                exp = '0', 
                                iat = '0', 
                                id = '0', )
                            ], 
                        name = '0', 
                        policies = [
                            '0'
                            ], )
                    ], 
                signature_keys = [
                    argocd_client.models.signature_key_is_the_specification_of_a_key_required_to_verify_commit_signatures_with.SignatureKey is the specification of a key required to verify commit signatures with(
                        key_id = '0', )
                    ], 
                source_repos = [
                    '0'
                    ], 
                sync_windows = [
                    argocd_client.models.sync_window_contains_the_kind,_time,_duration_and_attributes_that_are_used_to_assign_the_sync_windows_to_apps.SyncWindow contains the kind, time, duration and attributes that are used to assign the syncWindows to apps(
                        applications = [
                            '0'
                            ], 
                        clusters = [
                            '0'
                            ], 
                        duration = '0', 
                        kind = '0', 
                        manual_sync = True, 
                        namespaces = [
                            '0'
                            ], 
                        schedule = '0', )
                    ]
            )
        else :
            return V1alpha1AppProjectSpec(
        )

    def testV1alpha1AppProjectSpec(self):
        """Test V1alpha1AppProjectSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
