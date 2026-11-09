# Experimental API

SBOM API (experimental) (fourth issue)

Send the organization’s public API token as a bearer token:

authorization: Bearer $ORG_TOKEN

## List of organization projects

The Qodana Cloud SBOM API lets you list an organization’s active projects and retrieve a project’s dependency/license 
data in SPDX JSON format. It is intended for organizations that need to review dependencies across many projects without downloading each project’s license list from the UI.
Authentication

```cURL
GET https://qodana.cloud/api/experimental/organizations/{organizationId}/projects?offset=0&limit=20
```

Here is the description of the request body:


|Parameter|Description |
|--------|----------|
|`offset`| Integer, non-negative, optional. The default value is 0 |
|`limit`| Integer, optional, between 1 and 100 |


Returns a paginated list of active projects belonging to the token’s organization. Results are ordered by project ID.

```json
{
  "count": 42,
  "next": 20,
    "items": [
      {
        "id": "…",
        "name": "…",
        "teamId": "…",
        "teamName": "…",
        "defaultBranchName": "main"
      }
    ]
}
```

Pagination uses offsets: offset is optional, defaults to 0, and must be non-negative. limit is optional, defaults to 20, 
and must be between 1 and 100; out-of-range values return 400. The response follows the public API’s PaginatedList shape 
(count, next, prev, items); next and prev are omitted when there is no corresponding page.
Retrieve a project’s dependencies


## 

GET https://qodana.cloud/api/experimental/organizations/projects/{projectId}/dependencies

The endpoint returns a redirect to a presigned URL for the project’s projectStructure/thirdPartySoftwareList.json object. 
The data is the same SPDX/JSON data available through Download license list in the Qodana Cloud License tab. 
If the object is unavailable, the endpoint returns 204 No Content.

Supported Accept values are absent, application/json, and application/spdx+json. When application/spdx+json is requested, 
the response content type is set to application/spdx+json. The feature description says to assume the JSON data is SPDX format.
Documentation follow-up / verification

The parent feature describes the API as experimental. Before publishing, verify the final endpoint behavior and availability, 
especially the dependency endpoint’s redirect and content type, because those are implementation details specified in the 
feature proposal rather than confirmed by the documentation issue. The documentation issue itself has no comments or description to add further requirements.

## Documentation notes: team-scoped organization API tokens (first issue)

Purpose. An organization-wide API token can otherwise grant access across the organization, including the ability to mint project tokens for different teams. The proposed team-scoped token limits that exposure by restricting access to a selected set of teams.

How it works. An eligible team admin can create a token for teams they administer; an organization admin can select any team. The token can be named and given an expiry (90 days by default, up to 365 days). Its team scope is captured when created; the one-time secret is not retrievable later. The parent feature description specifies a maximum of 50 teams per token.

With the token, a client requests a project token through POST /api/v1/public/organizations/projects, providing a team and project by name or ID. The project is created if it does not exist. The resulting project token is short-lived; the implementation commit describes a one-hour default. It is invalidated when the organization token expires or the project leaves an allowed team.

Access and lifecycle behavior.

    Requests are limited to the token’s allowed teams, including project lookups, insights, and user-list read endpoints.
    It cannot create teams or access projects outside its scope; missing and out-of-scope teams receive the same 403 response.
    A team-scoped token is rejected by the deprecated team-and-project endpoint.
    Revocation or expiry blocks the token and project tokens issued from it.
    Creating and revoking tokens are audit-logged.
    Existing organization-wide tokens are intended to remain backward-compatible and separate from scoped tokens.

Implementation details noted in the parent issue and commits. The scoped JWT uses token_type=org_api_team_scoped, includes issuer/audience/token and subject identifiers, issued-at and expiry claims, and the team IDs. HS256 is pinned. The random secret is shown once; only its SHA-256 hash is stored and comparisons are constant-time. The scope is checked against the token record, expiry, and live teams on requests. The commit notes that deleting a team shrinks the effective scope.

Documentation cautions. The documentation task itself has no description, comments, or attachments, so these notes are derived from its linked backend feature. The feature is still marked Reviewing, while the documentation task is In progress; treat the behavior above as implementation/acceptance information rather than a confirmed release announcement. The feature text has one ambiguity worth resolving before publishing: it says “No team creation (projects?)”, while its acceptance criteria say a missing project is created. The commits support project creation behavior only indirectly; confirm the intended user-facing wording and exact endpoint/request format against the API specification before publication. No change-history record beyond the returned linked commits was available.

Source: this documentation task and its linked backend feature.

SECOND ISSUE

The documentation task is open and has no description or comments of its own. Its parent feature provides the substantive requirements; the implementation commits indicate the filter was moved to the experimental API. Treat the following as a documentation draft based on that issue/commit evidence, not as confirmation that the feature is released or available in a particular build.
Feature overview

The insights query API can filter results by vulnerability identifiers reported by Qodana. This helps identify projects affected by a particular vulnerability. IDs come from SARIF results[].properties.vulnerabilityIds and may include formats such as CVE-, GHSA-, or MAL-. Cloud uses this property, not result tags.
API surface

The parent issue specifies these experimental endpoints:

    POST /api/experimental/organizations/project-insights/query
    POST /api/experimental/organizations/inspection-insights/query

Both request bodies accept optional includeVulnerabilityIds: Set<String>. The response shape is unchanged, and matched vulnerability IDs are not included in the response. The parent issue scopes out the corresponding versioned public endpoints; commits also record moving the feature to experimental API.
Filtering behavior

    Project insights: keeps projects with matching results and limits severity counts to matching results from each project’s latest report on the default branch. Projects without matching results are omitted.
    Inspection insights: returns only inspections with matching results, with counts limited to those results.
    The filter can be combined with includeInspectionIds, includeProjectIds, includeTeamIds, and timeRange.
    A result matching multiple requested IDs is counted once.
    Matching is by the complete ID, not a prefix; case and surrounding whitespace are ignored.
    An ID is invalid if, after trimming and uppercasing, it does not match ^[A-Z0-9][A-Z0-9._:-]{0,127}$; the request is rejected with HTTP 400. A valid but unknown ID returns no matches.

Data and compatibility notes

The feature depends on vulnerability IDs being present in SARIF and persisted during report processing. Reports without properties.vulnerabilityIds should continue to process as before. Generic result-tag search is explicitly out of scope. The parent issue also calls for avoiding significant query-latency regression at organizations with roughly 1,000 or more projects.
Evidence and open documentation checks

Commits on the parent issue mention persistence during report processing, database migration, endpoint/query tests, ID normalization and validation, combined-filter cases, and the move to experimental API. The parent issue’s acceptance criteria and scope specify the behaviors above. However, the available issue data does not show the final OpenAPI schema or an example request/response, authentication requirements, release availability, or measured performance results. Verify those before publishing user-facing reference documentation.

THIRD ISSUE

The documentation task is open, assigned to anton.samarin, and marked for the Documentation domain. Its description is empty, so the details below come from its parent backend feature, not from a finalized documentation spec.
Feature to document

An experimental Qodana Cloud API endpoint for adding users to a team in bulk:

POST /api/experimental/teams/{id}/members
Authorization: Bearer $ORG_API_TOKEN
Content-Type: application/json

Request body contains a members array. Each entry has an email and an optional role; omitted roles default to VIEWER. The example roles are VIEWER, EDITOR, and ADMIN.
Behavior and limits

    Adds organization users who are not yet on the team; updates the role of existing team members when it differs from the requested role.
    Does not remove team members.
    Skips emails not found in the organization and emails with pending organization invitations; returns these in unknownEmails.
    Matches emails without regard to case. If an email is repeated in the request, the last entry wins.
    A request may contain at most 1,000 members; exceeding this returns 400.
    An unknown, deleted, or cross-organization team ID returns 404.
    The documented success response is 200, with numMembersAdded, numMembersUpdated, and unknownEmails.

Access and scope

The parent issue says this is an experimental feature available to organizations that have an Organization API token available (listed there as Ultimate Plus and Ultimate Plus Trial, and both Premium license plans); an existing token may continue to work after downgrade or license expiry. It says there is no dedicated permission for the feature while experimental. The described use case assumes SSO and that users already exist in Qodana; this endpoint does not send invitations. FUS and audit events are explicitly out of scope.
Documentation follow-ups

The parent issue provides a proposed request/response design, but the documentation task itself has no description. Before publishing, confirm the final contract and access wording against the shipped API, especially token/license availability and whether the endpoint remains experimental. The parent has linked commits mentioning tests and pending-invitation handling, but the available issue data does not establish a final release or documentation status. No comments are recorded on the documentation task or its parent.