[//]: # (title: Taint analysis)

<show-structure for="chapter" depth="3"/>

<var name="plugin-url" value="https://plugins.jetbrains.com/plugin/25724-security-analysis-by-qodana/edit"/>

<link-summary>Taint analysis is a process of assessing a flow of untrusted user input throughout the body of a 
function or method. If you have a taint in your code, hackers can execute these code fragments to cause SQL injection, 
arithmetic overflow, cross-site scripting, path traversal.</link-summary>

Taint analysis lets you trace the flow of potentially harmful or tainted data through a
program. It identifies paths where untrusted input or sources might reach sensitive operations or sinks without proper
validation or sanitization, which helps prevent security vulnerabilities like SQL injections, cross-site scripting (XSS), 
command injections, and path traversal.

The core goal of taint analysis is to determine if unanticipated input can affect program execution in malicious ways.

Taint analysis is supported by the [%php%](php.md) and [%jvm%](jvm.md) linters under the Ultimate Plus 
[license](pricing.md).

## How it works

<link-summary>Learn how taint analysis works.</link-summary>

Tainted data is called a **source**, while a vulnerable function that may contain a source is called a **sink**.
In this case, tainted data travels to sinks via propagators, such as function calls or assignments.

<img src="taint-analysis.png" dark-src="taint-analysis_dark.png" width="706" alt="Taint analysis diagram" border-effect="line"/>

To prevent such propagation, the taint analysis applies several approaches like data sanitization or data
transformation to a safe state. Here, tags are removed to resolve the taint:

```PHP
<?php
$taint = $_GET['some_key'];
$taint = strip_tags($taint);
```

Data validation conforms to a required pattern. In this sample, validation for the `$email` 
variable is enabled:
    
```PHP
<?php
$email = $_GET['email'];
if (filter_var($email, FILTER_VALIDATE_EMAIL)) {
  echo $email;
}
```

## Before you start

<link-summary>Prerequisites for running the taint analysis feature.</link-summary>

This section explains how you can run taint analysis in IntelliJ IDEA and CI/CD pipelines.

### IntelliJ IDEA
{id="ta-deploy-idea"}

Before you run taint analysis in IntelliJ IDEA, install the [**Security Analysis by Qodana**](%plugin-url%) plugin.
To do it, navigate to the **Problems** tool window and click the **Security Analysis** tab. On this tab, 
click the **Install plugin** button.  

<img src="taint-analysis-install.png" width="706" alt="Taint analysis installation" border-effect="line" />

Alternatively, navigate to **File | Settings | Plugins** and install the [**Security Analysis by Qodana**](%plugin-url%) 
plugin. 

### CI/CD
{id="ta-deploy-other"}

Taint analysis is available by default once you enable the
`qodana.recommended` [inspection profile](inspection-profiles.md#inspection-profiles-existing-profiles).

## Run taint analysis

<link-summary>Explore how you can run taint analysis.</link-summary>

### IntelliJ IDEA
{id="ta-analysis-idea"}

<procedure>
<step>
<p>Navigate to the <control>Problems</control> tool window and then click the <control>Security Analysis</control>
tab. On this tab, click the <control>Run Taint Analysis</control> button.</p>

<img src="taint-analysis-run-first-step.png" width="706" alt="Running taint analysis from the Problems tool window" border-effect="line"/>

<p>Alternatively, you can navigate to <control>Tools | Security Analysis | Run Taint Analysis</control>.</p>
</step>
<step>
<p>On the dialog that opens configure taint analysis.</p>
<img src="taint-analysis-configuration.png" width="610" alt="Configuring taint analysis" border-effect="line"/>
<p>Here you can configure the scope of files that you would like to analyze using taint analysis, as well as file masks
for the analyzed files.</p> 
<p>The <control>Inspection options</control> group contains several tabs:</p>
<tabs>
    <tab title="Settings for in-Editor Analysis" id="ta-in-editor-analysis">
        <p>Options applied to an opened file in real time.</p>
        <p>The <ui-path>Analysis depth (from a current file)</ui-path> field configures 
analysis depth using the <code>Current file -> File 1 (Low) -> File 2 (Medium) -> File 3 (High)</code> reference pattern. 
For example, the <ui-path>Medium</ui-path> setting configures the reference to <code>File 2</code> from this pattern.</p>
        <p>The <ui-path>Analysis time limit for in-editor analysis (ms)</ui-path> field configures the amount of time 
that can be allocated for a specific file. The default value is 5000 ms.</p>
    </tab>
    <tab title="Settings for Batch Analysis" id="ta-batch-analysis">
        <p>Configuration of batch analysis over an entire project.</p>
        <p>The <ui-path>Analysis depth (from a current file)</ui-path> field configures 
analysis depth using the <code>Current file -> File 1 (Low) -> File 2 (Medium) -> File 3 (High)</code> reference pattern. 
For example, the <ui-path>Medium</ui-path> setting configures the reference to <code>File 2</code> from this pattern.</p>
    </tab>
    <tab title="Common Settings" id="ta-common-settings">
        <p>The <ui-path>Use caches during analysis</ui-path> field lets you use caching. While consuming disk space, it
can improve analysis performance.</p>
        <p>If enabled, the <ui-path>Enable computation expensive configurations</ui-path> checkbox involves additional
analysis techniques that can improve output but will significantly impact performance.</p>
    </tab>
</tabs>
</step>
</procedure>

#### Explore results

In your IDE, point to a suspicious code fragment and then click the <ui-path>Show DFA trace 1</ui-path> link to open 
the **Security Analysis** tab.

<img src="taint-analysis-explore-results.gif" alt="Taint analysis in IntelliJ IDEA" width="793" border-effect="line"/>

The left part of the <ui-path>Security Analysis</ui-path> tab contains all steps of a source-to-sink track.
The right part shows the code fragments corresponding to a specific step. You can click any step to see the source trace 
to the sink.

<img src="taint-analysis-step-navigation.gif" alt="Navigating steps between a source and a sink" width="793" border-effect="line"/>

#### Configure the Security Analysis tab

Configure the **Security Analysis** tab by navigating to **File | Settings | Advanced settings**.
Here, find the **Security Analysis** section and then configure the **Show Problem Tab** checkbox.  

<img src="taint-analysis-configure-tab.png" alt="Configuring the Security Analysis tab" width="706" border-effect="line"/>

### CI/CD
{id="ta-analysis-other"}

<snippet id="running-taint-analysis">

<tabs>
  <tab title="%php%" id="php">
  <p>In the <a href="qodana-yaml.md"><code>qodana.yaml</code></a> file,
  <a href="qodana-yaml.md" anchor="Include+an+inspection+into+the+analysis+scope">include</a> the 
  <code>PhpVulnerablePathsInspection</code> inspection into the analysis scope:</p>

  <code-block lang="yaml">
  include:
    - name: PhpVulnerablePathsInspection
  </code-block>

  <p>Alternatively, you can use the <code>inspections</code> section of <code>qodana.yaml</code>:</p>

  <code-block lang="yaml">
  inspections:
    - inspection: PhpVulnerablePathsInspection
      enabled: true
  </code-block>

  </tab>
  <tab title="%jvm%" id="jvm">
  <p>In the <a href="qodana-yaml.md"><code>qodana.yaml</code></a> file,
  <a href="qodana-yaml.md" anchor="Include+an+inspection+into+the+analysis+scope">include</a> the 
  <code>JvmTaintAnalysis</code> inspection into the analysis scope:</p>

  <code-block lang="yaml">
  include:
    - name: JvmTaintAnalysis
  </code-block>

  <p>Alternatively, you can use the <code>inspections</code> section of <code>qodana.yaml</code>:</p>

  <code-block lang="yaml">
  inspections:
    - inspection: JvmTaintAnalysis
      enabled: true
  </code-block>
  </tab>
</tabs>
</snippet>