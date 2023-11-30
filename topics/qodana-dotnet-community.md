[//]: # (title: Qodana Community for .NET)

<!-- What technologies does this linter support ?? -->

<var name="linter" value="Qodana Community for .NET"/>
<var name="ide" value="ReSharper"/>
<var name="docker-image" value="jetbrains/qodana-cdnet:2023.3"/>
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

## Supported technologies

<!-- This needs to be checked by downloading the SARIF file -->

%linter% provides inspections for the following technologies.

<table header-style="none">
    <tr>
        <td>Programming languages</td>
        <td>
            <p>C#</p>
            <p>C</p>
            <p>C++</p>
            <p>VB.NET</p>
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
        <td>Build management</td>
        <td>
            <p>MSBuild</p>
        </td>
    </tr>
    <tr>
        <td>Frameworks and libraries</td>
        <td>
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
</table>

Here, C and C++ inspections are applicable for projects containing `.sln` files.

## Supported features

<include src="lib_qd.xml" include-id="linters-supported-features" use-filter="empty,cdnet"/>

## Prerequisites

The %linter% linter requires the following software to be accessible by it: 

* Java 11 version or later
* .NET SDK version 7 or later

These executables should be accessible using the path variables of your operating system. 

Using the [`bootstrap`](before-running-qodana.md) option, you can install the required packages. 

Although %linter% is a Community-licensed linter, it requires the [%product% Cloud token](cloud-onboarding.md). 

## Configure the linter

<!-- This needs to be reviewed -->

<p><include src="lib_qd.xml" include-id="docker-dotnet-specific-solution-project"/></p>

When %linter% starts, it builds your project. If the project build fails, code analysis cannot be performed.

If you wish to run your custom build, use the `--no-build` option while running the linter: 

<!-- Where to place the --no-build option -->

```shell
    qodana scan \
       -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
       --no-build
```


In the [`bootstrap`](before-running-qodana.md) section of the [`qodana.yaml`](qodana-yaml.md) file, you can build your
project.

<!-- This needs to be moved to the lib_qd.xml chunk -->

<note>Here, you need to provide the relative path to the solution file.</note>

## Run analysis

<p><include src="lib_qd.xml" include-id="qodana-cli-quickstart" use-filter="non-gs,other,empty,non-php"/></p>


<note>The %linter% does not support configuring inspections using the 
<a href="qodana-yaml.md"><code>qodana.yaml</code></a> file. 
You can use <code>EditorConfig</code> and <code>*.DotSettings</code> files to configure code analysis.</note>