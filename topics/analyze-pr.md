# Incremental analysis

<link-summary>For all linters except %dotnet-co% and %clang%, you can run incremental analysis on a change set like 
merge or pull requests, as well as analyze changes between two commits.</link-summary> 

<var name="mrp" value="https://docs.gitlab.com/ee/ci/pipelines/merged_results_pipelines.html"/>

<note>This feature is not supported by the <a href="dotnet.md">%dotnet-co%</a> and <a href="clang.md">%clang%</a> linters.</note>

With %product%, you can analyze not only your entire codebase but also change sets — such as merge or pull 
requests — as well as changes between two commits.

Configuration samples on this page contain `<GIT_START_HASH>` and `<GIT_END_HASH>` to denote the 
hashes of the earliest and latest commits that should be included in a change analysis. For example:

```generic
 commit 7a3f9f8e6b3a487f7e8e7f8a7f8e (HEAD -> main) <--- GIT_END_HASH
| Author: Your Name <your.email@example.com>
| Date:   Mon Oct 3 12:34:56 2024 +0200
|
|     The latest commit
|
* commit 2b4c8d9e6a3b486f7e9e8f8b8f8
| Author: Your Name <your.email@example.com>
| Date:   Mon Oct 2 12:30:00 2024 +0200
|
|     The second commit
|
* commit 5d6e9f0e7b4c587f8e0e9f0a9f0               <--- GIT_START_HASH
| Author: Your Name <your.email@example.com>
| Date:   Mon Oct 1 12:25:00 2024 +0200
|
|     The earliest commit
```

The `QODANA_TOKEN` variable refers to a <a href="project-token.md">project token</a> value.   

## Analysis performance

During incremental analyses, %product% is executed two times using a limited analysis scope, which means that the [configuration 
stage](inspect-your-code.md) is also performed twice. 

If you analyze a relatively small codebases, reducing the analysis scope does not yield a 
significant performance boost, it can only provide minor performance improvements compared to regular analysis. The complexity of a 
project, frequent changes to a project structure, and numerous other factors can affect the time required for incremental analyses. 

## Analyze pull and merge requests

<link-summary>
You can use the --diff-start option to analyze changes between the current version of a codebase and a specific commit.
</link-summary>

<p>If you just finished work and would like to analyze the changes, you
    can employ the <code>--diff-start</code> option and specify a hash of the commit that will act as a base
    for comparison:</p>

<tabs group="cli-settings">
    <tab title="%product% CLI" group-key="qodana-cli">
    <p>To run <a href="https://github.com/JetBrains/qodana-cli">%product% CLI</a> in the default mode, you must have Docker or Podman installed and running locally.
     If you are using Linux, you should be able to run Docker under your current
     <a href="https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user">non-root user</a>. Use this command to run Qodana CLI:</p>
        <code-block lang="shell" prompt="$">
            qodana scan \
            &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
            &nbsp;&nbsp;&nbsp;--diff-start=&lt;GIT_START_HASH&gt;
        </code-block>
    </tab>
    <tab title="GitHub Actions" group-key="github-actions">
    <p>In GitHub Actions, the <code>--diff-start</code> can be omitted because it will be added automatically while running
%product%, so you can follow this procedure:</p>
    <procedure>
                <step>On the <ui-path>Settings</ui-path> tab of the GitHub UI, create the <code>QODANA_TOKEN</code>
                <a href="https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository">encrypted secret</a>
                and save the <a href="cloud-projects.topic" anchor="cloud-manage-projects">project token</a> as its value.
            </step>
            <step>On the <ui-path>Actions</ui-path> tab of the GitHub UI, set up a new workflow and create the
                <code>.github/workflows/code_quality.yml</code> file.</step>
            <step><p>Add this snippet to the <code>.github/workflows/code_quality.yml</code> file:</p>
        <code-block lang="yaml">
                name: Qodana
    on:
      workflow_dispatch:
      pull_request:
      push:
        branches: # Specify your branches here
          - main # The 'main' branch
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
            env:
              QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
        </code-block>
    </step>
    </procedure>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab-cicd">
        <p>Make sure that your project repository is accessible to GitLab CI/CD.</p>
        <p>In the root directory of your project, save the <code>.gitlab-ci.yml</code> file containing the following snippet:</p>
                <code-block lang="yaml">
                    include:
                       - component: %gitlab-version%    
                         inputs:
                            args: --image &lt;image&gt;
                </code-block>
        <p>This configuration, by default, enables merge request analysis. To override the default behavior, you
        can use the following configuration:</p>
        <code-block lang="yaml">
            include:
               - component: %gitlab-version%
                         inputs:
                            args: --image &lt;image&gt;
            &nbsp;
            qodana:
            &nbsp;&nbsp;rules:
            &nbsp;&nbsp;&nbsp;&nbsp;# GIT_DEPTH: 0 is required for checkout in case Qodana works in merge request mode
            &nbsp;&nbsp;&nbsp;&nbsp;# (reports issues that appeared only in that merge request)
            &nbsp;&nbsp;&nbsp;&nbsp;- if: $CI_PIPELINE_SOURCE == "merge_request_event" && $QODANA_MR_MODE == "true"
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;variables:
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;GIT_DEPTH: 0
            &nbsp;&nbsp;&nbsp;&nbsp;# run analysis in case of merge request
            &nbsp;&nbsp;&nbsp;&nbsp;- if: $CI_PIPELINE_SOURCE == "merge_request_event"
            &nbsp;&nbsp;&nbsp;&nbsp;# restrict branch analysis only to main/master and release branches
            &nbsp;&nbsp;&nbsp;&nbsp;- if: $CI_COMMIT_BRANCH =~ /^releases/ || $CI_COMMIT_BRANCH == "master" || $CI_COMMIT_BRANCH == "main"
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# mr-mode does not make any sense for branch analysis
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;variables:
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;QODANA_MR_MODE: false
        </code-block>
    </tab>
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$">
            docker run \
            &nbsp;&nbsp;&nbsp;-v $(pwd):/data/project/ \
            &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
            &nbsp;&nbsp;&nbsp;jetbrains/qodana-&lt;image&gt; \
            &nbsp;&nbsp;&nbsp;--diff-start=&lt;GIT_START_HASH&gt;
        </code-block>
    </tab>
</tabs>

## Analyze changes between two commits

<p>To analyze a set of changes between two commits, employ both <code>--diff-start</code>
and <code>--diff-end</code> options:</p>

<tabs group="cli-settings">
    <tab title="Qodana CLI" group-key="qodana-cli">
    <p>To run <a href="https://github.com/JetBrains/qodana-cli">Qodana CLI</a> in the default mode, you must have Docker or Podman installed and running locally.
     If you are using Linux, you should be able to run Docker under your current
     <a href="https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user">non-root user</a>. Use this command to run Qodana CLI:</p>
        <code-block lang="shell" prompt="$">
            qodana scan \
            &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
            &nbsp;&nbsp;&nbsp;--diff-start=&lt;GIT_START_HASH&gt; \
            &nbsp;&nbsp;&nbsp;--diff-end=&lt;GIT_END_HASH&gt;
        </code-block>
    </tab>
    <tab title="GitHub Actions" group-key="github-actions">
    <procedure>
                <step>On the <ui-path>Settings</ui-path> tab of the GitHub UI, create the <code>QODANA_TOKEN</code>
                <a href="https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository">encrypted secret</a>
                and save the <a href="cloud-projects.topic" anchor="cloud-manage-projects">project token</a> as its value.
            </step>
            <step>On the <ui-path>Actions</ui-path> tab of the GitHub UI, set up a new workflow and create the
                <code>.github/workflows/code_quality.yml</code> file.</step>
            <step><p>Add this snippet to the <code>.github/workflows/code_quality.yml</code> file:</p>
        <code-block lang="yaml">
                name: Qodana
    on:
      workflow_dispatch:
      pull_request:
      push:
        branches: # Specify your branches here
          - main # The 'main' branch
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
              args: --diff-start &lt;GIT_START_HASH&gt; --diff-end &lt;GIT_END_HASH&gt; 
            env:
              QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
        </code-block>
    </step>
    </procedure>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab-cicd">
<p>Make sure that your project repository is accessible to GitLab CI/CD.</p>
<p>In the root directory of your project, save the <code>.gitlab-ci.yml</code> file containing the following snippet:</p>
        <code-block lang="yaml">
        include:
           - component: %gitlab-version%
             inputs:
                args: --diff-start $CI_MERGE_REQUEST_TARGET_BRANCH_SHA --diff-end $CI_MERGE_REQUEST_SOURCE_BRANCH_SHA --image &lt;image&gt;
        </code-block>
    </tab>
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$">
            docker run \
            &nbsp;&nbsp;&nbsp;-v $(pwd):/data/project/ \
            &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
            &nbsp;&nbsp;&nbsp;jetbrains/qodana-&lt;image&gt; \
            &nbsp;&nbsp;&nbsp;--diff-start=&lt;GIT_START_HASH&gt; \
            &nbsp;&nbsp;&nbsp;--diff-end=&lt;GIT_END_HASH&gt;
        </code-block>
    </tab>
</tabs>
