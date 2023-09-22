[//]: # (title: Visual Studio Code)

Visual Studio Code is a source code editor available for Windows, macOS and Linux. It comes with built-in support for 
JavaScript, TypeScript and Node.js and provides extensions for other languages and runtimes 
(such as C++, C#, Java, Python, PHP, Go, .NET).

This section shows how to use Visual Studio Code version 1.81 and later for overviewing %product% reports from
[Qodana Cloud](cloud-about.xml).

## Before you start

Make sure that you have a Qodana Cloud [project](cloud-projects.xml), and this project has at 
least one inspection [report](cloud-overview-reports.xml) related to the project opened by Visual Studio Code. Also,
make sure that you have accepted the [%product% Terms of Service](https://www.jetbrains.com/legal/docs/agreements/qodana/license/).

Finally, check whether Java 11 or never is available on your machine running the `java -version` command. If necessary, 
install Java on your local machine.  

## Configure the plugin

In Visual Studio Code, install the **Qodana Cloud Plugin**. After installation, you can configure it.

<img src="vscode-settings.png" dark-src="vscode-settings_dark.png" width="706" alt="Qodana settings in VS Code" border-effect="line"/>

The configuration section contains the following options:

<table>
<tr>
<td>Option</td>
<td>Description</td>
</tr>
<tr>
<td>Path Prefix</td>
<td><p>In case the report does not appear in the <menupath>PROBLEMS</menupath> tab, you can override the project path prefix. 
Here is the rule how the full path to project file is composed:</p>
<p>Full Path = Workspace + Path Prefix + Path in SARIF</p>
<p>Here are examples how to define the correct path prefix:</p>
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
<p>You can refer to the Qodana Cloud report within the Files section to see how the <menupath>Path in SARIF</menupath> is set.</p>
<p>Feel free to commit the <code>.vscode/settings.json</code> to your repository to share the Qodana settings with your team!</p>
</td>
</tr>
<tr>
<td>Project ID</td>
<td><p>The ID contained in your Qodana Cloud project URL. This URL and has the following structure: 
<code>https://qodana.cloud/projects/PROJECT_ID/reports/REPORT_ID</code>. From this URL, use only <code>PROJECT_ID</code>.
For example, from the URL <code>https://qodana.cloud/projects/AGvmx/reports/EDKYd</code> you will need <code>AGvmx</code>.</p>
<p>Alternatively, you can get the Project ID value by opening the project from the 
<a href="ui-overview.md" anchor="ui-overview-actual-problems">Qodana Cloud report</a> using the 
<menupath>Open file in ...</menupath> button and choosing Visual Studio Code as the tool for opening. </p>
</td>
</tr>
</table>

In the status bar of the Visual Studio Code UI, you can find the **Qodana** icon. This icon can have the following states:

* **Settings are not valid** means that you need to configure your plugin. To do it, you can click this icon, which will 
redirect you to the plugin configuration page.
* **Not attached to report** means that you have configured the plugin, but it did not yet download the report. To 
continue, you need to authorize in Qodana Cloud.
* **Attached to report** means that the report was downloaded from Qodana Cloud, and it should be available for 
[overviewing](#Overview+inspection+reports) in the Visual Studio Code UI. 
* 
## Overview inspection reports

Once configured, the plugin connects and downloads the latest %product% report from Qodana Cloud, and you can overview 
it in the **PROBLEMS** tab of Visual Studio Code. 

<img src="vscode-problems-tab.png" dark-src="vscode-problems-tab_dark.png" width="706" alt="The PROBLEMS in VS Code" animated="true" border-effect="line"/>

To disconnect from Qodana Cloud, you can apply the **Qodana: Reset authentication** command. 

To reset all settings and credentials, you can use the **Qodana: Reset all settings** command.

 