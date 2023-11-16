[//]: # (title: Qodana for .NET)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<img src="dotnet-linter.png" dark-src="dotnet-linter_dark.png" alt="Qodana for .NET linter languages" width="296"/>

<var name="linter" value="Qodana for .NET"/>
<var name="ide" value="Rider"/>
<var name="docker-image" value="jetbrains/qodana-dotnet:2023.2"/>
<var name="config-file" value="qodana-dotnet-docker-readme.xml"/>

%linter% is based on [%ide%](https://www.jetbrains.com/rider/) and provides static analysis for .NET projects.
It brings all the smarts from Rider, which help you:

* Detect anomalous code and probable bugs
* Eliminate dead code
* Highlight spelling problems
* Improve overall code structure
* Introduce coding best practices
* Upload inspection results to [Qodana Cloud](cloud-about.xml)

%linter% provides inspections for the C, C++, C#, VB.NET, JavaScript, and TypeScript programming languages.
C and C++ inspections of %linter% are limited by projects containing `.sln` files. 

## Supported technologies

%linter% provides inspections for the following technologies.

<table header-style="none">
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

<include src="lib_qd.xml" include-id="linters-supported-features" use-filter="empty,dotnet"/>

## Analyze a project locally

### Install project dependencies


%linter% is suitable for analyzing .NET Core projects and provides the following SDK versions:

* 3.0.103
* 6.0.405
* 7.0.102

All SDK versions are stored in the `/usr/share/dotnet/sdk` directory of the %linter% container filesystem.

<note>Functionality of .NET Framework-based project analysis will be added in future versions of the linter. Currently,
it is not recommended to inspect projects that require .NET Framework.</note>

In case a project requires a different version of the SDK, you can set it up before running the analysis using the
[`bootstrap`](before-running-qodana.md) field in the `qodana.yaml` file.
For example, this command will install the required version of the SDK that is specified in the
`global.json` file and located in the root of your project:

<code style="block" lang="yaml">
    bootstrap: curl -fsSL https://dot.net/v1/dotnet-install.sh |
      bash -s -- --jsonfile /data/project/global.json -i /usr/share/dotnet
</code>

### Run analysis

<p><include src="lib_qd.xml" include-id="docker-dotnet-specific-solution-project"/></p>

<p><include src="lib_qd.xml" include-id="qodana-cli-quickstart" use-filter="non-gs,other,empty,non-php"/></p>



## Next steps

<include src="lib_qd.xml" include-id="linter-next-steps-footer" use-filter="empty"/>