[//]: # (title: New in Qodana)

This page provides information about %product% updates available in the latest version, as well as the 
chronological list of all significant [%cloud%](cloud-quickstart.md) updates.

## Qodana version 2026.1

### Native mode release

Native mode is released from the EAP version. The details are available in the [](deploy-qodana.md#deploy-qodana-native-mode) section.

### %cpp% release

The [%cpp%](clang.md) linter for C and C++ languages is released from the EAP version.

### The new Rust linter

Now you can analyze Rust projects using the new [%rust%](rust.md) linter.

<!--Version 2025.3 of %product% contains the updates described below.

## Podman support 

Starting from this version, %product% supports Podman as a container engine, see the 
[](deploy-qodana.md#Different+Docker+contexts+or+Podman) section for details.
-->
<!--
## Improved monorepo support

### New configuration options

Version 2025.3 of %product% introduces the 
[`--only-directory`](docker-image-configuration.topic#docker-config-reference-directories) or 
[`onlyDirectory`](qodana-yaml.md#Specify+directory+in+your+project) option for specifying a directory inside
your monorepo project. 

Also, the `--repository-root` CLI option lets you configure VCS root for your project.

### Java and Kotlin projects

By default, %product% worked with a project file defined at the root level of the repository. 
Starting from version 2025.3, %product% supports monorepo consisting of loosely coupled projects not aggregated in a 
single project file. In this case, it will recursively collect projects from subdirectories and import them for analysis.
This change enables incremental analysis and fixes for projects where analyzed project and VCS root are different.

Using the `rootJavaProjects` option in the [`qodana.yaml`](qodana-yaml.md) file, you can specify which projects 
should be included in the analysis, for example:

```yaml
rootJavaProjects:
- "./gradleProject"
- "./mavenModule/pom.xml"
```


## SDK support in the %dotnet% linter

The Dockerized version of the [%dotnet%](dotnet.md) linter now supports versions 8.0, 9.0 and 10.0 of SDK.
-->

## Qodana Cloud

<show-structure depth="3"/>

### December 2025

[Global configuration](global-configuration.md) lets you share %product% configurations across multiple projects. Each
global configuration is a set of files consisting of the [`qodana.yaml`](qodana-yaml.md) configuration file and
[inspection profile configurations](inspection-profiles.md#inspection-profiles-custom-profiles) contained in YAML and XML files.

### September 2025

The [`.mailmap`](https://git-scm.com/docs/gitmailmap) file support was implemented for better contributor counting, see
the [](contributors.md#The+.mailmap+file+support) for details.

%cloud% and %premlite% now provide the public API that lets you create [teams](cloud-teams.topic) and [projects](cloud-projects.topic)
using your build pipelines. The details are available in the [](cloud-api.md) section.

### April 2025

Starting from version 2025.1 of %product%, the %cloud% UI contains the **Insights** page available by clicking the
button in the upper-right part of the UI. The description of this page is available on the [](insights.md) page
of this documentation.

Now you can also configure [Single Sign-on](cloud-sso.md) to authenticate using various third-party authentication providers.

### July 2024

The new project setup is implemented in %cloud%. Now you can choose how you would like to run %product%, and the
wizard will guide you through the configuration process. This covers running %product% locally as well as using various
CI/CD solutions.

The detailed information is available in the [](Quick-start.topic#quickstart-prerequisites) section of this documentation.


