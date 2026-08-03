[//]: # (title: Analysis reports)

<show-structure for="chapter" depth="3"/>

<link-summary>%instance% lets you review analysis reports in an interactive and user-friendly form either 
locally or in %cloud%.</link-summary>

%instance% lets you review analysis reports in an interactive and user-friendly form either 
[locally](#Open+an+HTML+report) or in [%cloud%](cloud-overview-reports.topic).

## Report UI overview

<img src="ui-overview.png" alt="Qodana report UI overview" thumbnail="true" scale="5" width="1059"/>

Each report contains the following tabs:

* **[Current problems](#ui-overview-actual-problems)** exposes the problems that %product% detected during the latest inspection. 
* **[Baseline problems](#ui-overview-baseline)** lists the problems that were marked as [baseline](baseline.topic) and were not fixed since then.
* **[Inspections](#ui-overview-configuration)** lets you configure %instance% for future use.
* **[License audit](#ui-overview-project-audit)** reveals [license audit](license-audit.topic) reports and shows the dependency licenses that are incompatible with the project license. 

The upper-right corner of the report shows a [code coverage](code-coverage.md) analysis report.

<img src="ui-overview-code-coverage.png" alt="Code coverage analysis report" thumbnail="true" width="323" border-effect="line"/>

### Current problems
{id="ui-overview-actual-problems"}

Using this tab, you can see the problems found as a result of the latest inspection.

<img src="ui-overview-actual-problems.png" alt="Current problems tab" thumbnail="true" width="706" border-effect="line"/>

This tab consists of several elements:

1. The sunburst diagram provides a graphical overview of the problems and allows you to drill down into the cause of 
the issue. 

2. The group of filters lets you filter the report data using various criteria. 

3. You can navigate between the list of problems and files, as well as search and group problems. 

4. The **Move selected to baseline** button saves the selected problems to the **[Baseline problems](#ui-overview-baseline)** list.  

5. Clicking a problem in the list expands the underlying code fragment containing the detailed description.

6. If you have JetBrains Toolbox and [](qodana-ide-plugin.md) installed, you can edit the file containing the problem
    using your IDE. To do it, select your IDE from the dropdown list and then click the **Open file in...** button. 

   If you have several versions of the same IDE, you can select which version will be used to open the file.
   In the JetBrains Toolbox UI, drag or move the required version of the IDE to the top of the list using the
    <shortcut>Ctrl + Shift + ↑/↓</shortcut> shortcut on Windows or Linux, or <shortcut>⌘ + ⇧ + ↑/↓ </shortcut> on macOS.

    You can also exclude a path, file, inspection, or category from analysis, see the [](#Adjust+the+analysis+scope) section for details.

    The **Find similar problems** button lets you filter problems by type.
    
    Finally, you can use the **Copy** button to copy a link to a specific problem contained in the report.

7.  The **Report as false positive** button lets you create a related issue in YouTrack.

### Baseline problems
{id="ui-overview-baseline"}

<link-summary>When you click the Move selected to baseline button on the Actual problems tab, the selected
problems move to the Baseline tab.</link-summary>

When you click the **Move selected to baseline** button on the **[Current problems](#ui-overview-actual-problems)** tab, the selected
problems move to this tab.

<img src="ui-overview-baseline-tab.png" alt="Baseline problems tab" thumbnail="true" width="706" border-effect="line"/>

This tab UI is similar to the **Current problems** tab. To enable the baseline feature for future
inspections, follow the instructions that appear in the report UI. To learn more about the feature, explore the
[](baseline.topic) section.

### Inspections
{id="ui-overview-configuration"}

<link-summary>The Inspections tab lists the inspections and lets you adjust your inspection profile by specifying a 
set of inspections that Qodana will be using the next run.</link-summary>

The **Inspections** tab lists the inspections and lets you adjust your inspection profile by specifying a set of 
inspections that Qodana will be using the next run.

<img src="ui-overview-configuration.png" alt="The Inspections tab" thumbnail="true" width="706" border-effect="line"/>

Here, you can learn what each inspection does, as well as enable or disable it. To use this configuration for future use, 
you can download the `qodana.yaml` file and save it into your project root directory. 

See the [](#Adjust+your+inspection+profile) section to learn the best practices. 

> To learn more about inspection profiles, see the [](qodana-yaml.md#Set+up+a+profile) section.
> You can also edit profile settings in the [`qodana.yaml`](qodana-yaml.md) file.

The lower part of this tab contains the **Profile configuration** pane that lets you view the actual
configuration of %product%. Once you modify the configuration, it will be updated in this pane accordingly. 


### License audit
{id="ui-overview-project-audit"}

<link-summary>On the License audit tab, you can configure how %product% will run this feature.</link-summary>

<include from="lib_qd.topic" element-id="license-audit-tab" use-filter="ui-overview,empty" />

## Severity levels

<link-summary>This table shows the relation between various severities.</link-summary>

<p>This table shows the relation between severities in JetBrains IDEs, SARIF files, and %product% reports.</p>

<include from="lib_qd.topic" element-id="qodana-severity-levels" use-filter="for-profile,empty"/>

## Adjust your inspection profile 

We believe that the ability to see what was checked is as important as the list of problems found. For example, if you
haven't checked for typos, you can be happy to see zero typos in your project. There may be many of them – you just
don't check.

> Inspection profile can be configured either using the **[](#ui-overview-configuration)** tab or editing the 
> [`qodana.yaml`](qodana-yaml.md) file. 

If the number of problems is manageable, you can fix them and consider the 'problem-free code' goal achieved. We 
suggest that you follow that goal and fix new problems as soon as they appear.

In case the number of problems is above your expectations, we suggest using the Qodana features to examine them.

When you have no possibility to fix old problems and want to prevent the appearance of new ones, you can run Qodana in
 [baseline](docker-image-configuration.topic#docker-config-reference-baseline) mode.

### Adjust the analysis scope

#### Reduce the scope of analyzed issues
{id="reduce-analysis-scope"}

When viewing a code fragment with a detected problem, you may decide that it is irrelevant. You can make sure that more 
problems of the same type are omitted in the future. For this purpose, you can edit [qodana.yaml](qodana-yaml.md) or use 
the [](#ui-overview-actual-problems) tab as shown below.

1. **Exclude from the future analysis**

*Reason*: The analysis of the file containing the error, or even the directory containing this file, doesn't make sense 
in your project. For example, it's actually not the source code but some generated or downloaded content.

*Howto*: Under the code fragment view, expand the **Exclude** dropdown list and select the necessary option.
   
<img src="ui-overview-analysis-1.png" alt="Options of excluding from analysis" thumbnail="true" width="706" border-effect="line"/>  
    
*OR*:

Above the code fragment view, click the file path to navigate to the File explorer. 
      
<img src="ui-overview-analysis-2.png" alt="Navigating the file path in the project" thumbnail="true" width="706" border-effect="line"/>

On the File explorer, click the icon to the left of the filename, and then select **Mark as Excluded**.

<img src="ui-overview-analysis-3.png" alt="Excluding from analysis" thumbnail="true" width="706" border-effect="line"/>

2. **Hide a problem type or category from the list of problems**

*Reason*: You suppose that the error type or its category is not relevant or want to get back to it later.  
*Howto*: Under the code fragment view, expand the **Exclude** dropdown list and select the necessary option.
   
<img src="ui-overview-analysis-1.png" alt="Options of excluding from analysis" thumbnail="true" width="706" border-effect="line"/>  

> If you exclude either type/category or file/directory, the UI will remind you to save the changes if you want to use 
> them in future checks. Download the `qodana.yaml` file and store it under your project root directory.

#### Enable excluded or hidden problems

To reverse the exclusions you made, download `qodana.yaml` in the **[Profile configuration](#ui-overview-configuration)** section, edit 
it as necessary, put it in the project root directory, and then run Qodana again with this new configuration. 

To learn how to configure Qodana using `qodana.yaml`, see the [Configure profile](qodana-yaml.md) section.

## Open an HTML report

You can open HTML-formatted %instance% reports using JetBrains IDEs and shell commands.

<tabs>
<tab title="JetBrains IDEs" id="open-report-ide">
<p>You can open HTML reports using IntelliJ IDEA, PhpStorm, WebStorm, Rider, 
GoLand, PyCharm, and Rider as explained in the <a href="qodana-ide-plugin.md" anchor="ide-plugin-study-reports"/> section.</p> 
<p>In this case, your IDE needs to be installed via <a href="https://www.jetbrains.com/toolbox-app/">JetBrains Toolbox App</a>.</p>

</tab>
<tab title="Visual Studio Code" id="open-report-vscode">
<p>See the <a href="vscode.md" anchor="vs-code-explore-reports">Visual Studio Code</a> section for details.</p>
</tab>
<tab title="Shell commands" id="open-report-shell">
<p>When you run %instance% with the <code>--save-report</code> option, it stores an HTML version of the report in 
<code>/data/results/report</code>. This directory is typically mounted via Docker to let you view the HTML report later, 
independently of running %instance%. Due to JavaScript security restrictions, you cannot browse the HTML report by 
double-clicking the <code>index.html</code> file. Instead, the HTML report needs to be served via a web server, and you 
can run the Dockerized version of nginx, or invoke the Python or PHP built-in web servers as shown below.</p>

<procedure>
<step>After running %instance%, navigate to the <code>report</code> directory and make sure that the 
<code>index.html</code> file is present there.</step>
<step>
    <p>Serve the report using the web server of your choice:</p>
    <tabs>
        <tab title="Dockerized version of nginx">
            <code-block prompt="$">
                docker run -it --rm -p 8000:80 \
                  -v $(pwd):/usr/share/nginx/html nginx
            </code-block>
            <p>In your browser, navigate to <a href="http://localhost:8000">http://localhost:8000</a> to see the generated report.</p>
        </tab>
        <tab title="Python 2">
            <code-block prompt="$">
                python2 -m SimpleHTTPServer
            </code-block>
            <p>In your browser, navigate to <a href="http://localhost:8000">http://localhost:8000</a> to see the generated report.</p>
        </tab>
        <tab title="Python 3">
            <code-block prompt="$">
                python3 -m http.server
            </code-block>
            <p>In your browser, navigate to <a href="http://localhost:8000">http://localhost:8000</a> to see the generated report.</p>
        </tab>
        <tab title="PHP">
            <code-block prompt="$">
                php -S localhost:8000
            </code-block> 
            <p>In your browser, navigate to <a href="http://localhost:8000">http://localhost:8000</a> to see the generated report.</p>
        </tab>
    </tabs>    
</step>
</procedure>
</tab>
</tabs>
