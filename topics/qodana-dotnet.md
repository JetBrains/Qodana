[//]: # (title: Qodana for .NET)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<note>
    <p>
        <include src="lib_qd.xml" include-id="eap-warning">
            <var name="product" value="Qodana for .NET"/>
        </include>
    </p>
</note>

<var name="linter" value="Qodana for .NET"/>
<var name="ide" value="Rider"/>
<var name="docker-image" value="jetbrains/qodana-dotnet:2023.1-eap"/>

%linter% is based on [%ide%](https://www.jetbrains.com/rider/) and provides static analysis for .NET projects.
It brings all the smarts from Rider, which help you:

* Detect anomalous code and probable bugs
* Eliminate dead code
* Highlight spelling problems
* Improve overall code structure
* Introduce coding best practices

## Supported languages and frameworks

The %linter% linter supports C#, VB.NET, F#, and C++ limited by projects containing `.sln` files, as well as
Blazor and ASP.NET frameworks including the Razor syntax.

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

