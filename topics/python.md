[//]: # (title: Python)

<show-structure for="chapter" depth="3"/>

<!-- Human-readable linter names -->
<var name="qd" value="%python%"/>
<var name="qd-co" value="%python-co%"/>
<!-- Docker images -->
<var name="qd-image" value="jetbrains/%python-linter%"/>
<var name="qd-co-image" value="jetbrains/%python-co-linter%"/>
<!-- Linter names -->
<var name="qd-linter" value="%python-linter%"/>
<var name="qd-co-linter" value="%python-co-linter%"/>

<!-- Combined names -->
<var name="qd-image-combined" value="jetbrains/qodana-python&lt;-community&gt;:2025.2-eap"/>
<var name="qd-linter-combined" value="qodana-python&lt;-community&gt;:2025.2-eap"/>

<var name="JenkinsCred" value="https://www.jenkins.io/doc/book/using/using-credentials/#adding-new-global-credentials"/>

<var name="MultipipeCreate" value="https://www.jenkins.io/doc/book/pipeline/multibranch/#creating-a-multibranch-pipeline"/>
<var name="TeamCityProject" value="https://www.jetbrains.com/help/teamcity/configure-and-run-your-first-build.html#Create+your+first+project"/>
<var name="TeamCityBuildConfig" value="https://www.jetbrains.com/help/teamcity/creating-and-editing-build-configurations.html"/>
<var name="TeamCityBuildSteps" value="https://www.jetbrains.com/help/teamcity/configuring-build-steps.html"/>
<var name="TeamCityCommandLine" value="https://www.jetbrains.com/help/teamcity/command-line.html#General+Settings"/>
<var name="TeamCityPullRequests" value="https://www.jetbrains.com/help/teamcity/pull-requests.html"/>
<var name="TeamCityBranches" value="https://www.jetbrains.com/help/teamcity/configuring-finish-build-trigger.html#Trigger+Settings"/>
<var name="non-root-user" value="https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user"/>
<var name="native-arg" value="&lt;linter-code&gt;"/>
<var name="ide-documentation" value="https://www.jetbrains.com/help/pycharm/customizing-profiles.html"/>
<var name="teamcity-linter-list" value="Here, select the %qd% linter."/>

<!-- Jenkins and Docker variables -->
<var name="Dplugin" value="https://plugins.jenkins.io/docker-plugin/"/>
<var name="DPplugin" value="https://plugins.jenkins.io/docker-workflow/"/>
<var name="Gplugin" value="https://plugins.jenkins.io/git/"/>
<var name="Dockeraccess" value="https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user"/>

<!-- IDE-related variable -->
<var name="ide" value="PyCharm"/>

<link-summary>You can analyze your Python code using the %qd% and %qd-co% linters.</link-summary>

All %product% linters are based on JetBrains IDEs designed for particular programming languages and frameworks. To analyze 
Python projects, you can use the following linters:

| Linter  | Linter name    | Based on                   | Available under licenses                          | Supported languages               |
|---------|----------------|----------------------------|---------------------------------------------------|-----------------------------------|
| %qd%    | `%qd-linter%`    | PyCharm Professional       | Ultimate and Ultimate Plus [licenses](pricing.md) | Python, JavaScript and Typescript |
| %qd-co% | `%qd-co-linter%` | PyCharm Community Edition  | Community [license](pricing.md)                   | Python                            |


To see the list of supported technologies and features, you can navigate to the [](#python-feature-matrix) chapter of this section.

## Before you start
{id="python-before-you-start"}

### Install dependencies

If your project has external `pip` dependencies, set them up using the [`bootstrap`](before-running-qodana.md) 
key in the [`qodana.yaml`](qodana-yaml.md) file. For example, if your project dependencies are specified 
by the `requirements.txt` file in your project root, go into the configuration file and add the following line:

```yaml
bootstrap: pip install -r requirements.txt
```

### %cloud%

<include from="lib_qd.topic" element-id="before-start-qodana-cloud" use-filter="empty,python"/>

### Prepare your software

<include from="lib_qd.topic" element-id="before-start-prepare-software" use-filter="empty,python"/>

## Run %product%

<include from="lib_qd.topic" element-id="run-qodana" use-filter="empty,python,non-ruby,native"/>

## Explore analysis results

<include from="lib_qd.topic" element-id="explore-analysis-results" use-filter="empty,python"/>

## Extend %product% configuration

### Adjusting the scope of analysis

<include from="lib_qd.topic" element-id="adjust-scope-of-analysis"/>

### Enabling the baseline feature

<include from="lib_qd.topic" element-id="enabling-baseline" use-filter="empty,python"></include>

### Enabling the quality gate

<tabs group="linter-tabs">
    <tab group-key="linter-tabs-dotnet" title="%qd%">
        <p>You can configure <a href="quality-gate.topic">quality gates</a> for the total number of project problems, 
            specific problem severities, and code coverage by saving this snippet to the 
            <a href="qodana-yaml.md"><code>qodana.yaml</code></a> file:
        </p>
        <code-block lang="yaml">
            failureConditions:
            &nbsp;&nbsp;severityThresholds:
            &nbsp;&nbsp;&nbsp;&nbsp;any: 50 # Total number of problems in all severities
            &nbsp;&nbsp;&nbsp;&nbsp;critical: 1 # Severities
            &nbsp;&nbsp;&nbsp;&nbsp;high: 2
            &nbsp;&nbsp;&nbsp;&nbsp;moderate: 3
            &nbsp;&nbsp;&nbsp;&nbsp;low: 4
            &nbsp;&nbsp;&nbsp;&nbsp;info: 5
            &nbsp;&nbsp;testCoverageThresholds:
            &nbsp;&nbsp;&nbsp;&nbsp;fresh: 6 # Fresh code coverage
            &nbsp;&nbsp;&nbsp;&nbsp;total: 7 # Total percentage
        </code-block>
    </tab>
    <tab group-key="linter-tabs-cdnet" title="%qd-co%">
        <p>You can configure <a href="quality-gate.topic">quality gates</a> for the total number of project problems 
            and specific problem severities by saving this snippet to the <a href="qodana-yaml.md"><code>qodana.yaml</code></a> file:
        </p>
        <code-block lang="yaml">
            failureConditions:
            &nbsp;&nbsp;severityThresholds:
            &nbsp;&nbsp;&nbsp;&nbsp;any: 50 # Total number of problems in all severities
            &nbsp;&nbsp;&nbsp;&nbsp;critical: 1 # Severities
            &nbsp;&nbsp;&nbsp;&nbsp;high: 2
            &nbsp;&nbsp;&nbsp;&nbsp;moderate: 3
            &nbsp;&nbsp;&nbsp;&nbsp;low: 4
            &nbsp;&nbsp;&nbsp;&nbsp;info: 5
        </code-block>
    </tab>
</tabs>

### Analyzing pull requests

<include from="lib_qd.topic" element-id="analyzing-pull-requests" use-filter="empty,python,native"/>

## Supported technologies and features
{id="python-feature-matrix"}

This table contains the list of technologies and %product% [features](features.topic) supported by both linters.

<table>
    <tr>
      <td>Support for</td>
      <td>Name</td>
      <td>%qd%</td>
      <td>%qd-co%</td>
    </tr>
    <tr>
        <td>Programming languages</td>
        <td>
            <p>Python</p>
            <p>JavaScript&nbsp;and&nbsp;TypeScript</p>
        </td>
        <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
        </td>
        <td>
            <p>&#x2714;</p>
            <p>&nbsp;</p>
        </td>
    </tr>
    <tr>
        <td>Frameworks and libraries</td>
        <td>
            <p>Pyramid</p>
            <p>Node.js</p>
            <p>React</p>
            <p>Vue</p>
        </td>
        <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
        </td>
        <td>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
        </td>
    </tr>
    <tr>
        <td>Databases and ORM</td>
        <td>
            <p>MySQL</p>
            <p>MongoDB</p>
            <p>Oracle</p>
            <p>SQL</p>
            <p>SQL Server</p>
            <p>PostgreSQL</p>
        </td>
        <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
        </td>
        <td>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
        </td>
    </tr>
    <tr>
        <td>Markup languages</td>
        <td>
            <p>HTML</p>
            <p>JSON and JSON5</p>
            <p>RELAX NG</p>
            <p>XML</p>
            <p>YAML</p>
            <p>TOML</p>
            <p>SASS/SCSS</p>
            <p>PostCSS</p>
            <p>Less</p>
            <p>CSS</p>
        </td>
        <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
        </td>
        <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
        </td>
    </tr>
    <tr>
        <td>Scripting languages</td>
        <td>
            <p>Shell script</p>
        </td>
        <td>
            <p>&#x2714;</p>
        </td>
        <td>
            <p>&#x2714;</p>
        </td>
    </tr>
    <tr>
        <td>Other</td>
        <td>
            <p>Regular expressions</p>
            <p>Structural search</p>
            <p>HTTP Client</p>
        </td>
        <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
        </td>
        <td>
            <p>&#x2714;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
        </td>
    </tr>
    <tr>
        <td>%product% features</td>
        <td>
            <p><a href="baseline.topic"/></p>
            <p><a href="quality-gate.topic"/></p>
            <p><a href="code-coverage.md"/></p>
            <p><a href="flexinspect.md"/></p>
            <p><a href="insights.md"/><b>*</b></p>
            <p><a href="license-audit.topic"/><b>*</b></p>
            <p><a href="quick-fix.md"/></p>
            <p><a href="cloud-sso.md"/><b>*</b></p>
            <p><a href="vulnerability-checker.md"/><b>*</b></p>
        </td>
        <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
        </td>
        <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
        </td>
    </tr>
</table>

\* Available only under the Ultimate Plus [license](pricing.md).



