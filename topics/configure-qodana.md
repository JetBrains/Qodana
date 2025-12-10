[//]: # (title: Configuration overview)

You have the following configuration approaches:

1. Configuring %product% via a [YAML-formatted](qodana-yaml.md) file, typically named `qodana.yaml`, is suitable for settings that require lengthy 
commands, such as inspection configuration, [bootstrap](before-running-qodana.md), and other settings that are not convenient to configure otherwise. 
Once a YAML configuration is saved, you can reuse it across different instances of Qodana.

1. Using [configuration capabilities](docker-image-configuration.topic) of the tools that are running %product% like Docker, 
[Qodana CLI](deploy-qodana.md#Qodana+CLI), [IDEs](ide-integration.md), and [CI/CD tools](ci.md). 

    Settings like [linter](linters.md) or [quality gate](quality-gate.topic) can be set up using both methods.
    In this case, tool configurations override configurations saved in a YAML-formatted file.  

    > The configured major version of a %product% linter (20**.*) should match the configured linter version specified in the `qodana.yaml` file.
    {style="note"}

1. Configuring inspection profiles lets you specify inspections and paths in your codebase that should be used for analysis by %product%. 
You can configure and use the [existing inspection profiles](inspection-profiles.md) or create [your custom profiles](inspection-profiles.md#inspection-profiles-custom-profiles) from scratch.

1. Finally, you can override the default JDK versions shipped with %product%, see the [](configure-jdk.md) for details.

