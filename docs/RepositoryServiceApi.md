# argocd_client.RepositoryServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_repository**](RepositoryServiceApi.md#create_repository) | **POST** /api/v1/repositories | CreateRepository creates a new repository configuration
[**delete_repository**](RepositoryServiceApi.md#delete_repository) | **DELETE** /api/v1/repositories/{repo} | DeleteRepository deletes a repository from the configuration
[**get_app_details**](RepositoryServiceApi.md#get_app_details) | **POST** /api/v1/repositories/{source.repoURL}/appdetails | GetAppDetails returns application details by given path
[**get_helm_charts**](RepositoryServiceApi.md#get_helm_charts) | **GET** /api/v1/repositories/{repo}/helmcharts | 
[**get_mixin3**](RepositoryServiceApi.md#get_mixin3) | **GET** /api/v1/repositories/{repo} | Get returns a repository or its credentials
[**list_apps**](RepositoryServiceApi.md#list_apps) | **GET** /api/v1/repositories/{repo}/apps | ListApps returns list of apps in the repo
[**list_repositories**](RepositoryServiceApi.md#list_repositories) | **GET** /api/v1/repositories | ListRepositories gets a list of all configured repositories
[**update_repository**](RepositoryServiceApi.md#update_repository) | **PUT** /api/v1/repositories/{repo.repo} | UpdateRepository updates a repository configuration
[**validate_access**](RepositoryServiceApi.md#validate_access) | **POST** /api/v1/repositories/{repo}/validate | ValidateAccess validates access to a repository with given parameters


# **create_repository**
> V1alpha1Repository create_repository(body)

CreateRepository creates a new repository configuration

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
    api_instance = argocd_client.RepositoryServiceApi(api_client)
    body = argocd_client.V1alpha1Repository() # V1alpha1Repository | Repository definition

    try:
        # CreateRepository creates a new repository configuration
        api_response = api_instance.create_repository(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoryServiceApi->create_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alpha1Repository**](V1alpha1Repository.md)| Repository definition | 

### Return type

[**V1alpha1Repository**](V1alpha1Repository.md)

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

# **delete_repository**
> object delete_repository(repo, force_refresh=force_refresh)

DeleteRepository deletes a repository from the configuration

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
    api_instance = argocd_client.RepositoryServiceApi(api_client)
    repo = 'repo_example' # str | Repo URL for query
force_refresh = True # bool | Whether to force a cache refresh on repo's connection state. (optional)

    try:
        # DeleteRepository deletes a repository from the configuration
        api_response = api_instance.delete_repository(repo, force_refresh=force_refresh)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoryServiceApi->delete_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Repo URL for query | 
 **force_refresh** | **bool**| Whether to force a cache refresh on repo&#39;s connection state. | [optional] 

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

# **get_app_details**
> RepositoryRepoAppDetailsResponse get_app_details(source_repo_url, body)

GetAppDetails returns application details by given path

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
    api_instance = argocd_client.RepositoryServiceApi(api_client)
    source_repo_url = 'source_repo_url_example' # str | RepoURL is the repository URL of the application manifests
body = argocd_client.RepositoryRepoAppDetailsQuery() # RepositoryRepoAppDetailsQuery | 

    try:
        # GetAppDetails returns application details by given path
        api_response = api_instance.get_app_details(source_repo_url, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoryServiceApi->get_app_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_repo_url** | **str**| RepoURL is the repository URL of the application manifests | 
 **body** | [**RepositoryRepoAppDetailsQuery**](RepositoryRepoAppDetailsQuery.md)|  | 

### Return type

[**RepositoryRepoAppDetailsResponse**](RepositoryRepoAppDetailsResponse.md)

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

# **get_helm_charts**
> RepositoryHelmChartsResponse get_helm_charts(repo, force_refresh=force_refresh)



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
    api_instance = argocd_client.RepositoryServiceApi(api_client)
    repo = 'repo_example' # str | Repo URL for query
force_refresh = True # bool | Whether to force a cache refresh on repo's connection state. (optional)

    try:
        api_response = api_instance.get_helm_charts(repo, force_refresh=force_refresh)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoryServiceApi->get_helm_charts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Repo URL for query | 
 **force_refresh** | **bool**| Whether to force a cache refresh on repo&#39;s connection state. | [optional] 

### Return type

[**RepositoryHelmChartsResponse**](RepositoryHelmChartsResponse.md)

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

# **get_mixin3**
> V1alpha1Repository get_mixin3(repo, force_refresh=force_refresh)

Get returns a repository or its credentials

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
    api_instance = argocd_client.RepositoryServiceApi(api_client)
    repo = 'repo_example' # str | Repo URL for query
force_refresh = True # bool | Whether to force a cache refresh on repo's connection state. (optional)

    try:
        # Get returns a repository or its credentials
        api_response = api_instance.get_mixin3(repo, force_refresh=force_refresh)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoryServiceApi->get_mixin3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Repo URL for query | 
 **force_refresh** | **bool**| Whether to force a cache refresh on repo&#39;s connection state. | [optional] 

### Return type

[**V1alpha1Repository**](V1alpha1Repository.md)

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

# **list_apps**
> RepositoryRepoAppsResponse list_apps(repo, revision=revision)

ListApps returns list of apps in the repo

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
    api_instance = argocd_client.RepositoryServiceApi(api_client)
    repo = 'repo_example' # str | 
revision = 'revision_example' # str |  (optional)

    try:
        # ListApps returns list of apps in the repo
        api_response = api_instance.list_apps(repo, revision=revision)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoryServiceApi->list_apps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**|  | 
 **revision** | **str**|  | [optional] 

### Return type

[**RepositoryRepoAppsResponse**](RepositoryRepoAppsResponse.md)

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

# **list_repositories**
> V1alpha1RepositoryList list_repositories(repo=repo, force_refresh=force_refresh)

ListRepositories gets a list of all configured repositories

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
    api_instance = argocd_client.RepositoryServiceApi(api_client)
    repo = 'repo_example' # str | Repo URL for query. (optional)
force_refresh = True # bool | Whether to force a cache refresh on repo's connection state. (optional)

    try:
        # ListRepositories gets a list of all configured repositories
        api_response = api_instance.list_repositories(repo=repo, force_refresh=force_refresh)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoryServiceApi->list_repositories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| Repo URL for query. | [optional] 
 **force_refresh** | **bool**| Whether to force a cache refresh on repo&#39;s connection state. | [optional] 

### Return type

[**V1alpha1RepositoryList**](V1alpha1RepositoryList.md)

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

# **update_repository**
> V1alpha1Repository update_repository(repo_repo, body)

UpdateRepository updates a repository configuration

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
    api_instance = argocd_client.RepositoryServiceApi(api_client)
    repo_repo = 'repo_repo_example' # str | URL of the repo
body = argocd_client.V1alpha1Repository() # V1alpha1Repository | 

    try:
        # UpdateRepository updates a repository configuration
        api_response = api_instance.update_repository(repo_repo, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoryServiceApi->update_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo_repo** | **str**| URL of the repo | 
 **body** | [**V1alpha1Repository**](V1alpha1Repository.md)|  | 

### Return type

[**V1alpha1Repository**](V1alpha1Repository.md)

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

# **validate_access**
> object validate_access(repo, body)

ValidateAccess validates access to a repository with given parameters

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
    api_instance = argocd_client.RepositoryServiceApi(api_client)
    repo = 'repo_example' # str | The URL to the repo
body = 'body_example' # str | The URL to the repo

    try:
        # ValidateAccess validates access to a repository with given parameters
        api_response = api_instance.validate_access(repo, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoryServiceApi->validate_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| The URL to the repo | 
 **body** | **str**| The URL to the repo | 

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

