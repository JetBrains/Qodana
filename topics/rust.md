[//]: # (title: Rust)


<show-structure for="chapter" depth="3"/>

<!--<img src="php-linter.png" dark-src="php-linter_dark.png" alt="Qodana for PHP linter languages" width="296"/>-->

<!-- Human-readable linter names -->
<var name="qd" value="%rust%"/>
<!-- Docker images -->
<var name="qd-image" value="%rust-image%"/>
<!-- Linter names -->
<var name="qd-linter" value="%rust-linter%"/>

<var name="JenkinsCred" value="https://www.jenkins.io/doc/book/using/using-credentials/#adding-new-global-credentials"/>
<var name="ide" value="RustRover"/>

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
<var name="teamcity-linter-list" value="Here, select the %qd% linter."/>

<link-summary>%qd% is based on %ide% and provides inspections for PHP, JavaScript, and TypeScript.</link-summary>

All %product% linters are based on JetBrains IDEs designed for particular programming languages and frameworks.
To analyze Rust projects, you can use the %rust% linter with the following characteristics:

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
        <td>A Docker image</td>
    </tr>
    <tr>
        <td>Supported languages</td>
        <td>Rust</td>
    </tr>
</table>

To see the list of supported technologies and features, you can navigate to the [](#php-feature-matrix) chapter of this section.

## Before you start
{id="php-before-you-start"}

### Install project dependencies

In case a project has external dependencies, you can set them up using the `bootstrap` key in the [`qodana.yaml`](qodana-yaml.md) file,
for example:

```yaml
bootstrap: rustup toolchain install nightly
```
The command will be automatically executed before the analysis.

### %cloud%

<include from="lib_qd.topic" element-id="before-start-qodana-cloud" use-filter="empty,generic"/>

### Prepare your software

<include from="lib_qd.topic" element-id="before-start-prepare-software" use-filter="empty,generic"/>

## Run Qodana

<include from="lib_qd.topic" element-id="run-qodana" use-filter="empty,ruby"/>
<include from="lib_qd.topic" element-id="run-qodana-container-mode-config-examples" use-filter="empty,generic"/>

## Explore analysis results

<include from="lib_qd.topic" element-id="explore-analysis-results" use-filter="empty,php"/>

## Extend Qodana configuration

### Adjusting the scope of analysis

<include from="lib_qd.topic" element-id="adjust-scope-of-analysis"/>

### Enabling the baseline feature

<include from="lib_qd.topic" element-id="enabling-baseline" use-filter="empty,generic,php"/>

### Enabling the quality gate

<include from="lib_qd.topic" element-id="enabling-quality-gate"/>

### Analyzing pull requests

<include from="lib_qd.topic" element-id="analyzing-pull-requests-for-temp-non-native-mode" use-filter="empty,generic,golang"/>

## Supported technologies and features
{id="php-feature-matrix"}

The %qd% linter provides inspections for the following technologies.

<table style="none">
    <tr>
        <td>Programming languages</td>
        <td>
            <p>Rust</p>
        </td>
    </tr>
    <tr>
        <td>Markup languages</td>
        <td>
            <p>Dockerfile</p>
            <p>JSON</p>
            <p>Markdown</p>
            <p>TOML</p>
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
        <td>Other</td>
        <td>
            <p>Regular expressions</p>
        </td>
    </tr> 
</table>

<include from="lib_qd.topic" element-id="linters-supported-features" use-filter="empty,rust"/>