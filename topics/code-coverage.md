[//]: # (title: Code coverage)

**Code coverage** processes test code coverage to identify the issues connected with the coverage of
a method, a class, or a file (except Java and Kotlin) and supported by several linters:

<!-- Is the inspection name information really useful in this case?-->
<!-- What does the default solution mean in this case? -->
<!-- Is the link to the IntelliJ IDEA code coverage solution correct? -->
<!-- The link to the Qodana report should be provided here -->

<table>
    <tr>
        <td>Linter</td>
        <td>Code coverage tool</td>
        <td>Supported report formats</td>
    </tr>
    <tr>
        <td rowspan="2"><a href="qodana-jvm.md"/></td>
        <td><a href="https://github.com/JetBrains/intellij-coverage">IntelliJ IDEA Code Coverage Agent</a></td>
        <td><code>IC</code> and <code>XML</code></td>
    </tr>
    <tr>
        <td><a href="https://www.jacoco.org/jacoco/">JaCoCo</a></td>
        <td><code>XML</code></td>
    </tr>
    <tr>
        <td><a href="qodana-js.md"/></td>
        <td><a href="https://jestjs.io/">Jest</a> and <a href="https://mochajs.org/">Mocha</a></td>
        <td><code>LCOV</code></td>
    </tr>
    <tr>
        <td><a href="qodana-php.md"/></td>
        <td><a href="https://phpunit.de/">PhpUnit</a></td>
        <td><code>XML</code></td>
    </tr>
</table>

This feature is available in the Ultimate and Ultimate Plus [linters](pricing.md#pricing-linters-licenses) and their 
trial versions.

## How it works

The predefined code coverage threshold in %product% is currently set to 50%.

Code coverage employs several inspections that are already included in the `qodana.recommended` and `qodana.starter` 
[default inspection profiles](inspection-profiles.md#Default+profiles):  

| Linter            | Inspection name          |
|-------------------|--------------------------|
| [](qodana-jvm.md) | `JvmCoverageInspection`  |
| [](qodana-js.md)  | `JsCoverageInspection`   |
| [](qodana-php.md) | `PhpCoverageInspection`  |

After inspecting, reports are available in [%product% reports](html-report.md) and [JetBrains IDEs](#overview-code-coverage-reports).

### Fresh code

<!-- This needs to be reviewed -->

When working on a Pull Request (PR), the code is considered to be fresh if being incorporated into the codebase using
the PR's merge. All added and modified code lines are considered. A distinct
coverage value will be calculated for these lines and displayed in the output. To utilize this mode, configure the PR-mode or
use it as a default mode while using, for example, [GitHub Actions](github.md). However, this cannot generate coverage
issues for missing coverage in methods, classes, and files.

## Prepare the project

<tip>You can find configuration examples on <a href="https://github.com/qodana/qodana-coverage/tree/main">GitHub</a>.</tip>

1. If necessary, in Qodana Cloud create a [project](cloud-projects.xml#cloud-manage-projects) that will be used for 
linking your project and storing your reports. 

2. Configure the code coverage tool. While configuring [Jest](https://jestjs.io/) or 
[Mocha](https://mochajs.org/), note that all files in coverage reports should contain the relative paths inside 
the project. For example, if your codebase files are contained in the `<project-root>/src/` directory, then 
file paths in code coverage reports should be `src/<file-name>`.

3. Generate the code coverage report and make it accessible by %product%.

## Run code coverage
{id="run-code-coverage"}

<note>
You can run only one test coverage solution at a time.
</note>

<tabs>
    <tab title="Docker or Qodana CLI" id="code-coverage-docker-cli">
        <p>Map the directory containing code coverage reports to the <code>/data/coverage</code> directory and
        the project token using the <code>QODANA_TOKEN</code> variable. Here are the Docker and 
        <a href="https://github.com/JetBrains/qodana-cli">Qodana CLI</a> command samples:</p>
        <tabs>
            <tab title="Docker" id="code-coverage-docker">
                <code style="block" lang="shell" prompt="$">
                    docker run \
                        -v $(pwd):/data/project/ \
                        -v /directory/with/coverage/report/:/data/coverage \
                        -e QODANA_TOKEN="&lt;qodana-cloud-token&gt;" \
                        jetbrains/qodana-&lt;linter&gt;
                </code>
            </tab>
            <tab title="Qodana CLI" id="code-coverage-cli">
                <code style="block" lang="shell" prompt="$">
                    qodana scan \
                       -v /directory/with/coverage/report/:/data/coverage \
                       -e QODANA_TOKEN="&lt;qodana-cloud-token&gt;"
                </code>
            </tab>
        </tabs>
    </tab>
    <tab title="GitHub Actions" id="code-coverage-pipeline">
        <p>Create a pipeline that will store all code coverage output files in the <code>&lt;project-root-dir&gt;/.qodana/code-coverage</code> 
directory. You can find 
configuration examples in our <a href="https://github.com/qodana/qodana-coverage">GitHub</a> repository.</p>
    </tab>
</tabs>

## Overview code coverage reports
{id="overview-code-coverage-reports"}

After you have [prepared the project](#Prepare+the+project) and [ran code coverage](#run-code-coverage), you can overview 
code coverage reports in [Qodana Cloud](#Qodana+Cloud) or using your [IDE](#IDE). 

### Qodana Cloud

You can find code coverage statistics in the upper-right corner of the [%product% report](html-report.md) UI. It also 
enumerates the inspections that were employed by the feature.

<img src="code-coverage-report-qodana.png" dark-src="code-coverage-report-qodana_dark.png" width="706" alt="Code coverage in Qodana Cloud" border-effect="line" animated="true"/>

### IDE

You can overview code coverage reports using IntelliJ IDEA, WebStorm, and PhpStorm IDEs starting from 
version 2023.2. 

<note>This feature is not available for XML-formatted reports generated by IntelliJ IDEA Code Coverage Agent and JaCoCo.</note>

#### Link your project with Qodana Cloud

To overview the report from Qodana Cloud, log in and link your project as described below.

<procedure>
<step>
<p>In your IDE, navigate to <menupath>Tools | Qodana | Log in to Qodana</menupath>.</p>
<img src="code-coverage-step-1.png" dark-src="code-coverage-step-1_dark.png" width="706" alt="The Log in to Qodana Cloud menu" border-effect="line"/>
</step>
<step><p>In the <menupath>Settings</menupath> dialog, click <menupath>Log in</menupath>.</p>
<img src="code-coverage-login-window.png" dark-src="code-coverage-login-window_dark.png" width="706" alt="The Settings window" border-effect="line"/>
<p>This will redirect you to the authentication page.</p>
</step>
<step>
    <p>In the <menupath>Settings</menupath> dialog, search for the project you would like to link with.</p>
<img src="code-coverage-login-linking-project.png" dark-src="code-coverage-login-linking-project_dark.png" width="706" alt="Linking with the project " border-effect="line"/>
</step>
</procedure>

#### Open a local coverage report

You can open a locally-based code coverage file in your IDE.

In your IDE, navigate to <menupath>Run | Show coverage data</menupath> and open the file containing the code coverage 
report. 

<img src="code-coverage-open-locally.png" dark-src="code-coverage-open-locally_dark.png" width="706" alt="The Choose Coverage Suite to Display dialog" border-effect="line"/>

In the <menupath>Coverage</menupath> tool window, you can overview the test coverage report. This report shows the 
percentage of the code that has been executed or covered by tests. 

<img src="code-coverage-coverage-window.png" dark-src="code-coverage-coverage-window_dark.png" width="706" alt="The Coverage tool window" border-effect="line" animated="true"/>

#### Overview the report

The IDE highlights the codebase test coverage using color marking. By default, the green color means
that a particular line was covered, and the red color means the uncovered line of code. 

<note>If you see that the code coverage results look incomplete, you probably need to reconfigure your
code coverage tool and generate a new code coverage report.</note>

<img src="code-coverage-report.png" dark-src="code-coverage-report_dark.png" width="706" alt="The coverage report overview" border-effect="line"/>

The report shows coverage for the lines implementing logic of a method, function, or a class. This excludes function, 
method, and class declaration from the report. For example, you cannot cover line 7 by tests, while line 8 is not covered.

<img src="code-coverage-report-coverage.png" dark-src="code-coverage-report-coverage_dark.png" width="706" alt="Code coverage for a specific method" border-effect="line"/>
