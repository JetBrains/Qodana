# Global configuration

Global configuration lets you share %product% configurations across multiple projects. Each global configuration is a set of files
consisting of the [`qodana.yaml`](qodana-yaml.md) configuration file and inspection profile configurations contained in [YAML](custom-profiles.md) and 
[XML](custom-xml-profiles.md) files.

## How the global configuration works

YAML-formatted configuration files are saved in project directories of VCS repositories. Using [CI/CD pipelines](ci.md), 
an uploader tool run using a [configuration token](#Configuration+token) you can send these files to Qodana Cloud. 
This lets global configurations become connected to Qodana Cloud projects; during project analyses, %product% linters 
obtain global configuration for use. 

You can use each global configuration for several projects within a single Qodana Cloud
[organization](cloud-organizations.topic). Each organization can have one or multiple global configurations, whereas each project 
can be configured using one global and/or project configuration.

Files contained in a global configuration can be updated using access to your VCS repository.

> To learn more about setting global configurations, see the [](cloud-organizations.topic#cloud-organizations-global-configurations) section.

### Global and project configurations

Project configuration is a configuration created for a specific project and located within a project repository.
Global configuration is a configuration that can be shared across multiple projects. 
Both configurations can be merged into a single configuration and contained in a single [YAML-formatted file](qodana-yaml.md), 
as well as two global configurations. In this case, profile configurations are merged as well using the 
[`profile`](qodana-yaml.md#Set+up+a+profile) option.

<!-- An example of a profile configuration should be provided here -->
<!-- An example of a profile.inspections configuration should be provided here -->
<!-- How does the flexInspect section work? -->

If a project has project and global configurations and the project settings collide with global, then 
project settings take precedence over global settings. In this case, the final configuration will contain settings
from both configurations as you can see the `critical` configuration option of the `severityThresholds` option.

<!-- This can probably be modified -->


<table>
    <tr>
        <td>Project configuration</td>
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

<!-- How do I specify a global configuration file? What is the syntax to it? -->

To merge two global configurations, you have to explicitly include one global configuration in the second one:

<!-- Need to have an example of merging two global configurations -->
<!-- What happens if one global configuration collides with another? -->

## Uploading to Qodana Cloud

To upload global configurations to Qodana Cloud, you should use a special configuration token. 

> You can manipulate tokens only if your user has either the Owner or the Admin role, see the [list of roles](cloud-user-roles.md) for details.

To upload configurations to Qodana Cloud, run your CI/CD pipeline. Once uploaded, global configurations become available 
in the [organization settings](cloud-organizations.topic) of Qodana Cloud UI.

### Configuration token

A configuration token is a token that you can generate on the **Global configurations** tab of your 
[organization settings](cloud-organizations.topic#cloud-organizations-global-configurations). Using this token, you can 
send your global configuration to Qodana Cloud as described in the [](#How+the+global+configuration+works) section on this page. 

