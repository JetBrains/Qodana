[//]: # (title: About Qodana)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

The Qodana linter lets you perform [static analysis](https://en.wikipedia.org/wiki/Static_program_analysis) of your
code base. It brings all the smarts from IntelliJ IDEs: 
<!---list!--->

The current version [supports PHP, Java, and Kotlin for Server Side](supported-technologies.md); support for more languages and technologies is on its way.

## Distribution

We provide a [Docker image](qodana-docker-readme.md) for the Qodana linter to support different usage scenarios:
- Running the analysis on a regular basis as part of your continuous integration (*CI-based execution*)
- Single-shot analysis (for example, performed *locally*).

If you don't have any CI for your project, we encourage you to try a free version of JetBrains [TeamCity](https://www.jetbrains.com/teamcity/), either in-cloud (currently in Beta) or on-premise. In this case, you can switch to our [TeamCity plugin](https://github.com/JetBrains/Qodana/tree/main/TeamCity%20Plugin) as it gives more options.
<!---broken link!--->
