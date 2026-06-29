# Go

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<!--<img src="golang.png" dark-src="golang_dark.png" alt="Golang" width="296"/>-->

<show-structure for="chapter" depth="3"/>

<!-- Human-readable linter names -->
<var name="qd" value="%go%"/>
<!-- Docker images -->
<var name="qd-image" value="%go-image%"/>
<!-- Linter names -->
<var name="qd-linter" value="%go-linter%"/>

<var name="JenkinsCred" value="https://www.jenkins.io/doc/book/using/using-credentials/#adding-new-global-credentials"/>
<var name="ide" value="GoLand"/>

<!-- Content-related variables -->
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
<var name="ide-documentation" value="https://www.jetbrains.com/help/go/customizing-profiles.html"/>
<var name="native-arg" value="QDGO"/>
<var name="teamcity-linter-list" value="Here, select the %qd% linter."/>

<link-summary>%qd% is based on %ide% and provides static analysis for Go projects.</link-summary>

All %product% linters are based on JetBrains IDEs designed for particular programming languages and frameworks. To analyze
Golang projects, you can use the %qd% linter with the following characteristics:

<table>
    <tr>
        <td>Characteristic</td>
        <td>Description</td>
    </tr>
    <tr>
        <td>Linter name</td>
        <td><code>%qd-linter%</code></td>
    </tr>
    <tr>
        <td>Docker image</td>
        <td><code>%qd-image%</code></td>
    </tr>
    <tr>
        <td>Based on</td>
        <td>%ide%</td>
    </tr>
    <tr>
        <td>Available under licenses</td>
        <td>Ultimate and Ultimate Plus <a href="pricing.md">licenses</a></td>
    </tr>
    <tr>
        <td>Shipped as</td>
        <td>A <a href="deploy-qodana.md" anchor="deploy-qodana-native-mode">native solution</a> and a Docker image</td>
    </tr>
    <tr>
        <td>Supported languages</td>
        <td>Golang, JavaScript and TypeScript</td>
    </tr>
</table>


To see the list of supported technologies and features, you can navigate to the [](#golang-feature-matrix) chapter of this section.

## Before you start
{id="golang-before-you-start"}

### Qodana Cloud

<include from="lib_qd.topic" element-id="before-start-qodana-cloud" use-filter="empty,generic"/>

### Prepare your software

<include from="lib_qd.topic" element-id="before-start-prepare-software" use-filter="empty,generic"/>

### Specify a linter

<include from="lib_qd.topic" element-id="before-start-specify-a-linter"/>

### Specify a directory in your project

<include from="lib_qd.topic" element-id="before-start-specify-directory"/>

## Run Qodana

<include from="lib_qd.topic" element-id="run-qodana" use-filter="empty,generic,golang,non-ruby,native"/>

## Explore analysis reports

<include from="lib_qd.topic" element-id="explore-analysis-results" use-filter="empty,golang"/>

## Extend Qodana configuration

### Adjusting the scope of analysis

<include from="lib_qd.topic" element-id="adjust-scope-of-analysis"/>

### Enabling the baseline feature

<include from="lib_qd.topic" element-id="enabling-baseline" use-filter="empty,generic,golang"/>

### Enabling the quality gate

<include from="lib_qd.topic" element-id="enabling-quality-gate"/>

### Analyzing pull requests

<include from="lib_qd.topic" element-id="analyzing-pull-requests" use-filter="empty,generic,native"/>

### Managing plugins

<include from="lib_qd.topic" element-id="extending-configuration-manage-pllugins"/>

## Supported technologies and features
{id="golang-feature-matrix"}

%qd% provides inspections for the following technologies.

<table style="none">
    <tr>
        <td>Programming languages</td>
        <td>
            <p>Golang</p>
            <p>JavaScript&nbsp;and&nbsp;TypeScript</p>
        </td>
    </tr>
    <tr>
        <td>Frameworks and libraries</td>
        <td>
            <p>Node.js</p>
            <p>React</p>
        </td>
    </tr>
    <tr>
        <td>Markup languages</td>
        <td>
            <p>CSS</p>
            <p>HTML</p>
            <p>JSON and JSON5</p>
            <p>JSONPath</p>
            <p>RELAX NG</p>
            <p>XML</p>
            <p>YAML</p>
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
              <p>SQL server</p>
        </td>
    </tr>
    <tr>
        <td>Scripting languages</td>
        <td>
            <p>Shell script</p>
        </td>
    </tr>
    <tr>
        <td>Other</td>
        <td>
            <p>HTTP Client</p>
            <p>Regular expressions</p>
            <p>Structural search</p>
        </td>
    </tr>
</table>

<include from="lib_qd.topic" element-id="linters-supported-features" use-filter="empty,non-jvm"/>