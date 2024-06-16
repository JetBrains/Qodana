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
.NET projects, you can use the following %product% linters:

* %qp% is based on Rider, licensed under the Ultimate and
  Ultimate Plus [licenses](pricing.md), and available as a native solution and the `%qp-linter%` Docker image,
* %qp-co% is based on ReSharper, licensed under the Community license, and available as the `%qp-co-linter%` Docker image.

You can compare these linters by navigating to the [](#dotnet-feature-matrix) section.

## Before your start
{id="dotnet-before-you-start"}

### Qodana Cloud
{id="dotnet-before-you-start-qodana-cloud"}

To run linters, you need to obtain a [project token](project-token.md) that
will be used by %product% for identifying and verifying a license. 

Navigate to [Qodana Cloud](https://qodana.cloud) and create an [account](cloud-quickstart.md) there.

In Qodana Cloud, create an [organization](cloud-organizations.topic), a [team](cloud-teams.topic), and a 
[project](cloud-projects.topic).

On the [project card](cloud-projects.topic#cloud-manage-projects), you can find the project token that you will be using
in this section.

### SDK version
{id="dotnet-sdk-version"}

<!-- Is this available only for the Qodana for .NET linter? -->

The Dockerized version of %qp% provides the following SDK versions:

* 6.0.417,
* 7.0.404,
* 8.0.100.

All SDK versions are stored in the `/usr/share/dotnet/sdk` directory of the %product% container filesystem.

In case a project requires a different version of the SDK, you can set it using the
[`bootstrap`](before-running-qodana.md) key in the `qodana.yaml` file.
For example, this command will install the required version of the SDK that is specified in the
`global.json` file and located in the root of your project:

<code-block lang="yaml">
    bootstrap: curl -fsSL https://dot.net/v1/dotnet-install.sh |
      bash -s -- --jsonfile /data/project/global.json -i /usr/share/dotnet
</code-block>

## Build the project
{id="dotnet-build-project"}

During the start, %product% builds your project. If the project build fails, code analysis cannot be performed. 
You can configure the project build using the [`bootstrap`](before-running-qodana.md) key of the [`qodana.yaml`](qodana-yaml.md) file contained in your 
project directory.

<!-- The bootstrap command examples should be provided here -->

Alternatively, you can build your project in a pipeline before %product% starts.

If you wish to run your custom build, use the `--no-build` option:

```shell
docker run \
   -v <source-directory>/:/data/project/ \
   -e QODANA_TOKEN="<cloud-project-token>" \
   %qd-image% \
   --no-build
```
{prompt="$"}

This is the GitHub Actions configuration sample invoking the `--no-build` option:

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
                args: --no-build
            env:
              QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
</code-block>

## Run %product%
{id="dotnet-run-qodana"}

<include from="lib_qd.topic" element-id="root-and-non-root-users-info-bubble"></include>

You can run the %qp% linter either in the [native mode](#dotnet-run-qodana-native-mode) (recommended) or using the 
linter in a [container mode](#dotnet-run-qodana-container-mode). 

You can run the %qp-co% linter in a [container mode](#dotnet-run-qodana-container-mode).

> Before running %product%, you need to [prepare](#dotnet-before-you-start) and [build](#dotnet-build-project) your project.
{style="note"}

### Native mode
{id="dotnet-run-qodana-native-mode"}

The [native mode](native-mode.md) is the recommended method for running the %qp% linter that lets you run the linter 
without using Docker containers. 

> If you plan to use private NuGet feeds, we recommend running the native mode on the same machine where
you build a project because this can guarantee that %instance% has access to private NuGet feeds.
{style="note"}

#### YAML file
{id="dotnet-run-qodana-native-yaml"}

Using the YAML configuration is the preferred method of configuring the linter because it lets you use such configuration
across all software that runs %product% without additional configuration.

You can configure the native mode by adding this line to the [`qodana.yaml`](qodana-yaml.md) file:

```yaml
ide: QDNET
```


#### JetBrains IDEs
{id="dotnet-run-qodana-native-mode-ides"}

You can run %instance% in %ide% and forward inspection reports to [Qodana Cloud](cloud-about.topic) for storage and analysis purposes.

<procedure>
<step>
   <p>In %ide%, navigate to <ui-path>Tools | Qodana | Try Code Analysis with Qodana</ui-path>.</p> 
</step>
<step>
   <p>On the <ui-path>Run Qodana</ui-path> dialog, you can configure:</p>
      <list>
        <li>Options used by %product% and configured by the <a href="qodana-yaml.md"><code>qodana.yaml</code></a> file. 
          You can see that the native mode is already configured.</li>
         <li>The <a href="cloud-forward-reports.topic"><ui-path>Send inspection results to Qodana Cloud</ui-path></a> option using a <a href="cloud-projects.topic" anchor="cloud-manage-projects">project token</a>.</li>
         <li>The <a href="baseline.topic"><ui-path>Use Qodana analysis baseline</ui-path></a> option to run %product% with a baseline.</li>
      </list>
   <img src="ide-plugin-dotnet-run-qodana.png" width="793" alt="Configuring Qodana in the Run Qodana dialog" border-effect="line"/>
    <p>Click <ui-path>Run</ui-path> for analyzing your code.</p>
</step>
<step>
   <p>In the <ui-path>Server-Side Analysis</ui-path> tool window, see the <a href="qodana-ide-plugin.md" anchor="ide-plugin-study-reports">inspection results</a>.</p>
</step>
</procedure>

#### GitHub Actions
{id="dotnet-run-qodana-native-mode-github"}

<!-- This should refer to the normal GitHub section -->

If you have already configured the [`qodana.yaml`](#dotnet-run-qodana-native-yaml) file, you can skip this and navigate 
to the [GitHub Actions](#dotnet-run-qodana-container-mode-github) section below.

You can run %product% using the [Qodana Scan GitHub action](https://github.com/marketplace/actions/qodana-scan) as shown
below.

<procedure>
    <step>On the <ui-path>Settings</ui-path> tab of the GitHub UI, create the <code>QODANA_TOKEN</code>
        <a href="https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository">encrypted secret</a>
        and save the <a href="cloud-projects.topic" anchor="cloud-manage-projects">project token</a> as its value.
    </step>
    <step>On the <ui-path>Actions</ui-path> tab of the GitHub UI, set up a new workflow and create the
        <code>.github/workflows/code_quality.yml</code> file.</step>
    <step>To inspect the <code>main</code> branch, release branches and the pull requests coming
    to your repository in the native mode, save this workflow configuration to the <code>.github/workflows/code_quality.yml</code> file:
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
                        args: --ide,QDNET
                    env:
                      QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
        </code-block>
      <p>This configuration invokes the native mode using:</p>
          <code-block lang="yaml">
             with:
             &nbsp;&nbsp;&nbsp;args: --ide,QDNET
          </code-block>
    </step>
</procedure>

#### Local run
{id="dotnet-run-qodana-native-mode-local-run"}

Assuming that you have already installed [Qodana CLI](https://github.com/JetBrains/qodana-cli/releases/latest) on your
machine, you can run this command in the project root directory:

```Shell
qodana scan \
   --ide QDNET
```
{prompt="$"}

Here, the `--ide` option downloads and employs the JetBrains IDE binary file.

Alternatively, in the `qodana.yaml` file save `ide: QDNET`, and then run %instance% using the
following command:

```Shell
qodana scan
```
{prompt="$"}


### Container mode
{id="dotnet-run-qodana-container-mode"}

The container mode is available for the %qp% and %qp-co% linters. For the %qp% linter, the 
[native mode](#dotnet-run-qodana-native-mode) is the recommended method.

For the %qp-co% linter, only the container mode is available.

#### GitHub Actions
{id="dotnet-run-qodana-container-mode-github"}

You can run %product% using the [Qodana Scan GitHub action](https://github.com/marketplace/actions/qodana-scan) as shown
below.

<procedure>
    <step>On the <ui-path>Settings</ui-path> tab of the GitHub UI, create the <code>QODANA_TOKEN</code>
        <a href="https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository">encrypted secret</a>
        and save the <a href="cloud-projects.topic" anchor="cloud-manage-projects">project token</a> as its value.
    </step>
    <step>On the <ui-path>Actions</ui-path> tab of the GitHub UI, set up a new workflow and create the
        <code>.github/workflows/code_quality.yml</code> file.</step>
    <step>To analyze the <code>main</code> branch, release branches and the pull requests coming
    to your repository in the container mode, save this workflow configuration to the <code>.github/workflows/code_quality.yml</code> file:
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
                    env:
                      QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
        </code-block>
    </step>
</procedure>


#### Local run
{id="dotnet-run-qodana-container-mode-local-run"}

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
&nbsp;&nbsp;&nbsp;%qd-image%
</code-block>
<p>Open <a href="https://qodana.cloud">Qodana Cloud</a> in your browser to examine analysis results.</p>

### Analyze a specific solution

By default, %product% tries to locate and employ a single solution file, or, if no solution file is present,
it tries to find a project file. If your project contains multiple solution files, you need to specify the exact
filename as shown below.

#### Specify a solution

You can specify a solution in various ways. Using a [`YAML configuration`](#dotnet-specify-solution-yaml) is the most
convenient method because you can configure it once and use the configuration across all software that runs %product%.

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

The %qp% linter uses the `--property` option, while the %qp-co% linter uses the `--solution` option to specify a path to
a solution file:

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

If your project contains no solution files and multiple project files, you need to employ a project file using the
`--property` and `--project` options:

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

Every solution contains the `Debug` and `Release` configurations that you can employ as shown below.

##### YAML file
{id="dotnet-configure-solution-yaml"}

You can switch configurations of the current solution in the `qodana.yaml` file:

```yaml
dotnet:
  configuration: Release
```

By default, the solution platform is set to `Any CPU`, and you can override it, for example:

```yaml
dotnet:
  platform: x86
```
<!-- Do I need to add GitHub config example here? -->

##### Docker
{id="dotnet-configure-solution-local-run"}

You can apply a configuration using the `--property` and `--configuration` options:

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

By default, the solution platform is set to `Any CPU`, and you can override it as shown below:

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


### Private NuGet repositories

You can run %qp% using private NuGet feeds. The linter does not support authentication for private NuGet repositories using, for 
example, Windows Authentication. To overcome this limitation, you can place all required packages within the %instance% 
cache as shown below:

<procedure>
    <step>In the local filesystem, create the folder that will contain cache. For example, it can be
        <code>C:/Temp/QodanaCache</code>.</step>
    <step><p>Run %instance% using the <code>--cache-dir C:/Temp/QodanaCache</code> option:</p>
      <code-block lang="shell" prompt="$">
          docker run \
          &nbsp;&nbsp;&nbsp;-v &lt;source-directory&gt;/:/data/project/ \
          &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
          &nbsp;&nbsp;&nbsp;-e QODANA_NUGET_URL=&lt;private-NuGet-feed-URL&gt; \
          &nbsp;&nbsp;&nbsp;-e QODANA_NUGET_USER=&lt;login&gt; \
          &nbsp;&nbsp;&nbsp;-e QODANA_NUGET_PASSWORD=&lt;plaintext-password&gt; \
          &nbsp;&nbsp;&nbsp;-e QODANA_NUGET_NAME=&lt;name-of-private-NuGet-feed&gt; \
          &nbsp;&nbsp;&nbsp;%qp-linter% \
          &nbsp;&nbsp;&nbsp;--cache-dir C:/Temp/QodanaCache
      </code-block>
</step>
    <step>Copy all NuGet packages contained by default in the
        <code ignore-vars="true">%userprofile%\.nuget\packages</code>
        folder to <code>C:/Temp/QodanaCache/nuget</code>. If you have a custom package folder, copy packages
        from that folder instead of <code ignore-vars="true">%userprofile%\.nuget\packages</code>.</step>
    <step>Run %instance% using the <code>--cache-dir C:/Temp/QodanaCache</code> once more.</step>
</procedure>

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
         On the <ui-path>Settings</ui-path> dialog, click <ui-path>Log in</ui-path>.
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
       <p>On the <ui-path>Server-Side Analysis</ui-path> tab of the <ui-path>Problems</ui-path> tool window, view <a href="qodana-ide-plugin.md" anchor="ide-plugin-study-reports">analysis results</a>.</p>
    </step>
</procedure>

### Qodana Cloud

Once %product% analyzed your project and uploaded the analysis results to Qodana Cloud, in
[Qodana Cloud](https://qodana.cloud) navigate to your project and review the analysis results report.

<!-- This image needs to be replaced with something from .NET -->

<img src="dotnet-report-example.png" alt="Analysis report example" width="720" border-effect="line"/>

<p>To learn more about %instance% report UI, see the <a href="ui-overview.md"/> section.</p>


## Extend the configuration
{id="dotnet-extend-configuration"}

### Adjust the scope of analysis

#### %qp%

%qp% reads configuration from the [`qodana.yaml`](qodana-yaml.md) file located in the root directory of your project. 
For example, add this configuration to run the linter using the [`qodana.recommended`](inspection-profiles.md) inspection profile:

```yaml
version: "1.0"
profile:
    name: qodana.recommended
```

You can analyze your code using Roslyn analyzers with each analyzer considered as a separate 
inspection. You can configure Roslyn analyzers as explained in the [](#dotnet-extend-configuration-editorconfig) section. 
This is an experimental feature, so use them at your own risk.

To disable Roslyn analyzers, you can [configure the %instance% profile](custom-profiles.md) using
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
reference to the existing profile by mapping the profile:

<code-block lang="shell" prompt="$">
docker run \
&nbsp;&nbsp;&nbsp;-v $(pwd):/data/project/ \
&nbsp;&nbsp;&nbsp;-v $(pwd)/.qodana/&lt;inspection-profile.xml&gt;:/data/project/myprofiles/&lt;inspection-profile.xml&gt; \
&nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
&nbsp;&nbsp;&nbsp;%qp-linter% \
&nbsp;&nbsp;&nbsp;--profile-path /data/project/myprofiles/&lt;inspection-profile.xml&gt;
</code-block>

#### %qp-co%

If you have previously worked on the target solution with ReSharper, you may have already
[configured code inspections settings](https://www.jetbrains.com/help/resharper/Code_Analysis__Configuring_Warnings.html).
If so, InspectCode will find your [custom settings](https://www.jetbrains.com/help/resharper/Sharing_Configuration_Options.html)
in `.DotSettings` files and apply them. If there are no settings files, then the default severity levels will be used
for all analyses. Besides custom severity levels for code inspections, InspectCode will look for the following settings in
`.DotSettings` files:

* Whether the solution-wide analysis is enabled.
* [Naming rules](https://www.jetbrains.com/help/resharper/Coding_Assistance__Naming_Style.html) (this can only be configured using `.DotSettings` files).
* [Files, folders, and file masks excluded from code analysis](https://www.jetbrains.com/help/resharper/Code_Analysis__Configuring_Warnings.html#exclude_items).
* [Files, file masks, and regions with generated code, where the code analysis is partly disabled](https://www.jetbrains.com/help/resharper/Code_Analysis__Configuring_Warnings.html#exclude_generated) (this can only be configured using `.DotSettings` files).
* A place where the code analysis engine should store caches. You can specify it on the **Environment | General** page of ReSharper options.
* Target languages (**ReSharper | Options | Environment | Products — Features**).

To configure InspectCode on a CI server, make all configurations locally with ReSharper, save the settings to the
[Solution Team-Shared layer](https://www.jetbrains.com/help/resharper/Sharing_Configuration_Options.html#saveTo),
and then commit the resulting `YourSolution.sln.DotSettings` file in the solution directory to your VCS. InspectCode on
the server will find and apply these settings.

By default, InspectCode also runs Roslyn analyzers on the target solution. To configure Roslyn analyzers, see the 
[](#dotnet-extend-configuration-editorconfig) section. 

To disable Roslyn analyzers, in the solution's `.DotSettings` file add the following configuration:

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

#### EditorConfig
{id="dotnet-extend-configuration-editorconfig"}

<p>If you use <a href="https://www.jetbrains.com/help/resharper/Using_EditorConfig.html">EditorConfig</a> to
    maintain code styles for your project, you can also configure code inspections from
    <code>.editorconfig</code> files.</p>

<p>As EditorConfig convention suggests, InspectCode will apply inspection settings defined in files named
    <code>.editorconfig</code> in the directory of the current file and in all its parent directories until
    it reaches the root filepath or finds an EditorConfig file with <code>root=true</code>. File masks specified in
    <code>.editorconfig</code> files, for example <code>*Test.cs</code> are also taken into account.</p>

<p>Inspection settings in <code>.editorconfig</code> files are configured similarly to other properties —
    by adding the corresponding lines:</p>

<code-block lang="shell">
    [inspection_property]=[error | warning | suggestion | hint | none]
</code-block>

<p>For example, you can change the
    <a href="https://www.jetbrains.com/help/resharper/Code_Analysis__Code_Inspections.html#severity">severity level</a>
    of the <code>Possible 'System.NullReferenceException'</code> inspection to <code>Error</code> with the
    following line:</p>

<code-block lang="shell">
    resharper_possible_null_reference_exception_highlighting=error
</code-block>

<p>or you can disable the <code>Redundant argument with default value</code> inspection with the following line:</p>

<code-block lang="shell">
    resharper_redundant_argument_default_value_highlighting=none
</code-block>

<tip>Inspection settings from <code>.editorconfig</code> files have higher priority than the settings
    configured on the <ui-path>Code Inspection | Inspection Severity</ui-path> page of InspectCode options.</tip>

<p>You can find EditorConfig property for each inspection on pages in the
    <a href="https://www.jetbrains.com/help/resharper/Reference_Code_Inspection_Index.html">Code inspection index</a>
    section as well as on the
    <a href="https://www.jetbrains.com/help/resharper/EditorConfig_Index.html">Index of EditorConfig properties</a> page. —
    just use the browser search to find the property for the desired inspection.</p>


### Enable the baseline

You can skip analysis for specific problems using the [baseline](baseline.topic) feature.

#### JetBrains IDEs
{id="dotnet-enable-baseline-ides"}

<procedure>
    <step>In your IDE, navigate to the <ui-path>Problems</ui-path> tool window. </step>
    <step>In the <ui-path>Problems</ui-path> tool window, click the <ui-path>Server-Side Analysis</ui-path> tab.</step>
    <step>On the <ui-path>Server-Side Analysis</ui-path> tab, click the <ui-path>Try Locally</ui-path> button.</step>
    <step>On the dialog that opens, expand the <ui-path>Advanced configuration</ui-path> section and specify the path to the baseline file, and then click <ui-path>Run</ui-path>.</step>
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

Because the [Qodana Scan GitHub action](https://github.com/marketplace/actions/qodana-scan) automatically analyzes all pull requests, you can use 
[this configuration](#dotnet-run-qodana-container-mode-github).

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

## Usage statistics

According to the [JetBrains EAP user
agreement](https://www.jetbrains.com/legal/agreements/user_eap.html), we can use third-party services to analyze the 
usage of our features to further improve the user experience. All data will be collected 
[anonymously](https://www.jetbrains.com/company/privacy.html). You can disable statistics by using the 
`--no-statistics=true` CLI option, for example:

```Shell
docker run \
   -v <source-directory>/:/data/project/ \
   -e QODANA_TOKEN="<cloud-project-token>" \
   %qd-image% \
   --no-statistics=true
```

## Supported technologies and features
{id="dotnet-feature-matrix"}

<!-- These need to be compared for both linters because now it's not clear what is what -->

<link-summary>Comparison matrix of the .NET linters.</link-summary>

<table>
    <tr>
      <td>Support for</td>
      <td>Name</td>
      <td>%qp%</td>
      <td>%qp-co%</td>
    </tr>
    <tr>
        <td>Programming languages</td>
        <td>
            <p>C#</p>
            <p>C++ <b>*</b></p>
            <p>VB.NET <b>**</b></p>
            <p>C <b>*</b></p>
            <p>JavaScript</p>
            <p>TypeScript</p>
        </td>
        <td>
            <p>&#x2714; All from the list</p>
        </td>
        <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x274c;</p>
            <p>&#x274c;</p>
            <p>&#x274c;</p>
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
        <td>
            <p>&#x2714; All from the list</p>
        </td>
        <td>
            <p>&#x274c; None</p>
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
       <td>
            <p>&#x2714; All from the list</p>
        </td>
        <td>
            <p>&#x274c; None</p>
        </td>
    </tr>
    <tr>
        <td>Markup languages</td>
        <td>
            <p>HTML</p>
            <p>XML</p>
            <p>CSS</p>
            <p>JSON and JSON5</p>
            <p>RELAX NG</p>
            <p>T4</p>
            <p>XPath</p>
            <p>XSLT</p>
            <p>YAML</p>
        </td>
        <td>
            <p>&#x2714; All from the list</p>
        </td>
        <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x274c;</p>
            <p>&#x274c;</p>
            <p>&#x274c;</p>
            <p>&#x274c;</p>
            <p>&#x274c;</p>
            <p>&#x274c;</p>
            <p>&#x274c;</p>
        </td>
    </tr>
    <tr>
        <td>Scripting languages</td>
        <td>
            <p>Shell script</p>
        </td>
       <td>
            <p>&#x2714;</p>
        </td>
        <td>
            <p>&#x274c;</p>
        </td>
    </tr>
    <tr>
        <td>Build management</td>
        <td>
            <p>MSBuild</p>
        </td>
       <td>
            <p>&#x2714;</p>
        </td>
        <td>
            <p>&#x274c;</p>
        </td>
    </tr>
    <tr>
      <td>%product% features</td>
      <td>
        <p><a href="baseline.topic">Baseline</a></p>
        <p><a href="quality-gate.topic">Quality gate</a></p>
        <p><a href="code-coverage.md">Code coverage</a></p>
        <p><a href="license-audit.topic">License audit</a></p>
      </td>
      <td>
            <p>&#x2714; All from the list</p>
      </td>
      <td>
         <p>&#x2714;</p>
         <p>&#x2714;</p>
         <p>&#x274c;</p>
         <p>&#x274c;</p>
      </td>
    </tr>
</table>

\* C and C++ inspections are applicable for projects containing `.sln` files.

** Supports Visual Basic inspections  only.
