# argocd_client.ApplicationServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mixin9**](ApplicationServiceApi.md#create_mixin9) | **POST** /api/v1/applications | Create creates an application
[**delete_mixin9**](ApplicationServiceApi.md#delete_mixin9) | **DELETE** /api/v1/applications/{name} | Delete deletes an application
[**delete_resource**](ApplicationServiceApi.md#delete_resource) | **DELETE** /api/v1/applications/{name}/resource | DeleteResource deletes a single application resource
[**get_application_sync_windows**](ApplicationServiceApi.md#get_application_sync_windows) | **GET** /api/v1/applications/{name}/syncwindows | Get returns an application by name
[**get_manifests**](ApplicationServiceApi.md#get_manifests) | **GET** /api/v1/applications/{name}/manifests | GetManifests returns application manifests
[**get_mixin9**](ApplicationServiceApi.md#get_mixin9) | **GET** /api/v1/applications/{name} | Get returns an application by name
[**get_resource**](ApplicationServiceApi.md#get_resource) | **GET** /api/v1/applications/{name}/resource | GetResource returns single application resource
[**list_mixin9**](ApplicationServiceApi.md#list_mixin9) | **GET** /api/v1/applications | List returns list of applications
[**list_resource_actions**](ApplicationServiceApi.md#list_resource_actions) | **GET** /api/v1/applications/{name}/resource/actions | 
[**list_resource_events**](ApplicationServiceApi.md#list_resource_events) | **GET** /api/v1/applications/{name}/events | ListResourceEvents returns a list of event resources
[**managed_resources**](ApplicationServiceApi.md#managed_resources) | **GET** /api/v1/applications/{applicationName}/managed-resources | 
[**patch**](ApplicationServiceApi.md#patch) | **PATCH** /api/v1/applications/{name} | Patch patch an application
[**patch_resource**](ApplicationServiceApi.md#patch_resource) | **POST** /api/v1/applications/{name}/resource | PatchResource patch single application resource
[**pod_logs**](ApplicationServiceApi.md#pod_logs) | **GET** /api/v1/applications/{name}/pods/{podName}/logs | PodLogs returns stream of log entries for the specified pod. Pod
[**resource_tree**](ApplicationServiceApi.md#resource_tree) | **GET** /api/v1/applications/{applicationName}/resource-tree | 
[**revision_metadata**](ApplicationServiceApi.md#revision_metadata) | **GET** /api/v1/applications/{name}/revisions/{revision}/metadata | Get the meta-data (author, date, tags, message) for a specific revision of the application
[**rollback**](ApplicationServiceApi.md#rollback) | **POST** /api/v1/applications/{name}/rollback | Rollback syncs an application to its target state
[**run_resource_action**](ApplicationServiceApi.md#run_resource_action) | **POST** /api/v1/applications/{name}/resource/actions | 
[**sync**](ApplicationServiceApi.md#sync) | **POST** /api/v1/applications/{name}/sync | Sync syncs an application to its target state
[**terminate_operation**](ApplicationServiceApi.md#terminate_operation) | **DELETE** /api/v1/applications/{name}/operation | TerminateOperation terminates the currently running operation
[**update_mixin9**](ApplicationServiceApi.md#update_mixin9) | **PUT** /api/v1/applications/{application.metadata.name} | Update updates an application
[**update_spec**](ApplicationServiceApi.md#update_spec) | **PUT** /api/v1/applications/{name}/spec | UpdateSpec updates an application spec
[**watch**](ApplicationServiceApi.md#watch) | **GET** /api/v1/stream/applications | Watch returns stream of application change events.


# **create_mixin9**
> V1alpha1Application create_mixin9(body)

Create creates an application

### Example

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
with argocd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = argocd_client.ApplicationServiceApi(api_client)
    body = argocd_client.V1alpha1Application() # V1alpha1Application | 

    try:
        # Create creates an application
        api_response = api_instance.create_mixin9(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationServiceApi->create_mixin9: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alpha1Application**](V1alpha1Application.md)|  | 

### Return type

[**V1alpha1Application**](V1alpha1Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mixin9**
> object delete_mixin9(name, cascade=cascade)

Delete deletes an application

### Example

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
with argocd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = argocd_client.ApplicationServiceApi(api_client)
    name = 'name_example' # str | 
cascade = True # bool |  (optional)

    try:
        # Delete deletes an application
        api_response = api_instance.delete_mixin9(name, cascade=cascade)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationServiceApi->delete_mixin9: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **cascade** | **bool**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_resource**
> object delete_resource(name, namespace=namespace, resource_name=resource_name, version=version, group=group, kind=kind, force=force)

DeleteResource deletes a single application resource

### Example

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
with argocd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = argocd_client.ApplicationServiceApi(api_client)
    name = 'name_example' # str | 
namespace = 'namespace_example' # str |  (optional)
resource_name = 'resource_name_example' # str |  (optional)
version = 'version_example' # str |  (optional)
group = 'group_example' # str |  (optional)
kind = 'kind_example' # str |  (optional)
force = True # bool |  (optional)

    try:
        # DeleteResource deletes a single application resource
        api_response = api_instance.delete_resource(name, namespace=namespace, resource_name=resource_name, version=version, group=group, kind=kind, force=force)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationServiceApi->delete_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **namespace** | **str**|  | [optional] 
 **resource_name** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 
 **group** | **str**|  | [optional] 
 **kind** | **str**|  | [optional] 
 **force** | **bool**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_sync_windows**
> ApplicationApplicationSyncWindowsResponse get_application_sync_windows(name)

Get returns an application by name

### Example

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
with argocd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = argocd_client.ApplicationServiceApi(api_client)
    name = 'name_example' # str | 

    try:
        # Get returns an application by name
        api_response = api_instance.get_application_sync_windows(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationServiceApi->get_application_sync_windows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**ApplicationApplicationSyncWindowsResponse**](ApplicationApplicationSyncWindowsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manifests**
> RepositoryManifestResponse get_manifests(name, revision=revision)

GetManifests returns application manifests

### Example

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
with argocd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = argocd_client.ApplicationServiceApi(api_client)
    name = 'name_example' # str | 
revision = 'revision_example' # str |  (optional)

    try:
        # GetManifests returns application manifests
        api_response = api_instance.get_manifests(name, revision=revision)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationServiceApi->get_manifests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **revision** | **str**|  | [optional] 

### Return type

[**RepositoryManifestResponse**](RepositoryManifestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mixin9**
> V1alpha1Application get_mixin9(name, refresh=refresh, project=project, resource_version=resource_version, selector=selector)

Get returns an application by name

### Example

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
with argocd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = argocd_client.ApplicationServiceApi(api_client)
    name = 'name_example' # str | the application's name
refresh = 'refresh_example' # str | forces application reconciliation if set to true. (optional)
project = ['project_example'] # list[str] | the project names to restrict returned list applications. (optional)
resource_version = 'resource_version_example' # str | when specified with a watch call, shows changes that occur after that particular version of a resource. (optional)
selector = 'selector_example' # str | the selector to to restrict returned list to applications only with matched labels. (optional)

    try:
        # Get returns an application by name
        api_response = api_instance.get_mixin9(name, refresh=refresh, project=project, resource_version=resource_version, selector=selector)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationServiceApi->get_mixin9: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| the application&#39;s name | 
 **refresh** | **str**| forces application reconciliation if set to true. | [optional] 
 **project** | [**list[str]**](str.md)| the project names to restrict returned list applications. | [optional] 
 **resource_version** | **str**| when specified with a watch call, shows changes that occur after that particular version of a resource. | [optional] 
 **selector** | **str**| the selector to to restrict returned list to applications only with matched labels. | [optional] 

### Return type

[**V1alpha1Application**](V1alpha1Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource**
> ApplicationApplicationResourceResponse get_resource(name, namespace=namespace, resource_name=resource_name, version=version, group=group, kind=kind)

GetResource returns single application resource

### Example

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
with argocd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = argocd_client.ApplicationServiceApi(api_client)
    name = 'name_example' # str | 
namespace = 'namespace_example' # str |  (optional)
resource_name = 'resource_name_example' # str |  (optional)
version = 'version_example' # str |  (optional)
group = 'group_example' # str |  (optional)
kind = 'kind_example' # str |  (optional)

    try:
        # GetResource returns single application resource
        api_response = api_instance.get_resource(name, namespace=namespace, resource_name=resource_name, version=version, group=group, kind=kind)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationServiceApi->get_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **namespace** | **str**|  | [optional] 
 **resource_name** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 
 **group** | **str**|  | [optional] 
 **kind** | **str**|  | [optional] 

### Return type

[**ApplicationApplicationResourceResponse**](ApplicationApplicationResourceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mixin9**
> V1alpha1ApplicationList list_mixin9(name=name, refresh=refresh, project=project, resource_version=resource_version, selector=selector)

List returns list of applications

### Example

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
with argocd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = argocd_client.ApplicationServiceApi(api_client)
    name = 'name_example' # str | the application's name. (optional)
refresh = 'refresh_example' # str | forces application reconciliation if set to true. (optional)
project = ['project_example'] # list[str] | the project names to restrict returned list applications. (optional)
resource_version = 'resource_version_example' # str | when specified with a watch call, shows changes that occur after that particular version of a resource. (optional)
selector = 'selector_example' # str | the selector to to restrict returned list to applications only with matched labels. (optional)

    try:
        # List returns list of applications
        api_response = api_instance.list_mixin9(name=name, refresh=refresh, project=project, resource_version=resource_version, selector=selector)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationServiceApi->list_mixin9: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| the application&#39;s name. | [optional] 
 **refresh** | **str**| forces application reconciliation if set to true. | [optional] 
 **project** | [**list[str]**](str.md)| the project names to restrict returned list applications. | [optional] 
 **resource_version** | **str**| when specified with a watch call, shows changes that occur after that particular version of a resource. | [optional] 
 **selector** | **str**| the selector to to restrict returned list to applications only with matched labels. | [optional] 

### Return type

[**V1alpha1ApplicationList**](V1alpha1ApplicationList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_resource_actions**
> ApplicationResourceActionsListResponse list_resource_actions(name, namespace=namespace, resource_name=resource_name, version=version, group=group, kind=kind)



### Example

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
with argocd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = argocd_client.ApplicationServiceApi(api_client)
    name = 'name_example' # str | 
namespace = 'namespace_example' # str |  (optional)
resource_name = 'resource_name_example' # str |  (optional)
version = 'version_example' # str |  (optional)
group = 'group_example' # str |  (optional)
kind = 'kind_example' # str |  (optional)

    try:
        api_response = api_instance.list_resource_actions(name, namespace=namespace, resource_name=resource_name, version=version, group=group, kind=kind)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationServiceApi->list_resource_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **namespace** | **str**|  | [optional] 
 **resource_name** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 
 **group** | **str**|  | [optional] 
 **kind** | **str**|  | [optional] 

### Return type

[**ApplicationResourceActionsListResponse**](ApplicationResourceActionsListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_resource_events**
> V1EventList list_resource_events(name, resource_namespace=resource_namespace, resource_name=resource_name, resource_uid=resource_uid)

ListResourceEvents returns a list of event resources

### Example

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
with argocd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = argocd_client.ApplicationServiceApi(api_client)
    name = 'name_example' # str | 
resource_namespace = 'resource_namespace_example' # str |  (optional)
resource_name = 'resource_name_example' # str |  (optional)
resource_uid = 'resource_uid_example' # str |  (optional)

    try:
        # ListResourceEvents returns a list of event resources
        api_response = api_instance.list_resource_events(name, resource_namespace=resource_namespace, resource_name=resource_name, resource_uid=resource_uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationServiceApi->list_resource_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **resource_namespace** | **str**|  | [optional] 
 **resource_name** | **str**|  | [optional] 
 **resource_uid** | **str**|  | [optional] 

### Return type

[**V1EventList**](V1EventList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **managed_resources**
> ApplicationManagedResourcesResponse managed_resources(application_name, namespace=namespace, name=name, version=version, group=group, kind=kind)



### Example

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
with argocd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = argocd_client.ApplicationServiceApi(api_client)
    application_name = 'application_name_example' # str | 
namespace = 'namespace_example' # str |  (optional)
name = 'name_example' # str |  (optional)
version = 'version_example' # str |  (optional)
group = 'group_example' # str |  (optional)
kind = 'kind_example' # str |  (optional)

    try:
        api_response = api_instance.managed_resources(application_name, namespace=namespace, name=name, version=version, group=group, kind=kind)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationServiceApi->managed_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**|  | 
 **namespace** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 
 **group** | **str**|  | [optional] 
 **kind** | **str**|  | [optional] 

### Return type

[**ApplicationManagedResourcesResponse**](ApplicationManagedResourcesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch**
> V1alpha1Application patch(name, body)

Patch patch an application

### Example

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
with argocd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = argocd_client.ApplicationServiceApi(api_client)
    name = 'name_example' # str | 
body = argocd_client.ApplicationApplicationPatchRequest() # ApplicationApplicationPatchRequest | 

    try:
        # Patch patch an application
        api_response = api_instance.patch(name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationServiceApi->patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **body** | [**ApplicationApplicationPatchRequest**](ApplicationApplicationPatchRequest.md)|  | 

### Return type

[**V1alpha1Application**](V1alpha1Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_resource**
> ApplicationApplicationResourceResponse patch_resource(name, body)

PatchResource patch single application resource

### Example

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
with argocd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = argocd_client.ApplicationServiceApi(api_client)
    name = 'name_example' # str | 
body = 'body_example' # str | 

    try:
        # PatchResource patch single application resource
        api_response = api_instance.patch_resource(name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationServiceApi->patch_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **body** | **str**|  | 

### Return type

[**ApplicationApplicationResourceResponse**](ApplicationApplicationResourceResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pod_logs**
> object pod_logs(name, pod_name, namespace=namespace, container=container, since_seconds=since_seconds, since_time_seconds=since_time_seconds, since_time_nanos=since_time_nanos, tail_lines=tail_lines, follow=follow)

PodLogs returns stream of log entries for the specified pod. Pod

### Example

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
with argocd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = argocd_client.ApplicationServiceApi(api_client)
    name = 'name_example' # str | 
pod_name = 'pod_name_example' # str | 
namespace = 'namespace_example' # str |  (optional)
container = 'container_example' # str |  (optional)
since_seconds = 'since_seconds_example' # str |  (optional)
since_time_seconds = 'since_time_seconds_example' # str | Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive. (optional)
since_time_nanos = 56 # int | Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive. This field may be limited in precision depending on context. (optional)
tail_lines = 'tail_lines_example' # str |  (optional)
follow = True # bool |  (optional)

    try:
        # PodLogs returns stream of log entries for the specified pod. Pod
        api_response = api_instance.pod_logs(name, pod_name, namespace=namespace, container=container, since_seconds=since_seconds, since_time_seconds=since_time_seconds, since_time_nanos=since_time_nanos, tail_lines=tail_lines, follow=follow)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationServiceApi->pod_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **pod_name** | **str**|  | 
 **namespace** | **str**|  | [optional] 
 **container** | **str**|  | [optional] 
 **since_seconds** | **str**|  | [optional] 
 **since_time_seconds** | **str**| Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z inclusive. | [optional] 
 **since_time_nanos** | **int**| Non-negative fractions of a second at nanosecond resolution. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be from 0 to 999,999,999 inclusive. This field may be limited in precision depending on context. | [optional] 
 **tail_lines** | **str**|  | [optional] 
 **follow** | **bool**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response.(streaming responses) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_tree**
> V1alpha1ApplicationTree resource_tree(application_name, namespace=namespace, name=name, version=version, group=group, kind=kind)



### Example

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
with argocd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = argocd_client.ApplicationServiceApi(api_client)
    application_name = 'application_name_example' # str | 
namespace = 'namespace_example' # str |  (optional)
name = 'name_example' # str |  (optional)
version = 'version_example' # str |  (optional)
group = 'group_example' # str |  (optional)
kind = 'kind_example' # str |  (optional)

    try:
        api_response = api_instance.resource_tree(application_name, namespace=namespace, name=name, version=version, group=group, kind=kind)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationServiceApi->resource_tree: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**|  | 
 **namespace** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **version** | **str**|  | [optional] 
 **group** | **str**|  | [optional] 
 **kind** | **str**|  | [optional] 

### Return type

[**V1alpha1ApplicationTree**](V1alpha1ApplicationTree.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revision_metadata**
> V1alpha1RevisionMetadata revision_metadata(name, revision)

Get the meta-data (author, date, tags, message) for a specific revision of the application

### Example

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
with argocd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = argocd_client.ApplicationServiceApi(api_client)
    name = 'name_example' # str | the application's name
revision = 'revision_example' # str | the revision of the app

    try:
        # Get the meta-data (author, date, tags, message) for a specific revision of the application
        api_response = api_instance.revision_metadata(name, revision)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationServiceApi->revision_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| the application&#39;s name | 
 **revision** | **str**| the revision of the app | 

### Return type

[**V1alpha1RevisionMetadata**](V1alpha1RevisionMetadata.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rollback**
> V1alpha1Application rollback(name, body)

Rollback syncs an application to its target state

### Example

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
with argocd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = argocd_client.ApplicationServiceApi(api_client)
    name = 'name_example' # str | 
body = argocd_client.ApplicationApplicationRollbackRequest() # ApplicationApplicationRollbackRequest | 

    try:
        # Rollback syncs an application to its target state
        api_response = api_instance.rollback(name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationServiceApi->rollback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **body** | [**ApplicationApplicationRollbackRequest**](ApplicationApplicationRollbackRequest.md)|  | 

### Return type

[**V1alpha1Application**](V1alpha1Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_resource_action**
> object run_resource_action(name, body)



### Example

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
with argocd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = argocd_client.ApplicationServiceApi(api_client)
    name = 'name_example' # str | 
body = 'body_example' # str | 

    try:
        api_response = api_instance.run_resource_action(name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationServiceApi->run_resource_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **body** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync**
> V1alpha1Application sync(name, body)

Sync syncs an application to its target state

### Example

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
with argocd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = argocd_client.ApplicationServiceApi(api_client)
    name = 'name_example' # str | 
body = argocd_client.ApplicationApplicationSyncRequest() # ApplicationApplicationSyncRequest | 

    try:
        # Sync syncs an application to its target state
        api_response = api_instance.sync(name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationServiceApi->sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **body** | [**ApplicationApplicationSyncRequest**](ApplicationApplicationSyncRequest.md)|  | 

### Return type

[**V1alpha1Application**](V1alpha1Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_operation**
> object terminate_operation(name)

TerminateOperation terminates the currently running operation

### Example

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
with argocd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = argocd_client.ApplicationServiceApi(api_client)
    name = 'name_example' # str | 

    try:
        # TerminateOperation terminates the currently running operation
        api_response = api_instance.terminate_operation(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationServiceApi->terminate_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mixin9**
> V1alpha1Application update_mixin9(application_metadata_name, body)

Update updates an application

### Example

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
with argocd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = argocd_client.ApplicationServiceApi(api_client)
    application_metadata_name = 'application_metadata_name_example' # str | Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names +optional
body = argocd_client.V1alpha1Application() # V1alpha1Application | 

    try:
        # Update updates an application
        api_response = api_instance.update_mixin9(application_metadata_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationServiceApi->update_mixin9: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_metadata_name** | **str**| Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names +optional | 
 **body** | [**V1alpha1Application**](V1alpha1Application.md)|  | 

### Return type

[**V1alpha1Application**](V1alpha1Application.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_spec**
> V1alpha1ApplicationSpec update_spec(name, body)

UpdateSpec updates an application spec

### Example

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
with argocd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = argocd_client.ApplicationServiceApi(api_client)
    name = 'name_example' # str | 
body = argocd_client.V1alpha1ApplicationSpec() # V1alpha1ApplicationSpec | 

    try:
        # UpdateSpec updates an application spec
        api_response = api_instance.update_spec(name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationServiceApi->update_spec: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **body** | [**V1alpha1ApplicationSpec**](V1alpha1ApplicationSpec.md)|  | 

### Return type

[**V1alpha1ApplicationSpec**](V1alpha1ApplicationSpec.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **watch**
> object watch(name=name, refresh=refresh, project=project, resource_version=resource_version, selector=selector)

Watch returns stream of application change events.

### Example

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
with argocd_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = argocd_client.ApplicationServiceApi(api_client)
    name = 'name_example' # str | the application's name. (optional)
refresh = 'refresh_example' # str | forces application reconciliation if set to true. (optional)
project = ['project_example'] # list[str] | the project names to restrict returned list applications. (optional)
resource_version = 'resource_version_example' # str | when specified with a watch call, shows changes that occur after that particular version of a resource. (optional)
selector = 'selector_example' # str | the selector to to restrict returned list to applications only with matched labels. (optional)

    try:
        # Watch returns stream of application change events.
        api_response = api_instance.watch(name=name, refresh=refresh, project=project, resource_version=resource_version, selector=selector)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApplicationServiceApi->watch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| the application&#39;s name. | [optional] 
 **refresh** | **str**| forces application reconciliation if set to true. | [optional] 
 **project** | [**list[str]**](str.md)| the project names to restrict returned list applications. | [optional] 
 **resource_version** | **str**| when specified with a watch call, shows changes that occur after that particular version of a resource. | [optional] 
 **selector** | **str**| the selector to to restrict returned list to applications only with matched labels. | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response.(streaming responses) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

