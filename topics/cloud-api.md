# Public API

<var name="api-yaml" value="https://github.com/jetbrains-qodana/public-api/blob/main/openapi.yaml"/>

<show-structure for="chapter" depth="3"/>

<link-summary>The public API lets you create teams and projects in %cloud% and %premlite% using your build pipelines.</link-summary>

The public API lets you create [teams](cloud-teams.topic) and [projects](cloud-projects.topic) in %cloud% and %premlite% 
using your build pipelines. 
The `openapi.yaml` file containing the description is available on the [GitHub](%api-yaml%) repository, and  
the sample client based on this file is also available in the `samples/kotlin` directory of the repository.

## Prerequisites

The public API requires a permanent organization API token for authentication purposes.

To be able to create and revoke API tokens, you should have an organization ID. To learn how to create an organization, see the
[](cloud-organizations.topic#cloud-organizations-create-organization) chapter.

Once an organization is created, you can extract the organization ID from the %cloud% or %premlite% URL: 

```curl
https://{qodana.cloud.url}/organizations/{organizationId}
```

### Obtain and revoke API tokens

> To generate and revoke API tokens, a %cloud% or %premlite% user should have the `OWNER` role in your organization, see the 
> [role description](cloud-user-roles.md#cloud-user-org-roles-owner) in the %cloud% documentation.
{style="note"}

You can generate an organization API token by sending the following request: 

```cURL
curl -X POST \
   https://api.qodana.cloud/v1/organizations/{organizationId}/tokens \
   -H "Authorization: Bearer YOUR_PERMANENT_ORGANIZATION_TOKEN" \
   -H "Content-Type: application/json"
```

Here, `{organizationId}` represents the ID of your [organization](cloud-organizations.topic). 

To revoke the API token, send the following request:

```cURL
curl -X DELETE \
   https://api.qodana.cloud/v1/organizations/{organizationId}/tokens \
   -H "Authorization: Bearer YOUR_PERMANENT_ORGANIZATION_TOKEN" \
   -H "Content-Type: application/json"
```

## Create teams and projects

To create a new team and project and obtain its [project token](project-token.md), send a `POST` request using the 
`https://api.qodana.cloud/v1/public/organizations/teams/projects` endpoint, for example: 

```cURL
QODANA_TOKEN=$(curl -X POST https://api.qodana.cloud/v1/public/organizations/projects \
  -H "Authorization: Bearer $PERMANENT_ORGANIZATION_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
        "projectName": "$REPOSITORY_NAME",
        "teamName": "$TEAM_NAME"
      }')
```

In this request, under the `teamName` parameter provides a string non-nullable name of the team that you would like to 
create. In case a team with such name already exists, creation of a new team will be skipped. 
Under the `projectName` parameter, provide a string non-nullable name of the project that you would like to create. In 
case a project with such name already exists, creation of a new project will be skipped.

As a response, a [project token](project-token.md) for a newly generated project will be returned. You can use 
the project token while running %product%.

This is the list of response codes:

| Response code   | Description                                       |
|-----------------|---------------------------------------------------|
| `200`           | Created project token for the existing project    |
| `201`           | Created project token for a newly created project |
| `400`           | Bad Request                                       |
| `401`           | Unauthorized                                      |
| `403`           | Forbidden                                         |
| `404`           | Not found                                         |
| `500`           | Internal server error                             |

## Get a list of users

To get a list of users of a specific organization in a paginated form, send a `GET` request using the
`https://api.qodana.cloud/v1/public/organizations/users` endpoint, for example: 

```cURL
curl -X GET \
   "https://api.qodana.cloud/v1/public/organizations/users?limit=10" \
   -H "Authorization: Bearer YOUR_PERMANENT_ORGANIZATION_TOKEN" \
   -H "Content-Type: application/json"
```

This is the list of response codes:

| Response code   | Description                |
|-----------------|----------------------------|
| `200`           | List of organization users |
| `401`           | Unauthorized               |
| `403`           | Forbidden                  |
