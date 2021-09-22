[//]: # (title: Qodana IntelliJ Docker image)

![official JetBrains project](https://jb.gg/badges/official-flat-square.svg)

Supported tags: [`2020.3-eap`](https://hub.docker.com/r/jetbrains/qodana/tags?page=1&ordering=last_updated&name=2020.3-eap), [`2021.1-eap`](https://hub.docker.com/r/jetbrains/qodana/tags?page=1&ordering=last_updated&name=2021.1-eap),  [`latest`](https://hub.docker.com/r/jetbrains/qodana/tags?page=1&ordering=last_updated&name=latest) (points to `2021.2-eap`)

The Docker images for the [Qodana IntelliJ linters](about-qodana-intellij.md) are provided to support different usage scenarios:
- Running the analysis on a regular basis as part of your continuous integration (*CI-based execution*)
- Single-shot analysis (for example, performed *locally*).

If you are familiar with [JetBrains IDEs code inspections](https://www.jetbrains.com/help/idea/code-inspection.html)
and know what to expect from the static analysis outside the editor, you can skip the following section and continue from [Using an existing profile](#Using+an+existing+profile).

If you are just starting in the field, we recommend proceeding with the [default setup](#quick-start-recommended-profile) we provide. You will see the
results of the most common checks performed on your code base. Later, you can [adjust them](#Configure+via+qodana.yaml) to suit your needs better.

<note>
<p>
    <include src="lib_qd.xml" include-id="generic-docker-image-note"/>
</p>
</note>  

## Quick start with the recommended profile
{id="quick-start-recommended-profile"}

### Run analysis locally
<note>
<include src="lib_qd.xml" include-id="docker-ram-note"/>
</note>

1) Pull the image from Docker Hub (only necessary to update to the `latest` version):

[//]: # "?"

   ```shell
   docker pull jetbrains/qodana-<linter>
   ```

2) Run the following command:

   ```shell
   docker run --rm -it -p 8080:8080 \
      -v <source-directory>/:/data/project/ \
      -v <output-directory>/:/data/results/ \
      jetbrains/qodana-<linter> --show-report
   ```

where `source-directory` and `output-directory` are full local paths to, respectively, the project source code directory and the analysis results directory.

<p>
<include src="lib_qd.xml" include-id="show-report-command-explanation"/>
</p>

If you don't need the user interface and prefer to study raw data, use the following command:

   ```shell
   docker run --rm -it \
      -v <source-directory>/:/data/project/ \
      -v <output-directory>/:/data/results/ \
      jetbrains/qodana-<linter>
   ```

The `output-directory` will contain [all the necessary results](qodana-intellij-output.md#Basic+output). You can further tune the command as described in the [technical guide](qodana-intellij-docker-techs.xml).

If you run the analysis several times in a row, make sure you've cleaned the results directory before using it in `docker run` again.

### Run analysis in CI

Use the following command as a task in a generic Shell executor:

   ```shell
       docker run --rm \
           -v <source-directory>/:/data/project/ \
           -v <output-directory>/:/data/results/ \
           jetbrains/qodana-<linter>
   ```

  where `source-directory` and `output-directory` are full paths to, respectively, the project source code directory and the [analysis results directory](qodana-intellij-output.md#Basic+output).

<p><include src="lib_qd.xml" include-id="docker-options-tip"/></p>

<tip><p>For details on available CI integrations, see <a href="ci.md"/>.</p></tip>

## Using an existing profile

This section is intended for users familiar with configuring code analysis via [IntelliJ inspection profiles](https://www.jetbrains.com/help/idea/customizing-profiles.html).

You can pass the reference to the existing profile in [multiple ways](qodana-intellij-docker-techs.xml#Order+of+resolving+a+profile). Here are some examples:

- Mapping the profile to `/data/profile.xml` inside the container:

  ```shell
        docker run --rm -it -p 8080:8080 \
            -v <source-directory>/:/data/project/ \
            -v <output-directory>/:/data/results/ \
            -v <inspection-profile.xml>:/data/profile.xml
            jetbrains/qodana-<linter> --show-report
   ```

- Using the name of the profile in your project `.idea/inspectionProfiles/` folder:

  ```shell
        docker run --rm -it -p 8080:8080 \
            -v <source-directory>/:/data/project/ \
            -v <output-directory>/:/data/results/ \
            jetbrains/qodana-<linter> --show-report --profile-name php.extended
  ```

## Configure via qodana.yaml

The `qodana.yaml` file will be automatically recognized and used for the analysis configuration, so that you don't need to pass any additional parameters.  
The references to the inspection profiles will be resolved [in a particular order](qodana-intellij-docker-techs.xml#Order+of+resolving+a+profile). To learn about the format, refer to the [`qodana.yaml` documentation](qodana-yaml.md).

## Plugins management

Paid plugins are not yet supported. Each vendor must clarify licensing terms for CI usage and collaborate with us to make it work.

Any free IntelliJ platform plugins or your custom plugin can be added by mounting it to the container plugins' directory using the following command:

```shell
docker run ... -v /your/custom/path/%pluginName%:/opt/idea/plugins/%pluginName% jetbrains/qodana-<linter>
```

Refer to the [technical guide](qodana-intellij-docker-techs.xml) for more details.

## Usage statistics

According to the [JetBrains EAP user agreement](https://www.jetbrains.com/legal/agreements/user_eap.html), we can use third-party services to analyze the usage of our features to further improve the user experience. All data will be collected [anonymously](https://www.jetbrains.com/company/privacy.html). You can disable the reporting of usage statistics by adjusting the options of the Docker command you use. Refer to the [technical guide](qodana-intellij-docker-techs.xml) for details.

<seealso>
    <category ref="external">
        <a href="https://rpadovani.com/gitlab-jetbrains-qodana">'Integrating JetBrains Qodana with GitLab pipelines' by Riccardo Padovani</a>
    </category>
</seealso>