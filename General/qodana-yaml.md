# Qodana. Configuration 

### Qodana.yaml

Qodana runs can be customized with the `qodana.yaml` file stored under your project's root folder.
Note that configuration through `qodana.yaml` is only supported by Qodana product.
It is not supported by any other JetBrains products like IDEA, PhpStorm, etc.

#### Setup profile
Setup profile by name:
```
profile:
    name: %name%
```
Setup profile by path:
```
profile:
    path: relative/path/in/your/project.xml
```

#### Exclude paths
Exclude paths from analysis for all inspections:
```
exclude:
  - name: All
    paths:
      - asm-test/src/main/java/org
      - asm/Visitor.java
      - benchmarks
```
Exclude paths from analysis for all inspections by ID:
```
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

#### Add fail threshold to use in quality gateways 

```
failThreshold: <number>
```

#### Full example
```
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
  - asm
  - benchmarks
  - tools
```