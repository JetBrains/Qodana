# JavaScript and TypeScript

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<!--<img src="js.png" dark-src="js_dark.png" alt="Qodana for .NET linter languages" width="296"/>-->

<show-structure for="chapter" depth="3"/>

<!-- Linter-related variables -->
<var name="qp" value="Qodana for JS"/>
<var name="qp-linter" value="jetbrains/qodana-js:2024.2"/>
<var name="JenkinsCred" value="https://www.jenkins.io/doc/book/using/using-credentials/#adding-new-global-credentials"/>
<var name="ide" value="WebStorm"/>

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
<var name="ide-documentation" value="https://www.jetbrains.com/help/webstorm/customizing-profiles.html"/>
<var name="native-arg" value="QDJS"/>
<var name="teamcity-linter-list" value="Here, select the %qp% linter."/>

<link-summary>%qp% is based on %ide% and provides static analysis for JavaScript or TypeScript projects.</link-summary>

All %product% linters are based on JetBrains IDEs designed for particular programming languages and frameworks. To analyze
JavaScript and TypeScript projects, you can use the %qp% linters based on [%ide%](https://www.jetbrains.com/webstorm/) and available under the Ultimate and
Ultimate Plus [licenses](pricing.md).

To see the list of supported technologies and features, you can navigate to the [](#js-feature-matrix) chapter of this section.


## Before you start
{id="js-before-you-start"}

### Install project dependencies

For a basic JavaScript project that has no external dependencies, no preliminary steps are required.

In case the project has external dependencies, you can set them up using the `bootstrap` key in the `qodana.yaml` file.
For example, if your project dependencies are specified by the `yarn.lock` file in your project root, add the following
line to `qodana.yaml`:

```yaml
bootstrap: yarn install
```
The command will be automatically executed before the analysis. You can use the `pnpm`, `npm` or `yarn` commands to install dependencies.

### Enable ESLint

ESLint is widely used in JavaScript projects. You can enable it using the `qodana.yaml` file:

```yaml
include:
    - name: Eslint
```

### Qodana Cloud

<include from="lib_qd.topic" element-id="before-start-qodana-cloud" use-filter="empty,generic"/>

### Prepare your software

<include from="lib_qd.topic" element-id="before-start-prepare-software" use-filter="empty,generic"/>

## Run %product%

<include from="lib_qd.topic" element-id="run-qodana" use-filter="empty,generic,js"/>

## Explore analysis results

<include from="lib_qd.topic" element-id="explore-analysis-results" use-filter="empty,js"/>

## Extend %product% configuration

### Adjusting the scope of analysis

<include from="lib_qd.topic" element-id="adjust-scope-of-analysis"/>

### Enabling the baseline feature

<include from="lib_qd.topic" element-id="enabling-baseline" use-filter="empty,generic,js"/>

### Enabling the quality gate

<include from="lib_qd.topic" element-id="enabling-quality-gate"/>

### Analyzing pull requests

<include from="lib_qd.topic" element-id="analyzing-pull-requests" use-filter="empty,generic,js"/>

## Supported technologies and features
{id="js-feature-matrix"}

%qp% provides inspections for the following technologies.

<table style="none">
    <tr>
        <td>Programming languages</td>
        <td>
            <p>JavaScript</p>
            <p>TypeScript</p>
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
    <tr>
        <td>Frameworks and libraries</td>
        <td>
            <p>Angular</p>
            <p>Cucumber</p>
            <p>EJS</p>
            <p>Handlebars/Mustache</p>
            <p>Less</p>
            <p>Node.js</p>
            <p>PostCSS</p>
            <p>Pug/Jade</p>
            <p>React</p>
            <p>Sass/SCSS</p>
            <p>Vue</p>
        </td>
    </tr>
</table>

<include from="lib_qd.topic" element-id="linters-supported-features" use-filter="empty,js"/>