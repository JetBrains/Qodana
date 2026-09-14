# Upgrading Qodana
<link-summary>Learn how you can update %product% depending on the deployment option.</link-summary>

Upgrading %product% to actual versions is a necessary step. For example, new features published in %cloud% can be 
incompatible with older versions of %product%. The current %product% version is %version-current%. 

This section explains how you can upgrade %product% to the latest version depending on the available [deployment options](deploy-qodana.md). 

## Qodana CLI

<link-summary>Upgrade %product% CLI depending on the deployment option.</link-summary>

Depending on how you deployed %product% CLI on your machine, run one of the following commands:

<tabs group="gs-cli">
    <tab title="macOS and Linux" group-key="gs-macos-linux">
        <p>Upgrade with <a href="https://brew.sh/">Homebrew</a>:</p>
        <code-block lang="shell" prompt="$">
                        brew upgrade qodana
                    </code-block>
        <p>Upgrade Qodana CLI to a specific version using our installer:</p>
        <code-block lang="shell" prompt="$">
                        curl -fsSL https://jb.gg/qodana-cli/install | bash -s -- v%version-current-upgrade%.1
                   </code-block>
        <p>On Linux, you can also upgrade %instance% using <a href="https://go.dev/doc/install">Go</a>:</p>
        <code-block lang="shell" prompt="$">
                        go install github.com/JetBrains/qodana-cli@latest
                    </code-block>
    </tab>
    <tab title="Microsoft Windows" group-key="gs-windows">
        <p>Upgrade with <a href="https://learn.microsoft.com/en-us/windows/package-manager/winget/">Windows Package Manager</a>:</p>
        <code-block lang="shell">
                        winget upgrade -e --id JetBrains.QodanaCLI
                    </code-block>
        <p>Upgrade with <a href="https://chocolatey.org/">Chocolatey</a>:</p>
        <code-block>
                        choco upgrade qodana
                    </code-block>
        <p>Upgrade with <a href="https://scoop.sh/">Scoop</a>:</p>
        <code-block lang="shell">
          scoop update qodana
        </code-block>
    </tab>
</tabs>

## CI/CD platforms

<link-summary>Keep the %product% version upgraded depending on a CI/CD platform.</link-summary>


Depending on a CI/CD platform used, you should keep upgraded either the Docker image version or the %product% application 
version while configuring, see the snippets below.

<tabs>
<tab title="Azure Pipelines">
         <p>The <code>task: %azure-version%</code> line configures the major version of the %product% task and automatically employs the newest minor version. 
            Use this line to upgrade %product% to the newest major version:</p>
      <code-block lang="yaml" emphasize-lines="17">
         trigger:
           - main
         &nbsp;
         pool:
           vmImage: ubuntu-latest
         &nbsp;
         steps:
           - checkout: self 
             persistCredentials: true
           - task: Cache@2
             inputs:
               key: '"$(Build.Repository.Name)" | "$(Build.SourceBranchName)" | "$(Build.SourceVersion)"'
               path: '$(Agent.TempDirectory)/qodana/cache'
               restoreKeys: |
                 "$(Build.Repository.Name)" | "$(Build.SourceBranchName)"
                 "$(Build.Repository.Name)"
           - task: %azure-version%
             inputs:
               uploadResult: true
             env:
               QODANA_TOKEN: $(QODANA_TOKEN)
         </code-block>
</tab>
<tab title="Bitbucket Cloud">
<p>The  <code>image: jetbrains/qodana-&lt;image&gt;:%version-current-upgrade%</code> 
line configures the Docker image used for %product% and specifies its version:</p>
        <code-block lang="yaml" emphasize-lines="10"><![CDATA[
            image: atlassian/default-image:4

            pipelines:
              branches:
                main:
                  - step:
                      name: Qodana
                      caches:
                        - qodana
                      image: jetbrains/qodana-<image>:%version-current-upgrade%
                      script:
                        - export QODANA_TOKEN=$QODANA_TOKEN
                        - qodana --results-dir=$BITBUCKET_CLONE_DIR/.qodana --report-dir=$BITBUCKET_CLONE_DIR/.qodana/report --cache-dir=$HOME/.qodana/cache
                      artifacts:
                        - .qodana/report

            definitions:
              caches:
                qodana: .qodana/cache
        ]]>
</code-block>
</tab>
<tab title="CircleCI">
<p>The <code>qodana: %circleci-version%</code> line configures the version of the used CircleCI Qodana orb:</p>
<code-block lang="yaml" emphasize-lines="4">
version: 2.1

orbs:
  qodana: %circleci-version%

jobs:
  code-quality:
    machine:
      image: 'ubuntu-2004:current'
    environment: $QODANA_TOKEN
    steps:
      - checkout
      - qodana/scan

workflows:
  main:
    jobs:
      - code-quality:
        context: qodana
</code-block>
</tab>
<tab title="GitHub Actions">
<p>The <code>uses: %action-version%</code> line configures the version of the employed Qodana Scan GitHub action:</p>
                <code-block lang="yaml" emphasize-lines="24">
                    name: Qodana
                    on:
                        workflow_dispatch:
                        pull_request:
                        push:
                            branches: # Specify your branches here
                                - main # The 'main' branch
                                - master # The 'master' branch
                                - 'releases/*' # The release branches
&nbsp;
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
                                      args: |
                                          --linter &lt;qodana-linter&gt;
                                          --within-docker false
                                  env:
                                      QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
                </code-block>
</tab>
<tab title="GitLab CI/CD">
<p>Configure the newest version of the Qodana Scan GitLab Pipeline component and the <a href="deploy-qodana.md" anchor="deploy-qodana-container-mode">Docker image</a> as shown below:</p>
      <code-block lang="yaml" emphasize-lines="2,4">
         include:
            - component: %gitlab-version%
              inputs:
                 image: jetbrains/qodana-&lt;image&gt;:%version-current-upgrade%
      </code-block>
<p>The component and Docker image versions should be identical so that %product% can operate correctly.</p>
</tab>
<tab title="Jenkins">
<p>The <code>image 'jetbrains/qodana-&lt;image&gt;:%version-current-upgrade%'</code> 
line configures the Docker image used for %product% and specifies its version:</p>
<code-block lang="groovy" emphasize-lines="11"><![CDATA[
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
            image 'jetbrains/qodana-<image>:%version-current-upgrade%'
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
<tab title="TeamCity">
<p>On the <ui-path>Qodana</ui-path> runner configuration page, click <ui-path>Show advanced options</ui-path> and make sure that <ui-path>Version</ui-path> is set to <code>Latest</code>.</p>
</tab>
</tabs>
