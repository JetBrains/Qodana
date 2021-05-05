[//]: # (title: About Qodana)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

The Qodana linter lets you perform [static analysis](https://en.wikipedia.org/wiki/Static_program_analysis) of your
codebase. It brings all the smarts from IntelliJ IDEs: 

[//]: # "list!"

Qodana comprises two main parts: a nicely packaged GUI-less IntelliJ IDEA engine tailored for use in a CI pipeline as a typical linter tool and an interactive web-based reporting UI.

The current version [supports PHP, Java, and Kotlin for Server Side](supported-technologies.md); support for more languages and technologies is on its way.

## Distribution

Modern CI-centric workflows require having a reliable quality gate in your build pipeline.
It was technically possible to run JetBrains IDE inspections for the whole project in headless batch mode well before the CI era. However, integrating an IDE into the CI pipeline as a typical linter proved difficult.

Qodana is packed into a ready-to-use [Docker image](qodana-docker-readme.md) which supports different usage scenarios:
- Running the analysis on a regular basis as part of your continuous integration (*CI-based execution*)
- Single-shot analysis (for example, performed *locally*)
- --[GitHub Action](qodana-github-action.md)

If you don't have any CI for your project, we encourage you to try a free version of JetBrains [TeamCity](https://www.jetbrains.com/teamcity/), either in-cloud (currently in Beta) or on-premise. In this case, you can switch to our [TeamCity plugin](qodana-teamcity-plugin.md) as it gives more options.

[//]: # "broken link!"
