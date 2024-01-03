[//]: # (title: Visual Studio Code)

Visual Studio Code is a source code editor available for Windows, macOS and Linux. This section shows how to use Visual 
Studio Code version 1.81 and later for viewing %product% reports from [Qodana Cloud](cloud-about.topic).

## Before you start

Make sure that you have a Qodana Cloud [project](cloud-projects.topic), and this project has at 
least one inspection [report](cloud-overview-reports.topic) related to the project opened by Visual Studio Code. 
Also, check whether Java 11 or later is installed on your machine by running the `java -version` command. If necessary, 
install Java on your local machine.  

Download and install **Qodana** the extension from the 
[Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=JetBrains.qodana-code) website, 
or by navigating to the **Extensions** view in Visual Studio Code.  

## Configure the extension
{id="vs-code-configure-extension"}

Here is an overview of the **Qodana** configuration page. 

<img src="vscode-settings.png" dark-src="vscode-settings_dark.png" width="706" alt="Qodana settings in VS Code" border-effect="line"/>

You can configure the extension using the following settings:

<table>
<tr>
<td>Setting</td>
<td>Description</td>
</tr>
<tr>
<td>Path Prefix</td>
<td><p>If necessary, you can override the project path prefix. Here is the rule how the full path to project files is composed:</p>
<p>Full Path = Workspace + Path Prefix + Path in a <a href="qodana-sarif-output.md">SARIF</a> file</p>
<p>Here are examples of how to define the correct path prefix:</p>
<table>
<tr>
<td>Full path</td>
<td>Path in SARIF</td>
<td>Workspace</td>
<td>Path prefix</td>
</tr>
<tr>
<td>/foo/bar/baz/file</td>
<td>baz/file</td>
<td>/foo/bar</td>
<td>(empty, no value)</td>
</tr>
<tr>
<td>/foo/bar/baz/file</td>
<td>baz/file</td>
<td>/foo/bar/baz</td>
<td>..</td>
</tr>
<tr>
<td>/foo/bar/baz/file</td>
<td>file</td>
<td>/foo/bar</td>
<td>baz</td>
</tr>
</table>
<p>In a <a href="ui-overview.md">Qodana Cloud report</a>, you can check with the <menupath>Files</menupath> section to 
see how the path in a SARIF file is set.</p>
<p>Feel free to commit the <code>.vscode/settings.json</code> to your repository to share the Qodana settings with your team!</p>
</td>
</tr>
<tr>
<td>Project ID</td>
<td>
<p>You can get the Project ID value by opening the project from the 
<a href="ui-overview.md" anchor="ui-overview-actual-problems">Qodana Cloud report</a> using the 
<menupath>Open file in ...</menupath> button and choosing Visual Studio Code as the tool for opening. </p>
<p>Alternatively, the ID is contained in your Qodana Cloud project URL. This URL has the following structure: 
<code>https://qodana.cloud/projects/PROJECT_ID/reports/REPORT_ID</code>. From this URL, use only <code>PROJECT_ID</code>.
For example, from the URL <code>https://qodana.cloud/projects/AGvmx/reports/EDKYd</code> you will need <code>AGvmx</code>.</p>
</td>
</tr>
</table>

In the status bar of the Visual Studio Code UI, you can find the **Qodana** icon. This icon can have the following states:

* **Settings are not valid** means that you need to configure the extension. To do it, you can click this icon, which will 
redirect you to the extension configuration page.
* **Not attached to report** means that you have configured the extension, but the report has not been downloaded yet. To 
download the report, click the icon. 
* **Attached to report** means that the report was downloaded from Qodana Cloud, and now you can 
[view](#vs-code-overview-reports) it using Visual Studio Code. 

## Inspection report overview
{id="vs-code-overview-reports"}

Once configured, the extension connects to Qodana Cloud and downloads the latest %product% report, so you can see 
it in the **PROBLEMS** tab of Visual Studio Code. If you still do not see the report in the **PROBLEMS** tab, configure 
the [**Path prefix**](#vs-code-configure-extension) setting. 

On this tab, you can click problem items and navigate to code fragments where %product% detected them.

<img src="vscode-problems-tab.png" dark-src="vscode-problems-tab_dark.png" width="706" alt="The PROBLEMS in VS Code" animated="true" border-effect="line"/>

## Troubleshooting
{id="vs-code-troubleshooting"}

### I need to switch to another Qodana Cloud account

You can use the **Qodana: Reset authentication** command to switch between Qodana Cloud accounts without clearing settings. 
This can be useful in case you have several organizations under different Qodana Cloud accounts.

### I cannot get %product% reports using current settings

You can use the **Qodana: Reset all settings** command to reset all settings and credentials and try to configure 
the extension again, or use other settings.

 