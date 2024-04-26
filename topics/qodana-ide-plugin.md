[//]: # (title: JetBrains IDEs)

You can run [%instance%](about-qodana.md) in JetBrains IDEs to inspect your codebase. %instance% supports several JetBrains IDEs 
installed via [JetBrains Toolbox App](https://www.jetbrains.com/toolbox-app/), such as IntelliJ IDEA, PhpStorm, WebStorm, Rider, GoLand, PyCharm, and Rider.

Using the IDE, you can:

* [Run %instance% locally](#ide-plugin-run-qodana)
* [Connect to Qodana Cloud](#ide-plugin-connect-cloud)
* [Configure %instance% for running in a CI pipeline](#ide-plugin-cicd)
* [Open a report from local storage](#ide-plugin-local-report)
* [Study %instance% reports in your IDE](#ide-plugin-study-reports)

## UI overview

In your IDE, navigate to <ui-path>Tools | Qodana</ui-path>.

<img src="ide-plugin-intro-menu.png" dark-src="ide-plugin-intro-menu_dark.png" width="706" alt="The Qodana menu" border-effect="line"/>

You can also have access to %instance% using the **Problems | Server-Side Analysis** tool window of your IDE.

<img src="ide-plugin-intro-tool-window.png" dark-src="ide-plugin-intro-tool-window_dark.png" width="706" alt="The Server-Side Analysis tool window" border-effect="line"/>

## Run %instance% locally
{id="ide-plugin-run-qodana"}

You can run %instance% locally and then forward inspection reports to [Qodana Cloud](cloud-about.topic) for storage and analysis purposes.

<procedure>
<step>
   <p>In your IDE, navigate to <ui-path>Tools | Qodana | Try Code Analysis with Qodana</ui-path>.</p> 
</step>
<step>
   <p>In the <ui-path>Run Qodana</ui-path> dialog, you can configure:</p>
      <list>
        <li>Options used by %product% in the <a href="qodana-yaml.md"><code>qodana.yaml</code></a> file</li>
         <li>The <a href="cloud-forward-reports.topic"><ui-path>Send inspection results to Qodana Cloud</ui-path></a> option using a <a href="cloud-projects.topic" anchor="cloud-manage-projects">project token</a></li>
         <li>The <a href="qodana-yaml.md"><ui-path>Save qodana.yaml in project root</ui-path></a> option</li>
         <li>The <a href="baseline.topic"><ui-path>Use Qodana analysis baseline</ui-path></a> option to run %product% with a baseline</li>
      </list>
   <img src="ide-plugin-run-qodana-2.png" width="793" alt="Configuring Qodana in the Run Qodana dialog" border-effect="line"/>
    <p>Click <ui-path>Run</ui-path> for inspecting your code.</p>
</step>
<step>
   <p>In the <ui-path>Server-Side Analysis</ui-path> tool window, see <a anchor="ide-plugin-study-reports">inspection results</a>.</p>
</step>
</procedure>

## Connect to Qodana Cloud
{id="ide-plugin-connect-cloud"}

You can log in to Qodana Cloud and connect your project opened in the IDE to a specific Qodana Cloud [project](cloud-projects.topic) to get the 
latest %instance% report and view it.

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
        <p>By enabling the <ui-path>Always load most relevant Qodana report</ui-path> option, you can get actual reports automatically retrieved from Qodana Cloud.</p>
      <img src="ide-plugin-connect-3.png" dark-src="ide-plugin-connect-3_dark.png" width="706" alt="Enabling to load the most relevant reports" border-effect="line"/>
        <p>In this case, the IDE will search and fetch from Qodana Cloud the report that has the revision ID corresponding to the 
        current revision ID (HEAD). If this report was not found, the IDE will select the previous report with the revision
        closest to the current revision ID (HEAD). Otherwise, the IDE retrieves the latest available report from Qodana Cloud.</p>
    </step> 
    <step>
       <p>In the <ui-path>Server-Side Analysis</ui-path> tool window, see <a anchor="ide-plugin-study-reports">inspection results</a>.</p>
    </step>
</procedure>

## Configure %instance% for CI
{id="ide-plugin-cicd"}

Once you logged in to [Qodana Cloud](https://qodana.cloud), you can configure %instance% in your CI pipelines.

<note>Depending on the %instance% <a href="pricing.md">license</a>, you will need to generate and use the 
<a href="cloud-projects.topic" anchor="cloud-manage-projects">project token</a>. To learn more about project tokens, see
the <a href="project-token.md"/> section.</note>

<procedure>
<step>
<p>In your IDE, navigate to <ui-path>Tools | Qodana | Add Qodana to CI Pipeline</ui-path></p>
</step>
<step>
<p>In the <ui-path>Add Qodana to CI Pipeline</ui-path> dialog, follow the recommendations applicable to your CI/CD solution.</p>
      <img src="ide-plugin-cicd-2.png" dark-src="ide-plugin-cicd-2_dark.png" width="706" alt="The Add Qodana to CI pipeline dialog" border-effect="line"/>
</step>
</procedure>

## Open a local report
{id="ide-plugin-local-report"}

You can open and study [SARIF-formatted %instance% reports](qodana-sarif-output.md) in your IDE. 

<snippet id="ide-open-local-report">
<procedure>
   <step>
        <p>In your IDE, navigate to <ui-path>Tools | Qodana | Open Local Report</ui-path>.</p>
   </step>
   <step>
        <p>Select the SARIF-formatted report file you would like to open.</p>
   </step>
   <step>
      <p>In the <ui-path>Server-Side Analysis</ui-path> tool window, you can view inspection results.</p>
   </step>
</procedure>
</snippet>

## Qodana report overview
{id="ide-plugin-study-reports"}

Using the **Server-Side Analysis** tool window of your IDE, you can view %instance% reports and navigate to the code fragments 
containing such problems.

<img src="ide-plugin-report-navigating.png" dark-src="ide-plugin-report-navigating_dark.png" width="706" alt="Navigating to problems in the IDE" animated="true" border-effect="line"/>

The upper part contains information about the project and branch names, the inspection date, and the number of problems. 
The left part of the **Server-Side Analysis** tool window contains several buttons. 

<img src="ide-plugin-report-navigating-buttons.png" dark-src="ide-plugin-report-navigating-buttons_dark.png" width="460" alt="Functionalities of the Server-Side Analysis tool window" border-effect="line"/>

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
      <td>Open the preview pane to view the selected issue in its source context. This preview lets you change the 
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