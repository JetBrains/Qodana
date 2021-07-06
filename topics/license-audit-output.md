[//]: # (title: License Audit Output Formats)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

## Basic output
{id="license-audit-basic-output"}

Full License Audit results are available in the file `report.json` located in the `results-dir` folder.

## Command-line output summary

An example of the License Audit command-line summary output:
``` shell
1/4 Gathering project metadata...
┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┓
┃ Dependency Type    ┃ Count ┃
┡━━━━━━━━━━━━━━━━━━━━╇━━━━━━━┩
│ gradle             │  39   │
└────────────────────┴───────┘
2/4 Obtaining licenses for 39 dependencies...
┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┓
┃ License Type       ┃ Count ┃
┡━━━━━━━━━━━━━━━━━━━━╇━━━━━━━┩
│ Permissive         │  26   │
│ Unstated License   │   2   │
│ Copyleft           │   2   │
│ Public Domain      │   3   │
│ Copyleft Limited   │   1   │
└────────────────────┴───────┘
3/4 Checking project with licenses (Apache-2.0) and dependencies for problems...
┏━━━━━━━━━━━━━━━━━━━━┳━━━━━━━┓
┃ Problem Type       ┃ Count ┃
┡━━━━━━━━━━━━━━━━━━━━╇━━━━━━━┩
│ Unrecognized       │   3   │
│ dependency license │       │
│ Prohibited         │   2   │
│ dependency license │       │
│ No dependency      │   4   │
│ licenses           │       │
│ Uncategorized      │   4   │
│ dependency license │       │
└────────────────────┴───────┘
✨   Done!
```

## UI-compatible output
{id="clone-finder-ui-output"}

In addition to programmatic output, you can generate a human-readable report in the HTML format by using the `--save-report` argument.
See [Open an HTML Report](html-report.md) for details.

```shell
├── asset-manifest.json  // UI
├── index.html // UI
├── preview.html // UI
├── results
│   ├── License_Audit
│   │   ├── licenseRules.json  // License rules based on project qodana.yaml
│   │   ├── licenseTexts.md  // All dependency licenses texts
│   │   └── projectMetadata.json  // Project and dependency licenses metadata
│   ├── descriptions
│   │   └── License_Audit.json
│   ├── metaInformation.json  // Found problems metadata
│   ├── projectStructure
│   │   └── Code_Inspection.json  // Inspection description
│   ├── qodana.yaml  // Project's qodana.yaml 
│   └── result-allProblems.json  // All found problems
└── versions // UI
```

License Audit extends the [Qodana UI](ui-overview.md) features to make license analysis more helpful and convenient.

1. A sunburst diagram offers a quick overview of the problems detected.
2. From the diagram, you can navigate to a complete list of detected problems.
3. Project audit window provides a view of project license, dependency licenses, and the current allowed/prohibited licenses configuration.

[//]: # "TODO discuss"

### 5 problem types (inspections)

### Analyze detected problems

### Follow up on detection results
{id="results-review"}

Find below a recommended course of action for each inspection type. 

<note>

- To override detection results, add the recommended settings to  [`qodana.yaml`](qodana-yaml.md#License+Audit+configuration) and save the configuration file to the root of the analyzed project.

- To report a problem, go to **More actions | Report** at the bottom of the problem card.

</note>

#### No dependency licenses
Try to find the dependency license, get legal advice, and
- Manually assign an [SPDX license ID](https://spdx.org/licenses/) to this dependency in the configuration, for example:

```yaml
    inspections:
     LicenseAudit:
       dependencyOverrides:
           - name: "numpy"
             version: "1.19.1"
             licenses:
               - "BSD-3-Clause"
```

- Ignore: hide this warning by ignoring the dependency licenses in the configuration 

```yaml
    inspections:
      LicenseAudit:
        dependencyIgnores:
          - name: "enry"
            licenses:
              - "NONE"
```

- Take action: remove the dependency
- Disable the check: do it in [the Checks window](ui-overview.md#Adjust+your+inspection+profile)
- Report: License Audit has not found an existing dependency license


#### Unrecognized dependency license

Try to find the dependency license, get legal advice, and
- Manually assign an [SPDX license ID](https://spdx.org/licenses/) to this dependency in the configuration, for example:

```yaml
    inspections:
     LicenseAudit:
       dependencyOverrides:
           - name: "numpy"
             version: "1.19.1"
             licenses:
               - "BSD-3-Clause"
```

- Ignore: hide this warning by ignoring the dependency licenses in the configuration, for example:

```yaml
    inspections:
      LicenseAudit:
        dependencyIgnores:
          - name: "enry"
            licenses:
              - "UNKNOWN"
```
- Take action: remove the dependency
- Disable the check: do it in the [Checks window](ui-overview.md#Adjust+your+inspection+profile)
- Report: License Audit has not recognized a valid dependency license

#### Uncategorized dependency license
Check the dependency license, get legal advice, and

- Manually add the [SPDX license ID](https://spdx.org/licenses/) to the allowed list, for example:

```yaml
    inspections:
      LicenseAudit:
        rules:
          - key:
              - "PROPRIETARY-LICENSE"
              - "MIT"
            allowed:
              - "ISC"
```
  
- Ignore: hide this warning by ignoring the dependency licenses in the configuration, for example: 

```yaml
    inspections:
      LicenseAudit:
        dependencyIgnores:
          - name: "numpy"
            licenses:
              - "GPL-3.0-only"
```
  
- Take action: remove the dependency
- Disable the check: do it in the [Checks window](ui-overview.md#Adjust+your+inspection+profile)
- Report: License Audit should list the reported dependency license as compatible with the given project license (reasons why)

#### Unrecognized project license
- Specify in your project files explicitly which licenses you want to use – add a LICENSE file. 
- Disable the check: do it in the [Checks window](ui-overview.md#Adjust+your+inspection+profile)
- Report: License Audit has not recognized an existing and valid project license

#### No project licenses
- Specify in your project files explicitly which licenses you want to use – add a LICENSE file.
- Disable the check: do it in the [Checks window](ui-overview.md#Adjust+your+inspection+profile)
- Report: License Audit has not recognized an existing and valid project license

#### Prohibited dependency license
Check the dependency license, get legal advice, and

- Manually add the license to the allowed list, for example: 

```yaml
    inspections:
      LicenseAudit:
        rules:
          - key:
              - "PROPRIETARY-LICENSE"
              - "MIT"
            allowed:
              - "ISC"
```

- Ignore: hide this warning by ignoring the dependency licenses in the configuration, for example:

```yaml
    inspections:
      LicenseAudit:
        dependencyIgnores:
          - name: "numpy"
            licenses:
              - "GPL-3.0-only"
```

- Take action: remove the dependency
- Disable the check: do it in the [Checks window](ui-overview.md#Adjust+your+inspection+profile)
- Report: License Audit is mistaken that the reported dependency license is not compatible with the given project license

### Save and share the results

1. In your report, open the Project audit window and go to the **Third-party licenses** tab.
2. Click the downward arrow to the right of the search field and select the necessary output format:
    * HTML
    * CSV
    * JSON

## Learn more

* How to open a generated report in your browser: [Open an HTML Report](html-report.md)

* Basic structure and configuration of Qodana HTML reports: [UI Overview](ui-overview.md)

* More information on command-line arguments for License Audit: [Docker Image Paths and Configuration Options](license-audit-docker-techs.md)

