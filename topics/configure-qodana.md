[//]: # (title: Configure Qodana)

You can configure %product% using the internal and external configuration methods.

You can set up %product% [internally](qodana-yaml.md) using the YAML-formatted file basically named `qodana.yaml`. 
Once %product% is configured, you can re-use the same configuration file across different instances of %product%. This
method is aimed at configuring things that require long commands like inspections, [bootstrap](before-running-qodana.md),
and other settings that are not convenient for configuring externally.

You can set up %product% [externally](docker-image-configuration.topic) using configuration of the tool that will be running 
%product% like Docker images, Qodana CLI, [GitHub Actions](github.md), [TeamCity](teamcity.md), [GitLab CI/CD](gitlab.md),
[Azure Pipelines](qodana-azure-pipelines.md), and others.

Several settings like [linter](linters.md) or [quality gate](quality-gate.topic) can be configured both internally and 
externally. Settings configured internally can be overridden by an external configuration. 

The configured major version of a %product% linter (20**.*) should match the version specified in the `qodana.yaml` file.




