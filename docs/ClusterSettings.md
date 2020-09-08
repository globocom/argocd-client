# ClusterSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_label_key** | **str** |  | [optional] 
**config_management_plugins** | [**list[V1alpha1ConfigManagementPlugin]**](V1alpha1ConfigManagementPlugin.md) |  | [optional] 
**dex_config** | [**ClusterDexConfig**](ClusterDexConfig.md) |  | [optional] 
**google_analytics** | [**ClusterGoogleAnalyticsConfig**](ClusterGoogleAnalyticsConfig.md) |  | [optional] 
**help** | [**ClusterHelp**](ClusterHelp.md) |  | [optional] 
**kustomize_options** | [**V1alpha1KustomizeOptions**](V1alpha1KustomizeOptions.md) |  | [optional] 
**kustomize_versions** | **list[str]** |  | [optional] 
**oidc_config** | [**ClusterOIDCConfig**](ClusterOIDCConfig.md) |  | [optional] 
**plugins** | [**list[ClusterPlugin]**](ClusterPlugin.md) |  | [optional] 
**resource_overrides** | [**dict(str, V1alpha1ResourceOverride)**](V1alpha1ResourceOverride.md) |  | [optional] 
**status_badge_enabled** | **bool** |  | [optional] 
**ui_css_url** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**user_logins_disabled** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


