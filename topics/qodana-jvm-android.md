[//]: # (title: Qodana Community for Android)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<var name="linter" value="Qodana Community for Android"/>
<var name="ide" value="IntelliJ IDEA"/>

%linter% is based on [%ide%](https://www.jetbrains.com/idea/) with the [Android Support](https://plugins.jetbrains.com/plugin/1792-android-support) plugin and provides static analysis for Android projects. <include src="lib_qd.xml" include-id="linter-intro"/>

## Try it now

### Analyze a project locally

<p><include src="lib_qd.xml" include-id="jvm-project-setup-note"/></p>

To start, pull the image from Docker Hub (only necessary to get the latest version):

<var name="docker-image" value="jetbrains/qodana-jvm-android"/>

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

- <a href="qodana-jvm-android-docker-readme.xml">Configure %linter% Docker image</a>
- <a href="qodana-github-action.md">Run %linter% on GitHub</a>
- <a href="qodana-github-application.md">Run %linter% as a GitHub App</a>
- <a href="service.md">Use %linter% as a Service</a>
- <a href="ci.md">Extend your CI/CD with %linter% plugins</a>
