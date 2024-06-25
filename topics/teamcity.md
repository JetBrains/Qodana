[//]: # (title: TeamCity)

<link-summary>Qodana functionality is available in TeamCity by default as a build step runner.</link-summary>

<var name="TeamCityProject" value="https://www.jetbrains.com/help/teamcity/configure-and-run-your-first-build.html#Create+your+first+project"/>
<var name="TeamCityBuildConfig" value="https://www.jetbrains.com/help/teamcity/creating-and-editing-build-configurations.html"/>
<var name="TeamCityBuildSteps" value="https://www.jetbrains.com/help/teamcity/configuring-build-steps.html"/>
<var name="TeamCityCommandLine" value="https://www.jetbrains.com/help/teamcity/command-line.html#General+Settings"/>
<var name="TeamCityPullRequests" value="https://www.jetbrains.com/help/teamcity/pull-requests.html"/>
<var name="TeamCityBranches" value="https://www.jetbrains.com/help/teamcity/configuring-finish-build-trigger.html#Trigger+Settings"/>

%product% is available in TeamCity as the `Qodana` 
[build runner](https://www.jetbrains.com/help/teamcity/build-runner.html). To start using it, these prerequisites
need to be met:

- You use TeamCity as a build server for your project. If not, learn how to do it in [TeamCity documentation](https://www.jetbrains.com/help/teamcity/teamcity-documentation.html).
- Your project language is included in the list of fully [supported technologies](linters.md).
- If you use your own TeamCity agents, make sure that Docker is installed on the agent machines and accessible by the users TeamCity is running under.
  TeamCity agents [hosted by JetBrains](https://www.jetbrains.com/help/teamcity/cloud/supported-platforms-and-environments.html#JetBrains-Hosted+Agents)
  already meet this condition.

<note>Currently, running Qodana on Windows-based build agents of TeamCity is not supported.</note>

### Add the Qodana runner
{id="teamcity-qodana-runner"}

<link-summary>You can configure the %product% runner in a TeamCity build.</link-summary>

<snippet id="teamcity-add-a-qodana-runner">

Assuming that you have already created your [project](%TeamCityProject%) and [build configuration](%TeamCityBuildConfig%), follow the steps below.    

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
      On the page that opens, select the <ui-path>Qodana</ui-path> runner.
   </step>
   <step>
      <p>On the <ui-path>New Build Step: Qodana</ui-path> page, click <ui-path>Show advanced options</ui-path> and configure the <ui-path>%product%</ui-path> runner:</p> 
   <list>
   <li>
      <ui-path>Step name</ui-path> uniquely identifies this step among other build steps.
   </li>
   <li>
      <ui-path>Step ID</ui-path> uniquely identifies this step among other build steps.
   </li>
   <li>
      <ui-path>Execute step</ui-path> configures the build condition that will trigger this build step.
   </li>
   <li>
      <ui-path>Working directory</ui-path> sets the directory for the build process, see the <a href="https://www.jetbrains.com/help/teamcity/build-working-directory.html">TeamCity</a> documentation for details. 
      You can leave this field empty if the <code>Checkout directory</code> parameter is specified on the <ui-path>Version Control Settings</ui-path> tab.
   </li>
   <li>
      <ui-path>Report ID</ui-path> uniquely identifies the report to let you distinguish between multiple reports when several inspection steps are configured within a single build.
   </li>
   <li>
      The <ui-path>Forward reports to TeamCity tests</ui-path> checkbox configures %instance% report availability in 
         the <a href="https://www.jetbrains.com/help/teamcity/build-results-page.html#Tests+Tab">Test tab</a> of the 
      TeamCity UI. Using this option, you can view codebase problems along with other problems detected. 
   </li>
   <li>
      <ui-path>Linter</ui-path> configures the <a href="linters.md">%product% linter</a>.
   </li>
   <li>
      <ui-path>Version</ui-path> is by default set to <code>Latest</code>.
   </li>
   <li>
      <p><ui-path>Inspection profile</ui-path> defines an <a href="inspection-profiles.md">inspection profile</a>:</p>
      <list>
         <li><code>Recommended (default)</code> is one of the <a href="inspection-profiles.md" anchor="inspection-profiles-existing-profiles">default profiles</a>.</li>
         <li><code>Embedded profile</code> lets you select a default profile, see the <a href="inspection-profiles.md" anchor="inspection-profiles-existing-profiles"/> section for details.</li>
         <li><code>Path to the IntelliJ profile</code> lets you specify the path to your <a href="inspection-profiles.md" anchor="inspection-profiles-custom-profiles">custom profile</a>. To use this option, 
      make sure that you also configure the custom profile in the <a href="inspection-profiles.md" anchor="inspection-profiles-yaml-file"><code>qodana.yaml</code></a> file.</li>
      </list>
   </li>
   <li><ui-path>Cloud Token</ui-path> configures a <a href="project-token.md">project token</a> generated in Qodana Cloud. </li>
   <li>
      <ui-path>Additional Docker arguments</ui-path> configures the arguments accepted by a Docker image, see the <a href="docker-image-configuration.topic"/> section for details.
   </li>
   <li>
      <ui-path>Additional Qodana arguments</ui-path> lets you extend the default Qodana functionality, see the <a href="docker-image-configuration.topic" anchor="docker-config-reference-option-overview"/> section for details.
   </li>
   </list>
      <img src="teamcity-runner.png" alt="Configuring the Qodana runner" width="680" border-effect="line"/>
   </step>
   <step>
      Click the <ui-path>Save</ui-path> button.
   </step>
</procedure>

</snippet>

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