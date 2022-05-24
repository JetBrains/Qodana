[//]: # (title: Linters)

A linter is a software tool that analyzes codebase for bugs, errors, and other mistakes that impact its quality and 
can cause problems. Basically, each Qodana linter associated with a specific programming language 
helps:

* Detect anomalous code and probable bugs
* Eliminate dead code
* Highlight spelling problems
* Improve overall code structure
* Introduce coding best practices

With time, Qodana will support all languages and technologies covered by JetBrains IDEs. The current version 
(%product-version%) of Qodana lets you analyze the following kinds of projects:

* [Java and Kotlin](#Java+and+Kotlin) projects
* [Non-JVM](#Non-JVM+technologies) projects: PHP, Python, JavaScript, and TypeScript
* Audit [clone and license](#Clone+Finder+and+License+Audit) usages in your codebase

## Java and Kotlin

Qodana lets you analyze [Java](https://www.java.com) and 
[Kotlin for Server Side](https://kotlinlang.org/lp/server-side/) projects based on [Gradle](https://gradle.org/), 
[Maven](https://maven.apache.org/) or [Jetbrains Project System (JPS)](https://github.com/JetBrains/JPS). 

To do this, you can use the following linters:

* The [Qodana for JVM](qodana-jvm.md) linter uses the [IntelliJ IDEA Ultimate](https://www.jetbrains.com/idea/) inspections
* The [Qodana Community for JVM](qodana-jvm-community.md) linter runs the inspections provided by [IntelliJ IDEA Community](https://www.jetbrains.com/idea/)
* The [Qodana Community for Android](qodana-jvm-android.md) linter provides the features of the 
[Android Support](https://plugins.jetbrains.com/plugin/1792-android-support) plugin

## Non-JVM technologies

Besides JVM, the current version (%product-version%) of Qodana provides inspections for the following programming languages: 

- The [Qodana for PHP](qodana-php.md) linter lets you inspect code written in [PHP](https://www.php.net) 
- The [Qodana for Python](qodana-python.md) linter can be used to inspect [Python](https://python.org) projects
- The [Qodana for JS](qodana-js.md) linter can inspect projects written in
[JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) and [TypeScript](https://www.typescriptlang.org/)

## Clone Finder and License Audit

The [Qodana Clone Finder](about-clone-finder.md) linter inspects your code for duplicate functions.

The [License audit](license-audit.xml) linter analyzes license usages and helps you avoid using software with
incompatible licenses.