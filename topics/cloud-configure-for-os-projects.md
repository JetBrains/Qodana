[//]: # (title: Analyze open-source projects)

<show-structure for="chapter" depth="3"/>

<var name="feature" value="License audit"/>
<var name="github-secret" value="https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository"/>
<var name="branch-protection-rule" value="https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/managing-a-branch-protection-rule"/>
<!-- I need to mention here more about OS projects -->

This section explains how you can analyze open-source projects using %instance% and covers the following use cases: 

* Configuring %instance% and its features
* Analyzing code locally or using CI/CD pipelines
* Forwarding analysis reports to %cloud% and viewing them there

The %product% products licensed under the Community [license](pricing.md) are free of charge and are well-suited for open-source projects.

> To get started with %product%, refer to the [Quick-start](Quick-start.topic) section.

## Before you start

### Available linters and features
{id="available-linters-and-features"}

The following %product% linters and their features are available with the Community license: 

<table>
    <tr>
        <td>Programming languages and features</td>
        <td>Description</td>
    </tr>
    <tr>
        <td>Java, Kotlin, Groovy</td>
        <td>The <code>%jvm-co-linter%</code> and <code>%jvm-co-a-linter%</code> <a href="jvm.md">linters</a></td>
    </tr>
    <tr>
        <td>C#, C/C++, VB.NET</td>
        <td>The <code>%dotnet-co-linter%</code> <a href="dotnet.md">linter</a></td>
    </tr>
    <tr>
        <td>C and C++</td>
        <td>The <code>%clang-linter%</code> <a href="clang.md">linter</a></td>
    </tr>
    <tr>
        <td>Python</td>
        <td>The <code>%python-co-linter%</code> <a href="python.md">linter</a></td>
    </tr>
    <tr>
        <td>Static analysis of code</td>
        <td>Analyze an entire codebase or its incremental changes</td>
    </tr>
    <tr>
        <td>Baseline</td>
        <td>Compare code against its snapshot to track various problems</td>
    </tr>
    <tr>
        <td>Quality gate</td>
        <td><p>Set thresholds to terminate %product% locally and in CI/CD pipelines.</p> 
            <p>This can be set up for a number of problems and their severities.</p>
        </td>
    </tr>
</table>

To run %product% locally, make sure that you have already deployed %product% CLI on your machine.

Use linter names from the table above to replace the `<linter>` placeholders in configuration snippets later provided in this section.

### Prepare %cloud%

<link-summary>Learn how to prepare %cloud% before inspecting your open-source project using %product%.</link-summary>

<procedure>
<step>
In the %cloud% UI, navigate to your organization.

<img src="qc-settings-organization-navigate-between.gif" width="706" alt="Creating an organization" border-effect="line"/>
</step>
<step>
    <p>On the organization page, click <ui-path>Create team</ui-path>.</p>
    <img src="qc-create-team.png" dark-src="qc-create-team_dark.png" alt="Create a team" width="706" border-effect="line"/>
    <p>This will open the <ui-path>Create team</ui-path> dialog.</p>
</step>
<step>
    <p>On the <ui-path>New team</ui-path> dialog, specify the team name, its visibility and then click <ui-path>Create</ui-path>.</p>
    <img src="qc-creating-team.png" dark-src="qc-creating-team_dark.png" alt="The New team dialog" width="706" border-effect="line"/>
</step>
<step>
        <p>On a <a href="cloud-teams.topic">team</a> page, click the <ui-path>Create project</ui-path> button.</p>
        <img src="qc-create-project.png" dark-src="qc-create-project_dark.png" width="706" alt="Creating a new project" border-effect="line"/>
</step>
<step>
In the project, click <ui-path>Generate token</ui-path> to generate a project token.

<img src="qc-generate-token.png" dark-src="qc-generate-token_dark.png" alt="Generate the project token" width="706" border-effect="line"/>
</step>
</procedure>

The generated [project token](project-token.md) will be used in the configuration snippets as the value for the `QODANA_TOKEN` variable.

## Analyze your projects

### Inspection profiles
{id="inspection-profiles"}

<link-summary>By default, %instance% analyzes your code using the `qodana.starter` profile. You can use additional 
inspections by specifying the `qodana.recommended` profile.</link-summary>

> This setting is not supported by the `%clang-linter%` linter. The details are available in the 
> [](clang.md#Adjusting+the+scope+of+analysis) chapter of the linter documentation.
> {style="note"}

By default, %instance% analyzes your code using the `qodana.starter` profile. You can use additional inspections by 
specifying the `qodana.recommended` profile. To do it, save this configuration to the `qodana.yaml` file contained in 
your project root:

<code-block lang="yaml">
    version: 1.0
    &nbsp;
    profile:
      name: qodana.recommended
    &nbsp;
    linter: &lt;linter&gt;
</code-block>

Alternatively, you can make the same configuration directly in the application configuration:

<tabs group="os-projects-snippets">
    <tab title="Qodana CLI" group-key="cli">
        <code-block lang="bash" prompt="$">
            qodana scan \
                -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                --profile-name qodana.recommended \
                --linter &lt;linter&gt;
</code-block>
    </tab>
    <tab title="GitHub Actions" group-key="github-actions">
        <code-block lang="yaml"><![CDATA[
            name: Qodana
            on:
              workflow_dispatch:
              pull_request:
                branches:
                  - main
              push:
                branches:
                  - main
                  - 'releases/*'
              jobs:
                qodana:
                  runs-on: ubuntu-latest
                  steps:
                    - uses: actions/checkout@v3
                      with:
                        fetch-depth: 0
                    - name: 'Qodana Scan'
                      uses: %action-version%
                      with:
                        args: |
                          --profile-name qodana.recommended
                          --linter <linter>
                      env:
                        QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
]]>
</code-block>
    </tab>
</tabs>

> Configuration examples for other CI/CD tools are provided in the [](ci.md) section.

> Information about inspection profiles is available in the [](inspection-profiles.md#inspection-profiles-existing-profiles) section.

To analyze the overall configuration of your project, employ the `qodana.sanity` profile instead.

### Incremental analysis
{id="incremental-analysis"}

Regular analyses are enabled by default and are performed on an entire project. Incremental analyses can be carried out as described below: 

| Incremental analysis                                     | Description                 |
|----------------------------------------------------------|-----------------------------|
| The `--diff-start` option                    | Pull or merge requests      |
| The `--diff-start` and `--diff-end` options | Changes between two commits |

To analyze pull requests, use the `--diff-start` option, for example: 

```bash
qodana scan \
   -e QODANA_TOKEN="<cloud-project-token>" \
   --diff-start=<GIT_START_HASH> \
   --linter <linter>
```
{prompt="$"}

The pull request mode is enabled by default in GitHub Actions, so it does not require any additional configuration.

Here are the configuration samples for analyzing changes between two commits:

<tabs group="os-projects-snippets">
    <tab title="Qodana CLI" group-key="cli">
        <code-block lang="bash" prompt="$"><![CDATA[
            qodana scan \
                -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                --diff-start=<GIT_START_HASH> \
                --diff-end=<GIT_END_HASH> \
                --linter &lt;linter&gt;
]]>
</code-block>
    </tab>
    <tab title="GitHub Actions" group-key="github-actions">
        <code-block lang="yaml"><![CDATA[
            name: Qodana
            on:
              workflow_dispatch:
              pull_request:
                branches:
                  - main
              push:
                branches:
                  - main
                  - 'releases/*'
              jobs:
                qodana:
                  runs-on: ubuntu-latest
                  steps:
                    - uses: actions/checkout@v3
                      with:
                        fetch-depth: 0
                    - name: 'Qodana Scan'
                      uses: %action-version%
                      with:
                        args: |
                          --diff-start <GIT_START_HASH>
                          --diff-end <GIT_END_HASH>
                          --linter <linter>
                      env:
                        QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
]]>
</code-block>
    </tab>
</tabs>

Information about incremental analysis is available in the [](analyze-pr.md) section.

### Baseline and quality gate
{id="baseline-quality-gate"}

<link-summary>A baseline lets you create a snapshot of your project that will be used as a basis for subsequent 
analysis. A quality gate lets you configure the ultimate number of problems that will cause a CI/CD pipeline failure.</link-summary>

[Baseline](baseline.topic) and [quality gates](quality-gate.topic) are configured using the following options:

<table>
  <tr>
    <td>Feature</td>
    <td>Configured via</td>
  </tr>
  <tr>
    <td>Baseline</td>
    <td><code>--baseline &lt;path-to-qodana.sarif.json&gt;</code></td>
  </tr>
  <tr>
    <td>Absolute number of problems</td>
    <td><code>fail-threshold &lt;number&gt;</code></td>
  </tr>
  <tr>
    <td>Severity thresholds</td>
    <td>
    <code-block lang="yaml"><![CDATA[
    failureConditions:
      severityThresholds:
        any: <number> # Total problems
        critical: <number> # Severities
        high: <number>
        moderate: <number>
        low: <number>
        info: <number>
        ]]>
</code-block>
</td>
  </tr>
</table>

<note><p>Severity thresholds are supported only by the following linters:</p>
    <ul>
        <li><code>qodana-jvm-community</code></li>
        <li><code>qodana-jvm-android</code></li>
        <li><code>qodana-python-community</code></li>
    </ul>
</note>

Use these snippets to configure a baseline and a quality gate for a total number of problems:

<tabs group="os-projects-snippets">
    <tab title="Qodana CLI" group-key="cli">
        <code-block lang="bash" prompt="$"><![CDATA[
            qodana scan \
                -e QODANA_TOKEN="<cloud-project-token>" \
                --baseline <path-to-qodana.sarif.json> \
                --fail-threshold <number> \
                --linter <linter>
]]>
</code-block>
    </tab>
    <tab title="GitHub Actions" group-key="github-actions">
        <code-block lang="yaml"><![CDATA[
            name: Qodana
            on:
              workflow_dispatch:
              pull_request:
                branches:
                  - main
              push:
                branches:
                  - main
                  - 'releases/*'
              jobs:
                qodana:
                  runs-on: ubuntu-latest
                  steps:
                    - uses: actions/checkout@v3
                      with:
                        fetch-depth: 0
                    - name: 'Qodana Scan'
                      uses: %action-version%
                      with:
                        args: |
                          --baseline <path-to-qodana.sarif.json>
                          --fail-threshold <number>
                          --linter <linter>
                      env:
                        QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
]]>
</code-block>
    </tab>
</tabs>

> When running in the baseline mode, a threshold is calculated as the sum of new and absent problems. Unchanged results are ignored.
{style="note"}


You can also configure the absolute number of problems using the `fail-threshold` option saved in the `qodana.yaml` file 
contained in your project root:

```yaml
    version: 1.0
    
    fail-threshold: <number>
    linter: <linter>
```

Once configured in the `qodana.yaml` file, this does not have to be set up in the application configuration.

Severity thresholds are configurable only via the `qodana.yaml` file. 

## View analysis reports

<link-summary>After your project is analyzed and the report is uploaded to %cloud%, you can view it.</link-summary>

<include from="cloud-overview-reports.topic" element-id="cloud-overview-reports-general"/>


<!--After your project is analyzed and the report is uploaded to %cloud%, you can view it as described in the 
[](cloud-overview-reports.topic) section. -->