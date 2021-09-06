[//]: # (title: Configure a Profile via qodana.yaml)

Qodana runs are configured via the `qodana.yaml` configuration file. Information stored in `qodana.yaml` overrides the default inspection profile settings and default configurations of Qodana linters. You can specify such overrides in the [HTML report](results.md), and the changes are imported to `qodana.yaml` automatically. 

To run subsequent checks with this customized configuration, save the file to the project's root directory. Alternatively, you can edit the `qodana.yaml` configuration file manually. This section will guide you through necessary settings.

<note>

Configuration through `qodana.yaml` is only supported by the Qodana product. It is not supported by any other JetBrains products like IntelliJ IDEA or PhpStorm.

</note>

## Set up a profile

Out of the box, Qodana provides several predefined profiles: 
* `empty`: an empty profile containing no inspections, which can be used as a basis for manual configuration.
* `qodana.recommended`: the default profile containing a preselected set of IntelliJ IDEA Java and Kotlin inspections.
* `kotlin.only`: a profile containing a preselected set of IntelliJ IDEA Kotlin inspections.
* `php.default`: a profile containing a preselected set of IntelliJ IDEA PHP inspections.

You can specify other profiles available in the respective IntelliJ Platform IDE for your source project. If you are using a CI system, make sure that the `.xml` file with this profile is in the working directory where the VCS stores your project before building it. The IntelliJ IDEA profiles for embedding into Qodana Docker images are hosted in the [qodana-profiles](https://github.com/JetBrains/qodana-profiles) GitHub repository.


Set up a profile by the name:

```yaml
profile:
    name: %name%
```

Set up a profile by the path:

```yaml
profile:
    path: relative/path/in/your/project.xml
```

### Exclude paths from the analysis scope
{id="exclude-paths"}

You can specify that the files in a certain directory are not analyzed. This can be done on a per-inspection basis or for all inspections at once. To exclude all paths in a project from the inspection scope, omit the `paths` node.

#### Example

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

When running in [baseline mode](qodana-intellij-docker-techs.md#Run+in+baseline+mode), a threshold is calculated as the sum of _new_ and _absent_ problems. _Unchanged_ results are ignored.

</note>

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

## License Audit configuration

Use license identifiers from the [SPDX License List](https://spdx.org/licenses/).

### Exclude an inspection
By default, Qodana License Audit includes all supported inspections.

Exclude inspections from the analysis:

```yaml
version: 1.0
profile:
  name: qodana.recommended
exclude:
  - name: NoDependencyLicenses
  - name: ProhibitedDependencyLicense
  - name: UncategorizedDependencyLicense
  - name: UnrecognizedDependencyLicense
  - name: UnrecognizedProjectLicense
```

### Allow or prohibit a license

Override the predefined licence compatibility matrix:

```yaml
inspections:
  LicenseAudit:
    rules:
      - key:
          - "PROPRIETARY-LICENSE"
          - "MIT"
        prohibited:
          - "Apache-2.0"
        allowed:
          - "MIT"
          - "BSD-3-Clause"
          - "ISC"

      - key: "Apache-2.0"
        prohibited:
          - "MIT"
```

where `key` is the project license(s); the dependency licenses are specified in `allowed` or `prohibited`.

### Override a dependency license

Override a dependency license ID if it has been detected incorrectly:

```yaml
inspections:
 LicenseAudit:
   dependencyOverrides:
       - name: "numpy"
         version: "1.19.1"
         licenses:
           - "BSD-3-Clause"
```

where `name` is the dependency name, `version` is the dependency version, and `licenses` is the list of redefined dependency licenses.

In the example above, you 'tell' License Audit to detect BSD-3-Clause and no other licenses for numpy (only 1.19.1).

### Ignore a dependency license

Ignore a dependency license to hide the related problems from the report:

```yaml
inspections:
  LicenseAudit:
    dependencyIgnores:
      - name: "enry"
        licenses:
          - "UNKNOWN"
          
      - name: "numpy"
        licenses:
          - "GPL-3.0-only"
```

where `name` is the dependency name, `licenses` is the list of dependency licenses ignored for the specified dependency.

In the example above, in the analyzed project, the dependency numpy, version 1.19.1 has the GPL-3.0 license (which is supposedly prohibited for this project) and the license for enry (0.1.1) is not recognized. The problems with these dependencies will be ignored in the reports, and you won't see the prohibited and unrecognized license problems you've seen before.

### Monorepo support

By default, Qodana License Audit looks for package manager manifests on the given project root. If you have applications with different package managers declared in subdirectories, use `paths` to specify such subdirectories relative to your project root.

```yaml
inspections:
  LicenseAudit:
    paths:
      - "."
      - "ui/"
```

If you want to scan both specific paths for package manager manifests  _and_ the root of your project, include `.` to the list of paths (for root).

### Dependency scopes

#### Gradle

By default, Qodana License Audit runs Gradle with `runtime` and `runtimeClasspath` configurations. You can specify the wanted Gradle configurations in `dependencyScopes` section.

```yaml
inspections:
  LicenseAudit:
    dependencyScopes:
      - type: "gradle"
        scopes:
          - "runtime"
```

#### npm, yarn

By default, npm or yarn exclude all non-development dependencies. To include development or test dependencies, put `all` to the configuration.

```yaml
inspections:
  LicenseAudit:
    dependencyScopes:
      - type: "yarn"
        scopes:
          - "all"
```

Other package managers supported do not allow specifying the scopes.

### Detector options

Default detector options:

```yaml
inspections:
  LicenseAudit:
    detectorOptions:
      threshold: 0.8
      includeText: true
      deep: false
```

where
* `threshold` is the license detection threshold value from 0.0 to 1.0
* `includeText` specifies whether to add the license text by which the license ID was recognized to the report or not
* `deep` specifies whether to run a deep license detection: check every file and always detect licenses from dependencies, even when they were declared on the package level

### An example with different License Audit overrides

```yaml
failThreshold: 100
profile:
  name: qodana.recommended
inspections:
  LicenseAudit:
    rules:
      - key:
          - "PROPRIETARY-LICENSE"
        prohibited:
          - "Apache-2.0"
        allowed:
          - "BSD-3-Clause"

    dependencyIgnores:
      - name: "numpy"
        licenses:
          - "GPL-3.0-only"

    dependencyScopes:
      - type: "gradle"
        scopes:
          - "runtime"
```
