# Environment variables

This section describes environment variables available while using the `qodana-installer-cli` 
utility.

<!-- How can I use these variables? Is it possible to provide a couple of examples? -->

<!-- A small introduction to each kind of variables is probably required -->

## General

| Environment variable                    | Description                                    | Default value                                 |
|-----------------------------------------|------------------------------------------------|-----------------------------------------------|
| `LOG_LEVEL`                             | Application logging level                      | `info`                                        |
| `DOCKER_SWARM_INIT`                     | Whether to initialize Docker Swarm             | `TRUE`                                        |
| `DOCKER_SWARM_ADDRESS_POOL`             | Address pool for Docker Swarm overlay network  | `10.20.0.0/16`                                |
| `DOMAIN`                                | Main domain of the application                 | `qodana.local`                                |
| `INGRESS_SUB_DOMAIN`                    | Subdomain for ingress traffic                  | `ingress`                                     |
| `IDP_SUB_DOMAIN`                        | Subdomain for identity provider (Keycloak)     | `login`                                       |
| `QODANA_DEPENDENCIES_MODE`              | Mode for Qodana dependencies (local or remote) | `local`                                       |
| `CONTAINER_REGISTRY_URL`                | Container registry URL for pulling images      | `quay.io`                                     |
| `DOCKER_SWARM_GC_IMAGE_NAME`            | Docker Swarm garbage collection image name     | `jetbrains/qodana-installer-cli-dependencies` |
| `DOCKER_SWARM_GC_IMAGE_TAG`             | Tag for the Docker GC image                    | `docker-gc-latest`                            |
| `UTILITY_SWISS_KNIFE_IMAGE_NAME`        | Utility Swiss Knife container image name       | `jetbrains/qodana-installer-cli-dependencies` |
| `UTILITY_SWISS_KNIFE_IMAGE_TAG`         | Tag for the Swiss Knife container              | `busybox-1.36.2`                              |

## Databases

| Environment variable            | Description                                     | Default value                                 |
|---------------------------------|-------------------------------------------------|-----------------------------------------------|
| `INGRESS_CONTAINER_NAME`        | Ingress container image name                    | `jetbrains/qodana-installer-cli-dependencies` |
| `INGRESS_CONTAINER_TAG`         | Tag for the ingress container (Traefik version) | `traefik-v3.0`                                |
| `POSTGRES_CONTAINER_IMAGE_NAME` | Postgres container image name                   | `jetbrains/qodana-installer-cli-dependencies` |
| `POSTGRES_CONTAINER_IMAGE_TAG`  | Tag for the Postgres container image            | `postgres-15.10.0`                            |
| `POSTGRES_USER`                 | Default Postgres database user                  | `postgres`                                    |
| `POSTGRES_PASSWORD`             | Password for Postgres user                      | `qodanapassword`                              |
| `DB_HOSTNAME`                   | Hostname for the database                       | `postgres`                                    |
| `DB_PORT`                       | Database port                                   | `5432`                                        |

## MinIO

| Environment variable               | Description                      | Default value                                 |
|------------------------------------|----------------------------------|-----------------------------------------------|
| `MINIO_HOSTNAME`                   | Hostname for Minio               |                                               |
| `MINIO_REGISTRY_IMAGE_NAME`        | MinIO registry image name        | `jetbrains/qodana-installer-cli-dependencies` |
| `MINIO_REGISTRY_IMAGE_TAG`         | Tag for the MinIO registry image | `minio-RELEASE.2025-01-20T14-49-07Z`          |
| `MINIO_CLIENT_REGISTRY_IMAGE_NAME` | MinIO client image name          | `jetbrains/qodana-installer-cli-dependencies` |
| `MINIO_CLIENT_REGISTRY_IMAGE_TAG`  | Tag for the MinIO client image   | `minio-mc-RELEASE.2025-01-17T23-25-50Z`       |
| `MINIO_ROOT_USER`                  | Root user for MinIO instance     | `qodana`                                      |
| `MINIO_ROOT_PASSWORD`              | Root password for MinIO          | `qodanapassword`                              |
| `MINIO_API_PORT`                   | Port for MinIO API service       | `9000`                                        |

## RabbitMQ

| Environment variable                     | Description                         | Default value                                 |
|------------------------------------------|-------------------------------------|-----------------------------------------------|
| `RABBITMQ_REGISTRY_IMAGE_NAME`           | RabbitMQ registry image name        | `jetbrains/qodana-installer-cli-dependencies` |
| `RABBITMQ_REGISTRY_IMAGE_TAG`            | Tag for the RabbitMQ registry image | `rabbitmq-4.0.7`                              |
| `RABBITMQ_HOSTNAME`                      | Hostname for the RabbitMQ service   | `queue.${APP_DOMAIN}`                         |
| `RABBITMQ_PORT`                          | Port for RabbitMQ service           | `5672`                                        |
| `RABBITMQ_VHOST`                         | Virtual host for RabbitMQ           | `/qodana`                                     |

## Keycloak

| Environment variable                | Description                    | Default value                                 |
|-------------------------------------|--------------------------------|-----------------------------------------------|
| `KEYCLOAK_REGISTRY_IMAGE_NAME`      | Keycloak registry image name   | `jetbrains/qodana-installer-cli-dependencies` |
| `KEYCLOAK_REGISTRY_IMAGE_TAG`       | Tag for the Keycloak image     | `keycloak-26.1`                               |
| `KEYCLOAK_HOSTNAME`                 | Hostname for Keycloak instance | `login.${APP_DOMAIN}`                         |
| `KEYCLOAK_DB_NAME`                  | Keycloak database name         | `keycloak`                                    |

## API

| Environment variable                      | Description                              | Default value                                                |
|-------------------------------------------|------------------------------------------|--------------------------------------------------------------|
| `API_MEMORY_LIMIT`                        | Memory limit for API service             | `500`                                                        |
| `API_JAVA_OPTS`                           | Java options for API (optional override) | `-Xmx${APP_API_JAVA_HEAP_LIMIT}m -XX:+PrintCommandLineFlags` |
| `API_POSTGRES_USER`                       | Username for API Postgres database       | `api_user`                                                   |
| `API_POSTGRES_DB_NAME`                    | Name of the API Postgres database        | `qodanadb`                                                   |
| `API_API_ZENDESK_FEEDBACK_EMAIL`          | Zendesk feedback email for API support   | `support@jbs1454063113.zendesk.com`                          |
| `API_LINTERS_VERSION_CI_TEMPLATES`        | Default version for linters CI templates | `2024.2`                                                     |
| `API_ORGANIZATION_NAME`                   | Organization name (optional)             |                                                              |
| `API_LICENSE_ID`                          | License ID for API (optional)            | `NULL`                                                       |

### OAuth

| Environment variable                        |  Description                                |Default value                                                                    |
|---------------------------------------------|---------------------------------------------|---------------------------------------------------------------------------------|
| `API_OAUTH_REDIRECT_URI`                    |  OAuth redirect URI for API                 |`http://${APP_API_HOSTNAME}/api/v1/oauth/callback`                               |
| `API_OAUTH_PROVIDER_BASE_URL`               |  Base URL for OAuth provider                |`http://${APP_KEYCLOAK_HOSTNAME}/realms/qodana/protocol/openid-connect`          |
| `API_OAUTH_AUTHORIZATION_FRONTEND_BASE_URL` |  Authorization frontend URL for OAuth       |`http://${APP_KEYCLOAK_HOSTNAME}/realms/qodana/protocol/openid-connect/auth`     |
| `API_OAUTH_CLIENT_ID`                       |  OAuth client ID                            |`qd-oauth-client`                                                                |
| `API_OAUTH_REQUEST_SCOPES_LIST`             |  List of OAuth request scopes               |`profile,email,openid`                                                           |
| `API_OAUTH_REQUIRED_SCOPES_LIST`            |  Required scopes for OAuth                  |`profile,email,openid`                                                           |
| `API_OAUTH_SERVICE_NAME`                    |  Service name for OAuth provider            |`keycloak`                                                                       |
| `API_OAUTH_USERINFO_URL`                    |  URL to fetch user info from OAuth provider |`http://${APP_KEYCLOAK_HOSTNAME}/realms/qodana/protocol/openid-connect/userinfo` |
| `API_OAUTH_USERINFO_ID_TITLE`               |  User ID field title in OAuth response      |`id`                                                                             |
| `API_OAUTH_EMAIL_TITLE`                     |  Email field title in OAuth response        |`email`                                                                          |
| `API_OAUTH_USER_FULL_NAME_TITLE`            |  Full name field title in OAuth response    |`full_name`                                                                      |
| `API_OAUTH_SAML_ENABLED`                    |  Whether SAML is enabled for OAuth          |`FALSE`                                                                          |
| `API_OAUTH_ROLES_FIELD`                     |  Roles field in OAuth token (if any)        |`NULL`                                                                           |
| `API_OAUTH_REALM_ACCESS_FIELD`              |  Realm access field in OAuth token          |`NULL`                                                                           |
| `API_OAUTH_RESOURCE_ACCESS_FIELD`           |  Resource access field in OAuth token       |`NULL`                                                                           |
| `API_OAUTH_CURRENT_CLIENT_FIELD`            |  Current client field in OAuth token        |`NULL`                                                                           |
| `API_OAUTH_CUSTOM_ROLES_FIELD`              |  Custom roles field in OAuth token          |`NULL`                                                                           |


### GitHub

| Environment variable             |Description                           | Default value                        | 
|----------------------------------|--------------------------------------|--------------------------------------|
| `API_GITHUB_INTEGRATION_ENABLED` |Whether GitHub integration is enabled | `FALSE`                              | 
| `API_GITHUB_HOST_ORIGIN`         |Origin URL for GitHub                 | `https://github.com`                 | 
| `API_GITHUB_APPLICATION_ID`      |GitHub Application ID                 | `NULL`                               | 
| `API_GITHUB_APPLICATION_NAME`    |GitHub Application Name               | `NULL`                               | 
| `API_GITHUB_OAUTH_CLIENT_ID`     |GitHub OAuth Client ID                | `NULL`                               | 

## Memory management

| Environment variable      | Description                           | Default value                                                   |
|---------------------------|---------------------------------------|-----------------------------------------------------------------|
| `AUDIT_MEMORY_LIMIT`      | Memory limit for Audit service        | `500`                                                           |
| `AUDIT_JAVA_OPTS`         | Java options for Audit                | `-Xmx${APP_AUDIT_JAVA_HEAP_LIMIT}m -XX:+PrintCommandLineFlags`  |
| `AUDIT_POSTGRES_USER`     | Username for Audit Postgres database  | `audit_user`                                                    |
| `AUDIT_POSTGRES_DB_NAME`  | Name of the Audit Postgres database   | `audit`                                                         |

## Linter API

<!-- What is Linters API service -->

| Environment variable                        | Description                                         | Default value                                                             |
|---------------------------------------------|-----------------------------------------------------|---------------------------------------------------------------------------|
| `LINTERS_API_MEMORY_LIMIT`                  | Memory limit for Linters API service                | `500`                                                                     |
| `LINTERS_API_JAVA_OPTS`                     | Java options for Linters API                        | `-Xmx${APP_LINTERS_API_JAVA_HEAP_LIMIT}m -XX:+PrintCommandLineFlags`      |
| `LINTERS_API_POSTGRES_USER`                 | Username for Linters API Postgres database          | `linters_api_user`                                                        |
| `LINTERS_API_POSTGRES_DB_NAME`              | Name of the Linters API Postgres database           | `qodanadb`                                                                |
| `GIT_MEMORY_LIMIT`                          | Memory limit for Git Service                        | `500`                                                                     |
| `GIT_JAVA_OPTS`                             | Java options for Git Service                        | `-Xmx${APP_GIT_JAVA_HEAP_LIMIT}m -XX:+PrintCommandLineFlags`              |
| `GIT_POSTGRES_USER`                         | Username for Git Postgres database                  | `git_user`                                                                |
| `GIT_POSTGRES_DB_NAME`                      | Name of the Git Postgres database                   | `git`                                                                     |
| `GIT_PROBE_TIMEOUT_SECONDS`                 | Timeout for Git probe checks                        | `5`                                                                       |
| `REPORT_PROCESSOR_MEMORY_LIMIT`             | Memory limit for the Report Processor service       | `500`                                                                     |
| `REPORT_PROCESSOR_JAVA_OPTS`                | Java options for the Report Processor               | `-Xmx${APP_REPORT_PROCESSOR_JAVA_HEAP_LIMIT}m -XX:+PrintCommandLineFlags` |
| `REPORT_PROCESSOR_POSTGRES_USER`            | Username for Report Processor Postgres database     | `report_processor_user`                                                   |
| `REPORT_PROCESSOR_POSTGRES_DB_NAME`         | Name of the Report Processor Postgres database      | `qodanadb`                                                                |
| `FUS_MEMORY_LIMIT`                          | Memory limit for FUS service                        | `500`                                                                     |
| `FUS_JAVA_OPTS`                             | Java options for FUS                                | `-Xmx${APP_FUS_JAVA_HEAP_LIMIT}m -XX:+PrintCommandLineFlags`              |
| `FUS_INTERNAL`                              | Whether FUS is internal only                        | `FALSE`                                                                   |
| `FUS_CONFIGURATION_ENDPOINT`                | Endpoint URL for FUS configuration                  | `https://resources.jetbrains.com/storage/fus/config/v4/QD/QDCLD.json`     |
| `FRONTEND_MEMORY_LIMIT`                     | Memory limit for Frontend service                   | `500`                                                                     |
| `MINIO_RESULTS_BUCKET`                      | Bucket name for storing Qodana results              | `qc-results`                                                              |
| `MINIO_BASELINES_BUCKET`                    | Bucket name for storing Qodana baselines            | `qc-baselines`                                                            |
| `MINIO_PRESIGNED_URL_EXPIRATION_IN_MINUTES` | Expiration time for MinIO presigned URLs in minutes | `120`                                                                     |
| `OBJECT_STORAGE_PROVIDER`                   | Object storage provider type                        | `minio`                                                                   |
| `MESSAGE_BROKER_PROVIDER`                   | Message broker provider (RabbitMQ)                  | `rabbitmq`                                                                |
| `RABBITMQ_REPORTS_QUEUE_NAME`               | Queue name for Qodana reports                       | `qodanaCloudQueue`                                                        |

## Git queue

<!-- A brief explanation is probably required here -->

| Environment variable                                        | Description                                         | Default value                        |
|-------------------------------------------------------------|-----------------------------------------------------|--------------------------------------|
| `GIT_RABBITMQ_CONTRIBUTORS_REQUEST_QUEUE_NAME`              | Queue name for Git contributors request             | `qodanaGetContributorsRequestQueue`  |
| `GIT_RABBITMQ_CONTRIBUTORS_RESPONSE_QUEUE_NAME`             | Queue name for Git contributors response            | `qodanaGetContributorsResponseQueue` |
| `GIT_RABBITMQ_CONTRIBUTORS_RESPONSE_WAIT_TIME`              | Wait time for contributors' responses               | `20`                                 |
| `GIT_RABBITMQ_CONTRIBUTORS_RESPONSE_MAX_NUMBER_OF_MESSAGES` | Max number of messages for contributors' responses  | `10`                                 |
| `GIT_RABBITMQ_CONTRIBUTORS_RESPONSE_WORKERS_NUM`            | Number of workers for contributors' responses       | `20`                                 |
| `GIT_RABBITMQ_TRIGGERS_QUEUE_NAME`                          | Queue name for Git triggers                         | `qodanaGitTriggersQueue`             |
| `GIT_RABBITMQ_TRIGGERS_WAIT_TIME`                           | Wait time for Git triggers                          | `20`                                 |
| `GIT_RABBITMQ_TRIGGERS_MAX_NUMBER_OF_MESSAGES`              | Max number of messages for Git triggers             | `10`                                 |
| `GIT_RABBITMQ_TRIGGERS_WORKERS_NUM`                         | Number of workers for Git triggers                  | `1`                                  |
