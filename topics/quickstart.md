[//]: # (title: Quick start)

<var name="linter" value="Qodana"/>

The current version of %product% (%product-version%) provides linters that let you analyze
<a href="supported-technologies.md">Java, Kotlin, PHP, Python, JavaScript, and TypeScript</a> projects. In addition, 
you can inspect your code for duplicate functions and incompatible licenses used in your project. 

## Analyze a project locally

This section assumes that you have the Docker application deployed on your machine.

1. Pull the image from Docker Hub (only necessary to get the latest version):

   ```shell
   docker pull <image>
   ```
   
   Here, `<image>` denotes the Docker image name of a %product% linter from this table:
   
   |Image name|Application|
   |-----|-----|
   |jetbrains/qodana-jvm|Java and Kotlin for Server Side projects, based on IntelliJ IDEA Ultimate.|
   |jetbrains/qodana-jvm-community|Java and Kotlin for Server Side projects, based on IntelliJ IDEA Community.|
   |jetbrains/qodana-jvm-android|Java and Kotlin for Server Side projects, based on IntelliJ IDEA with the Android support.|
   |jetbrains/qodana-php|PHP projects, based on PhpStorm.|
   |jetbrains/qodana-python|Python projects, based on PyCharm Professional.|
   |jetbrains/qodana-js|JavaScript and TypeScript projects, based on WebStorm.|
   |jetbrains/qodana-clone-finder|Detects duplicate functions.|
   |jetbrains/qodana-license-audit|Detects incompatible licenses.|

2. Run this command to analyze your codebase (all images except `jetbrains/qodana-clone-finder`): 

    ```shell
    docker run --rm -it -p 8080:8080 \
      -v <source-directory>/:/data/project/ \
      jetbrains/qodana-<linter> --show-report
    ```

    with `<source-directory>` pointing to the root of your project.

    For the `jetbrains/qodana-clone-finder` image, you can run this Docker command:

    ```shell
    docker run --rm -it -p 8080:8080 \
       -v <queried-project-directory>/:/data/project/ \
       -v <reference-projects-directory>/:/data/versus/ \
       -v <output-directory>/:/data/results/ \
       jetbrains/qodana-clone-finder --show-report
    ```

    This command uses the parameters:

    * `<queried-project-directory>` is a full local path to the project source code.
    * `<reference-projects-directory>` is the project directory to be compared with the source code. This parameter can be specified multiple times.
    * `<output-directory>` is the directory that will contain inspection reports.

3. Check inspection results [in your browser](html-report.md) at `http://localhost:8080`.

The detailed information about %product% linters is available in the [Qodana linters](supported-technologies.md) section.

## Next steps

 - <a href="docker-image-configuration.xml">Configure Docker images</a>
 - <a href="github-actions.md">Run %product% on GitHub</a> or use it as a <a href="qodana-github-application.md">GitHub App</a>
 - <a href="qodana_plugins.md">Extend your IDE using plugins</a>
 - <a href="ci.md">Explore how you can integrate %product% into your CI/CD system</a>
-  <a href="service.md">Use %product% as a Service</a>
 