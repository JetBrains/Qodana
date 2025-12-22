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
You can configure and use the [existing inspection profiles](inspection-profiles.md#inspection-profiles-existing-profiles) or create [your custom profiles](inspection-profiles.md#inspection-profiles-custom-profiles) from scratch.

1. Finally, you can override the default JDK versions shipped with %product%, see the [](configure-jdk.md) for details.

## Performance optimization

To make %product% work better during the project configuration stage, you can follow the recommendations below.

First of all, specify the [`--cache-dir`](docker-image-configuration.topic#docker-config-reference-cache-dependencies) option,
the `use-caches` input argument in case of [CI/CD integrations](ci.md), or the `/data/caches` directory in
the Docker container of a linter after the first linter analysis. Cache contains data related to project structure, indexes,
dependencies, which makes subsequent analyses faster. However, in case of significant and disruptive changes of your
project or %product% version updates, it may be beneficial to reset cache.

You can also store your IntelliJ IDEA setting files in the `.idea` folder, for example:
* The `modules.xml` file improves project structure parsing
* The language-specific files like `kotlinc.xml` or `php.xml` provide information about compiler versions and options
* The `*.iml` files contain information about directories

Make sure that your project is correctly configured by looking at the
`<results-dir-artifact>/projectStructure` directory after the first analysis. Also, make sure that:

* The project imports work correctly
* The tooling that you use matches the configured versions
* Project dependency pooling works correctly, as it should be done only once if you are using cache
* Analyses do not show [sanity problems](inspection-profiles.md#inspection-profiles-existing-profiles) because they are a key indicator of configuration issues

