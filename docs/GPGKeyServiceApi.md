# argocd_client.GPGKeyServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mixin7**](GPGKeyServiceApi.md#create_mixin7) | **POST** /api/v1/gpgkeys | Create one or more GPG public keys in the server&#39;s configuration
[**delete_mixin7**](GPGKeyServiceApi.md#delete_mixin7) | **DELETE** /api/v1/gpgkeys | Delete specified GPG public key from the server&#39;s configuration
[**get_mixin7**](GPGKeyServiceApi.md#get_mixin7) | **GET** /api/v1/gpgkeys/{keyID} | Get information about specified GPG public key from the server
[**list_mixin7**](GPGKeyServiceApi.md#list_mixin7) | **GET** /api/v1/gpgkeys | List all available repository certificates


# **create_mixin7**
> GpgkeyGnuPGPublicKeyCreateResponse create_mixin7(body)

Create one or more GPG public keys in the server's configuration

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
    api_instance = argocd_client.GPGKeyServiceApi(api_client)
    body = argocd_client.V1alpha1GnuPGPublicKey() # V1alpha1GnuPGPublicKey | Raw key data of the GPG key(s) to create

    try:
        # Create one or more GPG public keys in the server's configuration
        api_response = api_instance.create_mixin7(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GPGKeyServiceApi->create_mixin7: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alpha1GnuPGPublicKey**](V1alpha1GnuPGPublicKey.md)| Raw key data of the GPG key(s) to create | 

### Return type

[**GpgkeyGnuPGPublicKeyCreateResponse**](GpgkeyGnuPGPublicKeyCreateResponse.md)

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

# **delete_mixin7**
> object delete_mixin7(key_id=key_id)

Delete specified GPG public key from the server's configuration

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
    api_instance = argocd_client.GPGKeyServiceApi(api_client)
    key_id = 'key_id_example' # str | The GPG key ID to query for. (optional)

    try:
        # Delete specified GPG public key from the server's configuration
        api_response = api_instance.delete_mixin7(key_id=key_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GPGKeyServiceApi->delete_mixin7: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| The GPG key ID to query for. | [optional] 

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

# **get_mixin7**
> V1alpha1GnuPGPublicKey get_mixin7(key_id)

Get information about specified GPG public key from the server

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
    api_instance = argocd_client.GPGKeyServiceApi(api_client)
    key_id = 'key_id_example' # str | The GPG key ID to query for

    try:
        # Get information about specified GPG public key from the server
        api_response = api_instance.get_mixin7(key_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GPGKeyServiceApi->get_mixin7: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| The GPG key ID to query for | 

### Return type

[**V1alpha1GnuPGPublicKey**](V1alpha1GnuPGPublicKey.md)

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

# **list_mixin7**
> V1alpha1GnuPGPublicKeyList list_mixin7(key_id=key_id)

List all available repository certificates

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
    api_instance = argocd_client.GPGKeyServiceApi(api_client)
    key_id = 'key_id_example' # str | The GPG key ID to query for. (optional)

    try:
        # List all available repository certificates
        api_response = api_instance.list_mixin7(key_id=key_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GPGKeyServiceApi->list_mixin7: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| The GPG key ID to query for. | [optional] 

### Return type

[**V1alpha1GnuPGPublicKeyList**](V1alpha1GnuPGPublicKeyList.md)

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

