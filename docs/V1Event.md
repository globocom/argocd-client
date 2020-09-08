# V1Event

Event is a report of an event somewhere in the cluster.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**count** | **int** |  | [optional] 
**event_time** | [**V1MicroTime**](V1MicroTime.md) |  | [optional] 
**first_timestamp** | [**V1Time**](V1Time.md) |  | [optional] 
**involved_object** | [**V1ObjectReference**](V1ObjectReference.md) |  | [optional] 
**last_timestamp** | [**V1Time**](V1Time.md) |  | [optional] 
**message** | **str** |  | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) |  | [optional] 
**reason** | **str** |  | [optional] 
**related** | [**V1ObjectReference**](V1ObjectReference.md) |  | [optional] 
**reporting_component** | **str** |  | [optional] 
**reporting_instance** | **str** |  | [optional] 
**series** | [**V1EventSeries**](V1EventSeries.md) |  | [optional] 
**source** | [**V1EventSource**](V1EventSource.md) |  | [optional] 
**type** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


