[//]: # (title: About Qodana IntelliJ)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<note>

<include src="lib_qd.xml" include-id="supported-techs">
    <var name="linter" value="Qodana IntelliJ"/>
    </include>

</note>

The Qodana IntelliJ linter lets you perform [static analysis](https://en.wikipedia.org/wiki/Static_program_analysis) of your codebase. It brings all the smarts from IntelliJ IDEs: 

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
docker run --rm -it -v <source-directory>/:/data/project/ \ 
  -p 8080:8080 jetbrains/qodana --show-report
```

with `source-directory` pointing to the root of your project.

Check the results in your browser at [`http://localhost:8080`](http://localhost:8080).

> For details on running Qodana in Docker, see the [Docker guide](docker-images.md). 

 <seealso>
 <category ref="next_steps">
   <a href="qodana-intellij-docker-readme.md"/>
   <a href="qodana-intellij-github-action.md"/>
   <a href="qodana-intellij-github-application.md"/>
   <a href="service.md"/>
   <a href="qodana_plugins.md"/>
  </category>
 </seealso>

