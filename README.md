# argocd-client
Description of all APIs

- API version: version not set
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/globocom/argocd-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/globocom/argocd-client.git`)

Then import the package:
```python
import argocd_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import argocd_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
import argocd_client
from argocd_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = argocd_client.Configuration(
    host = "http://localhost"
)



# Enter a context with an instance of the API client
with argocd_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = argocd_client.AccountServiceApi(api_client)
    resource = 'resource_example' # str | 
action = 'action_example' # str | 
subresource = 'subresource_example' # str | 

    try:
        api_response = api_instance.can_i(resource, action, subresource)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountServiceApi->can_i: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountServiceApi* | [**can_i**](docs/AccountServiceApi.md#can_i) | **GET** /api/v1/account/can-i/{resource}/{action}/{subresource} | 
*AccountServiceApi* | [**create_token_mixin10**](docs/AccountServiceApi.md#create_token_mixin10) | **POST** /api/v1/account/{name}/token | 
*AccountServiceApi* | [**delete_token_mixin10**](docs/AccountServiceApi.md#delete_token_mixin10) | **DELETE** /api/v1/account/{name}/token/{id} | 
*AccountServiceApi* | [**get_account**](docs/AccountServiceApi.md#get_account) | **GET** /api/v1/account/{name} | 
*AccountServiceApi* | [**list_accounts**](docs/AccountServiceApi.md#list_accounts) | **GET** /api/v1/account | 
*AccountServiceApi* | [**update_password**](docs/AccountServiceApi.md#update_password) | **PUT** /api/v1/account/password | UpdatePassword updates an account&#39;s password to a new value
*ApplicationServiceApi* | [**create_mixin9**](docs/ApplicationServiceApi.md#create_mixin9) | **POST** /api/v1/applications | Create creates an application
*ApplicationServiceApi* | [**delete_mixin9**](docs/ApplicationServiceApi.md#delete_mixin9) | **DELETE** /api/v1/applications/{name} | Delete deletes an application
*ApplicationServiceApi* | [**delete_resource**](docs/ApplicationServiceApi.md#delete_resource) | **DELETE** /api/v1/applications/{name}/resource | DeleteResource deletes a single application resource
*ApplicationServiceApi* | [**get_application_sync_windows**](docs/ApplicationServiceApi.md#get_application_sync_windows) | **GET** /api/v1/applications/{name}/syncwindows | Get returns an application by name
*ApplicationServiceApi* | [**get_manifests**](docs/ApplicationServiceApi.md#get_manifests) | **GET** /api/v1/applications/{name}/manifests | GetManifests returns application manifests
*ApplicationServiceApi* | [**get_mixin9**](docs/ApplicationServiceApi.md#get_mixin9) | **GET** /api/v1/applications/{name} | Get returns an application by name
*ApplicationServiceApi* | [**get_resource**](docs/ApplicationServiceApi.md#get_resource) | **GET** /api/v1/applications/{name}/resource | GetResource returns single application resource
*ApplicationServiceApi* | [**list_mixin9**](docs/ApplicationServiceApi.md#list_mixin9) | **GET** /api/v1/applications | List returns list of applications
*ApplicationServiceApi* | [**list_resource_actions**](docs/ApplicationServiceApi.md#list_resource_actions) | **GET** /api/v1/applications/{name}/resource/actions | 
*ApplicationServiceApi* | [**list_resource_events**](docs/ApplicationServiceApi.md#list_resource_events) | **GET** /api/v1/applications/{name}/events | ListResourceEvents returns a list of event resources
*ApplicationServiceApi* | [**managed_resources**](docs/ApplicationServiceApi.md#managed_resources) | **GET** /api/v1/applications/{applicationName}/managed-resources | 
*ApplicationServiceApi* | [**patch**](docs/ApplicationServiceApi.md#patch) | **PATCH** /api/v1/applications/{name} | Patch patch an application
*ApplicationServiceApi* | [**patch_resource**](docs/ApplicationServiceApi.md#patch_resource) | **POST** /api/v1/applications/{name}/resource | PatchResource patch single application resource
*ApplicationServiceApi* | [**pod_logs**](docs/ApplicationServiceApi.md#pod_logs) | **GET** /api/v1/applications/{name}/pods/{podName}/logs | PodLogs returns stream of log entries for the specified pod. Pod
*ApplicationServiceApi* | [**resource_tree**](docs/ApplicationServiceApi.md#resource_tree) | **GET** /api/v1/applications/{applicationName}/resource-tree | 
*ApplicationServiceApi* | [**revision_metadata**](docs/ApplicationServiceApi.md#revision_metadata) | **GET** /api/v1/applications/{name}/revisions/{revision}/metadata | Get the meta-data (author, date, tags, message) for a specific revision of the application
*ApplicationServiceApi* | [**rollback**](docs/ApplicationServiceApi.md#rollback) | **POST** /api/v1/applications/{name}/rollback | Rollback syncs an application to its target state
*ApplicationServiceApi* | [**run_resource_action**](docs/ApplicationServiceApi.md#run_resource_action) | **POST** /api/v1/applications/{name}/resource/actions | 
*ApplicationServiceApi* | [**sync**](docs/ApplicationServiceApi.md#sync) | **POST** /api/v1/applications/{name}/sync | Sync syncs an application to its target state
*ApplicationServiceApi* | [**terminate_operation**](docs/ApplicationServiceApi.md#terminate_operation) | **DELETE** /api/v1/applications/{name}/operation | TerminateOperation terminates the currently running operation
*ApplicationServiceApi* | [**update_mixin9**](docs/ApplicationServiceApi.md#update_mixin9) | **PUT** /api/v1/applications/{application.metadata.name} | Update updates an application
*ApplicationServiceApi* | [**update_spec**](docs/ApplicationServiceApi.md#update_spec) | **PUT** /api/v1/applications/{name}/spec | UpdateSpec updates an application spec
*ApplicationServiceApi* | [**watch**](docs/ApplicationServiceApi.md#watch) | **GET** /api/v1/stream/applications | Watch returns stream of application change events.
*CertificateServiceApi* | [**create_certificate**](docs/CertificateServiceApi.md#create_certificate) | **POST** /api/v1/certificates | Creates repository certificates on the server
*CertificateServiceApi* | [**delete_certificate**](docs/CertificateServiceApi.md#delete_certificate) | **DELETE** /api/v1/certificates | Delete the certificates that match the RepositoryCertificateQuery
*CertificateServiceApi* | [**list_certificates**](docs/CertificateServiceApi.md#list_certificates) | **GET** /api/v1/certificates | List all available repository certificates
*ClusterServiceApi* | [**create**](docs/ClusterServiceApi.md#create) | **POST** /api/v1/clusters | Create creates a cluster
*ClusterServiceApi* | [**delete**](docs/ClusterServiceApi.md#delete) | **DELETE** /api/v1/clusters/{server} | Delete deletes a cluster
*ClusterServiceApi* | [**get_mixin2**](docs/ClusterServiceApi.md#get_mixin2) | **GET** /api/v1/clusters/{server} | Get returns a cluster by server address
*ClusterServiceApi* | [**invalidate_cache**](docs/ClusterServiceApi.md#invalidate_cache) | **POST** /api/v1/clusters/{server}/invalidate-cache | InvalidateCache invalidates cluster cache
*ClusterServiceApi* | [**list**](docs/ClusterServiceApi.md#list) | **GET** /api/v1/clusters | List returns list of clusters
*ClusterServiceApi* | [**rotate_auth**](docs/ClusterServiceApi.md#rotate_auth) | **POST** /api/v1/clusters/{server}/rotate-auth | RotateAuth rotates the bearer token used for a cluster
*ClusterServiceApi* | [**update**](docs/ClusterServiceApi.md#update) | **PUT** /api/v1/clusters/{cluster.server} | Update updates a cluster
*GPGKeyServiceApi* | [**create_mixin7**](docs/GPGKeyServiceApi.md#create_mixin7) | **POST** /api/v1/gpgkeys | Create one or more GPG public keys in the server&#39;s configuration
*GPGKeyServiceApi* | [**delete_mixin7**](docs/GPGKeyServiceApi.md#delete_mixin7) | **DELETE** /api/v1/gpgkeys | Delete specified GPG public key from the server&#39;s configuration
*GPGKeyServiceApi* | [**get_mixin7**](docs/GPGKeyServiceApi.md#get_mixin7) | **GET** /api/v1/gpgkeys/{keyID} | Get information about specified GPG public key from the server
*GPGKeyServiceApi* | [**list_mixin7**](docs/GPGKeyServiceApi.md#list_mixin7) | **GET** /api/v1/gpgkeys | List all available repository certificates
*ProjectServiceApi* | [**create_mixin6**](docs/ProjectServiceApi.md#create_mixin6) | **POST** /api/v1/projects | Create a new project.
*ProjectServiceApi* | [**create_token**](docs/ProjectServiceApi.md#create_token) | **POST** /api/v1/projects/{project}/roles/{role}/token | Create a new project token.
*ProjectServiceApi* | [**delete_mixin6**](docs/ProjectServiceApi.md#delete_mixin6) | **DELETE** /api/v1/projects/{name} | Delete deletes a project
*ProjectServiceApi* | [**delete_token**](docs/ProjectServiceApi.md#delete_token) | **DELETE** /api/v1/projects/{project}/roles/{role}/token/{iat} | Delete a new project token.
*ProjectServiceApi* | [**get_mixin6**](docs/ProjectServiceApi.md#get_mixin6) | **GET** /api/v1/projects/{name} | Get returns a project by name
*ProjectServiceApi* | [**get_sync_windows_state**](docs/ProjectServiceApi.md#get_sync_windows_state) | **GET** /api/v1/projects/{name}/syncwindows | GetSchedulesState returns true if there are any active sync syncWindows
*ProjectServiceApi* | [**list_events**](docs/ProjectServiceApi.md#list_events) | **GET** /api/v1/projects/{name}/events | ListEvents returns a list of project events
*ProjectServiceApi* | [**list_mixin6**](docs/ProjectServiceApi.md#list_mixin6) | **GET** /api/v1/projects | List returns list of projects
*ProjectServiceApi* | [**update_mixin6**](docs/ProjectServiceApi.md#update_mixin6) | **PUT** /api/v1/projects/{project.metadata.name} | Update updates a project
*RepoCredsServiceApi* | [**create_repository_credentials**](docs/RepoCredsServiceApi.md#create_repository_credentials) | **POST** /api/v1/repocreds | CreateRepositoryCredentials creates a new repository credential set
*RepoCredsServiceApi* | [**delete_repository_credentials**](docs/RepoCredsServiceApi.md#delete_repository_credentials) | **DELETE** /api/v1/repocreds/{url} | DeleteRepositoryCredentials deletes a repository credential set from the configuration
*RepoCredsServiceApi* | [**list_repository_credentials**](docs/RepoCredsServiceApi.md#list_repository_credentials) | **GET** /api/v1/repocreds | ListRepositoryCredentials gets a list of all configured repository credential sets
*RepoCredsServiceApi* | [**update_repository_credentials**](docs/RepoCredsServiceApi.md#update_repository_credentials) | **PUT** /api/v1/repocreds/{creds.url} | UpdateRepositoryCredentials updates a repository credential set
*RepositoryServiceApi* | [**create_repository**](docs/RepositoryServiceApi.md#create_repository) | **POST** /api/v1/repositories | CreateRepository creates a new repository configuration
*RepositoryServiceApi* | [**delete_repository**](docs/RepositoryServiceApi.md#delete_repository) | **DELETE** /api/v1/repositories/{repo} | DeleteRepository deletes a repository from the configuration
*RepositoryServiceApi* | [**get_app_details**](docs/RepositoryServiceApi.md#get_app_details) | **POST** /api/v1/repositories/{source.repoURL}/appdetails | GetAppDetails returns application details by given path
*RepositoryServiceApi* | [**get_helm_charts**](docs/RepositoryServiceApi.md#get_helm_charts) | **GET** /api/v1/repositories/{repo}/helmcharts | 
*RepositoryServiceApi* | [**get_mixin3**](docs/RepositoryServiceApi.md#get_mixin3) | **GET** /api/v1/repositories/{repo} | Get returns a repository or its credentials
*RepositoryServiceApi* | [**list_apps**](docs/RepositoryServiceApi.md#list_apps) | **GET** /api/v1/repositories/{repo}/apps | ListApps returns list of apps in the repo
*RepositoryServiceApi* | [**list_repositories**](docs/RepositoryServiceApi.md#list_repositories) | **GET** /api/v1/repositories | ListRepositories gets a list of all configured repositories
*RepositoryServiceApi* | [**update_repository**](docs/RepositoryServiceApi.md#update_repository) | **PUT** /api/v1/repositories/{repo.repo} | UpdateRepository updates a repository configuration
*RepositoryServiceApi* | [**validate_access**](docs/RepositoryServiceApi.md#validate_access) | **POST** /api/v1/repositories/{repo}/validate | ValidateAccess validates access to a repository with given parameters
*SessionServiceApi* | [**create_mixin11**](docs/SessionServiceApi.md#create_mixin11) | **POST** /api/v1/session | Create a new JWT for authentication and set a cookie if using HTTP.
*SessionServiceApi* | [**delete_mixin11**](docs/SessionServiceApi.md#delete_mixin11) | **DELETE** /api/v1/session | Delete an existing JWT cookie if using HTTP.
*SessionServiceApi* | [**get_user_info**](docs/SessionServiceApi.md#get_user_info) | **GET** /api/v1/session/userinfo | Get the current user&#39;s info
*SettingsServiceApi* | [**get**](docs/SettingsServiceApi.md#get) | **GET** /api/v1/settings | Get returns Argo CD settings
*VersionServiceApi* | [**version**](docs/VersionServiceApi.md#version) | **GET** /api/version | Version returns version information of the API server


## Documentation For Models

 - [AccountAccount](docs/AccountAccount.md)
 - [AccountAccountsList](docs/AccountAccountsList.md)
 - [AccountCanIResponse](docs/AccountCanIResponse.md)
 - [AccountCreateTokenRequest](docs/AccountCreateTokenRequest.md)
 - [AccountCreateTokenResponse](docs/AccountCreateTokenResponse.md)
 - [AccountToken](docs/AccountToken.md)
 - [AccountUpdatePasswordRequest](docs/AccountUpdatePasswordRequest.md)
 - [ApplicationApplicationPatchRequest](docs/ApplicationApplicationPatchRequest.md)
 - [ApplicationApplicationResourceResponse](docs/ApplicationApplicationResourceResponse.md)
 - [ApplicationApplicationRollbackRequest](docs/ApplicationApplicationRollbackRequest.md)
 - [ApplicationApplicationSyncRequest](docs/ApplicationApplicationSyncRequest.md)
 - [ApplicationApplicationSyncWindow](docs/ApplicationApplicationSyncWindow.md)
 - [ApplicationApplicationSyncWindowsResponse](docs/ApplicationApplicationSyncWindowsResponse.md)
 - [ApplicationLogEntry](docs/ApplicationLogEntry.md)
 - [ApplicationManagedResourcesResponse](docs/ApplicationManagedResourcesResponse.md)
 - [ApplicationResourceActionsListResponse](docs/ApplicationResourceActionsListResponse.md)
 - [ClusterConnector](docs/ClusterConnector.md)
 - [ClusterDexConfig](docs/ClusterDexConfig.md)
 - [ClusterGoogleAnalyticsConfig](docs/ClusterGoogleAnalyticsConfig.md)
 - [ClusterHelp](docs/ClusterHelp.md)
 - [ClusterOIDCConfig](docs/ClusterOIDCConfig.md)
 - [ClusterPlugin](docs/ClusterPlugin.md)
 - [ClusterSettings](docs/ClusterSettings.md)
 - [GpgkeyGnuPGPublicKeyCreateResponse](docs/GpgkeyGnuPGPublicKeyCreateResponse.md)
 - [OidcClaim](docs/OidcClaim.md)
 - [ProjectProjectCreateRequest](docs/ProjectProjectCreateRequest.md)
 - [ProjectProjectTokenCreateRequest](docs/ProjectProjectTokenCreateRequest.md)
 - [ProjectProjectTokenResponse](docs/ProjectProjectTokenResponse.md)
 - [ProjectProjectUpdateRequest](docs/ProjectProjectUpdateRequest.md)
 - [ProjectSyncWindowsResponse](docs/ProjectSyncWindowsResponse.md)
 - [ProtobufAny](docs/ProtobufAny.md)
 - [RepositoryAppInfo](docs/RepositoryAppInfo.md)
 - [RepositoryHelmAppSpec](docs/RepositoryHelmAppSpec.md)
 - [RepositoryHelmChart](docs/RepositoryHelmChart.md)
 - [RepositoryHelmChartsResponse](docs/RepositoryHelmChartsResponse.md)
 - [RepositoryKsonnetAppSpec](docs/RepositoryKsonnetAppSpec.md)
 - [RepositoryKsonnetEnvironment](docs/RepositoryKsonnetEnvironment.md)
 - [RepositoryKsonnetEnvironmentDestination](docs/RepositoryKsonnetEnvironmentDestination.md)
 - [RepositoryKustomizeAppSpec](docs/RepositoryKustomizeAppSpec.md)
 - [RepositoryManifestResponse](docs/RepositoryManifestResponse.md)
 - [RepositoryRepoAppDetailsQuery](docs/RepositoryRepoAppDetailsQuery.md)
 - [RepositoryRepoAppDetailsResponse](docs/RepositoryRepoAppDetailsResponse.md)
 - [RepositoryRepoAppsResponse](docs/RepositoryRepoAppsResponse.md)
 - [RuntimeStreamError](docs/RuntimeStreamError.md)
 - [SessionGetUserInfoResponse](docs/SessionGetUserInfoResponse.md)
 - [SessionSessionCreateRequest](docs/SessionSessionCreateRequest.md)
 - [SessionSessionResponse](docs/SessionSessionResponse.md)
 - [V1Event](docs/V1Event.md)
 - [V1EventList](docs/V1EventList.md)
 - [V1EventSeries](docs/V1EventSeries.md)
 - [V1EventSource](docs/V1EventSource.md)
 - [V1FieldsV1](docs/V1FieldsV1.md)
 - [V1GroupKind](docs/V1GroupKind.md)
 - [V1ListMeta](docs/V1ListMeta.md)
 - [V1LoadBalancerIngress](docs/V1LoadBalancerIngress.md)
 - [V1ManagedFieldsEntry](docs/V1ManagedFieldsEntry.md)
 - [V1MicroTime](docs/V1MicroTime.md)
 - [V1ObjectMeta](docs/V1ObjectMeta.md)
 - [V1ObjectReference](docs/V1ObjectReference.md)
 - [V1OwnerReference](docs/V1OwnerReference.md)
 - [V1Time](docs/V1Time.md)
 - [V1alpha1AWSAuthConfig](docs/V1alpha1AWSAuthConfig.md)
 - [V1alpha1AppProject](docs/V1alpha1AppProject.md)
 - [V1alpha1AppProjectList](docs/V1alpha1AppProjectList.md)
 - [V1alpha1AppProjectSpec](docs/V1alpha1AppProjectSpec.md)
 - [V1alpha1AppProjectStatus](docs/V1alpha1AppProjectStatus.md)
 - [V1alpha1Application](docs/V1alpha1Application.md)
 - [V1alpha1ApplicationCondition](docs/V1alpha1ApplicationCondition.md)
 - [V1alpha1ApplicationDestination](docs/V1alpha1ApplicationDestination.md)
 - [V1alpha1ApplicationList](docs/V1alpha1ApplicationList.md)
 - [V1alpha1ApplicationSource](docs/V1alpha1ApplicationSource.md)
 - [V1alpha1ApplicationSourceDirectory](docs/V1alpha1ApplicationSourceDirectory.md)
 - [V1alpha1ApplicationSourceHelm](docs/V1alpha1ApplicationSourceHelm.md)
 - [V1alpha1ApplicationSourceJsonnet](docs/V1alpha1ApplicationSourceJsonnet.md)
 - [V1alpha1ApplicationSourceKsonnet](docs/V1alpha1ApplicationSourceKsonnet.md)
 - [V1alpha1ApplicationSourceKustomize](docs/V1alpha1ApplicationSourceKustomize.md)
 - [V1alpha1ApplicationSourcePlugin](docs/V1alpha1ApplicationSourcePlugin.md)
 - [V1alpha1ApplicationSpec](docs/V1alpha1ApplicationSpec.md)
 - [V1alpha1ApplicationStatus](docs/V1alpha1ApplicationStatus.md)
 - [V1alpha1ApplicationSummary](docs/V1alpha1ApplicationSummary.md)
 - [V1alpha1ApplicationTree](docs/V1alpha1ApplicationTree.md)
 - [V1alpha1ApplicationWatchEvent](docs/V1alpha1ApplicationWatchEvent.md)
 - [V1alpha1Backoff](docs/V1alpha1Backoff.md)
 - [V1alpha1Cluster](docs/V1alpha1Cluster.md)
 - [V1alpha1ClusterCacheInfo](docs/V1alpha1ClusterCacheInfo.md)
 - [V1alpha1ClusterConfig](docs/V1alpha1ClusterConfig.md)
 - [V1alpha1ClusterInfo](docs/V1alpha1ClusterInfo.md)
 - [V1alpha1ClusterList](docs/V1alpha1ClusterList.md)
 - [V1alpha1Command](docs/V1alpha1Command.md)
 - [V1alpha1ComparedTo](docs/V1alpha1ComparedTo.md)
 - [V1alpha1ConfigManagementPlugin](docs/V1alpha1ConfigManagementPlugin.md)
 - [V1alpha1ConnectionState](docs/V1alpha1ConnectionState.md)
 - [V1alpha1EnvEntry](docs/V1alpha1EnvEntry.md)
 - [V1alpha1GnuPGPublicKey](docs/V1alpha1GnuPGPublicKey.md)
 - [V1alpha1GnuPGPublicKeyList](docs/V1alpha1GnuPGPublicKeyList.md)
 - [V1alpha1HealthStatus](docs/V1alpha1HealthStatus.md)
 - [V1alpha1HelmFileParameter](docs/V1alpha1HelmFileParameter.md)
 - [V1alpha1HelmParameter](docs/V1alpha1HelmParameter.md)
 - [V1alpha1Info](docs/V1alpha1Info.md)
 - [V1alpha1InfoItem](docs/V1alpha1InfoItem.md)
 - [V1alpha1JWTToken](docs/V1alpha1JWTToken.md)
 - [V1alpha1JWTTokens](docs/V1alpha1JWTTokens.md)
 - [V1alpha1JsonnetVar](docs/V1alpha1JsonnetVar.md)
 - [V1alpha1KnownTypeField](docs/V1alpha1KnownTypeField.md)
 - [V1alpha1KsonnetParameter](docs/V1alpha1KsonnetParameter.md)
 - [V1alpha1KustomizeOptions](docs/V1alpha1KustomizeOptions.md)
 - [V1alpha1Operation](docs/V1alpha1Operation.md)
 - [V1alpha1OperationInitiator](docs/V1alpha1OperationInitiator.md)
 - [V1alpha1OperationState](docs/V1alpha1OperationState.md)
 - [V1alpha1OrphanedResourceKey](docs/V1alpha1OrphanedResourceKey.md)
 - [V1alpha1OrphanedResourcesMonitorSettings](docs/V1alpha1OrphanedResourcesMonitorSettings.md)
 - [V1alpha1OverrideIgnoreDiff](docs/V1alpha1OverrideIgnoreDiff.md)
 - [V1alpha1ProjectRole](docs/V1alpha1ProjectRole.md)
 - [V1alpha1RepoCreds](docs/V1alpha1RepoCreds.md)
 - [V1alpha1RepoCredsList](docs/V1alpha1RepoCredsList.md)
 - [V1alpha1Repository](docs/V1alpha1Repository.md)
 - [V1alpha1RepositoryCertificate](docs/V1alpha1RepositoryCertificate.md)
 - [V1alpha1RepositoryCertificateList](docs/V1alpha1RepositoryCertificateList.md)
 - [V1alpha1RepositoryList](docs/V1alpha1RepositoryList.md)
 - [V1alpha1ResourceAction](docs/V1alpha1ResourceAction.md)
 - [V1alpha1ResourceActionParam](docs/V1alpha1ResourceActionParam.md)
 - [V1alpha1ResourceDiff](docs/V1alpha1ResourceDiff.md)
 - [V1alpha1ResourceIgnoreDifferences](docs/V1alpha1ResourceIgnoreDifferences.md)
 - [V1alpha1ResourceNetworkingInfo](docs/V1alpha1ResourceNetworkingInfo.md)
 - [V1alpha1ResourceNode](docs/V1alpha1ResourceNode.md)
 - [V1alpha1ResourceOverride](docs/V1alpha1ResourceOverride.md)
 - [V1alpha1ResourceRef](docs/V1alpha1ResourceRef.md)
 - [V1alpha1ResourceResult](docs/V1alpha1ResourceResult.md)
 - [V1alpha1ResourceStatus](docs/V1alpha1ResourceStatus.md)
 - [V1alpha1RetryStrategy](docs/V1alpha1RetryStrategy.md)
 - [V1alpha1RevisionHistory](docs/V1alpha1RevisionHistory.md)
 - [V1alpha1RevisionMetadata](docs/V1alpha1RevisionMetadata.md)
 - [V1alpha1SignatureKey](docs/V1alpha1SignatureKey.md)
 - [V1alpha1SyncOperation](docs/V1alpha1SyncOperation.md)
 - [V1alpha1SyncOperationResource](docs/V1alpha1SyncOperationResource.md)
 - [V1alpha1SyncOperationResult](docs/V1alpha1SyncOperationResult.md)
 - [V1alpha1SyncPolicy](docs/V1alpha1SyncPolicy.md)
 - [V1alpha1SyncPolicyAutomated](docs/V1alpha1SyncPolicyAutomated.md)
 - [V1alpha1SyncStatus](docs/V1alpha1SyncStatus.md)
 - [V1alpha1SyncStrategy](docs/V1alpha1SyncStrategy.md)
 - [V1alpha1SyncStrategyApply](docs/V1alpha1SyncStrategyApply.md)
 - [V1alpha1SyncStrategyHook](docs/V1alpha1SyncStrategyHook.md)
 - [V1alpha1SyncWindow](docs/V1alpha1SyncWindow.md)
 - [V1alpha1TLSClientConfig](docs/V1alpha1TLSClientConfig.md)
 - [VersionVersionMessage](docs/VersionVersionMessage.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




