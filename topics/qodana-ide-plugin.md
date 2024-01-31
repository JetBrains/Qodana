[//]: # (title: JetBrains IDEs)

You can run [%product%](about-qodana.md) in JetBrains IDEs to inspect your codebase. %product% supports several JetBrains IDEs 
installed via [JetBrains Toolbox App](https://www.jetbrains.com/toolbox-app/), such as IntelliJ IDEA, PhpStorm, WebStorm, Rider, GoLand, PyCharm, and Rider.

Using the IDE, you can:

* [Run %product% locally](#ide-plugin-run-qodana)
* [Connect to Qodana Cloud](#ide-plugin-connect-cloud)
* [Configure %product% for running in a CI pipeline](#ide-plugin-cicd)
* [Open a report from local storage](#ide-plugin-local-report)
* [Study %product% reports in your IDE](#ide-plugin-study-reports)

## UI overview

In your IDE, navigate to <menupath>Tools | Qodana</menupath>.

<img src="ide-plugin-intro-menu.png" dark-src="ide-plugin-intro-menu_dark.png" width="706" alt="The Qodana menu" border-effect="line"/>

You can also have access to %product% using the **Problems | Server-Side Analysis** tool window of your IDE.

<img src="ide-plugin-intro-tool-window.png" dark-src="ide-plugin-intro-tool-window_dark.png" width="706" alt="The Server-Side Analysis tool window" border-effect="line"/>

## Run %product% locally
{id="ide-plugin-run-qodana"}

You can run %product% locally and then forward inspection reports to [Qodana Cloud](cloud-about.xml) for storage and analysis purposes.

<procedure>
<step>
   <p>In your IDE, navigate to <menupath>Tools | Qodana | Try Code Analysis with Qodana</menupath>.</p> 
</step>
<step>
   <p>In the <menupath>Run Qodana</menupath> dialog, configure the <a href="qodana-yaml.md"><code>qodana.yaml</code></a> file.</p>
   <p>Under the text field, configure the options to make %product%:</p>
      <list>
         <li><a href="cloud-forward-reports.xml">Send inspection results</a> to Qodana Cloud using the <a href="cloud-projects.xml" anchor="cloud-manage-projects">project token</a></li>
         <li><a href="qodana-yaml.md">Save <code>qodana.yaml</code></a> in your project root</li>
         <li><a href="baseline.xml">Run the baseline</a> feature</li>
      </list>
   <img src="ide-plugin-run-qodana-2.png" dark-src="ide-plugin-run-qodana-2_dark.png" width="793" alt="Configuring Qodana in the Run Qodana dialog" border-effect="line"/>
    <p>Click <menupath>Run</menupath> for inspecting your code.</p>
</step>
<step>
   <p>In the <menupath>Server-Side Analysis</menupath> tool window, overview <a anchor="ide-plugin-study-reports">inspection results</a>.</p>
</step>
</procedure>

## Connect to Qodana Cloud
{id="ide-plugin-connect-cloud"}

You can log in to Qodana Cloud and connect your project opened in the IDE to a specific Qodana Cloud [project](cloud-projects.xml) to get the 
latest %product% report and overview it.

<procedure>
   <step>
      <p>In your IDE, navigate to <menupath>Tools | Qodana | Log in to Qodana</menupath>.</p>
   </step>
   <step>
      <p>
         In the <menupath>Settings</menupath> dialog, click <menupath>Log in</menupath>.
      </p>
      <img src="ide-plugin-connect-1.png" dark-src="ide-plugin-connect-1_dark.png" width="706" alt="Connecting to Qodana Cloud" border-effect="line"/>
   <p>This will redirect you to the authentication page.</p>
   </step>
   <step>
      <p>Select the <a href="cloud-projects.xml">Qodana Cloud project</a> to link your local project with.</p>
      <img src="ide-plugin-connect-2.png" dark-src="ide-plugin-connect-2_dark.png" width="706" alt="Linking the project to Qodana Cloud" border-effect="line"/>
   </step>
   <step>
        <p>By enabling the <menupath>Always load most relevant Qodana report</menupath> option, you can get actual reports automatically retrieved from Qodana Cloud.</p>
      <img src="ide-plugin-connect-3.png" dark-src="ide-plugin-connect-3_dark.png" width="706" alt="Enabling to load the most relevant reports" border-effect="line"/>
    </step> 
    <step>
       <p>In the <menupath>Server-Side Analysis</menupath> tool window, overview <a anchor="ide-plugin-study-reports">inspection results</a>.</p>
    </step>
</procedure>

## Configure %product% for CI
{id="ide-plugin-cicd"}

Once you logged in to [Qodana Cloud](https://qodana.cloud), you can configure %product% in your CI pipelines.

<note>Depending on the %product% <a href="pricing.md">license</a>, you will need to generate and use the 
<a href="cloud-projects.xml" anchor="cloud-manage-projects">project token</a>. To learn more about project tokens, see
the <a href="project-token.md"/> section.</note>

<procedure>
<step>
<p>In your IDE, navigate to <menupath>Tools | Qodana | Add Qodana to CI Pipeline</menupath></p>
</step>
<step>
<p>In the <menupath>Add Qodana to CI Pipeline</menupath> dialog, follow the recommendations applicable to your CI/CD solution.</p>
      <img src="ide-plugin-cicd-2.png" dark-src="ide-plugin-cicd-2_dark.png" width="706" alt="The Add Qodana to CI pipeline dialog" border-effect="line"/>
</step>
</procedure>

## Open a local report
{id="ide-plugin-local-report"}

You can open and study [SARIF-formatted %product% reports](qodana-sarif-output.md) in your IDE. 

<chunk id="ide-open-local-report">
<procedure>
   <step>
        <p>In your IDE, navigate to <menupath>Tools | Qodana | Open Local Report</menupath>.</p>
   </step>
   <step>
        <p>Select the SARIF-formatted report file you would like to open.</p>
   </step>
   <step>
      <p>In the <menupath>Server-Side Analysis</menupath> tool window, you can overview inspection results.</p>
   </step>
</procedure>
</chunk>

## Qodana report overview
{id="ide-plugin-study-reports"}

Using the **Server-Side Analysis** tool window of your IDE, you can view %product% reports and navigate to the code fragments 
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
      <td><menupath>Close Report</menupath></td>
      <td>Close the report that was previously opened</td>
   </tr>
   <tr>
      <td><menupath>Refresh Report</menupath></td>
      <td>Download the updated version of the report from Qodana Cloud. This requires that you first link your project with Qodana Cloud</td>
   </tr>
    <tr>
      <td><menupath>Log in to Qodana / Logged in to Qodana</menupath></td>
      <td>Log in Qodana Cloud, or log out. This action is a prerequisite for linking your project with Qodana Cloud-based reports
    </td>
   </tr>
   <tr>
      <td><menupath>Link project with Cloud / Linked with Cloud</menupath></td>
      <td>Link your project with a specific Qodana Cloud-based project, or unlink it. This requires that you first log in to Qodana Cloud </td>
   </tr>
   <tr>
      <td><menupath>View Options</menupath></td>
      <td>Filter out code issues by their severity and configure their sorting. When no grouping or sorting options are 
selected, the issues are listed in the order they appear in the file. You can also filter all issues by the <a href="baseline.xml">baseline</a></td>
   </tr>
   <tr>
      <td><menupath>Open Editor Preview</menupath></td>
      <td>Open the preview pane to view the selected issue in its source context. This preview lets you can change the 
    code and apply available quick-fixes</td>
   </tr>
   <tr>
      <td><menupath>Expand All</menupath></td>
      <td>Expand all nodes to see all issues in the expanded form</td>
   </tr>
   <tr>
      <td><menupath>Collapse All</menupath></td>
      <td>Collapse all nodes that were previously expanded</td>
   </tr>
   <tr>
      <td><menupath>Show Qodana in Browser</menupath></td>
      <td>Open the inspection report using your default browser</td>
   </tr>
   <tr>
      <td><menupath>Other</menupath></td>
      <td>Functionalities from the <menupath>Tools | Qodana</menupath> menu</td>
   </tr>
</table>

## Qodana log overview

In your IDE, navigate to **Help | Collect Logs and Diagnostic Data**. This will collect all necessary data and save 
them under a specific directory.   