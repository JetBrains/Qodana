[//]: # (title: SARIF output)

Qodana produces the SARIF output contained in a JSON file formatted in accordance with the [SARIF specification](http://docs.oasis-open.org/sarif/sarif/v2.1.0/sarif-v2.1.0.html). The Qodana implementation follows the general format rules but also specifies several custom properties written in [propertyBag](https://docs.oasis-open.org/sarif/sarif/v2.1.0/os/sarif-v2.1.0-os.html#_Toc34317448).

## Report example

```json
{
  "version": "2.1.0",
  "runs": [
    {
      "tool": {
        ...
      },
      "invocations": [
        {
          "exitCode": 0,
          "executionSuccessful": true
        }
      ],
      "language": "en-US",
      "versionControlProvenance": [
        {
          "repositoryUri": "https://github.com/avafanasiev/gson",
          "revisionId": "a785a47b348265d0e8034f2611f737b1b865a334",
          "branch": "master",
          "properties": {
            "vcsType": "Git",
            "tags": [
              "vcsType"
            ]
          }
        }
      ],
      "results": [...],
      "automationDetails": {
        "id": "project - 7/10/21, 7:29 AM",
        "guid": "9a1a0587-1819-41f8-bdc6-3452268ae572"
      },
      "newlineSequences": [
        "\r\n",
        "\n"
      ]
    }
  ]
}
```

## Common structure

A report file always contains one [Run](https://docs.oasis-open.org/sarif/sarif/v2.1.0/os/sarif-v2.1.0-os.html#_Toc34317484) object.
This object always contains the following sections:

### Invocations

The list of [Invocation objects](https://docs.oasis-open.org/sarif/sarif/v2.1.0/csprd01/sarif-v2.1.0-csprd01.html#_Toc10541005), which always contains a single invocation object. An invocation comprises the following:
- `exitCode` -  tool exit code.
    - `0` - indicates successful execution.
    - `1` - indicates any internal error.
    - `255` - indicates successful execution, but the exit code is non-zero due to `failThreshold` property.
- `executionSuccessful` - if `exitCode` is `0` or `255`.
- `exitCodeDescription` - the description of the exit code for non-zero values.

<note>

If the linter processes were finished by themselves, then the `result` folder should contain the report file and the process exit code should equal to the `exitCode` in the report. Otherwise, if the processes were terminated externally, the report could be absent and the process exit code could differ from the codes above. A typical exit code in such cases is `137`.

</note>

### AutomationDetails

The [AutomationDetails](https://docs.oasis-open.org/sarif/sarif/v2.1.0/os/sarif-v2.1.0-os.html#_Toc34317523) object, which contains:
 - `guid` - a unique report ID.
 - `id` - a user-defined string, should be unique for the report.

### VersionControlProvenance
The list of [VersionControlDetails](https://docs.oasis-open.org/sarif/sarif/v2.1.0/os/sarif-v2.1.0-os.html#_Toc34317602) objects, which contains zero or one object corresponding to the vcs repository in project root. Currently supported VCS list: Git.

An object contains the following:
- `repositoryUri` - the repository checkout URL.
- `revisionId` - the last commit hash.
- `branch` - the current repository branch.
- `properties` - the `propertyBag` object with the `vcsType` field, which can be any of the following:
  - `Git`
  - `Hg`
  - `Svn`

### Tool

The [Tool](https://docs.oasis-open.org/sarif/sarif/v2.1.0/os/sarif-v2.1.0-os.html#_Toc34317529) object contains the description of the [Docker image](qodana-jvm-docker-readme.xml), bundled plugins and inspections in them.

### Results

The list of [Result](https://docs.oasis-open.org/sarif/sarif/v2.1.0/csprd01/sarif-v2.1.0-csprd01.html#_Toc10541076) objects.

## Tool object

### Tool example

```json
{
  "driver": {
    "name": "QDJVM",
    "rules": []
  },
  "extensions": [
    {
      "name": "org.intellij.intelliLang",
      "version": "213.1056",
      "rules": [
        {
          "id": "InjectionNotApplicable",
          "shortDescription": {
            "text": "Injection Annotation not applicable"
          },
          "fullDescription": {
            "text": "<html>\n<body>\nReports when a <code>@Language</code> annotation is applied to an element with a type other than <code>String</code> or <code>String[]</code>.\n<p><b>Example:</b></p>\n<pre><code>\n  @Language(\"HTML\") <b>int</b> i;\n</code></pre>\n<p>After the quick-fix is applied:</p>\n<pre><code>\n  <b>int</b> i;\n</code></pre>\n</body>\n</html>\n"
          },
          "defaultConfiguration": {
            "enabled": false,
            "level": "error",
            "parameters": {
              "ideaSeverity": "ERROR",
              "tags": [
                "ideaSeverity"
              ]
            }
          }
        }
      ]
    }
  ]
}
```

### Tool structure

- `driver` - [ToolComponent](https://docs.oasis-open.org/sarif/sarif/v2.1.0/csprd01/sarif-v2.1.0-csprd01.html#_Toc10540971) object describing the [Qodana linter](linters.md).
- `extensions` - the list of [ToolComponent](https://docs.oasis-open.org/sarif/sarif/v2.1.0/csprd01/sarif-v2.1.0-csprd01.html#_Toc10540971) objects.
Each element of the list corresponds to the Intellij IDEA plugin used for this run.

### ToolComponent structure

The object contains:
- `name` - the `pluginId` for an Intellij IDEA plugin, "Qodana Intellij Linter" for the driver.
- `version` - the plugin version for an Intellij IDEA plugin, the tool version for the driver.
- `rules` - the list of [ReportingDescriptor](https://docs.oasis-open.org/sarif/sarif/v2.1.0/csprd01/sarif-v2.1.0-csprd01.html#_Toc10541274) objects.

### ReportingDescriptor structure

The object contains:
- `id` - the `inspectionId`, that is, the short name of an inspection.
- `shortDescription` - [MultiformatMessageString object]. Contains the field `text` with the name of an inspection as a value.
- `fullDescription` - [MultiformatMessageString object]. Contains the field `text` with the description of an inspection as a value. The description string is provided in the HTML format.
- `defaultConfiguration` - [ReportingConfiguration](https://docs.oasis-open.org/sarif/sarif/v2.1.0/csprd01/sarif-v2.1.0-csprd01.html#_Toc10541290) object.
The configuration of an inspection used by default.

### ReportingConfiguration structure

The object contains:
- `enabled` - true/false.
- `level` - the [SARIF severity level](#SARIF+severity) of a rule.

## SARIF severity

The SARIF severity values could be one of the following strings:
- `error` - if the Intellij IDEA inspection severity is _"ERROR"_.
- `warning` - if the Intellij IDEA inspection severity is _"WARNING"_.
- `note` - in any other case.
 
The original Intellij IDEA inspection severity is stored in the same object's `propertyBag` field.

## Result object

### Result example

```json
{
  "ruleId": "InfiniteRecursion",
  "kind": "fail",
  "level": "warning",
  "message": {
    "text": "Method <code>visitTypeVariable()</code> recurses infinitely, and can only end by throwing an exception"
  },
  "locations": [
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
```

### Result structure

- `ruleId` - the inspection short name (`inspectionId`), which is a unique inspection identifier.
- `kind` - always "fail".
- `level` - [SARIF severity level](#SARIF+severity).
- `message` - an object of type [Message](https://docs.oasis-open.org/sarif/sarif/v2.1.0/csprd01/sarif-v2.1.0-csprd01.html#_Toc10540897) with a single field `text`, which contains the result/problem description in the format of an Intellij IDEA message string.
- `partialFingerprints` - a technical field contains hashes for comparing results between different runs. Used in the _baseline_ feature.
- `baselineState` - the field only appears if a linter was executed in baseline mode and can be any of the following:
  - `new`: The problem was detected only in the current run but not in the baseline run.
  - `absent`: The problem was detected only in the baseline run but not in the current run.
  - `unchanged`: The problem was detected both in the current run and in the baseline run.
- `properties` - a `propertyBag` with the `ideaSeverity` field with the original Intellij IDEA inspection severity as a value.
- `locations` - the list of [Location](https://docs.oasis-open.org/sarif/sarif/v2.1.0/csprd01/sarif-v2.1.0-csprd01.html#_Toc10541108) objects. Always contains a single element.

### Location structure 

The object contains:
- `logicalLocations` - the list of [LogicalLocation](https://docs.oasis-open.org/sarif/sarif/v2.1.0/csprd01/sarif-v2.1.0-csprd01.html#_Toc10541157) objects, which contains zero or one element corresponding to the module in which the result appears. A module can be a Gradle subproject, Maven module, and so on. 
- `physicalLocation` - the [PhysicalLocation](https://docs.oasis-open.org/sarif/sarif/v2.1.0/csprd01/sarif-v2.1.0-csprd01.html#_Toc10541116) object. Could be absent.

### LogicalLocation Structure 

The object contains:
- `kind` - always "module".
- `fullyQualifiedName` - the module name obtained from the project build system.

### PhysicalLocation structure

The object contains:
- `artifactLocation` - [ArtifactLocation](https://docs.oasis-open.org/sarif/sarif/v2.1.0/csprd01/sarif-v2.1.0-csprd01.html#_Toc10540865) object, which contains the following:
    - `uri` - the path relative to the project root.
    - `uriBaseId` - always has the value _"SRCROOT"_.
- `region` - [Region](https://docs.oasis-open.org/sarif/sarif/v2.1.0/csprd01/sarif-v2.1.0-csprd01.html#_Toc10541123) object, which is a part of the artifact's location containing the text that should be highlighted as a reason of the current result.
- `contextRegion` - the [Region](https://docs.oasis-open.org/sarif/sarif/v2.1.0/csprd01/sarif-v2.1.0-csprd01.html#_Toc10541123) object, which is a part of the artifact location's surrounding _region_. Typically, two rows above and under _region_. Used for problems comparisons in baseline.

### Region structure

The object contains:
- `startLine` - the one-based line number of the first character in the region. 
- `startColumn` - the one-based column number of the first character in the region.
- `charOffset` - the zero-based character offset of the first character in the region from the beginning of the artifact.
- `charLength` - region length in characters.
- `snippet` - [ArtifactContent](https://docs.oasis-open.org/sarif/sarif/v2.1.0/csprd01/sarif-v2.1.0-csprd01.html#_Toc10540860) object, which contains the field `text` with the value equal to the text of the specified region extracted from the artifact.
