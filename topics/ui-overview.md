[//]: # (title: Inspection report)

%product% lets you overview inspection reports in an interactive and user-friendly form either 
[locally](html-report.md) or in [Qodana Cloud](cloud-overview-reports.xml).

<img src="ui-overview.png" dark-src="ui-overview_dark.png" alt="Qodana report UI overview" width="706" border-effect="line"/>

Each report contains the following tabs:

* **[Actual problems](#ui-overview-actual-problems)** exposes the problems that Qodana detected during the latest inspection 
* **[Baseline](#ui-overview-baseline)** lists the problems that were marked as [baseline](baseline.xml) and were not fixed since then
* **[Configuration](#ui-overview-configuration)** lets you configure %product% for future use
* **[Project audit](#ui-overview-project-audit)** reveals the [license audit](license-audit.xml) results and shows the dependency licenses that are incompatible with the project license 

The upper-right corner of the report shows [code coverage](code-coverage.md) inspection results.

<img src="ui-overview-code-coverage.png" dark-src="ui-overview-code-coverage_dark.png" alt="Qodana report UI overview" width="296" border-effect="line"/>

## Actual problems
{id="ui-overview-actual-problems"}

Using this tab, you can overview the problems found as a result of the latest inspection.

<img src="ui-overview-actual-problems.png" dark-src="ui-overview-actual-problems_dark.png" alt="The Actual problems tab" width="706" border-effect="line"/>

This tab consists of several elements:

1. The sunburst diagram provides a graphical overview of the problems and allows you to drill down into the cause of 
the issue. 

2. The group of filters lets you filter the report data using various criteria. 

3. You can navigate between the list of problems and files, as well as search and group problems. 

4. The **Move selected to baseline** button saves the selected problems to the **[Baseline](#ui-overview-baseline)** list.  

5. Clicking a problem in the list expands the underlying code fragment containing the detailed description.

6. If you have JetBrains Toolbox and [](qodana-ide-plugin.md) installed, you can edit the file containing the problem
    using your IDE. To do it, select your IDE from the dropdown list, and click the **Open file in...** button. 

   If you have several versions of the same IDE, you can select which version will be used to open the file.
   In the JetBrains Toolbox UI, drag or move the required version of the IDE to the top of the list using the
    <shortcut>Ctrl + Shift + ↑/↓</shortcut> shortcut on Windows or Linux, or <shortcut>⌘ + ⇧ + ↑/↓ </shortcut> on macOS.

    The **More actions** list provides other options for handling problems, see the [Adjust the analysis scope](#Adjust+the+analysis+scope) section.

7. You can copy the link to the problem and then navigate to it in Qodana Cloud.

## Baseline
{id="ui-overview-baseline"}

When you click the **Move selected to baseline** button on the **[Actual problems](#ui-overview-actual-problems)** tab, the selected
problems move to this tab.

This tab is similar to the **Actual problems** tab. To enable the baseline feature for future
inspections, follow the instructions that appear in the report UI. For more information, explore the
[](baseline.xml) section.

## Configuration
{id="ui-overview-configuration"}

The **Configuration** tab lists the inspections and lets you adjust your inspection profile by specifying a set of 
inspections that Qodana will be using the next run.

<img src="ui-overview-configuration.png" dark-src="ui-overview-configuration_dark.png" alt="The Configuration tab" width="706" border-effect="line"/>

Here, you can learn what each inspection does, as well as enable or disable it. To use this configuration for future use, 
you can download the `qodana.yaml` file and save it into your project root directory. 

See the [Adjust your inspection profile](#Adjust+your+inspection+profile) section to learn the best practices. 

> To learn more about inspection profiles, see the [](qodana-yaml.md#Set+up+a+profile) section.
> You can also edit profile settings in the [`qodana.yaml`](qodana-yaml.md) file.

## Project audit
{id="ui-overview-project-audit"}

<include src="lib_qd.xml" include-id="license-audit-tab" use-filter="ui-overview,empty" />

## Adjust your inspection profile 

We believe that the ability to see what was checked is as important as the list of problems found. For example, if you
haven't checked for typos, you can be happy to see zero typos in your project. There may be many of them – you just
don't check.

> Inspection profile can be configured either using the **[Configuration](#ui-overview-configuration)** tab, or editing the 
> [`qodana.yaml`](qodana-yaml.md) file. 

If the number of problems is manageable, you can fix them and consider the 'problem-free code' goal achieved. We 
suggest that you follow that goal and fix new problems as soon as they appear.

In case the number of problems is above your expectations, we suggest using the Qodana features to examine them.

When you have no possibility to fix old problems and want to prevent the appearance of new ones, you can run Qodana in
the [baseline](docker-image-configuration.xml#docker-config-reference-baseline) mode.

## Adjust the analysis scope

### Reduce the scope of analyzed issues
{id="reduce-analysis-scope"}

When viewing a code fragment with a detected problem, you may decide that it is irrelevant. You can make sure that more 
problems of the same type are omitted in the future. For this purpose, you can edit [qodana.yaml](qodana-yaml.md) or use 
the [](#ui-overview-actual-problems) tab as shown below.

1. **Exclude a file or directory from the future analysis**

*Reason*: The analysis of the file containing the error, or even the directory containing this file, doesn't make sense 
in your project. For example, it's actually not the source code but some generated or downloaded content.

*Howto*: Under the code fragment view, click **More actions** and select the necessary option.
   
<img src="ui-overview-analysis-1.png" dark-src="ui-overview-analysis-1_dark.png" alt="Selecting the options" width="706" border-effect="line"/>  
    
*OR*:

Above the code fragment view, click the file path to navigate to the File explorer. 
      
<img src="ui-overview-analysis-2.png" dark-src="ui-overview-analysis-2_dark.png" alt="Adjusting the analysis scope, first step" width="706" border-effect="line"/>

On the File explorer, click the icon to the left of the filename, and then select **Mark as Excluded**.

<img src="ui-overview-analysis-3.png" dark-src="ui-overview-analysis-3_dark.png" alt="Excluding from analysis" width="706" border-effect="line"/>

2. **Hide a problem type or category from the list of problems**

*Reason*: You suppose that the error type or its category is not relevant or want to get back to it later.  
*Howto*: Under the code fragment view, click **More actions** and select the necessary option.
   
<img src="ui-overview-analysis-1.png" dark-src="ui-overview-analysis-1_dark.png" alt="Selecting the options" width="706" border-effect="line"/>  

> If you exclude either type/category or file/directory, the UI will remind you to save the changes if you want to use 
> them in future checks. Download the `qodana.yaml` file and store it under your project root directory.

### Enable excluded or hidden problems

To reverse the exclusions you made, download `qodana.yaml` in the **[Profile configuration](#ui-overview-configuration)** section, edit 
it as necessary, put it in the project root directory, and then run Qodana again with this new configuration. 

To learn how to configure Qodana using `qodana.yaml`, see the [Configure profile](qodana-yaml.md) section.


