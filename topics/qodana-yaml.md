[//]: # (title: YAML file)

<var name="code-inspection-profiles-ide-help-url" value="https://www.jetbrains.com/help/idea/?Customizing_Profiles"/>
<var name="ide" value="IDE"/>
<var name="incorrect-formatting" value="https://www.jetbrains.com/help/inspectopedia/IncorrectFormatting.html"/>

<link-summary>You can configure Qodana via a YAML-formatted file. By default, this file should have the qodana.yaml 
name and be contained in the root directory of your project.</link-summary>

By default, Qodana reads configurations from the `qodana.yaml` file contained in the root directory of your project.
You can override this filename using the `--config` option, see the [](docker-image-configuration.topic#docker-config-reference-custom-yaml-config) section. For convenience, this 
will be referred in this section using the default `qodana.yaml` name.

Configurations applied in `qodana.yaml` override the default inspection profile settings and default configurations of 
Qodana linters, you can configure it using the [HTML report](ui-overview.md) section, and all changes will be applied 
automatically.

The JSON schema for `qodana.yaml` is published in the [SchemaStore](https://www.schemastore.org/qodana-1.0.json)
project, which provides completion and basic validation in IDEs.

To run subsequent analyses with this customized configuration, save the file in the root directory of your project.
Alternatively, you can edit the `qodana.yaml` configuration file manually.
This section will guide you through the necessary settings.

<note>
The configuration saved in the <code>qodana.yaml</code> file affects only %product% linters and does not impact other 
products, such as IntelliJ IDEA or PhpStorm.
</note>

<warning>
It is highly recommended not to store tokens, passwords, or any other secret information in the <code>qodana.yaml</code> file.
</warning>

## Run custom commands

<link-summary>Using the bootstrap key of qodana.yaml, %instance% can perform actions before running analysis.</link-summary>

During analyses, %product% linters may report that some inspections cannot find classes, packages, files or cannot resolve references
although linters related to [JVM](jvm.md), [.NET](dotnet.md) and [Golang](golang.md) try to figure out the
build system and project structure automatically. In these cases, %instance% needs a bit of help:

* Install third-party packages or libraries
* Run a program that sets up the build environment

These actions are carried out using the `bootstrap` [key](qodana-yaml.md#Run+custom+commands) of the `qodana.yaml` file
contained in the root directory of your project:

```yaml
bootstrap: |+
  set -eu
  # For PHP projects that use Laravel:
  #composer require --dev barryvdh/laravel-ide-helper

  # For JavaScript projects that use Node.js:
  #npm install

  # For Python projects
  #pip install -r requirements.txt 
```

> You can investigate %product% behavior using files contained in the
> [`/data/results`](troubleshooting.topic#troubleshooting-qodana-log-files) directory.

To be able to use syntax highlighting and validation in your IDE, you can create the `prepare-qodana.sh` shell script
and save it in the root directory of your project:

```shell
#! /bin/sh
# Example bootstrap steps, see https://jetbrains.com/help/qodana/before-running-qodana.html
set -eu

# For PHP projects that use Laravel:
#composer require --dev barryvdh/laravel-ide-helper

# For JavaScript projects that use Node.js:
#npm install
```

Run the script in a %instance% Docker container using the `bootstrap` key:

```shell
bootstrap: sh ./prepare-qodana.sh
```

To run %product% as the root user, you may need to invoke the ` --user=root` [option](docker-image-configuration.topic#docker-config-reference-qodana-scan).

## Set up a profile

Information about existing %product% profiles is available in the [](inspection-profiles.md#inspection-profiles-existing-profiles) section. 

You can configure %product% inspection profiles using the `profile` key, for example:

```yaml
profile:
    inspections:
        - group: "category:Java/Probable bugs"
          enabled: true

        - inspection: RedundantIf
          enabled: true
```

Information about available configuration options is available in the [](inspection-profiles.md#inspection-profiles-custom-profiles) section.

## Exclude paths from the analysis scope
{id="exclude-paths"}

<link-summary>You can exclude files and paths from analysis.</link-summary>

You can exclude files and paths from analyses on a per-analysis basis and for all inspections at once.
Information about inspection IDs is available on the [Inspectopedia](https://www.jetbrains.com/help/inspectopedia/) website.

To exclude all paths in a project from the analysis scope, omit the `paths` node.

<note>Starting from version 2022.3, if using the <code>qodana.recommended</code> and <code>qodana.starter</code> 
profiles, Qodana reads <code>.gitignore</code> files of your project and defines the files and folders to be ignored 
during the analysis.</note>

### Examples
{id="exclude-example"}

<link-summary>You can exclude paths from analyses for all inspections, as well as for specific inspections. </link-summary>

Exclude all inspections for specified project paths:

```yaml
exclude:
  - name: All
    paths:
      - asm-test/src/main/java/org
      - asm/Visitor.java
      - benchmarks
```

Exclude inspections specified by ID for specified project paths:
{id="exclude-inspection"}

```yaml
exclude:
  - name: Annotator
  - name: AnotherInspectionId
    paths:
      - relative/path
      - another/relative/path
  - name: All
    paths:
      - asm-test/src/main/java/org
      - asm
      - benchmarks
      - tools
```

You can find specific inspection IDs in the Profile settings in the HTML report or in the `.xml` file with your inspection profile.

## Include an inspection into the analysis scope

<link-summary>You can tell %product% to analyze files of a certain directory using an inspection that is not contained in the selected profile.</link-summary>

You can tell %product% to analyze files of a certain directory using an inspection that is not contained in the selected profile. 
This can be done on a per-analysis basis. To include all paths in a project into the inspection scope, omit the `paths` node.
Information about inspection IDs is available on the [Inspectopedia](https://www.jetbrains.com/help/inspectopedia/) website.

### Example
{id="include-example"}

In this example, the `empty` profile, which contains no inspections, is specified, and the `SomeInspectionId` inspection is explicitly included in the analysis scope for the `tools` directory. As a result, only the check performed by the `SomeInspectionId` inspection the `tools` directory contents will be included in the Qodana run.

```yaml
  profile:
  name: empty
include:
  - name: SomeInspectionId
    paths:
    - tools
```


## Set a quality gate

<link-summary>You have several options for configuring a quality gate.</link-summary>

You have several options to configure [quality gates](quality-gate.topic).

You can add a fail threshold to control the total number of problems in a project, which is supported by
all linters: 

```yaml
failThreshold: <number>
```

> When running in the baseline mode, a threshold is calculated as the sum of new and absent problems. Unchanged results are ignored.
{style="note"}

All linters except [%dotnet-co%](dotnet.md) and [%clang%](clang.md) let you use the following configuration:

```yaml
failureConditions:
  severityThresholds:
    any: <number> # Total problems
    critical: <number> # Critical and other severities
    high: <number>
    moderate: <number>
    low: <number>
    info: <number>
  testCoverageThresholds:
    fresh: <number> # Fresh code coverage
    total: <number> # Total code coverage
```

In this configuration, exceeding just one setting limitation will make the build fail.

The `severityThresholds:any` option lets you configure the total number of problems. Options like 
`severityThresholds:critical` let you configure quality gates for each [problem severity](faq.topic#faq-severities).
The `testCoverageThresholds:fresh` and `testCoverageThresholds:total` options let you configure the total and fresh code 
coverage supported by [several linters](quality-gate.topic#quality-gate-code-coverage). 

## Override the default run scenario

```yaml
script:
  name: <script-name>
  parameters:
      <parameter>: <value>
```

You can override the standard %instance% behavior, which can be helpful in the case of the 
[PHP version migration](php-language-upgrade.topic). To analyze your code from this perspective, you can run the 
`php-migration` scenario.     

By default, %instance% employs the `default` scenario, which means the normal %instance% run equivalent to this setting:

```yaml
script:
  name: default
```

## Example of different configuration options

<link-summary>Navigate to the section to see the combination of different configuration options.</link-summary>

```yaml
version: 1.0
failThreshold: 0
profile:
  name: qodana.recommended
include:
  - name: SomeInspectionId
exclude:
  - name: Annotator
  - name: AnotherInspectionId
    paths:
      - relative/path
      - another/relative/path
  - name: All
    paths:
      - asm-test/src/main/java/org
      - benchmarks
      - tools
```

In the example above,
* `SomeInspectionId` inspection is explicitly enabled for all paths, although it is disabled in the profile
* `Annotator` inspection is disabled for all paths
* `AnotherInspectionId` inspection is disabled for `relative/path` and `another/relative/path`
* no inspections are conducted over these paths: `asm-test/src/main/java/org`, `benchmarks`, `tools`

## Specify a linter

<link-summary>You can specify a linter that you are going to employ.</link-summary>

Using the `linter` option, you can specify a linter that you are going to employ. For example:

```yaml
linter: %jvm-co-a-linter%
```

## Specify directory in your project

Use the `onlyDirectory` option to specify a directory inside your project that has to be analyzed.
This has to be specified relatively to the project root, for example:

```yaml
onlyDirectory: project-a
```

This is useful while analyzing [monorepo projects](monorepo-project.md).


## Configure the JDK version

<link-summary>For JVM-based linters, you can configure the JDK version.</link-summary>

You can configure the JDK version for these linters:

* [%jvm%](jvm.md)
* [%jvm-co%](jvm.md)
* [%jvm-co-a%](jvm.md)

<include from="lib_qd.topic" element-id="configure-jdk-qodana-yaml" use-filter="configure-jdk-qodana-yaml,empty"/>

To learn more about configuring JDK, see the [](configure-jdk.md) section. 

## Configure the PHP version

<link-summary>For JVM-based linters, you can configure the JDK version.</link-summary>

You can configure the PHP version before running the [%php%](php.md) linter: 

```yaml
php:
  version: "X.x"
```

## Disable sanity checks

<link-summary>By default, sanity checks are enabled in %instance%, but you can disable them.</link-summary>

By default, sanity checks are enabled in %instance%. You can disable them using this snippet: 

```yaml
disableSanityInspections: true
```

## Configure license audit
{id="configure-license-audit"}

<link-summary>You can configure the license audit feature by configuring the CheckDependencyLicenses inspection.</link-summary>

Starting from version 2024.1 of %product%, the [license audit](license-audit.topic) feature is enabled by default. You can disable it by 
excluding the `CheckDependencyLicenses` inspection:

```yaml
exclude:
  - name: CheckDependencyLicenses
```

### Ignore a dependency

<link-summary>You can ignore a dependency to hide the related problems from the report.</link-summary>

Ignore a dependency to hide the related problems from the report:

```yaml
dependencyIgnores:
  - name: "enry"
```

where `name` is the dependency name to ignore.

In the example above, the `enry` dependency is completely excluded from the analysis. Because any possible license-related problems are dismissed, the dependency won't be included in the report at all. This is useful to quickly hide internal dependencies that do not need to be mentioned in the report.

### Allow or prohibit a license

<link-summary>You can override the license compatibility matrix predefined in %product% by allowing or prohibiting licenses.</link-summary>

Override the predefined license compatibility matrix:

```yaml
licenseRules:
  - keys:
      - "PROPRIETARY-LICENSE"
      - "MIT"
    prohibited:
      - "BSD-3-CLAUSE-NO-CHANGE"
    allowed:
      - "ISC"

  - keys: [ "Apache-2.0" ]
    prohibited:
      - "MIT"
```

In this configuration,  `keys` is the project license(s) and the dependency licenses identifiers are specified in `allowed` or `prohibited`.

### Override a dependency license

<link-summary>You can override a dependency license identifier.</link-summary>

Override a dependency license identifier:

```yaml

dependencyOverrides:
  - name: "jaxb-runtime"
    version: "2.3.1"
    url: "https://github.com/javaee/jaxb-v2"
    licenses:
      - key: "CDDL-1.1"
        url: "https://github.com/javaee/jaxb-v2/blob/master/LICENSE"
      - key: "GPL-2.0-with-classpath-exception"
        url: "https://github.com/javaee/jaxb-v2/blob/master/LICENSE"
```

where `name` is the dependency name, `version` is the dependency version, and `licenses` is the list of redefined dependency licenses.

In the example above, you 'tell' Qodana to detect CDDL-1.1, GPL-2.0-with-classpath-exception and no other licenses for jaxb-runtime (only 2.3.1). This is useful when a dependency is dual-licensed, and you want to omit some license or when it's not possible to detect the license from the dependency sources correctly.

### Custom dependencies

<link-summary>You can include a custom dependency in the license compatibility matrix.</link-summary>

Currently, the license audit with %instance% is possible only for JPS, Maven, Gradle, npm, yarn and composer projects. To include the dependency that should be mentioned in the report but is impossible to detect from the project sources, use `customDependencies` to specify it:

```yaml
customDependencies:
  - name: ".babelrc JSON Schema (.babelrc-schema.json)"
    version: "JSON schema for Babel 6+ configuration files"
    licenses:
      - key: "Apache-2.0"
        url: "https://github.com/SchemaStore/schemastore/blob/master/LICENSE"
```

## Configure Quick-Fixes

<link-summary>You can apply the cleanup or apply Quick-Fix strategies.</link-summary>

Using the `fixesStrategy` option, you can choose among the available [Quick-Fix strategies](quick-fix.md#How+Quick-Fix+works):

```yaml
fixesStrategy: cleanup/apply
```

## Configure the taint analysis
{id="configure-taint-analysis"}

<link-summary>Learn how you can configure the taint analysis feature.</link-summary>

<include from="taint-analysis.md" element-id="running-taint-analysis"/>

## Configure the vulnerability checker

<link-summary>Learn how you can configure the vulnerability checker feature.</link-summary>

To start using the [](vulnerability-checker.md) feature, enable
the `VulnerableLibrariesGlobal` inspection:

<include from="vulnerability-checker.md" element-id="package-checking-enable"/>

## Manage plugins

<link-summary>You can specify the plugins that will be downloaded and invoked during inspection.</link-summary>

You can specify the plugins that will be downloaded and invoked during inspection. 

```yaml
plugins:
  - id: <plugin.id>
```
Here, `<plugin-id>` denotes the Plugin ID from [JetBrains Marketplace](https://plugins.jetbrains.com/). For example, 
for [Grazie Professional](https://plugins.jetbrains.com/plugin/16136-grazie-professional), the Plugin ID will be `com.intellij.grazie.pro`. To find the Plugin ID, on the plugin
page click the **Overview** tab and then navigate to the **Additional Information** section.

Plugin cache is stored in the `/data/cache/plugins` directory.

To install third-party software required for your plugins, you can:

* Use the [`bootstrap`](before-running-qodana.md) key.
* Develop your custom `Dockerfile` that starts with `FROM jetbrains/qodana...`. You can use %instance% `Dockerfile`
examples available on [GitHub](https://github.com/jetbrains/qodana-docker).

## Incorrect Formatting inspection

The  [`IncorrectFormatting`](%incorrect-formatting%) inspection consolidates multiple formatting errors contained in
a file into a single problem instead of listing every issue separately. Now, a single problem per file is displayed with
example snippets to help you fix issues faster.

This feature is available for all [linters](linters.md) except %cpp%, %clang%, and %dotnet-co%.

To start using it, enable the `IncorrectFormatting` inspection in your %product%
[inspection profile](inspection-profiles.md) configuration, for example:

```yaml
include:
  - name: IncorrectFormatting
```

## Specify a CMake preset

Customize the %cpp% linter by using [CMake presets](clang.md#Configure+compilers+and+environments). Invoke presets using 
the `cpp` and `cmakePreset` options:

```yaml
cpp:
  cmakePreset: my-qodana-preset
```

## Configure native mode

You can configure [native mode](deploy-qodana.md#deploy-qodana-native-mode) by specifying a [linter](linters.md) and 
setting the `withinDocker` option to `false`, for example:

```yaml
linter: qodana-dotnet
withinDocker: false
```

> The `ide` notation available in previous versions of %product% is deprecated and will be removed in future versions of the product.
{style="note"}

Native mode is currently available for the following %product% linters:

<table>
    <tr>
        <td>
            Linter name
        </td>
        <td>
            Description
        </td>
    </tr>
    <tr>
        <td>
            <code>%jvm-linter%</code>
        </td>
        <td>
            <a href="jvm.md">%jvm%</a>
        </td>
    </tr>
    <tr>
        <td>
            <code>%jvm-co-linter%</code>
        </td>
        <td>
            <a href="jvm.md">%jvm-co%</a>
        </td>
    </tr>
    <tr>
        <td>
            <code>%php-linter%</code>
        </td>
        <td>
            <a href="php.md">%php%</a>
        </td>
    </tr>
    <tr>
        <td>
            <code>%js-linter%</code>
        </td>
        <td>
            <a href="js.md">%js%</a>
        </td>
    </tr>
    <tr>
        <td>
            <code>%dotnet-linter%</code>
        </td>
        <td>
            <a href="dotnet.md">%dotnet%</a>
        </td>
    </tr>
    <tr>
        <td>
            <code>%go-linter%</code>
        </td>
        <td>
            <a href="golang.md">%go%</a>
        </td>
    </tr>
    <tr>
        <td>
            <code>%python-linter%</code>
        </td>
        <td>
            <a href="python.md">%python%</a>
        </td>
    </tr>
    <tr>
        <td>
            <code>%python-co-linter%</code>
        </td>
        <td>
            <a href="python.md">%python-co%</a>
        </td>
    </tr>
    <!--<tr>
        <td>
            <code>qodana-cpp:2025.2-eap</code>
        </td>
        <td>
            <a href="clang.md">%clang%</a>
        </td>
    </tr>-->
</table>

## Configure Java and Kotlin projects in monorepo

Using the `rootJavaProjects` key, you can specify which projects should be included in the analysis, for example:

```yaml
rootJavaProjects:
- "./gradleProject"
- "./mavenModule/pom.xml"
```

By default, %product% recursively collects projects from subdirectories and imports them for analysis.
This change enables incremental analysis and fixes for projects where analyzed project and VCS root are different.

