# Global configuration

Global configuration lets you share %product% configurations across multiple projects. Each global configuration is a set of files
consisting of the [`qodana.yaml`](qodana-yaml.md) configuration file and inspection profile configurations contained in [YAML](custom-profiles.md) and 
[XML](custom-profiles.md#Custom+XML+profiles) files.

## How global configuration works

YAML-formatted configuration files are saved in project directories of VCS repositories. Using [CI/CD pipelines](ci.md) 
and an uploader tool, you can send these files to %cloud%. This lets global configurations become connected to 
%cloud% projects; during the project analysis, %product% linters obtain global configuration and use it as a base 
configuration during analysis. 

You can update these files in the %cloud% UI. 

You can use and configure each global configuration for several projects within a single %cloud% 
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

To be able to upload global configurations to %cloud%, you should use a special token. 

> You can manipulate tokens only if your user has an admin role, see the [list of roles](cloud-user-roles.md) for details.

To upload configurations to %cloud%, run your CI/CD pipeline. Once uploaded, global configurations become available 
in the [organization settings](cloud-organizations.topic) of %cloud% UI.

