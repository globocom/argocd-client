# argocd_client.CertificateServiceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_certificate**](CertificateServiceApi.md#create_certificate) | **POST** /api/v1/certificates | Creates repository certificates on the server
[**delete_certificate**](CertificateServiceApi.md#delete_certificate) | **DELETE** /api/v1/certificates | Delete the certificates that match the RepositoryCertificateQuery
[**list_certificates**](CertificateServiceApi.md#list_certificates) | **GET** /api/v1/certificates | List all available repository certificates


# **create_certificate**
> V1alpha1RepositoryCertificateList create_certificate(body)

Creates repository certificates on the server

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
    api_instance = argocd_client.CertificateServiceApi(api_client)
    body = argocd_client.V1alpha1RepositoryCertificateList() # V1alpha1RepositoryCertificateList | List of certificates to be created

    try:
        # Creates repository certificates on the server
        api_response = api_instance.create_certificate(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CertificateServiceApi->create_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1alpha1RepositoryCertificateList**](V1alpha1RepositoryCertificateList.md)| List of certificates to be created | 

### Return type

[**V1alpha1RepositoryCertificateList**](V1alpha1RepositoryCertificateList.md)

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

# **delete_certificate**
> V1alpha1RepositoryCertificateList delete_certificate(host_name_pattern=host_name_pattern, cert_type=cert_type, cert_sub_type=cert_sub_type)

Delete the certificates that match the RepositoryCertificateQuery

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
    api_instance = argocd_client.CertificateServiceApi(api_client)
    host_name_pattern = 'host_name_pattern_example' # str | A file-glob pattern (not regular expression) the host name has to match. (optional)
cert_type = 'cert_type_example' # str | The type of the certificate to match (ssh or https). (optional)
cert_sub_type = 'cert_sub_type_example' # str | The sub type of the certificate to match (protocol dependent, usually only used for ssh certs). (optional)

    try:
        # Delete the certificates that match the RepositoryCertificateQuery
        api_response = api_instance.delete_certificate(host_name_pattern=host_name_pattern, cert_type=cert_type, cert_sub_type=cert_sub_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CertificateServiceApi->delete_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_name_pattern** | **str**| A file-glob pattern (not regular expression) the host name has to match. | [optional] 
 **cert_type** | **str**| The type of the certificate to match (ssh or https). | [optional] 
 **cert_sub_type** | **str**| The sub type of the certificate to match (protocol dependent, usually only used for ssh certs). | [optional] 

### Return type

[**V1alpha1RepositoryCertificateList**](V1alpha1RepositoryCertificateList.md)

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

# **list_certificates**
> V1alpha1RepositoryCertificateList list_certificates(host_name_pattern=host_name_pattern, cert_type=cert_type, cert_sub_type=cert_sub_type)

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
    api_instance = argocd_client.CertificateServiceApi(api_client)
    host_name_pattern = 'host_name_pattern_example' # str | A file-glob pattern (not regular expression) the host name has to match. (optional)
cert_type = 'cert_type_example' # str | The type of the certificate to match (ssh or https). (optional)
cert_sub_type = 'cert_sub_type_example' # str | The sub type of the certificate to match (protocol dependent, usually only used for ssh certs). (optional)

    try:
        # List all available repository certificates
        api_response = api_instance.list_certificates(host_name_pattern=host_name_pattern, cert_type=cert_type, cert_sub_type=cert_sub_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CertificateServiceApi->list_certificates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_name_pattern** | **str**| A file-glob pattern (not regular expression) the host name has to match. | [optional] 
 **cert_type** | **str**| The type of the certificate to match (ssh or https). | [optional] 
 **cert_sub_type** | **str**| The sub type of the certificate to match (protocol dependent, usually only used for ssh certs). | [optional] 

### Return type

[**V1alpha1RepositoryCertificateList**](V1alpha1RepositoryCertificateList.md)

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

