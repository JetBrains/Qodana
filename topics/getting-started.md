[//]: # (title: Qodana)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)
><include src="lib_qd.xml" include-id="eap-warning"/>

![](banner-main.png)

**Qodana** is a code quality monitoring platform that allows you to evaluate the integrity of code you own, contract, or purchase.
It brings into your CI/CD pipelines all the smart features you love in the JetBrains IDEs plus continues adding project-level checks like clone detection and license audit (coming soon). 

Qodana allows you to get an overview of the project quality, set quality targets, and track progress on them. You can quickly adjust the list of checks applied for the project and include or remove directories from the analysis.

## Qodana at a glance
### Components
Qodana includes a growing number of command-line tools ([linters](linters.md)) which provide project analysis locally or in any CI.

### Results
Every linter provides two types of output:
* JSON files separately described per each linter in the [Results](results.md) chapter
* Web report for interactive results investigation and configuration adjustment described in [UI Overview](ui-overview.md)

The Qodana UI can be part of your CI user interface in case your CI supports the UI extension. If it doesn't, you can spin the Qodana UI on your own following our [guidelines](html-report.md).

The Qodana Cloud UI that comes in summer 2021 will let you see comparative analysis of your projects, aggregated results, trends, smart dashboards, and even more. Stay tuned!

### Distribution
To facilitate integration, extensibility, and advanced reporting, Qodana linters are supplied in a number of distribution formats and web services:
- [Docker images](docker-images.md)
- [Plugins](teamcity-plugins.md)
- [GitHub actions](github-actions.md)  and [application](qodana-intellij-github-application.md)
- [Cloud service](service.md)

## Try it now

### Analyse a project locally

Start with [Qodana IntelliJ linter](about-qodana-intellij.md) or check other [linters](linters.md) we provide.

```shell
docker run --rm -it -v <source-directory>/:/data/project/ -p 8080:8080 jetbrains/qodana --show-report
```
where `source-directory` should point to the root of your project. Read our [Docker guide](qodana-intellij-docker-readme.md) for more options and details related to the Qodana execution.

You will be able to [check results in your browser](html-report.md) at [`http://localhost:8080`](http://localhost:8080).

For all linters the procedure is basically the same, the differences and complete steps are provided in the detailed guides for every [distribution format](#Distribution).

### Run at GitHub

We published a dedicated GitHub action for every Qodana [linter](linters.md) so you can easily include it in any GitHub workflow.

### Supported languages
PHP, Java, and Kotlin are already supported. Eventually, all [languages and technologies](supported-technologies.md) covered by JetBrains IDEs will be added.

## License

<include src="lib_qd.xml" include-id="license-info"/>