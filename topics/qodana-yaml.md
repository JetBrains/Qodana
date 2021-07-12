[//]: # (title: Configure a Profile via qodana.yaml)

Qodana runs are configured via the `qodana.yaml` configuration file. Information stored in `qodana.yaml` overrides the default inspection profile settings and default configurations of Qodana linters. You can specify such overrides in the [HTML report](results.md), and the changes are imported to `qodana.yaml` automatically. To run subsequent checks with this customized configuration, save the file to the project's root directory. Alternatively, you can edit the `qodana.yaml` configuration file manually. This section will guide you through necessary settings.

<note>

Configuration through `qodana.yaml` is only supported by the Qodana product. It is not supported by any other JetBrains products like IntelliJ IDEA or PhpStorm.

</note>

## Set up a profile

Out of the box, Qodana provides several predefined profiles: 
 * `qodana.recommended`&nbsp;&mdash; the default profile containing a preselected set of IntelliJ IDEA Java and Kotlin inspections.
 * `empty`&nbsp;&mdash; an empty profile containing no inspections, which can be used as a basis for manual configuration.

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

## Exclude paths from the analysis scope
{id="exclude-paths"}

You can specify that the files in a certain directory are not analyzed. This can be done for a certain inspection or for all inspections.

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

You can find specific inspection IDs in the Profile settings in the HTML report or in the `.xml` file with your inspection profile.

## Include an inspection into the analysis scope

If an inspection is not contained in the selected profile, you can include it into the analysis scope explicitly via the `include` directive.

```yaml
profile:
    name: empty
include:
  - name: SomeInspectionId
```

In this example, the `empty` profile, which contains no inspections, is specified, and the `SomeInspectionId` inspection is explicitly included into the analysis scope. As a result, only the check performed by the `SomeInspectionId` inspection will be included in the Qodana run.

## Fail threshold

Add a fail threshold to use as a quality gate:

```yaml
failThreshold: <number>
```

[//]: # "Explain exit 255"

When this number of problems is reached, the container executes `exit 255`. Can be used to make the CI step fail. The default value is `10000`.


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
* `SomeInspectionId` inspection is explicitly enabled, although it is disabled in the profile
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