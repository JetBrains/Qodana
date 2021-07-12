[//]: # (title: Supported Technologies)

><include src="lib_qd.xml" include-id="eap-warning"/>

With time, Qodana will support all languages and technologies covered by JetBrains IDEs. The current version (%product-version%) lets you analyse:

* [Java](https://www.java.com) projects based on [Gradle](https://gradle.org/), [Maven](https://maven.apache.org/) or [Jetbrains Project
  System (JPS)](https://github.com/JetBrains/JPS), no preliminary steps are required.
* [Kotlin for Server Side](https://kotlinlang.org/lp/server-side/), no preliminary steps are required.
* [PHP](https://www.php.net) projects, see [below](#php).
* [Python](https://python.org) projects, see [below](#python).

If your project contains a frontend part written in Javascript or Typescript, the qualitative analysis will be possible only
if the project's directory contains downloaded dependencies and the project is ready to be built. We are working on simplifying this process and will provide smooth support at least for the projects based on [npm](https://www.npmjs.com).

## PHP
{id="php"}

For a PHP project, if you use PHP Composer, add the following step before you run the analysis:

```shell
 docker run --rm -v <source-directory>:/app composer:latest install
```

If you need to change the language level, place the following content into `<source-directory>/.idea/php.xml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="PhpProjectSharedConfiguration" php_language_level="<desired level>" />
</project>
```

## Python
{id="python"}

For a basic Python project, which only uses `stdlib`, no preliminary steps are required.

In case a project has external `pypi` dependencies, use any of the following  options:
- Create `virtualenv` as a subfolder in your project and exclude it in [qodana.yaml](qodana-yaml.md#exclude-paths) to skip analysis of vendor code.
- Mount a separate `virtualenv` as [cache](qodana-intellij-docker-techs.md#Cache+dependencies). 
  
  When you create the `virtualenv` folder, no actual `python` binary is copied into it. Instead, a symlink is created to `python` binary used to create virtualenv. This could lead to incorrect paths when your `virtualenv` is being read inside the Qodana container, since `python` location there could be different. To fix this, create `virtualenv` using the Qodana container's `python`:

  ```shell
  docker run --rm \
        -v <source-directory>/:/data/project/ \
        -v <cache-directory>/:/data/cache/ \
        --entrypoint=bash \
        jetbrains/qodana -c '
          python3 -m venv /data/cache/venv
          source /data/cache/venv/bin/activate
          pip3 install -r /data/project/requirements.txt
        '
  ```

  Now we have our project dependencies in `<cache-directory>`. This folder could be preserved between builds to speed them up. Start Qodana with cache mounted, and it would automatically look for `virtualenv` in `/data/cache/venv`:

   ```shell
   docker run --rm -it -p 8080:8080 \
      -v <source-directory>/:/data/project/ \
      -v <output-directory>/:/data/results/ \
      -v <cache-directory>/:/data/cache/ \
      jetbrains/qodana --show-report
   ```