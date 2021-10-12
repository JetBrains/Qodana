[//]: # (title: Qodana for PHP)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<note>
<p>
<include src="lib_qd.xml" include-id="eap-warning">
<var name="product" value="Qodana PHP"/>
</include>
</p>
</note>

<var name="linter" value="Qodana PHP"/>

%linter% is based on [PhpStorm](https://www.jetbrains.com/phpstorm/) and provides static analysis for PHP projects.

## Try it now

### Analyze a project locally

To start, pull the image from Docker Hub (only necessary to get the latest version):

<var name="docker-image" value="jetbrains/qodana-php"/>

<code style="block" lang="shell">
  docker pull %docker-image%
</code>

If you use PHP Composer, add the following step before running the analysis:

```shell
 docker run --rm -v <source-directory>:/app composer:latest install
```

If you need to change the language level, add the following into `<source-directory>/.idea/php.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="PhpProjectSharedConfiguration" php_language_level="<desired level>" />
</project>
```

Run the analysis locally:

```shell
docker run --rm -it -v <source-directory>/:/data/project/ \ 
  -p 8080:8080 %docker-image% --show-report
```

with `source-directory` pointing to the root of your project.

<p>
<include src="lib_qd.xml" include-id="show-report-command-explanation"/>
</p>

## Next steps

- <a href="qodana-intellij-docker-readme.md">Configure %linter% Docker image</a>
- <a href="qodana-intellij-github-action.md">Run %linter% on GitHub</a>
- <a href="qodana-intellij-github-application.md">Run %linter% as a GitHub App</a>
- <a href="service.md">Use %linter% as a Service</a>
- <a href="ci.md">Extend your CI/CD with %linter% plugins</a>