# Qodana. Supported Technologies

With time, Qodana will support all languages and technologies covered by IntelliJ IDEs. 

The current (2020.3.x) version lets you fully analyse:

* [Java](https://www.java.com) projects based on [Gradle](https://gradle.org/), [Maven](https://maven.apache.org/) or [Jetbrains Project 
  System (JPS)](https://github.com/JetBrains/JPS)
* [Kotlin](https://kotlinlang.org) projects, included [Kotlin-JS](https://kotlinlang.org/docs/reference/js-overview.html)
* [PHP](https://www.php.net) projects

The word 'fully' technically means that there is no need to 'prepare' project in any way to make the analysis happened. 
Qodana will configure the project, download dependencies and perform the analysis on the project folder. 

If your project contains frontend part written in Javascript or Typescript the qualitative analysis is possible only 
if the project's folder contains downloaded dependencies, and it's ready to be built. We are working to make this 
process simpler and will provide a smooth support at least for the projects based on [npm](https://www.npmjs.com).
 
Also, we started to work on smooth integration for [Python](https://www.python.org/) projects, stay tuned!

If you have any particular interest in a certain language or technologies, please don't hesitate to contact us at 
qodana-support@jetbrains.com or via [our issue tracker](https://youtrack.jetbrains.com/newIssue?project=QD). We want 
eagerly your feedback on what's already there and any features you miss. The more you tell us about your needs, the 
closer we will be to fit you!