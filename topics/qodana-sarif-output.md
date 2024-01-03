[//]: # (title: SARIF output)

%product% reports are formatted according to the
[SARIF specification](https://docs.oasis-open.org/sarif/sarif/v2.1.0/os/sarif-v2.1.0-os.html) and are contained in a JSON file.
The %product% implementation of SARIF follows the general format rules, but also specifies several custom properties
contained in [property bags](https://docs.oasis-open.org/sarif/sarif/v2.1.0/os/sarif-v2.1.0-os.html#_Toc34317448).

## Report structure

Here is the structure of reports produced by %product%:


```json
{
  "version": "2.1.0",
  "runs": [
    {
      "tool": {...},
      "invocations": [...],
      "language": "en-US",
      "versionControlProvenance": [...],
      "results": [...],
      "automationDetails": {...},
      "newlineSequences": [...],
      "properties": {...}
    }
  ]
}
```

<anchor name="sarif-run-object"/>

Each report is represented by a `runs` array containing a single %product%
[`run`](https://docs.oasis-open.org/sarif/sarif/v2.1.0/os/sarif-v2.1.0-os.html#_Toc34317484).
This object contains several nested objects, such as:

| Object                                                  | Description                                                           |
|---------------------------------------------------------|-----------------------------------------------------------------------|
| [`tool`](#tool)                                         | Information about the %product% linter, plugins and inspections       |
| [`invocations`](#invocations)                           | Result of the %product% invocation                                    |
| [`versionControlProvenance`](#versionControlProvenance) | The version control system from which the project was checked out     |
| [`results`](#results)                                   | Codebase problems detected by %product%                               |
| [`automationDetails`](#automationDetails)               | Identification of the %product% run                                   |
| [`newlineSequences`](#newlineSequences)                 | The newline sequences that were used for calculating the line numbers |
| [`properties`](#properties)                             | Custom %product% properties, see below                                |

The custom %product% properties are:

| Property        | Description                                                                                                          |
|-----------------|----------------------------------------------------------------------------------------------------------------------|
| `configProfile` | How the inspection profile was found; one of `empty`, `starter`, `recommended`, `path`, `single`, `absent`, `other`. |
| `deviceId`      | The tracking ID used for anonymous statistics.                                                                       |

### tool

The [`tool`](https://docs.oasis-open.org/sarif/sarif/v2.1.0/os/sarif-v2.1.0-os.html#_Toc34317529) object describes
the %product% [linter](linters.md), bundled plugins, and the available inspections.

```json
{
  "tool": {
    "driver": {...},
    "extensions": [...]
  }
}
```

The `tool` object contains two nested objects:

| Object                                 | Description                                              |
|----------------------------------------|----------------------------------------------------------|
| [`driver`](#The+driver+object)         | Information about the invoked [Qodana linter](linters.md)        |
| [`extensions`](#The+extensions+object) | The loaded plugins, as well as all available inspections |

#### The driver object

This object contains information about the invoked [Qodana linter](linters.md).

```json
{
  "driver": {
    "name": "QDPHP",
    "fullName": "Qodana for PHP",
    "version": "222.4190.104",
    "rules": [],
    "taxa": [
      {
        "id": "EditorConfig",
        "name": "EditorConfig"
      },
      {
        "id": "PHP",
        "name": "PHP"
      },
      {
        "id": "PHP/Php Inspections (EA Extended)",
        "name": "Php Inspections (EA Extended)",
        "relationships": [
          {
            "target": {
              "id": "PHP",
              "index": 1,
              "toolComponent": {
                "name": "QDPHP"
              }
            },
            "kinds": [
              "superset"
            ]
          }
        ]
      }
    ]
  }
}
```

The object consists of the following fields:

<anchor name="sarif-taxa-object"/>

| Field      | Description                                                                                                                                                        |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `name`     | ID of the %product% linter                                                                                                                                         |
| `fullName` | Full name of the %product% linter                                                                                                                                  |
| `version`  | Version of the %product% linter                                                                                                                                    |
| `rules`    | Descriptions of the available inspections, as [`reportingDescriptor`](https://docs.oasis-open.org/sarif/sarif/v2.1.0/os/sarif-v2.1.0-os.html#_Toc34317836) objects |
| `taxa`     | The categories of the inspections, including the relationships between categories                                                                                  |

#### The extensions object

Each element of the `extensions` array corresponds to one IntelliJ IDEA plugin,
providing information about the plugin name and version,
as well as the inspections provided by the plugin.

```json
{
  "extensions": [
    {
      "name": "org.editorconfig.editorconfigjetbrains",
      "version": "222.4190",
      "rules": [
        {
          "id": "EditorConfigCharClassRedundancy",
          "shortDescription": {
            "text": "Unnecessary character class"
          },
          "fullDescription": {
            "text": "Reports character classes that consist of a single character. Such classes can be simplified to a character, for example '[a]'→'a'.",
            "markdown": "Reports character classes that consist of a single character. Such classes can be simplified to a character, for example `[a]`→`a`."
          },
          "defaultConfiguration": {
            "enabled": true,
            "level": "warning",
            "parameters": {
              "ideaSeverity": "WARNING",
              "tags": [
                "ideaSeverity"
              ]
            }
          },
          "relationships": [
            {
              "target": {
                "id": "EditorConfig",
                "index": 0,
                "toolComponent": {
                  "name": "QDPHP"
                }
              },
              "kinds": [
                "superset"
              ]
            }
          ]
        }
      ],
      "language": "en-US",
      "contents": [
        "localizedData",
        "nonLocalizedData"
      ]
    }
  ]
}
```

This object contains the following fields:

| Field     | Description                            |
|-----------|----------------------------------------|
| `name`    | The ID of the %product% plugin         |
| `version` | The version of the %product% plugin    |
| `rules`   | The inspections provided by the plugin |

Each inspection from the plugin is described by a
[`reportingDescriptor`](https://docs.oasis-open.org/sarif/sarif/v2.1.0/os/sarif-v2.1.0-os.html#_Toc34317836)
with the following fields:

| Field                  | Description                                                                                                                                                                                                                                                    |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                   | Inspection ID                                                                                                                                                                                                                                                  |
| `shortDescription`     | Short description of the inspection                                                                                                                                                                                                                            |
| `fullDescription`      | Detailed description of the inspection                                                                                                                                                                                                                         |
| `defaultConfiguration` | The [`reportingConfiguration`](https://docs.oasis-open.org/sarif/sarif/v2.1.0/os/sarif-v2.1.0-os.html#_Toc34317852) object containing detailed information about the inspection, including its severity level and describing whether the inspection is enabled |
| `relationships`        | The relation of the inspection to other inspections, see [`taxa`](#sarif-taxa-object) for details                                                                                                                                                              |

### invocations

The `invocations` array contains a single element describing the %product%
[`invocation`](https://docs.oasis-open.org/sarif/sarif/v2.1.0/os/sarif-v2.1.0-os.html#_Toc34317567),
telling whether %product% ran successfully or not.

```json
{
  "invocations": [
    {
      "exitCode": 0,
      "toolExecutionNotifications": [
        {
          "message": {
            "text": "Reporting from [\"Java annotator\"] 'sanity' inspections was suspended due to high problems count."
          },
          "level": "error"
        }
      ],
      "executionSuccessful": true
    }
  ]
}
```

In the above example, Qodana execution was successful (`exitCode`, `executionSuccessful`). Despite the (technically)
successful execution, Qodana reported that its sanity inspections found some problems (`message`, `level=error`).
When the 'sanity' inspections fail, this typically means that the project configuration was broken.

The possible values for `exitCode` are:

| Value | Description                                                                                                  |
|-------|--------------------------------------------------------------------------------------------------------------|
| `0`   | Successful execution                                                                                         |
| `1`   | Any internal error                                                                                           |
| `137` | Out of memory, the Docker container for Qodana needs at least 6 GB of RAM                                    |
| `255` | Successful execution and exit resulted from the exceeded [`fail-threshold`](quality-gate.topic) property value |

Here is the description of the other fields from the `invocations` object:

The `toolExecutionNotifications` field contains notifications generated during a %product% run, such as a reached
[threshold](quality-gate.topic).

<note>
After the linter process has exited successfully,
the <code>results</code> folder contains the report file
and the process exit code is equal to the <code>exitCode</code> value in the report.

If the process was terminated abnormally,
the <code>results</code> folder may or may not contain the report file.
A typical exit code in such cases is <code>137</code> (SIGKILL, due to out of memory).
</note>

### versionControlProvenance

The `versionControlProvenance` array describes the version control systems that the project code was checked out from.
Each version control system is described by a
[`versionControlDetails`](https://docs.oasis-open.org/sarif/sarif/v2.1.0/os/sarif-v2.1.0-os.html#_Toc34317602) object.
If the project does not use a version control system, the whole `versionControlProvenance` is absent.

```json
{
  "versionControlProvenance": [
    {
      "repositoryUri": "https://github.com/example/example.git",
      "revisionId": "6c034f977505b058c7cf764b3d9b1abd068a725e",
      "branch": "master",
      "properties": {
        "repoUrl": "https://github.com/example/example.git",
        "lastAuthorName": "Jane Doe",
        "vcsType": "Git",
        "lastAuthorEmail": "mail@example.com",
        "tags": [
          "repoUrl",
          "lastAuthorEmail",
          "lastAuthorName",
          "vcsType"
        ]
      }
    }
  ]
}
```

Each `versionControlDetails` object contains the following fields:

| Field           | Description                      |
|-----------------|----------------------------------|
| `repositoryUri` | Repository checkout URL          |
| `revisionId`    | Latest commit hash               |
| `branch`        | Repository branch                |
| `properties`    | Additional properties, see below |

Additional properties are stored as a
[property bag](https://docs.oasis-open.org/sarif/sarif/v2.1.0/os/sarif-v2.1.0-os.html#_Toc34317448),
they contain information about the author of the last commit.
The `vcsType` property always has the value `Git`.

### results

The `results` array describes the problems detected during inspection.
Each problem detected by %product% is described by a separate
[`result`](https://docs.oasis-open.org/sarif/sarif/v2.1.0/os/sarif-v2.1.0-os.html#_Toc34317638) object.

```json
{
  "results": [
    {
      "ruleId": "InfiniteRecursion",
      "kind": "fail",
      "level": "warning",
      "message": {
        "text": "Method <code>visitTypeVariable()</code> recurses infinitely, and can only end by throwing an exception"
      },
      "locations": [
        ...
      ],
      "partialFingerprints": {
        "equalIndicator/v1": "ac5714b0b15b7e8c4311899afd1c2b44069865039f2a9d309dcab04eddd4681d"
      },
      "baselineState": "unchanged",
      "properties": {
        "ideaSeverity": "WARNING",
        "tags": [
          "ideaSeverity"
        ]
      }
    }
  ]
}
```

Each `result` object consists of the following fields:

| Field                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ruleId`              | The unique inspection ID (`inspectionId`)                                                                                                                                                                                                                                                                                                                                                                                                        |
| `kind`                | Always takes the `fail` value                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `level`               | The SARIF [severity level](#SARIF+severity)                                                                                                                                                                                                                                                                                                                                                                                                      |
| `message`             | A [`message`](https://docs.oasis-open.org/sarif/sarif/v2.1.0/os/sarif-v2.1.0-os.html#_Toc34317459) object with the nested `text` field containing the result/problem description in the format of an IntelliJ IDEA message string                                                                                                                                                                                                                |
| `locations`           | Array of the [`location`](https://docs.oasis-open.org/sarif/sarif/v2.1.0/os/sarif-v2.1.0-os.html#_Toc34317670) objects. Always contains a single element comprised of the [`physicalLocation`](#The+physicalLocation+object) and the [`logicalLocations`](#The+logicalLocations+object) objects                                                                                                                                                  |
| `partialFingerprints` | Contains hashes for comparing results between different runs. Used by the [baseline](baseline.topic) feature                                                                                                                                                                                                                                                                                                                                |
| `baselineState`       | <p>Indicates whether a linter was executed in baseline mode and can accept the following values:</p> <list><li>`new` denotes that the problem was detected only in the current run but not in the baseline run</li><li>`absent` denotes that the problem was detected only in the baseline run but not in the current run</li> <li>`unchanged` denotes that the problem was detected both in the current run and in the baseline run</li></list> |
| `properties`          | The `propertyBag` containing the `ideaSeverity` field with the original IntelliJ IDEA inspection severity as a value                                                                                                                                                                                                                                                                                                                             |

#### The location object

Each [`location`](https://docs.oasis-open.org/sarif/sarif/v2.1.0/os/sarif-v2.1.0-os.html#_Toc34317670) object
describes a concrete physical location in a file, augmented by a high-level logical location.

```json
{
  "physicalLocation": {
    "artifactLocation": {
      "uri": "asm-util/src/main/java/org/objectweb/asm/util/CheckSignatureAdapter.java",
      "uriBaseId": "SRCROOT"
    },
    "region": {
      "startLine": 259,
      "startColumn": 14,
      "charLength": 17,
      "snippet": {
        "text": "visitTypeVariable"
      },
      "sourceLanguage": "JAVA"
    },
    "contextRegion": {
      "startLine": 257,
      "startColumn": 1,
      "charOffset": 9764,
      "charLength": 152,
      "snippet": {
        "text": "\n  @Override\n  public void visitTypeVariable(final String name) {\n    visitTypeVariable(name);\n    if (type != TYPE_SIGNATURE || state != State.EMPTY) {"
      }
    }
  },
  "logicalLocations": [
    {
      "fullyQualifiedName": "root.asm-util.main",
      "kind": "module"
    }
  ]
}
```

#### The physicalLocation object

```json
{
  "physicalLocation": {
    "artifactLocation": {
      "uri": "asm-util/src/main/java/org/objectweb/asm/util/CheckSignatureAdapter.java",
      "uriBaseId": "SRCROOT"
    },
    "region": {
      "startLine": 259,
      "startColumn": 14,
      "charLength": 17,
      "snippet": {
        "text": "visitTypeVariable"
      },
      "sourceLanguage": "JAVA"
    },
    "contextRegion": {
      "startLine": 257,
      "startColumn": 1,
      "charOffset": 9764,
      "charLength": 152,
      "snippet": {
        "text": "\n  @Override\n  public void visitTypeVariable(final String name) {\n    visitTypeVariable(name);\n    if (type != TYPE_SIGNATURE || state != State.EMPTY) {"
      }
    }
  }
}
```

The `physicalLocation` object contains the following fields:

| Field              | Description                                                                                                                                                                                                                                                                                 |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `artifactLocation` | <p>The [`artifactLocation`](https://docs.oasis-open.org/sarif/sarif/v2.1.0/os/sarif-v2.1.0-os.html#_Toc34317427) object containing the following fields:</p> <list><li>`uri` denotes the path relative to the project root</li> <li>`uriBaseId` always has the `SRCROOT` value</li> </list> |
| `region`           | Contains information about the problem location and the snippet that should be highlighted. See the [section below](#The+region+object) for details                                                                                                                                         |
| `contextRegion`    | Contains information about the text that surrounds the snippet from the `region` field. This field is used for comparing problems in the [baseline](baseline.topic) mode                                                                                                               |

##### The region object

```json
{
  "region": {
    "startLine": 72,
    "startColumn": 23,
    "charOffset": 1852,
    "charLength": 11,
    "snippet": {
      "text": "options.php"
    },
    "sourceLanguage": "HTML"
  }
}
```

The [`region`](https://docs.oasis-open.org/sarif/sarif/v2.1.0/os/sarif-v2.1.0-os.html#_Toc34317685) object
contains the following fields:

| Field            | Description                                                                                                                                                                                              |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `startLine`      | The line number of the first character in the region. Starts with 1                                                                                                                                      |
| `startColumn`    | The column number of the first character in the region. Starts with 1, measured in UTF-16 code units                                                                                                     |
| `charOffset`     | The number of UTF-16 code units between the beginning of the file and the beginning of the region                                                                                                        |
| `charLength`     | The length of the region, measured in UTF-16 code units                                                                                                                                                  |
| `snippet`        | The [`artifactContent`](https://docs.oasis-open.org/sarif/sarif/v2.1.0/os/sarif-v2.1.0-os.html#_Toc34317422) object containing the `text` field with the value equal to the text of the specified region |
| `sourceLanguage` | Programming language of the inspected snippet. Used for highlighting in the user interface of %product%                                                                                                  |

#### The logicalLocations object

```json
{
  "logicalLocations": [
    {
      "fullyQualifiedName": "root.asm-util.main",
      "kind": "module"
    }
  ]
}
```

The `logicalLocations` object contains the following fields:

| Field                | Description                                            |
|----------------------|--------------------------------------------------------|
| `kind`               | Always takes the `module` value                        |
| `fullyQualifiedName` | The module name obtained from the project build system |

### automationDetails

The [`runAutomationDetails`](https://docs.oasis-open.org/sarif/sarif/v2.1.0/os/sarif-v2.1.0-os.html#_Toc34317523) object
provides details of the [`run`](#sarif-run-object) object.

```json
{
  "automationDetails": {
    "id": "project/qodana/2022-09-12",
    "guid": "bc9770e3-0cf4-4e46-a8fd-455e5bf116a2",
    "properties": {
      "jobUrl": "https://build.example.org/job/12345678",
      "tags": [
        "jobUrl"
      ]
    }
  }
}
```

The `automationDetails` object contains the following fields:

| Field        | Description                                                                                                          |
|--------------|----------------------------------------------------------------------------------------------------------------------|
| `id`         | User-readable string, unique per report                                                                              |
| `guid`       | Unique machine-readable report ID                                                                                    |
| `properties` | Additional information about the run, for %product%, it contains the URL of the CI/CD build that produced the report |

### newlineSequences

The [`newlineSequences`](https://docs.oasis-open.org/sarif/sarif/v2.1.0/os/sarif-v2.1.0-os.html#_Toc34317510) array
contains unique strings, each of which specifies a character sequence that %product% treated as a line break during a run.

```json
{
  "newlineSequences": [
    "\r\n",
    "\n"
  ]
}
```

### properties

In addition to the inspections configured in the inspection profile,
%product% runs a few extra inspections for sanity-checking the project configuration.
If these extra inspections find any problems, the project configuration is probably wrong.
The results of these extra inspections are recorded in the `qodana.sanity.results` property in the same format as the
regular [`result`](#results) objects.

```json
{
  "properties": {
    "qodana.sanity.results": [
      {
        "ruleId": "JavaAnnotator",
        "kind": "fail",
        "level": "error",
        "message": {
          "text": "Variable 'points' might not have been initialized",
          "markdown": "Variable 'points' might not have been initialized"
        },
        "locations": [
          {
            "physicalLocation": {
              "artifactLocation": {
                "uri": "core/src/main/java/com/google/zxing/datamatrix/detector/Detector.java",
                "uriBaseId": "SRCROOT"
              },
              "region": {
                "startLine": 52,
                "startColumn": 41,
                "charOffset": 1772,
                "charLength": 6,
                "snippet": {
                  "text": "points"
                },
                "sourceLanguage": "JAVA"
              },
              "contextRegion": {
                "startLine": 50,
                "startColumn": 1,
                "charOffset": 1670,
                "charLength": 180,
                "snippet": {
                  "text": "    ResultPoint[] cornerPoints = rectangleDetector.detect();\n\n    ResultPoint[] points = detectSolid2(points);\n    points[3] = correctTopRight(points);\n    if (points[3] == null) {"
                }
              }
            },
            "logicalLocations": [
              {
                "fullyQualifiedName": "core",
                "kind": "module"
              }
            ]
          }
        ],
        "partialFingerprints": {
          "equalIndicator/v1": "2bf8eae4ff0d22f23008fe342fb1cfc67aa4f6db9b276e16ba621c77e3fda618"
        },
        "properties": {
          "ideaSeverity": "ERROR"
        }
      }
    ]
  }
}
```

## SARIF severity

The [SARIF severity values](https://docs.oasis-open.org/sarif/sarif/v2.1.0/os/sarif-v2.1.0-os.html#_Toc34317648)
correspond to the severity values of IntelliJ IDEA according to this table:

<include src="lib_qd.xml" include-id="qodana-severity-levels" use-filter="for-report,empty"/>

The original IntelliJ IDEA inspection severity is stored in the `propertyBag` field of the same object.
