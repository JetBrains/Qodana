[//]: # (title: Qodana Community for .NET)

<var name="dotsettings" value="https://www.jetbrains.com/help/resharper/Sharing_Configuration_Options.html#solution-team-shared-layer"/>
<var name="linter" value="Qodana Community for .NET"/>
<var name="ide" value="ReSharper"/>
<var name="docker-image" value="jetbrains/qodana-cdnet:2023.3-eap"/>
<var name="config-file" value="qodana-cdnet-docker-readme.xml"/>

%linter% is a community linter based on [%ide%](https://www.jetbrains.com/rider/) and provides static analysis for .NET projects.
It brings all the smarts from ReSharper, which help you:

* Detect anomalous code and probable bugs
* Eliminate dead code
* Highlight spelling problems
* Improve overall code structure
* Introduce coding best practices
* Upload inspection results to [Qodana Cloud](cloud-about.xml)

%linter% provides inspections for the C, C++, C# and VB.NET programming languages.
C and C++ inspections of %linter% are limited by projects containing `.sln` solution files or `.csproj` project files.

## Supported features

<include src="lib_qd.xml" include-id="linters-supported-features" use-filter="empty,cdnet"/>

## Analyze a project locally

### Prepare the project

Because %linter% is licensed under the Community [license](pricing.md), it requires the
Qodana Cloud [project token](project-token.md).  

Docker should also be up and running on the machine. 

<include src="lib_qd.xml" include-id="docker-dotnet-specific-solution-project" use-filter="empty,cdnet"/>

The %linter% does not support inspection configuration using the [`qodana.yaml`](qodana-yaml.md) file.
You can use `.editorconfig` and [`.DotSettings`](%dotsettings%) files for these purposes. Besides that, %linter% supports Roslyn analyzers, 
with each analyzer considered as a separate inspection. You can configure Roslyn analyzers using the `.editorconfig` 
files. This is an experimental feature, so use them at your own risk.

### Build the project

When %linter% starts, it builds your project. If the project build fails, code analysis cannot be performed.

If you wish to run your custom build, use the `--no-build` option while running the linter: 

```shell
docker run \
   -v &lt;source-directory&gt;/:/data/project/ \
   -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
   %docker-image% \
   --no-build
```
{prompt="$"}

In this case, in the [`bootstrap`](before-running-qodana.md) section of the [`qodana.yaml`](qodana-yaml.md) file you can specify how to build 
your project, or run the build in a pipeline before passing it to %product%.

### Run the linter

Use this command to run the Dockerized version of the %linter% linter: 

```shell
docker run \
   -v &lt;source-directory&gt;/:/data/project/ \
   -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
   %docker-image%
```
{prompt="$"}

Here,  the `QODANA_TOKEN` variable specifies the [project token](project-token.md). After %product% finishes inspecting
your code, you can open [Qodana Cloud](https://qodana.cloud) to see the inspection report.

## Next steps

<include src="lib_qd.xml" include-id="linter-next-steps-footer" use-filter="empty"/>