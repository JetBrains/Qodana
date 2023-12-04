[//]: # (title: Qodana Community for .NET)

<!-- What technologies does this linter support ?? -->

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
C and C++ inspections of %linter% are limited by projects containing `.sln` files. 

## Supported features

<include src="lib_qd.xml" include-id="linters-supported-features" use-filter="empty,cdnet"/>

## Analyze a project locally

### Install project dependencies

%linter% requires the following software to be accessible by it: 

* Java 11 version or later
* .NET SDK version 7 or later

These executables should be accessible using the `PATH` variable of your operating system. 

Using the [`bootstrap`](before-running-qodana.md) field in the `qodana.yaml` file, you can install the required packages. 

Although %linter% is licensed under the Community [license](pricing.md), it requires the 
[%product% Cloud token](cloud-onboarding.md). 

## Run analysis

<!-- This needs to be reviewed -->
<!-- Does this linter support default profiles?-->
<!-- The relative path to solutions needs to be explained in details -->

### Configure the project

<include src="lib_qd.xml" include-id="docker-dotnet-specific-solution-project" use-filter="empty"/>

The %linter% does not support configuring inspections using the [`qodana.yaml`](qodana-yaml.md) file.
You can use `EditorConfig` and `*.DotSettings` files for these purposes. Besides that, %linter% supports Roslyn analyzers, 
with each analyzer considered as a separate inspection. You can configure Roslyn analyzers using the `EditorConfig` 
files. This is an experimental feature, so use them at your own risk.

### Build the project

When %linter% starts, it builds your project. If the project build fails, code analysis cannot be performed.

If you wish to run your custom build, use the `--no-build` option while running the linter: 

<!-- Where to place the --no-build option: qodana.yaml or CLI? -->
<!-- The no-build option needs to be added in the documentation -->

```shell
    qodana scan \
       -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
       --no-build
```

In this case, in the [`bootstrap`](before-running-qodana.md) section of the [`qodana.yaml`](qodana-yaml.md) file you can specify how to build 
your project.

## Run the linter

<p><include src="lib_qd.xml" include-id="qodana-cli-quickstart" use-filter="non-gs,other,empty,non-php"/></p>


## Next steps

<include src="lib_qd.xml" include-id="linter-next-steps-footer" use-filter="empty"/>