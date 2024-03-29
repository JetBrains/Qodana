# Analyze pull and merge requests

<link-summary>For all linter except Qodana Community for .NET, you can run incremental analysis on a change set like 
merge or pull requests.</link-summary> 

<note>This feature is not supported by the <a href="qodana-dotnet-community.md"/> linter.</note>

Using %product%, you can not only scan your entire codebase, but also run analysis on change sets like merge or pull 
requests.

<p>For example, if you just finished work and would like to analyze the changes, you
    can employ the <code>--diff-start</code> option and specify a hash of the commit that will act as a base
    for comparison:</p>

<tabs group="cli-settings">
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$">
            docker run \
            &nbsp;&nbsp;&nbsp;-v $(pwd):/data/project/ \
            &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
            &nbsp;&nbsp;&nbsp;jetbrains/qodana-&lt;linter&gt; \
            &nbsp;&nbsp;&nbsp;--diff-start=&lt;GIT_START_HASH&gt;
        </code-block>
    </tab>
    <tab title="Qodana CLI" group-key="qodana-cli">
        <code-block lang="shell" prompt="$">
            qodana scan \
            &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
            &nbsp;&nbsp;&nbsp;--diff-start=&lt;GIT_START_HASH&gt;
        </code-block>
    </tab>
    <tab title="GitHub Actions" group-key="github-actions">
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
            uses: JetBrains/qodana-action@v2023.3
            with:
              args: --diff-start,&lt;GIT_START_HASH&gt;,--diff-end,&lt;GIT_END_HASH&gt; 
            env:
              QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
        </code-block>
    </tab>
    <tab title="Jenkins" group-key="jenkins">
        <code-block lang="groovy">
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
            image 'jetbrains/qodana-&lt;linter&gt;'
        }
    }
    stages {
        stage('Qodana') {
            steps {
                sh '''
                qodana \
                --diff-start=&lt;GIT_START_HASH&gt;
                '''
            }
        }
    }
}
        </code-block>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab-cicd">
        <code-block lang="yaml">
            qodana:
   image:
      name: jetbrains/qodana-&lt;linter&gt;
      entrypoint: [""]
   cache:
      - key: qodana-2023.3-$CI_DEFAULT_BRANCH-$CI_COMMIT_REF_SLUG
        fallback_keys:
           - qodana-2023.3-$CI_DEFAULT_BRANCH-
           - qodana-2023.3-
        paths:
           - .qodana/cache
   variables:
      QODANA_TOKEN: $qodana_token           - 
   script:
      - qodana --diff-start=&lt;GIT_START_HASH&gt; --results-dir=$CI_PROJECT_DIR/.qodana/results
         --cache-dir=$CI_PROJECT_DIR/.qodana/cache
   artifacts:
      paths:
         - qodana/report/
      expose_as: 'Qodana report'
        </code-block>
    </tab>
</tabs>

<p>If you would like to inspect a set of changes between two commits, you can employ both <code>--diff-start</code>
and <code>--diff-end</code> options:</p>

<tabs group="cli-settings">
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
    <tab title="Qodana CLI" group-key="qodana-cli">
        <code-block lang="shell" prompt="$">
            qodana scan \
            &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
            &nbsp;&nbsp;&nbsp;--diff-start=&lt;GIT_START_HASH&gt; \
            &nbsp;&nbsp;&nbsp;--diff-end=&lt;GIT_END_HASH&gt;
        </code-block>
    </tab>
        <tab title="GitHub Actions" group-key="github-actions">
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
            uses: JetBrains/qodana-action@v2023.3
            with:
              args: --diff-start,&lt;GIT_START_HASH&gt;,--diff-end,&lt;GIT_END_HASH&gt; 
            env:
              QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
        </code-block>
    </tab>
    <tab title="Jenkins" group-key="jenkins">
        <code-block lang="groovy">
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
            image 'jetbrains/qodana-&lt;linter&gt;'
        }
    }
    stages {
        stage('Qodana') {
            steps {
                sh '''
                qodana \
                --diff-start=&lt;GIT_START_HASH&gt;\
                --diff-end=&lt;GIT_END_HASH&gt;
                '''
            }
        }
    }
}
        </code-block>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab-cicd">
        <code-block lang="yaml">
            qodana:
   image:
      name: jetbrains/qodana-&lt;linter&gt;
      entrypoint: [""]
   cache:
      - key: qodana-2023.3-$CI_DEFAULT_BRANCH-$CI_COMMIT_REF_SLUG
        fallback_keys:
           - qodana-2023.3-$CI_DEFAULT_BRANCH-
           - qodana-2023.3-
        paths:
           - .qodana/cache
   variables:
      QODANA_TOKEN: $qodana_token           - 
   script:
      - qodana --diff-start=&lt;GIT_START_HASH&gt; --diff-end=&lt;GIT_END_HASH&gt; --results-dir=$CI_PROJECT_DIR/.qodana/results
         --cache-dir=$CI_PROJECT_DIR/.qodana/cache
   artifacts:
      paths:
         - qodana/report/
      expose_as: 'Qodana report'
        </code-block>
    </tab>
</tabs>
