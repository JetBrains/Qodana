[//]: # (title: Code coverage)

**Code coverage** uses generated reports to calculate the overall code coverage inside a method, a class, and a file. 
It also reports on the issues connected with the missing coverage in these entities.

This feature is available under the Ultimate and Ultimate Plus [licenses](pricing.md#pricing-linters-licenses) in the 
following linters:

<table>
    <tr>
        <td>Linter</td>
        <td>Code coverage tool</td>
        <td>Supported report formats</td>
    </tr>
    <tr>
        <td rowspan="2"><a href="qodana-jvm.md"/></td>
        <td><a href="https://github.com/JetBrains/intellij-coverage">IntelliJ IDEA Code Coverage Agent</a> is the recommended tool</td>
        <td><code>ic</code> is the preferable format. <code>XML</code> is also supported.</td>
    </tr>
    <tr>
        <td><a href="https://www.jacoco.org/jacoco/">JaCoCo</a></td>
        <td><code>xml</code></td>
    </tr>
    <tr>
        <td><a href="qodana-js.md"/></td>
        <td><a href="https://jestjs.io/">Jest</a></td>
        <td><code>lcov</code></td>
    </tr>
    <tr>
        <td><a href="qodana-php.md"/></td>
        <td><a href="https://phpunit.de/">PhpUnit</a></td>
        <td><code>xml</code></td>
    </tr>
    <tr>
        <td><a href="qodana-dotnet.md"/></td>
        <td><a href="https://www.nuget.org/packages/coverlet.msbuild">coverlet.msbuild</a></td>
        <td><code>lcov</code></td>
    </tr>
    <tr>
        <td><a href="qodana-python.md"/></td>
        <td><a href="https://coverage.readthedocs.io/en/7.3.2/">Coverage.py</a></td>
        <td><code>xml</code></td>
    </tr>
    <tr>
        <td><a href="qodana-go.md"/></td>
        <td><code>go test</code></td>
        <td><code>out</code></td>
    </tr>
</table>

<note>Code coverage for files is available only in <a href="qodana-js.md"/>, <a href="qodana-php.md"/>, and
<a href="qodana-python.md"/> linters.</note>

## How it works

For the missing code coverage issues, the predefined threshold in %product% is currently set to 50%.

Code coverage employs several inspections that are already included in the `qodana.recommended` and `qodana.starter` 
[default inspection profiles](inspection-profiles.md#Default+profiles), so you do not need to enable them:  

<!-- Do I need to enable any inspections in case of .NET -->

| Linter               | Employed inspection                                                                                |
|----------------------|----------------------------------------------------------------------------------------------------|
| [](qodana-jvm.md)    | [`JvmCoverageInspection`](https://www.jetbrains.com/help/inspectopedia/JvmCoverageInspection.html) |
| [](qodana-js.md)     | [`JsCoverageInspection`](https://www.jetbrains.com/help/inspectopedia/JsCoverageInspection.html)   |
| [](qodana-php.md)    | [`PhpCoverageInspection`](https://www.jetbrains.com/help/inspectopedia/PhpCoverageInspection.html) |
| [](qodana-python.md) | [`PyCoverageInspection`](https://www.jetbrains.com/help/inspectopedia/PyCoverageInspection.html)                                                                         |
| [](qodana-go.md)     | [`GoCoverageInspection`](https://www.jetbrains.com/help/inspectopedia/GoCoverageInspection.html)   |
| [](qodana-dotnet.md) | `NetCoverageInspection`                                                                            |

Once the inspection is complete, reports are available in [%product% reports](html-report.md) and JetBrains IDEs.

### Code coverage calculation

%product% calculates a code coverage based on the number of code lines containing logic with function, method, and class statements
being ignored. Here is the snippet containing comments on how it works: 

```javascript
function divide(a, b) { // Not analyzed by the code coverage
  return a / b; // Analyzed by the code coverage
}
module.exports = divide; // Analyzed by the code coverage
```

## Prepare the project

<tip>You can find configuration examples on <a href="https://github.com/qodana/qodana-coverage/tree/main">GitHub</a>.</tip>

1. Configure a code coverage tool. While configuring [Jest](https://jestjs.io/), note that all files in coverage reports 
should have the relative paths inside the project. For example, if your codebase files are contained in the 
`<project-root>/src/` directory, then file paths in code coverage reports should be `src/<file-name>`.

2. If you run %product% [locally](Quick-start.xml), use your code coverage tool to generate a code coverage report. 
Save the report to the directory where %product% can read it. If you run %product% in your [GitHub](github.md) pipeline, configure the workflow as shown in the [](#run-code-coverage) section.

For the [](qodana-dotnet.md) linter, configure <a href="https://www.nuget.org/packages/coverlet.msbuild">coverlet.msbuild</a> for the test project.

## Run the code coverage
{id="run-code-coverage"}

<note>
You can run %product% over a single test coverage report generated by a single code coverage tool at a time.
</note>

To learn about running code coverage using the [](qodana-dotnet.md) linter, skip to the 
[](#code-coverage-qodana-for-dotnet) section of this page.

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
        <p>Create the pipeline that will store all code coverage output files in the <code>&lt;project-root-dir&gt;/.qodana/code-coverage</code> 
        directory. You can find various examples of the GitHub Actions configurations on the 
<a href="https://github.com/qodana/qodana-coverage/tree/7360c03be1f44a4ed0e591218977005b07dd569e/.github/workflows">GitHub</a> website.</p>

Below is the pipeline configuration example for the [](qodana-js.md) linter:

```yaml
name: JavaScript - Jest Test

on:
  workflow_dispatch:
  pull_request:
  push:
    branches:
      - main
      - 'releases/*'

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Code
      uses: actions/checkout@v3
      with:
        ref: ${{ github.event.pull_request.head.sha }}
        fetch-depth: 0

    - name: Use Node.js 18.x
      uses: actions/setup-node@v2
      with:
        node-version: 18.x

    - name: Install dependencies
      run: npm ci
      working-directory: JS/jest

    - name: Run tests
      run: npm test
      working-directory: JS/jest
      
    - name: Archive coverage data # Archive data for using by Qodana
      uses: actions/upload-artifact@v2
      with:
        name: jest-coverage-data
        path: JS/jest/.qodana/code-coverage

    - name: Qodana Scan # Run Qodana
      uses: JetBrains/qodana-action@main
      env:
        QODANA_TOKEN: ${{ secrets.QODANA_TOKEN_JS }}
      with:
        args: "-i,JS/jest,--linter,jetbrains/qodana-js:2023.3-eap"
        pr-mode: false
```
</tab>

<tab title="GitLab CI/CD" id="code-coverage-gitlab">
<p>Create a <a href="gitlab.md">GitLab CI/CD</a> pipeline that will store all code coverage output files in the <code>&lt;project-root-dir&gt;/coverage</code> 
directory:</p>
        <code style="block" lang="yaml">
        qodana:
           image:
              name: jetbrains/qodana-&lt;linter&gt;
              entrypoint: [""]
           cache:
              - key: qodana-2023.3-$CI_DEFAULT_BRANCH-$CI_COMMIT_REF_SLUG
                fallback_keys:
                   - qodana-2023.3-$CI_DEFAULT_BRANCH-
                   - qodana-2023.3-
                paths:
                   - .qodana/cache
           variables:
              QODANA_TOKEN: $qodana_token           -
           script:
              - qodana --save-report 
              --results-dir=$CI_PROJECT_DIR/.qodana/results 
              --coverage-dir=$CI_PROJECT_DIR/coverage
           artifacts:
              paths:
                 - .qodana/results/report
              expose_as: 'Qodana report'
        </code>
        <p>
            This uses the <code>QODANA_TOKEN</code> variable to contain the <a href="project-token.md">project token</a>.
            The <code>--coverage-dir=$CI_PROJECT_DIR/coverage</code> in the <code>script</code> block runs %product% with the
            code coverage directory. 
        </p>
</tab>
</tabs>

### Qodana for .NET
{id="code-coverage-qodana-for-dotnet"}

Here is an example of the [`qodana.yaml`](qodana-yaml.md) file configuration for the [](qodana-dotnet.md) linter:

```yaml
dotnet:
  solution: <your-solution-file>

bootstrap: dotnet build, cd <path-to-dir-with-test-project-file> && \\
  dotnet add package coverlet.msbuild && \\
  ((dotnet test /p:CollectCoverage=true /p:CoverletOutput=<your-project-folder>/.qodana/code-coverage /p:CoverletOutputFormat=lcov))
```

Here, the `dotnet` option configures the solution file. 

The [`bootstrap`](before-running-qodana.md) command performs several steps before running %product% and explained in the table:

| Command step                                                    | Description                                                                                   |
|-----------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| `dotnet build`                                                  | Build a project or a solution                                                                 |
| `cd <path-to-dir-with-test-project-file>`                       | Navigate to the directory containing the project test file                                    |
| `dotnet add package coverlet.msbuild`                           | Add the `coverlet.msbuild` package to the project. This command needs to be repeated for each |
| `dotnet test ... `                                              | Execute tests in the project, and:                                                            |
| `/p:CollectCoverage=true`                                       | Enable code coverage                                                                          |
| `/p:CoverletOutput=<your-project-folder>/.qodana/code-coverage` | Collect code coverage results to a specific directory                                         |
| `/p:CoverletOutputFormat=lcov`                                  | Specify the code coverage output format                                                       |

Code coverage inspection results for the [](qodana-dotnet.md) linter are available in [](#Qodana+Cloud).

### Fresh code

Fresh code is the code contained in a GitHub pull request. %product% can calculate fresh code coverage and display the results. 

<note>While working with fresh code, %product% cannot analyze coverage issues for missing coverage in methods, classes, and files.</note>

To enable the fresh code feature, in your [GitHub](github.md) workflow configure the PR-mode. Here is the sample for
inspecting the JavaScript fresh code:

```yaml
name: Code coverage fresh code

on:
  workflow_dispatch:
  pull_request:
  push:
    branches:
      - main
      - 'releases/*'

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v3
        with:
          ref: ${{ github.event.pull_request.head.sha }}
          fetch-depth: 0

      - name: Use Node.js 18.x
        uses: actions/setup-node@v2
        with:
          node-version: 18.x

      - name: Install dependencies
        run: npm ci

      - name: Run tests
        run: npm test
      
      - name: Archive coverage data
        uses: actions/upload-artifact@v2
        with:
          name: jest-coverage-data
          path: .qodana/code-coverage
      
      - name: Qodana Scan
        uses: JetBrains/qodana-action@main
        env:
          QODANA_TOKEN: ${{ secrets.QODANA_TOKEN_JS }}
        with:
          pr-mode: true # Enable the pull-request mode
```

## Report overview
{id="overview-code-coverage-reports"}

After you have [prepared the project](#Prepare+the+project) and [ran the code coverage](#run-code-coverage), you can view 
code coverage reports in [Qodana Cloud](#Qodana+Cloud) or using your [IDE](#IDE). 

### Qodana Cloud

You can find code coverage statistics in the upper-right corner of the [%product% report](html-report.md) UI. It also 
enumerates the inspections that were employed by the feature.

<img src="code-coverage-report-qodana.png" dark-src="code-coverage-report-qodana_dark.png" width="706" alt="Code coverage in Qodana Cloud" border-effect="line" animated="true"/>

### IDE

You can view code coverage reports using IntelliJ IDEA, WebStorm, and PhpStorm IDEs starting from 
version 2023.2. This feature is available for reports retrieved from Qodana Cloud after linking, or reports from local storage.

<note>Currently, code coverage overview is not available for XML-formatted reports generated by IntelliJ IDEA Code 
Coverage Agent and JaCoCo, and LCOV-formatted reports generated by coverlet.msbuild.</note>

#### Open reports from Qodana Cloud

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

#### View coverage reports in IDE

You can view locally-based code coverage reports directly in JetBrains IDEs.

In your IDE, navigate to <menupath>Run | Show coverage data</menupath> and open the file containing a code coverage 
report. 

<img src="code-coverage-open-locally.png" dark-src="code-coverage-open-locally_dark.png" width="706" alt="The Choose Coverage Suite to Display dialog" border-effect="line"/>

In the <menupath>Coverage</menupath> tool window, you can view the test coverage report. This report shows the 
percentage of the code that has been executed or covered by tests. 

<img src="code-coverage-coverage-window.png" dark-src="code-coverage-coverage-window_dark.png" width="706" alt="The Coverage tool window" border-effect="line" animated="true"/>

#### Report overview

The IDE highlights the codebase test coverage using color marking. By default, the green color means
that a particular line was covered, and the red color means the uncovered line of code. 

<note>If you see that code coverage results look incomplete, you probably need to reconfigure your
code coverage tool and generate a new code coverage report.</note>

<img src="code-coverage-report.png" dark-src="code-coverage-report_dark.png" width="706" alt="The coverage report overview" border-effect="line"/>

The report shows coverage for the lines that implement the logic of a method, function, or a class, but not for the function,
method, or class declaration. The image below shows that code coverage is not applicable to line 7, while line 8 is not 
covered.

<img src="code-coverage-report-coverage.png" dark-src="code-coverage-report-coverage_dark.png" width="706" alt="Code coverage for a specific method" border-effect="line"/>
