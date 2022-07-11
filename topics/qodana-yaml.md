[//]: # (title: Configure profile)

<var name="code-inspection-profiles-ide-help-url" value="https://www.jetbrains.com/help/idea/?Customizing_Profiles"/>
<var name="ide" value="IDE"/>

Qodana runs are configured via the `qodana.yaml` configuration file.
Information stored in `qodana.yaml` overrides the default inspection profile settings and default configurations of Qodana linters.
You can specify such overrides in the [HTML report](results.md),
and the changes are imported to `qodana.yaml` automatically.

The JSON schema for `qodana.yaml` is published in the [SchemaStore](https://www.schemastore.org/json/)
project, which allows for completion and basic validation in IDEs.

To run subsequent checks with this customized configuration, save the file to the project's root directory.
Alternatively, you can edit the `qodana.yaml` configuration file manually.
This section will guide you through necessary settings.

<note>

Configuration through `qodana.yaml` is only supported by Qodana.
It is not supported by any other JetBrains products like IntelliJ IDEA or PhpStorm.

</note>

## Default profiles

Out of the box, Qodana provides several predefined profiles:
* `empty`: an empty profile containing no inspections, which can be used as a basis for manual configuration.
* `qodana.starter`: the default profile that triggers the [3-phase analysis](#three-phase-analysis).
* `qodana.recommended`: a profile containing a preselected set of IntelliJ inspections.
* `qodana.sanity`: a profile containing a small preselected set of inspections that perform the project's "sanity" checks. If these checks fail, the project is probably misconfigured, and further examining it will not produce meaningful results. See [](linters.md) for details on configuring a project for the desired linter.

You can specify other profiles available in the respective IntelliJ Platform IDE for your source project. If you are using a CI system, make sure the `.xml` file with this profile resides in the working directory where the VCS stores your project before building it. The IntelliJ IDEA profiles for embedding into Qodana Docker images are hosted in the [qodana-profiles](https://github.com/JetBrains/qodana-profiles) GitHub repository.

## How to choose a proper profile

If you already have an inspection profile for your project, you [can use it](#Set+up+a+profile) with Qodana as a starting point. You can then adjust it via `qodana.yaml` and make it more convenient for the server-side use.

If you want a fresh start, you have two options:
1. Use Qodana in default mode to execute the [three-phase analysis](#three-phase-analysis). You don't need to create a `qodana.yaml` file in this case, but you can add it later to amend a set of checks.
2. Use Qodana with the recommended profile. In this case you need to create a `qodana.yaml` file with a reference to `qodana.recommended`. This profile contains the checks for critical or severe issues in the code, which require attention. This profile does not contain any style checks, and non-critical for the project operability folders, such as `tests`, are ignored.


## Three-phase analysis
{id="three-phase-analysis"}

Sometimes it may be challenging to set up analysis for a big project even with the `qodana.recommended` profile due to large amount of errors reported. To solve this, Qodana offers a 3-phase analysis, where each phase is focused on a certain type of results.

- The first phase is based on the `qodana.starter` profile that contains vital checks only. Non-critical for the project operability folders, such as `tests`, are ignored.

- The second phase reports the conditions that could affect truthfulness or completeness of the results. For example, if your project relies on external resources or generated code, and they are not available during the analysis, the final results could be compromised. Qodana notifies you about such suspicious results.  

- The last phase suggests additional checks that are not so vital for the project but still beneficial. To avoid overwhelming, Qodana analyzes only a fraction of the code, just enough to show you the possible outcome.

[//]: # (We recommend the following Qodana UI guidance to create the most effective profile you can support for your project.)

## Run custom commands

In particular cases, you may need to have a command or script executed in a Qodana Docker container prior to inspecting 
your code. It could be done as part of project preparation, software installation, or any other activity that needs to 
be performed only within the container and that does not affect the Qodana workflow. To solve this task, you can use the 
`bootstrap` option in the `qodana.yaml` file.

So, if you want to install a specific package in the Qodana container using the `apt` tool, you need to add this
line to `qodana.yaml`:

```yaml
bootstrap: apt install <package_name>
```

To run a custom script, save the script file to the project directory and specify execution in 
`qodana.yaml`. For example, this can be:

```yaml
bootstrap: sh ./script.sh
```

## Set up a profile



### Set up a profile by the name

```yaml
profile:
    name: <name>
```

<p>
<include src="lib_qd.xml" include-id="inspection-profile-name-note"/>
</p>

### Set up a profile by the path

```yaml
profile:
    path: relative/path/in/your/project.xml
```

### Exclude paths from the analysis scope
{id="exclude-paths"}

You can specify that the files in a certain directory are not analyzed. This can be done on a per-inspection basis or for all inspections at once. To exclude all paths in a project from the inspection scope, omit the `paths` node.

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

In this example, the `empty` profile, which contains no inspections, is specified, and the `SomeInspectionId` inspection is explicitly included into the analysis scope for the `tools` directory. As a result, only the check performed by the `SomeInspectionId` inspection the `tools` directory contents will be included in the Qodana run.

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

When running in [baseline mode](qodana-jvm-docker-techs.xml#Run+in+baseline+mode), a threshold is calculated as the sum of _new_ and _absent_ problems. _Unchanged_ results are ignored.

</note>

### Override the default run scenario

```yaml
script:
  name: <script-name>
  parameters:
      <parameter>: <value>
```

You can override the standard %product% behavior, which can be helpful in the case of the 
[PHP version migration](qodana-php-language-upgrade.xml). To inspect your code from this perspective, you can run the 
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

## Disable sanity checks

By default, sanity checks are enabled in %product%. You can disable them using this snippet: 

```yaml
disableSanityInspections: true
```

## License audit configuration

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

In the example above, in the analyzed project, the dependency `enry` is completely excluded from the analysis, any possible license-related problems are dismissed, the dependency won't be included in the report at all. This is useful to quickly hide internal dependencies that do not need to be mentioned in the report.

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

In the example above, you 'tell' Qodana to detect CDDL-1.1, GPL-2.0-with-classpath-exception and no other licenses for jaxb-runtime (only 2.3.1). This is useful when a dependency is dual-licensed and you want to omit some license or when it's not possible to detect the license from the dependency sources correctly.

### Custom dependencies

Currently, license audit with Qodana is possible only for JPS, Maven, Gradle, npm, yarn and composer projects. If you want to include the dependency that should be mentioned in the report but is impossible to detect from the project sources, you can use `customDependencies` to specify it:

```yaml
customDependencies:
  - name: ".babelrc JSON Schema (.babelrc-schema.json)"
    version: "JSON schema for Babel 6+ configuration files"
    licenses:
      - key: "Apache-2.0"
        url: "https://github.com/SchemaStore/schemastore/blob/master/LICENSE"
```

## Clone Finder license overrides 

[//]: # "Check if the new parameters are implemented"

You need license overrides when you want to stop seeing warnings about certain mismatched licenses in Clone Finder's reports. For example, Clone Finder's default license compatibility matrix specifies that a queried project with the **GPL-3.0-only** license may not use code from projects with the **ISC** license. That's why Qodana Clone Finder will show a warning for duplicate code fragments with such mismatched licenses. However, if your legal advisor says it is OK, you can specify to ignore warnings for this specific license in reference projects. You can do so in the HTML report via the Problem explorer or directly in `qodana.yaml` as shown in the example below.

```yaml
version: 1.0
profile:
  name: qodana.recommended
inspections:
  CloneFinder:
    failThreshold: 100
    licenseRules:
      - source: GPL-3.0-only
        target: ISC
        compatible: true
exclude:
  - name: CloneFinder
    paths:
      - copied_file_2.py
```

In the example above, using code from **ISC** reference projects (`target`) is allowed in the **GPL-3.0-only** queried project (`source`), although this combination is listed as incompatible, for example, in [choosealicense.com/appendix/](https://choosealicense.com/appendix/).
