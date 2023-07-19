[//]: # (title: Qodana for .NET)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<img src="dotnet-linter.png" dark-src="dotnet-linter_dark.png" alt="Qodana for .NET linter languages" width="296"/>

<note>
    <p>
        <include src="lib_qd.xml" include-id="eap-warning">
            <var name="product" value="Qodana for .NET"/>
        </include>
    </p>
</note>

<var name="linter" value="Qodana for .NET"/>
<var name="ide" value="Rider"/>
<var name="docker-image" value="jetbrains/qodana-dotnet:2023.2-eap"/>

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

<p><include src="lib_qd.xml" include-id="docker-dotnet-specific-requirements" use-filter="empty"/></p>

### Run analysis

<p><include src="lib_qd.xml" include-id="docker-dotnet-specific-solution-project"/></p>

<p><include src="lib_qd.xml" include-id="qodana-cli-quickstart" use-filter="non-gs,other,empty,non-php"/></p>



## Next steps

- <a href="qodana-dotnet-docker-readme.xml">Configure %linter% Docker image</a>
- <a href="github.md">Run %linter% on GitHub</a>
- <a href="service.md">Use %linter% as a Service</a>
- <a href="ci.md">Extend your CI/CD with %linter% plugins</a>

