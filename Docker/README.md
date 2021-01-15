# Qodana Docker Image

![official JetBrains project](https://jb.gg/badges/official-flat-square.svg)
![Docker Stars](https://img.shields.io/docker/stars/jetbrains/qodana.svg)
![Docker Pulls](https://img.shields.io/docker/pulls/jetbrains/qodana.svg)

![EAP](../resources/eap-alert.png)

Supported tags: [`2020.3-eap`](https://hub.docker.com/layers/jetbrains/qodana/2020.3-eap/images/sha256-2085028591a87b68f81c62278c6ea715a8043b30654fd791d7eda10651bc3709?context=explore), [`latest`](https://hub.docker.com/layers/jetbrains/qodana/latest/images/sha256-2085028591a87b68f81c62278c6ea715a8043b30654fd791d7eda10651bc3709?context=explore) (points to `2020.3-eap`)

## General

The Qodana Docker image lets you to perform [static analysis](https://en.wikipedia.org/wiki/Static_program_analysis) of your
code base. The current version [supports PHP, Java, and Kotlin](../General/supported-technologies.md); the support for more languages and technologies are on its way.

We provide two options optimized for different scenarios:
- Running the analysis on a regular basis as a part of your continuous integration (*CI-based execution*)
- Single-shot analysis (for example, performed *locally*)

If you prefer the first option and have established a continuous integration (CI) support for your project, this page
  will guide your through all available possibilities.  
  If you don't have any CI for your project, we encourage you to try a free version of JetBrains [TeamCity](https://www.jetbrains.com/teamcity/), either in-cloud (currently in Beta) or on-premise. In this case, you can switch to our [TeamCity plugin](https://github.com/JetBrains/Qodana/tree/main/TeamCity%20Plugin) as it gives more options.

If you are familiar with [JetBrains IDEs code inspections](https://www.jetbrains.com/help/idea/code-inspection.html)
and know what to expect from the static analysis outside the editor, you can start with the "[Using existing profile](#Using-existing-profile)" section.

If you are just starting in the field, we recommend proceeding with the [default setup](#Quick-start-with-recommended-profile) we provide. You will see the
results of the most common checks performed on your code base. Later, you can [adjust them](#Configure-via-qodanayaml) to suit your needs better.

### Quick start with recommended profile

To run analysis __locally__:

1) Pull the image from Docker Hub (only necessary to update the `latest` version):

   ```
   docker pull jetbrains/qodana

   ```
2) Run the following command:

   ```
   docker run --rm -it -p 8080:8080 \
      -v <source-directory>/:/data/project/ \
      -v <output-directory>/:/data/results/ \
      jetbrains/qodana --show-report
   ```

   where `source-directory` and `output-directory` are full local paths to, respectively, the project source code directory and the analysis results directory.

   This command will run the analysis on your source code and start the web server to provide a convenient view of the results. Open [`http://localhost:8080`](http://localhost:8080) in your browser to examine the found problems and performed checks. Here, you can also reconfigure the analysis. See the [UI section](../UI/README.md) of this guide for details. When done, you can stop the web server by pressing `Ctrl-C` in the Docker console.

   In case you don't need the user interface and prefer to study raw data, use the following command:

   ```
   docker run --rm -it \
      -v <source-directory>/:/data/project/ \
      -v <output-directory>/:/data/results/ \
      jetbrains/qodana
   ```

   The `output-directory` will contain [all the necessary results](../General/output.md#basic-output). You can further tune the command as described in the [technical guide](techs.md).

   If you run the analysis several times in a row, make sure you've cleaned the results' directory before using it in `docker run` again.

To run analysis __in CI__:
 - Use the following command as the task in generic Shell executor:
   ```
    docker run --rm \
        -v <source-directory>/:/data/project/ \
        -v <output-directory>/:/data/results/ \
        jetbrains/qodana
   ```
   where `source-directory` and `output-directory` are full paths to, respectively, the project source code directory and the analysis results directory. 
   The output of `output-directory` is described [here](../General/output.md#basic-output).  
   Consider using [fail-thresold](https://github.com/JetBrains/Qodana/blob/main/General/qodana-yaml.md#fail-threshold) to make build fail on certain number of problems reached.
   
 - Example for GitHub Action (`.github/workflows/qodana.yml`):
   ```yaml
   jobs:
     qodana:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v2
         - uses: docker://jetbrains/qodana
           with:
             args: --results-dir=/github/workspace/qodana --save-report --report-dir=/github/workspace/qodana/report
         - uses: actions/upload-artifact@v2
           with:
             path: qodana
   ```
   
 - Example for GitLab CI (`.gitlab-ci.yml`):
    ```yaml
    qodana:
      image: 
        name: jetbrains/qodana
        entrypoint: [sh, -c]
      script:
        - /opt/idea/bin/entrypoint --results-dir=$CI_PROJECT_DIR/qodana --save-report --report-dir=$CI_PROJECT_DIR/qodana/report
      artifacts:
        paths:
          - qodana
    ```

### Using existing profile

This section is intended for users familiar with configuring code analysis via [IntelliJ inspection profiles](https://www.jetbrains.com/help/idea/customizing-profiles.html).

You can pass the reference to the existing profile via [multiple ways](https://github.com/JetBrains/Qodana/blob/main/Docker/techs.md#order-of-resolving-profile). Here are some examples:

- Mapping profile to `/data/profile.xml` inside of container:
     ```
        docker run --rm -it -p 8080:8080 \
            -v <source-directory>/:/data/project/ \
            -v <output-directory>/:/data/results/ \
            -v <inspection-profile.xml>:/data/profile.xml
            jetbrains/qodana --show-report
       ```
  
- Using name of profile in your project `.idea/inspectionProfiles/` folder:
     ```
        docker run --rm -it -p 8080:8080 \
            -v <source-directory>/:/data/project/ \
            -v <output-directory>/:/data/results/ \
            jetbrains/qodana --show-report -profileName php.extended
       ```

### Configure via qodana.yaml

The `qodana.yaml` file will be automatically recognised and used for the analysis configuration, so that you don't need to pass any additional parameters.  
The references to the inspection profiles will be resolved [in a particular order](techs.md#order-of-resolving-profile). To learn about the format, refer to the [`qodana.yaml` documentation](../General/qodana-yaml.md).

### Plugins management

Paid plugins are yet unsupported, each vendor must clarify licenseing terms for CI usage and collaborate with us to make it work.

Any free IntellJ platform plugins or your custom plugin can be added by mounting it to the container plugins' directory using the follwoing command:

```
docker run ... -v /your/custom/path/%pluginName%:/opt/idea/plugins/%pluginName% jetbrains/qodana
```

Please refer to [this guide](techs.md) for more details.

### Usage statistics

According to the [JetBrains EAP user agreement](https://www.jetbrains.com/legal/agreements/user_eap.html), we can use third-party services to analyze the usage of our features for further improving the user experience. All data will be collected [anonymously](https://www.jetbrains.com/company/privacy.html). You can disable the reporting of usage statistics by adjusting the options of the Docker command you use. Refer to [this guide](techs.md) for details.

### License

By using the Qodana Docker image, you agree to the [JetBrains EAP user agreement](https://www.jetbrains.com/legal/agreements/user_eap.html) and [JetBrains privacy policy](https://www.jetbrains.com/company/privacy.html).  
The Docker image includes evaluation license, which will expire in 30 days. Please ensure you pull a new image on time.

### Contact

Contact us at [qodana-support@jetbrains.com](mailto:qodana-support@jetbrains.com) or via [our issue tracker](https://youtrack.jetbrains.com/newIssue?project=QD). We are eager to receive your feedback on the existing Qodana functionality and learn what other features you miss in it.
