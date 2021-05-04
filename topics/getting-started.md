[//]: # (title: Qodana)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)  
![](eap-alert.png)
![](banner-main.png)

**Qodana** is a code quality monitoring platform that allows you to evaluate the integrity of code you own, contract, or purchase.
It brings into your CI/CD pipelines all the smart features you love in the JetBrains IDEs plus continues adding project-level checks like clone detection and license audit (coming soon). 

Qodana allows you to get an overview of the project quality, set quality targets, and track progress on them. You can quickly adjust the list of checks applied for the project and include or remove directories from the analysis.

## Quick start guide

### Analyse a project locally

To start, pull the image from Docker Hub (only necessary to get the latest version):

```shell
docker pull jetbrains/qodana
```

and run the analysis locally:

```shell
docker run --rm -it -v <source-directory>/:/data/project/ -p 8080:8080 jetbrains/qodana --show-report
```

where `source-directory` should point to the root of your project.

Check the results in your browser at [`http://localhost:8080`](http://localhost:8080).

Please read our [Docker guide](docker-images.md) for more options and details related to the Qodana execution.

### Run at GitHub

You can set up a workflow in your GitHub repository using the [GitHub action](github-action.md) we published.

## Qodana at a glance
### Components
Qodana includes a growing number of command-line tools ([linters](linters.md)) which provide project analysis locally or in any CI.

### Results
The [project audit results]() are available as JSON files and
[web reports](ui-overview.md) featuring
- role-based reporting
- workflows
- easy navigation from diagrams to code.

### Distribution
To facilitate integration, extensibility, and advanced reporting, Qodana linters are supplied in a number of distribution formats and web services:
- [Docker images](docker-images.md)
- [Plugins](teamcity-plugins.md)
- [GitHub Actions](github-action.md) & [application](qodana-github-application.md)
- [Cloud service](service.md)

<!---a number of linters which are available as [Docker images for any CI](docker-images.md), [GitHub Actions](github-action.md) & [application](qodana-github-application.md), [TeamCity plugins](teamcity-plugins.md), and a separate [cloud service](service.md). Learn more about [Qodana linters](linters.md) and the [web-based UI](ui-overview.md), or continue to the next section to make your first steps check your code with Qodana.
Learn more about [Qodana linters](linters.md) and the [web-based UI](ui-overview.md), or continue to the next section to make your first steps check your code with Qodana.!--->

### Supported languages
PHP, Java, and Kotlin are already supported. Eventually, all [languages and technologies](supported-technologies.md) covered by JetBrains IDEs will be added.


## License

By using Qodana, you agree to the [JetBrains EAP user agreement](https://www.jetbrains.com/legal/agreements/user_eap.html) and [JetBrains privacy policy](https://www.jetbrains.com/company/privacy.html).

## Contact

Contact us at [qodana-support@jetbrains.com](mailto:qodana-support@jetbrains.com) or via [our issue tracker](https://youtrack.jetbrains.com/newIssue?project=QD). We are eager to receive your feedback on the existing Qodana functionality and learn what other features you miss in it.
