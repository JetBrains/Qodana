[//]: # (title: TeamCity Plugin Configuration)

The main Qodana functionality comes from the 'engine' shaped into the Docker image. If you want to go beyond the boundaries of the default settings, refer to the [Docker image guide](https://www.jetbrains.com/help/qodana/qodana-intellij-docker-readme.html). Note that you don't need to write `docker run` on your own: the plugin will do it for you. You can just use all other options and provide them via the dedicated UI or DSL properties.

## Add Qodana analysis to your project on TeamCity

### Prerequisites

- You use TeamCity as a build server for your project. If not, learn how to do it in [TeamCity documentation](https://www.jetbrains.com/help/teamcity/teamcity-documentation.html).
- Your project language is included in the list of fully [supported technologies](https://www.jetbrains.com/help/qodana/supported-technologies.html).
- The [Qodana plugin](https://plugins.jetbrains.com/plugin/15498-qodana) is installed on your TeamCity server (you can do it yourself or contact the server's administrator to do this).


### Add the Qodana runner to your build
{id=add-qodana-runner}

1. On TeamCity left navigation panel, select your project and go to **Edit configuration | Build Steps**.

[//]: # "Can't find how to add qodana.yaml "

2. Select **Add build step | Add qodana.yaml**.

   Write a custom `qodana.yaml` script that will be added to your working directory. Alternatively, you can put a custom `qodana.yaml` file to the root of your repository or, for repositories that are not yours, to the root of a forked repository.

[//]: # "?make it a separate ### subsection/reference this subsection"

3. Select **Add build step** and for **Runner type**, specify **Qodana**.

   In the following steps, specify additional parameters for Qodana's `docker run` command, which you can also see in the [readme for Qodana IntelliJ Docker Image](qodana-intellij-docker-readme.md).

4. Select the checkbox next to **Code Inspections** (stands for the Qodana IntelliJ linter).

   You can disable certain inspections later using [`qodana.yaml`](qodana-yaml.md#exclude-inspection) or [Profile settings](ui-overview.md#Adjust+your+inspection+profile) in your HTML report.

5. For **Root of the project for the analysis**, specify the path to your project root where its configuration files are located. Leave empty for ??the **Checkout directory** specified on the **Version Control Settings** tab (system agent working directory).

6. For **Image name:tag**, specify an image name. 
   
   **Public image (EAP)** points to the default `jetbrains/qodana:latest`. 
   
   **Custom** allows to specify your own value in the field that appear below or .
   
   Or you can click the question mark sign "?" to select an image from the Docker registry with Qodana images.

7. For **Profile**, select 
   - **Default** (`qodana.recommended`). 
   - **Empty** (no inspections included).
   - **Name of embedded profile** and specify the name of a profile available for your project in IntelliJ IDEA.
     
     **Note**: Make sure that the .idea directory with this profile .xml file is added to your working directory.
     
   - **Path to IntelliJ profile** and specify the path to the necessary .xml file in your working directory. Not recommended because in this case you will not be able to edit this profile from IntelliJ IDEA.
    
      IDEA profiles include customized sets of [inspections](https://www.jetbrains.com/help/idea/code-inspection.html). You can enable and disable them via [`qodana.yaml`](qodana-yaml.md#exclude-inspection) or in the [Profile settings](ui-overview.md#Adjust+your+inspection+profile) of your HTML report.
     

8. For **Disabled plugins**, select
   - **Default** or **None** to use all the plugins of the IntelliJ Platform included in the Qodana Docker image.
   - **Custom** or **File** to specify your own list of the plugins to disable. However, currently there is no need to disable any plugins.
     
9. For **Additional parameters for JVM**, you can specify more parameters to run the Docker image such as the logging level.

10. In **Additional arguments for Docker run**, you can specify any arguments accepted by the Docker image of the Qodana IntelliJ linter. For example, `-d` or `-changes` as you can see in the [docker techs for Qodana IntelliJ](qodana-intellij-docker-techs.md).

11. Click **Save**. Now you can run a build with new Qodana inspection parameters you specified.


[//]: # "" 


## Add more runners to your build
You can add [Clone Finder](about-clone-finder.md) or [License Audit](about-license-audit.md) so that their inspections are added to your build steps.

When viewing specific build analysis results later, you can disable certain runners and inspections and save such configuration for future reports in [`qodana.yaml`](qodana-yaml.md).

### Prerequisites for adding more runners

- Install the Qodana plugin.
- Install the plugins for Clone Finder or License Audit as necessary.

### Add the Clone Finder runner

....

### Add the License Audit runner 

....

## Advanced configuration

Advanced configuration lets you report all found problems via the standard TeamCity tests mechanism. It means
you can assign investigations, mute, see history, and do everything else you can do with regular tests in TeamCity. Qodana IntelliJ reports tests in four different ways:

- per problem
- per inspection type
- per inspection type/per module (if this information is available)
- per inspection type/per file

## Logs

On TeamCity, open your project build page and go to the **Build Log** tab. Here you can find a standard shell output where errors are highlighted in yellow.

For more details, go to the **Artifacts** tab, where more detailed logs for TeamCity and Qodana are provided.

For more about TeamCity logs, see [TeamCity Documentation](https://www.jetbrains.com/help/teamcity/teamcity-documentation.html).

[//]: # "is adding this section and info in it OK?"