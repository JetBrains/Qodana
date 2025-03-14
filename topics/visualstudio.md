# Visual Studio

<link-summary>Using Visual Studio, you can run %product%, explore %product% reports and connect to Qodana Cloud. </link-summary>

<show-structure for="chapter" depth="3"/>

Visual Studio is a comprehensive IDE for .NET and C++ developers on Windows. This section shows you how can use
%product% in Visual Studio:

* [Connect to Qodana Cloud](#vs-code-ui-overview)
* [Explore %product% reports](#visual-studio-explore-reports) downloaded from Qodana Cloud.

## Before you start

<link-summary>Make sure that you have a project in Qodana Cloud and you can install ReSharper. </link-summary>

Make sure that you have a Qodana Cloud [project](cloud-projects.topic), and this project has at
least one uploaded [analysis report](cloud-overview-reports.topic) related to the project opened locally in your Visual Studio.

Download and install %product% as a component of [JetBrains ReSharper](https://www.jetbrains.com/resharper/).

## UI overview
{id="vs-code-ui-overview"}

<link-summary>In Visual Studio, navigate to Extensions and run %product%.  </link-summary>

In Visual Studio, navigate to **Extensions | ReSharper | Qodana**, and then click **Show Qodana Panel**.

This will open the **%product% Analysis** panel in the lower part of your Visual Studio UI.

<img src="visual-studio-qodana-panel.png" width="670" border-effect="line" alt="The Qodana Analysis panel"/>

### Log in to Qodana Cloud

On the **%product% Analysis** panel, click **Log In to Qodana**. This will open the **Options** window.

Log in to %product% Cloud using the **Log In** button. This will redirect you to Qodana Cloud to complete the
login process.

<img src="visual-studio-option-window.png" alt="The Options window" width="535" border-effect="line"/>

To log in to your Qodana Self-hosted instance, check **Enable Qodana Self-Hosted** and then in the
**Qodana server URL** enter the URL to it.

<img src="visual-studio-self-hosted-login.png" alt="Logging in to Qodana Cloud Self-hosted" width="535" border-effect="line"/>

### Link and download report

Once you logged in to Qodana Cloud, you need to link your local project to a project in Qodana Cloud. To do this, open the
**%product% Analysis** panel and then click the **Link project** link. This will open the **Options** window containing 
Qodana Cloud projects that can be linked to your local project.  

<img src="visual-studio-list-for-linking.png" width="535" alt="List of projects for linking" border-effect="line"/>

Here, select the Qodana Cloud project and then click the **Link** button. 

If you cannot find the required project in the list, click the **Other project** button and enter the ID of your
project. You can take this ID from the Qodana Cloud URL according to the pattern 
`https://qodana.cloud/projects/ProjectID/reports/ReportID`. 

<img src="visual-studio-custom-linking.png" widh="535" alt="Custom project linking" border-effect="line"/>

## Explore %product% reports
{id="visual-studio-explore-reports"}

<link-summary>You can explore Qodana analysis reports in Visual Studio. </link-summary>

You can explore analysis reports of %product% using the **Qodana Analysis** panel of the Visual Studio UI.

<img src="visual-studio-explore-reports.png" width="980" alt="Exploring Qodana reports" border-effect="line"/>

On this panel, you can extend problem categories and then click specific problems to navigate to code fragments
containing such problems. 

The upper part of the **Qodana Analysis** panel contains buttons that let you refresh and close the report, as well
as group problems ba various metrics.
