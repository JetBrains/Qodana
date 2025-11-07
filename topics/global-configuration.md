# Global configuration

Global configuration lets you share %product% configurations across multiple projects. Each global configuration is a set of files
consisting of the [`qodana.yaml`](qodana-yaml.md) configuration file and [inspection profile configurations](custom-profiles.md) contained in YAML and 
XML files.

## How the global configuration works

YAML-formatted configuration files are saved in project directories of VCS repositories. In [CI/CD pipelines](ci.md), 
an uploader tool uses [configuration token](#Uploading+to+Qodana+Cloud) to send these files to Qodana Cloud. 
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

If a project has both configuration types with the project settings colliding with global ones, then 
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
<!-- How do I merge two global configurations in this case? -->

<!-- To merge two global configurations, you have to explicitly include one global configuration in the second one: -->

<!-- Need to have an example of merging two global configurations -->
<!-- What happens if one global configuration collides with another? -->

## Uploading to Qodana Cloud

To be able to share global configurations via Qodana Cloud, you should upload a special configuration token while running your CI/CD pipeline.
You can generate this token on the **Global configurations** tab of your [organization settings](cloud-organizations.topic#cloud-organizations-global-configurations). 

> You can manipulate tokens only if your user has either the `Owner` or the `Admin` role, see the [list of roles](cloud-user-roles.md) for details.
{style="note"}

After that, send your global configuration to Qodana Cloud as described in the [](#How+the+global+configuration+works) section on this page.
This will make your global configurations become available in the [organization settings](cloud-organizations.topic) of Qodana Cloud UI.



