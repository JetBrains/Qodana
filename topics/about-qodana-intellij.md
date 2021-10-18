[//]: # (title: Qodana IntelliJ)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<var name="linter" value="Qodana IntelliJ"/>
<var name="tech" value="linter"/>
<var name="techs" value="linters"/>
<var name="tech-link" value="linters.md"/>

<warning>
<p>
    <include src="lib_qd.xml" include-id="qodana-intellij-deprecation"/>
</p>
</warning>


<note>

<include src="lib_qd.xml" include-id="supported-techs">
    <var name="linter" value="Qodana IntelliJ"/>
    </include>

</note>

The Qodana IntelliJ linter lets you perform [static analysis](https://en.wikipedia.org/wiki/Static_program_analysis) of your
codebase. It brings all the smarts from IntelliJ IDEs:

* anomalous code and probable bug detection
* dead code elimination
* spelling problems highlighting
* overall code structure improvement
* coding best practices introduction

## Try it now

### Analyse a project locally

To start, pull the image from Docker Hub (only necessary to get the latest version):

```shell
docker pull jetbrains/qodana
```

and run the analysis locally:

```shell
docker run --rm -it -v <source-directory>/:/data/project/ -p 8080:8080 jetbrains/qodana --show-report
```

where `source-directory` should point to the root of your project.

Check the results in your browser at [`http://localhost:8080`](http://localhost:8080).

Read our [Docker guide](docker-images.md) for more options and details related to the Qodana execution.


<tip>

<include src="lib_qd.xml" include-id="qodana-playground-tip">
    <var name="qodana-playground-url" value="https://qodana.teamcity.com/project/Hosted_Root_Java?mode=builds#all-projects"/>
    <var name="linter" value="Qodana IntelliJ linters"/>
</include>

</tip>

## Next steps

- <a href="qodana-intellij-docker-readme.md">Configure %linter% Docker image</a>
- <a href="qodana-github-action.md">Run %linter% on GitHub</a>
- <a href="qodana-github-application.md">Run %linter% as a GitHub App</a>
- <a href="service.md">Use %linter% as a Service</a>
- <a href="ci.md">Extend your CI/CD with %linter% plugins</a>
