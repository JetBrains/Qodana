[//]: # (title: Code coverage)

**Code coverage** processes test code coverage for a range of languages and coverage engines:

<table>
    <tr>
        <td>Language</td>
        <td>Inspection name</td>
        <td>Code coverage agents</td>
    </tr>
    <tr>
        <td><a href="qodana-jvm.md">Java and Kotlin</a></td>
        <td><code>JvmCoverageInspection</code></td>
        <td>
            <p><menupath>IntelliJ Coverage Agent</menupath> is the default solution that supports the formats:</p>
            <list>
                <li>The default and preferred format is <code>ic</code></li>
                <li>The <code>xml</code> format is available as an alternative (please note, yet there is no support for obtaining this coverage data from the Qodana Cloud inside the IDE)</li>
            </list>
            <p><menupath>JaCoCo</menupath> supports the <code>xml</code> format (please note, there will be no support for obtaining this coverage data from the Qodana Cloud inside the IDE)</p>
        </td>
    </tr>
    <tr>
        <td><a href="qodana-js.md">JavaScript and TypeScript</a></td>
        <td><code>JsCoverageInspection</code></td>
        <td>
            <p><menupath>Jest/Mocha</menupath> supports the <code>lcov</code> format (please note that paths in the coverage file should be based on the project root when using this format)</p>
        </td>
    </tr>
    <tr>
        <td><a href="qodana-php.md">PHP</a></td>
        <td><code>PhpCoverageInspection</code></td>
        <td>
            <p><menupath>PhpUnit</menupath> supports the <code>xml</code> format</p>
        </td>
    </tr>
</table>

The `qodana.recommended` and `qodana.starter`[profiles](inspection-profiles.md#Default+profiles) 
support these inspections.

This feature is available in the Ultimate and Ultimate Plus [linters](pricing.md#pricing-linters-licenses) and their 
trial versions, and supported by the IntelliJ IDEA, WebStorm, and PhpStorm IDEs starting from version 2023.2 meaning that 
you can overview code coverage reports in the IDE.  

<tip>To overview code coverage reports in your IDE, create a Qodana Cloud <a href="cloud-projects.xml">project</a>.</tip>

## How it works

Code coverage identifies the issues connected with the coverage of a method, a class, or a file (except Java and Kotlin) 
falls below a predefined threshold currently set to be 50%. The resulting coverage is calculated and displayed in both the 
command line and user interfaces..

The IDEs display the detailed coverage information for the opened coverage reports. This feature is active once the 
IDE downloads the computed coverage report from Qodana Cloud and applies highlighting to 
covered/uncovered lines. Users can also open the Coverage view for more detailed statistics.

### Fresh code

<!-- This needs to be rephrased and simplified -->

When working on a Pull Request (PR), the code is considered to be fresh if being incorporated into the codebase using
the PR's merge. All added and modified code lines are considered. A distinct
coverage value will be calculated for these lines and displayed in the output. To utilize this mode, configure the PR-mode or
use it as a default mode while using, for example, [GitHub Actions](github.md). However, this cannot generate coverage
issues for missing coverage in methods, classes, and files.

## Prepare the project

<tip>You can find configuration examples on <a href="https://github.com/qodana/qodana-coverage/tree/main">GitHub</a>.</tip>

1. In Qodana Cloud, create a [project](cloud-projects.xml#cloud-manage-projects) that will be used for uploading your reports. 

2. Configure the test engine so that all files referred in a test coverage report would contain the relative paths 
inside the project. For example, if your codebase files are contained in the `src/` directory of the project repository,
then the path in code coverage reports should be `src/<file>`.

2. Run the test engine so that you have the test coverage report already generated and accessible by %product%. Because
%product% reads already generated reports, it should already be available for %product%.

## Run code coverage
{id="run-code-coverage"}

<note>
For each language and engine invoked, only one coverage engine and one coverage format can be used at a time.
</note>

You can run Code coverage using the available options:

<tabs>
    <tab title="Docker or Qodana CLI" id="code-coverage-docker">
        <p>Map the directory containing code coverage reports to the `/data/coverage` directory. </p>
        <p>Here is the example for Docker:</p>
        <code style="block" lang="shell" prompt="$">
            docker run \
               -v $(pwd):/data/project/ \
               -v /directory/with/coverage/report/:/data/coverage \
               -e QODANA_TOKEN="&lt;qodana-cloud-token&gt;" \
               jetbrains/qodana-&lt;linter&gt;
        </code>
        <p>This is the example of running Code coverage using 
        <a href="https://github.com/JetBrains/qodana-cli">Qodana CLI</a>:</p>
        <code style="block" lang="shell" prompt="$">
            qodana scan \
               -v /directory/with/coverage/report/:/data/coverage \
               -e QODANA_TOKEN="&lt;qodana-cloud-token&gt;" \
        </code>
    </tab>
    <tab title="Pipeline" id="code-coverage-pipeline">
        <p>Create a pipeline where all the output files from the coverage tool will be stored in the 
<code>.qodana/code-coverage</code> directory located in the root folder of the analyzed project. You can find 
configuration examples in our <a href="https://github.com/qodana/qodana-coverage">GitHub</a> repository.</p>
    </tab>
</tabs>

In the output, you can see the code coverage summary. You can also use your IDE to overview [code coverage](#overview-code-coverage-reports) results.

## Overview code coverage reports
{id="overview-code-coverage-reports"}

After you have performed all steps from the [](#Prepare+the+project) and [](#run-code-coverage) sections and your 
%product% report is now uploaded to Qodana Cloud, you can overview code coverage reports using your IDE as explained below.

<!-- The first and the second steps can be performed as a video -->

<procedure>
<step>If necessary, in your IDE log in and link your local project with Qodana Cloud.</step>
<step>Now you can overview code coverage results. Depending whether a specific line is covered, it is marked with a specific color.</step>

</procedure>

