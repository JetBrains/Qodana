[//]: # (title: Qodana for .NET)

<var name="linter" value="Qodana for .NET"/>
<var name="ide" value="Rider"/>
<var name="docker-image" value="jetbrains/qodana-dotnet:2022.3-eap"/>

%linter% is based on [%ide%](https://www.jetbrains.com/rider/) and provides static analysis for .NET projects.
It brings all the smarts from Rider, which help you:

* Detect anomalous code and probable bugs
* Eliminate dead code
* Highlight spelling problems
* Improve overall code structure
* Introduce coding best practices

## Analyze a project locally

### Install project dependencies

Docker image is based on the official SDK 6.0 Docker image from Microsoft suitable for analysis of .NET Core 
projects only. 

<p><include src="lib_qd.xml" include-id="docker-dotnet-specific-requirements"/></p>

### Run analysis

<p><include src="lib_qd.xml" include-id="docker-dotnet-specific-solution-project"/></p>

<p><include src="lib_qd.xml" include-id="qodana-cli-quickstart" use-filter="non-gs,other,empty"/></p>



## Next steps

- <a href="qodana-jvm-docker-readme.xml">Configure %linter% Docker image</a>
- <a href="github.md">Run %linter% on GitHub</a>
- <a href="service.md">Use %linter% as a Service</a>
- <a href="ci.md">Extend your CI/CD with %linter% plugins</a>

