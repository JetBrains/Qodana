# Qodana Docker Image

![official JetBrains project](https://jb.gg/badges/official-flat-square.svg)
![Docker Stars](https://img.shields.io/docker/stars/jetbrains/qodana.svg)
![Docker Pulls](https://img.shields.io/docker/pulls/jetbrains/qodana.svg)

![EAP](../resources/eap-alert.png)

Supported tags: 2020.3-eap, latest (points to 2020.3-eap)

## General

This Docker image lets you to perform [static analysis](https://en.wikipedia.org/wiki/Static_program_analysis) of your 
code base. The current version [supports](../General/supported-technologies.md) PHP, Java and Kotlin, more languages and technologies are coming.

We provide two options optimized for different scenarios:
- Running the analysis on a regular basis as a part of your continuous integration (*CI-based execution*)
- Single-shot analysis (performed *locally*, for example) 

If you prefer the first option and have established continuous integration (CI) support for your project, this page 
  will guide your through all possibilities. If you don't have any CI for your project, we encourage you to try 
  JetBrains TeamCity either on-premise or in the cloud. In this case you can switch to our [TeamCity plugin](https://github.com/JetBrains/Qodana/tree/main/TeamCity%20Plugin) as it gives more options. 


If you are familiar with [JetBrains IDEs code inspections](https://www.jetbrains.com/help/idea/code-inspection.html)
and know what to expect from the static analysis outside the editor, you can start with the [using existing profile](README.md#using-existing-profile) section. 


If you are just starting in the field, we recommend beginning with the [default setup](README.md#quick-start-with-recommended-profile) we provide. You will see the 
results of most common checks performed on your code base and then [adjust them](README.md#how-configure) to better cover your needs.


### Quick start with a recommended profile

*To run analysis locally*
1) Pull the image from Docker Hub Registry: 
   ```
   docker pull jetbrains/qodana
   ```
2) Run the following command:
   ```
   docker run -v <source-folder>/:/data/project/ \
              -v <output-folder>/:/data/results/ \
              -p 8080:8080 \
   jetbrains/qodana --show-report
   ```
   Note that `source-folder` and `output-folder` are the full local paths on your machines to the project 
   source code folder and the analysis results folder accordingly.
   
   This command will run the analysis on your source code and start the web server to give you a convenient way to 
   the see the results. Open `http://locahost:8080` in your browser to examine the found problems and performed checks. Here, you can also re-configure the analysis. See the [UI section](../UI/README.md) of 
   this guide for details.

   In case you don't need the user interface and prefer to study raw data, use the following command: 
   ```
   docker run -v <source-folder>/:/data/project/ \
              -v <output-folder>/:/data/results/ \             
   jetbrains/qodana 
   ```
   
   The `output-folder` will contain [all the necessary data](../General/output.md#basic-output). You can further tune the command as described in the [technical guide](techs.md).
   
   If you run analysis several times in a row, ensure you've cleaned the result folder before using it in `docker run` again. 
   

*To run analysis in CI*
1) Ensure the image is pulled from the Docker Hub Registry:
   ```
    docker pull jetbrains/qodana
   ```
2) Use the following command as the task:
   ```
    docker run \ 
        -v <source-folder>/:/data/project/ \
        -v <output-folder>/:/data/results/ \
        jetbrains/qodana
   ```
  
   Note that `source-folder` and `output-folder` are the full paths to the project 
   source code folder, and the analysis results folder accordingly. 
   The `output-folder` will contain the [following output](../General/output.md#basic-output).
   
   
### Using existing profile

In this section, we assume that you are familiar with the concept of configuring code analysis via [IntelliJ 
inspection profiles](https://www.jetbrains.com/help/idea/customizing-profiles.html). 

You can pass the reference to the existing profile either via the additional parameter `-v <inspection-profile.
xml>:/data/profile.xml` to the `docker run` command or via a [qodana.yaml](#configure-via-qodanayaml) added to your project's root folder.

With the additional parameter provided, the resulting command will look as follows:
- For local execution with results in the UI:
 ```
    docker run -v <source-folder>/:/data/project/ \
              -v <output-folder>/:/data/results/ \
              -v <inspection-profile.xml>:/data/profile.xml
              -p 8080:8080 \
               jetbrains/qodana --show-report
   ```
- For CI-based execution:
```
    docker run \ 
        -v <source-folder>/:/data/project/ \
        -v <output-folder>/:/data/results/ \
        -v <inspection-profile.xml>:/data/profile.xml
        jetbrains/qodana
   ```
### Configure via qodana.yaml

The `qodana.yaml` file will be 
automatically recognised and used for the analysis configuration, so that you don't need to pass any additional parameters.
The references to the inspection profiles will be resolved in [a particular order](techs.md#order-of-resolving-profile). To learn about the format, refer to the [qodana.yaml](../General/qodana-yaml.md) documentation.

### Usage statistics
According to [JetBrains EAP user agreement](https://www.jetbrains.com/legal/agreements/user_eap.html) we may use third-party services to analyze feature usage for the further user experience improving. All data will be collected [anonymously](https://www.jetbrains.com/company/privacy.html). 
You can deprecate the usage statistic reporting y adjusting the options of the docker command you use. Please refer to [this](techs.md) guide. 

### License
Using Qodana docker image you agree to [JetBrains EAP user agreement](https://www.jetbrains.com/legal/agreements/user_eap.html) and [JetBrains privacy policy](https://www.jetbrains.com/company/privacy.html).
The docker image includes evaluation license which will expire in 30-day. Please ensure you pull a new image on time. 

### Contact
Contact us at [qodana-support@jetbrains.com](mailto:qodana-support@jetbrains.com) or via [our issue tracker](https://youtrack.jetbrains.com/newIssue?project=QD). We eagerly want your feedback on what's already there and if there are any features that we miss.