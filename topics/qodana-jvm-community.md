[//]: # (title: Qodana for JVM Community)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<var name="linter" value="Qodana JVM Community"/>
<var name="ide" value="IntelliJ IDEA Community"/>

%linter% is based on [%ide%](https://www.jetbrains.com/idea/) and provides static analysis for Java and Kotlin for Server Side projects. <include src="lib_qd.xml" include-id="linter-intro"/>

## Try it now

### Analyze a project locally

<p><include src="lib_qd.xml" include-id="jvm-project-setup-note"/></p>

To start, pull the image from Docker Hub (only necessary to get the latest version):

<var name="docker-image" value="jetbrains/qodana-jvm-community"/>

<code style="block" lang="shell">
  docker pull %docker-image%
</code>

and run the analysis locally:

```shell
docker run --rm -it -v <source-directory>/:/data/project/ \ 
  -p 8080:8080 %docker-image% --show-report
```

with `source-directory` pointing to the root of your project.

<p>
<include src="lib_qd.xml" include-id="show-report-command-explanation"/>
</p>

## Next steps

- <a href="qodana-jvm-community-docker-readme.xml">Configure %linter% Docker image</a>
- <a href="qodana-github-action.md">Run %linter% on GitHub</a>
- <a href="qodana-github-application.md">Run %linter% as a GitHub App</a>
- <a href="service.md">Use %linter% as a Service</a>
- <a href="ci.md">Extend your CI/CD with %linter% plugins</a>
