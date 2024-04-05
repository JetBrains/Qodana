# Analyze changes

<link-summary>For all linter except Qodana Community for .NET, you can run incremental analysis on a change set like 
merge or pull requests, as well as inspect changes between two commits.</link-summary> 

<note>This feature is not supported by the <a href="qodana-dotnet-community.md"/> linter.</note>

Using %product%, you can not only scan your entire codebase, but also run analysis on change sets like merge or pull 
requests, as well as inspect changes between two commits.

## Analyze pull and merge requests

<link-summary>
You can use the --diff-start option to inspect changes between the current version of a codebase and a specific commit.
</link-summary>

<p>If you just finished work and would like to analyze the changes, you
    can employ the <code>--diff-start</code> option and specify a hash of the commit that will act as a base
    for comparison:</p>

<tabs group="cli-settings">
    <tab title="Qodana CLI" group-key="qodana-cli">
    <p>To run <a href="https://github.com/JetBrains/qodana-cli">Qodana CLI</a> in the default mode, you must have Docker or Podman installed and running locally.
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
            uses: JetBrains/qodana-action@v2024.1
            env:
              QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
        </code-block>
    </step>
    </procedure>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab-cicd">
<p>Make sure that your project repository is accessible by GitLab CI/CD.</p>
<p>In the root directory of your project, save the <code>.gitlab-ci.yml</code> file containing the following snippet:</p>
        <code-block lang="yaml">
            qodana:
   image:
      name: jetbrains/qodana-&lt;linter&gt;
      entrypoint: [""]
   cache:
      - key: qodana-2024.1-$CI_DEFAULT_BRANCH-$CI_COMMIT_REF_SLUG
        fallback_keys:
           - qodana-2024.1-$CI_DEFAULT_BRANCH-
           - qodana-2024.1-
        paths:
           - .qodana/cache
   variables:
      QODANA_TOKEN: $qodana_token
    script:
      - >
        qodana --diff-start=$CI_MERGE_REQUEST_TARGET_BRANCH_SHA \
          --results-dir=$CI_PROJECT_DIR/.qodana/results \
          --cache-dir=$CI_PROJECT_DIR/.qodana/cache
   artifacts:
      paths:
         - .qodana/results
      expose_as: 'Qodana report'
        </code-block>
    </tab>
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$">
            docker run \
            &nbsp;&nbsp;&nbsp;-v $(pwd):/data/project/ \
            &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
            &nbsp;&nbsp;&nbsp;jetbrains/qodana-&lt;linter&gt; \
            &nbsp;&nbsp;&nbsp;--diff-start=&lt;GIT_START_HASH&gt;
        </code-block>
    </tab>
</tabs>

## Analyze changes between two commits

<p>If you would like to inspect a set of changes between two commits, you can employ both <code>--diff-start</code>
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
            uses: JetBrains/qodana-action@v2024.1
            with:
              args: --diff-start,&lt;GIT_START_HASH&gt;,--diff-end,&lt;GIT_END_HASH&gt; 
            env:
              QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
        </code-block>
    </step>
    </procedure>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab-cicd">
<p>Make sure that your project repository is accessible by GitLab CI/CD.</p>
<p>In the root directory of your project, save the <code>.gitlab-ci.yml</code> file containing the following snippet:</p>
        <code-block lang="yaml">
            qodana:
   image:
      name: jetbrains/qodana-&lt;linter&gt;
      entrypoint: [""]
   cache:
      - key: qodana-2024.1-$CI_DEFAULT_BRANCH-$CI_COMMIT_REF_SLUG
        fallback_keys:
           - qodana-2024.1-$CI_DEFAULT_BRANCH-
           - qodana-2024.1-
        paths:
           - .qodana/cache
   variables:
      QODANA_TOKEN: $qodana_token
    script:
      - >
        qodana --diff-start=$CI_MERGE_REQUEST_TARGET_BRANCH_SHA \
          --diff-end=$CI_MERGE_REQUEST_SOURCE_BRANCH_SHA \
          --results-dir=$CI_PROJECT_DIR/.qodana/results \
          --cache-dir=$CI_PROJECT_DIR/.qodana/cache
   artifacts:
      paths:
         - .qodana/results
      expose_as: 'Qodana report'
        </code-block>
    </tab>
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$">
            docker run \
            &nbsp;&nbsp;&nbsp;-v $(pwd):/data/project/ \
            &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
            &nbsp;&nbsp;&nbsp;jetbrains/qodana-&lt;linter&gt; \
            &nbsp;&nbsp;&nbsp;--diff-start=&lt;GIT_START_HASH&gt; \
            &nbsp;&nbsp;&nbsp;--diff-end=&lt;GIT_END_HASH&gt;
        </code-block>
    </tab>
</tabs>
