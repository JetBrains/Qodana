# PHP

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<show-structure for="chapter" depth="3"/>

<!--<img src="php-linter.png" dark-src="php-linter_dark.png" alt="Qodana for PHP linter languages" width="296"/>-->

<!-- Linter-related variables -->
<var name="qp" value="Qodana for PHP"/>
<var name="qp-linter" value="jetbrains/qodana-php:2024.2"/>
<var name="JenkinsCred" value="https://www.jenkins.io/doc/book/using/using-credentials/#adding-new-global-credentials"/>
<var name="ide" value="PhpStorm"/>

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
<var name="ide-documentation" value="https://www.jetbrains.com/help/phpstorm/customizing-profiles.html"/>
<var name="native-arg" value="QDPHP"/>
<var name="teamcity-linter-list" value="Here, select the %qp% linter."/>

<link-summary>%qp% is based on %ide% and provides inspections for PHP, JavaScript, and TypeScript.</link-summary>

All %product% linters are based on JetBrains IDEs designed for particular programming languages and frameworks. To analyze
PHP, JavaScript and TypeScript projects, you can use the %qp% linters based on [%ide%](https://www.jetbrains.com/phpstorm/) and available under the Ultimate and
Ultimate Plus [licenses](pricing.md).

To see the list of supported technologies and features, you can navigate to the [](#php-feature-matrix) chapter of this section.

## Before you start
{id="php-before-you-start"}

### Qodana Cloud

<include from="lib_qd.topic" element-id="before-start-qodana-cloud" use-filter="empty,generic"/>

### Prepare your software

<include from="lib_qd.topic" element-id="before-start-prepare-software" use-filter="empty,generic"/>

## Run %product%

<include from="lib_qd.topic" element-id="run-qodana" use-filter="empty,generic,php"/>

## Explore analysis results

<include from="lib_qd.topic" element-id="explore-analysis-results" use-filter="empty,php"/>

## Extend %product% configuration

### Adjusting the scope of analysis

<include from="lib_qd.topic" element-id="adjust-scope-of-analysis"/>

### Enabling the baseline feature

<include from="lib_qd.topic" element-id="enabling-baseline" use-filter="empty,generic,php"/>

### Enabling the quality gate

<include from="lib_qd.topic" element-id="enabling-quality-gate"/>

### Analyzing pull requests

<include from="lib_qd.topic" element-id="analyzing-pull-requests" use-filter="empty,generic,php"/>

## Supported technologies and features
{id="php-feature-matrix"}

The %qp% linter provides inspections for the following technologies.

<table style="none">
    <tr>
        <td>Programming languages</td>
        <td>
            <p>PHP</p>
            <p>JavaScript</p>
            <p>TypeScript</p>
        </td>
    </tr>
    <tr>
        <td>Markup languages</td>
        <td>
            <p>Blade</p>
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
        <td>Dependency management</td>
        <td>
            <p>Composer</p>
        </td>
    </tr>
    <tr>
        <td>Frameworks and libraries</td>
        <td>
            <p>Cucumber</p>
            <p>Joomla!</p>
            <p>PHPUnit</p>
            <p>Psalm</p>
        </td>
    </tr>
</table>

<include from="lib_qd.topic" element-id="linters-supported-features" use-filter="empty,php"/>