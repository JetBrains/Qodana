# Public API

<var name="api-yaml" value="https://github.com/jetbrains-qodana/public-api/blob/main/openapi.yaml"/>
<var name="api-client" value="https://github.com/jetbrains-qodana/public-api/tree/main/samples/kotlin"/>

<show-structure for="chapter" depth="3"/>

<link-summary>The Public API lets you create teams, projects, and obtain a list of users in %cloud% and %premlite% using 
your build pipelines.</link-summary>

The Public API lets you create [teams](cloud-teams.topic), [projects](cloud-projects.topic) and obtain a list of users in %cloud% and %premlite% 
using your build pipelines. This feature is available only under the [Ultimate Plus license](pricing.md).

> The [OpenAPI file](%api-yaml%) and a [sample client](%api-client%) are available on a GitHub repository.

## Prerequisites

The Public API requires a permanent organization API token for authentication purposes.

Before using the Public API, make sure that the following requirements were met:

* You have access to an existing %cloud% organization under the `OWNER` [role](cloud-user-roles.md#cloud-user-org-roles-owner). To learn how to create organizations, see the [](cloud-organizations.topic#cloud-organizations-create-organization) chapter.
* Your %cloud% organization is licensed under the Ultimate Plus [license](pricing.md) of %product%.
* To generate a permanent organization API token, use the **API token** tab of your organization settings, see the [](cloud-organizations.topic#cloud-organizations-overview) chapter for details.
* In API request examples provided in this section, replace the `{qodana.cloud.url}` placeholder with your base URL, i.e. with `qodana.cloud` for %cloud%, or using your custom base URL in case of %premlite%.

In this section, an organization API token value is referred to as `$PERMANENT_ORGANIZATION_TOKEN`.

<!-- 

Once an organization is created, you can extract the organization ID from the %cloud% or %premlite% URL: 

```curl
https://{qodana.cloud.url}/organizations/{organizationId}
```
-->

## Create teams and projects

To create a new team (if applicable) along with a project and obtain a [project token](project-token.md), send a `POST` request to the 
`https://{qodana.cloud.url}/api/v1/public/organizations/teams/projects` endpoint and provide the team and project names, for example: 

```cURL
QODANA_TOKEN=$(curl -X POST https://{qodana.cloud.url}/api/v1/public/organizations/projects \
  -H "Authorization: Bearer $PERMANENT_ORGANIZATION_TOKEN" \
  -d '{
        "projectName": "My project name",
        "teamName": "My team name"
      }')
```

The `teamName` parameter provides a string non-nullable name of the [team](cloud-teams.topic) that you would like to
create. In case a team with such name already exists, creation of a new team will be skipped.
Under the `projectName` parameter, provide a string non-nullable name of the [project](cloud-projects.topic) that you would like to create. In
case a project with such name already exists, creation of a new project will be skipped.

The endpoint provides the responses with the following HTTP codes:

<table>
    <tr>
        <td>Response code</td>
        <td>Description</td>
        <td>Response example</td>
    </tr>
    <tr>
        <td><code>200</code></td>
        <td>
            <p>Returns a <a href="project-token.md">project token</a> for an existing project within an existing team.</p>
        </td>
        <td>
        <code-block lang="http">
            HTTP/2 200 OK
            date: Wed, 24 Sep 2025 10:35:13 GMT
            content-type: application/json
            x-request-id: vbf3up0ktfm6b25o
            vary: Origin
            content-length: 178
            x-http2-stream-id: 3
            {
                "projectToken": "{TheProjectTokenValue}"
            }
        </code-block>
        </td>
    </tr>
    <tr>
        <td><code>201</code></td>
        <td>
            <p>Creates a new team (if applicable) and a new project within the team, generates and returns a <a href="project-token.md">project token</a> for the newly created project.</p>
        </td>
        <td>
        <code-block lang="http">
            HTTP/2 201 Created
            date: Wed, 24 Sep 2025 10:33:37 GMT
            content-type: application/json
            x-request-id: nrkvy1od9m3ohb9u
            vary: Origin
            content-length: 178
            x-http2-stream-id: 3
            {
                "projectToken": "{TheProjectTokenValue}"
            }    
            </code-block>
        </td>
    </tr>
    <tr>
        <td><code>400</code></td>
        <td>
            <p>Bad request</p>
        </td>
        <td></td>
    </tr>
    <tr>
        <td><code>401</code></td>
        <td>
            <p>Unauthorized access</p>
        </td>
        <td>
        <code-block lang="http">
            HTTP/2 401 Unauthorized
            date: Wed, 24 Sep 2025 10:36:37 GMT
            content-type: application/json
            x-request-id: 89zthxrm5pxt9phi
            vary: Origin
            content-length: 67
            x-http2-stream-id: 3
            {
                "name": "invalid_token",
                "details": "Invalid organization API token"
            }
        </code-block>
        </td>
    </tr>
    <tr>
        <td><code>403</code></td>
        <td>
            <p>Access forbidden</p>
        </td>
        <td></td>
    </tr>
    <tr>
        <td><code>404</code></td>
        <td>
            <p>Endpoint not found</p>
        </td>
    </tr>
    <tr>
        <td><code>500</code></td>
        <td>
            <p>The internal server error, the request cannot be processed</p>
        </td>
        <td></td>
    </tr>
</table>

## Get a list of users

To get a list of users of a specific [%cloud% organization](cloud-organizations.topic) in a paginated form, send a `GET` request using the
`https://{qodana.cloud.url}/api/v1/public/organizations/users` endpoint, for example: 

```cURL
curl -X GET \
   "https://{qodana.cloud.url}/api/v1/public/organizations/users" \
   -H "Authorization: Bearer $PERMANENT_ORGANIZATION_TOKEN"
```

### Parameters

You can specify your requests by using the following optional parameters.

<table>
    <tr>
        <td>Parameter</td>
        <td>Type</td>
        <td>Description</td>
    </tr>
    <tr>
        <td><code>limit</code></td>
        <td>Integer</td>
        <td>Limit the number of users in a list</td>
    </tr>
    <tr>
        <td><code>offset</code></td>
        <td>Number</td>
        <td>Set the offset for the returned list to <code>N</code>. For example, <code>1</code> means that the list will start from the second user</td>
    </tr>
    <tr>
        <td><code>order</code></td>
        <td>String</td>
        <td>Sort the order. Accepts <code>DESC</code> for descending order or <code>ASC</code> for ascending order. By default, the list is sorted in ascending order</td>
    </tr>
    <tr>
        <td><code>search</code></td>
        <td>String</td>
        <td>Return a list of entries that contain a specified substring in the <code>email</code> or <code>displayName</code> fields, see the <a anchor="Responses"/> chapter for details</td>
    </tr>
</table>

For example; this request selects ten entries from the database starting from the second entry only if they contain `abc`
in the `email` or `displayName` fields and sorts the selected list in descending order:

```cURL
curl -X GET \
   "https://{qodana.cloud.url}/api/v1/public/organizations/users?limit=10&offset=1&order=DESC&search=abc" \
   -H "Authorization: Bearer $PERMANENT_ORGANIZATION_TOKEN"
```

### Responses

The endpoint provides responses with the following response codes:

| Response code | Description                |
|--------------|----------------------------|
| `200`        | List of organization users |
| `401`        | Unauthorized               |
| `403`        | Forbidden                  |


#### List of organization users

This is an example of response HTTP code `200` with comments:

```HTTP
HTTP/2 200 OK
date: Wed, 24 Sep 2025 10:39:06 GMT
content-type: application/json
x-request-id: 7vrrlorq2ocrz957
vary: Origin
content-length: 514
x-http2-stream-id: 3
{
    "count": 3, // The number of entries retrieved
    "next": 3,  // The `offset` value to fetch the next chunk of entries
    "prev": 0, // The offset from the first entry
    "items": [
       {
           "id": "GoKgG",
           "email": "email-address1@example.com",
           "displayName": "email-address1@example.com",
           "role": "OWNER", // %cloud% role
           "isActive": true,
           "isSsoManaged": false, // SSO feature is disabled
           "invitationId": "G4O3Y" //
       },
       {
           "id": "bvWmV",
           "email": "email-address2@example.com",
           "displayName": "email-address2@example.com",
           "role": "VIEWER",
           "isActive": false,
           "isSsoManaged": false
       },
       {
           "id": "NG4kY",
           "email": "email-address3@example.com",
           "displayName": "email-address3@example.com",
           "role": "VIEWER",
           "isActive": false,
           "isSsoManaged": false,
           "invitationId": "bLmWV"
       }
    ]
}
```

#### Other response examples

Here is an example of response containing HTTP code `401` (unauthorized):

<code-block lang="http">
    HTTP/2 401 Unauthorized
    date: Wed, 24 Sep 2025 10:50:12 GMT
    content-type: application/json
    x-request-id: y9us5cl4qnuj4lhu
    vary: Origin
    content-length: 67
    x-http2-stream-id: 3
    {
        "name": "invalid_token",
        "details": "Invalid organization API token"
    }
</code-block>

Here is the example of response containing HTTP code `403` (forbidden):

<!-- This should be provided too -->