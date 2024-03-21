[//]: # (title: YAML file)

<var name="code-inspection-profiles-ide-help-url" value="https://www.jetbrains.com/help/idea/?Customizing_Profiles"/>
<var name="ide" value="IDE"/>

<link-summary>You can configure Qodana via a YAML-formatted file. By default, this file should have the qodana.yaml 
name and be contained in the root directory of your project.</link-summary>

By default, Qodana is configured via the `qodana.yaml` configuration file contained in the root directory of your project.
You can override this filename using the `--config` option, see the 
[](docker-image-configuration.topic#docker-config-reference-custom-yaml-config) for details. For convenience, this 
will be referred in this section using the default `qodana.yaml` name.

Configuration applied in `qodana.yaml` override the default inspection profile settings and default configurations of 
Qodana linters, you can configure it using the [HTML report](results.md) section, and all changes will be applied 
automatically.

The JSON schema for `qodana.yaml` is published in the [SchemaStore](https://www.schemastore.org/json/)
project, which allows for completion and basic validation in IDEs.

To run subsequent checks with this customized configuration, save the file to the project's root directory.
Alternatively, you can edit the `qodana.yaml` configuration file manually.
This section will guide you through the necessary settings.

<note>
Configuration through <code>qodana.yaml</code> is only supported by Qodana.
It is not supported by any other JetBrains products like IntelliJ IDEA or PhpStorm.
</note>

<warning>
It is highly recommended not to store tokens, passwords, or any other secret information in the <code>qodana.yaml</code> file.
</warning>

## Run custom commands

<link-summary>Using the bootstrap option of qodana.yaml, %instance% can perform actions before running inspections.</link-summary>

Using the `bootstrap` option of `qodana.yaml`, %instance% can perform actions before running inspections. 

To install a specific package in the Qodana container using the `apt` tool, add this line to `qodana.yaml`:

```yaml
bootstrap: apt install <package_name>
```

To run a script, save the `prepare-qodana.sh` script file to the project directory and specify execution in 
`qodana.yaml`:

```yaml
bootstrap: sh ./prepare-qodana.sh
```
To learn more about use-cases, see the [](before-running-qodana.md) section.


## Set up a profile

Profile invocation is explained in the [Inspection profiles](inspection-profiles.md#Set+up+a+profile) section. Information
about custom profiles is also provided [here](inspection-profiles.md#Custom+profiles).

## Exclude paths from the analysis scope
{id="exclude-paths"}

<link-summary>You can specify the files to exclude from analysis.</link-summary>

You can specify the files to exclude from analysis on a per-inspection basis or for all inspections at once. 

To exclude all paths in a project from the inspection scope, omit the `paths` node.

<note>Starting from version 2022.3, if using the <code>qodana.recommended</code> and <code>qodana.starter</code> 
profiles, Qodana reads <code>.gitignore</code> files of your project and defines the files and folders to be ignored 
during inspections.</note>

### Example
{id="exclude-example"}

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

<link-summary>You can specify that the files in a certain directory are analyzed by an inspection that is not contained in the selected profile.</link-summary>

You can specify that the files in a certain directory are analyzed by an inspection that is not contained in the selected profile. This can be done on a per-inspection basis. To include all paths in a project into the inspection scope, omit the `paths` node.

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

First of all, you can add a fail threshold to control the total number of problems in a project, which is supported by
all linters: 

```yaml
failThreshold: <number>
```

> When running in the baseline mode, a threshold is calculated as the sum of new and absent problems. Unchanged results are ignored.
{style="note"}

All linters except [](qodana-dotnet-community.md) let you use the following configuration: 

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
[PHP version migration](php-language-upgrade.topic). To inspect your code from this perspective, you can run the 
`php-migration` scenario.     

By default, %instance% employs the `default` scenario, which means the normal %instance% run equivalent to this setting:

```yaml
script:
  name: default
```

## Example of different configuration options

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
linter: jetbrains/qodana-jvm-android:2024.1
```

## Configure the JDK version

<link-summary>For JVM-based linters, you can configure the JDK version.</link-summary>

You can configure the JDK version for these linters:

* [](qodana-jvm.md)
* [](qodana-jvm-community.md)
* [](qodana-jvm-android.md)

<include from="lib_qd.topic" element-id="configure-jdk-qodana-yaml" use-filter="configure-jdk-qodana-yaml,empty"/>

To learn more about configuring JDK, see the [](configure-jdk.md) section. 

## Configure the PHP version

<link-summary>For JVM-based linters, you can configure the JDK version.</link-summary>

You can configure the PHP version before running the [](qodana-php.md) linter: 

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

<link-summary>You can enable the license audit feature by enabling the CheckDependencyLicenses inspection.</link-summary>

You can run the [license audit](license-audit.topic) feature by enabling the `CheckDependencyLicenses` inspection:

```yaml
include:
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

where `keys` is the project license(s); the dependency licenses identifiers are specified in `allowed` or `prohibited`.

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

Currently, the license audit with %instance% is possible only for JPS, Maven, Gradle, npm, yarn and composer projects. If you want to include the dependency that should be mentioned in the report but is impossible to detect from the project sources, you can use `customDependencies` to specify it:

```yaml
customDependencies:
  - name: ".babelrc JSON Schema (.babelrc-schema.json)"
    version: "JSON schema for Babel 6+ configuration files"
    licenses:
      - key: "Apache-2.0"
        url: "https://github.com/SchemaStore/schemastore/blob/master/LICENSE"
```

## Configure quick-fixes

<link-summary>You can apply the cleanup or apply quick-fix strategies.</link-summary>

Using the `fixesStrategy` option, you can choose among the available [quick-fix strategies](quick-fix.md#How+it+works):

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
for [Grazie Professional](https://plugins.jetbrains.com/plugin/16136-grazie-professional) the Plugin ID will be `com.intellij.grazie.pro`. To find the Plugin ID, on the plugin
page click the **Overview** tab and then navigate to the **Additional Information** section.

Plugin cache is stored in the `/data/cache/plugins` directory.

To install third-party software required for your plugins, you can:

* Use the [`bootstrap`](before-running-qodana.md) option
* Develop your custom `Dockerfile` that starts with `FROM jetbrains/qodana...`. You can use %instance% `Dockerfile`
examples available on [GitHub](https://github.com/jetbrains/qodana-docker).

