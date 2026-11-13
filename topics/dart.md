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
<var name="native-arg" value="QDPOLY"/>
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
        <td>The Flutter SDK</td>
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
        <td>Supported language</td>
        <td>%dart-langs%</td>
    </tr>
    <tr>
        <td>Supported framework</td>
        <td>Flutter</td>
    </tr>
    <tr>
        <td>Supported %product% features</td>
        <td><a href="baseline.topic">Baseline</a>, <a href="quality-gate.topic">quality gate</a></td>
    </tr>
</table>

<note>
The %qd% linter is currently in Early Access, which means that it may not be reliable, may not work as intended, and may contain errors.
Your feedback is very welcome in our 
<a href="https://youtrack.jetbrains.com/newIssue?project=QD">issue tracker</a> or at
<a href="mailto:qodana-support@jetbrains.com">qodana-support@jetbrains.com</a>.
</note>

## Before you start
{id="dart-before-you-start"}

### Install project dependencies

Before starting the linter, make sure that project dependencies are set up. You can do this using the `bootstrap` key of 
your [YAML configuration](configuration-reference.md#Run+custom+commands), for example:

```yaml
bootstrap: flutter pub get
```
The command will be automatically executed before the analysis. For plain Dart projects, use the `dart pub get` command instead.

### %cloud%

<include from="lib_qd.topic" element-id="before-start-qodana-cloud" use-filter="empty,generic"/>

### Prepare your software

<tabs group="software">
    <tab title="GitHub Actions" group-key="github">
        On the <ui-path>Settings</ui-path> tab of the GitHub UI, create the <code>QODANA_TOKEN</code>
        <a href="https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository">encrypted secret</a>
        and save the <a href="project-token.md">project token</a> as its value.</tab>
    <tab title="Command line" group-key="command-line">
        <p>If you are using Linux, you should be able to run Docker under your current <a href="%non-root-user%">non-root user</a>.</p>
        <p>Follow the instructions from the <a href="https://github.com/JetBrains/qodana-cli">Qodana CLI</a> page on GitHub.</p></tab>
</tabs>

## Run Qodana

The Dart SDK dependency management uses absolute paths that are not cross-compatible between 
[Docker and native deployment modes](deploy-qodana.md#Deployment+modes). 
Use native mode to avoid the potential issues with dependency setup in your local development while using %product% CLI. 
In Docker mode, SDK is not shipped within the `%qd-image%` image, so you should provide it manually by using the 
[`bootstrap`](configuration-reference.md#Run+custom+commands) option. 

<tabs group="software">
    <tab title="GitHub Actions" group-key="github">
        <p>You can run %product% using the <a href="https://github.com/marketplace/actions/qodana-scan">Qodana Scan GitHub action</a>.</p>
        <p>To analyze the <code>main</code> branch, release branches and the pull requests coming
            to your repository in native mode, save this workflow configuration to the <code>.github/workflows/code_quality.yml</code> file:</p>
        <code-block lang="yaml" filter="generic">
            name: Qodana
            on:
                workflow_dispatch:
                pull_request:
                push:
                    branches: # Specify your branches here
                        - main # The 'main' branch
                        - 'releases/*' # The release branches
            jobs:
                qodana:
                    runs-on: ubuntu-latest
                    permissions:
                        contents: write
                        pull-requests: write
                        checks: write
                    steps:
                        - uses: actions/checkout@v3
                          with:
                              ref: ${{ github.event.pull_request.head.sha }}  # to check out the actual pull request commit, not the merge commit
                              fetch-depth: 0  # a full history is required for pull request analysis
                        - name: 'Qodana Scan'
                          uses: %action-version%
                          with:
                              args: |
                                  --linter %qd-linter%
                                  --within-docker false
                          env:
                              QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
        </code-block>
        <p>This configuration uses the <code>--linter</code>
            <a href="docker-image-configuration.topic" anchor="docker-config-reference-qodana-scan">option</a>
            to specify a <a href="linters.md">linter</a>. The
            <code>--within-docker</code> option in the <code>false</code> state is used for enabling native mode.</p>
        <p>More configuration examples are available in the <a href="github.md"/> section.</p>
    </tab>
    <tab title="Command line" group-key="command-line">
        <p>Run this command in the project root directory:</p>
        <code-block lang="shell" prompt="$" filter="generic">
            qodana scan \
            &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;qodana-cloud-token&gt;" \
            &nbsp;&nbsp;&nbsp;--linter %qd-linter% \
            &nbsp;&nbsp;&nbsp;--within-docker false
        </code-block>
        <p>This configuration uses the <code>--linter</code>
            <a href="docker-image-configuration.topic" anchor="docker-config-reference-qodana-scan">option</a>
            to specify the %dart% linter. The
            <code>--within-docker</code> option in the <code>false</code> state is used for enabling native mode.</p>
        <p>If you are using another %cloud% instance than https://qodana.cloud/, override it by declaring the <code>QODANA_ENDPOINT</code> environment variable.</p>
        <p>In your browser, open <a href="https://qodana.cloud">%cloud%</a> to examine analysis reports and
            reconfigure the analysis. See the <a href="ui-overview.md"/> section of the documentation for full details.</p>
    </tab>
</tabs>

## Explore analysis reports

<p>After %product% analyzed your project and uploaded the analysis reports to %cloud%, in
    <a href="https://qodana.cloud">%cloud%</a> navigate to your project and review analysis reports.</p>

## Extend Qodana configuration

### Configuring inspections and scope
{id="dart-inspection-configuration"}

The %qd% linter reads the analysis scope and rules from the [`analysis_options.yaml`](https://dart.dev/tools/analysis) files contained in the repository,
so any changes to the analysis scope, i.e., included and excluded files and directories or [ruleset](https://dart.dev/tools/linter-rules#sets) should be made in those files. 

> Using the `analysis_options.yaml` file takes precedence over the YAML configuration.
> A file excluded according to the `analysis_options.yaml` file will not be analyzed even if you include it in the YAML configuration.
{style="note"}

The only inspection that you can configure via a [YAML file](configuration-reference.md) is the `DartAnalyze` inspection 
acting as a single toggle for all Dart and Flutter analysis. This inspection is enabled by
default. To disable the inspection, for example, when you only need other inspections
from the linter, exclude it as follows:

```yaml
exclude:
  - name: DartAnalyze
```

### Configuring the Flutter SDK

The %qd% linter uses the Flutter SDK available via the `PATH`. To use a specific installation,
set the `QODANA_FLUTTER_PATH` environment variable to the `bin` directory of your Flutter SDK.

The Docker version of %qd% requires manual configuration of the Flutter/Dart SDK.

### Enabling the baseline feature

<tabs group="software">
    <tab title="GitHub Actions" group-key="github">
      <p>Save the snippet to the <code>.github/workflows/code_quality.yml</code> file containing the
          <code>--baseline</code> option that specifies the path to a SARIF-formatted baseline file:</p>
      <code-block lang="yaml" filter="generic">
          name: Qodana
          on:
            workflow_dispatch:
            pull_request:
            push:
              branches: # Specify your branches here
                - main # The 'main' branch
                - master # The 'master' branch
                - 'releases/*' # The release branches
          jobs:
            qodana:
              runs-on: ubuntu-latest
              permissions:
                contents: write
                pull-requests: write
                checks: write
              steps:
                - uses: actions/checkout@v3
                  with:
                    ref: ${{ github.event.pull_request.head.sha }}  # to check out the actual pull request commit, not the merge commit
                    fetch-depth: 0  # a full history is required for pull request analysis
                - name: 'Qodana Scan'
                  uses: %action-version%
                  with:
                    args: |
                      --baseline &lt;path/to/qodana.sarif.json&gt;
                      --linter %qd-linter%
                      --within-docker false
                  env:
                    QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
      </code-block>
    </tab>
    <tab title="Command line" group-key="command-line">
        <p>Run this command in the project root directory using the
            <code>--baseline</code> option to specify the path to a SARIF-formatted file containing a baseline:</p>
        <code-block lang="shell" prompt="$" filter="generic">
            qodana scan \
            &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
            &nbsp;&nbsp;&nbsp;--linter %qd-linter% \
            &nbsp;&nbsp;&nbsp;--within-docker false \
            &nbsp;&nbsp;&nbsp;--baseline &lt;path/to/qodana.sarif.json&gt;
        </code-block>
        <p>In your browser, open <a href="https://qodana.cloud">%cloud%</a> to examine the analysis reports and
    reconfigure the analysis. See the <a href="ui-overview.md"/> section of the documentation for full details.</p>
    </tab>
</tabs>

### Enabling the quality gate

<p>You can configure the <a href="quality-gate.topic">quality gate</a> for a total number of problems:</p>

<tabs group="software">
    <tab title="GitHub Actions" group-key="github">
      <p>Save the snippet to the <code>.github/workflows/code_quality.yml</code> file containing the
          <code>--fail-threshold</code> option that specifies the number of problems:</p>
      <code-block lang="yaml" filter="generic"><![CDATA[
          name: Qodana
          on:
            workflow_dispatch:
            pull_request:
            push:
              branches: # Specify your branches here
                - main # The 'main' branch
                - master # The 'master' branch
                - 'releases/*' # The release branches
          jobs:
            qodana:
              runs-on: ubuntu-latest
              permissions:
                contents: write
                pull-requests: write
                checks: write
              steps:
                - uses: actions/checkout@v3
                  with:
                    ref: ${{ github.event.pull_request.head.sha }}  # to check out the actual pull request commit, not the merge commit
                    fetch-depth: 0  # a full history is required for pull request analysis
                - name: 'Qodana Scan'
                  uses: %action-version%
                  with:
                    args: |
                      --fail-threshold <number>
                      --linter %qd-linter%
                      --within-docker false
                  env:
                    QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
      ]]>
</code-block>
    </tab>
    <tab title="Command line" group-key="command-line">
        <p>Run this command in the project root directory using the
            <code>--fail-threshold</code> option to specify the number of problems accepted as a 
            <a href="quality-gate.topic">quality gate</a>:</p>
        <code-block lang="shell" prompt="$" filter="generic"><![CDATA[
            qodana scan \
               -e QODANA_TOKEN="<cloud-project-token>" \
               --linter %qd-linter% \
               --within-docker false \
               --fail-threshold <number>
        ]]>
</code-block>
    </tab>
</tabs>

### Analyzing pull requests

<tabs group="software">
    <tab title="GitHub Actions" group-key="github">
      <p>
          The <a href="https://github.com/marketplace/actions/qodana-scan">Qodana Scan GitHub action</a> automatically
          analyzes all pull requests, so you do not have to provide any additional configuration. Save this configuration
          to the <code>.github/workflows/code_quality.yml</code> file:
      </p>
      <code-block lang="yaml" filter="generic"><![CDATA[
          name: Qodana
          on:
            workflow_dispatch:
            pull_request:
            push:
              branches: # Specify your branches here
                - main # The 'main' branch
                - master # The 'master' branch
                - 'releases/*' # The release branches
          jobs:
            qodana:
              runs-on: ubuntu-latest
              permissions:
                contents: write
                pull-requests: write
                checks: write
              steps:
                - uses: actions/checkout@v3
                  with:
                    ref: ${{ github.event.pull_request.head.sha }}  # to check out the actual pull request commit, not the merge commit
                    fetch-depth: 0  # a full history is required for pull request analysis
                - name: 'Qodana Scan'
                  uses: %action-version%
                  with:
                    args: |
                      --diff-start=<GIT_START_HASH>
                      --linter %qd-linter%
                      --within-docker false
                  env:
                    QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
      ]]>
</code-block>
    </tab>
    <tab title="Command line" group-key="command-line">
    <p>To <a href="analyze-pr.md">analyze changes</a> in your code, employ the <code>--diff-start</code>
        option and specify a hash of the commit that will act as a base for comparison:</p>
        <code-block lang="shell" prompt="$" filter="generic"><![CDATA[
            qodana scan \
               -e QODANA_TOKEN="<cloud-project-token>" \
               --linter %qd-linter% \
               --within-docker false \
               --diff-start=<GIT_START_HASH>
        ]]>
</code-block>
    </tab>
</tabs>

