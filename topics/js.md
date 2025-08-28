# JavaScript and TypeScript

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<!--<img src="js.png" dark-src="js_dark.png" alt="Qodana for .NET linter languages" width="296"/>-->

<show-structure for="chapter" depth="3"/>

<!-- Human-readable linter names -->
<var name="qd" value="%js%"/>
<!-- Docker images -->
<var name="qd-image" value="%js-image%"/>
<!-- Linter names -->
<var name="qd-linter" value="%js-linter%"/>

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
<var name="teamcity-linter-list" value="Here, select the %qd% linter."/>

<link-summary>%qd% is based on %ide% and provides static analysis for JavaScript or TypeScript projects.</link-summary>

All %product% linters are based on JetBrains IDEs designed for particular programming languages and frameworks. To analyze
JavaScript and TypeScript projects, you can use the %qd% linter with the following characteristics:

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
        <td>JavaScript and TypeScript</td>
    </tr>
</table>

To see the list of supported technologies and features, you can navigate to the [](#js-feature-matrix) chapter of this section.


## Before you start
{id="js-before-you-start"}

### Install project dependencies

For a basic JavaScript project that has no external dependencies, no preliminary steps are required.

In case a project has external dependencies, you can set them up using the `bootstrap` key in the `qodana.yaml` file.
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

### %cloud%

<include from="lib_qd.topic" element-id="before-start-qodana-cloud" use-filter="empty,generic"/>

### Prepare your software

<include from="lib_qd.topic" element-id="before-start-prepare-software" use-filter="empty,generic"/>

## Run %product%

<include from="lib_qd.topic" element-id="run-qodana" use-filter="empty,generic,js,native,non-ruby"/>

## Explore analysis results

<include from="lib_qd.topic" element-id="explore-analysis-results" use-filter="empty,js"/>

## Extend %product% configuration

### Adjusting the scope of analysis

<include from="lib_qd.topic" element-id="adjust-scope-of-analysis"/>

### Enabling the baseline feature

<include from="lib_qd.topic" element-id="enabling-baseline" use-filter="empty,generic,js,native"/>

### Enabling the quality gate

<include from="lib_qd.topic" element-id="enabling-quality-gate"/>

### Analyzing pull requests

<include from="lib_qd.topic" element-id="analyzing-pull-requests" use-filter="empty,generic,js,native"/>

## Supported technologies and features
{id="js-feature-matrix"}

%qd% provides inspections for the following technologies.

<table style="none">
    <tr>
        <td>Programming languages</td>
        <td>
            <p>JavaScript</p>
            <p>TypeScript</p>
        </td>
    </tr>
    <tr>
        <td>Frameworks and libraries</td>
        <td>
            <p>Angular</p>
            <p>Cucumber</p>
            <p>Node.js</p>
            <p>React</p>
            <p>Vue</p>
        </td>
    </tr>
    <tr>
        <td>Markup languages</td>
        <td>
            <p>CSS</p>
            <p>EJS</p>
            <p>Handlebars/Mustache</p>
            <p>HTML</p>
            <p>JSON and JSON5</p>
            <p>JSONPath</p>
            <p>Less</p>
            <p>PostCSS</p>
            <p>Pug/Jade</p>
            <p>RELAX NG</p>
            <p>Sass/SCSS</p>
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
            <p>Regular expressions</p>
            <p>Structural search</p>
            <p>HTTP Client</p>
        </td>
    </tr>
</table>

<include from="lib_qd.topic" element-id="linters-supported-features" use-filter="empty,js"/>