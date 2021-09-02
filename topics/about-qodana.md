[//]: # (title: About Qodana)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

**Qodana** is a code quality monitoring platform that allows you to evaluate the integrity of code you own, contract, or purchase. It brings into your CI/CD pipelines all the smart features you love in the JetBrains IDEs as well as project-level checks like clone detection and license audit. 

Qodana provides you an overview of the project quality, lets you set quality targets, and track progress on them. You can quickly adjust the list of checks applied for the project and include or remove directories from the analysis.

Watch this video to get a quick Qodana overview:

<video href="dgIw64OdjdU"/>

## Qodana at a glance

Qodana includes several command-line tools ([linters](linters.md)) which provide project analysis locally or in any CI.

Every linter provides two types of output:

* JSON files separately described per each linter in the [Results](results.md) chapter
* Web report for interactive results investigation and configuration adjustment described in [UI Overview](ui-overview.md)

The Qodana UI can be part of your CI user interface in case your CI supports the UI extension. If it doesn't, you can spin the Qodana UI on your own following our [guidelines](html-report.md).

## Distribution
Qodana linters are supplied in a number of distribution formats and web services:
- [Docker images](docker-images.md)
- [GitHub actions](github-actions.md)  and [application](qodana-intellij-github-application.md)
- [Cloud service](service.md)
- [Plugins](qodana_plugins.md)

## Qodana playground

Example projects: https://qodana.teamcity.com/overview?mode=builds

Github pull request: https://github.com/JetBrains/qodana-examples/pull/2/checks

## Contact us

Your feedback is very welcome in
<a href="https://youtrack.jetbrains.com/newIssue?project=QD">our issue tracker</a> or at <a href="mailto:qodana-support@jetbrains.com">
qodana-support@jetbrains.com</a>.

## Next steps

- <a href="getting-started.md"/>
  
- <a href="supported-technologies.md"/>