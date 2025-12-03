# Public API

<var name="api-yaml" value="https://github.com/jetbrains-qodana/public-api/blob/main/openapi.yaml"/>
<var name="api-client" value="https://github.com/jetbrains-qodana/public-api/tree/main/samples/kotlin"/>

<show-structure for="chapter" depth="3"/>

<link-summary>The public API lets you create teams, projects, obtain a list of users and Insights data in %cloud% and %premlite% using 
your build pipelines.</link-summary>

The public API lets you create <a href="cloud-teams.topic">teams</a>, <a href="cloud-projects.topic">projects</a>,
obtain a list of %cloud% and %premlite% organization users and [](insights.md) data using your build pipelines. 
This feature is available only under the [Ultimate Plus license](pricing.md).

> The [OpenAPI file](%api-yaml%) and a [sample client](%api-client%) are available in a GitHub repository.

## Prerequisites

The public API requires an organization API token for authentication purposes.

Before using the public API, make sure that the following requirements were met:

<list>
<li>
    <p>To create and manage an organization API token, you should have access to an existing %cloud% organization 
       under the <code>Owner</code> or <code>Admin</code> <a href="cloud-user-roles.md" anchor="cloud-user-org-roles-owner">role</a>.</p> 
       <p>To learn how to create organizations, see the <a href="cloud-organizations.topic" anchor="cloud-organizations-create-organization"></a> chapter.</p>
</li>
<li>
    <p>Your %cloud% organization is licensed under the Ultimate Plus <a href="pricing.md">license</a> of %product%.</p>
</li>
<li>
    <p>To generate an organization API token, use the 
    <a href="cloud-organizations.topic" anchor="cloud-organizations-api-token"><control>API token</control> tab</a> of 
    your organization settings.</p>
</li>
<li>
<p>For API request examples provided in this section, replace the <code>{qodana_cloud_url}</code> placeholder with your 
base URL, i.e. with <code>qodana.cloud</code> for %cloud%, or using your custom base URL in case of %premlite%.</p>
</li>
</list>

In this section, an organization API token value is referred to as `$permanent_organization_token`.

<!-- 

Once an organization is created, you can extract the organization ID from the %cloud% or %premlite% URL: 

```curl
https://{qodana_cloud_url}/organizations/{organizationId}
```
-->

## Create teams and projects

To create a new team (if applicable) along with a project and obtain a [project token](project-token.md), send a `POST` request to the 
`https://{qodana_cloud_url}/api/v1/public/organizations/projects` endpoint and provide the team and project names, for example: 

```cURL
qodana_token=$(curl -X POST https://{qodana_cloud_url}/api/v1/public/organizations/projects \
  -H "Authorization: Bearer $permanent_organization_token" \
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
        <td>Description and examples</td>
    </tr>
    <tr>
        <td><code>200</code></td>
        <td>
            <p>Returns a <a href="project-token.md">project token</a> for an existing project within an existing team:</p>
        <code-block lang="http">
            HTTP/2 200 OK
            date: Wed, 24 Sep 2025 10:35:13 GMT
            content-type: application/json
            x-request-id: vbf3up0ktfm6b25o
            vary: Origin
            content-length: 178
            x-http2-stream-id: 3
            &nbsp;
            {
                "projectToken": "{TheProjectTokenValue}"
            }
        </code-block>
        </td>
    </tr>
    <tr>
        <td><code>201</code></td>
        <td>
            <p>Creates a new team (if applicable) and a new project within the team, generates and returns a <a href="project-token.md">project token</a> for a newly created project:</p>
        <code-block lang="http">
            HTTP/2 201 Created
            date: Wed, 24 Sep 2025 10:33:37 GMT
            content-type: application/json
            x-request-id: nrkvy1od9m3ohb9u
            vary: Origin
            content-length: 178
            x-http2-stream-id: 3
            &nbsp;
            {
                "projectToken": "{TheProjectTokenValue}"
            }    
            </code-block>
        </td>
    </tr>
    <tr>
        <td><code>400</code></td>
        <td>
            <p>Bad request response returns if the public API is disabled for a specific environment:</p>
        <code-block lang="http">
            HTTP/2 400 Bad Request
            date: Wed, 24 Sep 2025 10:36:37 GMT
            content-type: application/json
            x-request-id: 89ztzxra5ptt3vio
            vary: Origin
            content-length: 67
            x-http2-stream-id: 3
            &nbsp;
            {
                "name": "public_api_disabled",
                "details": "Public API is disabled"
            }
        </code-block>
            <p>This returns if the number of projects in the %cloud% organization exceeds 5000:</p>
        <code-block lang="http">
            HTTP/2 400 Bad Request
            date: Wed, 24 Sep 2025 10:36:37 GMT
            content-type: application/json
            x-request-id: 89ztzxra5ptt3vio
            vary: Origin
            content-length: 67
            x-http2-stream-id: 3
            &nbsp;
            {
                "name": "too_many_projects_for_organization",
                "details": "Creation of the project failed because of reaching the limit of projects per organization"
            }
        </code-block>
        </td>
    </tr>
    <tr>
        <td><code>401</code></td>
        <td>
            <p>Unauthorized access occurs if an API token was not provided:</p>
            <code-block lang="http">
            HTTP/2 401 Unauthorized
            date: Wed, 24 Sep 2025 10:36:37 GMT
            content-type: application/json
            x-request-id: 89zthxrm5pxt9phi
            vary: Origin
            content-length: 67
            x-http2-stream-id: 3
            &nbsp;
            {
                "name": "no_auth",
                "details": "User is not authorized"
            }
        </code-block>
        </td>
    </tr>
    <tr>
        <td><code>403</code></td>
        <td>
        <p>Access forbidden.</p>
        <p>This returns in case the API token is no longer valid:</p>
        <code-block lang="http">
            HTTP/2 403 Forbidden
            date: Wed, 24 Sep 2025 10:36:37 GMT
            content-type: application/json
            x-request-id: 89zthxrm5pxt9phi
            vary: Origin
            content-length: 67
            x-http2-stream-id: 3
            &nbsp;
            {
                "name": "no_permission",
                "details": "Invalid organization API token"
            }
        </code-block>
        <p>This returns in case the %cloud% organization cannot use the public API feature:</p>
        <code-block lang="http">
            HTTP/2 403 Forbidden
            date: Wed, 24 Sep 2025 10:36:37 GMT
            content-type: application/json
            x-request-id: 89zthxrm5pxt9phi
            vary: Origin
            content-length: 67
            x-http2-stream-id: 3
            &nbsp;
            {
                "name": "no_permission",
                "details": "User has no public_api_create_or_get_project_token permission"
            }
        </code-block>
        </td>
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
        <p>The internal server error returns if a project token could not be created:</p>
        <code-block lang="http">
            HTTP/2 500 Internal Server Error
            date: Wed, 24 Sep 2025 10:36:37 GMT
            content-type: application/json
            x-request-id: 89zthxrm5pxt9phi
            vary: Origin
            content-length: 67
            x-http2-stream-id: 3
            &nbsp;
            {
                "name": "project_token_creation_failed",
                "details": "Creation of the project token failed because of an internal error"
            }
        </code-block>
        </td>
    </tr>
</table>

## Get a list of organization users

To get a list of users of a specific [%cloud% organization](cloud-organizations.topic) in a paginated form, send a `GET` request using the
`https://{qodana_cloud_url}/api/v1/public/organizations/users` endpoint, for example: 

```cURL
curl -X GET \
   "https://{qodana_cloud_url}/api/v1/public/organizations/users" \
   -H "Authorization: Bearer $permanent_organization_token"
```

### Parameters

You can customize your requests using the following optional parameters.

<table>
    <tr>
        <td>Parameter</td>
        <td>Type</td>
        <td>Description</td>
    </tr>
    <tr>
        <td><code>limit</code></td>
        <td>Integer</td>
        <td>Limit the number of users in the returned list</td>
    </tr>
    <tr>
        <td><code>offset</code></td>
        <td>Number</td>
        <td>Set the offset for the returned list to <code>N</code>. For example, <code>1</code> means that the list will start from the second user</td>
    </tr>
    <tr>
        <td><code>order</code></td>
        <td>String</td>
        <td>Sort the order. Accepts <code>DESC</code> for descending order or <code>ASC</code> for ascending order. By default, lists are sorted in ascending order</td>
    </tr>
    <tr>
        <td><code>search</code></td>
        <td>String</td>
        <td>Return a list of entries that contain a specified substring in the <code>email</code> or <code>displayName</code> fields, see the <a anchor="Responses"/> chapter for details</td>
    </tr>
</table>

For example, this request returns ten user entries starting from the second entry only if those contain `abc`
in the `email` or `displayName` fields and sorts the selected list in descending order:

```cURL
curl -X GET \
   "https://{qodana_cloud_url}/api/v1/public/organizations/users?limit=10&offset=1&order=DESC&search=abc" \
   -H "Authorization: Bearer $permanent_organization_token"
```

### Responses

The `https://{qodana_cloud_url}/api/v1/public/organizations/users` endpoint responds as described in the table:

<table>
    <tr>
        <td>Response code</td>
        <td>Description and examples</td>
    </tr>
    <tr>
        <td><code>200</code></td>
        <td>
            <p>Returns a list of organization users for a specified %cloud% organization:</p>
        <code-block lang="http">
            HTTP/2 200 OK
            date: Wed, 24 Sep 2025 10:39:06 GMT
            content-type: application/json
            x-request-id: 7vrrlorq2ocrz957
            vary: Origin
            content-length: 514
            x-http2-stream-id: 3
            &nbsp;
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
        </code-block>
        </td>
    </tr>
    <tr>
        <td><code>400</code></td>
        <td>
            <p>The public API is disabled:</p>
        <code-block lang="http">
            HTTP/2 400 Bad Request
            date: Wed, 24 Sep 2025 10:36:37 GMT
            content-type: application/json
            x-request-id: 89ztzxra5ptt3vio
            vary: Origin
            content-length: 67
            x-http2-stream-id: 3
            &nbsp;
            {
                "name": "public_api_disabled",
                "details": "Public API is disabled"
            }
        </code-block>
        </td>
    </tr>
    <tr>
        <td><code>401</code></td>
        <td>
            <p>Unauthorized access occurs if an API token was not provided:</p>
            <code-block lang="http">
            HTTP/2 401 Unauthorized
            date: Wed, 24 Sep 2025 10:36:37 GMT
            content-type: application/json
            x-request-id: 89zthxrm5pxt9phi
            vary: Origin
            content-length: 67
            x-http2-stream-id: 3
            &nbsp;
            {
                "name": "no_auth",
                "details": "User is not authorized"
            }
        </code-block>
        </td>
    </tr>
    <tr>
        <td><code>403</code></td>
        <td>
        <p>Access forbidden.</p>
        <p>This returns in case an API token is no longer valid:</p>
        <code-block lang="http">
            HTTP/2 403 Forbidden
            date: Wed, 24 Sep 2025 10:36:37 GMT
            content-type: application/json
            x-request-id: 89zthxrm5pxt9phi
            vary: Origin
            content-length: 67
            x-http2-stream-id: 3
            &nbsp;
            {
                "name": "no_permission",
                "details": "Invalid organization API token"
            }
        </code-block>
        <p>This returns in case the %cloud% organization cannot use the public API feature:</p>
        <code-block lang="http">
            HTTP/2 403 Forbidden
            date: Wed, 24 Sep 2025 10:36:37 GMT
            content-type: application/json
            x-request-id: 89zthxrm5pxt9phi
            vary: Origin
            content-length: 67
            x-http2-stream-id: 3
            &nbsp;
            {
                "name": "no_permission",
                "details": "User has no public_api_get_organization_users permission"
            }
        </code-block>
        </td>
    </tr>
    <tr>
        <td><code>404</code></td>
        <td>
            <p>Endpoint not found</p>
        </td>
    </tr>
</table>
