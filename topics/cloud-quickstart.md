[//]: # (title: Quick start)

<link-summary>Learn how you can start using %cloud%.</link-summary>

To start using %cloud%, navigate to the [%cloud% website](https://qodana.cloud) and 
[create your account](cloud-get-access.topic).

After logging in to %cloud% for the first time, you will be redirected to the [project setup](set-up-your-project.md) 
page for creating an [organization](cloud-organizations.topic), a [team](cloud-teams.topic), a [project](cloud-projects.topic), 
and have a [project token](cloud-projects.topic#cloud-manage-projects) generated for your project. 

<tip>This is how you can learn more about <a href="cloud-running-introduction.topic">%cloud% components</a>.</tip>

Use the generated project token for [forwarding %instance% reports](cloud-forward-reports.topic) to %cloud%.

Finally, run %instance% [locally](Quick-start.topic#quickstart-run-using-cli) or in a [CI/CD pipeline](ci.md), 
and [view](cloud-overview-reports.topic) analysis results in %cloud%.

If necessary, you can create additional teams and projects without the onboarding wizard:

1. On the organization page, you can create a [team](cloud-teams.topic#cloud-teams-create-team)
2. On the team page, you can create and configure a [project](cloud-projects.topic#cloud-create-project)

## IP addresses required by Qodana Cloud

To provide the correct work of the contributor counting functionality, add the IP address range
54.76.32.8/32 to a list of allowed inbound connections on your side.
