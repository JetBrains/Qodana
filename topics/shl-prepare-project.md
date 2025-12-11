# Prepare your project (Docker)

<!-- The ingress description should be added here. What is it?-->

## Domain name system (DNS)

<p>%premlite% exposes different HTTP endpoints as base URLs. Make sure to allocate a top-level domain like <code>qodana.local</code>.
    The majority of %premlite% components require dedicated base URLs, for example:</p>
<table>
    <tr>
        <td>Component</td>
        <td>URL</td>
    </tr>
    <tr>
        <td>Frontend</td>
        <td><code>qodana.local</code></td>
    </tr>
    <tr>
        <td>Backend</td>
        <td><code>api.qodana.local</code></td>
    </tr>
    <tr>
        <td>Linter API</td>
        <td><code>lintersapi.qodana.local</code></td>
    </tr>
    <tr>
        <td>Built-in file storage</td>
        <td><code>files.qodana.local</code></td>
    </tr>
    <tr>
        <td>Built-in SSO provider</td>
        <td><code>login.qodana.local</code></td>
    </tr>
    <tr>
        <td>Built-in ingress controller (optional)</td>
        <td><code>ingress.qodana.local</code></td>
    </tr>
</table>
<p>These hostnames enable interaction of %product% components and access to essential services.
services. The IP can be of your server or a load balancer, depending on your deployment architecture. </p>

In production environments, you should use a domain that aligns with your naming conventions like `qodana.mycompany.com`,
`files.qodana.mycompany.com` and others.

If you intend to use %product% only internally, configure DNS records in your internal DNS server. For external access, 
ensure that public DNS records point to appropriate IP addresses of your server or load balancer.

## PostgreSQL

### Databases

%premlite% operates multiple services with each service requiring their own database: 

| Database           | Description                                                                 | Variable             |
|--------------------|-----------------------------------------------------------------------------|----------------------|
| API Database       | Stores data related to Qodana’s API                                         | `${API_DATABASE}`    |
| Git Database       | Manages repositories and version control data                               | `${GIT_DATABASE}`    |
| Audit Database     | Handles audit logs and compliance data                                      | `${AUDIT_DATABASE}`  |
| Keycloak Database  | Optional. Used for authentication and authorization services like Keycloak  | `${APP_KC_DB_NAME}`  |

### Users and roles

Each service requires a dedicated PostgreSQL user for having access to its corresponding database. These users are 
assigned specific permissions to ensure security and proper data isolation:

| Database           | Description                                                            | Variable                        |
|--------------------|------------------------------------------------------------------------|---------------------------------|
| API User       | Read/write permissions for the API database                            | `${API_USER_NAME}`              |
| Linters API User       | Read-only permissions for certain tables                               | `${LINTERS_API_USER_NAME}`      |
| Report Processor User     | Read/write permissions for processing reports                          | `${REPORT_PROCESSOR_USER_NAME}` |
| Git User  | Full permissions for Git-related data                                  | `${GIT_USER_NAME}`              |
| Audit User  | Full permissions for audit logs                                        | `${AUDIT_USER_NAME}`            |
| Keycloak User  | Optional. Full ownership and permissions for the Keycloak database     | `${APP_KC_DB_USER}`             |

### Permissions

The following permission rules are applied to ensure proper access control:

* Users are granted access only to their respective databases.
* Default privileges are configured so that users automatically receive permissions on newly created objects like tables, sequences, and functions.
* Sensitive databases like an audit database are strictly controlled to prevent unauthorized access.

### Database organization

Each Qodana service (API, Git, Audit, Keycloak) should have its own database. This prevents data corruption, unauthorized access
between services, and lets you tune each database better to your needs.

Databases can be hosted on a single server or on different servers. A shared server is suitable for small-scale deployments 
with low traffic and minimal resource requirements. Separate servers are best suited for large-scale deployments or when 
handling highly sensitive data like audit logs or authentication.

### Security and compliance

Use strong, randomly generated passwords for all database users. Store credentials securely, such as in an environment 
variable manager or secret storage like HashiCorp Vault and others.

Restrict permissions to ensure users can only access their assigned databases. Avoid granting superuser or unnecessary privileges.

Enable logging for database activity to monitor access and changes, especially for the audit database.

### Backup and recovery

Implement a robust backup and recovery plan:
* Schedule regular automated backups for all databases.
* Test restoration processes regularly to ensure reliability.
* For critical data like audit logs and Keycloak, use frequent point-in-time recovery backups.

### Monitoring and maintenance

Use PostgreSQL monitoring tools like pgAdmin, Prometheus, or other to track database performance and health.

Periodically review database usage and clean up unused objects. Apply security updates and patches for PostgreSQL.

### Example SQL script for a single database server setup

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

## RabbitMQ

RabbitMQ acts as a message broker for various %product% services facilitating communication and task processing.

### Virtual hosts

Each %product% instance requires a dedicated virtual host to isolate messaging operations from other applications. 
Define a virtual host using the environment variable: `${RABBITMQ_VHOST}`. Example: `/qodana`

### Users

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

### Queues

%product% requires several durable queues for handling messaging related to reports, Git operations, and triggers. Create 
the following queues within the `${RABBITMQ_VHOST}` variable:

| Description                    | Name                                                | Example                              |
|--------------------------------|-----------------------------------------------------|--------------------------------------|
| Report queue                   | `${RABBITMQ_REPORTS_QUEUE_NAME};`                   | `qodanaCloudQueue`                   |
| Git contributor request queue  | `${GIT_RABBITMQ_CONTRIBUTORS_REQUEST_QUEUE_NAME};`  | `qodanaGetContributorsRequestQueue`  |
| Git contributor response queue | `${GIT_RABBITMQ_CONTRIBUTORS_RESPONSE_QUEUE_NAME};` | `qodanaGetContributorsResponseQueue` |
| Trigger queue                  | `${GIT_RABBITMQ_TRIGGERS_QUEUE_NAME};`              | `qodanaGitTriggersQueue`             |

All queues must be durable to ensure message persistence in case of RabbitMQ restarts.

### Permissions
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

### Example definition in JSON

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

## MinIO

%premlite% supports MinIO for object storage. %product% requires pre-signed URLs,
which lets %product% clients connect directly to a storage and upload artifacts for asynchronous processing or storage purposes.

%premlite% requires the `MINIO_RESULTS_BUCKET` and `MINIO_BASELINES_BUCKET` buckets, and they should be hosted on the 
same storage service. 

## OIDC provider

%premlite% does not provide a built-in user management module, so users should authenticate using an OIDC provider. 
%premlite% authorizes their actions according to permissions given to a specific user by an administrator. 

To get assistance with configuring an OIDC provider, please contact our support at <code>qodana-support@jetbrains.com</code>.

