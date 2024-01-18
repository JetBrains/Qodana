[//]: # (title: TeamCity)

<var name="TeamCityLink" value="www.jetbrains.com/help/teamcity/typed-parameters.html#Password+Type"/>

Starting from `2022.04`, Qodana functionality is available in TeamCity by default. To start using it, these prerequisites
need to be met:

- You use TeamCity as a build server for your project. If not, learn how to do it in [TeamCity documentation](https://www.jetbrains.com/help/teamcity/teamcity-documentation.html).
- Your project language is included in the list of fully [supported technologies](linters.md).
- If you use your own TeamCity agents, make sure that Docker is installed on the agent machines and accessible by the users TeamCity is running under.
  TeamCity agents [hosted by JetBrains](https://www.jetbrains.com/help/teamcity/cloud/supported-platforms-and-environments.html#JetBrains-Hosted+Agents)
  already meet this condition.

<note>Currently, running Qodana on Windows-based build agents of TeamCity is not supported.</note>

### Add a Qodana runner 

Assuming that you have already created your [project](https://www.jetbrains.com/help/teamcity/configure-and-run-your-first-build.html#Create+your+first+project) and configured your build, follow the steps below.    

1. Navigate to your build configuration.

<img src="teamcity-plugin-1.png" alt="Navigating to the build configuration" width="706" border-effect="line"/>

2. On the build configuration page, select **Build Steps** from the **Edit configuration** list.

<img src="teamcity-plugin-2.png" alt="Navigating to the step configuration" width="706" border-effect="line"/>

3. On the **Build steps** page, click the **Add build step** button.

<img src="teamcity-plugin-3.png" alt="Creating a new build step" width="706" border-effect="line"/>

4. From the **Runner type** list, select **Qodana** as a runner. On the **New Build Step** page, you can configure the `Qodana` runner
using the basic options. Otherwise, click **Show advanced options** to expand the list of configuration options.

<img src="teamcity-plugin-4.png" alt="Expanding all configuration options of the Qodana runner" width="706" border-effect="line"/>
   
5. Fill in the fields using this description.

   **Step name** uniquely identifies this step among other build steps.

   **Execute step** configures the build condition that will trigger this build step.
   
   **Working directory** sets the directory for the build process. For more information, see the [TeamCity](https://www.jetbrains.com/help/teamcity/2021.2/build-working-directory.html) documentation. You can leave this field empty if the `Checkout directory` parameter is specified on the **Version Control Settings** tab.

   **Report ID** uniquely identifies the report to let you distinguish between multiple reports when several inspection steps are configured within a single build.

   The **Forward reports to TeamCity tests** checkbox configures %instance% report availability in 
   the [Test](https://www.jetbrains.com/help/teamcity/build-results-page.html#Tests+Tab) tab of TeamCity UI. Using this 
   option, you can view codebase problems along with other problems detected. 

   **Linter** configures the [Qodana Linter](linters.md).

   **Version** is by default set to `Latest`.

   **Inspection profile** defines the inspection profile. For more information, see the [Configure profile](qodana-yaml.md) section.
   The available values are:
      * `Recommended (default)` is the default profile containing a preselected set of IntelliJ inspections 
      * `Embedded profile` lets you select from any available profiles, see the [Default profiles](inspection-profiles.md#Default+profiles) section for details
      * `Path to the IntelliJ profile` lets you specify the path to a custom profile. Make sure that the `.idea` directory containing the profile file is added to your working directory.

   You can disable certain inspections later using the [`qodana.yaml`](qodana-yaml.md#exclude-paths) file or [Profile settings](ui-overview.md#Adjust+your+inspection+profile) in your HTML report.

   **Additional arguments for 'docker run'** configures the arguments accepted by a Docker image, see the [](docker-image-configuration.topic#docker-config-reference-docker-environment) section for details.

   **Additional Qodana arguments** lets you extend the default Qodana functionality, see the [Docker image configuration](docker-image-configuration.topic) page for details.

7. Click **Save**. Now you can run Qodana in the build.

### Configure the project token

The [project token](project-token.md) is required by the paid %instance% [linters](pricing.md#pricing-linters-licenses),
and is optional for using with the Community linters. You can see these sections to learn how to generate the project token:  

* The [](cloud-onboarding.md) section explains how to get the project token generated while first working with Qodana Cloud
* The [](cloud-projects.topic#cloud-manage-projects) section explains how to create a project in the existing Qodana Cloud organization

To apply the generated project token, follow these steps:

1. In the TeamCity UI, open the build step that will run %instance%.
2. In the **Cloud Token** field, insert the [Qodana Cloud token](cloud-projects.topic#cloud-manage-projects) value.

   <img src="cloud-forward-reports-teamcity.png" width="706" alt="Configuring fields in TeamCity" border-effect="line"/>

### (Optional) Add a configuration script
{id="add-script"}

Custom profile configuration for Qodana linters is stored in `qodana.yaml`. When using a CI system, you need to put 
this file to the working directory manually. Alternatively, you can write a script that will do it for you.

1. Navigate to your build configuration.
   
<img src="teamcity-plugin-1.png" alt="Navigating to the build configuration" width="706" border-effect="line"/>

2. On the build configuration page, select **Build Steps** from the **Edit configuration** list.

<img src="teamcity-plugin-2.png" alt="Navigating to the step configuration" width="706" border-effect="line"/>

3. On the **Build steps** page, click the **Add build step** button.

<img src="teamcity-plugin-3.png" alt="Creating a new build step" width="706" border-effect="line"/>

4. From the **Runner type** list, select **Command Line**. On the **New Build Step** page, you can configure the
   `Command Line` runner using the basic options. Otherwise, click **Show advanced options** to expand the list of configuration options.

<img src="teamcity-plugin-5.png" alt="Expanding all configuration options of the Command Line runner" width="706" border-effect="line"/>

5. Fill in the fields using the [Command Line](https://www.jetbrains.com/help/teamcity/command-line.html#General+Settings)
   runner description from the TeamCity documentation portal.

   In the **Custom script** editor, paste a script that adds a custom `qodana.yaml` to the working directory. In the
   example below, the script appends the following inspection exclusions to the configuration file:

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
   - name: ProhibitedDependencyLicense
  
   EOM  
   ```

### Verify inspection results

Now that you have configured and run the build, you can observe inspection results in the TeamCity UI.  

1. Navigate to the project build page. In the **Overview** tab, click the build entry.

<img src="teamcity-plugin-verification-1.png" alt="Navigating to the build entry" width="706" border-effect="line"/>

2. On the build page, navigate to the **Qodana** tab to find the inspection report. To learn more about Qodana 
reports, see the <a href="ui-overview.md"/> section of this documentation.

<img src="teamcity-plugin-verification-2.png" alt="Navigating to the Qodana tab" width="706" border-effect="line"/>


