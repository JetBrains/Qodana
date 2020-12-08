#Qodana. Configuration 

###Qodana.yaml

Qodana runs could be customized with qodana.yaml file stored under root of your project.
Configuration through qodana.yaml is only supported by Qodana product.
It isn't supported by any other JetBrains products like IDEA, PhpStorm, etc.

#### Setup profile
Setup profile by name
```
profile:
    name: %name%
```
Setup profile by path
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
Exclude paths from analysis for all inspections by id:
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