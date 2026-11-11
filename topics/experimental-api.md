# Experimental API

<show-structure for="chapter" depth="3"/>

The experimental API helps you solve the following tasks: 

* Identify dependencies across organization projects
* Filter [project insights](insights.md) by specific [vulnerability IDs](https://nvd.nist.gov/vuln)
* Retrieve the latest project report in SARIF format for a specific branch

<note>
The API is experimental, which means no long-term support. Instead, we will deprecate APIs that become obsolete. 
We will continue to support deprecated APIs for at least three months.
</note>

## Prerequisites

The experimental API requires an organization API token for authentication purposes.

Before using the experimental API, make sure that the following requirements were met:

<list>
<li>
    <p>Your %cloud% organization is licensed under the Ultimate Plus <a href="pricing.md">license</a> of %product%.</p>
</li>
<li>
    <p>You have an organization API token. To generate a token, on the organization setting page of %cloud%, use the 
<a href="cloud-organizations.topic" anchor="cloud-organizations-api-token"><control>API token</control></a> tab. 
Generating a token requires the organization <code>Owner</code> or <code>Admin</code> <a href="cloud-user-roles.md" anchor="cloud-user-org-roles-owner">role</a> in %cloud%.</p>
</li>
<li>
    <p>To authorize API requests, use the organization API token as an <code>Authorization</code> header bearer token:</p> 
    <code-block lang="HTTP">Authorization: Bearer $organization_API_token</code-block>
</li>
<li>
<p>Use <code>https://qodana.cloud</code> as the base URL for %cloud% API requests.  
If you use %premlite%, replace this with your custom base URL.</p>
</li>
</list>

## Get project dependencies

The dependency data returned by the experimental API matches an
SPDX/JSON file available using the [**Download license list**](ui-overview.md#ui-overview-project-audit) button in %cloud%.

To return a SPDX/JSON dependency list to a specific %cloud% project, send the following `GET` request:

```http
GET /api/experimental/organizations/projects/{projectID}/dependencies HTTP/1.1
Accept: application/spdx+json
```

Here is the description of the accepted parameter:

| Parameter   | Type   | Required  | Description       | Example value |
|-------------|--------|-----------|-------------------|---------------|
| `projectId` | String | Yes       | ID of the project | `Abc12`    |

The accepted `Accept` values are absent, `application/json` or `application/spdx+json`.

If the stored object exists, the API responds with a redirect to a presigned URL to 
the `projectStructure/thirdPartySoftwareList.json` file; otherwise it returns `204 No Content`.

## Get project insights by vulnerability IDs
{id="experimental-api-insights-project"}

<link-summary>Explore how to get project insights of a specific %cloud% organization using the experimental API.</link-summary>

To retrieve project insights by vulnerability IDs, send the following `POST` request:

```cURL
POST /api/experimental/organizations/project-insights/query
```

Here is the description of the request body:

| Parameter              | Type          | Required  | Description                                                 | Example value                                                      |
|------------------------|---------------|-----------|-------------------------------------------------------------|--------------------------------------------------------------------|
| `includeProjectIds`    | array[string] | No        | List of project IDs to include in the query                 | `["Dg9Ca", "Ec3Bb"]`                                               |
| `includeInspectionIds` | array[string] | No        | List of inspection IDs to include in the query              | `["ReplaceMapGetOrDefault", "ObjectPrivatePropertyName"]`          |
| `includeTeamIds`       | array[string] | No        | List of team IDs to include in the query                    | `["2rcq6", "3hen0"]`                                               |
|`includeVulnerabilityIds`| array[string] | No | List of [vulnerability IDs](https://nvd.nist.gov/vuln) to include in the query | `["CVE-2026-109618", "CVE-2026-109619"]` |
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


## Retrieve latest SARIF report
{id="experimental-api-retrieve-sarif"}

To retrieve the latest project report in SARIF format, send the following `GET` request:

```cURL
GET /api/experimental/report/latest?branch={branch}
```

Here is the description of the accepted parameter:

| Parameter   | Type   | Required  | Description       | Example value |
|-------------|--------|-----------|-------------------|---------------|
| `branch` | String | No       | Name of the branch to retrieve the report for. If not specified, the default branch is used | `feature`    |

The API response does not include code snippets or full rule descriptions.











