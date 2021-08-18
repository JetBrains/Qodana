[//]: # (title: Supported Technologies)

><include src="lib_qd.xml" include-id="eap-warning"/>

With time, Qodana will support all languages and technologies covered by JetBrains IDEs. The current version (%product-version%) lets you analyse:

* [Java](https://www.java.com) projects based on [Gradle](https://gradle.org/), [Maven](https://maven.apache.org/) or [Jetbrains Project 
  System (JPS)](https://github.com/JetBrains/JPS)
* [Kotlin](https://kotlinlang.org) projects, including [Kotlin-JS](https://kotlinlang.org/docs/reference/js-overview.html)
* [PHP](https://www.php.net) projects

For Java and Kotlin, no preliminary steps are required.

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