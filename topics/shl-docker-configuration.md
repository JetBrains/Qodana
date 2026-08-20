# Docker configuration

<show-structure for="chapter" depth="3"/>

The `qodana-installer-cli` command-line tool is a Docker container that manages the lifecycle of %premlite%. 

This tool orchestrates Docker Swarm stacks for:

* Infrastructure services: PostgreSQL, MinIO, RabbitMQ, Keycloak
* Application services: API, Audit, Git, Linters API, Report Processor, FUS, Frontend
* Supporting tools: Traefik ingress proxy, image garbage collector

## Prepare your project

### Access and permissions

The container should be given access to the Docker socket:

```text
-v /var/run/docker.sock:/var/run/docker.sock
```

Your user should have permission to the `/var/run/docker.sock` resource, i.e. be part of the `docker` group on the host.

Port 80 on the host should be available so that the Traefik ingress proxy can bind to it in host-network mode.

### Networking

<!-- WHAT DOES THIS MEAN?  -->
All service hostnames should resolve the IP address of the Swarm manager node. You can achieve this using:

<!-- What does this mean? -->
- An internal DNS server that covers `*.<DOMAIN>`
- Manual `/etc/hosts` entries on every machine that should have access to %product%

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
        <td><code>http://&lt;domain&gt;</code></td>
    </tr>
    <tr>
        <td>Backend (API gateway)</td>
        <td><code>http://api.&lt;domain&gt;</code></td>
    </tr>
    <tr>
        <td>Linter API</td>
        <td><code>http://lintersapi.&lt;domain&gt;</code></td>
    </tr>
    <tr>
        <td>Built-in file storage (MinIO)</td>
        <td><code>http://files.&lt;domain&gt;</code></td>
    </tr>
    <tr>
        <td>Built-in SSO provider (Keycloak)</td>
        <td><code>http://login.&lt;domain&gt;</code></td>
    </tr>
    <tr>
        <td>Built-in ingress controller (Traefik)</td>
        <td><code>http://ingress.&lt;domain&gt;</code></td>
    </tr>
</table>

<!-- This is inconsistent here  -->
<p>These hostnames enable interaction of %product% components and provide access to essential services.
The IP address can be of your server or a load balancer, depending on your deployment architecture. </p>

Traefik routes inbound HTTP traffic to services based on the `Host` header, using routing rules configured via Docker
service labels. Each service registers its own Traefik route at deploy time.

In production environments, you should use a domain that aligns with your naming conventions like `qodana.mycompany.com`,
`files.qodana.mycompany.com` and others.

If you intend to use %product% only internally, configure DNS records in your internal DNS server. For external access,
ensure that public DNS records point to appropriate IP addresses of your server or load balancer.

#### Configure domains

On your local machine, make the changes to the <code>/etc/hosts</code> file
depending on your needs, i.e. for the default or your custom domain configuration:

```Apache
# Default domain / custom domain (mycompany.com)
127.0.0.1 qodana.local # / qodana.mycompany.com
127.0.0.1 files.qodana.local # / api.qodana.mycompany.com
127.0.0.1 api.qodana.local # / files.qodana.mycompany.com
127.0.0.1 ingress.qodana.local # / login.qodana.mycompany.com
127.0.0.1 login.qodana.local # / ingress.qodana.mycompany.com
127.0.0.1 lintersapi.qodana.local # / lintersapi.qodana.mycompany.com
```

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

## Command overview

Here is the list of available Docker commands and links to their respective use cases:

| Command       | Description                                                                                 |
|---------------|---------------------------------------------------------------------------------------------|
| `install-app` | [Deploy %premlite%](#Deploy+Qodana+Self-Hosted)                                             |
| `uninstall`   | [Remove all deployed resources](#Uninstall+%25premlite%25)                                  |
| `backup`      | [Create a compressed backup](#Backup+and+restore) of all local data                         |
| `restore`     | [Restore data](#Restoring+from+a+backup) from a backup file                                 |
| `credentials` | [Retrieve credentials](#Manage+credentials) for any infrastructure component                |
| `environment` | [Print all configurable variables](#Get+a+list+of+used+variables) and their resolved values |
| `logs`        | [Stream logs](#Retrieve+logs) from all %product% services                                   |
| `help`        | [Print command usage and examples](#Get+help+page)                                                       |



## Deploy Qodana Self-Hosted

Assuming that requirements from the [](shl-introduction.md) and [](#Prepare+your+project) chapters are satisfied, pull the
`quay.io/jetbrains/qodana-installer-cli:latest` Docker image. All commands running this image require the
`/var/run/docker.sock` Docker socket file for communicating with the Docker engine and Docker Swarm.

> Basically, the deployment process is idempotent: running it on an already deployed system skips existing Docker configurations and
> redeploys the service stacks from scratch. However, it is recommended to run the `uninstall` Docker command prior to redeploying %premlite%.
{style="note"}

By default, %premlite% comes configured with local dependencies for quick Proofs Of Concepts (PoCs) or Proofs of Value (PoV).

Depending on your needs, run the command to deploy %premlite% on your machine:

<tabs>
    <tab title="Default domain and user">
        <code-block lang="Bash" prompt="$">
            docker run \
                -v /var/run/docker.sock:/var/run/docker.sock \
                -e API_ORGANIZATION_NAME="&lt;Specify the name of your organization&gt;" \
                -e COMMON_LICENSE_KEY_SECRET="&lt;Specify a valid license key&gt;" \ 
                quay.io/jetbrains/qodana-installer-cli:latest \
                install-app
        </code-block>
        <p>This configuration creates the default user with the following credentials:</p>
        <ul>
            <li>Username: <code>tser@qodana.local</code></li>
            <li>Password: <code>@wesomeQodana</code></li>
        </ul>
         <p>These credentials are publicly known, so you should update them as soon as possible by navigating to 
            the <code>http://login.qodana.local</code> page.</p>
    </tab>
    <tab title="Custom domain and user">
        <code-block lang="Bash" prompt="$">
            docker run \
                -e DOMAIN=qodana.mycompany.com \
                -e QODANA_DEFAULT_USER_USERNAME=admin@mycompany.com \
                -e QODANA_DEFAULT_USER_PASSWORD=your-secure-password \
                -e API_ORGANIZATION_NAME="&lt;Specify the name of your organization&gt;" \
                -e COMMON_LICENSE_KEY_SECRET="&lt;Specify a valid license key&gt;" \
                -v /var/run/docker.sock:/var/run/docker.sock \
                quay.io/jetbrains/qodana-installer-cli:latest \ 
                install-app
        </code-block>
        <p>This command configures the <code>qodana.mycompany.com</code> custom domain along with user credentials.</p>
    </tab>
    <tab title="Configuration from a file">
        <code-block lang="Bash" prompt="$">
            docker run 
                -v /var/run/docker.sock:/var/run/docker.sock \ 
                -e API_ORGANIZATION_NAME="&lt;Specify the name of your organization&gt;" \
                -e COMMON_LICENSE_KEY_SECRET="&lt;Specify a valid license key&gt;" \ 
                --env-file qodana-self-hosted.env \
                quay.io/jetbrains/qodana-installer-cli:latest \ 
                install-app
        </code-block>
        <p>This command uses the <code>--env-file</code> option to specify the path to the configuration file; in this 
            case, the <code>qodana-self-hosted.env</code> file.</p>
        <p>You can use the same <code>--env-file</code> flag for each subsequent command like 
            <code>backup</code>, <code>credentials</code> or <code>environment</code> to ensure consistent behaviour.</p>
    </tab>
    <tab title="Persist secrets">
        <p>You can export and persist secrets created during deployment in the <code>${PWD}/secrets</code> directory:</p>
        <code-block lang="Bash" prompt="$">
            docker run \
                -v /var/run/docker.sock:/var/run/docker.sock \ 
                -v ${PWD}/secrets:/app/qodana-installer/secrets \
                -e API_ORGANIZATION_NAME="&lt;Specify the name of your organization&gt;" \
                -e COMMON_LICENSE_KEY_SECRET="&lt;Specify a valid license key&gt;" \ 
                quay.io/jetbrains/qodana-installer-cli:latest \
                install-app
        </code-block>
        <p>To make the secret idempotent, this command mounts the <code>/app/qodana-installer/secrets</code> directory for secret storage.</p>
    </tab>
</tabs>

Here, the `COMMON_LICENSE_KEY_SECRET` variable configures a license key for production use. Without a valid key, the 
application runs with limited functionality.

The `install-app` command performs the following steps:

1. Initializes Docker Swarm (`docker swarm init`) if the host is not already a Swarm node and `DOCKER_SWARM_INIT=true`
2. Creates the `qodana_self_hosted` overlay network
3. Deploys supporting tools: Traefik ingress (binds port 80) and `docker-swarm-gc`
4. Generates all service secrets using `openssl rand` and stores them as Docker configurations
5. Renders configuration templates for each service like API, Audit, Git, Linters API
6. Renders RabbitMQ definitions and Keycloak realm templates, then deploys infrastructure services like PostgreSQL, MinIO, RabbitMQ, Keycloak
7. Waits 20 seconds for infrastructure to become available
8. Deploys Qodana application services: API, Audit, Git, Linters API, Report Processor, FUS, Frontend

The `install-app` command exits after submitting all stacks. Services continue starting up in the background.

The entire deployment process may take two or three minutes to complete.

After the deployment, make sure that all services reached their desired replica count by running the following command:

```bash
docker service ls \
    --filter label=qodana.jetbrains.self-hosted.lite.select=true
```
{prompt="$"}

Every service should show `1/1` in the `REPLICAS` column. If any service shows `0/1`, inspect its logs:

```bash
docker service logs <service-name>
```
{prompt="$"}

Alternatively, use the installer log aggregation:

```bash
docker run \
    -v /var/run/docker.sock:/var/run/docker.sock \
    quay.io/jetbrains/qodana-installer-cli:latest \
    logs
```
{prompt="$"}

In your browser, navigate to the configured domain to receive access to %premlite%.

## Get a list of used variables

Run the `environment` command to display every configurable variable with its resolved value:

```bash
docker run \
    --env-file qodana.env \
    -v /var/run/docker.sock:/var/run/docker.sock \
    quay.io/jetbrains/qodana-installer-cli:latest \
    environment
```
{prompt="$"}

If you run this command with the same flags that you used for the `install-app` command, you will be able to see what 
values are in effect.

## Manage credentials

All infrastructure credentials like database passwords, object storage keys, message queue passwords, or Keycloak admin accounts
are generated randomly during deployment and stored as Docker configurations. They can be retrieved at any time without 
having to deploy %premlite% again.

All credentials are:

* Generated during deployment using cryptographically secure random bytes via `openssl rand`
* Stored immediately as Docker configs and labeled as `qodana.jetbrains.self-hosted.lite.select=true`
* Mounted read-only into each service container at the path that a service expects
* Never written to the host filesystem or any log output

Docker configs persist across container and service restarts. They are the single source of truth for all generated 
credentials and are what the `credentials` command reads.

> If you uninstall (the `uninstall` command) and then reinstall (the `install-app` command), new credentials are generated. 
> Any external integrations using the old credentials like scripts using MinIO keys must be updated.
{style="note"}

Using the `credentials` command, you can retrieve credentials:

```bash
docker run \
  -v /var/run/docker.sock:/var/run/docker.sock \
  quay.io/jetbrains/qodana-installer-cli:latest \
  credentials <target> [--format txt|json|yaml]
```
{prompt="$"}

Here, under `<target>` you can use the following values:

| Value              | Description                                                                                                                                |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| `--keycloak`       | Keycloak super-admin credentials.  Used at the admin console available via `http://login.<DOMAIN>` to manage users, realms, OAuth2 clients |
| `--default-user`   | Default Qodana UI user credentials, used as an out-of-the-box login capability at `http://<DOMAIN>`                                        |
| `--keycloak-db`    | PostgreSQL credentials for the Keycloak database, provides direct access for diagnostic purposes                                           |
| `--object-storage` | MinIO root user credentials. Used by MinIO console at `http://files.<DOMAIN>` to inspect buckets and analysis artifacts                    |
| `--message-queue`  | RabbitMQ application user credentials, used by the RabbitMQ management interface via the management plugin API                             |

The `--format` flag lets you use the following values:

| The `--format` value | Description                                      |
|----------------------|--------------------------------------------------|
| `txt`                | `Username: …` / `Password: …`, the default value |
| `json`               | `{"username":"…","password":"…"}`                |
| `yaml`               | `username: …\npassword: …`                       |

## Retrieve logs

Retrieve aggregated log entries from all running services using the `logs` command:

```bash
docker run \
    --env-file qodana.env \
    -v /var/run/docker.sock:/var/run/docker.sock \
    quay.io/jetbrains/qodana-installer-cli:latest \
    logs
```
{prompt="$"}

You can filter logs using the <code>--filters</code> parameter and labels described in
the [](#Configure+Qodana+Self-Hosted) chapter. For example, the `qodana.jetbrains.self-hosted.lite.service` [label](#Labels+related+to+local+dependencies) lets 
you filter logs by a service type. This label accepts the following values: 

| Value                | Services covered                                                              |
|----------------------|-------------------------------------------------------------------------------|
| `application`        | API, Audit, Git API, Git Worker, Linters API, Report Processor, FUS, Frontend |
| `local-dependencies` | PostgreSQL, MinIO, RabbitMQ, Keycloak                                         |
| `supporting-tools`   | Traefik, docker-swarm-gc                                                      |

Below is an example command using this label and the `application` label value: 

```bash
docker run \
    --env-file qodana.env \
    -v /var/run/docker.sock:/var/run/docker.sock \
    quay.io/jetbrains/qodana-installer-cli:latest \
    logs \
    --filters "label=qodana.jetbrains.self-hosted.lite.service-type=application"
```
{prompt="$"}

Using the Docker CLI, you can also query a single service directly:

```bash
docker service logs <service-name> --follow
```
{prompt="$"}

## Backup and restore

Using the `backup` and `restore` commands, you can create and restore compressed, timestamped backup data of all local data volumes.
In this case, each backup is a full-volume snapshot, which requires sufficient free disk space on the host machine.

The commands require that you use absolute paths on the Docker host. %premlite% spawns a utility container via the Docker socket and mounts the path directly using a `-v` bind-mount, for example:

| Command               | Argument example                      | Mounted inside utility container as                                |
|-----------------------|---------------------------------------|--------------------------------------------------------------------|
| `backup <HOST_DIR>`   | `/srv/qodana-backups`                 | `-v /srv/qodana-backups:/app/qodana-installer/backup`              |
| `restore <HOST_FILE>` | `/srv/qodana-backups/backup-….tar.gz` | `-v /srv/qodana-backups/backup-….tar.gz:/backup/restore.tar.gz:ro` |

> The `backup` and `restore` commands work only when the `QODANA_DEPENDENCIES_MODE` [dependency mode variable](#Dependency+mode+variables) 
> is set to `local`, i.e. the default setting. External dependencies must be backed up using their own tooling.
{style=note"}

If you mount an external filesystem into the %premlite% container like `-v /nas/backups:/backups`, you should still pass 
the host-side path like `/nas/backups` to the command — not the container-internal path like `/backups`. 

When using the `-v` flag to mount a volume in the utility container, the path is resolved by the Docker daemon on the 
host machine, not relatively to the installer container’s filesystem.

### Creating a backup

The destination directory should already exist on the Docker host, for example:

```bash
mkdir -p /srv/qodana-backups
```

Run the `backup` command to create a backup archive:

```bash
docker run \
    --env-file qodana.env \
    -v /var/run/docker.sock:/var/run/docker.sock \
    quay.io/jetbrains/qodana-installer-cli:latest \
    backup /srv/qodana-backups
```
{prompt="$"}

Here is a list of components contained in the backup archive:

| Component  | Data included                                                 |
|------------|---------------------------------------------------------------|
| PostgreSQL | All Qodana application databases (API, Audit, Git, Keycloak)  |
| MinIO      | Analysis reports, baselines, and global configuration buckets |
| RabbitMQ   | Message queue state                                           |

Docker configs (secrets) are stored in Docker's config store and survive as long as the Swarm node exists. 

The backup process does the following:

* Pauses all services by setting replicas to `0`
* Makes snapshots of all data volumes into a single timestamped archive: `backup-YYYY-MM-DD-HH-MM-SS.tar.gz`
* Verifies archive integrity before resuming services
* Resumes all services independently of the backup completion status

During the backup procedure, all services become unavailable. The archive step usually completes in seconds to a few minutes.

If the backup operation fails at any point after services are paused, they are automatically resumed. In this case, the 
archive is saved in the destination directory and should be deleted manually before the next backup attempt.

### Restoring from a backup

> This action completely and irreversibly erases all current volume data before extracting the backup. 
> Verify the file path and make sure that the archive contains correct data before proceeding.
{style=warning"}

To restore from a backup, follow these steps:

<procedure>
    <step>
        Before restoring, make sure that the backup archive file is available on the Docker host.
    </step>
    <step>
        Run the <a anchor="Deploy+Qodana+Self-Hosted"><code>install-app</code></a> command to create volumes and services. 
        This is the recommended method for migrating to a new host. Any external integrations relying on the old secret values must be updated after migration.
    </step>
    <step>
        <p>Run the <code>restore</code> command with an absolute path to the backup archive file, for example:</p>
        <code-block lang="bash" prompt="$">
            docker run \
                --env-file qodana.env \
                -v /var/run/docker.sock:/var/run/docker.sock \
                quay.io/jetbrains/qodana-installer-cli:latest \
                restore /srv/qodana-backups/backup-2025-02-17-14-30-16.tar.gz
        </code-block>
    </step>
</procedure>

The restore process does the following:

* Validates the backup archive. If the archive is missing or corrupt, the process stops
* Pauses all services by setting replicas to `0`
* Wipes all volume data, i.e deletes current contents of every managed volume
* Extracts the archive into clean volumes
* Resumes all services independently of the restore completion status

## Get help page

The `help` command lets you retrieve the help page for any available command:

```Bash
docker run \
    -v /var/run/docker.sock:/var/run/docker.sock \ 
    quay.io/jetbrains/qodana-installer-cli:latest \
    help
```
{prompt="$"}

## Uninstall %premlite%

> Because uninstalling deletes all application data stored in Docker volumes, we recommend creating a [backup](#Backup+and+restore) beforehand. 
{style="warning"}

Run the `uninstall` command to remove %premlite% from Docker:

```bash
docker run \
    --env-file qodana.env \
    -v /var/run/docker.sock:/var/run/docker.sock \
    quay.io/jetbrains/qodana-installer-cli:latest \ 
    uninstall
```
{prompt="$"}

This action removes the following components:

* Docker service stacks: application services, infrastructure services, supporting tools
* All Docker configurations created by %premlite% like secrets and service configurations
* All Docker volumes that are labeled as %product%-managed

The `qodana_self_hosted` overlay network is not removed because removing and recreating it between deployments on the 
same host causes Docker Swarm to lose network stability, i.e. containers can no longer resolve each other. 
If you need to remove it, run the following command: 

```bash
docker network rm qodana_self_hosted
```
{prompt="$"}

## Reset passwords

User password management is handled through Keycloak. To reset passwords, perform the following steps:

<procedure>
    <step>
        <p>Retrieve the Keycloak administrator credentials:</p>
        <code-block lang="Bash" prompt="$">
          docker run \
              -v /var/run/docker.sock:/var/run/docker.sock \
              quay.io/jetbrains/qodana-installer-cli:latest \
              credentials --keycloak
        </code-block>
    </step>
    <step>
        <p>Sign in to the Keycloak Admin Console at <code>http://login.&lt;DOMAIN&gt;</code>.</p>
    </step>
    <step>
        <p>At the Keycloak Admin Console, navigate to the <code>qodana</code>, and then navigate to <ui-path>Users</ui-path>. 
            Here, select the user's <ui-path>Credentials</ui-path> and then click <ui-path>Reset Password</ui-path>.</p>
    </step>
</procedure>


## Configure Qodana Self-Hosted

Labels and environment variables let you configure %premlite% specifically to your needs. 

### Global labels

%premlite% uses several global labels to mark the managed resources. You can use these labels to operate
%premlite%:

| Label and value                                                                  | Description                                                                                                                                 |
|----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| `qodana.jetbrains.self-hosted.lite.select=true`                                  | Identify all resources that are part of the %premlite% deployment                                                                           |
| `qodana.jetbrains.self-hosted.lite.version=${APP_QODANA_SELF_HOSTED_IMAGE_TAG}`  | Display at runtime a %premlite% version that a specific resouce is related to. Dependent on the `APP_QODANA_SELF_HOSTED_IMAGE_TAG` variable |

For example, you can use global variables to troubleshoot problems connected with service availability, for example:

```Bash
docker service ls \
    --filter label=qodana.jetbrains.self-hosted.lite.select=true
```
{prompt="$"}

### Domain and hostname variables

| Variable               | Default value         | Controls                                                                          | 
|------------------------|-----------------------|-----------------------------------------------------------------------------------|
| `DOMAIN`               | `qodana.local`        | Base domain; services without an explicit override default to `<prefix>.<DOMAIN>` |
| `FRONTEND_HOSTNAME`    | `<DOMAIN>`            | Web UI                                                                            |
| `API_HOSTNAME`         | `api.<DOMAIN>`        | API gateway                                                                       |
| `MINIO_HOSTNAME`       | `files.<DOMAIN>`      | Object storage                                                                    |
| `KEYCLOAK_HOSTNAME`    | `login.<DOMAIN>`      | Authentication                                                                    |
| `LINTERS_API_HOSTNAME` | `lintersapi.<DOMAIN>` | Linters API                                                                       |
| `INGRESS_SUB_DOMAIN`   | `ingress`             | Traefik subdomain *prefix* — full hostname is `<value>.<DOMAIN>`                  |
| `IDP_SUB_DOMAIN`       | `login`               | Keycloak subdomain prefix                                                         |

This Docker command shows how you can override domain and host names while deploying %premlite%:  

```Bash
docker run \
    -e DOMAIN=mycompany.com \
    -e FRONTEND_HOSTNAME=code-quality.mycompany.com \
    -e API_HOSTNAME=code-quality-api.mycompany.com \
    -e MINIO_HOSTNAME=code-quality-storage.mycompany.com \
    -e KEYCLOAK_HOSTNAME=sso.mycompany.com \
    -e LINTERS_API_HOSTNAME=linters.mycompany.com \
    -v /var/run/docker.sock:/var/run/docker.sock \
    quay.io/jetbrains/qodana-installer-cli:latest \ 
    install-app
```
{prompt="$"}

We recommend that you run the `uninstall` command prior to this command. This will let you remove
the existing Docker configurations that may contain hostname values.

### UI user variables

%premlite% creates one user in the `qodana` Keycloak realm that you can override using the following variables: 

| Variable                       | Default         | Description                                                   |
|--------------------------------|-----------------|---------------------------------------------------------------|
| `QODANA_DEFAULT_USER_USERNAME` | `tser@<DOMAIN>` | Username and email address                                    |
| `QODANA_DEFAULT_USER_PASSWORD` | `@wesomeQodana` | Plaintext password — hashed with Argon2id at deployment time  |

> There is no recovery mechanism for users other than recreating the user via the Keycloak admin console.
{style="note"}

You can override the user credentials using the following command:

```Bash
docker run \
    -e QODANA_DEFAULT_USER_USERNAME=admin@mycompany.com \
    -e QODANA_DEFAULT_USER_PASSWORD=your-secure-password \
    -v /var/run/docker.sock:/var/run/docker.sock \
    quay.io/jetbrains/qodana-installer-cli:latest \
    install-app
```
{prompt="$"}

### Dependency mode variables

The `QODANA_DEPENDENCIES_MODE` variable controls whether infrastructure services are deployed as part of the Swarm or supplied externally.
The variable accepts the following values:

| Value    | Description                                                                                       |
|----------|---------------------------------------------------------------------------------------------------|
| `local`  | The default value. %premlite% deploys PostgreSQL, MinIO, RabbitMQ, and Keycloak as Swarm services |
| `remote` | %premlite% skips dependency deployment; you supply connection details via environment variables   |

> The `backup` and `restore` commands are supported only in the `local` mode. For the `remote` 
> mode, the external services should be backed up and restored by their own tooling.
{style="note"}

You can override the dependency mode using the following command:

```bash
docker run \
    -e QODANA_DEPENDENCIES_MODE=remote \
    -v /var/run/docker.sock:/var/run/docker.sock \
    quay.io/jetbrains/qodana-installer-cli:latest \
    install-app
```
{prompt="$"}

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

| Environment variable                | Description                                | Default value                           |
|-------------------------------------|--------------------------------------------|-----------------------------------------|
| `LOG_LEVEL`                         | Application logging level                  | `info`                                  |
| `IDP_SUB_DOMAIN`                    | Subdomain for identity provider (Keycloak) | `login`                                 |
| `CONTAINER_REGISTRY_URL`            | Container registry URL for pulling images  | `quay.io`                               |
| `APP_QODANA_SELF_HOSTED_IMAGE_TAG`  | Current version of %premlite%              | `1.22.0-alpha.14`, actual for July 2025 |
| `FRONTEND_MEMORY_LIMIT`             | Memory limit for the Frontend service      | `500`                                   |
| `OBJECT_STORAGE_PROVIDER`           | Object storage provider type               | `minio`                                 |
| `MESSAGE_BROKER_PROVIDER`           | Message broker provider (RabbitMQ)         | `rabbitmq`                              |


##### FUS
{id="product-fus"}

Variables used for statistics collection and processing.

| Environment variable         | Description                                   | Default value                                                         |
|------------------------------|-----------------------------------------------|-----------------------------------------------------------------------|
| `FUS_MEMORY_LIMIT`           | Memory limit for FUS service                  | `500`                                                                 |
| `FUS_JAVA_OPTS`              | Java options for FUS                          | `-Xmx${APP_FUS_JAVA_HEAP_LIMIT}m -XX:+PrintCommandLineFlags`          |
| `FUS_INTERNAL`               | Whether FUS is internal only                  | `FALSE`                                                               |
| `FUS_CONFIGURATION_ENDPOINT` | Endpoint URL for FUS configuration            | `https://resources.jetbrains.com/storage/fus/config/v4/QD/QDCLD.json` |

#### Linter API

Linter API validates linters and checks for versions of supported linters and plugins.

##### General
{id="linter-api-general"}

| Environment variable                        | Description                                  | Default value                                                             |
|---------------------------------------------|----------------------------------------------|---------------------------------------------------------------------------|
| `LINTERS_API_MEMORY_LIMIT`                  | Memory limit for the Linters API service     | `500`                                                                     |
| `LINTERS_API_JAVA_OPTS`                     | Java options for the Linters API service     | `-Xmx${APP_LINTERS_API_JAVA_HEAP_LIMIT}m -XX:+PrintCommandLineFlags`      |
| `LINTERS_API_POSTGRES_USER`                 | Username for Linters API Postgres database   | `linters_api_user`                                                        |
| `LINTERS_API_POSTGRES_DB_NAME`              | Name of the Linters API Postgres database    | `qodanadb`                                                                |
| `API_MEMORY_LIMIT`                        | Memory limit for the API service             | `500`                                                        |
| `API_JAVA_OPTS`                           | Java options for the API (optional override) | `-Xmx${APP_API_JAVA_HEAP_LIMIT}m -XX:+PrintCommandLineFlags` |
| `API_POSTGRES_USER`                       | Username for API Postgres database           | `api_user`                                                   |
| `API_POSTGRES_DB_NAME`                    | Name of the API Postgres database            | `qodanadb`                                                   |
| `API_API_ZENDESK_FEEDBACK_EMAIL`          | Zendesk feedback email for API support       | `support@jbs1454063113.zendesk.com`                          |
| `API_LINTERS_VERSION_CI_TEMPLATES`        | Default version for linters CI templates     | `2024.2`                                                     |
| `API_ORGANIZATION_NAME`                   | Organization name (optional)                 |                                                              |
| `API_LICENSE_ID`                          | License ID for API (optional)                | `NULL`                                                       |

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

| Environment variable                | Description                                                    | Default value                                 |
|-------------------------------------|----------------------------------------------------------------|-----------------------------------------------|
| `DOCKER_SWARM_INIT`                 | Run the `docker swarm init` command automatically if necessary | `true`                                        |
| `DOCKER_SWARM_ADDRESS_POOL`         | Address pool for Docker Swarm overlay network                  | `10.20.0.0/16`                                |
| `DOCKER_SWARM_GC_IMAGE_NAME`        | Docker Swarm garbage collection image name                     | `jetbrains/qodana-installer-cli-dependencies` |
| `DOCKER_SWARM_GC_IMAGE_TAG`         | Tag for the Docker GC image                                    | `docker-gc-latest`                            |

For example, you can set the `DOCKER_SWARM_INIT` variable to `false` if the host is already a Swarm manager, which lets you skip the init attempt:

```bash
docker run \
    -e DOCKER_SWARM_INIT=false \
    -v /var/run/docker.sock:/var/run/docker.sock \
    quay.io/jetbrains/qodana-installer-cli:latest \
    install-app
```
{prompt="$"}

If `10.20.0.0/16` conflicts with existing networks on your host, use the `DOCKER_SWARM_ADDRESS_POOL` variable to a non-overlapping 
CIDR, for example:

```bash
docker run \
    -e DOCKER_SWARM_ADDRESS_POOL=10.21.0.0/16 \
    -v /var/run/docker.sock:/var/run/docker.sock \
    quay.io/jetbrains/qodana-installer-cli:latest \
    install-app
```
{prompt="$"}


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

| Environment variable      | Description                          | Default value                                                   |
|---------------------------|--------------------------------------|-----------------------------------------------------------------|
| `AUDIT_MEMORY_LIMIT`      | Memory limit for the Audit service   | `500`                                                           |
| `AUDIT_JAVA_OPTS`         | Java options for the Audit service   | `-Xmx${APP_AUDIT_JAVA_HEAP_LIMIT}m -XX:+PrintCommandLineFlags`  |
| `AUDIT_POSTGRES_USER`     | Username for Audit Postgres database | `audit_user`                                                    |
| `AUDIT_POSTGRES_DB_NAME`  | Name of the Audit Postgres database  | `audit`                                                         |

##### Git

| Environment variable                                        | Description                                        | Default value                        |
|-------------------------------------------------------------|----------------------------------------------------|--------------------------------------|
| `GIT_RABBITMQ_CONTRIBUTORS_REQUEST_QUEUE_NAME`              | Queue name for Git contributors request            | `qodanaGetContributorsRequestQueue`  |
| `GIT_RABBITMQ_CONTRIBUTORS_RESPONSE_QUEUE_NAME`             | Queue name for Git contributors response           | `qodanaGetContributorsResponseQueue` |
| `GIT_RABBITMQ_CONTRIBUTORS_RESPONSE_WAIT_TIME`              | Wait time for contributors' responses              | `20`                                 |
| `GIT_RABBITMQ_CONTRIBUTORS_RESPONSE_MAX_NUMBER_OF_MESSAGES` | Max number of messages for contributors' responses | `10`                                 |
| `GIT_RABBITMQ_CONTRIBUTORS_RESPONSE_WORKERS_NUM`            | Number of workers for contributors' responses      | `20`                                 |
| `GIT_RABBITMQ_TRIGGERS_QUEUE_NAME`                          | Queue name for Git triggers                        | `qodanaGitTriggersQueue`             |
| `GIT_RABBITMQ_TRIGGERS_WAIT_TIME`                           | Wait time for Git triggers                         | `20`                                 |
| `GIT_RABBITMQ_TRIGGERS_MAX_NUMBER_OF_MESSAGES`              | Max number of messages for Git triggers            | `10`                                 |
| `GIT_RABBITMQ_TRIGGERS_WORKERS_NUM`                         | Number of workers for Git triggers                 | `1`                                  |
| `GIT_MEMORY_LIMIT`                                          | Memory limit for the Git Service                   | `500`                                                                     |
| `GIT_JAVA_OPTS`                                             | Java options for the Git Service                   | `-Xmx${APP_GIT_JAVA_HEAP_LIMIT}m -XX:+PrintCommandLineFlags`              |
| `GIT_POSTGRES_USER`                                         | Username for Git Postgres database                 | `git_user`                                                                |
| `GIT_POSTGRES_DB_NAME`                                      | Name of the Git Postgres database                  | `git`                                                                     |
| `GIT_PROBE_TIMEOUT_SECONDS`                                 | Timeout for Git probe checks                       | `5`                                                                       |

##### Report processor

| Environment variable                | Description                                     | Default value                                 |
|-------------------------------------|-------------------------------------------------|-----------------------------------------------|
| `REPORT_PROCESSOR_MEMORY_LIMIT`     | Memory limit for the Report Processor service   | `500`                                                                     |
| `REPORT_PROCESSOR_JAVA_OPTS`        | Java options for the Report Processor service   | `-Xmx${APP_REPORT_PROCESSOR_JAVA_HEAP_LIMIT}m -XX:+PrintCommandLineFlags` |
| `REPORT_PROCESSOR_POSTGRES_USER`    | Username for Report Processor Postgres database | `report_processor_user`                                                   |
| `REPORT_PROCESSOR_POSTGRES_DB_NAME` | Name of the Report Processor Postgres database  | `qodanadb`                                                                |


## Known limitations

This table describes known limitations regarding the current Dockerized implementation of %premlite%:

| Limitation                       | Detail                                                                                                                                                       |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| No HTTPS                         | All communication is plain HTTP. An upstream TLS-terminating proxy is required for production                                                                |
| No backup in remote mode         | When the `QODANA_DEPENDENCIES_MODE` is set to `remote`, backup and restore commands are not supported                                                        |
| Single-node Swarm                | Designed for single-node Docker Swarm. Multi-node deployments require additional volume and network planning                                                 |
| Domain changes require reinstall | Hostnames are encoded in Docker configs at install time. Changing them requires running the `uninstall` and `install-app` commands                           |
| No incremental backup            | Each backup is a full volume snapshot                                                                                                                        |
| Docker configs not in backup     | Generated secrets are stored in Docker's config store, not in the data volume backup. They must be regenerated using the `install-app` command on a new host |
| Startup time                     | Services continue starting after the installer exits. You should wait for 2–3 minutes before accessing the UI                                                |


## Troubleshooting

To troubleshoot the issues that may arise during deployment, configuration, or operation
of %premlite%, use the following command to extract log entries:

```bash
docker run \
    -v /var/run/docker.sock:/var/run/docker.sock \ 
    quay.io/jetbrains/qodana-installer-cli:latest 
    logs > all.troubleshooting.logs
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


### Services show `0/1` replicas after deployment

Run the following commands to detect the services that are not running:

```bash
docker service ls \
    --filter label=qodana.jetbrains.self-hosted.lite.select=true
```
{prompt="$"}

```bash
docker service logs <service-name>
```
{prompt="$"}

Common causes: insufficient memory, port 80 already in use, hostnames not resolving.

### Cannot reach the UI after install completes

Take the following actions to troubleshoot the issue:

* Verify hostnames resolve: `curl -v http://qodana.local`
* Confirm that Traefik is running: `docker service ls | grep traefik`
* Confirm that port 80 is bound: `ss -tlnp | grep :80`

### The install-app command fails partway through

Consider rerunning the `install-app` command because it skips already created resources.
Identify the cause from logs, fix the underlying cause (e.g., network conflict, missing Docker socket), then run the command again.

### The credentials command returns nothing or errors

The credentials command reads Docker configs. If you have just uninstalled or are running on a different host, 
the configs do not exist. Consider running the `install-app` command first.


### Backup fails with a permission error

The backup destination path should exist on the Docker host and be writable by the Docker daemon. Ensure that the directory 
exists:

```bash
mkdir -p /srv/qodana-backups
```
{prompt="$"}

### Inspecting Docker configs

To make sure that Docker configs exist, run the following command: 

```bash
docker config ls \
    --filter label=qodana.jetbrains.self-hosted.lite.select=true
```
{prompt="$"}

### Inspecting %premlite% volumes

Run the following command to inspect %premlite% volumes:

```bash
docker volume ls \
    --filter label=qodana.jetbrains.self-hosted.lite.select=true
```
{prompt="$"}

## Post-configuration steps
<include from="shl-kubernetes-configuration.md" element-id="shl-kubernetes-configuration-post-config-steps"/>