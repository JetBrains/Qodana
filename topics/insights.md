# Insights

Insights let you examine problems on an organizational level using Qodana Cloud.

To start reviewing problems on your organization level, in the upper-right part of the Qodana Cloud UI click the **Insights** button.
This page contains various dashboards described below.

## Number of projects

Shows the number of projects in your organization. 

Active are the projects which reports were uploaded to Qodana Cloud within 90 days.
A project is classified as inactive in case it was not properly set up, contains 
[sanity problems](inspection-profiles.md#inspection-profiles-existing-profiles) or project reports older than
90 days.

If you hover over this dashboard, you can get information about active and inactive projects, and navigate to the list 
of projects.

<img src="insights-number-of-projects.png" alt="The number of projects" width="358" border-effect="line"/>

## Number of analyses

This dashboard provides information about analyses performed on your projects excluding pull or merge requests and carried 
out by %product% versions 2024.2 or later.

You can navigate to analysis reports by clicking this dashboard and then clicking a specific report entry. 

## Average code coverage rate

Indicates the extent to which your projects are covered with tests, calculated using the [code coverage](code-coverage.md) feature.

If you hover over the widget, you can view the number of projects covered and not covered with tests and navigate to the 
respective projects.

<img src="insights-code-coverage.png" alt="The code coverage rate widget" width="358" border-effect="line"/>

## Average license audit rate

Indicates the number of projects that passed codebase analysis using the [license audit](license-audit.topic) feature. 

If you hover over the widget, you can navigate to the projects that where license audit failed or was not enabled, and
jump to the related reports.

<img src="insights-license-audit.png" alt="The license audit widget" width="358" border-effect="line"/>

## Problems by severity

Contains the diagram showing the problem numbers by their severities, see the [](faq.topic#faq-severities) section
for details.

<img src="insights-problems-by-severity.png" width="706" alt="Problems by severity diagram" border-effect="line"/>

## Problems over a specific period

Shows the number of problems detected in your projects on a specific date within the latest month. Using this diagram, 
you can see the progress in code quality.

<img src="insights-problems-over-period.png" width="706" alt="Problems over a period diagram" border-effect="line"/>

## Projects sorted

In the lower-left part of the **Insights** page, you can filter your projects by the number of problems, number of 
critical problems, as well as code coverage. 

<img src="insights-projects-sorted.png" width="706" alt="Problems sorted by various parameters" border-effect="line"/>

## Problems sorted

In the lower-right part of the **Insights** page, you can sort problems detected in your projects by severity and occurrence. 

<img src="insights-problems-sorted.png" width="706" alt="Problems sorted by severity and occurrence" border-effect="line"/>



