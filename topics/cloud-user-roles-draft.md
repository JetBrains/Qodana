[//]: # (title: User roles draft)

<no-index/>

<link-summary>This section contains the list of user roles available in Qodana Cloud.</link-summary>

The role assigned to a [Qodana Cloud](https://qodana.cloud) user defines the set of the permissions that will be
granted to them. A permission means an ability to perform a specific action. 

Currently, Qodana Cloud supports the Viewer, Editor, Admin and Owner roles.

The Viewer, Editor, and Admin roles can be assigned on the [organization](#organization-roles) and [team](#team-roles) levels. 
The Owner role is available only on the organization level.

## Team roles
{id="team-roles"}

<link-summary>Team roles are the sets of permissions that can be assigned to users on a team level.</link-summary>

Team roles are the sets of permissions that can be assigned to users on a [team](cloud-teams.topic) level.
To learn more about how to invite members to a team, see the [](cloud-teams.topic#cloud-teams-manage-teams).

These roles are required for all organization members.

Below you can find the detailed description of all team-level roles and their permissions.

<tabs group="cloud-roles">
    <tab title="Viewer" group-key="viewer">
        <p>View teams, projects, reports and users associated with a team. This role is suitable for users outside 
        a team who would like to view reports.</p>
    </tab>
    <tab title="Editor" group-key="editor">
        <p>Manage team projects and project reports, members and tokens.
        This role is suitable for developers, devops and QA specialists.</p>
        <table>
            <tr>
                <td>Permission</td>
                <td>Create</td>
                <td>View</td>
                <td>Update</td>
                <td>Delete</td>
            </tr>
            <tr>
                <td>Teams</td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Team users</td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Projects</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
            </tr>
            <tr>
                <td>Project members</td>
                <td></td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td></td>
            </tr>
            <tr>
                <td>Project contributors</td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Project tokens</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td></td>
                <td>&#x2714;</td>
            </tr>
            <tr>
                <td>Public keys</td>
                <td></td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td></td>
            </tr>
            <tr>
                <td>Reports</td>
                <td></td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
            </tr>
        </table>
    </tab>
    <tab title="Admin" group-key="admin">
        <p>Manage teams and team members.
        This role is suitable for team managers, team leads, and senior developers.</p>
        <table>
            <tr>
                <td>Permission</td>
                <td>Create</td>
                <td>View</td>
                <td>Update</td>
                <td>Delete</td>
            </tr>
            <tr>
                <td>Teams</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
            </tr>
            <tr>
                <td>Team users</td>
                <td></td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td></td>
            </tr>
            <tr>
                <td>Membership requests</td>
                <td></td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
            </tr>
            <tr>
                <td>Projects</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
            </tr>
            <tr>
                <td>Project members</td>
                <td></td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td></td>
            </tr>
            <tr>
                <td>Project contributors</td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Project tokens</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td></td>
                <td>&#x2714;</td>
            </tr>
            <tr>
                <td>Public keys</td>
                <td></td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td></td>
            </tr>
            <tr>
                <td>Reports</td>
                <td></td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
            </tr>
        </table>
    </tab>
</tabs>

## Organization roles
{id="organization-roles"}

<link-summary>Team roles are the sets of permissions that can be assigned to users on an organization level.</link-summary>

Organization roles are the sets of permissions that can be assigned to users on an
[organization](cloud-organizations.topic) level. To learn more about how to invite members to a Qodana Cloud organization, see the 
[](cloud-organizations.topic#cloud-organizations-invitation) section.

These roles are required for all organization members.

Below you can find the detailed description of all organization-level roles and their permissions.

<tabs group="cloud-roles">
    <tab title="Viewer" group-key="viewer">
        <p>
            View organizations, members, teams, and all everything contained in teams like projects, reports and members. 
            This role is suitable for developers, QA specialists, support team members, and product leads.
        </p>
        <table>
            <tr>
                <td>Permission</td>
                <td>View</td>
                <td>Leave</td>
            </tr>
            <tr>
                <td>Organizations</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
            </tr>
            <tr>
                <td>Organization members</td>
                <td>&#x2714;</td>
                <td></td>
            </tr>
            <tr>
                <td>Teams</td>
                <td>&#x2714;</td>
                <td></td>
            </tr>
        </table>
    </tab>
    <tab title="Editor" group-key="editor">
        <p>
            Manage teams and team members within an organization, and view everything related to an organization. This role is suitable for team-leads and managers.
        </p>
        <table>
            <tr>
                <td>Permission</td>
                <td>Create</td>
                <td>View</td>
                <td>Update</td>
                <td>Delete</td>
                <td>Leave</td>
            </tr>
            <tr>
                <td>Organizations</td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
                <td></td>
                <td>&#x2714;</td>
            </tr>
            <tr>
                <td>Organization members</td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Contributors</td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Organization settings</td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Organization events</td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Teams</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td></td>
            </tr>
            <tr>
                <td>Team members</td>
                <td></td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td></td>
                <td></td>
            </tr>
        </table>
    </tab>
    <tab title="Admin" group-key="admin">
        <p>
            Manage organizations and their users, projects, project tokens and reports. This role is suitable for 
            members of IT departments.
        </p>
        <table>
            <tr>
                <td>Permission</td>
                <td>Create</td>
                <td>View</td>
                <td>Update</td>
                <td>Delete</td>
                <td>Leave</td>
            </tr>
            <tr>
                <td>Organizations</td>
                <td></td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td></td>
                <td>&#x2714;</td>
            </tr>
            <tr>
                <td>Organization members</td>
                <td></td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Contributors</td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Membership requests</td>
                <td></td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td></td>
            </tr>
            <tr>
                <td>Organization settings</td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Organization events</td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Public keys</td>
                <td></td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Teams</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td></td>
            </tr>
            <tr>
                <td>Team members</td>
                <td></td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Projects</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td></td>
            </tr>
            <tr>
                <td>Project members</td>
                <td></td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Project contributors</td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Project tokens</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
            </tr>
            <tr>
                <td>Reports</td>
                <td></td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td></td>
            </tr>
        </table>
    </tab>
    <tab title="Owner" group-key="owner">
        <p>
            Full control over an organization and its entities including users, teams, projects and project reports. 
            This role is suitable for IT department leads.
        </p>
        <table>
            <tr>
                <td>Permission</td>
                <td>Create</td>
                <td>View</td>
                <td>Update</td>
                <td>Delete</td>
                <td>Leave</td>
            </tr>
            <tr>
                <td>Organizations</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
            </tr>
            <tr>
                <td>Organization members</td>
                <td></td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Contributors</td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Membership requests</td>
                <td></td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td></td>
            </tr>
            <tr>
                <td>Organization settings</td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Organization events</td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Organization status</td>
                <td></td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Organization owners</td>
                <td></td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Organization licenses</td>
                <td></td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Public keys</td>
                <td></td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Teams</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td></td>
            </tr>
            <tr>
                <td>Team members</td>
                <td></td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Projects</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td></td>
            </tr>
            <tr>
                <td>Project members</td>
                <td></td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Project contributors</td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Project tokens</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
            </tr>
            <tr>
                <td>Reports</td>
                <td></td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td></td>
            </tr>
        </table>
    </tab>
</tabs>

