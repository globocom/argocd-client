# argocd_client.SessionServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mixin11**](SessionServiceApi.md#create_mixin11) | **POST** /api/v1/session | Create a new JWT for authentication and set a cookie if using HTTP.
[**delete_mixin11**](SessionServiceApi.md#delete_mixin11) | **DELETE** /api/v1/session | Delete an existing JWT cookie if using HTTP.
[**get_user_info**](SessionServiceApi.md#get_user_info) | **GET** /api/v1/session/userinfo | Get the current user&#39;s info


# **create_mixin11**
> SessionSessionResponse create_mixin11(body)

Create a new JWT for authentication and set a cookie if using HTTP.

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
    api_instance = argocd_client.SessionServiceApi(api_client)
    body = argocd_client.SessionSessionCreateRequest() # SessionSessionCreateRequest | 

    try:
        # Create a new JWT for authentication and set a cookie if using HTTP.
        api_response = api_instance.create_mixin11(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SessionServiceApi->create_mixin11: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SessionSessionCreateRequest**](SessionSessionCreateRequest.md)|  | 

### Return type

[**SessionSessionResponse**](SessionSessionResponse.md)

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

# **delete_mixin11**
> SessionSessionResponse delete_mixin11()

Delete an existing JWT cookie if using HTTP.

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
    api_instance = argocd_client.SessionServiceApi(api_client)
    
    try:
        # Delete an existing JWT cookie if using HTTP.
        api_response = api_instance.delete_mixin11()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SessionServiceApi->delete_mixin11: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SessionSessionResponse**](SessionSessionResponse.md)

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

# **get_user_info**
> SessionGetUserInfoResponse get_user_info()

Get the current user's info

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
    api_instance = argocd_client.SessionServiceApi(api_client)
    
    try:
        # Get the current user's info
        api_response = api_instance.get_user_info()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SessionServiceApi->get_user_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SessionGetUserInfoResponse**](SessionGetUserInfoResponse.md)

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

