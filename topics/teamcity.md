[//]: # (title: TeamCity)

<link-summary>Qodana functionality is available in TeamCity by default as a build step runner.</link-summary>

<var name="TeamCityProject" value="https://www.jetbrains.com/help/teamcity/configure-and-run-your-first-build.html#Create+your+first+project"/>
<var name="TeamCityBuildConfig" value="https://www.jetbrains.com/help/teamcity/creating-and-editing-build-configurations.html"/>
<var name="TeamCityBuildSteps" value="https://www.jetbrains.com/help/teamcity/configuring-build-steps.html"/>
<var name="TeamCityCommandLine" value="https://www.jetbrains.com/help/teamcity/command-line.html#General+Settings"/>
<var name="TeamCityPullRequests" value="https://www.jetbrains.com/help/teamcity/pull-requests.html"/>
<var name="TeamCityBranches" value="https://www.jetbrains.com/help/teamcity/configuring-finish-build-trigger.html#Trigger+Settings"/>
<var name="teamcity-linter-list" value="Here, specify the linter that you would like to run."/>

%product% is available in TeamCity as the `Qodana` 
[build runner](https://www.jetbrains.com/help/teamcity/build-runner.html). To start using it, these prerequisites
need to be met:

- You use TeamCity as a build server for your project. If not, learn how to do it in [TeamCity documentation](https://www.jetbrains.com/help/teamcity/teamcity-documentation.html).
- Your project language is included in the list of fully [supported technologies](linters.md).
- If you use your own TeamCity agents, make sure that Docker is installed on the agent machines and accessible to the users TeamCity is running under.
  TeamCity agents [hosted by JetBrains](https://www.jetbrains.com/help/teamcity/cloud/supported-platforms-and-environments.html#JetBrains-Hosted+Agents)
  already meet this condition.

<note>Currently, running Qodana on Windows-based build agents of TeamCity is not supported.</note>

### Add the Qodana runner
{id="teamcity-qodana-runner"}

<link-summary>You can configure the %product% runner in a TeamCity build.</link-summary>

<include from="lib_qd.topic" element-id="teamcity-add-a-qodana-runner" use-filter="empty"/>

### Quality gate and baseline

<snippet id="teamcity-code-quality-baseline">

Using the **Additional Qodana arguments** field of the [`Qodana`](#teamcity-qodana-runner) runner configuration, you can configure the 
[quality gate](quality-gate.topic) and [baseline](baseline.topic) features:

* `--fail-threshold <number>` option for configuring a quality gate, 
* `--baseline <path/to/qodana.sarif.json>` option for configuring a baseline. 

To configure both options, in the **Additional Qodana arguments** field separate them using a space character: 

```Shell
--fail-threshold <number> --baseline <path/to/qodana.sarif.json>
```

</snippet>

### Analyze pull requests and specific branches

Information about configuring TeamCity for analyzing pull and merge requests is available on the 
[TeamCity](%TeamCityPullRequests%) documentation portal.

To learn how to analyze specific branches, see the [Trigger Settings](%TeamCityBranches%) section of the TeamCity documentation.

### Add a configuration script
{id="add-script"}

<link-summary>Custom profile configuration for Qodana linters is stored in the qodana.yaml file. When using a CI system, 
you need to put this file to the working directory manually. Alternatively, you can write a script that will do it for you.</link-summary>

<!-- This should be rewritten the same way as before -->

Custom profile configuration for Qodana linters is stored in the [`qodana.yaml`](qodana-yaml.md) file. When using a CI 
system, you need to put this file to the working directory manually. Alternatively, you can write a script that will do it for you.

<procedure>
   <step>
      In the TeamCity UI, navigate to the <a href="%TeamCityBuildConfig%">configuration page</a> of a build where you would 
      like to run %product%.
   </step>
   <step>
      On the <ui-path>Build Configuration Settings</ui-path> page, navigate to the <a href="%TeamCityBuildSteps%"><ui-path>Build steps</ui-path></a> page.
   </step>
   <step>
      On the <ui-path>Build steps</ui-path> page, click the <ui-path>Add build step</ui-path> button.
   </step>
   <step>
      On the page that opens, select the <code>Command line</code> runner.
   </step>
   <step>
      <p>Configure the <code>Command line</code> runner as described on the <a href="%TeamCityCommandLine%">TeamCity documentation portal</a>.</p>
      <img src="teamcity-plugin-5.png" alt="Expanding all configuration options of the Command Line runner" width="706" border-effect="line"/>
   </step>
   <step>
      <p>In the <ui-path>Custom script</ui-path> field, paste a script that adds a 
custom <code>qodana.yaml</code> file to the working directory. In the example below, the script appends the 
following inspection exclusions to the configuration file:</p>
<code-block lang="shell">
<![CDATA[ 
#!/bin/sh

FILE="./qodana.yaml"

/bin/cat <<EOM >$FILE
exclude:
- name: Annotator
- name: AnotherInspectionId
  paths:
   - relative/path
   - another/relative/path
- name: ProhibitedDependencyLicense

EOM
]]>
</code-block>
   </step>
</procedure>

<!-- Add a use case about code quality and baseline -->
<!-- Add the analysis of specific branches use case here as well -->
<!-- Case about analyzing pull requests needs to be added here -->

### Verify inspection results

<link-summary>Now that you have configured and run the build, you can see analysis results.</link-summary>

Now that you have configured and run the build, you can examine analysis results in [Qodana Cloud](cloud-overview-reports.topic).  

Alternatively, you can view analysis results using the TeamCity UI, follow the steps below:

<!-- Images here should be updated as well -->

<procedure>
<step>
<p>Navigate to a project build page. On the <ui-path>Overview</ui-path> tab, click the build entry.</p>
<img src="teamcity-plugin-verification-1.png" alt="Navigating to the build entry" width="706" border-effect="line"/>
</step>
<step>
<p>On the build page, navigate to the <ui-path>Qodana</ui-path> tab to find the inspection report. To learn more about Qodana 
reports, see the <a href="ui-overview.md"/> section of this documentation.</p>
<img src="teamcity-plugin-verification-2.png" alt="Navigating to the Qodana tab" width="706" border-effect="line"/>
</step>
</procedure>