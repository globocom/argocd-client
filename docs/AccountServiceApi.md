# argocd_client.AccountServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**can_i**](AccountServiceApi.md#can_i) | **GET** /api/v1/account/can-i/{resource}/{action}/{subresource} | 
[**create_token_mixin10**](AccountServiceApi.md#create_token_mixin10) | **POST** /api/v1/account/{name}/token | 
[**delete_token_mixin10**](AccountServiceApi.md#delete_token_mixin10) | **DELETE** /api/v1/account/{name}/token/{id} | 
[**get_account**](AccountServiceApi.md#get_account) | **GET** /api/v1/account/{name} | 
[**list_accounts**](AccountServiceApi.md#list_accounts) | **GET** /api/v1/account | 
[**update_password**](AccountServiceApi.md#update_password) | **PUT** /api/v1/account/password | UpdatePassword updates an account&#39;s password to a new value


# **can_i**
> AccountCanIResponse can_i(resource, action, subresource)



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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource** | **str**|  | 
 **action** | **str**|  | 
 **subresource** | **str**|  | 

### Return type

[**AccountCanIResponse**](AccountCanIResponse.md)

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

# **create_token_mixin10**
> AccountCreateTokenResponse create_token_mixin10(name, body)



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
    api_instance = argocd_client.AccountServiceApi(api_client)
    name = 'name_example' # str | 
body = argocd_client.AccountCreateTokenRequest() # AccountCreateTokenRequest | 

    try:
        api_response = api_instance.create_token_mixin10(name, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountServiceApi->create_token_mixin10: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **body** | [**AccountCreateTokenRequest**](AccountCreateTokenRequest.md)|  | 

### Return type

[**AccountCreateTokenResponse**](AccountCreateTokenResponse.md)

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

# **delete_token_mixin10**
> object delete_token_mixin10(name, id)



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
    api_instance = argocd_client.AccountServiceApi(api_client)
    name = 'name_example' # str | 
id = 'id_example' # str | 

    try:
        api_response = api_instance.delete_token_mixin10(name, id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountServiceApi->delete_token_mixin10: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **id** | **str**|  | 

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

# **get_account**
> AccountAccount get_account(name)



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
    api_instance = argocd_client.AccountServiceApi(api_client)
    name = 'name_example' # str | 

    try:
        api_response = api_instance.get_account(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountServiceApi->get_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**AccountAccount**](AccountAccount.md)

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

# **list_accounts**
> AccountAccountsList list_accounts()



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
    api_instance = argocd_client.AccountServiceApi(api_client)
    
    try:
        api_response = api_instance.list_accounts()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountServiceApi->list_accounts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccountAccountsList**](AccountAccountsList.md)

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

# **update_password**
> object update_password(body)

UpdatePassword updates an account's password to a new value

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
    api_instance = argocd_client.AccountServiceApi(api_client)
    body = argocd_client.AccountUpdatePasswordRequest() # AccountUpdatePasswordRequest | 

    try:
        # UpdatePassword updates an account's password to a new value
        api_response = api_instance.update_password(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountServiceApi->update_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccountUpdatePasswordRequest**](AccountUpdatePasswordRequest.md)|  | 

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

