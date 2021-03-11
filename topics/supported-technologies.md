[//]: # (title: Supported Technologies)

With time, Qodana will support all languages and technologies covered by JetBrains IDEs. The current (2020.3.x) version lets you analyse:

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
```

If your project contains a frontend part written in Javascript or Typescript, the qualitative analysis will be possible only 
if the project's directory contains downloaded dependencies and the project is ready to be built. We are working on simplifying this process. We will provide smooth support at least for the projects based on [npm](https://www.npmjs.com).
 
Also, we have started working on the smooth integration for [Python](https://www.python.org/) projects, stay tuned!

If you have any particular interest in a certain language or technology, don't hesitate to contact us at
[qodana-support@jetbrains.com](mailto:qodana-support@jetbrains.com) or via [our issue tracker](https://youtrack.jetbrains.com/newIssue?project=QD). We are eager to receive your feedback on the existing Qodana functionality and learn what other features you miss in it. The more you tell us about your needs, the
better Qodana will fit you!