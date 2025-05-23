# Insights

<show-structure depth="3"/>

Insights let you examine aggregated data on organizational and team levels in %cloud%. This feature is available 
under the Ultimate Plus [license](pricing.md).

To view insights on an organization level, in the upper part of your [organization](cloud-organizations.topic) 
page click the **Insights** button. To do the same on a team level, click this button on your team page. 

<img src="insights-insights-button.png" width="706" alt="Navigating to the Insights page" border-effect="line"/>

> To navigate from team to organization-wide insights with a single click, in the upper part of the **Insights** 
> page click the **Reset filters** link. 
{style="tip"}

## Dashboard filters

The upper part of the **Insights** page contains filters that let you filter widgets by
[projects](cloud-projects.topic), [severities](troubleshooting.topic#troubleshooting-severities), [baseline](baseline.topic),
and inspections.

After you configure all the widgets, you can copy the link to the page that contains this configuration state.

<img src="insights-upper-filters.png" width="600" alt="The Insights page filters" border-effect="line"/> 

## Available widgets

### Projects

Displays the number of active and inactive projects in your organization. 

Active are the projects which reports were uploaded to %cloud% within 90 days.
A project is classified as inactive in case it contains 
[sanity problems](inspection-profiles.md#inspection-profiles-existing-profiles) or its reports are older than 90 days.

If you hover over this dashboard, you can see the number of active and inactive projects. Here, you can click the line
describing inactive projects to navigate to a comprehensive list these projects.

<img src="insights-number-of-projects.png" alt="The number of projects" width="358" border-effect="line"/>

### Scans

This dashboard provides information about analyses performed on your projects excluding pull or merge requests and carried 
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

Contains the diagram showing the problem numbers by their severities, see the [description of severities](faq.topic#faq-severities) 
for details.

<img src="insights-problems-by-severity.png" width="706" alt="Problems by severity diagram" border-effect="line"/>

### Problems over a specific period

Shows the number of problems detected in your projects on a specific date within the latest 90 days. Using this diagram, 
you can see the progress in code quality.

<img src="insights-problems-over-period.png" width="706" alt="Problems over a period diagram" border-effect="line"/>

### Projects sorted

In the lower-left part of the **Insights** page, you can filter your projects by the number of problems, number of 
critical problems, as well as code coverage. 

<img src="insights-projects-sorted.png" width="706" alt="Problems sorted by various parameters" border-effect="line"/>

By clicking a specific project entry, you can navigate to a project page.

### Problems sorted

In the lower part of the **Insights** page, you can sort problems detected in your projects by severity and occurrence. 

<img src="insights-problems-sorted.png" width="706" alt="Problems sorted by severity and occurrence" border-effect="line"/>

To view all projects containing a specific problem, click a problem in this widget.
To search a problem by its name, in the lower part of the widget click **View all problems** and use the search field.
