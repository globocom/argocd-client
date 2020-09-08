# argocd_client.ProjectServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mixin6**](ProjectServiceApi.md#create_mixin6) | **POST** /api/v1/projects | Create a new project.
[**create_token**](ProjectServiceApi.md#create_token) | **POST** /api/v1/projects/{project}/roles/{role}/token | Create a new project token.
[**delete_mixin6**](ProjectServiceApi.md#delete_mixin6) | **DELETE** /api/v1/projects/{name} | Delete deletes a project
[**delete_token**](ProjectServiceApi.md#delete_token) | **DELETE** /api/v1/projects/{project}/roles/{role}/token/{iat} | Delete a new project token.
[**get_mixin6**](ProjectServiceApi.md#get_mixin6) | **GET** /api/v1/projects/{name} | Get returns a project by name
[**get_sync_windows_state**](ProjectServiceApi.md#get_sync_windows_state) | **GET** /api/v1/projects/{name}/syncwindows | GetSchedulesState returns true if there are any active sync syncWindows
[**list_events**](ProjectServiceApi.md#list_events) | **GET** /api/v1/projects/{name}/events | ListEvents returns a list of project events
[**list_mixin6**](ProjectServiceApi.md#list_mixin6) | **GET** /api/v1/projects | List returns list of projects
[**update_mixin6**](ProjectServiceApi.md#update_mixin6) | **PUT** /api/v1/projects/{project.metadata.name} | Update updates a project


# **create_mixin6**
> V1alpha1AppProject create_mixin6(body)

Create a new project.

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
    api_instance = argocd_client.ProjectServiceApi(api_client)
    body = argocd_client.ProjectProjectCreateRequest() # ProjectProjectCreateRequest | 

    try:
        # Create a new project.
        api_response = api_instance.create_mixin6(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectServiceApi->create_mixin6: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectProjectCreateRequest**](ProjectProjectCreateRequest.md)|  | 

### Return type

[**V1alpha1AppProject**](V1alpha1AppProject.md)

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

# **create_token**
> ProjectProjectTokenResponse create_token(project, role, body)

Create a new project token.

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
    api_instance = argocd_client.ProjectServiceApi(api_client)
    project = 'project_example' # str | 
role = 'role_example' # str | 
body = argocd_client.ProjectProjectTokenCreateRequest() # ProjectProjectTokenCreateRequest | 

    try:
        # Create a new project token.
        api_response = api_instance.create_token(project, role, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectServiceApi->create_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**|  | 
 **role** | **str**|  | 
 **body** | [**ProjectProjectTokenCreateRequest**](ProjectProjectTokenCreateRequest.md)|  | 

### Return type

[**ProjectProjectTokenResponse**](ProjectProjectTokenResponse.md)

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

# **delete_mixin6**
> object delete_mixin6(name)

Delete deletes a project

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
    api_instance = argocd_client.ProjectServiceApi(api_client)
    name = 'name_example' # str | 

    try:
        # Delete deletes a project
        api_response = api_instance.delete_mixin6(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectServiceApi->delete_mixin6: %s\n" % e)
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

# **delete_token**
> object delete_token(project, role, iat, id=id)

Delete a new project token.

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
    api_instance = argocd_client.ProjectServiceApi(api_client)
    project = 'project_example' # str | 
role = 'role_example' # str | 
iat = 'iat_example' # str | 
id = 'id_example' # str |  (optional)

    try:
        # Delete a new project token.
        api_response = api_instance.delete_token(project, role, iat, id=id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectServiceApi->delete_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**|  | 
 **role** | **str**|  | 
 **iat** | **str**|  | 
 **id** | **str**|  | [optional] 

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

# **get_mixin6**
> V1alpha1AppProject get_mixin6(name)

Get returns a project by name

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
    api_instance = argocd_client.ProjectServiceApi(api_client)
    name = 'name_example' # str | 

    try:
        # Get returns a project by name
        api_response = api_instance.get_mixin6(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectServiceApi->get_mixin6: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**V1alpha1AppProject**](V1alpha1AppProject.md)

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

# **get_sync_windows_state**
> ProjectSyncWindowsResponse get_sync_windows_state(name)

GetSchedulesState returns true if there are any active sync syncWindows

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
    api_instance = argocd_client.ProjectServiceApi(api_client)
    name = 'name_example' # str | 

    try:
        # GetSchedulesState returns true if there are any active sync syncWindows
        api_response = api_instance.get_sync_windows_state(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectServiceApi->get_sync_windows_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**ProjectSyncWindowsResponse**](ProjectSyncWindowsResponse.md)

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

# **list_events**
> V1EventList list_events(name)

ListEvents returns a list of project events

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
    api_instance = argocd_client.ProjectServiceApi(api_client)
    name = 'name_example' # str | 

    try:
        # ListEvents returns a list of project events
        api_response = api_instance.list_events(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectServiceApi->list_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

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

# **list_mixin6**
> V1alpha1AppProjectList list_mixin6(name=name)

List returns list of projects

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
    api_instance = argocd_client.ProjectServiceApi(api_client)
    name = 'name_example' # str |  (optional)

    try:
        # List returns list of projects
        api_response = api_instance.list_mixin6(name=name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectServiceApi->list_mixin6: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 

### Return type

[**V1alpha1AppProjectList**](V1alpha1AppProjectList.md)

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

# **update_mixin6**
> V1alpha1AppProject update_mixin6(project_metadata_name, body)

Update updates a project

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
    api_instance = argocd_client.ProjectServiceApi(api_client)
    project_metadata_name = 'project_metadata_name_example' # str | Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names +optional
body = argocd_client.ProjectProjectUpdateRequest() # ProjectProjectUpdateRequest | 

    try:
        # Update updates a project
        api_response = api_instance.update_mixin6(project_metadata_name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProjectServiceApi->update_mixin6: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_metadata_name** | **str**| Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names +optional | 
 **body** | [**ProjectProjectUpdateRequest**](ProjectProjectUpdateRequest.md)|  | 

### Return type

[**V1alpha1AppProject**](V1alpha1AppProject.md)

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

