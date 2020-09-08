# argocd_client.VersionServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**version**](VersionServiceApi.md#version) | **GET** /api/version | Version returns version information of the API server


# **version**
> VersionVersionMessage version()

Version returns version information of the API server

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
    api_instance = argocd_client.VersionServiceApi(api_client)
    
    try:
        # Version returns version information of the API server
        api_response = api_instance.version()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VersionServiceApi->version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VersionVersionMessage**](VersionVersionMessage.md)

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

