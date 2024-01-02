[//]: # (title: JetBrains IDEs)

Starting from version 2022.3, you can use [%product%](about-qodana.md) to inspect your codebase for problems and use
the recommendations to eliminate them using JetBrains IDEs installed via 
[JetBrains Toolbox App](https://www.jetbrains.com/toolbox-app/) such as IntelliJ IDEA, PhpStorm, WebStorm, Rider, GoLand, 
PyCharm, and Rider.

<note>Prior to version 2022.3, this functionality was available as a plugin published 
on <a href="https://plugins.jetbrains.com/plugin/16938-qodana">JetBrains Marketplace</a>. However, this plugin can be 
less functional compared to version 2022.3. </note>

Using the IDE, you can:

* [Run %product% locally](#ide-plugin-run-qodana)
* [Configure %product% for running in a CI pipeline](#ide-plugin-cicd)
* [Connect to Qodana Cloud](#ide-plugin-connect-cloud)
* [Open a report from local storage](#ide-plugin-local-report)
* [Study %product% reports in your IDE](#ide-plugin-study-reports)

## UI overview

%product% functionality is available using the <ui-path>Tools | Qodana</ui-path> menu of your IDE.

<img src="ide-plugin-intro-menu.png" dark-src="ide-plugin-intro-menu_dark.png" width="706" alt="The Qodana menu" border-effect="line"/>

You can also have access to %product% using the **Problems | Server-Side Analysis** tool window of your IDE.

<img src="ide-plugin-intro-tool-window.png" dark-src="ide-plugin-intro-tool-window_dark.png" width="706" alt="The Server-Side Analysis tool window" border-effect="line"/>

## Run %product% locally
{id="ide-plugin-run-qodana"}

You can configure and run %product% locally using your IDE, and then forward inspection reports to 
[Qodana Cloud](cloud-about.topic) for storage and analysis purposes.

<procedure>
<step>
   <p>In your IDE, navigate to <ui-path>Tools | Qodana | Try Code Analysis with Qodana</ui-path>.</p> 
</step>
<step>
   <p>In the <ui-path>Run Qodana</ui-path> dialog, click the <ui-path>Try locally</ui-path> button. </p>
   <img src="ide-plugin-run-qodana-1.png" dark-src="ide-plugin-run-qodana-1_dark.png" width="706" alt="First step of the Run Qodana dialog" border-effect="line"/>
</step>
<step>
   <p>In the upper part of the <ui-path>Run Qodana</ui-path> dialog, configure the <a href="qodana-yaml.md"><code>qodana.yaml</code></a> file.</p>
   <p>Under the text field, configure the options to make %product%:</p>
      <list>
         <li><a href="cloud-forward-reports.topic">Forward inspection results</a> to Qodana Cloud using the <a href="cloud-projects.topic" anchor="cloud-manage-projects">project token</a></li>
         <li><a href="qodana-yaml.md">Save <code>qodana.yaml</code></a> in your project root</li>
         <li><a href="baseline.topic">Run the baseline</a> feature</li>
      </list>
   <img src="ide-plugin-run-qodana-2.png" dark-src="ide-plugin-run-qodana-2_dark.png" width="793" alt="Configuring Qodana in the Run Qodana dialog" border-effect="line"/>
    <p>Click <ui-path>Run</ui-path> for inspecting your code.</p>
</step>
<step>
   <p>In the <ui-path>Server-Side Analysis</ui-path> tool window, overview <a anchor="ide-plugin-study-reports">inspection results</a>.</p>
</step>
</procedure>

## Configure %product% for CI
{id="ide-plugin-cicd"}

You can add %product% into CI pipelines using the configuration wizard.

<note>Depending on the %product% license, you will need to generate and use the <a href="cloud-projects.topic" anchor="cloud-manage-projects">project token</a> at Qodana Cloud.</note>

<procedure>
   <step>
      <p>In your IDE, navigate to <ui-path>Tools | Qodana | Try Code Analysis with Qodana</ui-path>.</p>
   </step>
   <step>
      <p>In the <ui-path>Run Qodana</ui-path> dialog, click the <ui-path>Add to CI Pipeline</ui-path> button. </p>
      <img src="ide-plugin-run-qodana-1.png" dark-src="ide-plugin-run-qodana-1_dark.png" width="706" alt="First step of the Run Qodana dialog" border-effect="line"/>
   </step>
   <step>
      <p>In the <ui-path>Run Qodana</ui-path> dialog, configure the <a href="qodana-yaml.md"><code>qodana.yaml</code></a> file.</p>
      <img src="ide-plugin-cicd-1.png" dark-src="ide-plugin-cicd-1_dark.png" width="706" alt="Second step of the CI/CD configuration in the Run Qodana dialog" border-effect="line"/>
   </step>
   <step>
      <p>Select the CI solution you would like to configure %product% for, and study the instructions.</p>
      <img src="ide-plugin-cicd-2.png" dark-src="ide-plugin-cicd-2_dark.png" width="706" alt="Third step of the CI/CD configuration in the Run Qodana dialog" border-effect="line"/>
   </step>
</procedure>

## Connect to Qodana Cloud
{id="ide-plugin-connect-cloud"}

You can connect your local project to a specific Qodana Cloud [project](cloud-projects.topic), get the latest %product% 
report, and overview it using the IDE.

<procedure>
   <step>
      <p>In your IDE, navigate to <ui-path>Tools | Qodana | Log in to Qodana</ui-path>.</p>
   </step>
   <step>
      <p>
         In the <ui-path>Settings</ui-path> dialog, click <ui-path>Log in</ui-path>.
      </p>
      <img src="ide-plugin-connect-1.png" dark-src="ide-plugin-connect-1_dark.png" width="706" alt="Connecting to Qodana Cloud" border-effect="line"/>
   <p>This will redirect you to the authentication page.</p>
   </step>
   <step>
      <p>Select the <a href="cloud-projects.topic">Qodana Cloud project</a> to link your local project with.</p>
      <img src="ide-plugin-connect-2.png" dark-src="ide-plugin-connect-2_dark.png" width="706" alt="Linking the project to Qodana Cloud" border-effect="line"/>
   </step>
    <step>
       <p>In the <ui-path>Server-Side Analysis</ui-path> tool window, overview <a anchor="ide-plugin-study-reports">inspection results</a>.</p>
    </step>
</procedure>

## Open a local report
{id="ide-plugin-local-report"}

You can open and study [SARIF-formatted %product% reports](qodana-sarif-output.md) in your IDE. 

<snippet id="ide-open-local-report">
<procedure>
   <step>
        <p>In your IDE, navigate to <ui-path>Tools | Qodana | Open Local Report</ui-path>.</p>
   </step>
   <step>
        <p>Select the SARIF-formatted report file you would like to open.</p>
   </step>
   <step>
      <p>In the <ui-path>Server-Side Analysis</ui-path> tool window, you can overview inspection results.</p>
   </step>
</procedure>
</snippet>

## Qodana report overview
{id="ide-plugin-study-reports"}

Using the **Server-Side Analysis** tool window of your IDE, you can view %product% reports and navigate to the code fragments 
containing such problems.

<img src="ide-plugin-report-navigating.png" dark-src="ide-plugin-report-navigating_dark.png" width="706" alt="Navigating to problems in the IDE" animated="true" border-effect="line"/>

The left part of the **Server-Side Analysis** tool window contains several buttons. 

<img src="ide-plugin-report-navigating-buttons.png" dark-src="ide-plugin-report-navigating-buttons_dark.png" width="460" alt="Buttons in the Server-Side Analysis tool window" border-effect="line"/>

This table describes each button from top to bottom:

<table>
   <tr>
      <td>Button</td>
      <td>Description</td>
   </tr>
   <tr>
      <td><ui-path>Close Report</ui-path></td>
      <td>Close the report that was previously opened</td>
   </tr>
   <tr>
      <td><ui-path>Refresh Report</ui-path></td>
      <td>Download the updated version of the report from Qodana Cloud. This requires that you first link your project with Qodana Cloud</td>
   </tr>
    <tr>
      <td><ui-path>Log in to Qodana / Logged in to Qodana</ui-path></td>
      <td>Log in Qodana Cloud, or log out. This action is a prerequisite for linking your project with Qodana Cloud-based reports
    </td>
   </tr>
   <tr>
      <td><ui-path>Link project with Cloud / Linked with Cloud</ui-path></td>
      <td>Link your project with a specific Qodana Cloud-based project, or unlink it. This requires that you first log in to Qodana Cloud </td>
   </tr>
   <tr>
      <td><ui-path>View Options</ui-path></td>
      <td>Filter out code issues by their severity and configure their sorting. When no grouping or sorting options are 
selected, the issues are listed in the order they appear in the file. You can also filter all issues by the <a href="baseline.topic">baseline</a></td>
   </tr>
   <tr>
      <td><ui-path>Open Editor Preview</ui-path></td>
      <td>Open the preview pane to view the selected issue in its source context. This preview lets you can change the 
    code and apply available quick-fixes</td>
   </tr>
   <tr>
      <td><ui-path>Expand All</ui-path></td>
      <td>Expand all nodes to see all issues in the expanded form</td>
   </tr>
   <tr>
      <td><ui-path>Collapse All</ui-path></td>
      <td>Collapse all nodes that were previously expanded</td>
   </tr>
   <tr>
      <td><ui-path>Show Qodana in Browser</ui-path></td>
      <td>Open the inspection report using your default browser</td>
   </tr>
   <tr>
      <td><ui-path>Other</ui-path></td>
      <td>Functionalities from the <ui-path>Tools | Qodana</ui-path> menu</td>
   </tr>
</table>

## Qodana log overview

In your IDE, navigate to **Help | Collect Logs and Diagnostic Data**. This will collect all necessary data and save 
them under a specific directory.   