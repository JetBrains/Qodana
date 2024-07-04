[//]: # (title: User roles draft)

<no-index/>

<link-summary>This section contains the list of user roles available in Qodana Cloud.</link-summary>

The role assigned to your [Qodana Cloud](https://qodana.cloud) account stipulates the permissions that will be
granted. Currently, Qodana Cloud has the Viewer, Editor, Admin and Owner roles.

The Viewer, Editor, and Admin roles can be assigned on the [organization](#organization-roles) and [team](#team-roles) levels. 
The Owner role is available only on the organization level.

## Organization roles
{id="organization-roles"}

Organization-level roles are sets of permissions that can be assigned to users to manage 
[organizations](cloud-organizations.topic) and their members, teams, projects, reports, and settings. 

The Viewer role is the default user role that lets users view everything on the organization level; however, they cannot 
manage anything other than their own user account. This role is suitable for developers, QA specialists, support team 
members, and product leads.

The Editor role covers all Viewer permissions and additionally lets users manage teams and team members.
This role is suitable for team-leads and managers.

The Admin role covers all Editor permissions and lets users manage organization and team users, projects and reports 
except assigning the Owner role. This role is suitable for members of IT departments.

The Owner role covers all Admin permissions and lets users delete organizations, change organization privacy, and manage
other Owner users. This role is suitable for IT department leads.

Below you can find the detailed description of all roles and their permissions.

### Detailed description of permissions
{id="roles-org-description"}

<tabs>
    <tab title="Organizations">
        <table>
            <tr>
                <td>Permission</td>
                <td>Owner</td>
                <td>Admin</td>
                <td>Editor</td>
                <td>Viewer</td>
            </tr>
            <tr>
                <td>Organizations: View</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
            </tr>
            <tr>
                <td>Organizations: Update</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
                <td>&#x274c;</td>
            </tr>
            <tr>
                <td>Organizations: Archive</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
                <td>&#x274c;</td>
                <td>&#x274c;</td>
            </tr>
            <tr>
                <td>Organizations: Delete</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
                <td>&#x274c;</td>
                <td>&#x274c;</td>
            </tr>
            <tr>
                <td>Organizations: Leave</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
            </tr>
            <tr>
                <td>Organization members: View</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
            </tr>
            <tr>
                <td>Organization members: Update</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
                <td>&#x274c;</td>
            </tr>
            <tr>
                <td>Contributors: View</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
            </tr>
            <tr>
                <td>Membership requests: Manage</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
                <td>&#x274c;</td>
            </tr>
            <tr>
                <td>Organization settings: View</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
            </tr>
            <tr>
                <td>Organization events: View</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
            </tr>
            <tr>
                <td>Organization events: View</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
            </tr>
            <tr>
                <td>Organization status: Update</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
                <td>&#x274c;</td>
                <td>&#x274c;</td>
            </tr>
            <tr>
                <td>Organization owners: Update</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
                <td>&#x274c;</td>
                <td>&#x274c;</td>
            </tr>
            <tr>
                <td>Organization licenses: Update</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
                <td>&#x274c;</td>
                <td>&#x274c;</td>
            </tr>
            <tr>
                <td>Public keys: View and Update</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
                <td>&#x274c;</td>
            </tr>
        </table>
    </tab>
    <tab title="Teams">
        <table>
            <tr>
                <td>Permission</td>
                <td>Owner</td>
                <td>Admin</td>
                <td>Editor</td>
                <td>Viewer</td>
            </tr>
            <tr>
                <td>Teams: Create</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
            </tr>
            <tr>
                <td>Teams: View</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
            </tr>
            <tr>
                <td>Teams: Update</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
            </tr>
            <tr>
                <td>Teams: Delete</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
            </tr>
            <tr>
                <td>Teams: Archive</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
            </tr>
            <tr>
                <td>Teams members: View</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
            </tr>
            <tr>
                <td>Teams members: Update</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
            </tr>
        </table>
    </tab>
    <tab title="Projects">
        <table>
            <tr>
                <td>Permission</td>
                <td>Owner</td>
                <td>Admin</td>
                <td>Editor</td>
                <td>Viewer</td>
            </tr>
            <tr>
                <td>Projects: Create</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
                <td>&#x274c;</td>
            </tr>
            <tr>
                <td>Projects: View</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
                <td>&#x274c;</td>
            </tr>
            <tr>
                <td>Projects: Update</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
                <td>&#x274c;</td>
            </tr>
            <tr>
                <td>Projects: Delete</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
                <td>&#x274c;</td>
            </tr>
            <tr>
                <td>Projects: Archive</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
                <td>&#x274c;</td>
            </tr>
            <tr>
                <td>Project members: Update</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
                <td>&#x274c;</td>
            </tr>
            <tr>
                <td>Project contributors: View</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
                <td>&#x274c;</td>
            </tr>
            <tr>
                <td>Project token: Create, View and Delete</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
                <td>&#x274c;</td>
            </tr>
        </table>
    </tab>
    <tab title="Project reports">
      <table>
            <tr>
                <td>Permission</td>
                <td>Owner</td>
                <td>Admin</td>
                <td>Editor</td>
                <td>Viewer</td>
            </tr>
            <tr>
                <td>Project reports: Create, View, Update and Delete</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
                <td>&#x274c;</td>
            </tr>
      </table>
    </tab>
</tabs>


### Team roles
{id="team-roles"}

Team-level roles are sets of permissions that can be assigned to users to manage [teams](cloud-teams.topic) and their projects, 
members, projects, reports and settings. 

The Viewer role lets users view team members, projects, and reports associated with a team.
This role is suitable for users outside a team who require access to view reports.

The Editor role covers all Viewer permissions and lets users manage projects and reports within the team.
This role is suitable for members of development teams such as developers, devops and QA specialists.

The Admin role covers all Editor permissions and lets users manage both teams and team members, and delete teams.
This role is suitable for team managers, team leads, and senior developers.

Below you can find the detailed description of all roles and their permissions.

### Detailed description of permissions
{id="roles-team-description"}

<tabs>
    <tab title="Teams">
        <table>
            <tr>
                <td>Permission</td>
                <td>Admin</td>
                <td>Editor</td>
                <td>Viewer</td>
            </tr>
            <tr>
                <td>Teams: View</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
            </tr>
            <tr>
                <td>Teams: Update</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
                <td>&#x274c;</td>
            </tr>
            <tr>
                <td>Teams: Delete</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
                <td>&#x274c;</td>
            </tr>
            <tr>
                <td>Teams: Archive</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
                <td>&#x274c;</td>
            </tr>
            <tr>
                <td>Team users: View and Update, Manage membership requests</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
                <td>&#x274c;</td>
            </tr>
        </table>
    </tab>
    <tab title="Projects">
        <table>
            <tr>
                <td>Permission</td>
                <td>Admin</td>
                <td>Editor</td>
                <td>Viewer</td>
            </tr>
            <tr>
                <td>Projects: Create</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
            </tr>
            <tr>
                <td>Projects: View</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
            </tr>
            <tr>
                <td>Projects: Update</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
            </tr>
            <tr>
                <td>Projects: Delete</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
            </tr>
            <tr>
                <td>Projects: Archive</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
            </tr>
            <tr>
                <td>Project members: Update</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
            </tr>
            <tr>
                <td>Project members: Update</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
            </tr>
            <tr>
                <td>Project contributor: Read</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
            </tr>
            <tr>
                <td>Project token: Create, View and Delete</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
            </tr>
        </table>
    </tab>
    <tab title="Project reports">
        <table>
            <tr>
                <td>Permission</td>
                <td>Admin</td>
                <td>Editor</td>
                <td>Viewer</td>
            </tr>
            <tr>
                <td>Project reports: Create</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
            </tr>
            <tr>
                <td>Project reports: View</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
            </tr>
            <tr>
                <td>Project reports: Update</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
            </tr>
            <tr>
                <td>Project reports: Delete</td>
                <td>&#x2714;</td>
                <td>&#x2714;</td>
                <td>&#x274c;</td>
            </tr>
        </table>
    </tab>
</tabs>




