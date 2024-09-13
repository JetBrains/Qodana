[//]: # (title: Python)

<show-structure for="chapter" depth="3"/>

<var name="qp" value="Qodana for Python"/>
<var name="qp-co" value="Qodana Community for Python"/>
<var name="qp-linter" value="jetbrains/qodana-python:2024.2"/>
<var name="qp-co-linter" value="jetbrains/qodana-python-community:2024.2"/>
<var name="qd-image" value="jetbrains/qodana-python<-community>:2024.2"/>
<var name="JenkinsCred" value="https://www.jenkins.io/doc/book/using/using-credentials/#adding-new-global-credentials"/>
<var name="ide" value="PyCharm"/>
<var name="Dplugin" value="https://plugins.jenkins.io/docker-plugin/"/>
<var name="DPplugin" value="https://plugins.jenkins.io/docker-workflow/"/>
<var name="Gplugin" value="https://plugins.jenkins.io/git/"/>
<var name="Dockeraccess" value="https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user"/>
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
<var name="teamcity-linter-list" value="Here, select either the %qp% or %qp-co% linter."/>

<link-summary>You can analyze your Python code using the %qp% and %qp-co% linters.</link-summary>

All %product% linters are based on JetBrains IDEs designed for particular programming languages and frameworks. To analyze 
Python projects, you can use the following linters:

* %qp% is based on PyCharm Professional and licensed under the Ultimate and 
Ultimate Plus [licenses](pricing.md), 
* %qp-co% is based on PyCharm Community and licensed under the Community license.

To see the list of supported technologies and features, you can navigate to the [](#python-feature-matrix) section.

## Before your start
{id="python-before-you-start"}

### Install dependencies

If your project has external `pip` dependencies, set them up using the [`bootstrap`](before-running-qodana.md) 
key in the [`qodana.yaml`](qodana-yaml.md) file. For example, if your project dependencies are specified 
by the `requirements.txt` file in your project root, in the configuration file add the following line:

```yaml
bootstrap: pip install -r requirements.txt
```

### Qodana Cloud

<include from="lib_qd.topic" element-id="before-start-qodana-cloud" use-filter="empty,python"/>

### Prepare your software

<include from="lib_qd.topic" element-id="before-start-prepare-software" use-filter="empty,python"/>

## Run %product%

<include from="lib_qd.topic" element-id="run-qodana" use-filter="empty,python"/>

## Explore analysis results

<include from="lib_qd.topic" element-id="explore-analysis-results" use-filter="empty,python"/>

## Extend %product% configuration

### Adjusting the scope of analysis

<include from="lib_qd.topic" element-id="adjust-scope-of-analysis"/>

### Enabling the baseline

<include from="lib_qd.topic" element-id="enabling-baseline" use-filter="empty,python"></include>

### Enabling the quality gate

<tabs group="linter-tabs">
    <tab group-key="linter-tabs-dotnet" title="%qp%">
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
    <tab group-key="linter-tabs-cdnet" title="%qp-co%">
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

<include from="lib_qd.topic" element-id="analyzing-pull-requests" use-filter="empty,python"/>

## Supported technologies and features
{id="python-feature-matrix"}

This table contains the list of technologies supported by both linters.

<table style="none">
    <tr>
        <td>Programming languages</td>
        <td>
            <p>Python</p>
        </td>
    </tr>
    <tr>
        <td>Frameworks and libraries</td>
        <td>
            <p>Django</p>
            <p>Google App Engine</p>
            <p>Jupyter</p>
            <p>Pyramid</p>
        </td>
    </tr>
    <tr>
        <td>Databases and ORM</td>
        <td>
            <p>MongoDB</p>
            <p>MySQL</p>
            <p>Oracle</p>
            <p>PostgreSQL</p>
            <p>SQL</p>
            <p>SQL Server</p>
        </td>
    </tr>
    <tr>
        <td>Markup languages</td>
        <td>
            <p>CSS</p>
            <p>HTML</p>
            <p>JSON and JSON5</p>
            <p>RELAX NG</p>
            <p>XML</p>
            <p>YAML</p>
        </td>
    </tr>
    <tr>
        <td>Scripting languages</td>
        <td>
            <p>Shell script</p>
        </td>
    </tr>
</table>

Here is the list of %product% features supported by each linter.

| Feature                       | %qp-co%  | %qp%      |
|-------------------------------|----------|-----------|
| [](baseline.topic)            | &#x2714; | &#x2714;  |
| [](quality-gate.topic)        | &#x2714; | &#x2714;  |
| [](code-coverage.md)          | &nbsp;   | &#x2714;  |
| [](license-audit.topic)       | &nbsp;   | &#x2714;  |
| [](quick-fix.md)              | &nbsp;   | &#x2714;  |
| [](vulnerability-checker.md)  | &nbsp;   | &#x2714;  |




