[//]: # (title: Lua)


<show-structure for="chapter" depth="3"/>

<!-- Human-readable linter names -->
<var name="qd" value="%lua%"/>
<!-- Docker images -->
<var name="qd-image" value="%lua-image%"/>
<!-- Linter names -->
<var name="qd-linter" value="%lua-linter%"/>

<var name="JenkinsCred" value="https://www.jenkins.io/doc/book/using/using-credentials/#adding-new-global-credentials"/>
<!-- TODO(QD-16413): Lua is NOT based on a shipped JetBrains IDE. It runs on the qodana-poly linter (OpenGrep plugin), see QD-16140/QD-15967. The %ide% variable and every "Based on <IDE>" reference below need to be revisited with the dev team. -->
<var name="ide" value="TODO-no-ide"/>

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
<!-- TODO(QD-16413): confirm the inspection-profile help URL for Lua (OpenGrep-based rules, not an IDE profile). -->
<var name="ide-documentation" value="https://www.jetbrains.com/help/idea/customizing-profiles.html"/>
<!-- TODO(QD-16413): confirm native-mode argument name for Lua (if any) with the dev team. -->
<var name="native-arg" value="QDLUA"/>
<var name="teamcity-linter-list" value="Here, select the %qd% linter."/>

<link-summary>%qd% provides static analysis for the Lua programming language.</link-summary>

<!-- TODO(QD-16413): standard linter intro says "based on JetBrains IDEs". The Lua linter runs OpenGrep taint and pattern rules via the qodana-poly linter (QD-16140/QD-15967). Rewrite this intro with the dev team before publishing. -->
To analyze Lua projects, you can use the %lua% linter with the following characteristics:

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
        <!-- TODO(QD-16413): confirm. Not a JetBrains IDE — the qodana-poly linter built on the OpenGrep plugin (taint and pattern rules). -->
        <td>TODO: qodana-poly linter (OpenGrep plugin) (confirm wording)</td>
    </tr>
    <tr>
        <td>Available under licenses</td>
        <!-- TODO(QD-16413): confirm licensing tier for the Lua linter. -->
        <td>TODO: confirm licenses</td>
    </tr>
    <tr>
        <td>Shipped as</td>
        <td>A Docker image</td>
    </tr>
    <tr>
        <td>Supported languages</td>
        <td>%lua-langs%</td>
    </tr>
</table>

To see the list of supported technologies and features, you can navigate to the [](#lua-feature-matrix) chapter of this section.

<note>
The %qd% linter is currently in Early Access, which means that it may not be reliable, may not work as intended, and may contain errors.
Your feedback is very welcome in our 
<a href="https://youtrack.jetbrains.com/newIssue?project=QD">issue tracker</a> or at
<a href="mailto:qodana-support@jetbrains.com">qodana-support@jetbrains.com</a>.
</note>

## Before you start
{id="lua-before-you-start"}

### Install project dependencies

<!-- TODO(QD-16413): confirm whether Lua projects need any dependency bootstrap step (e.g. luarocks install) with the dev team. -->
In case a project has external dependencies, you can set them up using the `bootstrap` key of your [YAML configuration](configuration-reference.md#Run+custom+commands),
for example:

```yaml
bootstrap: luarocks install <list of dependencies>
```
The command will be automatically executed before the analysis.

### %cloud%

<include from="lib_qd.topic" element-id="before-start-qodana-cloud" use-filter="empty,generic"/>

### Prepare your software

<include from="lib_qd.topic" element-id="before-start-prepare-software" use-filter="empty,generic"/>

## Run Qodana

<include from="lib_qd.topic" element-id="run-qodana" use-filter="empty,ruby"/>
<include from="lib_qd.topic" element-id="run-qodana-container-mode-config-examples" use-filter="empty,generic"/>

## Explore analysis reports

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

<!-- NOTE(QD-16413): Unlike the Dart linter, the Lua linter supports normal inspection configuration in qodana.yaml
     (enabling/disabling inspections), per Peter Hilton's confirmation in QD-16300. This means the Qodana Cloud
     Inspections tab works without restrictions for Lua. Consider documenting inspection configuration here once
     the qodana.yaml keys are confirmed with the dev team. -->

## Supported technologies and features
{id="lua-feature-matrix"}

The %qd% linter provides inspections for the following technologies.

<!-- TODO(QD-16413): confirm the full feature matrix with the dev team. Initial scope (QD-15967) is basic Lua
     support analyzed by OpenGrep taint and pattern rules, without statement differentiation at the AST level. -->
<table style="none">
    <tr>
        <td>Programming languages</td>
        <td>
            <p>Lua</p>
        </td>
    </tr>
</table>

<!-- TODO(QD-16413): add the shared feature list once a "lua" filter exists in lib_qd.topic.
<include from="lib_qd.topic" element-id="linters-supported-features" use-filter="empty,lua"/>
-->
