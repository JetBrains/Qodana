# Qodana. Supported Technologies

With time, Qodana will support all languages and technologies covered by JetBrains IDEs. 

The current (2020.3.x) version lets you analyse:

* [Java](https://www.java.com) projects based on [Gradle](https://gradle.org/), [Maven](https://maven.apache.org/) or [Jetbrains Project 
  System (JPS)](https://github.com/JetBrains/JPS)
* [Kotlin](https://kotlinlang.org) projects, included [Kotlin-JS](https://kotlinlang.org/docs/reference/js-overview.html)
* [PHP](https://www.php.net) projects

For Java and Kotlin steps you don't need any preliminary step. 

For you PHP project, if you use PHP Composer, please add the following step before you run analysis. 

```
 docker run --rm --interactive=false --tty=false --user=1001 -v <source-folder>:/app composer:latest install
```

If you need to change the language level, please place the following content into `<source-folder>/.idea/php.xml`

```
<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="PhpProjectSharedConfiguration" php_language_level="<desired level>" />
</project>
```

If your project contains a frontend part written in Javascript or Typescript, then the qualitative analysis will be possible only 
if the project's folder contains downloaded dependencies, and it is ready to be built. We are working to make this 
process simpler and will provide smooth support at least for the projects based on [npm](https://www.npmjs.com).
 
Also, we started to work on smooth integration for [Python](https://www.python.org/) projects, stay tuned!

If you have any particular interest in a certain language or technology, don't hesitate to contact us at
[qodana-support@jetbrains.com](mailto:qodana-support@jetbrains.com) or via [our issue tracker](https://youtrack.jetbrains.com/newIssue?project=QD). We eagerly want your feedback on what's already there and if there are any features that we miss. The more you tell us about your needs, the
better we will be to fit you!