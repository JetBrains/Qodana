[//]: # (title: About Qodana IntelliJ)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

The Qodana IntelliJ linter lets you perform [static analysis](https://en.wikipedia.org/wiki/Static_program_analysis) of your
codebase. It brings all the smarts from IntelliJ IDEs: 

* anomalous code and probable bug detection
* dead code elimination
* spelling problems highlighting
* overall code structure improvement
* coding best practices introduction

## Try it now

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

You can set up a workflow in your GitHub repository using the [GitHub actions](github-actions.md) we published.

### Supported languages
PHP, Java, and Kotlin are already supported. Eventually, all [languages and technologies](supported-technologies.md) covered by JetBrains IDEs will be added.

## License

By using Qodana linters, you agree to the [JetBrains EAP user agreement](https://www.jetbrains.com/legal/agreements/user_eap.html) and [JetBrains privacy policy](https://www.jetbrains.com/company/privacy.html).

## Contact

Contact us at [qodana-support@jetbrains.com](mailto:qodana-support@jetbrains.com) or via [our issue tracker](https://youtrack.jetbrains.com/newIssue?project=QD). We are eager to receive your feedback on the existing Qodana functionality and learn what other features you miss in it.
