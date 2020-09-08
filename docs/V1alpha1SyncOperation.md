# V1alpha1SyncOperation

SyncOperation contains sync operation details.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** |  | [optional] 
**manifests** | **list[str]** |  | [optional] 
**prune** | **bool** |  | [optional] 
**resources** | [**list[V1alpha1SyncOperationResource]**](V1alpha1SyncOperationResource.md) |  | [optional] 
**revision** | **str** | Revision is the revision in which to sync the application to. If omitted, will use the revision specified in app spec. | [optional] 
**source** | [**V1alpha1ApplicationSource**](V1alpha1ApplicationSource.md) |  | [optional] 
**sync_options** | **list[str]** |  | [optional] 
**sync_strategy** | [**V1alpha1SyncStrategy**](V1alpha1SyncStrategy.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


