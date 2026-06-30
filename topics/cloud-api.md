# Qodana Cloud API

<var name="api-yaml" value="https://github.com/jetbrains-qodana/public-api/blob/main/openapi.yaml"/>
<var name="api-client" value="https://github.com/jetbrains-qodana/public-api/tree/main/samples/kotlin"/>

<show-structure for="chapter" depth="3"/>

<link-summary>The Qodana Cloud API lets you create teams, projects, obtain a list of users and Insights data in %cloud% and %premlite% using 
your build pipelines.</link-summary>

The Qodana Cloud API lets you create <a href="cloud-teams.topic">teams</a>, <a href="cloud-projects.topic">projects</a>,
obtain a list of %cloud% and %premlite% organization users and [](insights.md) data using your build pipelines. 
This API is available on the Ultimate Plus [license](pricing.md). To learn more about available %product% licenses, 
visit the [Subscription Options and Pricing](https://www.jetbrains.com/qodana/buy/?billing=yearly) page.
You can also [request a demo](https://www.jetbrains.com/qodana/request-a-demo/).

> The [OpenAPI file](%api-yaml%) and a [sample client](%api-client%) are available in a GitHub repository.

## Prerequisites

The Qodana Cloud API requires an organization API token for authentication purposes.

Before using the Qodana Cloud API, make sure that the following requirements were met:

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
    your organization settings. This token should be referred in requests as the <code>$permanent_organization_token</code> authorization header, i.e.:</p> 
<code-block lang="cURL">-H "Authorization: Bearer $permanent_organization_token"</code-block>
</li>
<li>
<p>All API request examples provided in this section require that you use either the <code>https://qodana.cloud</code> 
URL for %cloud% or your custom base URL in case of %premlite%. For simplicity, the %cloud% URL is used.</p>
</li>
</list>

## Teams and projects

### Create teams and projects

To create a new team (if applicable) along with a project and get a [project token](project-token.md), send the request: 

```cURL
POST https://qodana.cloud/api/v1/public/organizations/projects
```

Here is the description of the request body:

| Parameter     | Type      | Description                                                                                               | Example value     |
|---------------|-----------|-----------------------------------------------------------------------------------------------------------|-------------------|
| `teamName`    | String    | Non-nullable name of the [team](cloud-teams.topic) to create. If exists, creation will be skipped         | `My team name`    |
| `projectName` | String    | Non-nullable name of the [project](cloud-projects.topic) to create. If exists, creation will be skipped   | `My project name` |

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
            <p>Bad request response returns if the Qodana Cloud API is disabled for a specific environment:</p>
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
                "name": "PUBLIC_API_DISABLED",
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
                "name": "TOO_MANY_PROJECTS_FOR_ORGANIZATION",
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
                "name": "NO_AUTH",
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
                "name": "NO_PERMISSION",
                "details": "Invalid organization API token"
            }
        </code-block>
        <p>This returns in case the %cloud% organization cannot use the Qodana Cloud API feature:</p>
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
                "name": "NO_PERMISSION",
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
                "name": "PROJECT_TOKEN_CREATION_FAILED",
                "details": "Creation of the project token failed because of an internal error"
            }
        </code-block>
        </td>
    </tr>
</table>

### Get project metadata by project name
{id="cloud-api-project-report-metadata-project-name"}

To get project metadata for the default branch of a project, send the request with a %cloud% project name:

```cURL
GET https://qodana.cloud/api/v1/public/organizations/projects?projectName={projectName}
```

Here is the description of accepted parameters:

| Parameter     | Type   | Required  | Description                     | Example value        |
|---------------|--------|-----------|---------------------------------|----------------------|
| `projectName` | String | No        | Name of the project to retrieve | `My Awesome Project` |

Here is the description of responses:

<table>
    <tr>
        <td>Response code</td>
        <td>Description and examples</td>
    </tr>
    <tr>
        <td><code>200</code></td>
        <td>
            <p>Returns a JSON object containing project metadata:</p>
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
              "id": "proj_123",
              "name": "My Awesome Project",
              "teamId": "team_456",
              "teamName": "Dev Team A",
              "defaultBranchName": "main",
              "latestFullScanReport": {
                "id": "report_789",
                "timestamp":"2026-05-28T14:34:52.935342Z",
                "licenseAudit": {
                  "isPassed": true,
                  "isEnabled": true
                },
                "codeCoverage": {
                  "percentage": 85,
                  "isEnabled": true
                },
                "inspections": [
                  {
                    "id": "insp_12345",
                    "name": "Security Scan",
                    "severity": "HIGH",
                    "baseline": 10,
                    "actual": 5
                  }
                ]
              }
            }
        </code-block>
        </td>
    </tr>
    <tr>
        <td><code>400</code></td>
        <td>
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
              "name": "VALIDATION_FAILED",
              "details": "Invalid projectName: must be a non-empty string."
            }
        </code-block>
        </td>
    </tr>
    <tr>
        <td><code>401</code></td>
        <td>
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
              "name": "NO_CREDENTIALS_PROVIDED",
              "details": "API token is required."
            }
        </code-block>
        </td>
    </tr>
    <tr>
        <td><code>403</code></td>
        <td>
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
              "name": "NO_PERMISSION",
              "details": "User does not have permission to view projects."
            }
        </code-block>
        </td>
    </tr>
    <tr>
        <td><code>404</code></td>
        <td>
            <code-block lang="http">
                HTTP/2 404 Not Found
                date: Wed, 24 Sep 2025 10:36:37 GMT
                content-type: application/json
                x-request-id: 89zthxrm5pxt9phi
                vary: Origin
                content-length: 67
                x-http2-stream-id: 3
                &nbsp;
                {
                  "name": "NO_PROJECT",
                  "details": "Project 'nonexistent-project' not found."
                }
            </code-block>
        </td>
    </tr>
</table>

### Get project metadata by project ID
{id="cloud-api-project-report-metadata-project-id"}

Get project metadata by sending a request containing a project ID:

```cURL
GET https://qodana.cloud/api/v1/public/organizations/projects/{projectID}
```

| Parameter   | Type   | Required  | Description       | Example value |
|-------------|--------|-----------|-------------------|---------------|
| `projectId` | String | Yes       | ID of the project | `proj_123`    |

Here is the description of responses:

<table>
    <tr>
        <td>Response code</td>
        <td>Description and examples</td>
    </tr>
    <tr>
        <td><code>200</code></td>
        <td>
            <p>Returns a JSON object containing project metadata:</p>
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
              "id": "proj_123",
              "name": "My Awesome Project",
              "teamId": "team_456",
              "teamName": "Dev Team A",
              "defaultBranchName": "main",
              "latestFullScanReport": {
                "id": "report_789",
                "timestamp":"2026-05-28T14:34:52.935342Z",
                "licenseAudit": {
                  "isPassed": true,
                  "isEnabled": true
                },
                "codeCoverage": {
                  "percentage": 85,
                  "isEnabled": true
                },
                "inspections": [
                  {
                    "id": "insp_12345",
                    "name": "Security Scan",
                    "severity": "HIGH",
                    "baseline": 10,
                    "actual": 5
                  }
                ]
              }
            }
        </code-block>
        </td>
    </tr>
    <tr>
        <td><code>400</code></td>
        <td>
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
              "name": "VALIDATION_FAILED",
              "details": "Invalid projectId: must be a non-empty string."
            }
        </code-block>
        </td>
    </tr>
    <tr>
        <td><code>401</code></td>
        <td>
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
              "name": "NO_CREDENTIALS_PROVIDED",
              "details": "API token is required."
            }
        </code-block>
        </td>
    </tr>
    <tr>
        <td><code>403</code></td>
        <td>
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
              "name": "NO_PERMISSION",
              "details": "User does not have permission to view this project."
            }
        </code-block>
        </td>
    </tr>
    <tr>
        <td><code>404</code></td>
        <td>
            <code-block lang="http">
                HTTP/2 404 Not Found
                date: Wed, 24 Sep 2025 10:36:37 GMT
                content-type: application/json
                x-request-id: 89zthxrm5pxt9phi
                vary: Origin
                content-length: 67
                x-http2-stream-id: 3
                &nbsp;
                {
                  "name": "NO_PROJECT",
                  "details": "Project with ID 'proj_999' not found."
                }
            </code-block>
        </td>
    </tr>
</table>

## Users
{id="cloud-api-users"}

To list users of a specific [%cloud% organization](cloud-organizations.topic) in a paginated form, send the request: 

```cURL
GET https://qodana.cloud/api/v1/public/organizations/users
```

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
        <td>Sets the sort order users' email addresses. Accepts <code>DESC</code> for descending order or <code>ASC</code> for ascending order. By default, lists are sorted in ascending order</td>
    </tr>
    <tr>
        <td><code>search</code></td>
        <td>String</td>
        <td>Return a list of entries that contain a specified substring in the <code>email</code> or <code>displayName</code> fields</td>
    </tr>
</table>

For example, this request returns ten user entries starting from the second entry only if those contain `abc`
in the `email` or `displayName` fields and sorts the selected list in descending order:

```cURL
curl -X GET \
   "https://qodana.cloud/api/v1/public/organizations/users?limit=10&offset=1&order=DESC&search=abc" \
   -H "Authorization: Bearer $permanent_organization_token"
```

This endpoint responds as described in the table:

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
                        "invitationId": "G4O3Y",
                        "invitationUrl": "https://qodana.cloud/invite/G4O3Y"
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
                        "invitationId": "bLmWV",
                        "invitationUrl": "https://qodana.cloud/invite/bLmWV"
                    }
                ]
            }
        </code-block>
        </td>
    </tr>
    <tr>
        <td><code>400</code></td>
        <td>
            <p>The Qodana Cloud API is disabled:</p>
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
                "name": "PUBLIC_API_DISABLED",
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
                "name": "NO_AUTH",
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
                "name": "NO_PERMISSION",
                "details": "Invalid organization API token"
            }
        </code-block>
        <p>This returns in case the %cloud% organization cannot use the Qodana Cloud API feature:</p>
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
                "name": "NO_PERMISSION",
                "details": "User has no public_api_get_organization_users permission"
            }
        </code-block>
        </td>
    </tr>
</table>


## Inspections
{id="cloud-api-inspections"}

List all inspections including FlexInspect inspections used by an organization by sending the request:

```cURL
GET https://qodana.cloud/api/v1/public/organizations/inspections
```

This endpoint does not provide any parameters.

Here is the description of responses:

<table>
    <tr>
        <td>Response code</td>
        <td>Description and examples</td>
    </tr>
    <tr>
        <td><code>200</code></td>
        <td>
            <p>Returns a list of inspections:</p>
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
              "inspections": [
                {
                  "id": "insp_12345",
                  "name": "Security Scan"
                },
                {
                  "id": "insp_67890",
                  "name": "Code Quality"
                }
              ]
            }
        </code-block>
        </td>
    </tr>
    <tr>
        <td><code>400</code></td>
        <td>
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
              "name": "VALIDATION_FAILED",
              "details": "Invalid query parameter."
            }
        </code-block>
        </td>
    </tr>
    <tr>
        <td><code>401</code></td>
        <td>
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
              "name": "NO_AUTH",
              "details": "Authentication required to access inspections."
            }
        </code-block>
        </td>
    </tr>
    <tr>
        <td><code>403</code></td>
        <td>
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
                "name": "NO_PERMISSION",
                "details": "Invalid organization API token"
            }
        </code-block>
        </td>
    </tr>
</table>

## Insights
{id="cloud-api-insights"}

### Project Insights
{id="cloud-api-insights-project"}

To retrieve project insights, send the request:

```cURL
POST https://qodana.cloud/api/v1/public/organizations/project-insights/query
```

Here is the description of the request body:

| Parameter              | Type          | Required  | Description                                                 | Example value                                                      |
|------------------------|---------------|-----------|-------------------------------------------------------------|--------------------------------------------------------------------|
| `includeProjectIds`    | array[string] | No        | List of project IDs to include in the query                 | `["Dg9Ca", "Ec3Bb"]`                                               |
| `includeInspectionIds` | array[string] | No        | List of inspection IDs to include in the query              | `["ReplaceMapGetOrDefault", "ObjectPrivatePropertyName"]`          |
| `includeTeamIds`       | array[string] | No        | List of team IDs to include in the query                    | `["2rcq6", "3hen0"]`                                               |
| `timeRange`            | object        | No        | Time range for the query. Contains start and end timestamps | `{"start": "2026-01-01T00:00:00Z", "end": "2026-05-12T00:00:00Z"}` |


Here is the description of responses:

<table>
    <tr>
        <td>Response code</td>
        <td>Description and examples</td>
    </tr>
    <tr>
        <td><code>200</code></td>
        <td>
            <p>A list of projects with scan data for the given timestamp, where one entry exists for each unique
combination of project ID and timestamp. If no time range is specified, entries at the latest timestamp are returned:</p>
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
              "projects": [
                {
                  "id": "proj_123",
                  "name": "My Awesome Project",
                  "teamId": "team_456",
                  "teamName": "Dev Team A",
                  "codeCoverage": {
                    "percentage": 85,
                    "isEnabled": true
                  },
                  "licenseAudit": {
                    "isPassed": true,
                    "isEnabled": true
                  },
                  "severityToActualProblems": {
                    "info": 5,
                    "low": 10,
                    "moderate": 3,
                    "high": 1,
                    "critical": 0,
                    "total": 19
                  },
                  "severityToBaselineProblems": {
                    "info": 8,
                    "low": 12,
                    "moderate": 5,
                    "high": 2,
                    "critical": 0,
                    "total": 27
                  },
                  "timestamp": "2026-05-12T00:00:00Z"
                }
              ]
            }
        </code-block>
        </td>
    </tr>
    <tr>
        <td><code>400</code></td>
        <td>
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
              "name": "NO_FILTER_SELECTION",
              "details": "At least one filter (includeProjectIds, includeInspectionIds, or includeTeamIds) must be provided."
            }
        </code-block>
        </td>
    </tr>
    <tr>
        <td><code>401</code></td>
        <td>
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
              "name": "INVALID_TOKEN",
              "details": "The provided API token is expired or invalid."
            }
        </code-block>
        </td>
    </tr>
    <tr>
        <td><code>403</code></td>
        <td>
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
              "name": "FEATURE_NOT_SUPPORTED",
              "details": "Project insights are not enabled for this organization."
            }
        </code-block>
        </td>
    </tr>
</table>


### Inspection Insights
{id="cloud-api-insights-inspection"}

To retrieve inspection insights, send the request:

```cURL
POST https://qodana.cloud/api/v1/public/organizations/inspection-insights/query
```

Here is the description of the request body:

| Parameter              | Type          | Required  | Description                                                 | Example value                                                      |
|------------------------|---------------|-----------|-------------------------------------------------------------|--------------------------------------------------------------------|
| `includeProjectIds`    | array[string] | No        | List of project IDs to include in the query                 | `["proj_123", "proj_456"]`                                         |
| `includeInspectionIds` | array[string] | No        | List of inspection IDs to include in the query              | `["insp_123", "insp_456"]`                                         |
| `includeTeamIds`       | array[string] | No        | List of team IDs to include in the query                    | `["team_123", "team_456"]`                                         |
| `timeRange`            | object        | No        | Time range for the query. Contains start and end timestamps | `{"start": "2026-01-01T00:00:00Z", "end": "2026-05-12T00:00:00Z"}` |

Here is the description of responses:

<table>
    <tr>
        <td>Response code</td>
        <td>Description and examples</td>
    </tr>
    <tr>
        <td><code>200</code></td>
        <td>
            <p>A list of inspections counts, where one entry exists for each unique combination of inspection ID, name, severity, baseline, actual and timestamp. If a time range is specified, entries for 10 equally distant timestamps within the range are returned. If no time range is specified, entries at the latest timestamp are returned.</p>
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
              "inspections": [
                {
                  "id": "insp_12345",
                  "name": "Security Scan",
                  "severity": "HIGH",
                  "baseline": 10,
                  "actual": 5,
                  "timestamp": "2026-05-12T00:00:00Z"
                },
                {
                  "id": "insp_67890",
                  "name": "Code Quality",
                  "severity": "MODERATE",
                  "baseline": 20,
                  "actual": 15,
                  "timestamp": "2026-05-12T00:00:00Z"
                }
              ]
            }
        </code-block>
        </td>
    </tr>
    <tr>
        <td><code>400</code></td>
        <td>
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
              "name": "VALIDATION_FAILED",
              "details": "Invalid timeRange: 'end' must be after 'start'."
            }
        </code-block>
        </td>
    </tr>
    <tr>
        <td><code>401</code></td>
        <td>
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
              "name": "NO_CREDENTIALS_PROVIDED",
              "details": "Authentication token is missing or invalid."
            }
        </code-block>
        </td>
    </tr>
    <tr>
        <td><code>403</code></td>
        <td>
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
              "name": "NO_PERMISSION",
              "details": "User does not have permission to query inspection insights."
            }
        </code-block>
        </td>
    </tr>
</table>
