[//]: # (title: User interface overview)

The Qodana UI focuses on the single-shot analysis, making it easy to act on results and customize checks.

> To learn how to open such reports in your browser, see the [Open an HTML report](html-report.md) section.

## HTML report structure

Qodana report data is grouped in tabs.

<img src="ui-overview.png" dark-src="ui-overview_dark.png" alt="Overview of the Qodana UI" width="706" border-effect="line"/>

Each report contains the following tabs:

* **[Actual problems](#Actual+problems)** shows the problems that Qodana detected during this run 
* **[Baseline](#Baseline)** lists the problems that remained intact from previous runs
* **[Checks](#Checks)** shows the list of inspections and lets you configure them
* **[Project audit](#Project+audit)** describes the problems detected by the [License Audit](license-audit.xml) feature

### Actual problems

Using this tab, you can overview the problems found during the current Qodana run.

<img src="html-report.png" dark-src="html-report_dark.png" alt="The Actual problems tab" width="706" border-effect="line"/>

This includes several elements:

1. The sunburst diagram provides a graphical overview for the problems and allows you to drill down into the cause of 
the issue. 

2. The filter lets you filter the report data. 

<!-- Where are these files stored? -->

3. Configured filters can be saved using the **Save as...** button. The **Reorder** button toggles the editing mode, so 
you can rearrange the sunburst diagram by dragging its components. 

4. The **Problems** tab lists and classifies all detected problems by severity, filename, path, category, and type. The 
**Files** tab presents problems in the file tree.      

5. The **Move to baseline** button saves the selected problems to the **[Baseline](#Baseline)** list.  

6. Clicking a problem in the list will expand the underlying code fragment to provide the detailed description.

7. If you have JetBrains Toolbox and [](qodana-ide-plugin.md) installed, you can click the **Open file in** button to open the file in your IDE. The **More actions** list provides other options for handling problems, see the [Adjust the analysis scope](#Adjust+the+analysis+scope) section.

### Baseline

When you click the **Move to baseline** button in the **[Actual problems](#Actual+problems)** tab, the selected
problems will move to this tab.

<img src="html-report-baseline.png" dark-src="html-report-baseline_dark.png" alt="The Technical debt tab overview" width="706" border-effect="line"/>

This tab structure is similar to the **Actual problems** tab. To enable the baseline feature in future runs of
Qodana, download the configuration file and save it to the project root folder. For more information, explore the
[Baseline](qodana-baseline.xml) section.

### Checks

The **Checks** tab lists the inspections and lets you adjust your inspection profile by specifying a set of 
inspections that Qodana will be using during next run.

<img src="html-report-check.png" dark-src="html-report-check_dark.png" alt="List of checks/inspections" width="706" border-effect="line"/>

Here, you can study each inspection, enable or disable it. To use this configuration for future Qodana runs, you can 
download the `qodana.yaml` file in the **Profile configuration** section, and save it into your project root directory. 

See the [Adjust your inspection profile](#Adjust+your+inspection+profile) section to learn the best practices. 

> To learn more about inspection profiles, see the [Set up a profile](qodana-yaml.md#Set+up+a+profile) section.
> You can also edit profile settings in the [`qodana.yaml`](qodana-yaml.md) file.

### Project audit

<include src="lib_qd.xml" include-id="license-audit-tab" use-filter="ui-overview,empty" />

## Adjust your inspection profile 

We believe that the ability to see what was checked is as important as the list of problems found. For example, if you
haven't checked for typos, you can be happy to see zero typos in your project. There may be many of them – you just
don't check.

> Inspection profile can be configured either using the **[Checks](#Checks)** tab, or editing the 
> [`qodana.yaml`](qodana-yaml.md) file. 

If the number of problems is manageable, you can fix them and consider the 'problem-free code' goal achieved. We 
suggest that you follow that goal and fix new problems as soon as they appear.

In case the number problems is above your expectations, we suggest using the Qodana UI features to examine them. You can 
then formalize a not-so-big cluster of the problems to fix. Repeat the procedure to work on the next goal, and so on.

When you have no possibility to fix old problems and want to prevent the appearance of new ones, you can run Qodana in
the [technical debt or baseline](qodana-jvm-docker-techs.xml#Run+in+baseline+mode) running mode.

## Adjust the analysis scope

### Reduce the scope of analyzed issues
{id="reduce-analysis-scope"}

When viewing a code fragment with a detected problem, you may decide that it is irrelevant. You can make sure that more 
problems of the same type are omitted in the future. For this purpose, you can edit [qodana.yaml](qodana-yaml.md) or use 
the Problem and File explorers in the UI as shown below.

1. **Exclude a file or directory from the future analysis**

*Reason*: The analysis of the file containing the error, or even the directory containing this file, doesn't make sense 
in your project. For example, it's actually not the source code but some generated or downloaded content.

*Howto*: Under the code fragment view, click **More actions** and select the necessary option.
   
<img src="ui-overview-analysis-1.png" dark-src="ui-overview-analysis-1_dark.png" alt="Selecting the options" width="810" border-effect="line"/>  
    
*OR*:

Above the code fragment view, click the file path to navigate to the File explorer. 
      
<img src="ui-overview-analysis-2.png" dark-src="ui-overview-analysis-2_dark.png" alt="Adjusting the analysis scope, first step" width="810" border-effect="line"/>

You can mark the file/directory as **Excluded**.

<img src="ui-overview-analysis-3.png" dark-src="ui-overview-analysis-3_dark.png" alt="Adjusting the analysis scope, second step" width="810" border-effect="line"/>

2. **Hide a problem type or category from the list of problems**

*Reason*: You suppose that the type of the error or its category is not relevant or want to get back to it later.  
*Howto*: Under the code fragment view, click **More actions** and select the necessary option.
   
<img src="ui-overview-analysis-1.png" dark-src="ui-overview-analysis-1_dark.png" alt="Selecting the options" width="810" border-effect="line"/>  

> If you exclude either type/category or file/directory, the UI will remind you to save the changes if you want to use 
> them in future checks. Download the `qodana.yaml` file and store it under your project root directory.

### Enable excluded or hidden problems

To reverse the exclusions you made, download `qodana.yaml` in the **[Profile configuration](#Checks)** section, edit 
it as necessary, put it in the project root directory, and then run Qodana again with this new configuration. 

To learn how to configure Qodana using `qodana.yaml`, see the [Configure profile](qodana-yaml.md) section.


