[//]: # (title: Dart)


<show-structure for="chapter" depth="3"/>

<!-- Human-readable linter names -->
<var name="qd" value="%dart%"/>
<!-- Docker images -->
<var name="qd-image" value="%dart-image%"/>
<!-- Linter names -->
<var name="qd-linter" value="%dart-linter%"/>

<var name="JenkinsCred" value="https://www.jenkins.io/doc/book/using/using-credentials/#adding-new-global-credentials"/>
<!-- qodana-dart is NOT based on a shipped JetBrains IDE: it is built on the IJ Void distribution + the qodana-dart plugin, which wraps the Dart SDK linter (QD-15779/QD-15780). The %ide% variable is therefore unused on this page. -->
<var name="ide" value="Dart SDK linter"/>

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
<var name="ide-documentation" value="https://dart.dev/tools/linter-rules"/>
<!-- TODO(QD-2785): confirm native-mode argument name for Dart (e.g. QDDART) with the dev team. -->
<var name="native-arg" value="QDDART"/>
<var name="teamcity-linter-list" value="Here, select the %qd% linter."/>

<link-summary>%qd% provides inspections for the Dart programming language and Flutter projects.</link-summary>

To analyze Dart and Flutter projects, you can use the %dart% linter that has the following characteristics:

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
        <td>The Dart SDK linter (via the <code>qodana-dart</code> plugin on the IntelliJ Void distribution)</td>
    </tr>
    <tr>
        <td>Available under licenses</td>
        <!-- TODO(QD-2785): confirm licensing tier for the Dart linter with the dev team. -->
        <td>TODO: confirm licenses</td>
    </tr>
    <tr>
        <td>Shipped as</td>
        <td>A Docker image</td>
    </tr>
    <tr>
        <td>Supported languages</td>
        <td>%dart-langs%</td>
    </tr>
</table>

To see the list of supported technologies and features, you can navigate to the [](#dart-feature-matrix) chapter of this section.

<note>
The %qd% linter is currently in Early Access, which means that it may not be reliable, may not work as intended, and may contain errors.
Your feedback is very welcome in our 
<a href="https://youtrack.jetbrains.com/newIssue?project=QD">issue tracker</a> or at
<a href="mailto:qodana-support@jetbrains.com">qodana-support@jetbrains.com</a>.
</note>

## Before you start
{id="dart-before-you-start"}

### Install project dependencies

<!-- TODO(QD-2785): confirm the recommended bootstrap command (dart pub get vs flutter pub get) with the dev team. -->
In case a project has external dependencies, you can set them up using the `bootstrap` key of your [YAML configuration](configuration-reference.md#Run+custom+commands),
for example:

```yaml
bootstrap: dart pub get
```
The command will be automatically executed before the analysis. For Flutter projects, use `flutter pub get` instead.

### %cloud%

<include from="lib_qd.topic" element-id="before-start-qodana-cloud" use-filter="empty,generic"/>

### Prepare your software

<include from="lib_qd.topic" element-id="before-start-prepare-software" use-filter="empty,generic"/>

## Configure the Dart SDK and ruleset

The `qodana-dart` plugin downloads the appropriate Dart SDK dynamically, selecting the
correct build for your operating system and architecture. You can configure the analysis
through your [YAML configuration](configuration-reference.md) file, where the plugin supports:

* Standard `include` and `exclude` patterns for adjusting the scope of analysis.
* Selecting a [Dart linter rule set](https://dart.dev/tools/linter-rules#sets).

<note>
Enabling and disabling individual inspections through <code>qodana.yaml</code> is not
supported for the Dart linter, because it relies on directory-specific
<code>analysis_options.yaml</code> files. Configure Dart rules in those files instead.
See the <a href="#dart-inspection-configuration">Inspection configuration</a> section below.
</note>

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

### Inspection configuration
{id="dart-inspection-configuration"}

The Dart linter manages its inspections through directory-specific
[`analysis_options.yaml`](https://dart.dev/tools/analysis) files rather than through
`qodana.yaml`. As a result:

* Individual Dart inspections cannot be enabled or disabled through `qodana.yaml` or the
  %cloud% *Inspections* tab, where they are shown but remain read-only.
* The only inspection setting controllable from `qodana.yaml` is a single toggle that
  enables or disables all Dart rules at once.
* File and directory exclusions, and the quality gate, continue to work without
  restrictions.

## Supported technologies and features
{id="dart-feature-matrix"}

The %qd% linter provides inspections for the following technologies.

<!-- TODO(QD-2785): confirm the full feature matrix with the dev team. Initial scope (QD-15779) is limited to the
     Dart SDK linter rules. -->
<table style="none">
    <tr>
        <td>Programming languages</td>
        <td>
            <p>Dart</p>
        </td>
    </tr>
    <tr>
        <td>Frameworks</td>
        <td>
            <p>Flutter</p>
        </td>
    </tr>
</table>

<!-- TODO(QD-2785): add the shared feature list once a "dart" filter exists in lib_qd.topic.
<include from="lib_qd.topic" element-id="linters-supported-features" use-filter="empty,dart"/>
-->
