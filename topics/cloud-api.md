# Public API

<var name="api-yaml" value="https://github.com/jetbrains-qodana/public-api/blob/main/openapi.yaml"/>
<var name="api-client" value="https://github.com/jetbrains-qodana/public-api/tree/main/samples/kotlin"/>

<show-structure for="chapter" depth="3"/>

<link-summary>The public API lets you create teams, projects, and obtain a list of users in %cloud% and %premlite% using 
your build pipelines.</link-summary>

The public API lets you create [teams](cloud-teams.topic), [projects](cloud-projects.topic) and obtain a list of users in %cloud% and %premlite% 
using your build pipelines. This feature is available only under the [Ultimate Plus license](pricing.md).

> The [OpenAPI file](%api-yaml%) and a [sample client](%api-client%) are available on a GitHub repository.

## Prerequisites

The public API requires a permanent organization API token for authentication purposes.

To be able to create and revoke API tokens, you should have a %cloud% organization, see the
[](cloud-organizations.topic#cloud-organizations-create-organization) chapter for details.

Once an organization is created, you can extract the organization ID from the %cloud% or %premlite% URL: 

```curl
https://{qodana.cloud.url}/organizations/{organizationId}
```

Here and later in this section, `{qodana.cloud.url}` denotes a base URL and accepts:

* `qodana.cloud` in case of %cloud%
* Your custom base URL in case of %premlite%

## Generate and manage API tokens

> To be able to manage and API tokens, a %cloud% or %premlite% user should have the `OWNER` role in your organization, see the 
> [role description](cloud-user-roles.md#cloud-user-org-roles-owner) in the %cloud% documentation.
{style="note"}

You can generate, regenerate and delete an organization API token using the API token tab of your organization settings, see the 
[](cloud-organizations.topic#cloud-organizations-overview) chapter for details.

In this section, an organization API token value is referred to as `$PERMANENT_ORGANIZATION_TOKEN`. 

## Create teams and projects

To create a new team and project and obtain its [project token](project-token.md), send a `POST` request using the 
`https://{qodana.cloud.url}/v1/public/organizations/teams/projects` endpoint, for example: 

```cURL
QODANA_TOKEN=$(curl -X POST https://{qodana.cloud.url}/v1/public/organizations/projects \
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
`https://{qodana.cloud.url}/v1/public/organizations/users` endpoint, for example: 

```cURL
curl -X GET \
   "https://{qodana.cloud.url}/v1/public/organizations/users?limit=10" \
   -H "Authorization: Bearer $PERMANENT_ORGANIZATION_TOKEN" \
   -H "Content-Type: application/json"
```

Here is the list of accepted parameters:

<!-- The description of parameters is required here -->

| Parameter | Type    | Required | Description                |
|-----------|---------|----------|----------------------------|
| `offset`  | Number  | No       | List of organization users |
| `limit`   | Integer | No       | Unauthorized               |
| `order`   | String  | No       | Forbidden                  |
| `search`  | String  | No       | Forbidden                  |



<!-- Example response containing all parameters is required here -->

This is the list of response codes:

| Response code   | Description                |
|-----------------|----------------------------|
| `200`           | List of organization users |
| `401`           | Unauthorized               |
| `403`           | Forbidden                  |
