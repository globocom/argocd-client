# V1alpha1ResourceNetworkingInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_ur_ls** | **list[str]** | ExternalURLs holds list of URLs which should be available externally. List is populated for ingress resources using rules hostnames. | [optional] 
**ingress** | [**list[V1LoadBalancerIngress]**](V1LoadBalancerIngress.md) |  | [optional] 
**labels** | **dict(str, str)** |  | [optional] 
**target_labels** | **dict(str, str)** |  | [optional] 
**target_refs** | [**list[V1alpha1ResourceRef]**](V1alpha1ResourceRef.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


