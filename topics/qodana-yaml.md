[//]: # (title: YAML file)

<var name="code-inspection-profiles-ide-help-url" value="https://www.jetbrains.com/help/idea/?Customizing_Profiles"/>
<var name="ide" value="IDE"/>

Qodana runs are configured via the `qodana.yaml` configuration file contained in the root directory of your project.
Configuration settings of `qodana.yaml` override the default inspection profile settings and default configurations of Qodana linters.
You can specify such overrides in the [HTML report](results.md),
and the changes are imported to `qodana.yaml` automatically.

The JSON schema for `qodana.yaml` is published in the [SchemaStore](https://www.schemastore.org/json/)
project, which allows for completion and basic validation in IDEs.

To run subsequent checks with this customized configuration, save the file to the project's root directory.
Alternatively, you can edit the `qodana.yaml` configuration file manually.
This section will guide you through the necessary settings.

<note>

Configuration through `qodana.yaml` is only supported by Qodana.
It is not supported by any other JetBrains products like IntelliJ IDEA or PhpStorm.

</note>

## Run custom commands

Using the `bootstrap` option of `qodana.yaml`, %product% can perform actions before running inspections. 

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

All possible options for configuring profiles are explained in the [](inspection-profiles.md) section.

### Exclude paths from the analysis scope
{id="exclude-paths"}

You can specify that the files in a certain directory are not analyzed. This can be done on a per-inspection basis or for all inspections at once. To exclude all paths in a project from the inspection scope, omit the `paths` node.

<note>Starting from version 2022.3, if using the <code>qodana.recommended</code> and <code>qodana.starter</code> 
profiles, Qodana reads <code>.gitignore</code> files of your project and defines the files and folders to be ignored 
during inspections.</note>

#### Example
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

### Include an inspection into the analysis scope

You can specify that the files in a certain directory are analyzed by an inspection that is not contained in the selected profile. This can be done on a per-inspection basis. To include all paths in a project into the inspection scope, omit the `paths` node.

#### Example
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


### Set a fail threshold

Add a fail threshold to use as a quality gate:

```yaml
failThreshold: <number>
```

[//]: # "Explain exit 255"

When this number of problems is reached, the container executes `exit 255`. This can be used to make a CI step fail. The default value is `10000`.

<note>

When running in [baseline mode](docker-image-configuration.xml#docker-config-reference-baseline), a threshold is calculated as the sum of _new_ and _absent_ problems. _Unchanged_ results are ignored.

</note>

### Override the default run scenario

```yaml
script:
  name: <script-name>
  parameters:
      <parameter>: <value>
```

You can override the standard %product% behavior, which can be helpful in the case of the 
[PHP version migration](php-language-upgrade.xml). To inspect your code from this perspective, you can run the 
`php-migration` scenario.     

By default, %product% employs the `default` scenario, which means the normal %product% run equivalent to this setting:

```yaml
script:
  name: default
```

### Example of different configuration options

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

Using the `linter` option, you can specify the linter that you are going to employ. For example:

```yaml
linter: jetbrains/qodana-jvm-android:2023.1-eap
```

## Configure the JDK version

You can configure the JDK version for these linters:

* [](qodana-jvm.md)
* [](qodana-jvm-community.md)
* [](qodana-jvm-android.md)

<include src="lib_qd.xml" include-id="configure-jdk-qodana-yaml" use-filter="configure-jdk-qodana-yaml,empty"/>

To learn more about configuring JDK, see the [](configure-jdk.md) section. 

## Disable sanity checks

By default, sanity checks are enabled in %product%. You can disable them using this snippet: 

```yaml
disableSanityInspections: true
```

## Configure the License audit

You can enable the License audit feature using the `CheckDependencyLicenses` inspection:

```yaml
include:
  - name: CheckDependencyLicenses
```

### Ignore a dependency

Ignore a dependency to hide the related problems from the report:

```yaml
dependencyIgnores:
  - name: "enry"
```

where `name` is the dependency name to ignore.

In the example above, the `enry` dependency is completely excluded from the analysis. Because any possible license-related problems are dismissed, the dependency won't be included in the report at all. This is useful to quickly hide internal dependencies that do not need to be mentioned in the report.

### Allow or prohibit a license

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

Currently, the license audit with Qodana is possible only for JPS, Maven, Gradle, npm, yarn and composer projects. If you want to include the dependency that should be mentioned in the report but is impossible to detect from the project sources, you can use `customDependencies` to specify it:

```yaml
customDependencies:
  - name: ".babelrc JSON Schema (.babelrc-schema.json)"
    version: "JSON schema for Babel 6+ configuration files"
    licenses:
      - key: "Apache-2.0"
        url: "https://github.com/SchemaStore/schemastore/blob/master/LICENSE"
```

## Manage plugins

You can specify the plugins that will be downloaded and invoked during inspection. 

```yaml
version: "1.0"
plugins:
  - id: <plugin.id>
```
Here, `<plugin-id>` denotes the plugin ID from [JetBrains Marketplace](https://plugins.jetbrains.com/). For example, 
for [Grazie Professional](https://plugins.jetbrains.com/plugin/16136-grazie-professional) the Plugin ID will be 
`com.intellij.grazie.pro`.

Plugin cache is stored in the `/data/cache/plugins` directory.

To install third-party software required for your plugins, you can:

* Use the [`bootstrap`](before-running-qodana.md) option
* Develop your custom `Dockerfile` that starts with `FROM jetbrains/qodana...`. You can use %product% `Dockerfile`
examples available on [GitHub](https://github.com/jetbrains/qodana-docker).

