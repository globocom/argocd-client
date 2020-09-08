# argocd_client.ClusterServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ClusterServiceApi.md#create) | **POST** /api/v1/clusters | Create creates a cluster
[**delete**](ClusterServiceApi.md#delete) | **DELETE** /api/v1/clusters/{server} | Delete deletes a cluster
[**get_mixin2**](ClusterServiceApi.md#get_mixin2) | **GET** /api/v1/clusters/{server} | Get returns a cluster by server address
[**invalidate_cache**](ClusterServiceApi.md#invalidate_cache) | **POST** /api/v1/clusters/{server}/invalidate-cache | InvalidateCache invalidates cluster cache
[**list**](ClusterServiceApi.md#list) | **GET** /api/v1/clusters | List returns list of clusters
[**rotate_auth**](ClusterServiceApi.md#rotate_auth) | **POST** /api/v1/clusters/{server}/rotate-auth | RotateAuth rotates the bearer token used for a cluster
[**update**](ClusterServiceApi.md#update) | **PUT** /api/v1/clusters/{cluster.server} | Update updates a cluster


# **create**
> V1alpha1Cluster create(body)

Create creates a cluster

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
    api_instance = argocd_client.ClusterServiceApi(api_client)
    body = argocd_client.V1alpha1Cluster() # V1alpha1Cluster | 

    try:
        # Create creates a cluster
        api_response = api_instance.create(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClusterServiceApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alpha1Cluster**](V1alpha1Cluster.md)|  | 

### Return type

[**V1alpha1Cluster**](V1alpha1Cluster.md)

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

# **delete**
> object delete(server, name=name)

Delete deletes a cluster

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
    api_instance = argocd_client.ClusterServiceApi(api_client)
    server = 'server_example' # str | 
name = 'name_example' # str |  (optional)

    try:
        # Delete deletes a cluster
        api_response = api_instance.delete(server, name=name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClusterServiceApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**|  | 
 **name** | **str**|  | [optional] 

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

# **get_mixin2**
> V1alpha1Cluster get_mixin2(server, name=name)

Get returns a cluster by server address

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
    api_instance = argocd_client.ClusterServiceApi(api_client)
    server = 'server_example' # str | 
name = 'name_example' # str |  (optional)

    try:
        # Get returns a cluster by server address
        api_response = api_instance.get_mixin2(server, name=name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClusterServiceApi->get_mixin2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**|  | 
 **name** | **str**|  | [optional] 

### Return type

[**V1alpha1Cluster**](V1alpha1Cluster.md)

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

# **invalidate_cache**
> V1alpha1Cluster invalidate_cache(server)

InvalidateCache invalidates cluster cache

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
    api_instance = argocd_client.ClusterServiceApi(api_client)
    server = 'server_example' # str | 

    try:
        # InvalidateCache invalidates cluster cache
        api_response = api_instance.invalidate_cache(server)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClusterServiceApi->invalidate_cache: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**|  | 

### Return type

[**V1alpha1Cluster**](V1alpha1Cluster.md)

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

# **list**
> V1alpha1ClusterList list(server=server, name=name)

List returns list of clusters

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
    api_instance = argocd_client.ClusterServiceApi(api_client)
    server = 'server_example' # str |  (optional)
name = 'name_example' # str |  (optional)

    try:
        # List returns list of clusters
        api_response = api_instance.list(server=server, name=name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClusterServiceApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 

### Return type

[**V1alpha1ClusterList**](V1alpha1ClusterList.md)

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

# **rotate_auth**
> object rotate_auth(server)

RotateAuth rotates the bearer token used for a cluster

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
    api_instance = argocd_client.ClusterServiceApi(api_client)
    server = 'server_example' # str | 

    try:
        # RotateAuth rotates the bearer token used for a cluster
        api_response = api_instance.rotate_auth(server)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClusterServiceApi->rotate_auth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server** | **str**|  | 

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

# **update**
> V1alpha1Cluster update(cluster_server, body)

Update updates a cluster

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
    api_instance = argocd_client.ClusterServiceApi(api_client)
    cluster_server = 'cluster_server_example' # str | Server is the API server URL of the Kubernetes cluster
body = argocd_client.V1alpha1Cluster() # V1alpha1Cluster | 

    try:
        # Update updates a cluster
        api_response = api_instance.update(cluster_server, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ClusterServiceApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_server** | **str**| Server is the API server URL of the Kubernetes cluster | 
 **body** | [**V1alpha1Cluster**](V1alpha1Cluster.md)|  | 

### Return type

[**V1alpha1Cluster**](V1alpha1Cluster.md)

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

