# Qodana. Supported Technologies

With time, Qodana will support all languages and technologies covered by JetBrains IDEs. 

The current (2020.3.x) version lets you fully analyse:

* [Java](https://www.java.com) projects based on [Gradle](https://gradle.org/), [Maven](https://maven.apache.org/) or [Jetbrains Project 
  System (JPS)](https://github.com/JetBrains/JPS)
* [Kotlin](https://kotlinlang.org) projects, included [Kotlin-JS](https://kotlinlang.org/docs/reference/js-overview.html)
* [PHP](https://www.php.net) projects

The word 'fully' technically means that there is no need to 'prepare' a project in any way to make the analysis happen. 
Qodana will configure the project, download dependencies and perform the analysis on the project folder. 

If your project contains a frontend part written in Javascript or Typescript, then the qualitative analysis will be possible only 
if the project's folder contains downloaded dependencies, and it is ready to be built. We are working to make this 
process simpler and will provide smooth support at least for the projects based on [npm](https://www.npmjs.com).
 
Also, we started to work on smooth integration for [Python](https://www.python.org/) projects, stay tuned!

If you have any particular interest in a certain language or technology, don't hesitate to contact us at
[qodana-support@jetbrains.com](mailto:qodana-support@jetbrains.com) or via [our issue tracker](https://youtrack.jetbrains.com/newIssue?project=QD). We eagerly want your feedback on what's already there and if there are any features that we miss. The more you tell us about your needs, the
better we will be to fit you!