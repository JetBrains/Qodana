# Global configuration

Global configuration lets you re-use %product% configurations across multiple projects. Each global configuration covers
[`qodana.yaml`](qodana-yaml.md) files and inspection profile configurations in [YAML](custom-profiles.md) and 
[XML](custom-xml-profiles.md) formats.

## How it works

Configuration files are saved in VCS repositories. Using [CI/CD pipelines](ci.md), these files are then pushed to 
Qodana Cloud. You can update these files in the Qodana Cloud UI. 

You can use and configure each global configuration for several projects within a single Qodana Cloud 
[organization](cloud-organizations.topic). 

### Global and local configurations

Local configuration is a configuration created for a specific project and located within a repository of such a project.

If a project has local and global configurations and the local settings collide with global, then 
local settings take precedence over global settings. In this case, the final configuration will contain settings
from both configurations, see the table below.

<!-- This can probably be modified -->

<table>
    <tr>
        <td>Local configuration</td>
        <td>Global configuration</td>
        <td>Final (resolved) configuration</td>
    </tr>
    <tr>
        <td>
            <code-block lang="yaml">
                failureConditions:
                    severityThresholds: 
                        critical: 1
                        any: 10
            </code-block>
        </td>
        <td>
            <code-block lang="yaml">
                plugins:
                    - org-plugin
                &nbsp;
                properties:
                    orgPluginIntProperty: 10
                &nbsp;
                failureConditions:
                    severityThresholds:
                        critical: 0
            </code-block>
        </td>
        <td>
            <code-block lang="yaml">
                plugins:
                    - org-plugin
                &nbsp;
                properties:
                    orgPluginIntProperty: 10
                &nbsp;
                failureConditions:
                    severityThresholds:
                        critical: 1
                        any: 10
            </code-block>
        </td>
    </tr>
</table>

Before uploading configurations to Qodana Cloud, you should use a special token. 

> You can manipulate tokens only if your user has an admin role, see the [list of roles](cloud-user-roles.md) for details.

To upload configurations to Qodana Cloud, run your CI/CD pipeline. Once uploaded, global configurations become available 
in the [organization settings](cloud-organizations.topic) of Qodana Cloud UI.

