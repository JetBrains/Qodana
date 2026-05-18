# Docker configuration

<show-structure for="chapter" depth="3"/>

The `qodana-installer-cli` command-line tool is a Docker container that manages the lifecycle of %premlite%. 

This tool orchestrates Docker Swarm stacks for:

* Infrastructure services: PostgreSQL, MinIO, RabbitMQ, Keycloak
* Application services: API, Audit, Git, Linters API, Report Processor, FUS, Frontend
* Supporting tools: Traefik ingress proxy, image garbage collector

## Prepare your project

### Docker

The container should be given access to the Docker socket:

```text
-v /var/run/docker.sock:/var/run/docker.sock
```

You should have permission to the `/var/run/docker.sock` resource, i.e. your user should be part  the `docker` group on the host.

Port 80 on the host should be open for the Traefik ingress proxy to bind to it in host-network mode.

### Networking

<!-- WHAT DOES THIS MEAN?  -->
All service hostnames should resolve the IP address of the Swarm manager node. You can achieve this via:

- An internal DNS server that covers `*.<DOMAIN>`
- Manual `/etc/hosts` entries on every machine that should have access to %product%

See the [](#Domain+name+system+%28DNS%29) chapter for the full list of hostnames and their setup.

### Domain name system (DNS)

<!-- How can they be allocated in this case  -->
<!-- Where are these variables applied?  -->

<p>%premlite% exposes different HTTP endpoints as base URLs. Make sure to allocate a top-level domain like <code>qodana.local</code>.
    The majority of %premlite% components require dedicated base URLs, for example:</p>
<table>
    <tr>
        <td>Component</td>
        <td>URL</td>
    </tr>
    <tr>
        <td>Frontend (web UI)</td>
        <td><code>qodana.local</code></td>
    </tr>
    <tr>
        <td>Backend (API gateway)</td>
        <td><code>api.qodana.local</code></td>
    </tr>
    <tr>
        <td>Linter API</td>
        <td><code>lintersapi.qodana.local</code></td>
    </tr>
    <tr>
        <td>Built-in file storage (MinIO)</td>
        <td><code>files.qodana.local</code></td>
    </tr>
    <tr>
        <td>Built-in SSO provider (Keycloak)</td>
        <td><code>login.qodana.local</code></td>
    </tr>
    <tr>
        <td>Built-in ingress controller (Traefik)</td>
        <td><code>ingress.qodana.local</code></td>
    </tr>
</table>

<!-- This is inconsistent here  -->
<p>These hostnames enable interaction of %product% components and access to essential services.
services. The IP can be of your server or a load balancer, depending on your deployment architecture. </p>

In production environments, you should use a domain that aligns with your naming conventions like `qodana.mycompany.com`,
`files.qodana.mycompany.com` and others.

<!-- This needs to be described and detalized  -->

If you intend to use %product% only internally, configure DNS records in your internal DNS server. For external access,
ensure that public DNS records point to appropriate IP addresses of your server or load balancer.

### PostgreSQL

#### Databases

%premlite% operates multiple services with each service requiring their own database:


<!-- Where are they used  -->

| Database           | Description                                                                 | Variable             |
|--------------------|-----------------------------------------------------------------------------|----------------------|
| API Database       | Stores data related to Qodana’s API                                         | `${API_DATABASE}`    |
| Git Database       | Manages repositories and version control data                               | `${GIT_DATABASE}`    |
| Audit Database     | Handles audit logs and compliance data                                      | `${AUDIT_DATABASE}`  |
| Keycloak Database  | Optional. Used for authentication and authorization services like Keycloak  | `${APP_KC_DB_NAME}`  |

#### Users and roles

Each service requires a dedicated PostgreSQL user for having access to its corresponding database. These users are
assigned specific permissions to ensure security and proper data isolation:

<table>
    <tr>
        <td>Database</td>
        <td>Description</td>
        <td>Variable</td>
    </tr>
    <tr>
        <td>API User</td>
        <td>Read/write permissions for the API database</td>
        <td><code>${API_USER_NAME}</code></td>
    </tr>
    <tr>
        <td>Linters API User</td>
        <td>Read-only permissions for certain tables</td>
        <td><code>${LINTERS_API_USER_NAME}</code></td>
    </tr>
    <tr>
        <td>Report Processor User</td>
        <td>Read/write permissions for processing reports</td>
        <td><code>${REPORT_PROCESSOR_USER_NAME}</code></td>
    </tr>
    <tr>
        <td>Git User</td>
        <td>Full permissions for Git-related data</td>
        <td><code>${GIT_USER_NAME}</code></td>
    </tr>
    <tr>
        <td>Audit User</td>
        <td>Full permissions for audit logs</td>
        <td><code>${AUDIT_USER_NAME}</code></td>
    </tr>
    <tr>
        <td>Keycloak User</td>
        <td>Optional. Full ownership and permissions for the Keycloak database</td>
        <td><code>${APP_KC_DB_USER}</code></td>
    </tr>
</table>

#### Permissions

The following permission rules are applied to ensure proper access control:

* Users are granted access only to their respective databases.
* Default privileges are configured so that users automatically receive permissions on newly created objects like tables, sequences, and functions.
* Sensitive databases like an audit database are strictly controlled to prevent unauthorized access.

#### Database organization

Each Qodana service (API, Git, Audit, Keycloak) should have its own database. This prevents data corruption, unauthorized access
between services, and lets you tune each database better to your needs.

Databases can be hosted on a single server or on different servers. A shared server is suitable for small-scale deployments
with low traffic and minimal resource requirements. Separate servers are best suited for large-scale deployments or when
handling highly sensitive data like audit logs or authentication.

#### Security and compliance

Use strong, randomly generated passwords for all database users. Store credentials securely, such as in an environment
variable manager or secret storage like HashiCorp Vault and others.

Restrict permissions to ensure users can only access their assigned databases. Avoid granting superuser or unnecessary privileges.

Enable logging for database activity to monitor access and changes, especially for the audit database.

#### Backup and recovery

Implement a robust backup and recovery plan:
* Schedule regular automated backups for all databases.
* Test restoration processes regularly to ensure reliability.
* For critical data like audit logs and Keycloak, use frequent point-in-time recovery backups.

#### Monitoring and maintenance

Use PostgreSQL monitoring tools like pgAdmin, Prometheus, or other to track database performance and health.

Periodically review database usage and clean up unused objects. Apply security updates and patches for PostgreSQL.

#### Example SQL script for a single database server setup

This snippet contains an example script that documents the instructions for configuring a single database server for
%premlite%. The script references environment variables instead of hard coded values. The Keycloak database and user
permissions configuration are optional. They are documented in the script if you plan to use Keycloak as an identity provider.

```Bash
#!/usr/bin/env bash
set -o errexit
set -o pipefail
set -o nounset
export PGPASSWORD="${POSTGRESQL_PASSWORD}"
psql -U "${POSTGRESQL_USERNAME}" <<-END
   -- Create databases and database roles for application services
   CREATE DATABASE ${API_DATABASE};
   CREATE DATABASE ${GIT_DATABASE};
   CREATE DATABASE ${AUDIT_DATABASE};
   CREATE DATABASE ${APP_KC_DB_NAME};

   CREATE USER ${API_USER_NAME} WITH PASSWORD '${API_USER_PASSWORD}';
   CREATE USER ${LINTERS_API_USER_NAME} WITH PASSWORD '${LINTERS_API_USER_PASSWORD}';
   CREATE USER ${REPORT_PROCESSOR_USER_NAME} WITH PASSWORD '${REPORT_PROCESSOR_USER_PASSWORD}';
   CREATE USER ${GIT_USER_NAME} WITH PASSWORD '${GIT_USER_PASSWORD}';
   CREATE USER ${AUDIT_USER_NAME} WITH PASSWORD '${AUDIT_USER_PASSWORD}';
   CREATE USER ${APP_KC_DB_USER} WITH PASSWORD '${APP_KC_DB_PASSWORD}';

   -- Switch to the qodanadb database and grant access right to schema and existing objects
   \c ${API_DATABASE};

   GRANT CREATE,USAGE ON SCHEMA public TO ${API_USER_NAME};
   GRANT SELECT,INSERT,UPDATE,DELETE,TRUNCATE,REFERENCES,TRIGGER ON ALL TABLES IN SCHEMA public TO ${API_USER_NAME};
   GRANT SELECT,USAGE ON ALL SEQUENCES IN SCHEMA public to ${API_USER_NAME};

   -- Grant default privileges on future tables to api database user
   ALTER DEFAULT PRIVILEGES IN SCHEMA public
       GRANT SELECT,INSERT,UPDATE,DELETE,TRUNCATE,REFERENCES,TRIGGER ON TABLES TO ${API_USER_NAME};
   ALTER DEFAULT PRIVILEGES IN SCHEMA public
       GRANT SELECT,USAGE ON SEQUENCES TO ${API_USER_NAME};

   GRANT CREATE,USAGE ON SCHEMA public TO ${REPORT_PROCESSOR_USER_NAME};
   GRANT SELECT,INSERT,UPDATE,DELETE,TRUNCATE,REFERENCES,TRIGGER ON ALL TABLES IN SCHEMA public TO ${REPORT_PROCESSOR_USER_NAME};
   GRANT SELECT,USAGE ON ALL SEQUENCES IN SCHEMA public to ${REPORT_PROCESSOR_USER_NAME};

   -- Grant default privileges on future tables to report-processor database user
   ALTER DEFAULT PRIVILEGES IN SCHEMA public
       GRANT SELECT,INSERT,UPDATE,DELETE,TRUNCATE,REFERENCES,TRIGGER ON TABLES TO ${REPORT_PROCESSOR_USER_NAME};
   ALTER DEFAULT PRIVILEGES IN SCHEMA public
       GRANT SELECT,USAGE ON SEQUENCES TO ${REPORT_PROCESSOR_USER_NAME};

   GRANT CREATE,USAGE ON SCHEMA public TO ${LINTERS_API_USER_NAME};
   GRANT SELECT ON ALL TABLES IN SCHEMA public TO ${LINTERS_API_USER_NAME};
   GRANT SELECT,USAGE ON ALL SEQUENCES IN SCHEMA public to ${LINTERS_API_USER_NAME};

   -- Grant default privileges on future tables to linters-api database user
   ALTER DEFAULT PRIVILEGES IN SCHEMA public
       GRANT SELECT ON TABLES TO ${LINTERS_API_USER_NAME};
   ALTER DEFAULT PRIVILEGES IN SCHEMA public
       GRANT SELECT,USAGE ON SEQUENCES TO ${LINTERS_API_USER_NAME};

   -- Switch to the git database and grant access right to schema and existing objects
   \c ${GIT_DATABASE};

   GRANT CREATE,USAGE ON SCHEMA public TO ${GIT_USER_NAME};
   GRANT SELECT,INSERT,UPDATE,DELETE,TRUNCATE,REFERENCES,TRIGGER ON ALL TABLES IN SCHEMA public TO ${GIT_USER_NAME};
   GRANT SELECT,USAGE ON ALL SEQUENCES IN SCHEMA public to ${GIT_USER_NAME};

   -- Grant default privileges on future tables to git database user
   ALTER DEFAULT PRIVILEGES IN SCHEMA public
       GRANT SELECT,INSERT,UPDATE,DELETE,TRUNCATE,REFERENCES,TRIGGER ON TABLES TO ${GIT_USER_NAME};
   ALTER DEFAULT PRIVILEGES IN SCHEMA public
       GRANT SELECT,USAGE ON SEQUENCES TO ${GIT_USER_NAME};

   -- Switch to the audit database and grant access right to schema and existing objects
   \c ${AUDIT_DATABASE};

   GRANT CREATE,USAGE ON SCHEMA public TO ${AUDIT_USER_NAME};
   GRANT SELECT,INSERT,UPDATE,DELETE,TRUNCATE,REFERENCES,TRIGGER ON ALL TABLES IN SCHEMA public TO ${AUDIT_USER_NAME};
   GRANT SELECT,USAGE ON ALL SEQUENCES IN SCHEMA public to ${AUDIT_USER_NAME};

   -- Grant default privileges on future tables to audit database user
   ALTER DEFAULT PRIVILEGES IN SCHEMA public
       GRANT SELECT,INSERT,UPDATE,DELETE,TRUNCATE,REFERENCES,TRIGGER ON TABLES TO ${AUDIT_USER_NAME};
   ALTER DEFAULT PRIVILEGES IN SCHEMA public
       GRANT SELECT,USAGE ON SEQUENCES TO ${AUDIT_USER_NAME};

   \c ${APP_KC_DB_NAME};

   GRANT ALL PRIVILEGES ON DATABASE ${APP_KC_DB_NAME} TO ${APP_KC_DB_USER};
   GRANT CREATE,USAGE ON SCHEMA public TO ${APP_KC_DB_USER};
   GRANT SELECT,INSERT,UPDATE,DELETE,TRUNCATE,REFERENCES,TRIGGER ON ALL TABLES IN SCHEMA public TO ${APP_KC_DB_USER};
   GRANT SELECT,USAGE ON ALL SEQUENCES IN SCHEMA public to ${APP_KC_DB_USER};

   -- Grant default privileges on future tables, sequences, and functions to the Keycloak user
   ALTER DEFAULT PRIVILEGES IN SCHEMA public
       GRANT ALL PRIVILEGES ON TABLES TO ${APP_KC_DB_USER};
   ALTER DEFAULT PRIVILEGES IN SCHEMA public
       GRANT ALL PRIVILEGES ON SEQUENCES TO ${APP_KC_DB_USER};
   ALTER DEFAULT PRIVILEGES IN SCHEMA public
       GRANT ALL PRIVILEGES ON FUNCTIONS TO ${APP_KC_DB_USER};
END
```
{collapsible="true"}

### RabbitMQ
{id="docker-configuration-prepare-project-rabbitmq"}

RabbitMQ acts as a message broker for various %product% services facilitating communication and task processing.

#### Virtual hosts

Each %product% instance requires a dedicated virtual host to isolate messaging operations from other applications.
Define a virtual host using the environment variable: `${RABBITMQ_VHOST}`. Example: `/qodana`

#### Users

A dedicated RabbitMQ user is required by Qodana for authenticating and performing operations on a virtual host. Create a
user with the following parameters:

| Parameter | Description                                        |
|-----------|----------------------------------------------------|
| Username  | `${APP_RABBITMQ_APPLICATION_USERNAME};`            |
| Password  | `${APP_RABBITMQ_APPLICATION_PASSWORD};`            |
| Tags      | Assign the administrator tag to grant full access  |


Example:
```JSON
{
  "name": "qodana_user",
  "password": "secure_password",
  "tags": "administrator"
}
```

#### Queues

%product% requires several durable queues for handling messaging related to reports, Git operations, and triggers. Create
the following queues within the `${RABBITMQ_VHOST}` variable:

| Description                    | Name                                                | Example                              |
|--------------------------------|-----------------------------------------------------|--------------------------------------|
| Report queue                   | `${RABBITMQ_REPORTS_QUEUE_NAME};`                   | `qodanaCloudQueue`                   |
| Git contributor request queue  | `${GIT_RABBITMQ_CONTRIBUTORS_REQUEST_QUEUE_NAME};`  | `qodanaGetContributorsRequestQueue`  |
| Git contributor response queue | `${GIT_RABBITMQ_CONTRIBUTORS_RESPONSE_QUEUE_NAME};` | `qodanaGetContributorsResponseQueue` |
| Trigger queue                  | `${GIT_RABBITMQ_TRIGGERS_QUEUE_NAME};`              | `qodanaGitTriggersQueue`             |

All queues must be durable to ensure message persistence in case of RabbitMQ restarts.

#### Permissions
{id="rabbitmq-permissions"}

Define access permissions for the Qodana user to operate within the vhost. Grant the following permissions to
the `${RABBITMQ_APPLICATION_USERNAME}` variable for the  `${RABBITMQ_VHOST}` variable:

| Permission | Configuration | Description                            |
|------------|---------------|----------------------------------------|
| Configure  | `.*`          | Enables configuration of all resources |
| Write      | `.*`          | Enables publishing to all queues       |
| Read       | `.*`          | Enables consuming from all queues      |

This is an example configuration in JSON:

```JSON
{ 
  "user": "qodana_user", 
  "vhost": "/qodana", 
  "configure": ".*", 
  "write": ".*", 
  "read": ".*" 
}
```

#### Example definition in JSON

This is and example RabbitMQ configuration. For more details, see visit the
[RabbitMQ website](https://www.rabbitmq.com/docs/definitions#import).

```JSON
{
 "vhosts": [
   {
     "name": "${RABBITMQ_VHOST}"
   }
 ],
 "users": [
   {
     "name": "${RABBITMQ_APPLICATION_USERNAME}",
     "password": "${RABBITMQ_APPLICATION_PASSWORD}",
     "tags": "administrator"
   }
 ],
 "queues": [
   {
     "name": "${RABBITMQ_REPORTS_QUEUE_NAME}",
     "durable": true,
     "vhost": "${RABBITMQ_VHOST}"
   },
   {
     "name": "${GIT_RABBITMQ_CONTRIBUTORS_REQUEST_QUEUE_NAME}",
     "durable": true,
     "vhost": "${RABBITMQ_VHOST}"
   },
   {
     "name": "${GIT_RABBITMQ_CONTRIBUTORS_RESPONSE_QUEUE_NAME}",
     "durable": true,
     "vhost": "${RABBITMQ_VHOST}"
   },
   {
     "name": "${GIT_RABBITMQ_TRIGGERS_QUEUE_NAME}",
     "durable": true,
     "vhost": "${RABBITMQ_VHOST}"
   }
 ],
 "permissions": [
   {
     "user": "${RABBITMQ_APPLICATION_USERNAME}",
     "vhost": "${RABBITMQ_VHOST}",
     "configure": ".*",
     "write": ".*",
     "read": ".*"
   }
 ]
}
```
{collapsible="true"}

### MinIO
{id="docker-configuration-prepare-project-minio"}

%premlite% supports MinIO for object storage. %product% requires pre-signed URLs,
which lets %product% clients connect directly to a storage and upload artifacts for asynchronous processing or storage purposes.

%premlite% requires the `MINIO_RESULTS_BUCKET` and `MINIO_BASELINES_BUCKET` buckets, and they should be hosted on the
same storage service.

### OIDC provider

%premlite% does not provide a built-in user management module, so users should authenticate using an OIDC provider.
%premlite% authorizes their actions according to permissions given to a specific user by an administrator.

To get assistance with configuring an OIDC provider, please contact our support at <code>qodana-support@jetbrains.com</code>.

## Run Qodana Self-Hosted

Assuming that requirements from the [](shl-introduction.md) and [](#Prepare+your+project) chapters are satisfied, pull the
`quay.io/jetbrains/qodana-installer-cli:latest` Docker image. All commands running this image require the
`/var/run/docker.sock` Docker socket file for communicating with the Docker engine and Docker Swarm.

> The list of commands is available in the [](#Docker+commands) chapter.

### Basic use case

Follow the steps below for installing %premlite% on your machine:

<procedure>
    <step>
        <p>On your local Linux machine, configure the <code>/etc/hosts</code> file as shown below:</p>
        <code-block lang="text">
            # Added for Qodana Self-Hosted Version
            127.0.0.1 qodana.local
            127.0.0.1 files.qodana.local
            127.0.0.1 api.qodana.local
            127.0.0.1 ingress.qodana.local
            127.0.0.1 login.qodana.local
            127.0.0.1 lintersapi.qodana.local
        </code-block>
    </step>
    <step>
        <p>On your local machine, run the following Docker command:</p>
        <code-block lang="Bash" prompt="$">
            docker run \
                -v /var/run/docker.sock:/var/run/docker.sock \
                -e API_ORGANIZATION_NAME="&lt;Specify the name of your organization&gt;" \
                -e COMMON_LICENSE_KEY_SECRET="&lt;Specify a valid license key&gt;" \ 
                quay.io/jetbrains/qodana-installer-cli:latest \
                install-app
        </code-block>
    </step>
</procedure>

In your browser, navigate to `http://qodana.local` to receive access to %premlite%.

By default, %premlite% comes configured with local dependencies for quick Proofs Of Concepts (PoCs) or Proofs of Value (PoV).
The credentials for a built-in administrator test user are as follows:

|Credential | Value               |
|-----------|---------------------|
|Username | `tser@qodana.local` |
|Password | `@wesomeQodana`     |

You can update these credentials by navigating to the `http://login.qodana.local` page.

### Use configuration from file

Run the following Docker command to use a configuration contained in a file:

```Bash
docker run 
    -v /var/run/docker.sock:/var/run/docker.sock \ 
    -e API_ORGANIZATION_NAME="<Specify the name of your organization>" \
    -e COMMON_LICENSE_KEY_SECRET="<Specify a valid license key>" \ 
    --env-file qodana-self-hosted.env \
    quay.io/jetbrains/qodana-installer-cli:latest 
    install-app
```
{prompt="$"}

This command uses the `--env-file` option to specify the path to the configuration file, in this case this is the
`qodana-self-hosted.env` file.

### Persist secrets

This command lets you export and persist secrets created during installation in the `${PWD}/secrets` directory:

```Bash
docker run \
    -v /var/run/docker.sock:/var/run/docker.sock \ 
    -v ${PWD}/secrets:/app/qodana-installer/secrets \
    -e API_ORGANIZATION_NAME="<Specify the name of your organization>" \
    -e COMMON_LICENSE_KEY_SECRET="<Specify a valid license key>" \ 
    quay.io/jetbrains/qodana-installer-cli:latest \
    install-app
```
{prompt="$"}

To make the secret idempotent, this command mounts the `/app/qodana-installer/secrets` directory for storing secrets.

## Docker commands

Here is an overview of commands available for the Dockerized version of %premlite%.

<table>
    <tr>
        <td>Command</td>
        <td>Description</td>
        <td>Examples</td>
    </tr>
    <tr>
        <td><code>backup</code></td>
        <td>Create a compressed backup of all local data</td>
        <td><!-- What is going on here after the command is run? -->
            <code-block lang="bash" prompt="$">
                docker run \
                  -v /var/run/docker.sock:/var/run/docker.sock \ 
                  quay.io/jetbrains/qodana-installer-cli:latest \
                  backup
            </code-block>
        </td>
    </tr>
    <tr>
        <td><code>credentials</code></td>
        <td>Retrieve credentials for any infrastructure component</td>
        <td>
            <code-block lang="bash" prompt="$">
                docker run \
                  -v /var/run/docker.sock:/var/run/docker.sock \ 
                  quay.io/jetbrains/qodana-installer-cli:latest \
                  credentials
            </code-block>
        </td>
    </tr>
    <tr>
        <td><code>environment</code></td>
        <td>Display all active configurations passed or used by %premlite%</td>
        <td>
            <code-block lang="bash" prompt="$">
                docker run \
                  -v /var/run/docker.sock:/var/run/docker.sock \ 
                  quay.io/jetbrains/qodana-installer-cli:latest \
                  environment
            </code-block></td>
    </tr>
    <tr>
        <td><code>help</code></td>
        <td>Help for %premlite%</td>
        <td>
            <code-block lang="bash" prompt="$">
                docker run \
                  -v /var/run/docker.sock:/var/run/docker.sock \ 
                  quay.io/jetbrains/qodana-installer-cli:latest \
                  help
            </code-block></td>
    </tr>
    <tr>
        <td><code>install-app</code></td>
        <td>Deploy %premlite% on your machine</td>
        <td>
            <code-block lang="bash" prompt="$">
                docker run \
                  -v /var/run/docker.sock:/var/run/docker.sock \
                  -e API_ORGANIZATION_NAME="&lt;Specify the name of your organization&gt;" \
                  -e COMMON_LICENSE_KEY_SECRET="&lt;Specify a valid license key&gt;" \ 
                  quay.io/jetbrains/qodana-installer-cli:latest \
                  install-app
            </code-block></td>
    </tr>
    <tr>
        <td><code>logs</code></td>
        <td>Retrieve log entries from %premlite% services</td>
        <td>
            <code-block lang="bash" prompt="$">
                docker run \
                  -v /var/run/docker.sock:/var/run/docker.sock \ 
                  quay.io/jetbrains/qodana-installer-cli:latest 
                  logs
            </code-block>
<p>You can filter log output using the <code>--filters</code> parameter and labels described in the <a anchor="Labels+and+environment+variables"/> chapter and
separated by a space character, for example:</p>
            <code-block lang="bash" prompt="$">
                docker run \ 
                  -v /var/run/docker.sock:/var/run/docker.sock \ 
                  quay.io/jetbrains/qodana-installer-cli:latest \ 
                  logs \
                  --filters "label=com.docker.stack.namespace=qodana_self_hosted_services label=qodana.jetbrains.self-hosted.lite.service-type=application"
            </code-block>
        </td>
    </tr>
    <tr>
        <td><code>restore</code></td>
        <td>Restore data from a backup file</td>
        <td>
            <code-block lang="bash" prompt="$">
                docker run \
                  -v /var/run/docker.sock:/var/run/docker.sock \ 
                  quay.io/jetbrains/qodana-installer-cli:latest 
                  logs
            </code-block></td>
    </tr>
    <tr>
        <td><code>uninstall</code></td>
        <td>Uninstall %premlite% from your machine</td>
        <td>
            <code-block lang="bash" prompt="$">
                docker run \
                  -v /var/run/docker.sock:/var/run/docker.sock \ 
                  quay.io/jetbrains/qodana-installer-cli:latest \
                  uninstall
            </code-block>
        <p>To remove Docker volumes of %premlite%, run the following command:</p>
            <code-block lang="bash" prompt="$">
                echo "[INFO] Cleaning the Docker volumes" && docker volume ls \
                  --filter "label=qodana.jetbrains.self-hosted.lite.dependencies.local=true" \
                  --quiet | xargs -r docker volume rm
            </code-block>
        <p>To delete persisting secrets from your machine located in the <code>${PWD}/secrets</code> directory, 
        run this command:</p>
            <code-block lang="bash" prompt="$">
                echo "[INFO] Cleaning the local secrets directory" && rm -rf ${PWD}/secrets
            </code-block>
        </td>
    </tr>
</table>


## Labels and environment variables

### Global labels

%premlite% uses several global labels to mark the resources it owns and manages. You can use these labels to operate
%premlite%:

| Label and value                                                                  | Description                                                                                                                                 |
|----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| `qodana.jetbrains.self-hosted.lite.select=true`                                  | Identify all resources that are part of the %premlite% installation                                                                         |
| `qodana.jetbrains.self-hosted.lite.version=${APP_QODANA_SELF_HOSTED_IMAGE_TAG}`  | Display at runtime a %premlite% version that a specific resouce is related to. Dependent on the `APP_QODANA_SELF_HOSTED_IMAGE_TAG` variable |


### Component-specific labels

%premlite% is operated by several services. To simplify administration, they are combined into the following groups:

| Group name           | Description                                                |
|----------------------|------------------------------------------------------------|
| `local-dependencies` | Stateful components                                        |
| `application`        | %product% API, %product% Git API, linter API and others    |
| `supporting-tools`   | Ingress and garbage collection of Docker images and others |

Here, each group identifies a specific Docker Swarm stack.

#### Labels related to local dependencies

The `qodana.jetbrains.self-hosted.lite.dependencies.local=true` and `qodana.jetbrains.self-hosted.lite.service-type=local-dependencies`
labels identify resources related to the `qodana_self_hosted_local_dependencies` stack or group.

The `qodana.jetbrains.self-hosted.lite.database.volume.name` label defines the internal name of a volume that will be
mapped to a related stateful service that is part of a certain Docker stack.

You can find out the volume name for a given container using this Docker CLI command:

```Bash
docker inspect <containerid> \
  --format "{{ range .HostConfig.Mounts }}{{ json .VolumeOptions.Labels }}{{end}}"
```
{prompt="$"}

To understand the mount point of a specific Docker volume, you can use the
`qodana.jetbrains.self-hosted.lite.database.volume.path` label.

#### Labels related to %premlite%

The `qodana.jetbrains.self-hosted.lite.service-type=application` label identifies the resources related to the
`qodana_self_hosted_local_service_tools` stack.

<!-- What are the supporting tools here ? -->

#### Label related to supporting tools

The `qodana.jetbrains.self-hosted.lite.service-type=supporting-tools` label identifies the resources related to the
`qodana_self_hosted_local_service_tools` stack.

### Environment variables

#### Product
{id="product"}

##### General
{id="product-general"}

| Environment variable                | Description                                    | Default value                                 |
|-------------------------------------|------------------------------------------------|-----------------------------------------------|
| `DOMAIN`                            | Main domain of the application                 | `qodana.local`                                |
| `LOG_LEVEL`                         | Application logging level                      | `info`                                        |
| `IDP_SUB_DOMAIN`                    | Subdomain for identity provider (Keycloak)     | `login`                                       |
| `CONTAINER_REGISTRY_URL`            | Container registry URL for pulling images      | `quay.io`                                     |
| `QODANA_DEPENDENCIES_MODE`          | Mode for Qodana dependencies (local or remote) | `local`                                       |
| `APP_QODANA_SELF_HOSTED_IMAGE_TAG`  | Current version of %premlite%                  | `1.22.0-alpha.14`, actual for July 2025       |
| `FRONTEND_MEMORY_LIMIT`                     | Memory limit for Frontend service                   | `500`                                                                     |
| `OBJECT_STORAGE_PROVIDER`                   | Object storage provider type                        | `minio`                                                                   |
| `MESSAGE_BROKER_PROVIDER`                   | Message broker provider (RabbitMQ)                  | `rabbitmq`                                                                |

##### FUS
{id="product-fus"}

Variables used for statistics collection and processing.

| Environment variable         | Description                                    | Default value                                 |
|------------------------------|------------------------------------------------|-----------------------------------------------|
| `FUS_MEMORY_LIMIT`           | Memory limit for FUS service                        | `500`                                                                     |
| `FUS_JAVA_OPTS`              | Java options for FUS                                | `-Xmx${APP_FUS_JAVA_HEAP_LIMIT}m -XX:+PrintCommandLineFlags`              |
| `FUS_INTERNAL`               | Whether FUS is internal only                        | `FALSE`                                                                   |
| `FUS_CONFIGURATION_ENDPOINT` | Endpoint URL for FUS configuration                  | `https://resources.jetbrains.com/storage/fus/config/v4/QD/QDCLD.json`     |

#### Linter API

Linter API validates linters and checks for versions of supported linters and plugins.

##### General
{id="linter-api-general"}

| Environment variable                        | Description                                         | Default value                                                             |
|---------------------------------------------|-----------------------------------------------------|---------------------------------------------------------------------------|
| `LINTERS_API_MEMORY_LIMIT`                  | Memory limit for Linters API service                | `500`                                                                     |
| `LINTERS_API_JAVA_OPTS`                     | Java options for Linters API                        | `-Xmx${APP_LINTERS_API_JAVA_HEAP_LIMIT}m -XX:+PrintCommandLineFlags`      |
| `LINTERS_API_POSTGRES_USER`                 | Username for Linters API Postgres database          | `linters_api_user`                                                        |
| `LINTERS_API_POSTGRES_DB_NAME`              | Name of the Linters API Postgres database           | `qodanadb`                                                                |
| `API_MEMORY_LIMIT`                        | Memory limit for API service             | `500`                                                        |
| `API_JAVA_OPTS`                           | Java options for API (optional override) | `-Xmx${APP_API_JAVA_HEAP_LIMIT}m -XX:+PrintCommandLineFlags` |
| `API_POSTGRES_USER`                       | Username for API Postgres database       | `api_user`                                                   |
| `API_POSTGRES_DB_NAME`                    | Name of the API Postgres database        | `qodanadb`                                                   |
| `API_API_ZENDESK_FEEDBACK_EMAIL`          | Zendesk feedback email for API support   | `support@jbs1454063113.zendesk.com`                          |
| `API_LINTERS_VERSION_CI_TEMPLATES`        | Default version for linters CI templates | `2024.2`                                                     |
| `API_ORGANIZATION_NAME`                   | Organization name (optional)             |                                                              |
| `API_LICENSE_ID`                          | License ID for API (optional)            | `NULL`                                                       |

##### GitHub

| Environment variable                        | Description                                         | Default value                      |
|---------------------------------------------|-----------------------------------------------------|------------------------------------|
| `API_GITHUB_INTEGRATION_ENABLED` |Whether GitHub integration is enabled | `FALSE`                            | 
| `API_GITHUB_HOST_ORIGIN`         |Origin URL for GitHub                 | `https://github.com`               | 
| `API_GITHUB_APPLICATION_ID`      |GitHub Application ID                 | `NULL`                             | 
| `API_GITHUB_APPLICATION_NAME`    |GitHub Application Name               | `NULL`                             | 
| `API_GITHUB_OAUTH_CLIENT_ID`     |GitHub OAuth Client ID                | `NULL`                             | 

##### OAuth
{id="linter-api-oauth"}

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

#### Dependency services

##### Utility Swiss Knife container

| Environment variable                | Description                                    | Default value                                 |
|-------------------------------------|------------------------------------------------|-----------------------------------------------|
| `UTILITY_SWISS_KNIFE_IMAGE_NAME`    | Utility Swiss Knife container image name       | `jetbrains/qodana-installer-cli-dependencies` |
| `UTILITY_SWISS_KNIFE_IMAGE_TAG`     | Tag for the Swiss Knife container              | `busybox-1.36.2`                              |

##### Docker Swarm

| Environment variable                | Description                                    | Default value                                 |
|-------------------------------------|------------------------------------------------|-----------------------------------------------|
| `DOCKER_SWARM_INIT`                 | Whether to initialize Docker Swarm             | `TRUE`                                        |
| `DOCKER_SWARM_ADDRESS_POOL`         | Address pool for Docker Swarm overlay network  | `10.20.0.0/16`                                |
| `DOCKER_SWARM_GC_IMAGE_NAME`        | Docker Swarm garbage collection image name     | `jetbrains/qodana-installer-cli-dependencies` |
| `DOCKER_SWARM_GC_IMAGE_TAG`         | Tag for the Docker GC image                    | `docker-gc-latest`                            |

##### Ingress traffic

| Environment variable            | Description                                     | Default value                                 |
|---------------------------------|-------------------------------------------------|-----------------------------------------------|
| `INGRESS_CONTAINER_NAME`        | Ingress container image name                    | `jetbrains/qodana-installer-cli-dependencies` |
| `INGRESS_CONTAINER_TAG`         | Tag for the ingress container (Traefik version) | `traefik-v3.0`                                |
| `INGRESS_SUB_DOMAIN`                | Subdomain for ingress traffic                  | `ingress`                                     |

##### Database

| Environment variable            | Description                                     | Default value                                 |
|---------------------------------|-------------------------------------------------|-----------------------------------------------|
| `POSTGRES_CONTAINER_IMAGE_NAME` | Postgres container image name                   | `jetbrains/qodana-installer-cli-dependencies` |
| `POSTGRES_CONTAINER_IMAGE_TAG`  | Tag for the Postgres container image            | `postgres-15.10.0`                            |
| `POSTGRES_USER`                 | Default Postgres database user                  | `postgres`                                    |
| `POSTGRES_PASSWORD`             | Password for Postgres user                      | `qodanapassword`                              |
| `DB_HOSTNAME`                   | Hostname for the database                       | `postgres`                                    |
| `DB_PORT`                       | Database port                                   | `5432`                                        |

##### MinIO
{id="docker-configuration-environment-variables-minio"}

| Environment variable                        | Description                                         | Default value                                 |
|---------------------------------------------|-----------------------------------------------------|-----------------------------------------------|
| `MINIO_HOSTNAME`                            | Hostname for MinIO                                  |                                               |
| `MINIO_REGISTRY_IMAGE_NAME`                 | MinIO registry image name                           | `jetbrains/qodana-installer-cli-dependencies` |
| `MINIO_REGISTRY_IMAGE_TAG`                  | Tag for the MinIO registry image                    | `minio-RELEASE.2025-01-20T14-49-07Z`          |
| `MINIO_CLIENT_REGISTRY_IMAGE_NAME`          | MinIO client image name                             | `jetbrains/qodana-installer-cli-dependencies` |
| `MINIO_CLIENT_REGISTRY_IMAGE_TAG`           | Tag for the MinIO client image                      | `minio-mc-RELEASE.2025-01-17T23-25-50Z`       |
| `MINIO_ROOT_USER`                           | Root user for MinIO instance                        | `qodana`                                      |
| `MINIO_ROOT_PASSWORD`                       | Root password for MinIO                             | `qodanapassword`                              |
| `MINIO_API_PORT`                            | Port for MinIO API service                          | `9000`                                        |
| `MINIO_RESULTS_BUCKET`                      | Bucket name for storing Qodana results              | `qc-results`                                                              |
| `MINIO_BASELINES_BUCKET`                    | Bucket name for storing Qodana baselines            | `qc-baselines`                                                            |
| `MINIO_PRESIGNED_URL_EXPIRATION_IN_MINUTES` | Expiration time for MinIO presigned URLs in minutes | `120`                                                                     |

##### RabbitMQ
{id="docker-configuration-environment-variables-rabbitmq"}

| Environment variable                     | Description                         | Default value                                 |
|------------------------------------------|-------------------------------------|-----------------------------------------------|
| `RABBITMQ_REGISTRY_IMAGE_NAME`           | RabbitMQ registry image name        | `jetbrains/qodana-installer-cli-dependencies` |
| `RABBITMQ_REGISTRY_IMAGE_TAG`            | Tag for the RabbitMQ registry image | `rabbitmq-4.0.7`                              |
| `RABBITMQ_HOSTNAME`                      | Hostname for the RabbitMQ service   | `queue.${APP_DOMAIN}`                         |
| `RABBITMQ_PORT`                          | Port for RabbitMQ service           | `5672`                                        |
| `RABBITMQ_VHOST`                         | Virtual host for RabbitMQ           | `/qodana`                                     |
| `RABBITMQ_REPORTS_QUEUE_NAME`               | Queue name for Qodana reports                       | `qodanaCloudQueue`                                                        |

##### Keycloak

| Environment variable                | Description                    | Default value                                 |
|-------------------------------------|--------------------------------|-----------------------------------------------|
| `KEYCLOAK_REGISTRY_IMAGE_NAME`      | Keycloak registry image name   | `jetbrains/qodana-installer-cli-dependencies` |
| `KEYCLOAK_REGISTRY_IMAGE_TAG`       | Tag for the Keycloak image     | `keycloak-26.1`                               |
| `KEYCLOAK_HOSTNAME`                 | Hostname for Keycloak instance | `login.${APP_DOMAIN}`                         |
| `KEYCLOAK_DB_NAME`                  | Keycloak database name         | `keycloak`                                    |

##### Audit

| Environment variable      | Description                           | Default value                                                   |
|---------------------------|---------------------------------------|-----------------------------------------------------------------|
| `AUDIT_MEMORY_LIMIT`      | Memory limit for Audit service        | `500`                                                           |
| `AUDIT_JAVA_OPTS`         | Java options for Audit                | `-Xmx${APP_AUDIT_JAVA_HEAP_LIMIT}m -XX:+PrintCommandLineFlags`  |
| `AUDIT_POSTGRES_USER`     | Username for Audit Postgres database  | `audit_user`                                                    |
| `AUDIT_POSTGRES_DB_NAME`  | Name of the Audit Postgres database   | `audit`                                                         |

##### Git

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
| `GIT_MEMORY_LIMIT`                                          | Memory limit for Git Service                        | `500`                                                                     |
| `GIT_JAVA_OPTS`                                             | Java options for Git Service                        | `-Xmx${APP_GIT_JAVA_HEAP_LIMIT}m -XX:+PrintCommandLineFlags`              |
| `GIT_POSTGRES_USER`                                         | Username for Git Postgres database                  | `git_user`                                                                |
| `GIT_POSTGRES_DB_NAME`                                      | Name of the Git Postgres database                   | `git`                                                                     |
| `GIT_PROBE_TIMEOUT_SECONDS`                                 | Timeout for Git probe checks                        | `5`                                                                       |

##### Report processor

| Environment variable                | Description                                    | Default value                                 |
|-------------------------------------|------------------------------------------------|-----------------------------------------------|
| `REPORT_PROCESSOR_MEMORY_LIMIT`     | Memory limit for the Report Processor service       | `500`                                                                     |
| `REPORT_PROCESSOR_JAVA_OPTS`        | Java options for the Report Processor               | `-Xmx${APP_REPORT_PROCESSOR_JAVA_HEAP_LIMIT}m -XX:+PrintCommandLineFlags` |
| `REPORT_PROCESSOR_POSTGRES_USER`    | Username for Report Processor Postgres database     | `report_processor_user`                                                   |
| `REPORT_PROCESSOR_POSTGRES_DB_NAME` | Name of the Report Processor Postgres database      | `qodanadb`                                                                |


## Troubleshooting

To troubleshoot the issues that may arise during deployment, configuration, or operation
of %premlite%, use the following command to extract log entries:

```bash
docker run -v /var/run/docker.sock:/var/run/docker.sock \ quay.io/jetbrains/qodana-installer-cli:latest logs > all.troubleshooting.logs
```
{prompt="$"}

Study log entries and also try to:

* Look for the message related to a specific issue
* Review the possible causes of the issue
* Find the trace and debug the issue

If you cannot debug the issue or if the issue persists, navigate to the [JetBrains website](https://qodana-support.jetbrains.com/hc/en-us) and
create a request containing the following information:

| Information item | Description                                                                                                                |
|------------------|----------------------------------------------------------------------------------------------------------------------------|
| Summary          | Short and self-contained description of the issue                                                                          |
| Description      | Additional information to outline the issue better                                                                         |
| Attachments      | Any log files and screenshots, if available                                                                                |
| Tags             | Specify the version                                                                                                        |
| Type             | Try to categorize the title and the description of your case. This will be refined after the maintainers analyze the issue |
| Priority         | Set the priority to the issue. Apply common sense for the definition of the urgency level                                  |
