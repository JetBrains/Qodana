[//]: # (title: Supported technologies)

With time, Qodana will support all languages and technologies covered by JetBrains IDEs. The current version (%product-version%) lets you analyze:

- [Java](https://www.java.com) projects based on [Gradle](https://gradle.org/), [Maven](https://maven.apache.org/) or [Jetbrains Project
  System (JPS)](https://github.com/JetBrains/JPS)
- [Kotlin for Server Side](https://kotlinlang.org/lp/server-side/)
- [PHP](https://www.php.net) projects
- [Python](https://python.org) projects
- [Go](https://golang.org) projects

> For details on getting started with a particluar technology, see [](linters.md).

If your project contains a frontend part written in Javascript or Typescript, the qualitative analysis will be possible only
if the project's directory contains downloaded dependencies and the project is ready to be built. Simplifying this process and providing smooth support for at least for the projects based on [npm](https://www.npmjs.com) is currently in development.