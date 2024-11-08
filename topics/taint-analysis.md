[//]: # (title: Taint analysis)

<show-structure for="chapter" depth="3"/>

<link-summary>Taint analysis is a process of assessing a flow of untrusted user input throughout the body of a 
function or method. If you have a taint in your code, hackers can execute these code fragments to cause SQL injection, 
arithmetic overflow, cross-site scripting, path traversal.</link-summary>

Taint analysis is a method used in security testing to trace the flow of potentially harmful or tainted data through a
program. It identifies paths where untrusted input or sources might reach sensitive operations or sinks without proper
validation or sanitization, which helps prevent security vulnerabilities like SQL injections, cross-site scripting (
XSS), command injections, and path traversal.

The core goal of taint analysis is to determine if unanticipated input can affect program execution in malicious ways.

Taint analysis is supported by the [%php%](php.md) and [%jvm%](jvm.md) linters under the Ultimate Plus 
[license](pricing.md).

## How it works

Tainted data is called a **source**, while a vulnerable function that may contain a source is called a **sink**.
In this case, tainted data travels to sinks via propagators, such as function calls or assignments.

<img src="taint-analysis.png" dark-src="taint-analysis_dark.png" width="706" alt="Taint analysis diagram" border-effect="line"/>

To prevent such propagation, the taint analysis feature applies several approaches. For example, data sanitization or data
transformation to a safe state. Here, tags are removed to resolve the taint:

```PHP
<?php
$taint = $_GET['some_key'];
$taint = strip_tags($taint);
```

Data validation, i.e. checking the data conforms with a required pattern. In this sample, validation for the `$email` 
variable is enabled:
    
```PHP
<?php
$email = $_GET['email'];
if (filter_var($email, FILTER_VALIDATE_EMAIL)) {
  echo $email;
}
```

## Deployment

### IntelliJ IDEA
{id="ta-deploy-idea"}

In IntelliJ IDEA, you should install the 
[**Security Analysis by Qodana**](https://plugins.jetbrains.com/plugin/25724-security-analysis-by-qodana/edit) plugin.
To do it, navigate to the **Problems** tool window and then click the **Security Analysis** tab. On this tab, 
click the **Download security analysis plugin** link.

<img src="taint-analysis-install.gif" width="793" alt="Taint analysis installation" border-effect="line" />

To configure taint analysis, follow the steps below.
<procedure>
<step>In IntelliJ IDEA, navigate to 
<a href="https://www.jetbrains.com/help/idea/inspections-settings.html"><ui-path>Inspections</ui-path></a>.</step>
<step>In <ui-path>Inspections</ui-path>, navigate to the <ui-path>Security</ui-path> list, and then expand it.</step>
<step>In the <ui-path>Security</ui-path> list, click <ui-path>Taint analysis</ui-path>.</step>
</procedure>

The lower-right part of the window contains options divided into several tabs described below.

<img src="taint-analysis-configuration.png" alt="Taint analysis configuration" width="706" border-effect="line"/>

<tabs>
    <tab title="Settings for in-Editor Analysis" id="ta-in-editor-analysis">
        <p>This configures the in-Editor analysis that occurs over a specific file in real time.</p>
        <p>The <ui-path>Max depth of referenced file from current for in-editor analysis</ui-path> field configures 
analysis depth using the <code>file 1 -> file 2 (level 1) -> file 3 (level 2) -> -> file 4 (level 3) -> ...</code> pattern 
where a specified value configures how deep your code will be analyzed. From the pattern, you can see that, for example, 
<code>2</code> will cover two references. The default value is <code>1</code> (one) meaning that only one reference to 
another file will be analyzed.</p>
        <p>The <ui-path>Analysis time limit for in-editor analysis (ms)</ui-path> field configures the amount of time 
that can be allocated for a specific file. The default value is 5000 ms.</p>
    </tab>
    <tab title="Settings for Batch Analysis" id="ta-batch-analysis">
        <p>This configures the batch analysis that occurs over an entire project.</p>
        <p>The <ui-path>Max depth of referenced file from current for batch analysis</ui-path> field configures analysis 
depth using the <code>file 1 -> file 2 (level 1) -> file 3 (level 2) -> -> file 4 (level 3) -> ...</code> pattern where 
a specified value configures how deep your code will be analyzed. From the pattern, you can see that, for example, 
<code>2</code> will cover two references. The default value is <code>1</code> (one) meaning that only one reference to 
another file will be analyzed.</p>
        <p>The <ui-path>Operation count limit for batch analysis (millions)</ui-path> field limits the number of steps
in batch analyses.</p>
        <p>The <ui-path>Record performance metrics in %product%</ui-path> checkbox is useful in case of 
performance problems. By enabling this, you can send us the <code>qodana.sarif.json</code> file once analysis is complete.</p>
    </tab>
    <tab title="Common Settings" id="ta-common-settings">
        <p>The <ui-path>Maximum number of declarations to analyze at once</ui-path> configures the maximal number of 
    declarations that will be analyzed within a single file. Once this limit is reached, the maximal analysis depth will be 
    set to 1.</p>
        <p>The <ui-path>Use caches during analysis</ui-path> lets you use caching. Using caches can consume disk space, but
can improve analysis performance.</p>
    </tab>
</tabs>

### Other
{id="ta-deploy-other"}

If you run %product% outside JetBrains IDEs, taint analysis is available by default once you enable the
`qodana.recommended` [inspection profile](inspection-profiles.md#inspection-profiles-existing-profiles).

## Analysis

<link-summary>Explore how you can run the taint analysis using JetBrains IDE and Qodana.</link-summary>

<!-- The Open DFA 1 section needs to be mentioned here -->

### IntelliJ IDEA
{id="ta-analysis-idea"}

Once analysis is complete, in your IDE point to a suspicious code fragment, and then click the 
<ui-path>Show DFA trace 1</ui-path> link.

<img src="ta-analysis-idea.gif" alt="Taint analysis in IntelliJ IDEA" width="793" border-effect="line"/>

The left part of the <ui-path>Security Analysis</ui-path> contains a track of a source to a sink including all steps.
The right part shows the code fragments related to steps.

<img src="ta-analysis-idea_2.png" alt="The Security Analysis tab" width="706" border-effect="line"/>

You can click any step to see the source trace to the sink.

### Other
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
  <code>PhpVulnerablePathsInspection</code> inspection into the analysis scope:</p>

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