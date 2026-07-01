# Insights

<show-structure depth="3"/>

Insights let you examine aggregated data on organizational and team levels in %cloud%. The Insights dashboard is available 
under the Ultimate Plus [license](pricing.md). To learn more about available %product% licenses, visit the [Subscription Options and Pricing](https://www.jetbrains.com/qodana/buy/?billing=yearly) page.
You can also [request a demo](https://www.jetbrains.com/qodana/request-a-demo/).

To view insights on an organization level, in the upper part of your [organization](cloud-organizations.topic) 
page click the **Insights** button. To do the same on a team level, click this button on your team page. 

<img src="insights-insights-button.png" width="706" alt="Navigating to the Insights page" border-effect="line"/>

> To navigate from team to organization-wide insights with a single click, in the upper part of the **Insights** 
> page, click the **Reset filters** link. 
{style="tip"}

## Dashboard filters

The upper part of the **Insights** page contains filters that let you filter widgets by
[projects](cloud-projects.topic), [severities](ui-overview.md#Severity+levels), inspections (checks), and [baseline](baseline.topic).

After you configure all widgets, you can save the configured dashboard using the **Saved filters** dropdown list.
Alternatively, you can copy the link to the dashboard configuration and share it with others.

<img src="insights-upper-filters.png" width="735" alt="The Insights page filters" border-effect="line" thumbnail="true"/> 

## Available widgets

### Projects

Displays the number of active and inactive projects in your organization. 

Active are the projects which reports were uploaded to %cloud% within 90 days.
A project is classified as inactive in case it contains 
[unexpected problems](inspection-profiles.md#inspection-profiles-existing-profiles) or its reports are older than 90 days.

If you hover over this widget, you can see the number of active and inactive projects. Here, you can click the line
describing inactive projects to navigate to a comprehensive list of these projects.

<img src="insights-number-of-projects.png" alt="The number of projects" width="358" border-effect="line"/>

### Scans

This widget provides information about analyses performed on your projects excluding pull or merge requests and carried 
out by %product% versions 2024.2 or later.

### Average code coverage rate

Indicates the extent to which your projects are covered with tests, calculated using the [code coverage](code-coverage.md) feature, 
and lets you navigate to the projects with disabled code coverage.

If you hover over the widget, you can view the number of projects covered and not covered with tests and navigate to the
respective projects.

<img src="insights-code-coverage.png" alt="The code coverage rate widget" width="358" border-effect="line"/>

### Average license audit rate

Indicates the percentage of projects that passed the codebase analysis using the [license audit](license-audit.topic) feature. 

If you hover over the widget, you can navigate to the projects where license audit failed or was not enabled, and
view related analysis reports.

<img src="insights-license-audit.png" alt="The license audit widget" width="358" border-effect="line"/>

### Problems by severity

Contains a diagram showing the problem numbers by their severities, see the [description of severities](ui-overview.md#Severity+levels) 
for details.

<img src="insights-problems-by-severity.png" width="706" alt="Problems by severity diagram" border-effect="line"/>

### Trends over period

Shows the trends for a selected period of time based on the number of problems and code coverage rates. Using this widget, 
you can see the progress in code quality.

<img src="insights-trends-over-period.png" width="706" alt="Trends over a period widget" border-effect="line"/>

### Projects sorted

In the lower-left part of the **Insights** page, you can filter your projects by the number of problems, number of 
critical problems, as well as code coverage. 

<img src="insights-projects-sorted.png" width="706" alt="Problems sorted by various parameters" border-effect="line"/>

By clicking a specific project entry, you can navigate to a project page.

### Problems sorted

In the lower part of the **Insights** page, you can sort problems detected in your projects by severity, occurrence and inspections (checks). 

<img src="insights-problems-sorted.png" width="706" alt="Problems sorted by severity and occurrence" border-effect="line"/>

To view all projects containing a specific problem, click a problem in this widget.
To search a problem by its name, in the lower part of the widget click **View all problems** and use the search field.