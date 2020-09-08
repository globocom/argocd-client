# V1alpha1ApplicationSpec

ApplicationSpec represents desired application state. Contains link to repository with application definition and additional parameters link definition revision.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | [**V1alpha1ApplicationDestination**](V1alpha1ApplicationDestination.md) |  | [optional] 
**ignore_differences** | [**list[V1alpha1ResourceIgnoreDifferences]**](V1alpha1ResourceIgnoreDifferences.md) |  | [optional] 
**info** | [**list[V1alpha1Info]**](V1alpha1Info.md) |  | [optional] 
**project** | **str** | Project is a application project name. Empty name means that application belongs to &#39;default&#39; project. | [optional] 
**revision_history_limit** | **str** | This limits this number of items kept in the apps revision history. This should only be changed in exceptional circumstances. Setting to zero will store no history. This will reduce storage used. Increasing will increase the space used to store the history, so we do not recommend increasing it. Default is 10. | [optional] 
**source** | [**V1alpha1ApplicationSource**](V1alpha1ApplicationSource.md) |  | [optional] 
**sync_policy** | [**V1alpha1SyncPolicy**](V1alpha1SyncPolicy.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


