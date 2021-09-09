[//]: # (title: TeamCity plugin configuration)

The main Qodana functionality comes from the 'engine' shaped into the Docker image. If you want to go beyond the boundaries of the default settings, refer to the [Docker image guide](https://www.jetbrains.com/help/qodana/qodana-intellij-docker-readme.html). Note that you don't need to write `docker run` on your own: the plugin will do it for you. You can just use all other options and provide them via the dedicated UI or DSL properties.

## Add Qodana analysis to your project builds on TeamCity

### Prerequisites

- You use TeamCity as a build server for your project. If not, learn how to do it in [TeamCity documentation](https://www.jetbrains.com/help/teamcity/teamcity-documentation.html).
- Your project language is included in the list of fully [supported technologies](https://www.jetbrains.com/help/qodana/supported-technologies.html).
- The [Qodana plugin](https://plugins.jetbrains.com/plugin/15498-qodana) is installed on your TeamCity server (you can do it yourself or contact the server's administrator to do this).


### (Optional) Add a configuration script
{id="add-script"}

Custom profile configuration for Qodana linters is stored in `qodana.yaml`. When using a CI system, you need to put this file to the working directory manually. Alternatively, you can write a script that will do it for you.

1. On TeamCity left navigation panel, select your project and go to **Edit configuration | Build Steps**.

2. Select **Add build step | Command Line**.

3. For **Step name**, specify an optional name, for example, "Add qodana.yaml".

4. For **Run**, select **Custom script**.

5. In the **Custom script** editor, write a script that adds a custom `qodana.yaml` to the working directory. 

   In the example below, the script appends the following inspection exclusions to the configuration file:

```shell
#!/bin/sh

FILE="./qodana.yaml"

/bin/cat <<EOM >$FILE
exclude:
  - name: Annotator
  - name: AnotherInspectionId
    paths:
      - relative/path
      - another/relative/path
  - name: CloneFinder
  - name: ProhibitedDependencyLicense
  
EOM  
```
   
[//]: # "OK?"  


### Add a Qodana runner

1. On TeamCity left navigation panel, select your project and go to **Edit configuration | Build Steps**.

2. Select **Add build step** and for **Runner type**, specify **Qodana**.

   In the following steps, specify additional parameters for Qodana's `docker run` command, which you can also see in the [Qodana IntelliJ Docker Image readme](https://www.jetbrains.com/help/qodana/qodana-intellij-docker-readme.html).

3. Select the checkbox next to **Code Inspections** (stands for the Qodana IntelliJ linter).

   >You can disable certain inspections later via [`qodana.yaml`](https://www.jetbrains.com/help/qodana/qodana-yaml.html#exclude-paths) or [Profile settings](https://www.jetbrains.com/help/qodana/ui-overview.html#Adjust+your+inspection+profile) in your HTML report.

4. For **Root of the project for the analysis**, specify the path to your project root where its configuration files are located. Leave empty for the **Checkout directory** specified on the **Version Control Settings** tab (system agent working directory).

5. For **Image name:tag**, specify an image name. 
   
   **Public image (EAP)** points to the default `jetbrains/qodana:latest`. 
   
   **Custom** allows to specify your own value in the field that appears below.
   
   Or you can click the question mark sign "**?**" to select an image from the Docker registry with Qodana images.

6. For **Profile**, select 
   - **Default** (`qodana.recommended`). 
   - **Name of embedded profile** and specify the name of a profile available for your project in IntelliJ IDEA.
     
     >Make sure that the `.idea` directory with this profile's `.xml` file is added to your working directory.
     
   - **Path to IntelliJ profile** and specify the path to the necessary `.xml` file in your working directory. Not recommended because in this case you will not be able to edit this profile from IntelliJ IDEA.
    
      >IDEA profiles include customized sets of [inspections](https://www.jetbrains.com/help/idea/code-inspection.html). You can enable and disable them via [`qodana.yaml`](https://www.jetbrains.com/help/qodana/qodana-yaml.html#exclude-paths) or in the [Profile settings](https://www.jetbrains.com/help/qodana/ui-overview.html#Adjust+your+inspection+profile) of your HTML report.
     

7. For **Disabled plugins**, select
   - **Default** or **None** to use all the plugins of the IntelliJ Platform included in the Qodana Docker image.
   - **Custom** or **File** to specify your own list of the plugins to disable. However, currently there is no need to disable any plugins.
     
8. For **Additional parameters for JVM**, you can specify [more parameters](https://www.jetbrains.com/help/qodana/qodana-intellij-docker-techs.html#qodana-execution-tuneup) to run the Docker image such as the logging level.

9. In **Additional arguments for Docker run**, you can specify any arguments accepted by the Docker image of the Qodana IntelliJ linter. For example, `-d` or `-changes` as you can see in the [docker techs for Qodana IntelliJ](https://www.jetbrains.com/help/qodana/qodana-intellij-docker-techs.html#Configuration).

10. Click **Save**. Now you can run a build with new Qodana inspection parameters you specified.


## Add more runners to your build
You can add inspections by [Clone Finder](https://www.jetbrains.com/help/qodana/about-clone-finder.html) or [License Audit](https://www.jetbrains.com/help/qodana/about-license-audit.html) to your build steps.

When viewing analysis results for a specific build later, you can disable certain runners and inspections via [`qodana.yaml`](https://www.jetbrains.com/help/qodana/qodana-yaml.html) and update the [configuration script](#add-script).

[//]: # "correct?"


### Prerequisites for adding more runners

- The Qodana plugin for teamCity is installed.
- The Clone Finder or License Audit plugins for teamCity are installed as necessary.

## Advanced configuration

[//]: # "delete? supplement? ...todo: Failure Conditions based on Qodana metrics"

Advanced configuration lets you report all found problems via the standard TeamCity tests mechanism. It means
you can assign investigations, mute, see history, and do everything else you can do with regular tests in TeamCity. Qodana IntelliJ reports tests in four different ways:

- per problem
- per inspection type
- per inspection type/per module (if this information is available)
- per inspection type/per file

## Logs

On TeamCity, open your project build page and go to the **Build Log** tab. Here you can find a standard shell output where errors are highlighted in yellow.

For more details, go to the **Artifacts** tab, where more detailed logs for TeamCity and Qodana are provided.

For more about TeamCity logs, see [TeamCity documentation](https://www.jetbrains.com/help/teamcity/teamcity-documentation.html).