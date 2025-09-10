# Release notes

<show-structure depth="3"/>

## July 2024

The new project setup is implemented in %cloud%. Now you can choose how you would like to run %product%, and the
wizard will guide you through the configuration process. This covers running %product% locally as well as using various
CI/CD solutions.

The detailed information is available in the [](set-up-your-project.md) section of this
documentation.

## April 2025

Starting from version 2025.1 of %product%, the %cloud% UI contains the **Insights** page available by clicking the 
button in the upper-right part of the UI. The description of this page is available on the [](insights.md) page
of this documentation.

Now you can also configure [Single Sign-on](cloud-sso.md) to authenticate using various third-party authentication providers

## September 2025

<link-summary>The public API lets you create teams and projects in %cloud% and %premlite% using your build pipelines.</link-summary>

%cloud% and %premlite% provide the public API that lets you create [teams](cloud-teams.topic) and [projects](cloud-projects.topic)
using your build pipelines.

### Prerequisites

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

### Create teams and projects

To create a new team and project and obtain its [project token](project-token.md), send a `POST` request using the
`https://api.qodana.cloud/v1/public/organizations/teams/projects` endpoint, for example:

```cURL
QODANA_TOKEN=$(curl -X POST https://api.qodana.cloud/v1/public/organizations/teams/projects \
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
