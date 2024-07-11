[//]: # (title: User roles draft)

<no-index/>

<link-summary>This section contains the list of user roles available in Qodana Cloud.</link-summary>

The role assigned to your [Qodana Cloud](https://qodana.cloud) account stipulates the permissions that will be
granted. Currently, Qodana Cloud has the Viewer, Editor, Admin and Owner roles.

The Viewer, Editor, and Admin roles can be assigned on the [organization](#organization-roles) and [team](#team-roles) levels. 
The Owner role is available only on the organization level.

## Team roles
{id="team-roles"}

Team-level roles are sets of permissions that can be assigned to users on a [team](cloud-teams.topic) level to manage teams and their 
projects, members, projects, reports and settings.

<!-- This needs to be described what it means when a role is assigned -->

Below you can find the detailed description of all roles and their permissions.

<tabs group="cloud-roles">
    <tab title="Viewer" group-key="viewer">
        <p>The Viewer role lets users view team members, projects, and reports associated with a team.
        This role is suitable for users outside a team who require access to view reports.</p>
        <table>
            <tr>
                <td>Permission</td>
                <td>Create</td>
                <td>View</td>
                <td>Update</td>
                <td>Delete</td>
                <td>Archive</td>
            </tr>
            <tr>
                <td>Teams</td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Projects</td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Reports</td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
        </table>
    </tab>
    <tab title="Editor" group-key="editor">
        <p>The Editor role covers all Viewer permissions and lets users manage projects and reports within the team.
        This role is suitable for members of development teams such as developers, devops and QA specialists.</p>
        <table>
            <tr>
                <td>Permission</td>
                <td>Create</td>
                <td>View</td>
                <td>Update</td>
                <td>Delete</td>
                <td>Archive</td>
            </tr>
            <tr>
                <td>Teams</td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
            <tr>
                <td>Projects</td>
                <td>&#x2714;</td>
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
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td></td>
            </tr>
        </table>
    </tab>
    <tab title="Admin" group-key="admin">
        <p>The Admin role covers all Editor permissions and lets users manage both teams and team members, and delete teams.
        This role is suitable for team managers, team leads, and senior developers.</p>
        <table>
            <tr>
                <td>Permission</td>
                <td>Create</td>
                <td>View</td>
                <td>Update</td>
                <td>Delete</td>
                <td>Archive</td>
            </tr>
            <tr>
                <td>Teams</td>
                <!-- Is this true? Needs to be checked -->
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
            </tr>
            <tr>
                <td>Team users</td>
                <!-- Is this true? Needs to be checked -->
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
                <td>&#x2714;</td>
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

## Organization roles
{id="organization-roles"}

Organization-level roles are sets of permissions that can be assigned to users to manage 
[organizations](cloud-organizations.topic) and their members, teams, projects, reports, and settings. 

<tabs group="cloud-roles">
    <tab title="Viewer" group-key="viewer">
        <p>
            The default user role that lets view everything on the organization level. This role is suitable for 
            developers, QA specialists, support team members, and product leads.
        </p>
        <table>
            <tr>
                <td>Permission</td>
                <td>Create</td>
                <td>View</td>
                <td>Update</td>
                <td>Delete</td>
                <td>Archive</td>
                <td>Leave</td>
            </tr>
            <tr>
                <td>Organizations</td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
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
                <td></td>
            </tr>
            <tr>
                <td>Teams</td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
            </tr>
        </table>
    </tab>
    <tab title="Editor" group-key="editor">
        <p>
            Manage teams and team members. This role is suitable for team-leads and managers.
        </p>
        <table>
            <tr>
                <td>Permission</td>
                <td>Create</td>
                <td>View</td>
                <td>Update</td>
                <td>Delete</td>
                <td>Archive</td>
                <td>Leave</td>
            </tr>
            <tr>
                <td>Organizations</td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
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
                <td></td>
            </tr>
            <tr>
                <td>Contributors</td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
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
                <td></td>
            </tr>
            <tr>
                <td>Organization events</td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
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
                <td></td>
            </tr>
        </table>
    </tab>
    <tab title="Admin" group-key="admin">
        <p>
            The Admin role covers all Editor permissions and lets users manage organization and team users, projects and reports 
            except assigning the Owner role. This role is suitable for members of IT departments.
        </p>
        <table>
            <tr>
                <td>Permission</td>
                <td>Create</td>
                <td>View</td>
                <td>Update</td>
                <td>Delete</td>
                <td>Archive</td>
                <td>Leave</td>
            </tr>
            <tr>
                <td>Organizations</td>
                <td></td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td></td>
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
                <td></td>
            </tr>
            <tr>
                <td>Contributors</td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
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
                <td></td>
            </tr>
            <tr>
                <td>Organization settings</td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
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
                <td></td>
            </tr>
            <tr>
                <td>Public keys</td>
                <td></td>
                <td>&#x2714;</td>
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
                <td></td>
            </tr>
            <tr>
                <td>Projects</td>
                <td>&#x2714;</td>
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
                <td></td>
            </tr>
            <tr>
                <td>Project contributors</td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
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
                <td></td>
            </tr>
            <tr>
                <td>Reports</td>
                <td></td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td></td>
                <td></td>
            </tr>
        </table>
    </tab>
    <tab title="Owner" group-key="owner">
        <p>
            The Owner role covers all Admin permissions and lets users delete organizations, change organization privacy, and manage
            other Owner users. This role is suitable for IT department leads.
        </p>
        <table>
            <tr>
                <td>Permission</td>
                <td>Create</td>
                <td>View</td>
                <td>Update</td>
                <td>Delete</td>
                <td>Archive</td>
                <td>Leave</td>
            </tr>
            <tr>
                <td>Organizations</td>
                <td></td>
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
                <td></td>
            </tr>
            <tr>
                <td>Contributors</td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
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
                <td></td>
            </tr>
            <tr>
                <td>Organization settings</td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
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
                <td></td>
            </tr>
            <tr>
                <td>Organization status</td>
                <td></td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
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
                <td></td>
            </tr>
            <tr>
                <td>Organization licenses</td>
                <td></td>
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
                <td></td>
            </tr>
            <tr>
                <td>Teams</td>
                <td>&#x2714;</td>
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
                <td></td>
            </tr>
            <tr>
                <td>Projects</td>
                <td>&#x2714;</td>
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
                <td></td>
            </tr>
            <tr>
                <td>Project contributors</td>
                <td></td>
                <td>&#x2714;</td>
                <td></td>
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
                <td></td>
            </tr>
            <tr>
                <td>Reports</td>
                <td></td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td></td>
                <td></td>
            </tr>
        </table>
    </tab>
</tabs>

