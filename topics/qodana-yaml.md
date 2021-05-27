[//]: # (title: Qodana.yaml)

Qodana runs can be customized with the `qodana.yaml` file stored under your project's root directory.
Note that configuration through `qodana.yaml` is only supported by the Qodana product.
It is not supported by any other JetBrains products like IDEA or PhpStorm.

## Set up a profile

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

## Exclude paths

Exclude paths from the analysis scope for all inspections:

```yaml
exclude:
  - name: All
    paths:
      - asm-test/src/main/java/org
      - asm/Visitor.java
      - benchmarks
```

Exclude paths from the analysis scope for all inspections by the ID:
[//]: # "how do i get the id?"

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

When this number of problems is reached, the container executes `exit 255`. Can be used to make the CI step fail.

## Clone Finder license override 

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
 
* **forwardCompatible** describes the compatibility from referenced project to the queried project
* **backwardCompatible** describes the compatibility from queried project to the referenced project

In this example the behaviour will be:
If in the referenced project ('from' project) the code will be covered with GPL-3.0-only license and in queried project ('to' project) the license will be set to MIT, then the analysis will report license mismatch, otherwise there will be no warning for the clone found.

In case when Clone Finder default license compatibility matrix suited yur needs you don't need any license overrides provided in qodana.yaml. 

## An example with different exclude options

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

