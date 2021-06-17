[//]: # (title: Qodana.yaml)

Information stored in `qodana.yaml` overrides the default inspection profile settings and default configurations of Qodana linters. Namely, you can specify a certain profile name, exclude paths from the analysis scope, disable or enable inspections included in your profile, and so on. You can specify such overrides directly in the [UI report](ui-overview.md): in the Problem explorer for specific reported problems and paths, and in profile settings for inspections. All changes made via the UI are automatically imported into `qodana.yaml`, which file should be saved to the project's root directory if you want to run subsequent checks with the same configuration. Alternatively, you can read or edit the `qodana.yaml` configuration file manually. This section will guide you through necessary settings.

**Note**: Configuration through `qodana.yaml` is only supported by the Qodana product. It is not supported by any other JetBrains products like IDEA or PhpStorm.

## Set up a profile

The default profile is `qodana.recommended`. You can specify other profiles available in the respective IntelliJ Platform IDE for your source project. If you are using a CI system, make sure that the **.xml** file with this profile is available in the working directory where the VCS stores your project before building it. Here you can find IDEA profiles for embedding to Qodana docker images: [github.com/JetBrains/qodana-profiles](https://github.com/JetBrains/qodana-profiles).


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

## Exclude paths from the analysis scope
{id="exclude-paths"}

It is possible to specify that files in a certain directory are not analyzed. You can do it for a certain inspection or for all inspections.

For all inspections:

```yaml
exclude:
  - name: All
    paths:
      - asm-test/src/main/java/org
      - asm/Visitor.java
      - benchmarks
```

For inspections specified by the ID:
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

**Note**: You can find specific inspection IDs: 1) in the Profile settings in the UI report, 2) in the .xml file with your inspection profile.

## Fail threshold

Add a fail threshold to use as a quality gate:

```yaml
failThreshold: <number>
```

[//]: # "Explain exit 255"

When this number of problems is reached, the container executes `exit 255`. Can be used to make the CI step fail.

The default value is `10000`.

## Clone Finder license overrides 

[//]: # "Check if the new parameters are implemented"

You need license overrides when you want to stop seeing warnings about certain mismatched licenses in Clone Finder's reports. For example, Clone Finder's default license compatibility matrix specifies that a queried project with the **GPL-3.0-only** license may not use code from projects with the **ISC** license. That's why Qodana Clone Finder will show a warning for duplicate code fragments with such mismatched licenses. However, if your legal advisor says it is OK, you can specify to ignore warnings for this specific license in reference projects. You can do so in the UI report via the Problem explorer or directly in `qodana.yaml` as shown in the example below.

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

## License Audit Configuration

Use license identifiers from [SPDX License List](https://spdx.org/licenses/).

### Exclude inspections
By default, Qodana License Audit includes all supported inspections.

Exclude inspections from analysis:

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

### Allowed and prohibited licenses

Override predefined list of licences:

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

where `key` is project license, dependency license specified in `allowed` or `prohibited`.

### Override dependency license

Override a dependency license if it has been detected incorrectly:

```yaml
inspections:
 LicenseAudit:
   dependencyOverrides:
       - name: "numpy"
         version: "1.19.1"
         licenses:
           - "BSD-3-Clause"
```

where `name` is dependency name, `version` is dependency version and `licenses` - list of new redefined dependency licenses used by License Audit.

### Ignore dependency license

Ignore a dependency license to hide the related problems from the view:

```yaml
inspections:
  LicenseAudit:
    dependencyIgnores:
      - name: "numpy"
        licenses:
          - "GPL-3.0-only"
```

where `name` is dependency name, `licenses` - list of dependency licenses ignored for dependency.

### Monorepo support

By default, Qodana License Audit runs on the given project root, but you can customize this behavior if you have different applications with different package managers declared in subdirectories. Specify `paths` – paths of the directories you want to run the tool relative to your project root.

```yaml
inspections:
  LicenseAudit:
    paths:
      - "."
      - "ui/"
```

If you want the root of your project to be scanned by the tool when you've specified paths in the configuration, don't forget to include `.` path.

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

Other package managers supported do not allow specifying scopes.

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

* **threshold** – license detection threshold value from 0.0 to 1.0 to
* **includeText** – include license text license was detected by to the report or not
* **deep** – run deep license detection – check every file and always detect licenses from dependencies, even when they were declared on package level.

### Example with different options

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

## An example with different configuration options

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
* `SomeInspectionId` inspection is enabled (although it is disabled in the profile)
* `Annotator` inspection is disabled for all paths
* `AnotherInspectionId` inspection is disabled for `relative/path` and `another/relative/path`
* no inspections are conducted over these paths: `asm-test/src/main/java/org`, `benchmarks`, `tools`
