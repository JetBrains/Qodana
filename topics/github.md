[//]: # (title: GitHub Actions)

<link-summary>The Qodana Scan GitHub action allows you to run Qodana in a GitHub repository.</link-summary>
<var name="pull-requests" value="https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#preventing-github-actions-from-creating-or-approving-pull-requests"/>
<var name="branch-protection-rule" value="https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/managing-a-branch-protection-rule"/>

<show-structure depth="3"/>

The [Qodana Scan GitHub action](https://github.com/marketplace/actions/qodana-scan) allows you to run Qodana in a GitHub repository.

## Prepare your project

### Qodana Cloud

<include from="lib_qd.topic" element-id="cicd-cloud-intro"/>

### Argument notation

<include from="lib_qd.topic" element-id="ci-cd-argument-notation-update"/>

### Basic configuration

<anchor name="basic-configuration"/>

<link-summary>In the GitHub UI, create an encrypted secret for a project token, and configure a workflow file.</link-summary>

<include from="lib_qd.topic" element-id="major-version-note"/>

> Information about native and container modes is available in the [](deploy-qodana.md) section.

<include from="lib_qd.topic" element-id="github-basic-configuration"/>

<note><code>fetch-depth: 0</code> is required for checkout in case Qodana works in pull request mode
(reports issues that appeared only in that pull request).</note> 

We recommend that you have a separate workflow file for Qodana
because [different jobs run in parallel](https://help.github.com/en/actions/getting-started-with-github-actions/core-concepts-for-github-actions#job)

## Quick-Fixes

<include from="lib_qd.topic" element-id="ci-cd-feature-availability-quick-fix"/>

To automatically fix issues found by %product% and push the changes to your repository, follow the procedure below.

<procedure>
   <step>
      <p>Choose the <a href="quick-fix.md">Quick-Fix strategy</a> using either of two configuration methods:</p> 
         <tabs>
            <tab title="qodana.yaml">
               <code-block lang="yaml">
                  # Possible values: apply | cleanup
                  fixesStrategy: apply               
               </code-block>
            </tab>
            <tab title="Workflow configuration">
               <code-block lang="yaml">
                  # Possible values: --apply-fixes | --cleanup
                  args: --apply-fixes
               </code-block>   
            </tab>
         </tabs>
   </step>
   <step>
      <p>Depending on your needs, configure the <code>push-fixes</code> option of your workflow configuration:</p>
      <tabs>
         <tab title="Pull request">
            <p>Save this configuration to create a new branch with fixes and a pull request to the original branch:</p>
            <code-block lang="yaml">
               push-fixes: pull-request
            </code-block>
            <p>Also, enable GitHub Actions to <a href="%pull-requests%">create and approve</a> pull requests.</p>
         </tab>
         <tab title="Original branch">
            <p>Save this configuration to push fixes to the original branch:</p>
            <code-block lang="yaml">
               push-fixes: branch
               pr-mode: false
            </code-block> 
         </tab>
      </tabs>
   </step>
   <step>
      <p>Set the correct permissions for the job, for example:</p>
      <code-block lang="yaml">
      permissions:
      &nbsp;&nbsp;contents: write
      &nbsp;&nbsp;pull-requests: write
      &nbsp;&nbsp;checks: write
      </code-block>
   </step>
</procedure>

This is an example configuration snippet containing all options:

<code-block lang="yaml">
    permissions:
      contents: write
      pull-requests: write
      checks: write
    steps:
      - name: 'Qodana Scan'
        uses: %action-version%
        with:
          args: --apply-fixes
          push-fixes: pull-request
        env:
          QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
</code-block>

> **Note**
> Qodana could automatically modify not only the code, but also the configuration in `.idea`: if you do not wish to push these changes, add `.idea` to your `.gitignore` file.

## GitHub code scanning

You can set
up [GitHub code scanning](https://docs.github.com/en/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/about-code-scanning)
for your project using Qodana. To do this, add these lines to the `code_quality.yml` workflow file right below
[the basic configuration](#Basic+configuration) of Qodana Scan:

```yaml
      - uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: ${{ runner.temp }}/qodana/results/qodana.sarif.json
```

This sample invokes the `codeql-action` for uploading a SARIF-formatted Qodana report to GitHub, and specifies the report
file using the `sarif_file` key.

> GitHub code scanning does not export analysis results to third-party tools, which means that you cannot use this 
> data for further processing by Qodana. In this case, you have to set up a baseline and quality gate processing on the 
> Qodana side before submitting analysis results to GitHub code scanning, see the [](#Baseline+and+quality+gate) section for details.

## Pull requests

> To learn more about pull request analysis, see the [](inspect-your-code.md#Incremental+analysis) chapter.

By default, analysis of pull requests is enabled in %product%, see the [`pr-mode`](#Configuration) option description for details.
To learn how to analyze code between two commits, see the [](analyze-pr.md#Analyze+changes+between+two+commits) chapter for details.

### Pull request quality gate

<link-summary>You can enforce GitHub to block merge of pull requests if a quality gate has failed.</link-summary>

You can configure GitHub to block the merging of pull requests if a quality gate has failed. 
To do this, create a [branch protection rule](%branch-protection-rule%) as described below:

<procedure>
   <step>
      <p>Create a new or open an existing GitHub workflow that invokes the Qodana Scan action.</p>
   </step>
   <step>
      <p>Set the workflow to run on <code>pull_request</code> events that target the <code>main</code> branch:</p>
      <code-block lang="yaml">
         on:
            pull_request:
              branches:
                - main
      </code-block>
      <p>Instead of <code>main</code>, you can specify your branch here.</p>
   </step>
   <step>
      <p>Set the number of problems (integer) for the Qodana action <code>fail-threshold</code> option.</p>
   </step>
   <step>
      <p>Under your repository name, click <ui-path>Settings</ui-path>.</p>
   </step>
   <step>
      <p>On the left menu, click <ui-path>Branches</ui-path>.</p>
   </step>
   <step>
      <p>In the branch protection rules section, click <ui-path>Add rule</ui-path>.</p>
   </step>
   <step>
      <p>Add <code>main</code> to <ui-path>Branch name pattern</ui-path>.</p>
   </step>
   <step>
      <p>Select <ui-path>Require status checks to pass before merging</ui-path>.</p>
   </step>
   <step>
      <p>Search for the <code>Qodana</code> status check, then check it.</p>
   </step>
   <step>
      <p>Click <ui-path>Create</ui-path>.</p>
   </step>
</procedure>

<anchor name="quality-gate-and-baseline"/>

## Baseline and quality gate

### Baseline

<link-summary>Learn how to configure the baseline feature on GitHub.</link-summary>

Follow these steps to establish a baseline for your project:

<procedure>
   <step>
      <p>Run Qodana <a href="Quick-start.topic">locally</a> on your project:</p>
      <code-block lang="shell">
      cd project
      qodana scan \
        -e QODANA_TOKEN="&lt;cloud-project-token&gt;"
      </code-block>
   </step>
   <step>
      <p>In %cloud%, <a href="ui-overview.md" anchor="ui-overview-baseline">add detected problems</a> to the baseline 
         and then download the <code>qodana.sarif.json</code> file.</p>
   </step>
   <step>
      <p>Upload the <code>qodana.sarif.json</code> file to your project root on GitHub.</p>
   </step>
   <step>
      <p>Append the <code>--baseline,qodana.sarif.json</code> argument to the Qodana Scan action configuration 
         <code>args</code> parameter in the  <code>code_quality.yml</code> file:</p>
      <code-block lang="yaml">
         - name: Qodana Scan
           uses: JetBrains/qodana-action@main
           with:
             args: --baseline qodana.sarif.json
      </code-block>
   </step>
</procedure>

To update your baseline, you need to repeat these steps once more.

From this point onward, GitHub will generate alerts only for problems that were not included in the baseline as new issues.

### Quality gate

<link-summary>Learn how to configure the quality gate feature on GitHub.</link-summary>

To establish a quality gate, in the workflow configuration specify the `--fail-threshold` option:

```yaml
- name: Qodana Scan
  uses: %action-version%
  with:
    args: --fail-threshold <number-of-accepted-problems>
  env:
    QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
```

### Combined configuration

<link-summary>You can combine the baseline and quality gate features to manage your technical debt, report only new 
problems, and block pull requests that contain too many problems.</link-summary>

You can combine the [baseline](baseline.topic) and [quality gate](quality-gate.topic) features to manage your
technical debt, report only new problems, and block pull requests that contain too many problems.
Using this configuration, you will be able to detect only new problems in pull requests that fall beyond the baseline. 

```yaml
- name: Qodana Scan
  uses: %action-version%
  with:
    args: --baseline qodana.sarif.json --fail-threshold <number-of-accepted-problems>
  env:
    QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
```

At the same time, pull requests with **new** problems exceeding the `--fail-threshold` limit will be blocked, and the 
workflow will fail.

## Analyze a specific solution

<link-summary>Learn how to analyze your .NET projects using a specific solution.</link-summary>

To analyze your [.NET project](dotnet.md) using a [specific solution](dotnet.md#Analyze+a+specific+solution), specify the 
path to the solution file relative to the project root, for example:

```yaml
- name: Qodana Scan
  uses: %action-version%
  with:
    args: --solution "src/path_to_your.sln"
  env:
    QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
```

## Get a Qodana badge

<link-summary>You can set up a Qodana workflow badge in your repository.</link-summary>

You can set up a Qodana workflow badge in your repository, to do it, follow these steps:

<procedure>
    <step>Navigate to the workflow run that you previously configured.</step>
    <step>
        <p>On the workflow page, select <ui-path>Create status badge</ui-path>.</p>
        <img src="https://user-images.githubusercontent.com/13538286/148529278-5d585f1d-adc4-4b22-9a20-769901566924.png" alt="Creating status badge" width="706"/>
    </step>
    <step>
        <p>Copy the Markdown text to your repository README file.</p>
    </step>
</procedure>

## Qodana logs

In the `.github/workflows/code_quality.yml` file, set `upload-result` to `true`:

```yaml
- name: 'Qodana Scan'
  uses: %action-version%
  env:
    QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
  with:
    upload-result: true
```

Run %product% using this configuration to produce a `qodana-report` artifact. Navigate to the `log` directory to see logs.

## Configuration

<link-summary>The full list of action parameters.</link-summary>

Most likely, you won't need other options than `args`: all other options can be helpful if you are configuring multiple Qodana Scan jobs in one workflow.

Use [`with`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstepswith) to define any action parameters:

```yaml
with:
  args: --baseline qodana.sarif.json
  cache-default-branch-only: true
```

| Name                        | Description                                                                                                                                                                                                                       | Default Value                                       |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| `args`                      | Additional [Qodana CLI `scan` command](https://github.com/jetbrains/qodana-cli#scan) arguments, split the arguments with commas (`,`), for example `-i,frontend,--print-problems`. Optional.                                      | -                                                   |
| `results-dir`               | Directory to store the analysis results. Optional.                                                                                                                                                                                | `${{ runner.temp }}/qodana/results`                 |
| `upload-result`             | Upload Qodana results (SARIF, other artifacts, logs) as an artifact to the job. Optional.                                                                                                                                         | `false`                                             |
| `artifact-name`             | Specify Qodana results artifact name, used for results uploading. Optional.                                                                                                                                                       | `qodana-report`                                     |
| `cache-dir`                 | Directory to store Qodana cache. Optional.                                                                                                                                                                                        | `${{ runner.temp }}/qodana/caches`                  |
| `use-caches`                | Utilize [GitHub caches](https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows#usage-limits-and-eviction-policy) for Qodana runs. Optional.                                                | `true`                                              |
| `primary-cache-key`         | Set [the primary cache key](https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows#matching-a-cache-key). If not found, cache from `additional-cache-key` will be used instead.  Optional. | `qodana-2025.2-${{ github.ref }}-${{ github.sha }}` | 
| `additional-cache-key`      | Set [the additional cache key](https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows#matching-a-cache-key). Optional.                                                                     | `qodana-2025.2-${{ github.ref }}`                   |
| `cache-default-branch-only` | Upload cache for the default branch only. Optional.                                                                                                                                                                               | `false`                                             |
| `use-annotations`           | Use annotation to mark the results in the GitHub user interface. Optional.                                                                                                                                                        | `true`                                              |
| `pr-mode`                   | Analyze ONLY changed files in a pull request. Optional.                                                                                                                                                                           | `true`                                              |
| `post-pr-comment`           | Post a comment with the Qodana results summary to the pull request. Optional.                                                                                                                                                     | `true`                                              |
| `github-token`              | GitHub token to access the repository: post annotations, comments. Optional.                                                                                                                                                      | `${{ github.token }}`                               |
| `push-fixes`                | Push Qodana fixes to the repository, can be `none`, `branch` to the current branch, or `pull-request`. Optional.                                                                                                                  | `none`                                              |

