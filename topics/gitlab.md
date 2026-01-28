[//]: # (title: GitLab CI/CD)

<show-structure for="chapter" depth="3"/>

<var name="GitLabLink" value="https://docs.gitlab.com/ee/ci/variables/"/>
<var name="GitLabPredefined" value="https://docs.gitlab.com/ee/ci/variables/predefined_variables.html#predefined-variables-reference"/>
<var name="GitLabExpose" value="https://docs.gitlab.com/ee/ci/yaml/#artifactsexpose_as"/>
<var name="GitLabComponent" value="https://docs.gitlab.com/ci/components/"/>
<var name="ComponentInvocation" value="https://docs.gitlab.com/ci/components/#use-a-component"/>
<var name="MirrorComponent" value="https://docs.gitlab.com/ci/components/#use-a-gitlabcom-component-on-gitlab-self-managed"/>
<var name="Variables" value="https://docs.gitlab.com/ci/variables/#define-a-cicd-variable-in-the-ui"/>
<var name="PersonalToken" value="https://docs.gitlab.com/user/profile/personal_access_tokens/"/>
<var name="ProjectToken" value="https://docs.gitlab.com/user/project/settings/project_access_tokens/"/>
<var name="OnPrem" value="https://gitlab.com/qodana/qodana/-/blob/v2025.2/templates/qodana-gitlab-ci.yml?ref_type=heads"/>

<link-summary>You can run the %instance% Scan GitLab Pipeline.</link-summary>

[GitLab CI/CD](https://docs.gitlab.com/ee/ci/) is a tool for software development that uses various CI/CD methodologies. This 
section explains how you can run the %instance% Scan GitLab Pipeline [component](%GitLabComponent%).

## Before you start

### %cloud%

<include from="lib_qd.topic" element-id="cicd-cloud-intro"/>

<!--### Native mode on Linux

To run %product% in [native mode](deploy-qodana.md#deploy-qodana-native-mode) on Linux, prepare your own Docker image 
containing Linux with pre-installed Node.js, Git, Bash, cURL and Java. -->

### Prepare your project

<link-summary>Make sure that your project repository is accessible to GitLab CI/CD, and in the root directory of your 
project save the pipeline configuration file.</link-summary>

Make sure that your project repository is accessible to GitLab CI/CD.

In GitLab CI/CD UI, create the following environment variables: 

<table>
   <tr>
      <td>
       Variable name
      </td>
      <td>
       Description  
      </td>
   </tr>
   <tr>
      <td>
       <code>QODANA_TOKEN</code>  
      </td>
      <td>
       <p>Generated <a href="project-token.md">project token</a>. Save it in the GitLab CI/CD UI as described on the <a href="%Variables%">GitLab CI/CD website</a>.
          Also, make sure that the variable is not marked as protected and the <ui-path>Expand variable reference</ui-path> flag is enabled.
       </p>  
      </td>
   </tr>
   <tr>
      <td>
       <code>QODANA_GITLAB_TOKEN</code>  
      </td>
      <td>
       <p>A <a href="%PersonalToken%">personal access token</a> or a <a href="%ProjectToken%">project access token</a> 
         required for <a anchor="Quick-Fixes">Quick-Fixes</a> and 
         <a anchor="Configuration">summary reports</a> as comments in merge requests. The holder of a personal access 
         token will be shown as an author for all %product% actions, so it is advised to use a project access token.</p>
       <p>For Quick-Fixes, enable the <code>api</code> and <code>write_repository</code> permissions while configuring
         access tokens.</p>
      </td>
   </tr>
</table>

In the root directory of your project, save the `.gitlab-ci.yml` file. This file will contain a pipeline configuration 
that will be used by GitLab CI/CD. 

## Basic configuration

<link-summary>This section shows the basic GitLab CI/CD configuration for running %product%.</link-summary>

<include from="lib_qd.topic" element-id="major-version-note"/>

For the cloud-based version of GitLab CI/CD, in the `.gitlab-ci.yml` file save the following configuration to [include](%ComponentInvocation%) the 
%product% Scan GitLab Pipeline component:

```yaml
include:
   - component: %gitlab-version%
     inputs:
        args: --image,<image>
```

This configuration already enables [caches](#Configure+cache),
[Code Quality report](#gitlab-generate-code-quality-reports) generation, [merge request](#Specific+branches) analysis,
and comments to merge requests. You can override these settings using descriptions from the sections below and the
[](#Configuration) chapter. The `--image` argument specifies a %product% [image](docker-image-configuration.topic#docker-config-reference-qodana-scan-image) that you would like to employ.

The included component creates the `qodana` job that can be configured as any other job in GitLab CI/CD. 
You can view the predefined configuration of this job using our [template](https://gitlab.com/qodana/qodana/-/blob/main/templates/qodana-gitlab-ci.yml).

For example, this code snippet lets you change the image used for running the `qodana` job, define `before_script`, 
change job execution rules, and add an environmental variable.

```yaml
include:
  - component: %gitlab-version%

some-task:
  stage: test
  script:
    - echo "I am complete!"
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"

qodana:
  image: docker:28.3.2
  services:
    - docker:28.3.2-dind
  before_script:
    - echo "Qodana job starts..."
  needs:
    - some-task
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
  variables:
    MAVEN_OPTS: "-Dmaven.repo.local=.m2/repository"
```

For the on-premise version of GitLab CI/CD, in the `.gitlab-ci.yml` file save the following configuration:

```yaml
include:
   - component: $CI_SERVER_FQDN/<org>/<repo>/qodana-gitlab-ci@v%version-current%
     inputs:
        args: --image,<image>
```

In this snippet, `qodana-gitlab-ci` is the GitLab CI/CD component described on the [GitLab CI/CD website](%OnPrem%). 

> Before running %product% using the on-premises version of GitLab CI/CD, you need to [mirror the component](%MirrorComponent%).
{style="note"}

### Configure cache

By default, caching is enabled in %product% with the following keys: 

```yaml
      - key: qodana-2025.1-$CI_DEFAULT_BRANCH-$CI_COMMIT_REF_SLUG
        fallback_keys:
           - qodana-2025.1-$CI_DEFAULT_BRANCH-
           - qodana-2025.1-
```

If you wish to override the default cache settings, use this configuration: 

```yaml
include:
   - component: %gitlab-version%
     inputs:
        args: --image,<image>

qodana:
   cache:
      - key: qodana-2025.1-$CI_DEFAULT_BRANCH-$CI_COMMIT_REF_SLUG
        fallback_keys:
           - qodana-2025.1-$CI_DEFAULT_BRANCH-
           - qodana-2025.1-
        paths:
           - $[[ inputs.cache-dir ]]

```

### Override an operating system

> Description of each script is available on the [GitLab CI/CD website](https://gitlab.com/qodana/qodana/-/blob/main/templates/qodana-gitlab-ci.yml).
{style="tip"}


By default, %product% is configured for Linux. You can override an operating system using the `os` keyword. For example,
you can use the following configuration for Microsoft Windows:

```yaml
include:
   - component: %gitlab-version%
     inputs:
        os: windows
        args: --image,<image>
```

<!-- ### Run %product% on Linux in native mode

To run %product% in [native mode on Linux](#Native+mode+on+Linux), use the following configuration that uses your custom
Docker image containing Linux:

```yaml
include:
  - component: %gitlab-version%
    inputs:
      args: --image,<image>,--within-docker,false

qodana:
  image: <your-custom-docker-image-with-linux>
```

Here, the [`--linter`](docker-image-configuration.topic#docker-config-reference-qodana-scan-linter) option specifies 
the %product% linter that you would like to employ. 
The [`--within-docker`](docker-image-configuration.topic#docker-config-reference-qodana-scan-within-docker) enables native mode.
-->

## Specific branches

<link-summary>This section explains how you can tell %instance% what branches of your project to inspect.</link-summary>

By default, %product% is configured for analyzing the `master` and `main` branches, release branches and merge requests meaning
that you do not have to provide any additional configurations and use the [basic configuration](#Basic+configuration).

If you wish to override this behavior, you can modify the following configuration:

```yaml
include:
   - component: %gitlab-version%
     inputs:
        args: --image,<image>

qodana:
  rules:
     # GIT_DEPTH: 0 is required for checkout in case Qodana works in merge request mode 
     # (reports issues that appeared only in that merge request)
     - if: $CI_PIPELINE_SOURCE == "merge_request_event" && $QODANA_MR_MODE == "true"
       variables:
          GIT_DEPTH: 0
     # run analysis in case of merge request
     - if: $CI_PIPELINE_SOURCE == "merge_request_event"
     # restrict branch analysis only to main/master and release branches
     - if: $CI_COMMIT_BRANCH =~ /^releases/ || $CI_COMMIT_BRANCH == "master" || $CI_COMMIT_BRANCH == "main"
        # mr-mode does not make any sense for branch analysis
       variables:
          QODANA_MR_MODE: false

```

The `rules` block of this configuration tells %product% what branches to inspect.


## Quick-Fixes

<include from="lib_qd.topic" element-id="ci-cd-feature-availability-quick-fix"/>

<!-- Should the third step be reflected in the configuration? Needs to be checked -->

> Make sure that you have configured the [`QODANA_GITLAB_TOKEN`](#Prepare+your+project) variable.  
{style="note"}

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
            <tab title="Pipeline configuration">
               <code-block lang="yaml">
                  # Possible values: --apply-fixes | --cleanup
                  args: --apply-fixes
               </code-block>   
            </tab>
         </tabs>
   </step>
   <step>
      <p>Depending on your needs, in the pipeline configuration define the <code>push-fixes</code> property:</p>
      <tabs>
         <tab title="Merge request">
            <p>Save this configuration to create a new branch with fixes and a merge request to the original branch:</p>
            <code-block lang="yaml">
               push-fixes: merge-request
            </code-block>
         </tab>
         <tab title="Original branch">
            <p>Save this configuration to push fixes to the original branch:</p>
            <code-block lang="yaml">
               push-fixes: branch
            </code-block> 
         </tab>
      </tabs>
   </step>
</procedure>

Here is an example configuration that uses the `inputs` block for configuring the pipeline:

```yaml
include:
   - component: %gitlab-version%
     inputs:
        push-fixes: merge-request
        args: |
            --apply-fixes,
          --image,<image>
```

> Qodana could automatically modify not only the code, but also the configuration in 
> the `.idea` directory: if you do not wish to push these changes, add `.idea` to your `.gitignore` file.
{style="note"}


## Expose Qodana reports

<link-summary>To make a report available in any given merge request without using %cloud%, you can change the path 
to the artifacts.</link-summary>

To make a report available in any given merge request without using %cloud%,
you can use the `upload-result` keyword and specify the artifact name using the 
`artifact-name` keyword, for example:

```yaml
include:
   - component: %gitlab-version%
     inputs:
        upload-result: true
        artifact-name: Qodana report
        args: --image,<image>
```

Assuming that you have configured your pipeline similarly, this is what it may look like:

1. Qodana report affiliated with a pipeline in a merge request

   <img src="gitlab-exposed-artifacts.png" alt="Qodana report affiliated with a pipeline in a merge request" width="706" border-effect="line"/>

2. Available actions for a given exposed Qodana artifact
   
   <img src="gitlab-exposed-artifacts-expanded.png" alt="Available actions for a given exposed Qodana artifact" width="706" border-effect="line"/>

## Quality gate and baseline

<link-summary>You can use the --fail-threshold number and --baseline path/to/qodana.sarif.json lines in the script block 
to invoke the quality gate and baseline features.</link-summary>

You can employ the `--fail-threshold <number>` and `--baseline <path/to/qodana.sarif.json>` lines in the `inputs:args` 
block to run the [quality gate](quality-gate.topic) and [baseline](baseline.topic) features.

```yaml
include:
   - component: %gitlab-version%
     inputs:
        args: |
            --baseline,qodana.sarif.json,
            --fail-threshold,<number-of-accepted-problems>,
            --image,<image>
```

## Code Quality reports
{id="gitlab-generate-code-quality-reports"}

<link-summary>By default, %product% lets you use the merge request UI of GitLab CI/CD to view specific lines of code 
that contain problems along with their description and recommendations for improvement.</link-summary>

Starting from version 2024.1 of %product%, you can use the merge request UI of GitLab CI/CD to view specific lines of 
code that contain problems along with their description and recommendations for improvement. 

To implement this feature, %product% generates JSON-formatted analysis reports supported by 
[Code Quality](https://docs.gitlab.com/ee/ci/testing/code_quality.html) and contained in the `gl-code-quality-report.json` file. 

By default, this feature is configured to `true`, so you do not need to make any additional settings. If necessary, 
you can override a path to reports using the `codequality` option: 

```yaml
include:
   - component: %gitlab-version%
     inputs:
        args: --image,<image>

qodana:
   artifacts:
      reports:
         codequality: $QODANA_RESULTS_DIR/gl-code-quality-report.json


```

## %product% logs

Use the following configuration to get log data from %product% on GitLab CI/CD:

```yaml
include:
   - component: %gitlab-version%
     inputs:
        args: --image,<image>
        upload-result: true
        results-dir: $CI_PROJECT_DIR/.qodana/results

qodana:
   artifacts:
      paths:
         - .qodana/results/
      expose_as: 'Qodana report'


```
This configuration uses the `.qodana/results` directory for generating logs and then exposes this directory as an artifact.

To upload logs from a Qodana job that fails with a timeout, add the `RUNNER_SCRIPT_TIMEOUT` variable with a value less 
than a pipeline timeout:

```yaml
include:
   - component: %gitlab-version%
     inputs:
        args: --image,<image>
        upload-result: true
        results-dir: $CI_PROJECT_DIR/.qodana/results

qodana:
   timeout: <specify timeout>
   variables:
      RUNNER_SCRIPT_TIMEOUT: <specified timeout value minus 5 minutes>
   artifacts:
      paths:
         - .qodana/results/
      expose_as: 'Qodana report'


```

The details are available on the [GitLab CI/CD website](https://gitlab.com/gitlab-org/gitlab/-/issues/284186).

## Configuration

> The description of all configuration options is available in our [repository](https://gitlab.com/qodana/qodana/-/blob/main/templates/qodana-gitlab-ci.yml).
{style="tip"}

This table contains the list of options that can be configured using the `inputs` block:

| Name                                           | Description                                                                                                                                                                                 | Default Value                     |
|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| `stage`                                        | CI stage for %product% execution                                                                                                                                                            | `test`                            |
| `job-name`                                     | A %product% job name. Could be used to customize the order of running several %product% jobs within the same pipeline                                                                       | `qodana`                          |
| `args`                                         | Additional [Qodana CLI `scan` command](https://github.com/jetbrains/qodana-cli#scan) arguments, split the arguments with commas (`,`), for example `-i,frontend,--print-problems`. Optional. | -                                 |
| `results-dir`                                  | Directory to store the analysis results relative to the project root. Optional.                                                                                                             | `$CI_PROJECT_DIR/.qodana/results` |
| `upload-result`                                | Upload Qodana results (SARIF, other artifacts, logs) as an artifact to the job. Optional.                                                                                                   | `false`                           |
| `artifact-name`                                | Specify Qodana results artifact name, used for result uploading. Optional.                                                                                                                  | `Qodana report`                   |
| `cache-dir`                                    | Directory to store Qodana cache relative to the project root. Optional.                                                                                                                     | `$CI_PROJECT_DIR/.qodana/caches`  |
| `use-caches`                                   | Utilize [GitHub caches](https://docs.gitlab.com/ci/caching/) for Qodana runs. Optional.                                                                                                     | `true`                            |
| `code-quality-report`                          | Use [Code Quality report](https://docs.gitlab.com/ci/testing/code_quality/) produced by Qodana                                                                                              | `true`                            |
| `mr-mode`                                      | Analyze ONLY changed files in a merge request. Optional.                                                                                                                                    | `true`                            |
| `post-mr-comment` {id="gitlab-summary-report"} | Post a comment with a Qodana results summary to a merge request. Optional.                                                                                                                  | `true`                            |
| `push-fixes`                                   | Push Qodana fixes to the repository, can be `none`, `branch` to the current branch, or `merge-request`. Optional.                                                          | `none`                            |
| `commit-message`                               | Commit message used when Quick-Fixes are applied                                                                                                                                            | `Apply quick-fixes by Qodana`     | 
| `os`                                           | Operating system used for running pipelines, required for pre-configuration. Could accept the `linux`, `windows` or `mac` values                                                            | `linux`                           |


<seealso>
    <category ref="external">
        <a href="https://rpadovani.com/gitlab-jetbrains-qodana">'Integrating JetBrains Qodana with GitLab
            pipelines' by Riccardo Padovani
        </a>
        <a href="https://blog.griefed.de/2022/04/30/qodana-and-gitlab/">'Qodana, GitLab and Discord'
            by Griefed
        </a>
    </category>
</seealso>
