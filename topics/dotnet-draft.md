[//]: # (title: .NET)

<no-index/>

<show-structure for="chapter" depth="3"/>

<var name="qp" value="Qodana for .NET"/>
<var name="qp-co" value="Qodana Community for .NET"/>
<var name="qp-linter" value="jetbrains/qodana-dotnet:2024.1"/>
<var name="qp-co-linter" value="jetbrains/qodana-cdnet:2024.1-eap"/>
<var name="qd-image" value="jetbrains/qodana-dotnet/cdnet:2024.1<-eap>"/>
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

### Prepare a solution

By default, %product% tries to locate and employ a single solution file, or, if no solution file is present,
it tries to find a project file. If your project contains multiple solution files, you need to specify the exact
filename as shown below.

#### Specify a solution

<!-- These headers can probably be removed -->

##### YAML file
{id="dotnet-specify-solution-yaml"}

Using [`qodana.yaml`](qodana-yaml.md) is the easiest method of configuring a solution. Once configured,
it can be applied across all software products without additional configuration. Specify the
relative path to the solution file from the project root:

```yaml
dotnet:
  solution: <relative-path-to-solution-file>
```

If your project contains no solution files and multiple project files, you need to employ a project file:

```yaml
dotnet:
  project: <relative-path-to-project-file>
```

##### Local run
{id="dotnet-specify-solution-local-run"}

<!-- The entire Docker command should be provided here. Or configured for GitHub and others -->

Here are the example Docker commands:

<tabs>
<tab title="%qp%">
<code-block lang="shell">
--property=qodana.net.solution=&lt;relative-path-to-solution-file&gt;
</code-block>
</tab>
<tab title="%qp-co%">
<code-block lang="shell">
--solution=&lt;relative-path-to-solution-file&gt;
</code-block>
</tab>
</tabs>

If your project contains no solution files and multiple project files, you need to employ a project file:

<!-- The entire Docker command should be provided here. Or configured for GitHub and others -->

<tabs>
<tab title="%qp%">
<code-block lang="shell">
--property=qodana.net.project=&lt;relative-path-to-project-file&gt;
</code-block>
</tab>
<tab title="%qp-co%">
<code-block lang="shell">
--project=&lt;relative-path-to-project-file&gt;
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

##### Local run
{id="dotnet-configure-solution-local-run"}

You can configure a solution using the `--configuration` option:

<tabs>
<tab title="%qp%">
<code-block lang="shell">
--property=qodana.net.configuration=Release
</code-block>
</tab>
<tab title="%qp-co%">
<code-block lang="shell">
--configuration=Release
</code-block>
</tab>
</tabs>


By default, the solution platform is set to `Any CPU`, and you can override it using the `--platform` option:

<tabs>
<tab title="%qp%">
<code-block lang="shell">
--property=qodana.net.platform=x86
</code-block>
</tab>
<tab title="%qp-co%">
<code-block lang="shell">
--platform=x86
</code-block>
</tab>
</tabs>

### Configure inspections

<!-- This needs to be extended from the Deployment section -->

The %qp-co% linter does not support inspection configuration using the [`qodana.yaml`](qodana-yaml.md) file.
You can use `.editorconfig` and [`.DotSettings`](%dotsettings%) files for these purposes. Besides that, %product% supports Roslyn analyzers,
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

Another configuration example is available [on GitHub](https://github.com/hybloid/fluentassertions/blob/develop/qodana.yaml).

<!-- Does the Qodana for .NET  linter let configure using qodana.yaml? -->


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


<!-- Explore analysis results -->
<!-- Extend the configuration -->
<!-- The baseline feature needs to be added here -->
<!-- The quality gate feature needs to be added here -->
<!-- Analyzing pull requests needs to be added here -->

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
