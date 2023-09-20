[//]: # (title: Visual Studio Code)

Visual Studio Code is a source code editor available for Windows, macOS and Linux. It comes with built-in support for 
JavaScript, TypeScript and Node.js and provides extensions for other languages and runtimes 
(such as C++, C#, Java, Python, PHP, Go, .NET).

This section shows how to use Visual Studio Code for overviewing %product% reports from
[Qodana Cloud](cloud-about.xml).

## Before you start

Make sure that you have a Qodana Cloud [project](cloud-projects.xml), and this project has at 
least one inspection [report](cloud-overview-reports.xml) related to the project on opened by Visual Studio Code. 

Check whether Java is available on your machine running the `java -version` command. If necessary, install Java on your 
local machine.  

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
<td>License Accepted</td>
<td>Confirms that you have accepted the <a href="https://www.jetbrains.com/legal/docs/agreements/qodana/license/">%product% Terms of Service</a></td>
</tr>
<tr>
<td>Path Prefix</td>
<td>If necessary, you can specify the correct project prefix. Suppose that in Visual Studio Code you opened a project contained in the <code>/foo</code> directory,
and this directory contains the <code>bar</code> subdirectory.
In this case, if the %product% report contains the <code>/bar/&lt;filename&gt;</code> file paths, then the <code>foo</code> prefix is required. If  
the %product% report specifies only file names without directories, then <code>/foo/bar</code> has to be prefixed.
</td>
</tr>
<tr>
<td>Project ID</td>
<td>The ID contained in your Qodana Cloud project URL. This URL and has the following structure: 
<code>https://qodana.cloud/projects/PROJECT_ID/reports/REPORT_ID</code>. From this URL, use only <code>PROJECT_ID</code>.
For example, from the URL <code>https://qodana.cloud/projects/AGvmx/reports/EDKYd</code> you will need <code>AGvmx</code>.
</td>
</tr>
</table>

## Overview inspection reports

Once configured, the plugin connects and downloads the latest %product% report from Qodana Cloud, and you can overview 
it in the **PROBLEMS** tab of Visual Studio Code. 

<img src="vscode-problems-tab.png" dark-src="vscode-problems-tab_dark.png" width="706" alt="The PROBLEMS in VS Code" animated="true" border-effect="line"/>

To disconnect from Qodana Cloud, you can apply the **Qodana: Reset authentication** command. 