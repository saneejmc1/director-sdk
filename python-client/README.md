# cloudera-director-python-client
Software-defined EDH clusters on cloud infrastructure

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: d6.0
- Package version: 6.0.0
- Build date: 2018-08-16T18:13:47.245-04:00
- Build package: com.cloudera.director.PythonClientCodegen
For more information, please visit [http://www.cloudera.com/](http://www.cloudera.com/)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import cloudera.director 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import cloudera.director
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import cloudera.director
from cloudera.director.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
cloudera.director.configuration.username = 'YOUR_USERNAME'
cloudera.director.configuration.password = 'YOUR_PASSWORD'
# create an instance of the API class
api_instance = cloudera.director.AuthenticationApi()
login = cloudera.director.Login() # Login | login

try:
    # Log in to the API
    api_response = api_instance.login(login)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->login: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost:7189*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthenticationApi* | [**login**](docs/AuthenticationApi.md#login) | **POST** /api/d6.0/login | Log in to the API
*AuthenticationApi* | [**logout**](docs/AuthenticationApi.md#logout) | **POST** /api/d6.0/logout | Log out from the API
*ClustersApi* | [**collect_diagnostic_data**](docs/ClustersApi.md#collect_diagnostic_data) | **POST** /api/d6.0/environments/{environment}/deployments/{deployment}/clusters/{cluster}/diagnosticData | Collects diagnostic data
*ClustersApi* | [**create**](docs/ClustersApi.md#create) | **POST** /api/d6.0/environments/{environment}/deployments/{deployment}/clusters | Create a new cluster
*ClustersApi* | [**delete**](docs/ClustersApi.md#delete) | **DELETE** /api/d6.0/environments/{environment}/deployments/{deployment}/clusters/{cluster} | Delete a cluster by name
*ClustersApi* | [**export_cluster_configuration**](docs/ClustersApi.md#export_cluster_configuration) | **GET** /api/d6.0/environments/{environment}/deployments/{deployment}/clusters/{cluster}/config | Exports the cluster configuration for this cluster
*ClustersApi* | [**get_administration_settings**](docs/ClustersApi.md#get_administration_settings) | **GET** /api/d6.0/environments/{environment}/deployments/{deployment}/clusters/{cluster}/settings | Get administration settings for a cluster
*ClustersApi* | [**get_history**](docs/ClustersApi.md#get_history) | **GET** /api/d6.0/environments/{environment}/deployments/{deployment}/clusters/{cluster}/history | Get history of updates for a cluster
*ClustersApi* | [**get_metrics**](docs/ClustersApi.md#get_metrics) | **GET** /api/d6.0/environments/{environment}/deployments/{deployment}/clusters/{cluster}/metrics | Get cluster metrics by name
*ClustersApi* | [**get_redacted**](docs/ClustersApi.md#get_redacted) | **GET** /api/d6.0/environments/{environment}/deployments/{deployment}/clusters/{cluster} | Get a cluster by name
*ClustersApi* | [**get_status**](docs/ClustersApi.md#get_status) | **GET** /api/d6.0/environments/{environment}/deployments/{deployment}/clusters/{cluster}/status | Get a cluster status by name
*ClustersApi* | [**get_template_redacted**](docs/ClustersApi.md#get_template_redacted) | **GET** /api/d6.0/environments/{environment}/deployments/{deployment}/clusters/{cluster}/template | Get a cluster template by name
*ClustersApi* | [**list**](docs/ClustersApi.md#list) | **GET** /api/d6.0/environments/{environment}/deployments/{deployment}/clusters | List all clusters
*ClustersApi* | [**update**](docs/ClustersApi.md#update) | **PUT** /api/d6.0/environments/{environment}/deployments/{deployment}/clusters/{cluster} | Update an existing cluster
*ClustersApi* | [**update_administration_settings**](docs/ClustersApi.md#update_administration_settings) | **PUT** /api/d6.0/environments/{environment}/deployments/{deployment}/clusters/{cluster}/settings | Update administration settings for a cluster
*DatabaseServersApi* | [**create**](docs/DatabaseServersApi.md#create) | **POST** /api/d6.0/environments/{environment}/databaseServers | Create a new external database server
*DatabaseServersApi* | [**delete**](docs/DatabaseServersApi.md#delete) | **DELETE** /api/d6.0/environments/{environment}/databaseServers/{externalDatabaseServer} | Delete an external database server by name
*DatabaseServersApi* | [**get_database_server_usage**](docs/DatabaseServersApi.md#get_database_server_usage) | **GET** /api/d6.0/environments/{environment}/databaseServers/{externalDatabaseServer}/usage | Get an external database server usage by name
*DatabaseServersApi* | [**get_redacted**](docs/DatabaseServersApi.md#get_redacted) | **GET** /api/d6.0/environments/{environment}/databaseServers/{externalDatabaseServer} | Get an external database server by name
*DatabaseServersApi* | [**get_status**](docs/DatabaseServersApi.md#get_status) | **GET** /api/d6.0/environments/{environment}/databaseServers/{externalDatabaseServer}/status | Get an external database server status by name
*DatabaseServersApi* | [**get_template_redacted**](docs/DatabaseServersApi.md#get_template_redacted) | **GET** /api/d6.0/environments/{environment}/databaseServers/{externalDatabaseServer}/template | Get an external database server template by name
*DatabaseServersApi* | [**list**](docs/DatabaseServersApi.md#list) | **GET** /api/d6.0/environments/{environment}/databaseServers | List all externalDatabaseServers
*DatabaseServersApi* | [**update**](docs/DatabaseServersApi.md#update) | **PUT** /api/d6.0/environments/{environment}/databaseServers/{externalDatabaseServer} | Update an existing external database server (unsupported)
*DeploymentsApi* | [**collect_diagnostic_data**](docs/DeploymentsApi.md#collect_diagnostic_data) | **POST** /api/d6.0/environments/{environment}/deployments/{deployment}/diagnosticData | Collects diagnostic data
*DeploymentsApi* | [**create**](docs/DeploymentsApi.md#create) | **POST** /api/d6.0/environments/{environment}/deployments | Create a new deployment
*DeploymentsApi* | [**delete**](docs/DeploymentsApi.md#delete) | **DELETE** /api/d6.0/environments/{environment}/deployments/{deployment} | Delete a deployment by name
*DeploymentsApi* | [**get_redacted**](docs/DeploymentsApi.md#get_redacted) | **GET** /api/d6.0/environments/{environment}/deployments/{deployment} | Get a deployment by name
*DeploymentsApi* | [**get_status**](docs/DeploymentsApi.md#get_status) | **GET** /api/d6.0/environments/{environment}/deployments/{deployment}/status | Get a deployment status by name
*DeploymentsApi* | [**get_template_redacted**](docs/DeploymentsApi.md#get_template_redacted) | **GET** /api/d6.0/environments/{environment}/deployments/{deployment}/template | Get a deployment template by name
*DeploymentsApi* | [**list**](docs/DeploymentsApi.md#list) | **GET** /api/d6.0/environments/{environment}/deployments | List all deployments
*DeploymentsApi* | [**update**](docs/DeploymentsApi.md#update) | **PUT** /api/d6.0/environments/{environment}/deployments/{deployment} | Update an existing deployment template
*DeploymentsApi* | [**update_metering_setting**](docs/DeploymentsApi.md#update_metering_setting) | **PUT** /api/d6.0/environments/{environment}/deployments/{deployment}/metering | Update billing ID for an existing deployment
*EnvironmentsApi* | [**create**](docs/EnvironmentsApi.md#create) | **POST** /api/d6.0/environments | Create a new environment
*EnvironmentsApi* | [**delete**](docs/EnvironmentsApi.md#delete) | **DELETE** /api/d6.0/environments/{name} | Delete an environment by name
*EnvironmentsApi* | [**get_redacted**](docs/EnvironmentsApi.md#get_redacted) | **GET** /api/d6.0/environments/{name} | Get an environment by name
*EnvironmentsApi* | [**list**](docs/EnvironmentsApi.md#list) | **GET** /api/d6.0/environments | List all environments
*EnvironmentsApi* | [**update**](docs/EnvironmentsApi.md#update) | **PUT** /api/d6.0/environments/{name} | Update an existing environment
*EnvironmentsApi* | [**update_provider_credentials**](docs/EnvironmentsApi.md#update_provider_credentials) | **PUT** /api/d6.0/environments/{name}/provider/credentials | Update provider credentials for a specific environment
*EulaApi* | [**get**](docs/EulaApi.md#get) | **GET** /api/d6.0/eula | Get the EULA
*EulaApi* | [**update**](docs/EulaApi.md#update) | **PUT** /api/d6.0/eula | Update the EULA
*ImportClientConfigApi* | [**convert_simple**](docs/ImportClientConfigApi.md#convert_simple) | **POST** /api/d6.0/import/clientConfig/convertSimple | Convert Simple Configuration
*ImportClientConfigApi* | [**import_client_config**](docs/ImportClientConfigApi.md#import_client_config) | **POST** /api/d6.0/import | Import Client Config
*ImportClientConfigApi* | [**validate**](docs/ImportClientConfigApi.md#validate) | **POST** /api/d6.0/import/clientConfig/validate | Validate Client Config
*InstanceTemplatesApi* | [**create**](docs/InstanceTemplatesApi.md#create) | **POST** /api/d6.0/environments/{environment}/templates/instances | Create a new instance template
*InstanceTemplatesApi* | [**delete**](docs/InstanceTemplatesApi.md#delete) | **DELETE** /api/d6.0/environments/{environment}/templates/instances/{template} | Delete an instance template by name
*InstanceTemplatesApi* | [**get**](docs/InstanceTemplatesApi.md#get) | **GET** /api/d6.0/environments/{environment}/templates/instances/{template} | Get an instance template by name
*InstanceTemplatesApi* | [**list**](docs/InstanceTemplatesApi.md#list) | **GET** /api/d6.0/environments/{environment}/templates/instances | List all instance templates
*InstanceTemplatesApi* | [**update**](docs/InstanceTemplatesApi.md#update) | **PUT** /api/d6.0/environments/{environment}/templates/instances/{template} | Update an existing instance template
*NotificationsApi* | [**get**](docs/NotificationsApi.md#get) | **GET** /api/d6.0/notifications | Get system notification messages
*ProviderMetadataApi* | [**get**](docs/ProviderMetadataApi.md#get) | **GET** /api/d6.0/metadata/providers/{providerId} | Get a provider by name
*ProviderMetadataApi* | [**list**](docs/ProviderMetadataApi.md#list) | **GET** /api/d6.0/metadata/providers | List all provider metadata
*ServerConfigApi* | [**get**](docs/ServerConfigApi.md#get) | **GET** /api/d6.0/serverConfigs | Get server configuration
*ServerConfigApi* | [**metadata**](docs/ServerConfigApi.md#metadata) | **GET** /api/d6.0/serverConfigs/metadata | Retrieves the metadata for server configuration
*ServerConfigApi* | [**update_configs**](docs/ServerConfigApi.md#update_configs) | **POST** /api/d6.0/serverConfigs | Get server configuration
*UsersApi* | [**create**](docs/UsersApi.md#create) | **POST** /api/d6.0/users | Create a new user
*UsersApi* | [**current_redacted**](docs/UsersApi.md#current_redacted) | **GET** /api/d6.0/users/current | Get the current user
*UsersApi* | [**delete**](docs/UsersApi.md#delete) | **DELETE** /api/d6.0/users/{username} | Delete a user by username
*UsersApi* | [**get_redacted**](docs/UsersApi.md#get_redacted) | **GET** /api/d6.0/users/{username} | Get a user by username
*UsersApi* | [**get_user_management_status**](docs/UsersApi.md#get_user_management_status) | **GET** /api/d6.0/users/managementStatus | Gets user management status
*UsersApi* | [**list**](docs/UsersApi.md#list) | **GET** /api/d6.0/users | List all users
*UsersApi* | [**update**](docs/UsersApi.md#update) | **PUT** /api/d6.0/users/{username} | Update an existing user
*UsersApi* | [**update_password**](docs/UsersApi.md#update_password) | **PUT** /api/d6.0/users/{username}/password | Update the password of an existing user


## Documentation For Models

 - [Capabilities](docs/Capabilities.md)
 - [CloudProviderMetadata](docs/CloudProviderMetadata.md)
 - [Cluster](docs/Cluster.md)
 - [ClusterAdministrationSettings](docs/ClusterAdministrationSettings.md)
 - [ClusterTemplate](docs/ClusterTemplate.md)
 - [ClusterUpdateEventSummary](docs/ClusterUpdateEventSummary.md)
 - [ConfigurationProperty](docs/ConfigurationProperty.md)
 - [ConfigurationPropertyValue](docs/ConfigurationPropertyValue.md)
 - [Deployment](docs/Deployment.md)
 - [DeploymentTemplate](docs/DeploymentTemplate.md)
 - [DiagnosticDataSummary](docs/DiagnosticDataSummary.md)
 - [DisplayProperty](docs/DisplayProperty.md)
 - [Environment](docs/Environment.md)
 - [ErrorInfo](docs/ErrorInfo.md)
 - [Eula](docs/Eula.md)
 - [ExternalAccount](docs/ExternalAccount.md)
 - [ExternalDatabase](docs/ExternalDatabase.md)
 - [ExternalDatabaseServer](docs/ExternalDatabaseServer.md)
 - [ExternalDatabaseServerTemplate](docs/ExternalDatabaseServerTemplate.md)
 - [ExternalDatabaseServerUsage](docs/ExternalDatabaseServerUsage.md)
 - [ExternalDatabaseTemplate](docs/ExternalDatabaseTemplate.md)
 - [Health](docs/Health.md)
 - [HealthCheck](docs/HealthCheck.md)
 - [ImportResult](docs/ImportResult.md)
 - [ImportStatus](docs/ImportStatus.md)
 - [Instance](docs/Instance.md)
 - [InstanceProviderConfig](docs/InstanceProviderConfig.md)
 - [InstanceState](docs/InstanceState.md)
 - [InstanceTemplate](docs/InstanceTemplate.md)
 - [Login](docs/Login.md)
 - [MeteringSetting](docs/MeteringSetting.md)
 - [Metrics](docs/Metrics.md)
 - [MigratingGroup](docs/MigratingGroup.md)
 - [Migration](docs/Migration.md)
 - [NormalizationConfiguration](docs/NormalizationConfiguration.md)
 - [Notification](docs/Notification.md)
 - [PasswordChange](docs/PasswordChange.md)
 - [ResourceProviderMetadata](docs/ResourceProviderMetadata.md)
 - [Script](docs/Script.md)
 - [Service](docs/Service.md)
 - [SshCredentials](docs/SshCredentials.md)
 - [Status](docs/Status.md)
 - [TimeSeries](docs/TimeSeries.md)
 - [TimeSeriesAggregateStatistics](docs/TimeSeriesAggregateStatistics.md)
 - [TimeSeriesCrossEntityMetadata](docs/TimeSeriesCrossEntityMetadata.md)
 - [TimeSeriesData](docs/TimeSeriesData.md)
 - [TimeSeriesMetadata](docs/TimeSeriesMetadata.md)
 - [TimeSeriesResponse](docs/TimeSeriesResponse.md)
 - [TimeSeriesResponseList](docs/TimeSeriesResponseList.md)
 - [TimeSeriesRow](docs/TimeSeriesRow.md)
 - [User](docs/User.md)
 - [UserManagementStatus](docs/UserManagementStatus.md)
 - [ValidationExceptionCondition](docs/ValidationExceptionCondition.md)
 - [ValidationResult](docs/ValidationResult.md)
 - [ValidationResults](docs/ValidationResults.md)
 - [VirtualInstance](docs/VirtualInstance.md)
 - [VirtualInstanceGroup](docs/VirtualInstanceGroup.md)
 - [WarningInfo](docs/WarningInfo.md)


## Documentation For Authorization


## basic

- **Type**: HTTP basic authentication


## Author

sme-eng-cloud@cloudera.com

