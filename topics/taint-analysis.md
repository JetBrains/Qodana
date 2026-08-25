[//]: # (title: Taint analysis)

<show-structure for="chapter" depth="3"/>

<var name="plugin-url" value="https://plugins.jetbrains.com/plugin/25724-security-analysis-by-qodana/edit"/>

<link-summary>Taint analysis is a process of assessing a flow of untrusted user input throughout the body of a 
function or method. If you have a taint in your code, hackers can execute these code fragments to cause SQL injection, 
arithmetic overflow, cross-site scripting, path traversal.</link-summary>

Taint analysis lets you trace the flow of potentially harmful or tainted data through a
program. It identifies paths where untrusted input or sources might reach sensitive operations or sinks without proper
validation or sanitization, which helps prevent security vulnerabilities like SQL injections, cross-site scripting (XSS), 
command injections, and path traversal. The core goal is to determine if unanticipated input can affect program 
execution in malicious ways.

Taint analysis is supported by IntelliJ IDEA Ultimate, as well as by the [%php%](php.md), [%jvm%,](jvm.md) 
and the [%dotnet%](dotnet.md) linters under the Ultimate Plus [license](pricing.md). Information about available %product% licenses is available on the 
[Subscription Options and Pricing](https://www.jetbrains.com/qodana/buy/?billing=yearly) page.
You can also [request a demo](https://www.jetbrains.com/qodana/request-a-demo/).

This feature provides built-in taint rules for the most common 
categories of OWASP Top 10:2021 vulnerabilities (A01, A03, A07, A08, A10). In addition to the built-in rules, you can 
configure custom taint rules for your own application or library code, designating specific functions or methods as sources or sinks.

The taint analysis feature runs locally and does not require any external dependencies or services.

## How taint analysis works

<link-summary>Learn how taint analysis works.</link-summary>

Tainted data is called a **source**, while a vulnerable function that may contain a source is called a **sink**.

<img src="taint-analysis.png" dark-src="taint-analysis_dark.png" width="706" alt="Taint analysis diagram" border-effect="line"/>

Between a source and a sink, tainted data can travel through various **passthrough** functions whose calls are also marked as
tainted if the input data was initially marked as tainted. The **sanitizer** functions can be used to make data safe 
for further processing through several approaches like data sanitization or data transformation to a safe state.

The projection approach lets you share the taint status across all arguments of a function call. This ensures that 
the taint status of the arguments is transferred to the return value.

### Default behavior in IntelliJ IDEA

If there is no specific configuration available for a library function call, a projection will be applied by default. 
This means the taint status of the function arguments will be passed to the return value, maintaining the integrity of the taint analysis.

To override the default behavior, you can apply [custom configurations](#Configure+function+calls) to specific function calls. 

### %dotnet%

Starting from version 2026.2, the [%dotnet%](dotnet.md) linter supports rules compatible with [Opengrep](https://www.opengrep.dev/) 
for configuring taint analysis. It already includes a set of built-in C#, JavaScript, and TypeScript rules that you can 
use as %product% inspections, so you don’t have to download or configure them manually. Examples of such rules are available in our [GitHub repository](https://github.com/qodana/opengrep-sast-rules/tree/master/jetbrains).
The list of supported rules is provided in the [](#ta-dotnet-rules-list) chapter.

Information about developing custom rules is available on the [Semgrep website](https://docs.semgrep.dev/writing-rules/overview).

## Before you start

<link-summary>Prerequisites for running the taint analysis feature.</link-summary>

This section explains how you can run taint analysis using IntelliJ IDEA and %product% linters.

### IntelliJ IDEA
{id="ta-deploy-idea"}

Before you run taint analysis in your IDE, install the [**Security Analysis by Qodana**](%plugin-url%) plugin.
To do it, in IntelliJ IDEA navigate to the **Problems** tool window and click the **Security Analysis** tab. On this tab, 
click the **Install plugin** button.  

<img src="taint-analysis-install.png" width="706" alt="Taint analysis installation" border-effect="line" />

Alternatively, navigate to **File | Settings | Plugins** and install the [**Security Analysis by Qodana**](%plugin-url%) 
plugin. 

### Qodana linters
{id="ta-deploy-other"}

Taint analysis is available for the [%php%](php.md) and [%jvm%](jvm.md) linters once you invoke the
`qodana.recommended` [inspection profile](inspection-profiles.md#inspection-profiles-existing-profiles):

```yaml
version: 1.0
profile:
  name: qodana.recommended
```

For the [%dotnet%](dotnet.md) linter, taint analysis is enabled by default. 

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
<p>On the dialog that opens, configure the taint analysis.</p>
<img src="taint-analysis-configuration.png" width="610" alt="Configuring taint analysis" border-effect="line"/>
<p>Here you can configure the scope of files that you would like to analyze using taint analysis, as well as file masks
for the analyzed files.</p> 
<p>The <control>Inspection options</control> group contains several tabs:</p>
<tabs>
    <tab title="Settings for in-Editor Analysis" id="ta-in-editor-analysis">
        <p>Options applied to an opened file in real time.</p>
        <p>The <ui-path>Analysis depth (from a current file)</ui-path> field configures 
analysis depth using the <code>Current file → File 1 (Low) → File 2 (Medium) → File 3 (High)</code> reference pattern. 
For example, the <ui-path>Medium</ui-path> setting configures the reference to <code>File 2</code> from this pattern.</p>
        <p>The <ui-path>Analysis time limit for in-editor analysis (ms)</ui-path> field configures the amount of time 
that can be allocated for a specific file. The default value is 5000 ms.</p>
    </tab>
    <tab title="Settings for Batch Analysis" id="ta-batch-analysis">
        <p>Configuration of batch analysis over an entire project.</p>
        <p>The <ui-path>Analysis depth (from a current file)</ui-path> field configures 
analysis depth using the <code>Current file → File 1 (Low) → File 2 (Medium) → File 3 (High)</code> reference pattern. 
For example, the <ui-path>Medium</ui-path> setting configures the reference to <code>File 2</code> from this pattern.</p>
    </tab>
    <tab title="Common Settings" id="ta-common-settings">
        <p>The <ui-path>Use caches during analysis</ui-path> field lets you use caching. While consuming disk space, it
can improve analysis performance.</p>
        <p>If enabled, the <ui-path>Enable computation expensive configurations</ui-path> checkbox involves additional
analysis techniques that can improve output but will significantly impact performance.</p>
        <p>Using the <ui-path>Safe classes</ui-path> box, you can configure the existing safe classes and define your own.</p>
    </tab>
</tabs>
</step>
</procedure>

If no issues were detected, it is possible that the taint analysis configuration is incomplete. Make sure that you 
defined all necessary sources, sinks, and sanitizers, as explained in the [](#Configure+function+calls) chapter. 

#### Explore results

In your IDE, point to a suspicious code fragment and then click the <ui-path>Show taint ... trace</ui-path> link to open 
the **Security Analysis** tab.

<img src="taint-analysis-explore-results.gif" alt="Taint analysis in IntelliJ IDEA" width="793" border-effect="line"/>

The left part of the <ui-path>Security Analysis</ui-path> tab contains all steps of a taint trace.
The right part shows the code fragments corresponding to a specific step. You can click any step to see the source trace 
to the sink.

<img src="taint-analysis-step-navigation.gif" alt="Navigating steps between a source and a sink" width="793" border-effect="line"/>


#### Configure function calls

The analysis of function calls is carried out using the default configuration in case a function call does 
not match any existing configuration. In this case, the taint analysis builds a projection for this function. The default
configuration already covers basic sources, sinks, and sanitizers. 

You can configure function calls as your custom sources and sinks as explained below. This example uses the following
unconfigured function calls:

*  `java.net.URI.getQuery` can be configured as a source of tainted data to represent a point where potentially untrusted input enters the system.
* `java.io.OutputStream.write` can be configured as a sink where potentially tainted data may be written to an output stream, such as a file or network socket.

<procedure>
<step><p>In the upper-right part of the <ui-path>Security Analysis</ui-path> tab, click the context menu and then click 
        the <ui-path>Highlight Taint Configuration</ui-path> link.</p>  
        <img src="taint-analysis-step-navigation-2.png" alt="Navigating to Hightlight Taint Configuration" width="706" border-effect="line"/>
<p>This will open the tab containing current configuration settings applied to all function calls or places where functions are 
called within the currently opened file.</p> 
<img src="taint-analysis-step-navigation-3.png" alt="Settings available for all function calls" width="706" border-effect="line"/>
<p>If a function reference matches a specific configuration, the corresponding configuration will be highlighted 
indicating how it will be treated during analysis. The configuration for function references will appear in the list in 
the same order as references are located in the file.</p>
</step>
<step><p>In the list of projections, select the projection reference and apply a respective Quick-Fix option.</p>
<img src="taint-analysis-step-navigation-4.png" alt="Applying Quick-Fixes" width="706" border-effect="line"/>
<p>This will create the <code>inspections/config.inspection.kts</code> file for a source, sink, and sanitizer configuration. 
To ensure consistency of analysis reports save this file in the root directory of your project.</p>
</step>
<step><p>In the <code>inspections/config.inspection.kts</code> file, assign specific taint rules to a newly added
sources and sinks. The configuration from this file is applied to the <a anchor="ta-analysis-other">Taint Analysis inspection</a> when the project opens.</p> 
<p>For the <code>java.net.URI.getQuery</code> function call as a source, save this configuration to define a point where 
potentially untrusted input enters a system:</p>
<code-block lang="kotlin">
    source(
        "java.net.URI.getQuery",
        "java.lang.String",
        TaintRule.allRulesList()
    )
</code-block>
<p>For the <code>java.io.OutputStream.write</code> function call as a sink, save the following configuration to ensure 
that the data reaching the sink are verified for proper sanitization according to the chosen rule to prevent the 
propagation of unsafe data:</p>
<code-block lang="kotlin">
    sink(
        "java.io.OutputStream.write",
        listOf(1),
        TaintRule.XSS
    )
</code-block>
</step>
<step>Once the configuration is written, recompile the <code>inspections/config.inspection.kts</code> file.</step>
</procedure>

#### Configure the Security Analysis tab

Configure the **Security Analysis** tab by navigating to **File | Settings | Advanced settings**.
Here, find the **Security Analysis** section and then configure the **Show Problem Tab** checkbox.  

<img src="taint-analysis-configure-tab.png" alt="Configuring the Security Analysis tab" width="706" border-effect="line"/>

### Qodana linters
{id="ta-analysis-other"}

<snippet id="running-taint-analysis">

<tabs>
  <tab title="%php%" id="php">
  <p>In the <code>qodana.yaml</code> file,
  <a href="configuration-reference.md" anchor="Including+inspections">include</a> the 
  <a href="https://www.jetbrains.com/help/inspectopedia/PhpVulnerablePathsInspection.html"><code>PhpVulnerablePathsInspection</code></a> 
    inspection into the analysis scope:</p>

  <code-block lang="yaml" emphasize-lines="7-8"><![CDATA[
  version: "1.0"

  linter: %php-linter%

  profile:
    inspections:
      — inspection: PhpVulnerablePathsInspection
        enabled: true
  ]]>
</code-block>
  </tab>
  <tab title="%jvm%" id="jvm">
  <p>In the <code>qodana.yaml</code> file,
  <a href="configuration-reference.md" anchor="Including+inspections">include</a> the 
  <code>JvmTaintAnalysis</code> inspection into the analysis scope:</p>

  <code-block lang="yaml" emphasize-lines="7-8"><![CDATA[
  version: "1.0"

  linter: %jvm-linter%

  profile:
    inspections:
      — inspection: JvmTaintAnalysis
        enabled: true
  ]]>
</code-block>
  </tab>
</tabs>
</snippet>

#### Qodana for .NET

Taint analysis is by default enabled for the %dotnet% linter. You can override the default behavior using 
capabilities explained below.

##### Set the number of traces

By default, taint analysis is configured for monitoring one hundred (100) traces at a time. You can override this
using the `dfa.analysis.rml.max.traces.count=<number>` property, for example:

<tabs group="cli-settings">
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$" emphasize-lines="5"><![CDATA[
            docker run \
               -v $(pwd):/data/project/ \
               -e QODANA_TOKEN="<cloud-project-token>" \
               %dotnet-image% \
               --property=dfa.analysis.rml.max.traces.count=1000 
        ]]>
</code-block>
    </tab>
    <tab title="Qodana CLI" group-key="qodana-cli">
        <code-block lang="shell" prompt="$" emphasize-lines="3"><![CDATA[
            qodana scan \
               -e QODANA_TOKEN="<cloud-project-token>" \
               --property=dfa.analysis.rml.max.traces.count=1000
        ]]>
</code-block>
    </tab>
    <tab title="GitHub Actions" group-key="github-actions">
    <code-block lang="yaml" emphasize-lines="25"><![CDATA[
        name: Qodana
        on:
            workflow_dispatch:
            pull_request:
            push:
                branches: # Specify your branches here
                    - main # The 'main' branch
                    - master # The 'master' branch
                    - 'releases/*' # The release branches
        jobs:
            qodana:
                runs-on: ubuntu-latest
                permissions:
                    contents: write
                    pull-requests: write
                    checks: write
                steps:
                    - uses: actions/checkout@v3
                      with:
                          ref: ${{ github.event.pull_request.head.sha }}  # to check out the actual pull request commit, not the merge commit
                          fetch-depth: 0  # a full history is required for pull request analysis
                    - name: 'Qodana Scan'
                      uses: %action-version%
                      with:
                          args: --property=dfa.analysis.rml.max.traces.count=1000
                      env:
                          QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
    ]]>
</code-block>
    </tab>
    <tab title="Jenkins" group-key="jenkins">
        <code-block lang="groovy" emphasize-lines="19"><![CDATA[
            pipeline {
                environment {
                    QODANA_TOKEN=credentials('qodana-token')
                }
                agent {
                    docker {
                        args '''
                          -v "${WORKSPACE}":/data/project
                          --entrypoint=""
                          '''
                        image '%dotnet-image%'
                    }
                }
                stages {
                    stage('Qodana') {
                        steps {
                            sh '''
                            qodana \
                            --property=dfa.analysis.rml.max.traces.count=1000
                            '''
                        }
                    }
                }
            }
        ]]>
</code-block>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
        <code-block lang="yaml" emphasize-lines="5"><![CDATA[
            include:
                - component: %gitlab-version%
                  inputs:
                      args: |
                          --property=dfa.analysis.rml.max.traces.count=1000
                          --linter %dotnet-linter%
        ]]>
</code-block>
    </tab>
    <tab title="TeamCity" group-key="teamcity">
        <p>In the runner configuration, find the <ui-path>Additional Docker arguments</ui-path> field and
            specify the property:</p>
        <code-block lang="shell"><![CDATA[
            --property=dfa.analysis.rml.max.traces.count=1000
        ]]>
</code-block>
    </tab>
</tabs>

##### Disable bundled rules

You can disable the bundled rules by configuring the `IDEA_PROPERTIES` variable:

<tabs group="cli-settings">
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$" emphasize-lines="4"><![CDATA[
            docker run \
               -v $(pwd):/data/project/ \
               -e QODANA_TOKEN="<cloud-project-token>" \
               -e IDEA_PROPERTIES=intellij.opengrep.rules.downloaded.source.enabled=false \
               %dotnet-image% \
        ]]>
</code-block>
    </tab>
    <tab title="Qodana CLI" group-key="qodana-cli">
        <code-block lang="shell" prompt="$" emphasize-lines="3"><![CDATA[
            qodana scan \
               -e QODANA_TOKEN="<cloud-project-token>" \
               -e IDEA_PROPERTIES=intellij.opengrep.rules.downloaded.source.enabled=false
        ]]>
</code-block>
    </tab>
    <tab title="GitHub Actions" group-key="github-actions">
    <code-block lang="yaml" emphasize-lines="25"><![CDATA[
        name: Qodana
        on:
            workflow_dispatch:
            pull_request:
            push:
                branches: # Specify your branches here
                    - main # The 'main' branch
                    - master # The 'master' branch
                    - 'releases/*' # The release branches
        jobs:
            qodana:
                runs-on: ubuntu-latest
                permissions:
                    contents: write
                    pull-requests: write
                    checks: write
                steps:
                    - uses: actions/checkout@v3
                      with:
                          ref: ${{ github.event.pull_request.head.sha }}  # to check out the actual pull request commit, not the merge commit
                          fetch-depth: 0  # a full history is required for pull request analysis
                    - name: 'Qodana Scan'
                      uses: %action-version%
                      with:
                          args: -e IDEA_PROPERTIES=intellij.opengrep.rules.downloaded.source.enabled=false
                      env:
                          QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
    ]]>
</code-block>
    </tab>
    <tab title="Jenkins" group-key="jenkins">
        <code-block lang="groovy" emphasize-lines="9"><![CDATA[
            pipeline {
                environment {
                    QODANA_TOKEN=credentials('qodana-token')
                }
                agent {
                    docker {
                        args '''
                          -v "${WORKSPACE}":/data/project
                          -e IDEA_PROPERTIES=intellij.opengrep.rules.downloaded.source.enabled=false  
                          --entrypoint=""
                          '''
                        image '%dotnet-image%'
                    }
                }
                stages {
                    stage('Qodana') {
                        steps {
                            sh '''qodana'''
                        }
                    }
                }
            }
        ]]>
</code-block>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
        <code-block lang="yaml" emphasize-lines="5"><![CDATA[
            include:
                - component: %gitlab-version%
                  inputs:
                      args: |
                          -e IDEA_PROPERTIES=intellij.opengrep.rules.downloaded.source.enabled=false
                          --linter %dotnet-linter%
        ]]>
</code-block>
    </tab>
    <tab title="TeamCity" group-key="teamcity">
        <p>In the runner configuration, find the <ui-path>Additional Docker arguments</ui-path> field and
            specify the property:</p>
        <code-block lang="shell"><![CDATA[
            -e IDEA_PROPERTIES=intellij.opengrep.rules.downloaded.source.enabled=false
        ]]>
</code-block>
    </tab>
</tabs>


##### Use your own rules

In addition to the bundled rules, you can apply your own rules by saving rule files to the `.qodana/opengrep` directory
of your project root.

## Qodana for .NET list of rules
{id="ta-dotnet-rules-list"}

The repository containing rules is available on the [GitHub website](https://github.com/qodana/opengrep-sast-rules).

### OWASP Top 2017 Coverage Matrix

| Category | C# | JavaScript | TypeScript |
| :--- | :---: | :---: | :---: |
| A1 Injection | ✓ | ✓ | ✓ |
| A2 Broken Authentication | ✓ | ✓ | - |
| A3 Sensitive Data Exposure | ✓ | ✓ | ✓ |
| A4 XML External Entities (XXE) | - | ✓ | - |
| A5 Broken Access Control | ✓ | ✓ | ✓ |
| A6 Security Misconfiguration | ✓ | ✓ | - |
| A7 Cross-Site Scripting (XSS) | ✓ | ✓ | ✓ |
| A8 Insecure Deserialization | ✓ | ✓ | ✓ |
| A9 Using Components with Known Vulnerabilities | - | ✓ | ✓ |
| A10 Insufficient Logging & Monitoring | - | - | - |

Information about these rules is available on the [OWASP website](https://owasp.org/www-project-top-ten/2017/).


### OWASP Top 2021 Coverage Matrix

| Category | csharp | javascript | typescript |
| :--- | :---: | :---: | :---: |
| A1 Broken Access Control | ✓ | ✓ | ✓ |
| A2 Cryptographic Failures | ✓ | ✓ | ✓ |
| A3 Injection | ✓ | ✓ | ✓ |
| A4 Insecure Design | ✓ | - | - |
| A5 Security Misconfiguration | ✓ | ✓ | - |
| A6 Vulnerable and Outdated Components | - | ✓ | ✓ |
| A7 Identification and Authentication Failures | ✓ | ✓ | - |
| A8 Software and Data Integrity Failures | ✓ | ✓ | ✓ |
| A9 Security Logging and Monitoring Failures | - | - | - |
| A10 Server Side Request Forgery (SSRF) | - | ✓ | ✓ |

Information about these rules is available on the [OWASP website](https://owasp.org/Top10/2021/).

<!--### OWASP Top 2025 Coverage Matrix

| Category | csharp | javascript | typescript |
| :--- | :---: | :---: | :---: |
| A1 Broken Access Control | ✓ | ✓ | ✓ |
| A2 Security Misconfiguration | - | - | - |
| A3 Software Supply Chain Failures | - | - | - |
| A4 Cryptographic Failures | - | - | - |
| A5 Injection | ✓ | ✓ | ✓ |
| A6 Insecure Design | ✓ | - | - |
| A7 Authentication Failures | - | - | - |
| A8 Software or Data Integrity Failures | - | - | - |
| A9 Security Logging and Alerting Failures | - | - | - |
| A10 Mishandling of Exceptional Conditions | - | - | - |

Information about these rules is available on the [OWASP website](https://owasp.org/Top10/2025/).

### CWE Top 25 (2025) Coverage Matrix

| # | CWE | Description | csharp | javascript | typescript |
| :--- | :--- | :--- | :---: | :---: | :---: |
| 1 | CWE-79 | Cross-site Scripting | ✓ | ✓ | ✓ |
| 2 | CWE-89 | SQL Injection | ✓ | ✓ | - |
| 3 | CWE-352 | Cross-Site Request Forgery (CSRF) | - | - | - |
| 4 | CWE-862 | Missing Authorization | - | - | - |
| 5 | CWE-787 | Out-of-bounds Write | - | ✓ | - |
| 6 | CWE-22 | Path Traversal | ✓ | ✓ | ✓ |
| 7 | CWE-416 | Use After Free | - | - | - |
| 8 | CWE-125 | Out-of-bounds Read | - | ✓ | - |
| 9 | CWE-78 | OS Command Injection | ✓ | ✓ | ✓ |
| 10 | CWE-94 | Code Injection | - | ✓ | ✓ |
| 11 | CWE-120 | Classic Buffer Overflow | - | - | - |
| 12 | CWE-434 | Unrestricted File Upload | - | - | - |
| 13 | CWE-476 | NULL Pointer Dereference | - | - | - |
| 14 | CWE-121 | Stack-based Buffer Overflow | - | - | - |
| 15 | CWE-502 | Deserialization of Untrusted Data | ✓ | ✓ | ✓ |
| 16 | CWE-122 | Heap-based Buffer Overflow | - | - | - |
| 17 | CWE-863 | Incorrect Authorization | - | - | - |
| 18 | CWE-20 | Improper Input Validation | - | - | - |
| 19 | CWE-284 | Improper Access Control | - | - | - |
| 20 | CWE-200 | Exposure of Sensitive Information | - | - | - |
| 21 | CWE-306 | Missing Authentication for Critical Function | - | - | - |
| 22 | CWE-918 | Server-Side Request Forgery (SSRF) | - | ✓ | ✓ |
| 23 | CWE-77 | Command Injection | - | - | - |
| 24 | CWE-639 | Authorization Bypass Through User-Controlled Key | - | - | - |
| 25 | CWE-770 | Allocation of Resources Without Limits or Throttling | - | ✓ | ✓ |

Information about these rules is available on the [CWE website](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25.html).

-->

<!--Use the `dfa.analysis.rml.max.traces.count=<number>` property for configuring 


| Configuration capability           | Action or setting                                                                   |
|------------------------------------|-------------------------------------------------------------------------------------|
| Set the number of traces           | Use the `--property=dfa.analysis.rml.max.traces.count=<number>` CLI property        |
| Disable all bundled Opengrep rules | Use the `IDEA_PROPERTIES="intellij.opengrep.rules.downloaded.source.enabled=false"` CLI property |
| Apply your own rules               | Save rule files to `.qodana/opengrep` of your project root                          |
-->

  <!--<p>Alternatively, you can use the <code>inspections</code> section of <code>qodana.yaml</code>:</p>

  <code-block lang="yaml">
  inspections:
    - inspection: JvmTaintAnalysis
      enabled: true
  </code-block>-->

  <!--<p>Alternatively, you can use the <code>inspections</code> section of <code>qodana.yaml</code>:</p>

  <code-block lang="yaml">
  inspections:
    - inspection: PhpVulnerablePathsInspection
      enabled: true
  </code-block>-->
