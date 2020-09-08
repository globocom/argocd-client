# V1alpha1ClusterConfig

ClusterConfig is the configuration attributes. This structure is subset of the go-client rest.Config with annotations added for marshalling.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_auth_config** | [**V1alpha1AWSAuthConfig**](V1alpha1AWSAuthConfig.md) |  | [optional] 
**bearer_token** | **str** | Server requires Bearer authentication. This client will not attempt to use refresh tokens for an OAuth2 flow. TODO: demonstrate an OAuth2 compatible client. | [optional] 
**password** | **str** |  | [optional] 
**tls_client_config** | [**V1alpha1TLSClientConfig**](V1alpha1TLSClientConfig.md) |  | [optional] 
**username** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


