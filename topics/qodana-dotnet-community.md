[//]: # (title: Qodana Community for .NET)

<var name="dotsettings" value="https://www.jetbrains.com/help/resharper/Sharing_Configuration_Options.html#solution-team-shared-layer"/>
<var name="linter" value="Qodana Community for .NET"/>
<var name="ide" value="ReSharper"/>
<var name="docker-image" value="jetbrains/qodana-cdnet:2023.3-eap"/>
<var name="config-file" value="qodana-cdnet-docker-readme.xml"/>

<note>%linter% is currently in the Early Access, which means it may be not reliable, work not as intended, and contain errors.
Any use of the EAP product is at your own risk. Your feedback is very welcome in our
<a href="https://youtrack.jetbrains.com/newIssue?project=QD">issue tracker</a> or at
<a href="mailto:qodana-support@jetbrains.com">qodana-support@jetbrains.com</a>.
</note>

%linter% is a community linter based on [%ide%](https://www.jetbrains.com/rider/) and provides static analysis for .NET projects.
It brings all the smarts from ReSharper, which helps you:

* Detect anomalous code and probable bugs
* Eliminate dead code
* Highlight spelling problems
* Improve overall code structure
* Introduce coding best practices
* Upload inspection results to [Qodana Cloud](cloud-about.xml)

<note>This linter requires the Qodana Cloud <a href="project-token.md">project token</a>.</note>

%linter% lets you inspect .NET Core projects that use the C# and Visual Basic.NET (VB.NET) languages. 
It also supports C/C++ inspections for projects containing `.sln` solution files.

## Supported technologies

<table header-style="none">
    <tr>
        <td>Programming languages</td>
        <td>
            <p>C#</p>
            <p>C</p>
            <p>C++</p>
        </td>
    </tr>
    <tr>
        <td>Markup languages</td>
        <td>
            <p>XML</p>
        </td>
    </tr>
    <tr>
        <td>Frameworks and libraries</td>
        <td>
            <p>.NET Core</p>
            <p>EntityFramework</p>
            <p>Unreal Engine</p>
        </td>
    </tr>
</table>

## Supported features

<include src="lib_qd.xml" include-id="linters-supported-features" use-filter="empty,cdnet"/>

## Analyze a project locally

### Prepare the project

If you plan to run %linter% on a local machine, make sure that Docker on this machine is up and running. 

By default, %product% tries to locate and employ a single solution file, or, if no solution file is present,
it tries to find a project file. If your project contains multiple solution files, you need to specify the exact
filename using the `--solution` option and a relative path to a solution file. For example, to
make %product% always analyze the `MySolution.sln` solution file, you can use:

%linter% requires the relative path to a solution or a project file from the repository root. 

You can configure it in the `qodana.yaml` file:

```yaml
dotnet:
  solution: <relative-path-to-solution-file>
```

Alternatively, you can do it using the `--solution` option:

```shell
--solution=<relative-path-to-solution-file>
```

If your project contains no solution files and multiple project files, you need to use the `--project` option and a 
relative path to a project file. For example, for the `MyProject.csproj` project file, you can save the following 
configuration to the `qodana.yaml` file:

```yaml
dotnet:
  project: MyProject.csproj
```

Alternatively, you can do it using the `--project` option:

```shell
--project=MyProject.csproj
```

The %linter% does not support inspection configuration using the [`qodana.yaml`](qodana-yaml.md) file.
You can use `.editorconfig` and [`.DotSettings`](%dotsettings%) files for these purposes. Besides that, %linter% supports Roslyn analyzers,
with each analyzer considered as a separate inspection. You can configure Roslyn analyzers using the `.editorconfig`
files. This is an experimental feature, so use them at your own risk.

#### Configure a solution

A solution configuration defines which projects in the solution to build, and which project configurations to use for 
specific projects within the solution.

Each newly created solution includes the `Debug` and `Release` configurations, which can be complemented by your custom 
configurations.

You can switch configurations of the current solution in the `qodana.yaml` file:

```yaml
dotnet:
  configuration: Release
```

Alternatively, you can do it using the `--property` option:

```shell
--property=qodana.net.configuration=Release
```

By default, the solution platform is set to `Any CPU`, and you can override it in the `qodana.yaml` file:

```yaml
dotnet:
  platform: x86
```

Alternatively, you can do it using the `--property` option:

```shell
--property=qodana.net.platform=x86
```

### Build the project

When %linter% starts, it builds your project. If the project build fails, code analysis cannot be performed.

If you wish to run your custom build, use the `--no-build` option while running the linter: 

```shell
docker run \
   -v <source-directory>/:/data/project/ \
   -e QODANA_TOKEN="<cloud-project-token>" \
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
   -v <source-directory>/:/data/project/ \
   -e QODANA_TOKEN="<cloud-project-token>" \
   %docker-image%
```
{prompt="$"}

Here, the `QODANA_TOKEN` variable specifies the [project token](project-token.md). After %product% finishes inspecting
your code, you can open [Qodana Cloud](https://qodana.cloud) to see the inspection report.

## Next steps

<include src="lib_qd.xml" include-id="linter-next-steps-footer" use-filter="empty"/>