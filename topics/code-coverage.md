[//]: # (title: Code coverage)

<show-structure for="chapter" depth="3"/>

<link-summary>Code coverage uses generated reports to calculate the overall code coverage inside a method, class, and file. 
It also reports on the issues associated with the missing coverage in these entities.</link-summary>

**Code coverage** uses generated reports to calculate the overall code coverage inside a method, class, and file. 
It also reports on the issues associated with the missing coverage in these entities.

This feature is available under the Ultimate and Ultimate Plus [licenses](pricing.md#pricing-linters-licenses) in the
following linters:

<table>
    <tr>
        <td>Linter</td>
        <td>Code coverage tool</td>
        <td>Supported report file extensions</td>
    </tr>
    <tr>
        <td rowspan="2"><a href="jvm.md">%jvm%</a></td>
        <td><a href="https://github.com/JetBrains/intellij-coverage">IntelliJ IDEA Code Coverage Agent</a> is the recommended tool</td>
        <td><code>ic</code></td>
    </tr>
    <tr>
        <td><a href="https://www.jacoco.org/jacoco/">JaCoCo</a></td>
        <td><code>xml</code></td>
    </tr>
    <tr>
        <td><a href="js.md">%js%</a></td>
        <td><a href="https://jestjs.io/">Jest</a></td>
        <td><code>info</code> (LCOV-formatted file)</td>
    </tr>
    <tr>
        <td><a href="php.md">%php%</a></td>
        <td><a href="https://phpunit.de/">PhpUnit</a></td>
        <td><code>xml</code></td>
    </tr>
    <tr>
        <td rowspan="2"><a href="dotnet.md">%dotnet%</a></td>
        <td rowspan="2"><a href="https://www.nuget.org/packages/coverlet.msbuild">coverlet.msbuild</a></td>
    </tr>
    <tr>
        <td><p><code>lcov</code> (LCOV-formatted file)</p>
        <p>For Cobertura:<code>info</code> or <code>cobertura</code>*</p></td>
    </tr>
    <tr>
        <td><a href="python.md">%python%</a></td>
        <td><a href="https://coverage.readthedocs.io/en/7.3.2/">Coverage.py</a></td>
        <td><code>xml</code></td>
    </tr>
    <tr>
        <td><a href="golang.md">%go%</a></td>
        <td><code>go test</code></td>
        <td><code>out</code></td>
    </tr>
</table>

\* When both LCOV (`.info`) and Cobertura (`.cobertura`) reports are present, LCOV (`.info`) is preferred.

<note>Code coverage for files is available only for <a href="js.md">%js%</a>, <a href="php.md">%php%</a>, and
<a href="python.md">%python%</a> linters.</note>

## How code coverage works

<link-summary>Learn how the code coverage feature works.</link-summary>

For the missing code coverage issues, the predefined threshold in %instance% is currently set to 50%.

Code coverage uses several inspections that are already included in the `qodana.recommended` and `qodana.starter` 
[default inspection profiles](inspection-profiles.md#inspection-profiles-existing-profiles), so you do not need to enable them:  

<!-- Do I need to enable any inspections in case of .NET -->

| Linter                | Employed inspection                                                                                |
|-----------------------|----------------------------------------------------------------------------------------------------|
| [%jvm%](jvm.md)       | [`JvmCoverageInspection`](https://www.jetbrains.com/help/inspectopedia/JvmCoverageInspection.html) |
| [%js%](js.md)         | [`JsCoverageInspection`](https://www.jetbrains.com/help/inspectopedia/JsCoverageInspection.html)   |
| [%php%](php.md)       | [`PhpCoverageInspection`](https://www.jetbrains.com/help/inspectopedia/PhpCoverageInspection.html) |
| [%python%](python.md) | [`PyCoverageInspection`](https://www.jetbrains.com/help/inspectopedia/PyCoverageInspection.html)   |
| [%go%](golang.md)     | [`GoCoverageInspection`](https://www.jetbrains.com/help/inspectopedia/GoCoverageInspection.html)   |
| [%dotnet%](dotnet.md) | [`NetCoverageInspection`](https://www.jetbrains.com/help/inspectopedia/NetCoverageInspection.html) |

Once analysis is complete, reports are available in [%instance% reports](ui-overview.md#Open+an+HTML+report) and JetBrains IDEs.

### Code coverage calculation

<link-summary>%instance% calculates code coverage based on the number of code lines containing logic, with function, 
method, and class statements being ignored.</link-summary>

%instance% calculates code coverage based on the number of code lines containing logic with function, method, and class statements
being ignored. Here is the snippet containing comments on how it works: 

```javascript
function divide(a, b) { // Not analyzed by the code coverage
  return a / b; // Analyzed by the code coverage
}
module.exports = divide; // Analyzed by the code coverage
```

## Before you start
{id="code-coverage-before-you-start"}

<link-summary>Learn how to prepare your coverage tool and project before running the code coverage feature.</link-summary>

<tip>You can find configuration examples on <a href="https://github.com/qodana/qodana-coverage/tree/main">GitHub</a>.</tip>

1. Configure your code coverage tool. For example, [Jest](https://jestjs.io/) code coverage reports should contain paths relative to a project root. 
If your codebase files are contained in the `<project-root>/src/` directory, then reports should contain 
`src/<file-name>` file paths. 

1. Use your code coverage tool to generate coverage reports. These reports should be saved to the `<project-root>/.qodana/code-coverage` 
directory. You can copy the coverage report file by using the [`boostrap`](qodana-yaml.md#Run+custom+commands) key, for example:

    ```yaml
   boostrap: copy path/to/coverage/file <project-root>/.qodana/code-coverage 
    ```

    To learn how to override the `<project-root>/.qodana/code-coverage` directory, see the recommendation from the [](#run-code-coverage) chapter.
    
    For a [monorepo project](monorepo-project.md) containing multiple repositories, this directory should be created in each repository.

1. Prepare your project. If you have a monorepo project, save %product% configuration for each repository in a 
separate `qodana.yaml` file. You can put these files in repository directories, or give them custom names and save them 
in the root directory of a project.

    For the [%dotnet%](dotnet.md) linter, add the <a href="https://www.nuget.org/packages/coverlet.msbuild"><code>coverlet.msbuild</code></a> 
    and [`coverlet.collector`](https://www.nuget.org/packages/coverlet.collector) packages to the test project. Also, for the [%dotnet%](dotnet.md) linter check 
    whether a code coverage report contains information about generated files.

## Run code coverage
{id="run-code-coverage"}

<link-summary>Learn how to run the code coverage feature.</link-summary>

<note>
You can run %instance% over a single test coverage report generated by a single code coverage tool at a time.
</note>

<note>
The <a href="golang.md">%go%</a> linter requires that your project contains no <code>.idea</code> directory. 
</note>

To learn more about running code coverage using the [%dotnet%](dotnet.md) linter, skip to the 
[](#code-coverage-qodana-for-dotnet) section of this page.

<tabs>
    <tab title="Docker or Qodana CLI" id="code-coverage-docker-cli">
        <p>Map the directory containing code coverage reports to the <code>/data/coverage</code> directory and
        a project token using the <code>QODANA_TOKEN</code> variable. Here are the Docker and 
        <a href="https://github.com/JetBrains/qodana-cli">Qodana CLI</a> command samples:</p>
        <tabs>
            <tab title="Docker" id="code-coverage-docker">
                <code-block lang="shell" prompt="$">
                    docker run \
                        -v $(pwd):/data/project/ \
                        -v .qodana/code-coverage/:/data/coverage \
                        -e QODANA_TOKEN="&lt;qodana-cloud-token&gt;" \
                        jetbrains/qodana-&lt;image&gt;
                </code-block>
            </tab>
            <tab title="Qodana CLI" id="code-coverage-cli">
                <code-block lang="shell" prompt="$">
                    qodana scan \
                       -v .qodana/code-coverage/:/data/coverage \
                       -e QODANA_TOKEN="&lt;qodana-cloud-token&gt;"
                </code-block>
            </tab>
        </tabs>
        <p>If you have a <a href="monorepo-project.md">monorepo project</a>, use the 
        <a href="docker-image-configuration.topic" anchor="docker-image-configuration-project-dir"><code>-i &lt;path-relative-to-project-root&gt;</code></a> 
        option to point a repository directory. If you saved 
        <a href="qodana-yaml.md">%product% configuration</a> files under 
        <a anchor="code-coverage-before-you-start">custom names</a>, use the 
        <a href="docker-image-configuration.topic" anchor="docker-image-configuration-config"><code>--config &lt;path-relative-to-project-root&gt;</code></a> option.
        To override the default code coverage report directory, use the 
        <a href="docker-image-configuration.topic" anchor="docker-config-reference-code-coverage"><code>--coverage-dir &lt;path-relative-to-project-root&gt;</code></a> option.
        </p>
    </tab>
<tab title="GitHub Actions" id="code-coverage-pipeline">
        <p>Create the pipeline that will store all code coverage output files in the <code>&lt;project-root-dir&gt;/.qodana/code-coverage</code> 
        directory. You can find various examples of the GitHub Actions configurations on the 
<a href="https://github.com/qodana/qodana-coverage/tree/7360c03be1f44a4ed0e591218977005b07dd569e/.github/workflows">GitHub</a> website.</p>

Below is the pipeline configuration example for the [%js%](js.md) linter running in the `JS/jest` directory of a repository:

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
      
    - name: Archive coverage data # Archive data for use by Qodana
      uses: actions/upload-artifact@v4
      with:
        name: jest-coverage-data
        path: JS/jest/.qodana/code-coverage

    - name: Qodana Scan # Run Qodana
      uses: JetBrains/qodana-action@main
      env:
        QODANA_TOKEN: ${{ secrets.QODANA_TOKEN_JS }}
      with:
        args: "-i JS/jest --image %js-image%"
        pr-mode: false
```
<p>If you have a <a href="monorepo-project.md">monorepo project</a> and saved <a href="qodana-yaml.md">%product% configuration</a> 
files under <a anchor="code-coverage-before-you-start">custom names</a>, then in the <code>args</code> block use the 
<a href="docker-image-configuration.topic" anchor="docker-image-configuration-config"><code>--config,&lt;path-relative-to-project-root&gt;</code></a> option.
To override the default code coverage report directory, use the 
<a href="docker-image-configuration.topic" anchor="docker-config-reference-code-coverage"><code>--coverage-dir,&lt;path-relative-to-project-root&gt;</code></a> option.
</p>
</tab>

<tab title="GitLab CI/CD" id="code-coverage-gitlab">
<p>Create a <a href="gitlab.md"/> pipeline that will read all generated code coverage output files from the <code>.qodana/coverage</code> 
directory using the <a href="docker-image-configuration.topic" anchor="docker-image-configuration-coverage-dir"><code>--coverage-dir</code></a> option:</p>
        <code-block lang="yaml">
        include:
            - component: %gitlab-version%
              inputs:
                args: --coverage-dir $CI_PROJECT_DIR/.qodana/code-coverage --image &lt;image&gt;
        </code-block>
        <p>
            If you have a <a href="monorepo-project.md">monorepo project</a> and saved 
            <a href="qodana-yaml.md">%product% configuration</a> files under 
            <a anchor="code-coverage-before-you-start">custom names</a>, then add the 
            <a href="docker-image-configuration.topic" anchor="docker-image-configuration-config"><code>--config,&lt;path-relative-to-project-root&gt;</code></a> option to <code>args</code>:
        </p>
        <code-block lang="yaml">
        include:
            - component: %gitlab-version%
              inputs:
                args: --coverage-dir $CI_PROJECT_DIR/.qodana/code-coverage --config &lt;path-relative-to-project-root&gt; --image &lt;image&gt;
        </code-block>
</tab>
<tab title="Azure Pipelines" id="code-coverage-azure">
<p>Create a <a href="qodana-azure-pipelines.md">pipeline</a> that will read all generated code coverage output files from the <code>.qodana/coverage</code> 
directory using the <a href="docker-image-configuration.topic" anchor="docker-image-configuration-coverage-dir"><code>--coverage-dir</code></a> option:</p>
<tabs>
   <tab title="Pipeline configuration">
      <p>In this configuration, the <code>args:</code> block maps the results of code coverage analysis to the <code>/data/coverage</code> directory.</p>
      <code-block lang="yaml">
         # Start with a minimal pipeline that you can customize to build and deploy your code.
         # Add steps that build, run tests, deploy, and more:
         # https://aka.ms/yaml
         &nbsp;
         trigger:
           - main
         &nbsp;
         pool:
           vmImage: ubuntu-latest
         &nbsp;
         steps:
           - task: Cache@2  # Not required, but Qodana will open projects with cache faster.
               key: '"$(Build.Repository.Name)" | "$(Build.SourceBranchName)" | "$(Build.SourceVersion)"'
               path: '$(Agent.TempDirectory)/qodana/cache'
               restoreKeys: |
                 "$(Build.Repository.Name)" | "$(Build.SourceBranchName)"
                 "$(Build.Repository.Name)"
           - task: %azure-version%
             env:
               QODANA_TOKEN: $(QODANA_TOKEN)
             inputs:
               args: '-v $(System.DefaultWorkingDirectory)/&lt;ProjectPath&gt;/.qodana/:/data/coverage'
           </code-block>
        </tab>
        <tab title="Classic interface">
            <p>Use the <ui-path>Qodana CLI arguments</ui-path> field to map the results of code coverage analysis to the 
                <code>/data/coverage</code> directory. For example, this can be the <code>$(System.DefaultWorkingDirectory)/&lt;ProjectPath&gt;</code> directory:</p>
            <img src="azure-pipelines-code-coverage.png" width="375" alt="The Qodana Scan task UI config for baseline and quality gate" border-effect="line"/>
        </tab>
</tabs>
</tab>
</tabs>

### Qodana for .NET
{id="code-coverage-qodana-for-dotnet"}

> Configuration examples for code coverage are available on the [GitHub](https://github.com/qodana/qodana-coverage) website.
> {style="tip"}

Here is an example of the [`qodana.yaml`](qodana-yaml.md) file configuration for the [%dotnet%](dotnet.md) linter:

```yaml
version: 1.0

dotnet:
  solution: <your-solution-file>

bootstrap: |
  dotnet build
  cd <path-to-dir-with-test-project-file>
  dotnet add package coverlet.msbuild 
  dotnet add package coverlet.collector
  dotnet test \
    /p:CollectCoverage=true \
    /p:CoverletOutput=$(pwd)/.qodana/code-coverage/ \
    /p:CoverletOutputFormat=<format>
```

Here, the `dotnet` section configures the solution file. 

The [`bootstrap`](qodana-yaml.md#Run+custom+commands) key configures steps that will be performed before running %instance%:

| Command step                                      | Description                                                                                                                      |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| `dotnet build`                                    | Build a project or a solution                                                                                                    |
| `cd <path-to-dir-with-test-project-file>`         | Navigate to the directory containing the project test file                                                                       |
| `dotnet add package coverlet.msbuild`             | Add the `coverlet.msbuild` package to the project. This command needs to be repeated for each package                            |
| `dotnet test ... `                                | Execute tests in the project, and:                                                                                               |
| `/p:CollectCoverage=true`                         | Enable code coverage                                                                                                             |
| `/p:CoverletOutput=$(pwd)/.qodana/code-coverage/` | Collect code coverage results to a specific directory. In case of Cobertura, also specify here a file and extension              |
| `/p:CoverletOutputFormat=<format>`                | Specify the code coverage report format: `lcov` or `cobertura`. The `lcov` format is preferred in all cases including Cobertura  |

If a code coverage report file contains information about generated files, exclude this information by adding one or 
both of the following lines to the `dotnet test ...` line:

```yaml
/p:ExcludeByAttribute="Obsolete,GeneratedCodeAttribute,CompilerGeneratedAttribute" 
/p:ExcludeByFile="some-exclude-pattern"
```

Here is the description of these lines: 

| Command step                  | Description                                                   |
|-------------------------------|---------------------------------------------------------------|
| `/p:ExcludeByAttribute="..."` | Exclude methods or classes marked with specific attributes    |
| `/p:ExcludeByFile="..."`      | Excludes files matching a pattern (e.g., `**/Generated/*.cs`) |

> If your project has a single source file, the generated Cobertura report will contain an empty path to that file. 
> To work around this issue, either add a second source file to the project or use the LCOV format instead.
{style="note"}

Code coverage analysis results for the [Qodana for .NET](dotnet.md) linter are available in [](#overview-code-coverage-qodana-cloud).

### Fresh code

Fresh code is the code contained in a GitHub pull request. %instance% can calculate fresh code coverage and display the results. 

<note>While working with fresh code, %instance% cannot analyze coverage issues for missing coverage in methods, classes, and files.</note>

To enable the fresh code feature, configure the PR-mode in your [GitHub](github.md) workflow. 

Here is the sample for inspecting the JavaScript fresh code:

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
        uses: actions/upload-artifact@v4
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

After you have [prepared the project](#code-coverage-before-you-start) and [run the code coverage](#run-code-coverage), you can view 
code coverage reports in [%cloud%](#overview-code-coverage-qodana-cloud) or using your [IDE](#IDE). 

### Qodana Cloud
{id="overview-code-coverage-qodana-cloud"}

You can find code coverage statistics in the upper-right corner of the [%instance% report](ui-overview.md#Open+an+HTML+report) UI. It also 
lists the inspections used by the feature.

<img src="code-coverage-report-qodana.png" dark-src="code-coverage-report-qodana_dark.png" width="706" alt="Code coverage in %cloud%" border-effect="line" animated="true"/>

### IDE

You can view code coverage reports using IntelliJ IDEA, WebStorm, PhpStorm, PyCharm, and GoLand IDEs starting from 
version 2023.2. This feature is available for reports retrieved from %cloud% after linking, or reports from local storage.

<note>Currently, code coverage overview is not available for XML-formatted reports generated by IntelliJ IDEA Code 
Coverage Agent and JaCoCo, and LCOV-formatted reports generated by coverlet.msbuild.</note>

#### Open reports from %cloud%

<procedure>
<step>
<p>In your IDE, navigate to <ui-path>Tools | %product% | Log in to %product%</ui-path>.</p>
<img src="code-coverage-step-1.png" dark-src="code-coverage-step-1_dark.png" width="706" alt="The Log in to %cloud% menu" border-effect="line"/>
</step>
<step><p>On the <ui-path>Settings</ui-path> dialog, click <ui-path>Log in</ui-path>.</p>
<img src="code-coverage-login-window.png" dark-src="code-coverage-login-window_dark.png" width="706" alt="The Settings window" border-effect="line"/>
<p>This will redirect you to the authentication page.</p>
</step>
<step>
    <p>In the <ui-path>Settings</ui-path> dialog, search for the project you would like to link with.</p>
<img src="code-coverage-login-linking-project.png" dark-src="code-coverage-login-linking-project_dark.png" width="706" alt="Linking with the project " border-effect="line"/>
</step>
</procedure>

#### View coverage reports in IDE

You can view code coverage reports based locally using JetBrains IDEs.

In your IDE, navigate to <ui-path>Run | Show coverage data</ui-path> and open the file containing a code coverage 
report. 

<img src="code-coverage-open-locally.png" dark-src="code-coverage-open-locally_dark.png" width="706" alt="The Choose Coverage Suite to Display dialog" border-effect="line"/>

In the <ui-path>Coverage</ui-path> tool window, you can view the test coverage report. This report shows the 
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
