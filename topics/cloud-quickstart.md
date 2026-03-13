[//]: # (title: Quick start)

<link-summary>Learn how you can start using %cloud%.</link-summary>

To start using %cloud%, navigate to the [%cloud% website](https://qodana.cloud).

<img src="qc-get-access.png" alt="%cloud% start page" width="706" border-effect="line"/>

1. You can click the **Continue with JetBrains account** button to create a
   [JetBrains account](https://account.jetbrains.com/login) to log in to %cloud%.
2. As a non-registered user, you can explore demo projects already analyzed by %product%. To explore
   reports in detail, see the [cloud-overview-reports.topic](cloud-overview-reports.topic) section.

After logging in to %cloud% for the first time, you will be redirected to the [project setup](Quick-start.topic#quickstart-prerequisites) 
page for creating an [organization](cloud-organizations.topic), a [team](cloud-teams.topic), a [project](cloud-projects.topic), 
and have a [project token](cloud-projects.topic#cloud-manage-projects) generated for your project. 

Use the generated project token for forwarding %product% reports to %cloud%.

Finally, run %instance% [locally](Quick-start.topic#quickstart-run-using-cli) or in a [CI/CD pipeline](ci.md), 
and [view](cloud-overview-reports.topic) analysis results in %cloud%.

If necessary, you can create additional teams and projects without the onboarding wizard:

1. On the organization page, you can create a [team](cloud-teams.topic#cloud-teams-create-team)
2. On the team page, you can create and configure a [project](cloud-projects.topic#cloud-create-project)

## IP addresses required by Qodana Cloud

To provide the correct work of the contributor counting functionality, add the IP address range
54.76.32.8/32 to a list of allowed inbound connections on your side.

## Qodana Cloud components

<p>The basic entity in <a href="https://qodana.cloud">%cloud%</a> is an organization. Every %cloud% user
    creates and becomes an organization member and can later create additional organizations. </p>
<p>Each organization can contain several teams, where each team provides unified access to projects for its team
    members. If you run the <a href="pricing.md" anchor="pricing-linters-licenses">Ultimate and Ultimate Plus</a>
    linters, you can create an unlimited number of teams. If you use only the Community linters, you can create
    only one team in your organization.</p>
<p>Each project contains the results of inspection carried out by %instance% over a specific codebase.</p>

<img src="qc-running-introduction.png" dark-src="qc-running-introduction_dark.png" width="706" alt="%cloud% entity hierarchy" border-effect="line"/>


## License costs

<p>The total license cost is based on the number of active contributors. An active contributor is defined as a
    person who
    has made commits to any number of %cloud% <a href="cloud-projects.topic">projects</a> within the same
    <a href="cloud-organizations.topic">organization</a> and under a single license during the past ninety (90)
    days.
    The minimal number of contributors used for licensing is three (3).</p>
