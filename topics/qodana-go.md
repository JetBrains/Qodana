[//]: # (title: Qodana for Go)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<note>
<p>
<include src="lib_qd.xml" include-id="eap-warning">
<var name="product" value="Qodana Go"/>
</include>
</p>
</note>

<var name="linter" value="Qodana Go"/>

%linter% is based on [Goland](https://www.jetbrains.com/go/) and provides static analysis for Go projects.

## Try it now

### Analyze a project locally

To start, pull the image from Docker Hub (only necessary to get the latest version):

<var name="docker-image" value="jetbrains/qodana-go"/>

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

- <a href="qodana-docker-readme.xml">Configure %linter% Docker image</a>
- <a href="qodana-github-action.md">Run %linter% on GitHub</a>
- <a href="qodana-github-application.md">Run %linter% as a GitHub App</a>
- <a href="service.md">Use %linter% as a Service</a>
- <a href="ci.md">Extend your CI/CD with %linter% plugins</a>
