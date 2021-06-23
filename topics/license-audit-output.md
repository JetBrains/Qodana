[//]: # (title: License Audit Output Formats)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

## Basic output
{id="license-audit-basic-output"}

Full License Audit results are available in the file `report.json` located in the `results-dir` folder.

[//]: # "verify"

## Command-line output summary

An example of the Clone Finder command-line summary output:
``` shell
...
```
[//]: # "add"

## UI-compatible output
{id="license-audit-ui-output"}

In addition to programmatic output, you can generate a human-readable report in the HTML format by using the `--save-report` argument.
See [Open an HTML Report](html-report.md) for details.

```shell
...
```
[//]: # "add"

In addition to the sunburst diagram and other features of Qodana's [HTML report](ui-overview.md), ---

### 5 problem types (inspections)

### Analyze detected problems

### Follow up on detection results
{id="results-review"}

Find below a recommended course of action for each inspection type.

#### No dependency licenses
Try to find the dependency license, get legal advice, and
- Manually assign a license ID to this dependency in the configuration (dependencyOverride)

- Ignore: hide this warning by ignoring the dependency in the configuration (dependencyIgnores)
- Take action: remove the dependency | fix the dependency license file
- Report: License Audit has not found an existing dependency license


#### Unrecognized dependency license

Try to find the dependency license, get legal advice, and
- Manually assign a license ID to this dependency (dependencyOverride)

- Ignore: hide this warning by ignoring the dependency in the configuration (dependencyIgnores)
- Take action: remove the dependency | fix the dependency license file
- Report: License Audit has not recognized a valid dependency license

#### Uncategorized dependency license
Check the dependency license, get legal advice, and

- Manually add the license to the allowed list
  
- Ignore: hide this warning by ignoring the dependency in the configuration (dependencyIgnores)
- Take action: remove the dependency
- ----Report???

#### Unrecognized project license
- Specify in your project files explicitly which licenses you want to use

- Report: License Audit has not recognized an existing and valid project license

#### Prohibited dependency license
Check the dependency license, get legal advice, and

- Manually add the license to the allowed list: 

- Ignore: hide this warning by ignoring the dependency in the configuration (dependencyIgnores)
- Take action: remove the dependency
- Report: License Audit is mistaken that the reported dependency license is not compatible with the given project license

### View all third-party licenses


## Learn more

* How to open a generated report in your browser: [Open an HTML Report](html-report.md)

* Basic structure and configuration of Qodana HTML reports: [UI Overview](ui-overview.md)

* More information on command-line arguments for License Audit: [Docker Image Paths and Configuration Options](license-audit-docker-techs.md)

