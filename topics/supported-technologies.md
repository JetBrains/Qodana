[//]: # (title: Supported technologies)

><include src="lib_qd.xml" include-id="eap-warning"/>

With time, Qodana will support all languages and technologies covered by JetBrains IDEs. The current version (%product-version%) lets you analyse:

* [Java](https://www.java.com) projects based on [Gradle](https://gradle.org/), [Maven](https://maven.apache.org/) or [Jetbrains Project
  System (JPS)](https://github.com/JetBrains/JPS), no preliminary steps are required.
* [Kotlin for Server Side](https://kotlinlang.org/lp/server-side/), no preliminary steps are required.
* [PHP](https://www.php.net) projects, see [below](#php).

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
````