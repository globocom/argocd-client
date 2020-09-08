# V1alpha1AppProjectSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_resource_blacklist** | [**list[V1GroupKind]**](V1GroupKind.md) |  | [optional] 
**cluster_resource_whitelist** | [**list[V1GroupKind]**](V1GroupKind.md) |  | [optional] 
**description** | **str** |  | [optional] 
**destinations** | [**list[V1alpha1ApplicationDestination]**](V1alpha1ApplicationDestination.md) |  | [optional] 
**namespace_resource_blacklist** | [**list[V1GroupKind]**](V1GroupKind.md) |  | [optional] 
**namespace_resource_whitelist** | [**list[V1GroupKind]**](V1GroupKind.md) |  | [optional] 
**orphaned_resources** | [**V1alpha1OrphanedResourcesMonitorSettings**](V1alpha1OrphanedResourcesMonitorSettings.md) |  | [optional] 
**roles** | [**list[V1alpha1ProjectRole]**](V1alpha1ProjectRole.md) |  | [optional] 
**signature_keys** | [**list[V1alpha1SignatureKey]**](V1alpha1SignatureKey.md) |  | [optional] 
**source_repos** | **list[str]** |  | [optional] 
**sync_windows** | [**list[V1alpha1SyncWindow]**](V1alpha1SyncWindow.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


