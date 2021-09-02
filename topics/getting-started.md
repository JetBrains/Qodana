[//]: # (title: Get started with Qodana)

<note>

<include src="lib_qd.xml" include-id="supported-techs">
<var name="linter" value="Qodana"/>
</include>

</note>

## Analyse a project locally

Start with [Qodana IntelliJ linter](about-qodana-intellij.md) or check out [other linters](linters.md) we provide. For all linters the procedure is basically the same.

```shell
docker run --rm -it -v <source-directory>/:/data/project/ \ 
  -p 8080:8080 jetbrains/qodana --show-report
```

with `source-directory` pointing to the root of your project.

> For details on the Qodana IntelliJ linter execution, see [Qodana IntelliJ Docker Image](qodana-intellij-docker-readme.md) 

You can [check results in your browser](html-report.md) at `http://localhost:8080`.


 ## Next steps

 - <a href="docker-images.md"/>
 - <a href="github-actions.md"/>
 - <a href="qodana-intellij-github-application.md"/>
 - <a href="service.md"/>
 - <a href="qodana_plugins.md"/>

 