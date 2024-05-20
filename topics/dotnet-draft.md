[//]: # (title: .NET)

<no-index/>

<show-structure for="chapter" depth="3"/>

<var name="qp" value="Qodana for .NET"/>
<var name="qp-co" value="Qodana Community for .NET"/>
<var name="qp-linter" value="jetbrains/qodana-dotnet:2024.1"/>
<var name="qp-co-linter" value="jetbrains/qodana-cdnet:2024.1-eap"/>
<var name="qd-image" value="jetbrains/qodana-&lt;dotnet/cdnet&gt;:2024.1&lt;-eap&gt;"/>
<var name="JenkinsCred" value="https://www.jenkins.io/doc/book/using/using-credentials/#adding-new-global-credentials"/>
<var name="ide" value="Rider"/>
<var name="ide-co" value="ReSharper"/>
<var name="Dplugin" value="https://plugins.jenkins.io/docker-plugin/"/>
<var name="DPplugin" value="https://plugins.jenkins.io/docker-workflow/"/>
<var name="Gplugin" value="https://plugins.jenkins.io/git/"/>
<var name="Dockeraccess" value="https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user"/>
<var name="MultipipeCreate" value="https://www.jenkins.io/doc/book/pipeline/multibranch/#creating-a-multibranch-pipeline"/>
<var name="dotsettings" value="https://www.jetbrains.com/help/resharper/Sharing_Configuration_Options.html#solution-team-shared-layer"/>

<link-summary>You can analyze your .NET code using the %qp% and %qp-co% linters.</link-summary>

<warning>This is a draft document, so we do not recommend that you use it.</warning>

All %product% linters are based on IDEs designed for particular programming languages and frameworks. To analyze
Python projects, you can use the following linters:

* %qp% is based on Rider and licensed under the Ultimate and
  Ultimate Plus [licenses](pricing.md),
* %qp-co% is based on ReSharper and licensed under the Community license.

To see the list of supported features, you can navigate to the [](#dotnet-feature-matrix) section.

<!-- The native mode needs to be added here -->

## Before your start
{id="dotnet-before-you-start"}

Create a [Qodana Cloud account](cloud-quickstart.md). In Qodana Cloud, obtain a [project token](project-token.md) that
will be used by %product% for identifying and verifying a license.

### SDK version

<!-- Is this available only for the Qodana for .NET linter? -->

The Dockerized version of %qp% provides the following SDK versions:

* 6.0.417
* 7.0.404
* 8.0.100

All SDK versions are stored in the `/usr/share/dotnet/sdk` directory of the %product% container filesystem.

In case a project requires a different version of the SDK, you can set it using the
[`bootstrap`](before-running-qodana.md) key in the `qodana.yaml` file.
For example, this command will install the required version of the SDK that is specified in the
`global.json` file and located in the root of your project:

<code-block lang="yaml">
    bootstrap: curl -fsSL https://dot.net/v1/dotnet-install.sh |
      bash -s -- --jsonfile /data/project/global.json -i /usr/share/dotnet
</code-block>

### Solution configuration

By default, %product% tries to locate and employ a single solution file, or, if no solution file is present,
it tries to find a project file. If your project contains multiple solution files, you need to specify the exact
filename as shown below.

#### Specify a solution

You can specify a solution in various ways. Using a [`YAML configuration`](#dotnet-specify-solution-yaml) is the most 
convenient method because once configured, you can use it in any software that runs %product% without any additional 
configuration.

##### YAML file
{id="dotnet-specify-solution-yaml"}

Specify the relative path to the solution file from the project root:

```yaml
dotnet:
  solution: <relative-path-to-solution-file>
```

If your project contains no solution files and multiple project files, you need to employ a project file:

```yaml
dotnet:
  project: <relative-path-to-project-file>
```

##### Docker
{id="dotnet-specify-solution-local-run"}

To start, pull the image from Docker Hub (only necessary to get the latest version):

<code-block lang="shell" prompt="$">
    docker pull %qd-image%
</code-block>

Start local analysis with `source-directory` pointing to the root of your project and `QODANA_TOKEN` referring to the 
[project token](project-token.md):

<tabs group="docker-commands">
  <tab title="%qp%" group-key="qodana-dotnet">
    <code-block lang="shell">
      docker run \
      &nbsp;&nbsp;&nbsp;-v &lt;source-directory&gt;/:/data/project/ \
      &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
      &nbsp;&nbsp;&nbsp;%qp-linter% \
      &nbsp;&nbsp;&nbsp;--property=qodana.net.solution=&lt;relative-path-to-solution-file&gt;
    </code-block>
  </tab>
  <tab title="%qp-co%" group-key="qodana-cdnet">
    <code-block lang="shell">
      docker run \
      &nbsp;&nbsp;&nbsp;-v &lt;source-directory&gt;/:/data/project/ \
      &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
      &nbsp;&nbsp;&nbsp;%qp-co-linter% \
      &nbsp;&nbsp;&nbsp;--solution=&lt;relative-path-to-solution-file&gt;
    </code-block>
    </tab>
</tabs>

If your project contains no solution files and multiple project files, you need to employ a project file:

<tabs group="docker-commands">
<tab title="%qp%" group-key="qodana-dotnet">
<code-block lang="shell">
docker run \
&nbsp;&nbsp;&nbsp;-v &lt;source-directory&gt;/:/data/project/ \
&nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
&nbsp;&nbsp;&nbsp;%qp-linter% \
&nbsp;&nbsp;&nbsp;--property=qodana.net.project=&lt;relative-path-to-project-file&gt;
</code-block>
</tab>
<tab title="%qp-co%" group-key="qodana-cdnet">
<code-block lang="shell">
docker run \
&nbsp;&nbsp;&nbsp;-v &lt;source-directory&gt;/:/data/project/ \
&nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
&nbsp;&nbsp;&nbsp;%qp-co-linter% \
&nbsp;&nbsp;&nbsp;--project=&lt;relative-path-to-project-file&gt;
</code-block>
</tab>
</tabs>

#### Configure a solution

A solution configuration defines which projects in the solution to build, and which project configurations to use for
specific projects within the solution.

Each newly created solution includes the `Debug` and `Release` configurations, which can be complemented by your custom
configurations.

##### YAML file
{id="dotnet-configure-solution-yaml"}

You can switch configurations of the current solution in the `qodana.yaml` file:

```yaml
dotnet:
  configuration: Release
```

By default, the solution platform is set to `Any CPU`, and you can override it in the `qodana.yaml` file:

```yaml
dotnet:
  platform: x86
```
<!-- Do I need to add GitHub config example here? -->

##### Docker
{id="dotnet-configure-solution-local-run"}

You can configure a solution using the `--configuration` option:

<tabs group="docker-commands">
<tab title="%qp%" group-key="qodana-dotnet">
<code-block lang="shell">
docker run \
&nbsp;&nbsp;&nbsp;-v &lt;source-directory&gt;/:/data/project/ \
&nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
&nbsp;&nbsp;&nbsp;%qp-linter% \
&nbsp;&nbsp;&nbsp;--property=qodana.net.configuration=Release
</code-block>
</tab>
<tab title="%qp-co%" group-key="qodana-cdnet">
<code-block lang="shell">
docker run \
&nbsp;&nbsp;&nbsp;-v &lt;source-directory&gt;/:/data/project/ \
&nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
&nbsp;&nbsp;&nbsp;%qp-co-linter% \
&nbsp;&nbsp;&nbsp;--configuration=Release
</code-block>
</tab>
</tabs>

By default, the solution platform is set to `Any CPU`, and you can override it using the `--platform` option:

<tabs group="docker-commands">
<tab title="%qp%" group-key="qodana-dotnet">
<code-block lang="shell">
docker run \
&nbsp;&nbsp;&nbsp;-v &lt;source-directory&gt;/:/data/project/ \
&nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
&nbsp;&nbsp;&nbsp;%qp-linter% \
&nbsp;&nbsp;&nbsp;--property=qodana.net.platform=x86
</code-block>
</tab>
<tab title="%qp-co%" group-key="qodana-cdnet">
<code-block lang="shell">
docker run \
&nbsp;&nbsp;&nbsp;-v &lt;source-directory&gt;/:/data/project/ \
&nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
&nbsp;&nbsp;&nbsp;%qp-co-linter% \
&nbsp;&nbsp;&nbsp;--platform=x86
</code-block>
</tab>
</tabs>

### Build the project

During the start, %product% builds your project. If the project build fails, code analysis cannot be performed. 
You can configure the project build using the [`bootstrap`](before-running-qodana.md) key of the [`qodana.yaml`](qodana-yaml.md) file contained in your 
project directory.

<!-- The bootstrap command examples should be provided here -->

Alternatively, you can build your project in a pipeline before %product% starts.

<!-- GitHub pipeline build needs to be provided here -->

If you wish to run your custom build, use the `--no-build` option while running the linter:

```shell
docker run \
   -v <source-directory>/:/data/project/ \
   -e QODANA_TOKEN="<cloud-project-token>" \
   %qd-image% \
   --no-build
```
{prompt="$"}

<!-- GitHub pipeline using no-build should be provided here -->

<!-- The native mode needs to be explained in the Run Qodana section -->

## Run %product%

<include from="lib_qd.topic" element-id="root-and-non-root-users-info-bubble"></include>

<p>You can run <a href="https://github.com/JetBrains/qodana-cli">Qodana CLI</a> in the native mode, which is the recommended method 
for the %qp% linter. Alternatively, you can use the Docker command from the <ui-path>Docker image</ui-path> tab.</p>

<!-- Mention the possibility to run Qodana for .NET in the native mode -->

<tabs group="cli-settings">
    <tab  group-key="qodana-cli" title="Native mode using Qodana CLI">
        <p>Assuming that you have already
            <a href="https://github.com/JetBrains/qodana-cli/releases/latest">installed</a> Qodana CLI on your
            machine and followed the recommendations from 
<a href="native-mode.md" anchor="Before+you+start">this section</a>, you can run this command in the project root directory:</p>
        <code-block lang="shell" prompt="$">
            qodana scan \
            &nbsp;&nbsp;&nbsp;--ide QDNET
        </code-block>
        <p>Here, the <code>--ide</code> option downloads and employs the JetBrains IDE binary file.</p>
        <p>Alternatively, in the <code>qodana.yaml</code> file you can save the <code>ide: QDNET</code> configuration, 
    and then run %instance% using this command:</p>
        <code-block lang="shell" prompt="$">
            qodana scan
        </code-block>
    <p>If you plan to use private NuGet feeds, we recommend running the native mode on the same machine where
you build a project because this can guarantee that %instance% has access to private NuGet feeds.</p>
    </tab>
    <tab group-key="docker-image" title="Docker image">
        <p>To start, pull the image from Docker Hub (only necessary to get the latest version):</p>
        <code-block filter="non-gs" style="block" lang="shell" prompt="$">
            docker pull %qd-image%
        </code-block>
        <p>Start local analysis with <code>source-directory</code>
            pointing to the root of your project and
            <code>QODANA_TOKEN</code> referring to the <a href="project-token.md">project token</a>:</p>
        <code-block lang="shell" prompt="$">
        docker run \
        &nbsp;&nbsp;&nbsp;-v &lt;source-directory&gt;/:/data/project/ \
        &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
        &nbsp;&nbsp;&nbsp;%qd-image% \
        &nbsp;&nbsp;&nbsp;--show-report
        </code-block>
        <p>Open <a href="https://qodana.cloud">Qodana Cloud</a> in your browser to examine inspection results.</p>
        <p>You can run %qp% using private NuGet feeds:</p>
        <code-block lang="shell" prompt="$">
        docker run \
        &nbsp;&nbsp;&nbsp;-v &lt;source-directory&gt;/:/data/project/ \
        &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
        &nbsp;&nbsp;&nbsp;-e QODANA_NUGET_URL=&lt;private-NuGet-feed-URL&gt; \
        &nbsp;&nbsp;&nbsp;-e QODANA_NUGET_USER=&lt;login&gt; \
        &nbsp;&nbsp;&nbsp;-e QODANA_NUGET_PASSWORD=&lt;plaintext-password&gt; \
        &nbsp;&nbsp;&nbsp;-e QODANA_NUGET_NAME=&lt;name-of-private-NuGet-feed&gt; \
        &nbsp;&nbsp;&nbsp;%qd-image% \
        &nbsp;&nbsp;&nbsp;--show-report
        </code-block>
        <p>Configuration examples for using private NuGet feeds are available on the 
            <a href="https://github.com/qodana/qodanaprivateFeed/">GitHub</a> website.</p>
    </tab>
</tabs>

## Explore analysis results

### JetBrains IDEs
{id="dotnet-explore-results-ides"}

You can get the latest %instance% report in your IDE as explained below.

<procedure>
   <step>
      <p>In your IDE, navigate to <ui-path>Tools | Qodana | Log in to Qodana</ui-path>.</p>
   </step>
   <step>
      <p>
         In the <ui-path>Settings</ui-path> dialog, click <ui-path>Log in</ui-path>.
      </p>
      <img src="ide-plugin-connect-1.png" dark-src="ide-plugin-connect-1_dark.png" width="706" alt="Connecting to Qodana Cloud" border-effect="line"/>
   <p>This will redirect you to the authentication page.</p>
   </step>
   <step>
      <p>Select the <a href="cloud-projects.topic">Qodana Cloud project</a> to link your local project with.</p>
      <img src="ide-plugin-connect-2.png" dark-src="ide-plugin-connect-2_dark.png" width="706" alt="Linking the project to Qodana Cloud" border-effect="line"/>
   </step>
   <step>
        <p>By enabling the <ui-path>Always load most relevant Qodana report</ui-path> option, you get actual reports automatically retrieved from Qodana Cloud.</p>
      <img src="ide-plugin-connect-3.png" dark-src="ide-plugin-connect-3_dark.png" width="706" alt="Enabling to load the most relevant reports" border-effect="line"/>
        <p>In this case, the IDE will search and fetch from Qodana Cloud the report that has the revision ID corresponding to the 
        current revision ID (HEAD). If this report was not found, the IDE will select the previous report with the revision
        closest to the current revision ID (HEAD). Otherwise, the IDE retrieves the latest available report from Qodana Cloud.</p>
    </step> 
    <step>
       <p>In the <ui-path>Server-Side Analysis</ui-path> tool window, view <a href="qodana-ide-plugin.md" anchor="ide-plugin-study-reports">analysis results</a>.</p>
    </step>
</procedure>

### Qodana Cloud

Once %product% analyzed your project and uploaded the analysis results to Qodana Cloud, in
[Qodana Cloud](https://qodana.cloud) navigate to your project and study the analysis results report.

<!-- This image needs to be replaced with something from .NET -->

<img src="qc-report-example.png" dark-src="qc-report-example_dark.png" alt="Analysis report example" width="720" border-effect="line"/>

<p>To learn more about %instance% report UI, see the <a href="ui-overview.md"/> section.</p>


## Extend the configuration

### Adjust the scope of analysis

#### %qp%

%qp% automatically recognizes the [`qodana.yaml`](qodana-yaml.md) file for the analysis configuration, so that you don't need to provide any
additional parameters.

You can also use `.editorconfig` and [`.DotSettings`](%dotsettings%) files for configuring %qp%.

Also, the %qp% linter supports Roslyn analyzers,
with each analyzer considered as a separate inspection. You can configure Roslyn analyzers using the `.editorconfig`
files. This is an experimental feature, so use them at your own risk.

To disable them, you can [configure the %instance% profile](custom-profiles.md) using
the `qodana.yaml` file, for example:

```yaml
name: "Custom profile"

baseProfile: qodana.starter

groups: # List of configured groups
  - groupId: InspectionsToExclude
    groups:
      - "category:C#/Roslyn Analyzers"

inspections: # Group invocation
  - group: InspectionsToExclude
    enabled: false # Disable the InspectionsToExclude group
```

Configuration examples are available [on GitHub](https://github.com/hybloid/fluentassertions/blob/develop/qodana.yaml).

If you are familiar with configuring code analysis via
[%ide% inspection profiles](https://www.jetbrains.com/help/rider/Code_Analysis__Code_Inspections.html), you can pass the
reference to the existing profile by mapping the profile to the `/data/profile.xml` file inside the container:

<code-block lang="shell" prompt="$">
docker run \
&nbsp;&nbsp;&nbsp;-v &lt;source-directory&gt;/:/data/project/ \
&nbsp;&nbsp;&nbsp;-v &lt;inspection-profile.xml&gt;:/data/profile.xml \
&nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
&nbsp;&nbsp;&nbsp;%qp-linter%
</code-block>

#### %qp-co%

If you have previously worked on the target solution with ReSharper, you may have already
[configured code inspections settings](https://www.jetbrains.com/help/resharper/Code_Analysis__Configuring_Warnings.html).
If so, InspectCode will find your [custom settings](https://www.jetbrains.com/help/resharper/Sharing_Configuration_Options.html)
in `.DotSettings` files and apply them. If there are no settings files, then the default severity levels will be used
for all analyses. Besides custom severity levels for code inspections, InspectCode will look for the following settings in
`.DotSettings` files:

* Whether the solution-wide analysis is enabled.
* [Naming rules](https://www.jetbrains.com/help/resharper/Coding_Assistance__Naming_Style.html) (this can only be configured using `DotSettings` files).
* [Files, folders, and file masks excluded from code analysis](https://www.jetbrains.com/help/resharper/Code_Analysis__Configuring_Warnings.html#exclude_items).
* [Files, file masks, and regions with generated code, where the code analysis is partly disabled](https://www.jetbrains.com/help/resharper/Code_Analysis__Configuring_Warnings.html#exclude_generated) (this can only be configured using `.DotSettings` files).
* A place where the code analysis engine should store caches. You can specify it on the **Environment | General** page of ReSharper options.
* Target languages (**ReSharper | Options | Environment | Products — Features**).

To configure InspectCode on a CI server, make all configurations locally with ReSharper, save the settings to the
[Solution Team-Shared layer](https://www.jetbrains.com/help/resharper/Sharing_Configuration_Options.html#saveTo),
and then commit the resulting `YourSolution.sln.DotSettings` file in the solution directory to your VCS. InspectCode on
the server will find and apply these settings.

By default, InspectCode also runs Roslyn analyzers on the target solution. If you want to disable  Roslyn analyzers, you
can do it in the solution's `.DotSettings` file, for example:

```xml
<wpf:ResourceDictionary xml:space="preserve"
     xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
     xmlns:s="clr-namespace:System;assembly=mscorlib"
     xmlns:ss="urn:shemas-jetbrains-com:settings-storage-xaml"
     xmlns:wpf="http://schemas.microsoft.com/winfx/2006/xaml/presentation">

     <!-- Enable/disable Roslyn analyzers and Source Generators -->
     <s:Boolean x:Key="/Default/CodeInspection/Roslyn/RoslynEnabled/@EntryValue">False</s:Boolean>

     <!-- Include/exclude Roslyn analyzers in Solution-Wide Analysis -->
     <s:Boolean x:Key="/Default/CodeInspection/Roslyn/UseRoslynInSwea/@EntryValue">False</s:Boolean>

     </wpf:ResourceDictionary>
```

### Enable the baseline

You can skip analysis for specific problems using the [baseline](baseline.topic) feature.

#### JetBrains IDEs
{id="dotnet-enable-baseline-ides"}

<procedure>
    <step>In your IDE, navigate to the <ui-path>Problems</ui-path> tool window. </step>
    <step>In the <ui-path>Problems</ui-path> tool window, click the <ui-path>Server-Side Analysis</ui-path> tab.</step>
    <step>On the <ui-path>Server-Side Analysis</ui-path> tab, click the <ui-path>Try Locally</ui-path> button.</step>
    <step>In the dialog that opens, expand the <ui-path>Advanced configuration</ui-path> section and specify the path to the baseline file, and then click <ui-path>Run</ui-path>.</step>
</procedure>

#### GitHub Actions
{id="dotnet-enable-baseline-github"}

This snippet contains the `args: --baseline,qodana.sarif.json` line that specifies the path to the SARIF-formatted file containing
a baseline:

<code-block lang="yaml">
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
            uses: JetBrains/qodana-action@v2024.1
            with:
              args: --baseline,qodana.sarif.json
            env:
              QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
</code-block>

#### Jenkins
{id="dotnet-enable-baseline-jenkins"}

The `stages` block contains the `--baseline <path/to/qodana.sarif.json>` line that specifies
the path to the SARIF-formatted file containg information about a baseline:

```groovy
pipeline {
    environment {
        QODANA_TOKEN=credentials('qodana-token')
    }
    agent {
        docker {
            args '''
              -v "${WORKSPACE}":/data/project
              --entrypoint=""
              '''
            image '%qd-image%'
        }
    }
    stages {
        stage('Qodana') {
            steps {
                sh '''
                qodana \
                --baseline <path/to/qodana.sarif.json>
                '''
            }
        }
    }
}
```

#### GitLab CI/CD
{id="dotnet-enable-baseline-gitlab"}

You can use the  `--baseline <path/to/qodana.sarif.json>` line in the `script` block to
invoke the baseline feature.

```yaml
qodana:
   image:
      name: jetbrains/qodana-<linter>
      entrypoint: [""]
   cache:
      - key: qodana-2024.1-$CI_DEFAULT_BRANCH-$CI_COMMIT_REF_SLUG
        fallback_keys:
           - qodana-2024.1-$CI_DEFAULT_BRANCH-
           - qodana-2024.1-
        paths:
           - .qodana/cache
   variables:
      QODANA_TOKEN: $qodana_token           - 
   script:
      - qodana --baseline <path/to/qodana.sarif.json> --results-dir=$CI_PROJECT_DIR/.qodana/results
         --cache-dir=$CI_PROJECT_DIR/.qodana/cache
   artifacts:
      paths:
         - qodana/report/
      expose_as: 'Qodana report'
```


#### Local run
{id="dotnet-enable-baseline-local-run"}

In these snippets, the `--baseline` option configures the path to the SARIF-formatted file containing a baseline:

<code-block lang="shell" prompt="$">
    docker run \
       -v &lt;source-directory&gt;/:/data/project/ \
       -v &lt;path_to_baseline&gt;:/data/base/ \
       -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
       %qd-image% \
       --baseline /data/base/qodana.sarif.json
</code-block>


### Enable the quality gate

You can configure [quality gates](quality-gate.topic) for the total number of project problems, specific problem severities, and code
coverage by saving this snippet to the [`qodana.yaml`](qodana-yaml.md) file:

```yaml
failureConditions:
  severityThresholds:
    any: 50 # Total number of problems in all severities
    critical: 1 # Severities
    high: 2
    moderate: 3
    low: 4
    info: 5
  testCoverageThresholds:
    fresh: 6 # Fresh code coverage
    total: 7 # Total percentage
```

### Analyze pull requests

#### GitHub Actions
{id="dotnet-pull-requests-github"}

In GitHub Actions, `--diff-start` can be omitted because it will be added automatically while running
%product%, so you can follow this procedure:
<procedure>
<step>On the <ui-path>Settings</ui-path> tab of the GitHub UI, create the <code>QODANA_TOKEN</code>
<a href="https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository">encrypted secret</a>
and save the <a href="cloud-projects.topic" anchor="cloud-manage-projects">project token</a> as its value.
</step>
<step>On the <ui-path>Actions</ui-path> tab of the GitHub UI, set up a new workflow and create the
<code>.github/workflows/code_quality.yml</code> file.</step>
<step><p>Add this snippet to the <code>.github/workflows/code_quality.yml</code> file:</p>
<code-block lang="yaml">
&nbsp;&nbsp;&nbsp;&nbsp;name: Qodana
&nbsp;&nbsp;&nbsp;&nbsp;on:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;workflow_dispatch:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pull_request:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;push:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;branches: # Specify your branches here
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- main # The 'main' branch
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 'releases/*' # The release branches
&nbsp;&nbsp;&nbsp;&nbsp;jobs:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qodana:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;runs-on: ubuntu-latest
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;permissions:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;contents: write
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pull-requests: write
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;checks: write
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;steps:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- uses: actions/checkout@v3
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;with:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ref: ${{ github.event.pull_request.head.sha }}  # to check out the actual pull request commit, not the merge commit
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fetch-depth: 0  # a full history is required for pull request analysis
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name: 'Qodana Scan'
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uses: JetBrains/qodana-action@v2024.1
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;env:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
</code-block>
</step>
</procedure>


#### GitLab CI/CD
{id="dotnet-pull-requests-gitlab"}

In the root directory of your project, save the `.gitlab-ci.yml` file containing the following snippet:

<code-block lang="yaml">
            qodana:
   image:
      name: %qd-image%
      entrypoint: [""]
   cache:
      - key: qodana-2024.1-$CI_DEFAULT_BRANCH-$CI_COMMIT_REF_SLUG
        fallback_keys:
           - qodana-2024.1-$CI_DEFAULT_BRANCH-
           - qodana-2024.1-
        paths:
           - .qodana/cache
   variables:
      QODANA_TOKEN: $qodana_token
    script:
      - >
        qodana --diff-start=$CI_MERGE_REQUEST_TARGET_BRANCH_SHA \
          --results-dir=$CI_PROJECT_DIR/.qodana/results \
          --cache-dir=$CI_PROJECT_DIR/.qodana/cache
   artifacts:
      paths:
         - .qodana/results
      expose_as: 'Qodana report'
</code-block>

Here, the `--diff-start` option specifies a hash of the commit that will act as a base for comparison.

#### Local run
{id="dotnet-pull-requests-local-run"}

To analyze changes in your code, employ the `--diff-start` option and specify a hash of the commit that will act as a
base for comparison:

<code-block lang="shell" prompt="$">
    docker run \
    &nbsp;&nbsp;&nbsp;-v $(pwd):/data/project/ \
    &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
    &nbsp;&nbsp;&nbsp;%qd-image% \
    &nbsp;&nbsp;&nbsp;--diff-start=&lt;GIT_START_HASH&gt;
</code-block>

## Supported technologies and features
{id="dotnet-feature-matrix"}

<table style="none">
    <tr>
        <td>Programming languages</td>
        <td>
            <p>C#</p>
            <p>C</p>
            <p>C++</p>
            <p>JavaScript</p>
            <p>TypeScript</p>
            <p>VB.NET</p>
        </td>
    </tr>
    <tr>
        <td>Frameworks and libraries</td>
        <td>
            <p>.NET Framework</p>
            <p>.NET Core</p>
            <p>Handlebars/Mustache</p>
            <p>Less</p>
            <p>Node.JS</p>
            <p>NUnit</p>
            <p>Pug/Jade</p>
            <p>Sass/SCSS</p>
            <p>Unity</p>
            <p>Unreal Engine</p>
            <p>Vue</p>
            <p>Xunit</p>
        </td>
    </tr>
        <tr>
        <td>Databases and ORM</td>
        <td>
            <p>MongoJS</p>
            <p>MySQL</p>
            <p>Oracle</p>
            <p>PostgreSQL</p>
            <p>SQL</p>
            <p>SQL server</p>
        </td>
    </tr>
    <tr>
        <td>Markup languages</td>
        <td>
            <p>CSS</p>
            <p>HTML</p>
            <p>JSON and JSON5</p>
            <p>RELAX NG</p>
            <p>T4</p>
            <p>XML</p>
            <p>XPath</p>
            <p>XSLT</p>
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
        <td>Build management</td>
        <td>
            <p>MSBuild</p>
        </td>
    </tr>
</table>

<table filter="cdnet">
    <tr>
        <td>Feature</td>
        <td>Available under the license</td>
    </tr>
    <tr>
        <td><a href="baseline.topic"/></td>
        <td>Community</td>
    </tr>
    <tr>
        <td><a href="quality-gate.topic"/></td>
        <td>Community</td>
    </tr>
</table>

Here, C and C++ inspections are applicable for projects containing `.sln` files.
