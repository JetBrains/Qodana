[//]: # (title: Qodana IDE plugin)

The Qodana IDE plugin is a JetBrains IDE plugin that binds Qodana reports, both stored locally and in Qodana Cloud, 
with your project opened in the IDE. 

By default, this plugin is available in all JetBrains IDEs starting from version 2022.3. Otherwise, you can install it
using [JetBrains Marketplace](https://plugins.jetbrains.com/plugin/16938-qodana).

<note>The functionalities described in this section are available only with the nightly images of IntelliJ IDEA and PhpStorm.</note>

## Before you start

1. Make sure your preferred IDE is installed via [JetBrains Toolbox App](https://www.jetbrains.com/toolbox-app/).
2. Install the plugin for the IDE as described in the [IntelliJ IDEA Documentation](https://www.jetbrains.com/help/idea/?Managing_Plugins). IDE versions 2021.2 and later are supported. Starting from 2021.3, this plugin is installed by default.
3. To open Qodana reports from your local storage, make sure that you previously opened the project by the IDE at least 
   one time. This action establishes the link between the %product% report and your IDE.



<anchor name="plugin-qodana-cloud-login"/>

## Log in to Qodana Cloud

Logging in to Qodana Cloud is required before [linking your project](#plugin-link-project-with-cloud) with any Qodana Cloud-based project.

<procedure>
<step>
In your IDE, navigate to <menupath>Tools | Qodana | Log in to Qodana</menupath>. 

<img src="ide-plugin-login-1.png" dark-src="ide-plugin-login-1_dark.png" width="706" alt="Logging into Qodana Cloud" border-effect="line"/>

Alternatively, you can click the **Log in to Qodana** button of the **[Qodana](#tab-overview-buttons)** tab.

</step>
<step>
On the <menupath>Settings | Tools | Qodana </menupath> window, click <menupath>Log in</menupath>. This will redirect you 
to the authentication page.

<img src="ide-plugin-login-2.png" dark-src="ide-plugin-login-2_dark.png" width="594" alt="The log in button" border-effect="line"/>

</step>
<step>On the authentication page, complete the <a href="cloud-get-access.xml">authentication step</a>.</step>
</procedure>

<anchor name="plugin-link-project-with-cloud"/>

## Link your project with Qodana Cloud

You can synchronize your project with Qodana Cloud by linking it with your <a href="cloud-projects.xml">project</a> based
in Qodana Cloud.

<note>You can link your project only after you <a anchor="plugin-qodana-cloud-login">log in to Qodana Cloud</a>.</note>

<note>To successfully link your project, it should already be inspected by Qodana at least once with the report
uploaded to Qodana Cloud, so linking occurs on the basis of the previous report uploading.</note>

<procedure>
<step>In your IDE, navigate to <menupath>Tools | Qodana </menupath>, and then click 
<menupath>Link Project with Cloud</menupath>. 

<img src="ide-plugin-linking-1.png" dark-src="ide-plugin-linking-1_dark.png" width="706" alt="Linking the project with Qodana Cloud" border-effect="line"/>

Alternatively, you can click the **Link project with Cloud** button of the **[Qodana](#tab-overview-buttons)** tab.

</step>
<step>
On the <menupath>Link Project with Qodana Cloud</menupath> window, select the Qodana Cloud project you would like to
link your local project with, and then click <menupath>Apply</menupath> If necessary, you can create a new project
that your local project will be linked to.

<img src="ide-plugin-linking-2.png" dark-src="ide-plugin-linking-2_dark.png" width="594" alt="The link project with Qodana Cloud window" border-effect="line"/>

</step>

</procedure>

After linking, you can overview the downloaded report using the <menupath>Qodana</menupath> tab of the <menupath>Problems</menupath>
window as shown in the [](#Overview+results+in+the+IDE) section, or [run %product%](#plugin-run-qodana) on your local machine.


<anchor name="plugin-run-qodana"/>

## Run Qodana

<procedure>

<step>
After you open your project in the IDE, navigate to <menupath>Tools | Qodana | Run Qodana</menupath>.

<img src="ide-plugin-run-qodana-1.png" dark-src="ide-plugin-run-qodana-1_dark.png" width="706" alt="Overview of the Qodana tab" border-effect="line"/>

</step>
<step>
Choose whether you would like to upload the inspection result to Qodana Cloud, or save them in your local filesystem.

<img src="ide-plugin-report-type.png" dark-src="ide-plugin-report-type_dark.png" width="706" alt="Choosing the report type" border-effect="line"/>

</step>

<step>
Depending on your choice, you will need to perform a certain set of actions:

<tabs>
<tab title="Run locally" id="ide-plugin-keep-local">

Provide additional configuration parameters, see the [](qodana-yaml.md) section for details.

<img src="ide-plugin-run-config.png" dark-src="ide-plugin-run-config_dark.png" width="706" alt="Configuring Qodana" border-effect="line"/>

Once the code inspection stage is complete, you can overview inspection results in your browser. To do this, in the 
lower-right corner of the IDE click the **Show results in browser** link. 

<img src="ide-plugin-report-open-locally.png" dark-src="ide-plugin-report-open-locally_dark.png" width="706" alt="Overview the report locally" border-effect="line"/>

</tab>
<tab title="Run with Cloud" id="ide-plugin-cloud-upload">

If necessary, log in to Qodana Cloud from your IDE.

<img src="ide-plugin-run-qodana-login.png" dark-src="ide-plugin-run-qodana-login_dark.png" width="706" alt="Logging in Qodana" border-effect="line"/>

If necessary, select a team and link your local project with the project in Qodana Cloud, or create a new project.

<img src="ide-plugin-run-qodana-link-project.png" dark-src="ide-plugin-run-qodana-link-project_dark.png" width="706" alt="Logging in to Qodana Cloud" border-effect="line"/>

Provide additional configuration parameters, see the [](qodana-yaml.md) section for details.

<img src="ide-plugin-run-config.png" dark-src="ide-plugin-run-config_dark.png" width="706" alt="Configuring Qodana" border-effect="line"/>

Once the code inspection stage is complete, you can overview inspection results in your browser. To do this, in the
lower-right corner of the IDE click the **Open qodana.cloud** link.

<img src="ide-plugin-report-open-cloud.png" dark-src="ide-plugin-report-open-cloud_dark.png" width="706" alt="Overview the report locally" border-effect="line"/>

</tab>
</tabs>

</step>

</procedure>

You can [overview inspection results](#plugin-overview-results-in-ide) in your IDE.

To learn more about %product% HTML reports, see the [](ui-overview.md) section.

<anchor name="plugin-overview-results-in-ide"/>

## Overview results in the IDE

Once the [inspection stage](#plugin-run-qodana) is complete, the inspection report is available in the **Qodana** tab of the
**Problems** window of your IDE . This window is located in the lower-left part of the IDE user interface, and opens automatically.

<img src="ide-plugin-tab-overview-1.png" dark-src="ide-plugin-tab-overview-1_dark.png" width="706" alt="Overview of the Qodana tab" border-effect="line"/>

It contains the problems grouped by the severity level, inspection category, inspection name, and files where
the problems were detected.

By clicking a specific problem, you can jump to the code fragment containing it. 

<img src="ide-plugin-code-highlighting.png" dark-src="ide-plugin-code-highlighting_dark.png" width="706" alt="Code highlighting from the Qodana IDE plugin" animated="true" border-effect="line"/>

In the upper-left corner of the **Qodana** window, you can find two buttons. 

<img src="ide-plugin-left-window-buttons.png" dark-src="ide-plugin-left-window-buttons_dark.png" width="706" alt="Buttons in the upper-left corner of the Qodana window" border-effect="line"/>

<anchor name="tab-overview-buttons"/>

The **Log in to Qodana** button lets you log in to Qodana Cloud. This action is a prerequisite for linking your project
with Qodana Cloud-based projects. Alternatively, you can do it using the
**Tools | Qodana | Log in to Qodana** menu of your IDE as [described here](#plugin-qodana-cloud-login).

Below is the **Link project with Cloud** button that you can use for linking your project with a specific project in 
Qodana Cloud. This lets you exchange %product% reports between your local project and Qodana Cloud.
Alternatively, you can link your project using the **Tools | Qodana | Link Project with Cloud** menu
of your IDE as [described here](#plugin-link-project-with-cloud).

<!-- This can be renamed for open a local report -->

<anchor name="plugin-update-report"/>

## Update report

To update the report, you should first [link](#plugin-link-project-with-cloud) it with Qodana Cloud.

In your IDE, navigate to <menupath>Tools | Qodana</menupath>, uncheck
**Cloud Project &lt;project-name&gt;**, and then check it back.

<img src="ide-plugin-update-report-1.png" dark-src="ide-plugin-update-report-1_dark.png" width="706" alt="Updating the report using the Tools menu" border-effect="line"/>

Alternatively, in the <menupath>Qodana</menupath> tab of the <menupath>Problems</menupath> window, you can uncheck
<menupath>Cloud Project &lt;project-name&gt;</menupath>, and then check it back.

<img src="ide-plugin-update-report-2.png" dark-src="ide-plugin-update-report-2_dark.png" width="706" alt="Updating the report using the Qodana tab" border-effect="line"/>

<anchor name="plugin-open-from-local-storage"/>

## Open report from the Qodana UI

In a Qodana HTML report, choose a problem and click **Open file in \<IDE\>**.

<img src="qd-report-open-in-ide.png" dark-src="qd-report-open-in-ide_dark.png" alt="The Open in IDE button" width="706" border-effect="line"/>


## Open report from a local storage

In the IDE, go to <menupath>Tools | Qodana | Open local report</menupath> and select the
<code>qodana.sarif.json</code> report file you would like to open.

<img src="ide-plugin-local-file-1.png" dark-src="ide-plugin-local-file-1_dark.png" width="706" alt="Opening a local Qodana report" border-effect="line"/>

After opening, you can [overview and navigate](#plugin-overview-results-in-ide) in the detected problems using your IDE. 
In case a problem was fixed before opening the <code>qodana.sarif.json</code> file, it is marked as
<code>[Not present]</code>.