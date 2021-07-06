[//]: # (title: About Qodana License Audit)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

Qodana License Audit can help software projects avoid problems with incompatible third-party licenses. The tool can detect more than 1600 licenses and works with several package managers. Like any other Qodana linter, License Audit is a CI-first tool: users can set up a Continuous License Compliance pipeline and tune it up to their needs.

Read [License Audit Output Formats](license-audit-output.md) to find information about all inspections and possible ways to resolve reported problems.

## Try it now

### Analyse a project locally

To start, pull the image from Docker Hub (only necessary to get the latest version):

```shell
docker pull jetbrains/qodana-license-audit
```

and run the analysis locally:

```shell
docker run --rm -it -v <source-directory>/:/data/project/ -p 8080:8080 jetbrains/qodana-license-audit --show-report
```

where `source-directory` points to the root of your project.

Check the results in your browser at [`http://localhost:8080`](http://localhost:8080).

Read our [Docker guide](license-audit-docker-readme.md) for more options and details related to the License Audit execution.

### Run at GitHub

You can set up a workflow in your GitHub repository using the [GitHub actions](license-audit-github-action.md) we published.

### Supported languages

PHP with Composer, Java and Kotlin with Gradle, Python with Pip, Pipenv and Poetry, JavaScript and TypeScript with NPM and Yarn. Eventually, all [languages and technologies](supported-technologies.md) covered by JetBrains IDEs will be added.

## License

<include src="lib_qd.xml" include-id="license-info">
    <var name="product" value="Qodana linters"/>
</include>
