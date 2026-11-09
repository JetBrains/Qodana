# Experimental API

<show-structure for="chapter" depth="3"/>

The experimental API helps you identify dependencies across organization projects. The dependency data matches an 
SPDX/JSON file available using the [**Download license list**](ui-overview.md#ui-overview-project-audit) button in %cloud%.

<note>
The API is experimental: it may be unstable, change without notice, or behave unexpectedly.
Your feedback is very welcome in our 
<a href="https://youtrack.jetbrains.com/newIssue?project=QD">issue tracker</a> or at
<a href="mailto:qodana-support@jetbrains.com">qodana-support@jetbrains.com</a>.
</note>

## Prerequisites

The experimental API requires an organization API token for authentication purposes.

Before using the experimental API, make sure that the following requirements were met:

<list>
<li>
    <p>To create and manage an organization API token, you should have access to an existing %cloud% organization 
       under the <code>Owner</code> or <code>Admin</code> <a href="cloud-user-roles.md" anchor="cloud-user-org-roles-owner">role</a>.</p>
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

## Get project dependencies

To return a SPDX/JSON dependency list to a specific %cloud% project, send the following `GET` request:

```http
GET /api/experimental/organizations/projects/{projectID}/dependencies
```

Here is the description of the accepted parameter:

| Parameter   | Type   | Required  | Description       | Example value |
|-------------|--------|-----------|-------------------|---------------|
| `projectId` | String | Yes       | ID of the project | `proj_123`    |

The accepted `Accept` values are absent or `application/json`.

If the stored object exists, the API responds with a redirect to a presigned URL to 
the `projectStructure/thirdPartySoftwareList.json` file; otherwise it returns `204 No Content`.













