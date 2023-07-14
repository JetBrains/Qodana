[//]: # (title: Code coverage)

**Code coverage** supports processing test code coverage for a range of languages and coverage engines:

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
            <p><menupath>IntelliJ Coverage Agent</menupath> (default and preferred) supports the formats:</p>
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

Àll inspections from this table are already integrated into the `qodana.recommended` and `qodana.starter` 
[profiles](inspection-profiles.md#Default+profiles).

This feature is available under the Ultimate and Ultimate Plus [licenses](pricing.md) and their trial versions, and 
supported by the IntelliJ IDEA, WebStorm, and PhpStorm IDEs starting from version 2023.2.

## How it works

Inspections will identify issues if the coverage of a method, class, or file (excluding Java and Kotlin) falls below a 
predefined threshold (set at 50% by default). The resulting coverage will be calculated and displayed in both the 
Command Line Interface (CLI) output and the User Interface (UI).

The IDEs display the detailed coverage information for the opened coverage reports. This feature is active once the 
IDE downloads the computed coverage report from Qodana Cloud and applies highlighting to 
covered/uncovered lines. Users can also open the Coverage view for more detailed statistics.

### Fresh code

When working on a Pull Request (PR), the code is considered to be fresh if being incorporated into the codebase using 
the PR's merge. All added and modified code lines are considered. A distinct 
coverage value will be calculated for these lines and displayed in the output. To utilize this mode, configure the PR-mode or
use it as a default mode while using, for example, [GitHub Actions](github.md). However, this cannot generate coverage 
issues for missing coverage in methods, classes, and files.

## Run Code coverage

<note>
For each language and engine invoked, only one coverage engine and one coverage format can be used at a time.
</note>

You can run Code coverage using the available options:

<tabs>
    <tab title="Docker" id="code-coverage-docker">
        <p>Map the directory containing all coverage files to the `/data/coverage` directory:</p>
        <code style="block" lang="shell" prompt="$">
            docker run \
               -v /my/folder/with/coverage:/data/coverage \
               jetbrains/qodana-&lt;linter&gt;
        </code>
    </tab>
    <tab title="Pipeline" id="code-coverage-pipeline">
        <p>Create a pipeline where all the output files from the coverage tool will be stored in the 
<code>.qodana/code-coverage</code> directory located in the root folder of the analyzed project. You can find examples of such 
pipelines on our <a href="https://github.com/qodana/qodana-coverage">GitHub</a> repository.</p>
    </tab>
</tabs>
