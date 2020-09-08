# argocd_client.SettingsServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](SettingsServiceApi.md#get) | **GET** /api/v1/settings | Get returns Argo CD settings


# **get**
> ClusterSettings get()

Get returns Argo CD settings

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
    api_instance = argocd_client.SettingsServiceApi(api_client)
    
    try:
        # Get returns Argo CD settings
        api_response = api_instance.get()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SettingsServiceApi->get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterSettings**](ClusterSettings.md)

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

