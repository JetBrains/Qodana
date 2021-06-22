# Qodana. Supported Technologies

With time, Qodana will support all languages and technologies covered by JetBrains IDEs. 

The current (2021.2.x) version lets you analyse:

* [Java](https://www.java.com) projects based on [Gradle](https://gradle.org/), [Maven](https://maven.apache.org/) or [Jetbrains Project 
  System (JPS)](https://github.com/JetBrains/JPS), no preliminary steps are required.
* [Kotlin for Server Side](https://kotlinlang.org/lp/server-side/), no preliminary steps are required.
* [PHP](https://www.php.net) projects, see [below](#php)
* [Python](https://python.org) projects, see [below](#python)

If your project contains a frontend part written in Javascript or Typescript, the qualitative analysis will be possible only
if the project's directory contains downloaded dependencies and the project is ready to be built. We are working on simplifying this process. We will provide a smooth support at least for the projects based on [npm](https://www.npmjs.com).

If you have any particular interest in a certain language or technology, don't hesitate to contact us at
[qodana-support@jetbrains.com](mailto:qodana-support@jetbrains.com) or via [our issue tracker](https://youtrack.jetbrains.com/newIssue?project=QD). We are eager to receive your feedback on the existing Qodana functionality and learn what other features you miss in it. The more you tell us about your needs, the
better Qodana will fit you!

### PHP
For a PHP project, if you use PHP Composer, add the following step before you run the analysis:

```
 docker run --rm -v <source-directory>:/app composer:latest install
```

If you need to change the language level, place the following content into `<source-directory>/.idea/php.xml`:

```
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="PhpProjectSharedConfiguration" php_language_level="<desired level>" />
</project>
```

### Python
For basic Python project, which only use stdlib no preliminary steps are required.
In case you have external pypi dependencies, you have 2 options: 
 - Create `virtualenv` as a subfolder in your project and exclude it in [qodana.yaml](qodana-yaml.md#exclude-paths) (to skip analyse of vendor code)
 - Mount separate `virtualenv` as [cache](../Docker/techs.md#cache-dependencies). Let's discuss this option in more details

When you create `virtualenv` folder, no actual python binary is copied into it. Instead, symlink is being created to python binary used to create virtualenv. This could lead to incorrect paths, when your virtualenv is being read inside qodana container (because python there could be located in other place). To fix this, we should create virtualenv using qodana container's python:

```
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

Now we have our project dependencies in `<cache-directory>`. This folder could be preserved between builds to speed them up. Start qodana with cache mounted, and it would automatically look for virtualenv in `/data/cache/venv`:

 ```
 docker run --rm -it -p 8080:8080 \
    -v <source-directory>/:/data/project/ \
    -v <output-directory>/:/data/results/ \
    -v <cache-directory>/:/data/cache/ \
    jetbrains/qodana --show-report
 ```