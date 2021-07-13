[//]: # (title: Qodana Intellij Linter results in SARIF )

## Common description
SARIF result it's a json file with format specified in this [document](http://docs.oasis-open.org/sarif/sarif/v2.1.0/sarif-v2.1.0.html)

Qodana implementation follows format rules, but also specifies several custom properties written in [propertyBag](https://docs.oasis-open.org/sarif/sarif/v2.1.0/os/sarif-v2.1.0-os.html#_Toc34317448).
## Example of report
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
Report file always contain one [Run](https://docs.oasis-open.org/sarif/sarif/v2.1.0/os/sarif-v2.1.0-os.html#_Toc34317484) object.
This object always contains sections:

### invocations
List of [Invocation object](https://docs.oasis-open.org/sarif/sarif/v2.1.0/csprd01/sarif-v2.1.0-csprd01.html#_Toc10541005).
Always contain single invocation object. Invocation contains:
- _exitCode_ - tool exit code
    - __0__ - success execution 
    - __1__ - any internal error
    - __255__ - success execution but exit code is not zero cause of _failThreshold_ property
- _executionSuccessful_ - if _exitCode_ is 0 or 255
- _exitCodeDescription_ - description of exit code for nonzero values

_Note:_
If linter process were finished by itself then result folder should contain report file and process exit code should be 
equal to _exitCode_ in report. If process were terminated from outside the report could be absent 
and process exit code could differ from codes above. Typical code 137. 

### automationDetails
[AutomationDetails object](https://docs.oasis-open.org/sarif/sarif/v2.1.0/os/sarif-v2.1.0-os.html#_Toc34317523) 
Object contains:
 - _guid_ unique report id
 - _id_ user defined string, should be unique for the report

### versionControlProvenance
List of [VersionControlDetails objects](https://docs.oasis-open.org/sarif/sarif/v2.1.0/os/sarif-v2.1.0-os.html#_Toc34317602)
Contains zero or one object corresponding to vcs repository in project root. Current supported vcs list: Git.
Object contains:
- _repositoryUri_ - repo checkout url
- _revisionId_ - last commit hash
- _branch_ - current repo branch
- _properties_ - propertyBag with "vcsType" field. _vcsType_ - Git/Hg/Svn.

### tool
[Tool object](https://docs.oasis-open.org/sarif/sarif/v2.1.0/os/sarif-v2.1.0-os.html#_Toc34317529) contains description of qodana image, bundled plugins and inspections in them.

### results
List of [Result object](https://docs.oasis-open.org/sarif/sarif/v2.1.0/csprd01/sarif-v2.1.0-csprd01.html#_Toc10541076)

## Tool object
### Tool example
```json
{
  "driver": {
    "name": "Qodana Intellij Linter",
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
- _driver_ - [ToolComponent object](https://docs.oasis-open.org/sarif/sarif/v2.1.0/csprd01/sarif-v2.1.0-csprd01.html#_Toc10540971).
Object describes Qodana Intellij Linter tool.
- _extensions_ - List of [ToolComponent objects](https://docs.oasis-open.org/sarif/sarif/v2.1.0/csprd01/sarif-v2.1.0-csprd01.html#_Toc10540971).
Each element of list corresponds to Intellij IDEA plugin used for this run.

### ToolComponent structure
Object contains:
- _name_ - pluginId for Intellij IDEA plugin, "Qodana Intellij Linter" for driver
- _version_ - plugin version Intellij IDEA plugin, tool version for driver
- _rules_ - list of [ReportingDescriptor objects](https://docs.oasis-open.org/sarif/sarif/v2.1.0/csprd01/sarif-v2.1.0-csprd01.html#_Toc10541274)

### ReportingDescriptor structure
Object contains:
- _id_ - inspectionId - short name of inspection.
- _shortDescription_ - [MultiformatMessageString object]. Contains field "text" with name of inspection as value.
- _fullDescription_ - [MultiformatMessageString object]. Contains field "text" with description of inspection as value. Description string has html format.
- _defaultConfiguration_ - [ReportingConfiguration object](https://docs.oasis-open.org/sarif/sarif/v2.1.0/csprd01/sarif-v2.1.0-csprd01.html#_Toc10541290).
Configuration of inspection used by default.

### ReportingConfiguration structure
Object contains:
- _enabled_ - true/false.
- _level_ - [SARIF severity level](#SARIF severity) of rule

## SARIF severity
SARIF severity values could be one of the strings:
- __error__ - if IDEA inspection severity was "ERROR"
- __warning__ - if IDEA inspection severity was "WARNING"
- __note__ - in any other case
 
Origin IDEA inspection severity is stored in same object "propertyBag" field.

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
- _ruleId_ - inspection short name(inspectionId), unique inspection identifier
- _kind_ - always "fail"
- _level_ - [SARIF severity level](#SARIF severity)
- _message_ - object of type [Message](https://docs.oasis-open.org/sarif/sarif/v2.1.0/csprd01/sarif-v2.1.0-csprd01.html#_Toc10540897) with single field "text".
"text" contains result/problem description in format of IDEA message string.
- _partialFingerprints_ - technical field contains hashes for comparing results between different runs. Used in baseline feature.
- _baselineState_ - this field only appeared if linter was executed in baseline mode. Could take values:
    - __new__ - problems was absent in baseline report but exists in current
    - __absent__ - problems is absent in current report but absent in current
    - __unchanged__ - same problem appears in both reports
- _properties_ - propertyBag with "ideaSeverity" field with origin IDEA severity as value.
- locations - list of [Location objects](https://docs.oasis-open.org/sarif/sarif/v2.1.0/csprd01/sarif-v2.1.0-csprd01.html#_Toc10541108). Always contains single element.

### Location structure 
- _logicalLocations_ - list of [LogicalLocation](https://docs.oasis-open.org/sarif/sarif/v2.1.0/csprd01/sarif-v2.1.0-csprd01.html#_Toc10541157). 
Consist zero or one element corresponding to module in which result appears. Module is a gradle subproject, maven module, etc... 
- _physicalLocation_ - [PhysicalLocation object](https://docs.oasis-open.org/sarif/sarif/v2.1.0/csprd01/sarif-v2.1.0-csprd01.html#_Toc10541116). Could be absent.

###LogicalLocation Structure 
Object contains:
- _kind_ - always "module"
- _fullyQualifiedName_ - module name, obtained from project build system

### PhysicalLocation structure
Object consists:
- _artifactLocation_ - [ArtifactLocation object](https://docs.oasis-open.org/sarif/sarif/v2.1.0/csprd01/sarif-v2.1.0-csprd01.html#_Toc10540865)
Object contains:
    - _uri_ - relative path based on project root path
    - _uriBaseId_ - always have value "SRCROOT"
- _region_ - [Region object](https://docs.oasis-open.org/sarif/sarif/v2.1.0/csprd01/sarif-v2.1.0-csprd01.html#_Toc10541123).
Part of artifact location containing text which should be highlighted as a reason of current result.
- _contextRegion_ - [Region object](https://docs.oasis-open.org/sarif/sarif/v2.1.0/csprd01/sarif-v2.1.0-csprd01.html#_Toc10541123).
Part of artifact location surrounding _region_. Typically, two rows above and under _region_. Used for problems comparisons in baseline.

### Region structure
Object contains:
- _startLine_ - the one-based line number of the first character in the region. 
- _startColumn_ - the one-based column number of the first character in the region.
- _charOffset_ - the zero-based character offset of the first character in the region from the beginning of the artifact
- _charLength_ - region length in characters
- _snippet_ - [ArtifactContent object](https://docs.oasis-open.org/sarif/sarif/v2.1.0/csprd01/sarif-v2.1.0-csprd01.html#_Toc10540860)
Object contains field "text" with value equals to extracted from artifact text of specified region.
