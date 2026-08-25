# Global configuration

<link-summary>Global configurations let you share %product% configurations across multiple projects.</link-summary>

<show-structure for="chapter" depth="3"/>

Global configurations let you share %product% configurations across multiple projects. Each global configuration is a set of files
consisting of the [`qodana.yaml`](configuration-reference.md) configuration file and [inspection profile configurations](inspection-profiles.md#inspection-profiles-custom-profiles) contained in YAML and 
XML files.

This feature is available under the Ultimate Plus [license](pricing.md).

<tip>
    An example of a global configuration is available on the <a href="https://github.com/qodana/qodana-global-project-configuration">GitHub website</a>.
</tip>

## How the global configuration works

YAML-formatted configuration files are stored in project directories of VCS repositories. For example, your project 
can have the following structure that will create a global configuration: 

```text
root/
    project-a/
        qodana.yaml
    project-b/
        qodana.yaml
        project-b-profile.yaml
    qodana-global-configurations.yaml    
```

In this structure, the `project-a` and `project-b` directories contain [%product% configuration files](configuration-reference.md). Besides that,
the `project-b` directory contains the `project-b-profile.yaml` file containing a [custom profile](inspection-profiles.md#inspection-profiles-custom-profiles). To be 
included in the global configuration, it should be [referred](inspection-profiles.md#inspection-profiles-setup-a-profile) 
from the `qodana.yaml` file contained, for example, in the same directory. 

The `qodana-global-configuraton.yaml` file describes a global configuration using specific fields:

```yaml
configurations:
    - id: project_a
      name: Project A # Displayed in %cloud% UI
      description: Description for configuration project A # Displayed in %cloud% UI
      qodanaYaml: project-a/qodana.yaml # Path to the config file relatively to file

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
Both configurations can be merged into a single configuration and contained in a single [YAML-formatted file](configuration-reference.md), 
as well as two global configurations. In this case, profile configurations are merged as well using the 
[`profile`](configuration-reference.md#configuration-reference-inspection-profile) option.

If a project has both configuration types with the project settings colliding with global ones, then 
project settings take precedence over global settings. In this case, the final configuration will contain settings
from both configurations as you can see the `critical` configuration option of the `severityThresholds` option.

For example, the project configuration file contains the following configuration:

```yaml
linter: jetbrains/qodana-jvm:2025.2

failureConditions:
    severityThresholds:
        critical: 1
        any: 10
```

The global configuration file contains the following:

```yaml
failureConditions:
    severityThresholds:
        critical: 0

profile:
    name: qodana.recommended
```

In this case, the final or resolved configuration will look as follows:

```yaml
linter: jetbrains/qodana-jvm:2025.2

failureConditions:
    severityThresholds:
        critical: 1
        any: 10

profile:
    name: qodana.recommended
```

### Merging configurations

Using the `imports` key, you can reference another configuration file from your global configuration.

For example, the global configuration file contains the `imports` key to reference the `../base/qodana.yaml` file:

```yaml
version: "1.0"

imports:
  - ../base/qodana.yaml

profile:
    name: qodana.recommended
```

The referenced `../base/qodana.yaml` file contains the following %product% configuration:

```yaml
version: "1.0"

linter: jetbrains/qodana-jvm:2025.2
```

In this case, the merged configuration will look as follows:

```yaml
version: "1.0"

profile:
    name: qodana.recommended

linter: jetbrains/qodana-jvm:2025.2
```

## Uploading to Qodana Cloud

To be able to share global configurations via Qodana Cloud, you should upload a special configuration token while running your CI/CD pipeline.
You can generate this token on the **Global configurations** tab of your [organization settings](cloud-organizations.topic#cloud-organizations-global-configurations). 

> You can manipulate tokens only if your user has either the `Owner` or the `Admin` role, see the [list of roles](cloud-user-roles.md) for details.
{style="note"}

After that, send your global configuration to Qodana Cloud as described in the [](#How+the+global+configuration+works) section on this page.
This will make your global configurations become available in the [organization settings](cloud-organizations.topic) of the %cloud% UI.



