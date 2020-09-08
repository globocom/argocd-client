# argocd_client.RepoCredsServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_repository_credentials**](RepoCredsServiceApi.md#create_repository_credentials) | **POST** /api/v1/repocreds | CreateRepositoryCredentials creates a new repository credential set
[**delete_repository_credentials**](RepoCredsServiceApi.md#delete_repository_credentials) | **DELETE** /api/v1/repocreds/{url} | DeleteRepositoryCredentials deletes a repository credential set from the configuration
[**list_repository_credentials**](RepoCredsServiceApi.md#list_repository_credentials) | **GET** /api/v1/repocreds | ListRepositoryCredentials gets a list of all configured repository credential sets
[**update_repository_credentials**](RepoCredsServiceApi.md#update_repository_credentials) | **PUT** /api/v1/repocreds/{creds.url} | UpdateRepositoryCredentials updates a repository credential set


# **create_repository_credentials**
> V1alpha1RepoCreds create_repository_credentials(body)

CreateRepositoryCredentials creates a new repository credential set

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
    api_instance = argocd_client.RepoCredsServiceApi(api_client)
    body = argocd_client.V1alpha1RepoCreds() # V1alpha1RepoCreds | Repository definition

    try:
        # CreateRepositoryCredentials creates a new repository credential set
        api_response = api_instance.create_repository_credentials(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepoCredsServiceApi->create_repository_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alpha1RepoCreds**](V1alpha1RepoCreds.md)| Repository definition | 

### Return type

[**V1alpha1RepoCreds**](V1alpha1RepoCreds.md)

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

# **delete_repository_credentials**
> object delete_repository_credentials(url)

DeleteRepositoryCredentials deletes a repository credential set from the configuration

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
    api_instance = argocd_client.RepoCredsServiceApi(api_client)
    url = 'url_example' # str | 

    try:
        # DeleteRepositoryCredentials deletes a repository credential set from the configuration
        api_response = api_instance.delete_repository_credentials(url)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepoCredsServiceApi->delete_repository_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**|  | 

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

# **list_repository_credentials**
> V1alpha1RepoCredsList list_repository_credentials(url=url)

ListRepositoryCredentials gets a list of all configured repository credential sets

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
    api_instance = argocd_client.RepoCredsServiceApi(api_client)
    url = 'url_example' # str | Repo URL for query. (optional)

    try:
        # ListRepositoryCredentials gets a list of all configured repository credential sets
        api_response = api_instance.list_repository_credentials(url=url)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepoCredsServiceApi->list_repository_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| Repo URL for query. | [optional] 

### Return type

[**V1alpha1RepoCredsList**](V1alpha1RepoCredsList.md)

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

# **update_repository_credentials**
> V1alpha1RepoCreds update_repository_credentials(creds_url, body)

UpdateRepositoryCredentials updates a repository credential set

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
    api_instance = argocd_client.RepoCredsServiceApi(api_client)
    creds_url = 'creds_url_example' # str | URL is the URL that this credentials matches to
body = argocd_client.V1alpha1RepoCreds() # V1alpha1RepoCreds | 

    try:
        # UpdateRepositoryCredentials updates a repository credential set
        api_response = api_instance.update_repository_credentials(creds_url, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepoCredsServiceApi->update_repository_credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creds_url** | **str**| URL is the URL that this credentials matches to | 
 **body** | [**V1alpha1RepoCreds**](V1alpha1RepoCreds.md)|  | 

### Return type

[**V1alpha1RepoCreds**](V1alpha1RepoCreds.md)

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

