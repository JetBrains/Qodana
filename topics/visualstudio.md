# Visual Studio

<link-summary>Using Visual Studio, you can explore %product% reports and connect to %cloud%. </link-summary>

<show-structure for="chapter" depth="3"/>

Visual Studio is a comprehensive IDE for .NET and C++ developers on Windows developed by Microsoft. Starting from version 
2025.1 of %product%, you can run it in Visual Studio and perform the following actions:

* [Connect to %cloud%](#vs-code-ui-overview)
* [Explore %product% reports](#visual-studio-explore-reports) downloaded from %cloud%

> Using %product% in Visual Studio does not require a ReSharper license.
{style="note"}

## Before you start

<link-summary>Make sure that you have a project in %cloud%, and you can install ReSharper. </link-summary>

Make sure that you have a %cloud% [project](cloud-projects.topic), and this project has at
least one uploaded [analysis report](cloud-overview-reports.topic) related to the project opened locally in your Visual Studio.

Download and install Qodana as a component of [JetBrains ReSharper](https://www.jetbrains.com/resharper/).

## UI overview
{id="vs-code-ui-overview"}

<link-summary>In Visual Studio, navigate to Extensions and run %product%.  </link-summary>

In Visual Studio, navigate to **Extensions | ReSharper | Qodana**, and then click **Show Qodana Panel**.

This will open the **%product% Analysis** panel in the lower part of your Visual Studio UI.

<img src="visual-studio-qodana-panel.png" width="670" border-effect="line" alt="The Qodana Analysis panel"/>

### Log in to Qodana Cloud

On the **%product% Analysis** panel, click **Log In to %product%**. This will open the **Options** window.

Log in to %cloud% using the **Log In** button. This will redirect you to %cloud% to complete the
login process.

<img src="visual-studio-option-window.png" alt="The Options window" width="535" border-effect="line"/>

To log in to your %product% Self-hosted instance, check **Enable %product% Self-Hosted** and then in the
**Qodana server URL** enter the URL to it.

<img src="visual-studio-self-hosted-login.png" alt="Logging in to %cloud% Self-hosted" width="535" border-effect="line"/>

### Link and download report

Once you logged in to %cloud%, you need to link your local project to a project in %cloud%. To do this, open the
**%product% Analysis** panel and then click the **Link project** link. This will open the **Options** window containing
%cloud% projects that can be linked to your local project.  

<img src="visual-studio-list-for-linking.png" width="535" alt="List of projects for linking" border-effect="line"/>

Here, select the %cloud% project and then click the **Link** button. 

If you cannot find the required project in the list, click the **Other project** button and enter the ID of your
project. You can take this ID from the %cloud% URL according to the pattern 
`https://qodana.cloud/projects/ProjectID/reports/ReportID`. 

<img src="visual-studio-custom-linking.png" widh="535" alt="Custom project linking" border-effect="line"/>

## Explore Qodana reports
{id="visual-studio-explore-reports"}

<link-summary>You can explore Qodana analysis reports in Visual Studio. </link-summary>

You can explore analysis reports of %product% using the **Qodana Analysis** panel of the Visual Studio UI.

<img src="visual-studio-explore-reports.png" width="980" alt="Exploring Qodana reports" border-effect="line"/>

On this panel, you can extend problem categories and then click specific problems to navigate to code fragments
containing such problems. 

The upper part of the **Qodana Analysis** panel contains buttons that let you refresh and close the report, as well
as group problems by various categories. Here, you can use the **Show Preview** button for viewing code fragments in the 
**Qodana Analysis** panel.
