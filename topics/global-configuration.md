# Global configuration

Global configuration lets you share %product% configurations across multiple projects. Each global configuration is a set of files
consisting of the [`qodana.yaml`](qodana-yaml.md) configuration file and [inspection profile configurations](custom-profiles.md) contained in YAML and 
XML files.

This feature is available under the Ultimate Plus [license](pricing.md).

## How the global configuration works

YAML-formatted configuration files are stored in project directories of VCS repositories. For example, your project 
can have the following structure that will constitute a global configuration: 

```text
root/
    project-a/
        qodana.yaml
    project-b/
        qodana.yaml
    qodana-global-configurations.yaml    
```

<!--```text
root/
    project-a/
        qodana.yaml
        project-a-profile.yaml
    project-b/
        qodana.yaml
        project-b-profile.yaml
    qodana-global-configurations.yaml    
```
-->

<!--In this example, the `project-a` and `project-b` directories contain [%product% configuration files](qodana-yaml.md) along with [inspection
profile configuration](custom-profiles.md) files. The `qodana-global-configuraton.yaml` file describes the global configuration, for example: -->

In this structure, the `project-a` and `project-b` directories contain [%product% configuration files](qodana-yaml.md).


The `qodana-global-configuraton.yaml` file describes the global configuration, for example:

```yaml
configurations:
    - id: project_a
      name: Project A # Displayed in %cloud% UI
      description: Description for configuration project A # Displayed in %cloud% UI
      qodanaYaml: project-a/qodana.yaml # Path to the config file 

    - id: project_b
      name: Project B
      description: Description for configuration project B
      qodanaYaml: project-b/qodana.yaml
        
```


[CI/CD pipelines](ci.md) use an uploader tool and [configuration token](#Uploading+to+Qodana+Cloud) to send these files to Qodana Cloud. 
This lets global configurations become connected to Qodana Cloud projects; during project analyses, %product% linters 
obtain global configuration for use. 

You can use each global configuration for several projects within a single Qodana Cloud
[organization](cloud-organizations.topic#cloud-organizations-global-configurations). 
Each organization can have one or multiple global configurations, whereas each project can be configured using one global and/or project configuration.

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
This will make your global configurations become available in the [organization settings](cloud-organizations.topic) of the %cloud% UI.



