# V1alpha1OperationState

OperationState contains information about state of currently performing operation on application.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**finished_at** | [**V1Time**](V1Time.md) |  | [optional] 
**message** | **str** | Message hold any pertinent messages when attempting to perform operation (typically errors). | [optional] 
**operation** | [**V1alpha1Operation**](V1alpha1Operation.md) |  | [optional] 
**phase** | **str** |  | [optional] 
**retry_count** | **str** |  | [optional] 
**started_at** | [**V1Time**](V1Time.md) |  | [optional] 
**sync_result** | [**V1alpha1SyncOperationResult**](V1alpha1SyncOperationResult.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


