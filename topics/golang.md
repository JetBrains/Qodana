# Golang

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<img src="golang.png" dark-src="golang_dark.png" alt="Golang" width="296"/>

<show-structure for="chapter" depth="3"/>

<!-- Linter-related variables -->
<var name="qp" value="Qodana for Go"/>
<var name="qp-linter" value="jetbrains/qodana-go:2024.2-eap"/>
<var name="JenkinsCred" value="https://www.jenkins.io/doc/book/using/using-credentials/#adding-new-global-credentials"/>
<var name="ide" value="GoLand"/>

<!-- Content-related variables -->
<var name="Dplugin" value="https://plugins.jenkins.io/docker-plugin/"/>
<var name="DPplugin" value="https://plugins.jenkins.io/docker-workflow/"/>
<var name="Gplugin" value="https://plugins.jenkins.io/git/"/>
<var name="Dockeraccess" value="https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user"/>
<var name="MultipipeCreate" value="https://www.jenkins.io/doc/book/pipeline/multibranch/#creating-a-multibranch-pipeline"/>
<var name="TeamCityProject" value="https://www.jetbrains.com/help/teamcity/configure-and-run-your-first-build.html#Create+your+first+project"/>
<var name="TeamCityBuildConfig" value="https://www.jetbrains.com/help/teamcity/creating-and-editing-build-configurations.html"/>
<var name="TeamCityBuildSteps" value="https://www.jetbrains.com/help/teamcity/configuring-build-steps.html"/>
<var name="TeamCityCommandLine" value="https://www.jetbrains.com/help/teamcity/command-line.html#General+Settings"/>
<var name="TeamCityPullRequests" value="https://www.jetbrains.com/help/teamcity/pull-requests.html"/>
<var name="TeamCityBranches" value="https://www.jetbrains.com/help/teamcity/configuring-finish-build-trigger.html#Trigger+Settings"/>
<var name="non-root-user" value="https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user"/>

<link-summary>%qp% is based on %ide% and provides static analysis for Go projects.</link-summary>

All %product% linters are based on JetBrains IDEs designed for particular programming languages and frameworks. To analyze
Golang projects, you can use the %qp% linters based on [%ide%](https://www.jetbrains.com/go/) and licensed under the Ultimate and
Ultimate Plus [licenses](pricing.md).

To see the list of supported technologies and features, you can navigate to the [](#golang-feature-matrix) section.

## Before you start
{id="golang-before-you-start"}

### Qodana Cloud

To run linters, you need to obtain a [project token](project-token.md) that
will be used by %product% for identifying and verifying a license.

<procedure>
    <step>
        Navigate to <a href="https://qodana.cloud">Qodana Cloud</a> and create an <a href="cloud-quickstart.md">account</a> there.
    </step>
    <step>
        In Qodana Cloud, create an <a href="cloud-organizations.topic">organization</a>, a <a href="cloud-teams.topic">team</a>, 
        and a <a href="cloud-projects.topic">project</a>.
    </step>
    <step>
        On the <a href="cloud-projects.topic" anchor="cloud-manage-projects">project card</a>, you can find the <a href="project-token.md">project token</a> 
        that you will be using further in this section.
    </step>
</procedure>

<note>This linter requires the Qodana Cloud <a href="project-token.md">project token</a>.</note>

### Prepare your software

The examples below show how to prepare software before running %product%.

<tabs group="software">
    <tab title="GitHub Actions" group-key="github">
        <p>You can run %product% using the <a href="https://github.com/marketplace/actions/qodana-scan">Qodana Scan GitHub action</a>.</p>
        <procedure>
            <step>On the <ui-path>Settings</ui-path> tab of the GitHub UI, create the <code>QODANA_TOKEN</code>
                <a href="https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository">encrypted secret</a>
                and save the <a href="project-token.md">project token</a> as its value.
            </step>
            <step><p>On the <ui-path>Actions</ui-path> tab of the GitHub UI, set up a new workflow and save the
                following workflow configuration to the <code>.github/workflows/code_quality.yml</code> file:</p>
                  <code-block lang="yaml">
                      name: Qodana
                      on:
                        workflow_dispatch:
                        pull_request:
                        push:
                          branches:
                            - main
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
                              uses: JetBrains/qodana-action@v2024.2
                              env:
                                QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
                  </code-block>
                  <p>This configuration sample will be modified throughout the section.</p>
            </step>
        </procedure>
    </tab>
    <tab title="Jenkins" group-key="jenkins">
        <procedure>
            <step>
              <p>In Jenkins, make sure that these plugins are up and running:</p>
              <list>
              <li><a href="%Dplugin%">Docker</a> and <a href="%DPplugin%">Docker Pipeline</a> are required for running Docker images,</li>
              <li><a href="%Gplugin%">git</a> is required for git operations in Jenkins projects.</li>
              </list>
              <p>Make sure that Docker is installed and accessible by Jenkins.</p>
              <p>If applicable, make sure that Docker is accessible by the <code>jenkins</code> user as described in the
              <a href="%Dockeraccess%">Manage Docker as a non-root user</a> section of the Docker documentation.</p>
            </step>
            <step>In Jenkins, create the <code>qodana-token</code> <a href="https://www.jenkins.io/doc/book/using/using-credentials/">credential</a> and save the 
              <a href="project-token.md">project token</a> as its value.</step>
            <step>
              <p>In Jenkins, create a Multibranch Pipeline project as described on the <a href="%MultipipeCreate%">Jenkins documentation portal</a>.</p>
            </step>
            <step>
              <p>In the root directory of your project repository, save the <code>Jenkinsfile</code> containing the following configuration:</p>
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
                                image '%qp-linter%'
                            }
                        }
                        stages {
                            stage('Qodana') {
                                steps {
                                    sh '''
                                    qodana
                                    '''
                                }
                            }
                        }
                    }
                </code-block>
                  <p>This configuration sample will be modified throughout the section.</p>
            </step>
        </procedure>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab">
        <procedure>
            <step><p>Make sure that your project repository is accessible by GitLab CI/CD.</p></step>
            <step>In GitLab CI/CD, create the <a href="https://docs.gitlab.com/ee/ci/variables/"><code>$qodana_token</code></a> 
            variable and save the <a href="project-token.md">project token</a> as its value.</step>
            <step><p>In the root directory of your project, create the <code>.gitlab-ci.yml</code> and save the following configuration in it:</p>
                <code-block lang="yaml">
                    qodana:
                       image:
                          name: %qp-linter%
                          entrypoint: [""]
                       cache:
                          - key: qodana-2024.2-$CI_DEFAULT_BRANCH-$CI_COMMIT_REF_SLUG
                            fallback_keys:
                               - qodana-2024.2-$CI_DEFAULT_BRANCH-
                               - qodana-2024.2-
                            paths:
                               - .qodana/cache
                       variables:
                          QODANA_TOKEN: $qodana_token           - 
                       script:
                          - qodana --cache-dir=$CI_PROJECT_DIR/.qodana/cache
                </code-block>
                  <p>This configuration sample will be modified throughout the section.</p>
            </step>
        </procedure>
    </tab>
    <tab title="TeamCity" group-key="teamcity">
        <p>In TeamCity, Create a 
        <a href="https://www.jetbrains.com/help/teamcity/configure-and-run-your-first-build.html#Create+your+first+project">project</a> 
        and a <a href="https://www.jetbrains.com/help/teamcity/creating-and-editing-build-configurations.html">build configuration</a>.</p>
    </tab>
    <tab title="Command line" group-key="command-line">
        <p>You have two options to run %product% locally: you can either run 
        <a href="https://github.com/JetBrains/qodana-cli">Qodana CLI</a> or directly use the Docker image of %product%.
        As %product% linters are distributed in Docker containers, Docker needs to be installed on your local machine.  
        If you are using Linux, you should be able to run Docker under your current <a href="%non-root-user%">non-root user</a>, check
        the <a href="https://github.com/JetBrains/qodana-cli/releases/latest">installation page</a> for details.</p>
    </tab>
</tabs>

## Run %product%

<note><include from="lib_qd.topic" element-id="docker-ram-note"/></note>

<include from="lib_qd.topic" element-id="root-and-non-root-users-info-bubble"></include>

<!--<p>You can run all linters described in this section in two modes:</p>
<list>
  <li>The <a href="native-mode.md">native mode</a> is the recommended method that lets you run 
    linters without using Docker containers,</li>
  <li>Container mode is an alternative that involves Docker containers the linters.</li>
</list>
<tabs group="native-container">
  <tab title="Native mode" group-key="native-mode">
    <snippet id="dotnet-run-qodana-native-mode-yaml">
      <p>Using a YAML configuration is the preferred method of configuring linters because it lets you use such configurations
          across all software that runs %product% without additional efforts.</p>
      <p>Here is the list of values for configuring the native mode:</p>
      <list>
        <li><code>QDJVM</code> for the %jvm% linter,</li>
        <li><code>QDAND</code> for the %jvm-a% linter,</li>
        <li><code>QDJVMC</code> for the %jvm-co% linter,</li>
        <li><code>QDANDC</code> for the %jvm-co-a% linter.</li>
      </list>
          <p>You can configure the <a href="native-mode.md">native mode</a> by adding this line to the 
          <a href="qodana-yaml.md"><code>qodana.yaml</code></a> file, for example:</p>
      <code-block lang="yaml">
          ide: QDJVM
      </code-block>
    </snippet>
      <p>Alternatively, you can implement the native mode configuration as shown in examples below.</p>
      <tabs group="software">
          <tab title="GitHub Actions" group-key="github">
              <p>You can run %product% using the <a href="https://github.com/marketplace/actions/qodana-scan">Qodana Scan GitHub action</a>.</p>
              <procedure>
                  <step>On the <ui-path>Settings</ui-path> tab of the GitHub UI, create the <code>QODANA_TOKEN</code>
                      <a href="https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository">encrypted secret</a>
                      and save the <a href="cloud-projects.topic" anchor="cloud-manage-projects">project token</a> as its value.
                  </step>
                  <step>On the <ui-path>Actions</ui-path> tab of the GitHub UI, set up a new workflow and create the
                      <code>.github/workflows/code_quality.yml</code> file.</step>
                  <step>To inspect the <code>main</code> branch, release branches and the pull requests coming
                  to your repository in the native mode, save this workflow configuration to the <code>.github/workflows/code_quality.yml</code> file:
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
                                  uses: JetBrains/qodana-action@v2024.2
                                  with:
                                      args: --ide,&lt;QDJVM/QDAND/QDJVMC/QDANDC&gt;
                                  env:
                                    QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
                      </code-block>
                  </step>
              </procedure>
              <p>More configuration examples are available in the <a href="github.md"/> section.</p>
          </tab>
          <tab title="Command line" group-key="command-line">
              <p>Run this command in the project root directory:</p>
              <code-block lang="shell" prompt="$">
                  qodana scan \
                  &nbsp;&nbsp;&nbsp;--ide &lt;QDJVM/QDAND/QDJVMC/QDANDC&gt;
              </code-block>
              <p>Here, the <code>--ide</code> option downloads and employs the JetBrains IDE binary file.</p>
              <p>Alternatively, in the <code>qodana.yaml</code> file save <code>ide: &lt;QDJVM/QDAND/QDJVMC/QDANDC&gt;</code>, and then run %instance% 
                  using the following command:</p>
              <code-block lang="shell" prompt="$">
                  qodana scan
              </code-block>
              <p>In your browser, open <a href="https://qodana.cloud">Qodana Cloud</a> to examine analysis results and
                reconfigure the analysis, see the <a href="ui-overview.md"/> section for
                details.</p>
          </tab>
      </tabs>
  </tab>
  <tab title="Container mode" group-key="container-mode">
      <p>The container mode is available for all linters; however, we recommend that you use the native mode.</p>-->
<tabs group="software">
    <tab title="GitHub Actions" group-key="github">
      <p>To analyze the <code>main</code> branch, release branches and the pull requests coming
      to your repository in the container mode, save this workflow configuration to the <code>.github/workflows/code_quality.yml</code> file:</p>
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
                      uses: JetBrains/qodana-action@v2024.2
                      env:
                        QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
          </code-block>
  <p>More configuration examples are available in the <a href="github.md"/> section.</p>
    </tab>
    <tab title="Jenkins" group-key="jenkins">
        <p>Save this snippet to the <code>Jenkinsfile</code>:</p>
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
                        image '%qp-linter%'
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
        </code-block>
        <p>More configuration examples are available in the <a href="jenkins.md"/>section.</p>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab">
        <p>Save this snippet to the <code>.gitlab-ci.yml</code> file and uncomment the linter that you would like to run:</p>
        <code-block lang="yaml">
            qodana:
               image:
                  name: %qp-linter% 
                  entrypoint: [""]
               cache:
                  - key: qodana-2024.2-$CI_DEFAULT_BRANCH-$CI_COMMIT_REF_SLUG
                    fallback_keys:
                       - qodana-2024.2-$CI_DEFAULT_BRANCH-
                       - qodana-2024.2-
                    paths:
                       - .qodana/cache
               variables:
                  QODANA_TOKEN: $qodana_token           - 
               script:
                  - qodana --cache-dir=$CI_PROJECT_DIR/.qodana/cache
        </code-block>
      <p>In this snippet:</p>
      <list>
      <li>The <a href="https://docs.gitlab.com/ee/ci/caching/"><code>cache</code></a> keyword configures GitLab CI/CD caches to store the %instance% cache,
        so subsequent runs will be faster,</li>
      <li>The <a href="https://docs.gitlab.com/ee/ci/yaml/#script"><code>script</code></a> keyword runs the <code>qodana</code> command and enumerates the %instance%
        configuration options described in the <a href="docker-image-configuration.topic"/> section,</li>
      <li>The <code>variables</code> keyword defines the <code>QODANA_TOKEN</code>
      <a href="https://docs.gitlab.com/ee/ci/variables/#define-a-cicd-variable-in-the-ui">variable</a> referring to the 
      <a href="project-token.md">project token</a>.</li>
      </list>
    <p>More configuration examples are available in the <a href="gitlab.md"/>section.</p>
    </tab>
    <tab title="TeamCity" group-key="teamcity" id="jvm-run-qodana-teamcity">
      <include from="teamcity.md" element-id="teamcity-add-a-qodana-runner"/>
      <p>More configuration examples are available in the <a href="teamcity.md"/>section.</p>
    </tab>
    <tab title="Command line" group-key="command-line">
        <p>Start local analysis with <code>source-directory</code>
            pointing to the root of your project and
            <code>QODANA_TOKEN</code> referring to the <a href="project-token.md">project token</a>:</p>
        <tabs group="cli-settings">
          <tab title="Qodana CLI" group-key="qodana-cli">
                <code-block lang="shell" prompt="$">
                    qodana scan \
                       -e QODANA_TOKEN="&lt;qodana-cloud-token&gt;"
                       -l %qp-linter%
                </code-block>
          </tab>
          <tab title="Docker image" group-key="docker-image">
            <code-block lang="shell" prompt="$">
                docker run \
                &nbsp;&nbsp;&nbsp;-v &lt;source-directory&gt;/:/data/project/ \
                &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                &nbsp;&nbsp;&nbsp;%qp-linter%
            </code-block>
          </tab>
        </tabs>
<p>In your browser, open <a href="https://qodana.cloud">Qodana Cloud</a> to examine analysis results and
  reconfigure the analysis, see the <a href="ui-overview.md"/> section for
    details.</p>
    </tab>
    <tab title="JetBrains IDEs" group-key="ides">
        <procedure>
            <step>
               <p>In %ide%, navigate to <ui-path>Tools | Qodana | Try Code Analysis with Qodana</ui-path>.</p> 
            </step>
            <step>
               <p>On the <ui-path>Run Qodana</ui-path> dialog, you can configure:</p>
                  <list>
                    <li>Options used by %product% and configured by the <a href="qodana-yaml.md"><code>qodana.yaml</code></a> file.</li>
                     <li>The <a href="cloud-forward-reports.topic"><ui-path>Send inspection results to Qodana Cloud</ui-path></a> option 
                      using a <a href="cloud-projects.topic" anchor="cloud-manage-projects">project token</a>.</li>
                     <li>The <a href="baseline.topic"><ui-path>Use Qodana analysis baseline</ui-path></a> option to run %product% with a baseline.</li>
                  </list>
                   <img src="ide-plugin-run-qodana-2.png" width="793" alt="Configuring Qodana in the Run Qodana dialog" border-effect="line"/>
                <p>Click <ui-path>Run</ui-path> for analyzing your code.</p>
            </step>
            <step>
               <p>In the <ui-path>Server-Side Analysis</ui-path> tool window, see the <a href="qodana-ide-plugin.md" anchor="ide-plugin-study-reports">inspection results</a>.</p>
            </step>
        </procedure>
    </tab>
</tabs>
  <!--</tab>-->
<!--</tabs>-->

## Explore analysis results

<tabs group="software">
    <tab title="JetBrains IDEs" group-key="ides" id="jvm-explore-results-ides">
      <p>You can load the latest %instance% report from Qodana Cloud to your IDE as explained below.</p>
      <procedure>
         <step>
            <p>In your IDE, navigate to <ui-path>Tools | Qodana | Log in to Qodana</ui-path>.</p>
         </step>
         <step>
            <p>
               On the <ui-path>Settings</ui-path> dialog, click <ui-path>Log in</ui-path>.
            </p>
            <img src="ide-plugin-connect-1.png" dark-src="ide-plugin-connect-1_dark.png" width="706" alt="Connecting to Qodana Cloud" border-effect="line"/>
         <p>This will redirect you to the authentication page.</p>
         </step>
         <step>
            <p>Select the <a href="cloud-projects.topic">Qodana Cloud project</a> to link your local project with.</p>
            <img src="ide-plugin-connect-2.png" dark-src="ide-plugin-connect-2_dark.png" width="706" alt="Linking the project to Qodana Cloud" border-effect="line"/>
         </step>
         <step>
            <p>If you check the <ui-path>Always load most relevant Qodana report</ui-path> option, you will be able to receive the most actual and relevant reports from Qodana Cloud.</p>
            <img src="ide-plugin-connect-3.png" dark-src="ide-plugin-connect-3_dark.png" width="706" alt="Enabling to load the most relevant reports" border-effect="line"/>
              <p>In this case, the IDE will search and fetch from Qodana Cloud the report that has the revision ID corresponding to the 
              current revision ID (HEAD). If this report was not found, the IDE will select the previous report with the revision
              closest to the current revision ID (HEAD). Otherwise, the IDE retrieves the latest available report from Qodana Cloud.</p>
          </step> 
          <step>
             <p>On the <ui-path>Server-Side Analysis</ui-path> tab of the <ui-path>Problems</ui-path> tool window, view <a href="qodana-ide-plugin.md" anchor="ide-plugin-study-reports">analysis results</a>.</p>
          </step>
      </procedure>
    </tab>
    <tab title="Qodana Cloud" group-key="cloud" id="jvm-explore-results-qodana-cloud">
      <p>Once %product% analyzed your project and uploaded the analysis results to Qodana Cloud, in
      <a href="https://qodana.cloud">Qodana Cloud</a> navigate to your project and review the analysis results report.</p>
      <img src="qc-report-example-js.png" alt="Analysis report example" width="720" border-effect="line"/>
      <p>To learn more about %instance% report UI, see the <a href="ui-overview.md"/> section.</p>
    </tab>
</tabs> 

## Extend %product% configuration

### Adjusting the scope of analysis

Out of the box, Qodana provides two [predefined profiles](inspection-profiles.md#inspection-profiles-existing-profiles) hosted on
[GitHub](https://github.com/JetBrains/qodana-profiles/tree/master/.idea/inspectionProfiles):

* `qodana.starter` is the default profile and a subset of the more comprehensive `qodana.recommended` profile,
* `qodana.recommended` is suitable for running in CI/CD pipelines and mostly implements the default %ide% profile, see the
  [%ide%](https://www.jetbrains.com/help/idea/customizing-profiles.html) documentation for details.

You can customize %product% profiles using configurations in [YAML](custom-profiles.md) and [XML](custom-xml-profiles.md) formats.

To learn more about configuration basics, visit the [](override-a-profile.md) section. Complete guides are
available in the [](custom-profiles.md) and [](custom-xml-profiles.md) sections.

### Enabling the baseline

You can skip analysis for specific problems using the [baseline](baseline.topic) feature. Information about a baseline is contained
in a SARIF-formatted file.

<!--<tabs group="native-container">
  <tab title="Native mode" group-key="native-mode">
      <tabs group="software">
          <tab title="GitHub Actions" group-key="github">
            <p>This snippet contains the <code>args: --baseline,qodana.sarif.json</code> line that specifies the path to the SARIF-formatted baseline file:</p>
            <code-block lang="yaml">
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
                        uses: JetBrains/qodana-action@v2024.2
                        with: 
                          args: --ide,&lt;QDJVM/QDAND/QDJVMC/QDANDC&gt;,--baseline,&lt;path/to/qodana.sarif.json&gt;
                        env:
                          QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
            </code-block>
          </tab>
          <tab title="Command line" group-key="command-line">
              <p>Run this command in the project root directory:</p>
              <code-block lang="shell" prompt="$">
                  qodana scan \
                  &nbsp;&nbsp;&nbsp;--ide &lt;QDJVM/QDAND/QDJVMC/QDANDC&gt; \
                  &nbsp;&nbsp;&nbsp;--baseline,&lt;path/to/qodana.sarif.json&gt;
              </code-block>
              <p>Here, the <code>--baseline,&lt;path/to/qodana.sarif.json&gt;</code> option specifies the <a href="baseline.topic">baseline</a> feature.</p>
              <p>Alternatively, in the <code>qodana.yaml</code> file save <code>ide: &lt;QDJVM/QDAND/QDJVMC/QDANDC&gt;</code>, and then run %instance% 
                  using the following command:</p>
              <code-block lang="shell" prompt="$">
                  qodana scan \
                  &nbsp;&nbsp;&nbsp;--baseline,&lt;path/to/qodana.sarif.json&gt;
              </code-block>
        <p>Here, <code>--ide</code> denotes the following linters:</p>
        <table>
          <tr>
            <td>Value</td>
            <td>Linter</td>
          </tr>
          <tr>
            <td><code>QDJVM</code></td>
            <td>Qodana for JVM</td>
          </tr>
          <tr>
            <td><code>QDJVMC</code></td>
            <td>Qodana Community for JVM</td>
          </tr>
          <tr>
            <td><code>QDANDC</code></td>
            <td>Qodana Community for Android</td>
          </tr>
          <tr>
            <td><code>QDAND</code></td>
            <td>Qodana for Android</td>
          </tr>
        </table>
        <p>In your browser, open <a href="https://qodana.cloud">Qodana Cloud</a> to examine analysis results and
          reconfigure the analysis, see the <a href="ui-overview.md"/> section for
          details.</p>
          </tab>
      </tabs>
  </tab>
  <tab title="Container mode" group-key="container-mode">-->
<tabs group="software">
    <tab title="GitHub Actions" group-key="github">
      <p>This snippet contains the <code>args: --baseline,qodana.sarif.json</code> line that specifies the path to the SARIF-formatted baseline file:</p>
      <code-block lang="yaml">
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
                  uses: JetBrains/qodana-action@v2024.2
                  with:
                    args: --baseline,&lt;path/to/qodana.sarif.json&gt;
                  env:
                    QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
      </code-block>
    </tab>
    <tab title="Jenkins" group-key="jenkins">
      <p>The <code>stages</code> block contains the <code>--baseline &lt;path/to/qodana.sarif.json&gt;</code> line that specifies
      the path to the SARIF-formatted baseline file:</p>
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
                    image '%qp-linter%'
                }
            }
            stages {
                stage('Qodana') {
                    steps {
                        sh '''
                        qodana \
                        --baseline &lt;path/to/qodana.sarif.json&gt;
                        '''
                    }
                }
            }
        }
      </code-block>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab">
      <p>The <code>--baseline &lt;path/to/qodana.sarif.json&gt;</code> line in the <code>script</code> block invokes the 
        baseline feature.</p>
      <code-block lang="yaml">
        qodana:
           image:
              name: %qp-linter% 
              entrypoint: [""]
           cache:
              - key: qodana-2024.2-$CI_DEFAULT_BRANCH-$CI_COMMIT_REF_SLUG
                fallback_keys:
                   - qodana-2024.2-$CI_DEFAULT_BRANCH-
                   - qodana-2024.2-
                paths:
                   - .qodana/cache
           variables:
              QODANA_TOKEN: $qodana_token           - 
           script:
              - qodana --baseline &lt;path/to/qodana.sarif.json&gt; --results-dir=$CI_PROJECT_DIR/.qodana/results
                 --cache-dir=$CI_PROJECT_DIR/.qodana/cache
      </code-block>
    </tab>
    <tab title="TeamCity" group-key="teamcity">
      <p>Using the <ui-path>Additional Qodana arguments</ui-path> field from the <a anchor="jvm-run-qodana-teamcity">previous section</a>  
      configure the <a href="baseline.topic">baseline</a> feature by specifying the <code>--baseline &lt;path/to/qodana.sarif.json&gt;</code>
      option.</p>
    </tab>
    <tab title="Command line" group-key="command-line">
      <p>Choose how you would like to run the baseline feature from the command line:</p>
      <tabs group="cli-settings">
          <tab group-key="qodana-cli" title="Qodana CLI">
              <code-block prompt="$">
                  qodana scan \
                     -v &lt;path_to_baseline&gt;:/data/base/ \
                     -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                     -l %qp-linter% \
                     --baseline /data/base/&lt;path-relative-to-project-dir&gt;/qodana.sarif.json
              </code-block>
          </tab>
          <tab group-key="docker-image" title="Docker image">
              <code-block lang="shell" prompt="$">
                  docker run \
                     -v &lt;source-directory&gt;/:/data/project/ \
                     -v &lt;path_to_baseline&gt;:/data/base/ \
                     -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                     %qp-linter% \
                     --baseline /data/base/&lt;path-relative-to-project-dir&gt;/qodana.sarif.json
              </code-block>
          </tab>
      </tabs>
    </tab>
    <tab title="JetBrains IDEs" group-key="ides">
    <procedure>
        <step>In your IDE, navigate to the <ui-path>Problems</ui-path> tool window. </step>
        <step>In the <ui-path>Problems</ui-path> tool window, click the <ui-path>Server-Side Analysis</ui-path> tab.</step>
        <step>On the <ui-path>Server-Side Analysis</ui-path> tab, click the <ui-path>Try Locally</ui-path> button.</step>
        <step>On the dialog that opens, expand the <ui-path>Advanced configuration</ui-path> section and specify the path to the baseline file, and then click <ui-path>Run</ui-path>.</step>
    </procedure>
    </tab>
</tabs>
<!--  </tab>
</tabs>-->


### Enabling the quality gate

You can configure [quality gates](quality-gate.topic) for:

* The total number of project problems, 
* Multiple quality gates for <a href="faq.topic" anchor="faq-severities">problem severities</a>, 
* <a href="code-coverage.md">Code coverage</a> thresholds.

Save this snippet to the [`qodana.yaml`](qodana-yaml.md) file:

```yaml
failureConditions:
  severityThresholds:
    any: 50 # Total number of problems in all severities
    critical: 1 # Severities
    high: 2
    moderate: 3
    low: 4
    info: 5
  testCoverageThresholds: 
    fresh: 6 # Fresh code coverage
    total: 7 # Total percentage
```


### Analyzing pull requests

<!--<tabs group="native-container">
  <tab title="Native mode" group-key="native-mode">
    <tabs group="software">
      <tab title="GitHub Actions" group-key="github">
          <p>Add this snippet to the <code>.github/workflows/code_quality.yml</code> file:</p>
            <code-block lang="yaml">
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
                        uses: JetBrains/qodana-action@v2024.2
                        with: 
                          args: --ide,&lt;QDJVM/QDAND/QDJVMC/QDANDC&gt;,--diff-start,&lt;GIT_START_HASH&gt;
                        env:
                          QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
            </code-block>
      </tab>
      <tab title="Command line" group-key="command-line">
        <p>To analyze changes in your code, employ the <code>--diff-start</code> option and specify a hash of the commit 
        that will act as a base for comparison:</p>
              <code-block lang="shell" prompt="$">
                  qodana scan \
                  &nbsp;&nbsp;&nbsp;--ide &lt;QDJVM/QDAND/QDJVMC/QDANDC&gt; \
                  &nbsp;&nbsp;&nbsp;--diff-start=&lt;GIT_START_HASH&gt;
              </code-block>
              <p>Alternatively, in the <code>qodana.yaml</code> file save <code>ide: &lt;QDJVM/QDAND/QDJVMC/QDANDC&gt;</code>, and then run %instance% 
                  using the following command:</p>
              <code-block lang="shell" prompt="$">
                  qodana scan \
                  &nbsp;&nbsp;&nbsp;--diff-start=&lt;GIT_START_HASH&gt;
              </code-block>
        <p>Here, <code>--ide</code> denotes the following linters:</p>
        <table>
          <tr>
            <td>Value</td>
            <td>Linter</td>
          </tr>
          <tr>
            <td><code>QDJVM</code></td>
            <td>Qodana for JVM</td>
          </tr>
          <tr>
            <td><code>QDJVMC</code></td>
            <td>Qodana Community for JVM</td>
          </tr>
          <tr>
            <td><code>QDANDC</code></td>
            <td>Qodana Community for Android</td>
          </tr>
          <tr>
            <td><code>QDAND</code></td>
            <td>Qodana for Android</td>
          </tr>
        </table>
        <p>In your browser, open <a href="https://qodana.cloud">Qodana Cloud</a> to examine analysis results and
          reconfigure the analysis, see the <a href="ui-overview.md"/> section for
          details.</p>
      </tab>
    </tabs>
  </tab>
  <tab title="Container mode" group-key="container-mode">-->
  <tabs group="software">
    <tab title="GitHub Actions" group-key="github">
      <p>In GitHub Actions, the <code>--diff-start</code> can be omitted because it will be added automatically while running
        %product%, so you can save this snippet to the <code>.github/workflows/code_quality.yml</code> file:</p>
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
                        uses: JetBrains/qodana-action@v2024.2
                        env:
                          QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
        </code-block>
  </tab>
    <tab title="GitLab CI/CD" group-key="gitlab">
    <p>In the root directory of your project, save the <code>.gitlab-ci.yml</code> file containing the following snippet and then uncomment the required linter:</p>
    <code-block lang="yaml">
     qodana:
       image:
          name: %qp-linter% 
          entrypoint: [""]
       cache:
          - key: qodana-2024.2-$CI_DEFAULT_BRANCH-$CI_COMMIT_REF_SLUG
            fallback_keys:
               - qodana-2024.2-$CI_DEFAULT_BRANCH-
               - qodana-2024.2-
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
    <p>Here, the <code>--diff-start</code> option specifies a hash of the commit that will act as a base for comparison.</p>
  </tab>
    <tab title="TeamCity" group-key="teamcity">
    <p>Information about configuring TeamCity for analyzing pull and merge requests is available on the 
    <a href="%TeamCityPullRequests%">TeamCity</a> documentation portal.
  </p>
  </tab>
    <tab title="Command line" group-key="command-line">
    <p>To analyze changes in your code, employ the <code>--diff-start</code> option and specify a hash of the commit that will 
    act as a base for comparison:</p>
      <tabs group="cli-settings">
          <tab group-key="qodana-cli" title="Qodana CLI">
              <code-block prompt="$">
                  qodana scan \
                     -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                     -l %qp-linter% \
                     --diff-start=&lt;GIT_START_HASH&gt;
              </code-block>
          </tab>
          <tab group-key="docker-image" title="Docker image">
              <code-block lang="shell" prompt="$">
                docker run \
                &nbsp;&nbsp;&nbsp;-v $(pwd):/data/project/ \
                &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                &nbsp;&nbsp;&nbsp;%qp-linter% \
                &nbsp;&nbsp;&nbsp;--diff-start=&lt;GIT_START_HASH&gt;
              </code-block>
          </tab>
      </tabs>
    </tab>
 <!--</tab>-->
  </tabs>
<!--</tab>
</tabs>-->


## Supported technologies and features
{id="golang-feature-matrix"}

%qp% provides inspections for the following technologies.

<table style="none">
    <tr>
        <td>Programming languages</td>
        <td>
            <p>Golang</p>
        </td>
    </tr>
    <tr>
        <td>Markup languages</td>
        <td>
            <p>CSS</p>
            <p>HTML</p>
            <p>JSON and JSON5</p>
            <p>RELAX NG</p>
            <p>XML</p>
            <p>YAML</p>
        </td>
    </tr>
    <tr>
        <td>Scripting languages</td>
        <td>
            <p>Shell script</p>
        </td>
    </tr>
</table>

<include from="lib_qd.topic" element-id="linters-supported-features" use-filter="empty,non-jvm"/>