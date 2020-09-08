# V1alpha1Cluster

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**V1alpha1ClusterConfig**](V1alpha1ClusterConfig.md) |  | [optional] 
**connection_state** | [**V1alpha1ConnectionState**](V1alpha1ConnectionState.md) |  | [optional] 
**info** | [**V1alpha1ClusterInfo**](V1alpha1ClusterInfo.md) |  | [optional] 
**name** | **str** |  | [optional] 
**namespaces** | **list[str]** | Holds list of namespaces which are accessible in that cluster. Cluster level resources would be ignored if namespace list is not empty. | [optional] 
**refresh_requested_at** | [**V1Time**](V1Time.md) |  | [optional] 
**server** | **str** |  | [optional] 
**server_version** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


