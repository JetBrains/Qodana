[//]: # (title: Quick start)

<var name="linter" value="Qodana"/>

The current version of %product% (%product-version%) lets you analyze 
<a href="supported-technologies.md">Java, Kotlin, PHP, Python, JavaScript, and TypeScript</a> projects. Eventually, all 
languages and technologies covered by JetBrains IDEs will be added.

## Analyze a project locally

For all linters the procedure is basically the same.

1. Pull the image from Docker Hub (only necessary to get the latest version):

```shell
docker pull jetbrains/qodana-<linter>
```

Here, `jetbrains/qodana-<linter>` denotes the linter names listed under these tabs:

<tabs>
    <tab title="Programming languages">
    <table>
        <tr><td>Name</td><td>Application</td></tr>
        <tr><td>jetbrains/qodana-jvm</td><td>Java and Kotlin for Server Side projects. Based on IntelliJ IDEA Ultimate.</td></tr>
        <tr><td>jetbrains/qodana-jvm-community</td><td>Java and Kotlin for Server Side projects. Based on IntelliJ IDEA Community.</td></tr>
        <tr><td>jetbrains/qodana-jvm-android</td><td>Java and Kotlin for Server Side projects. Based on IntelliJ IDEA with the Android support.</td></tr>
        <tr><td>jetbrains/qodana-php</td><td>PHP projects. Based on PhpStorm.</td></tr>
        <tr><td>jetbrains/qodana-python</td><td>Python projects. Based on PyCharm Professional.</td></tr>
        <tr><td>jetbrains/qodana-js</td><td>JavaScript and TypeScript projects. Based on WebStorm.</td></tr>
    </table>
    </tab>
    <tab title="Duplicates and incompatible licenses">
        <table>
            <tr><td>Name</td><td>Application</td></tr>
            <tr><td>jetbrains/qodana-clone-finder</td><td>Detects duplicate functions.</td></tr>
            <tr><td>jetbrains/qodana-license-audit</td><td>Detects incompatible licenses.</td></tr>
        </table>
    </tab>
</tabs>

2. For the Java, Kotlin, PHP, Python, and JavaScript projects, run this command to analyze you codebase: 

```shell
docker run --rm -it -v <source-directory>/:/data/project/ \ 
  -p 8080:8080 jetbrains/qodana-<linter> --show-report
```

with `source-directory` pointing to the root of your project.

3. Check inspection results [in your browser](html-report.md) at `http://localhost:8080`.



Detailed information about linters is available in the [Qodana linters](supported-technologies.md) section.

## Next steps

 - <a href="docker-image-configuration.xml">Configure %linter% Docker images</a>
 - <a href="github-actions.md">Run %linter% on GitHub</a>
 - <a href="qodana-github-application.md">Run %linter% as a GitHub App</a>
 - <a href="service.md">Use %linter% as a Service</a>
 - <a href="ci.md">Extend your CI/CD with %linter% plugins</a>

 