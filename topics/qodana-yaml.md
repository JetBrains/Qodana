[//]: # (title: Qodana.yaml)

Using the Problem explorer in the [UI report](ui-overview.md), you can specify what types of problems and what files shouldn't be reported (exclusions). This information is stored in `qodana.yaml` as overrides to default profile settings. The file is stored under your project's root directory. In this section, you can learn how to customize profile settings _manually_.

[//]: # "Note that configuration through `qodana.yaml` is only supported by the Qodana product. It is not supported by any other JetBrains products like IDEA or PhpStorm."

## Set up a profile
[//]: # "How do I set a profile on my own? What values are possible? How do I use the .xml?"

By the name:

```yaml
profile:
    name: %name%
```

By the path:

```yaml
profile:
    path: relative/path/in/your/project.xml
```

## Exclude paths from the analysis scope

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

[//]: # "how do i get the an inspection ID? Does this example also show how to exclude an inspection for all paths (Annotator)?"

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

## Fail threshold

Add a fail threshold to use as a quality gate:

```yaml
failThreshold: <number>
```

[//]: # "Explain exit 255"

When this number of problems is reached, the container executes `exit 255`. Can be used to make the CI step fail.

The default value is `10000`.

## Clone Finder license override 

You need to specify license overrides when....

[//]: # "Clarify!"

When Clone Finder default license compatibility matrix suits your needs, you don't need any license overrides provided in `qodana.yaml`.

```yaml
version: 1.0
profile:
  name: qodana.recommended
inspections:
  CloneFinder:
    failThreshold: 100
    licenseOverrides:
      - from: MIT
        to: GPL-3.0-only
        forwardCompatible: true
        backwardCompatible: false
exclude:
  - name: CloneFinder
    paths:
      - copied_file_2.py
```
[//]: # "Clarify!"

* **forwardCompatible** sets whether you can copy code from a reference project under the `to` license to the queried project under the `from` license
* **backwardCompatible**  sets whether you can copy from a reference project under the `from` license to the queried project under the `to` license
  
In the example above, the behaviour is as follows:

If in the reference project (`from` project) the code is covered with the `GPL-3.0-only` license and in the queried project (`to` project) the license is set to `MIT`, then a license mismatch is reported, otherwise there will be no warning for the clone found.

 

## An example with different exclude options

[//]: # "It is almost the same as in 'For inspections specified by the ID:'"

```yaml
version: 1.0
failThreshold: 0
profile:
  name: qodana.recommended
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

