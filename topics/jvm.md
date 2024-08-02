[//]: # (title: Java, Kotlin, and Groovy)

<no-index/>

<show-structure for="chapter" depth="3"/>

<!-- Linter-related variables -->
<var name="qp" value="Qodana for JVM"/>
<var name="qp-co" value="Qodana Community for JVM"/>
<var name="qp-a" value="Qodana Community for Android"/>
<var name="qp-an" value="Qodana for Android"/>
<var name="qp-linter" value="jetbrains/qodana-jvm:2024.2-eap"/>
<var name="qp-co-linter" value="jetbrains/qodana-jvm-community:2024.2-eap"/>
<var name="qp-a-linter" value="jetbrains/qodana-jvm-android:2024.2-eap"/>
<var name="qp-an-linter" value="jetbrains/qodana-android:2024.2-eap"/>
<var name="qd-image" value="jetbrains/qodana<-jvm><-community><-android>:2024.2-eap"/>
<var name="JenkinsCred" value="https://www.jenkins.io/doc/book/using/using-credentials/#adding-new-global-credentials"/>
<var name="ide" value="IntelliJ IDEA Ultimate"/>
<var name="ide-co" value="IntelliJ IDEA Community"/>
<var name="ide-a" value="IntelliJ IDEA"/>

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

<link-summary>You can analyze your Java code using the %qp% and %qp-co% linters.</link-summary>

<warning>This is a draft document, so we do not recommend that you use it.</warning>

All %product% linters are based on IDEs designed for particular programming languages and frameworks. To analyze
Java projects, you can use the following linters:

* %qp% and %qp-an% are based on %ide% and licensed under the Ultimate and
  Ultimate Plus [licenses](pricing.md),
* %qp-co% and %qp-a% are based on %ide-co% and licensed under the Community license.

To see the list of supported features, you can navigate to the [](#jvm-feature-matrix) section.

## Before your start
{id="jvm-before-you-start"}

Before running %instance%, you can [configure the JDK](configure-jdk.md) for your project.

<include from="lib_qd.topic" element-id="root-and-non-root-users-info-bubble"></include>

<!-- Prerequisites for each software need to be added here from .NET -->

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

A project token is required for the %qp% and %qp-an% linters, and optional for the %qp-co% and %qp-a% linters.

### Prepare your software

This shows how to configure software from this section to %product% analysis. 

<tabs group="software">
    <tab title="GitHub Actions" group-key="github">
        <p>You can run %product% using the <a href="https://github.com/marketplace/actions/qodana-scan">Qodana Scan GitHub action</a>.</p>
        <procedure>
            <step>On the <ui-path>Settings</ui-path> tab of the GitHub UI, create the <code>QODANA_TOKEN</code>
                <a href="https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository">encrypted secret</a>
                and save the <a href="cloud-projects.topic" anchor="cloud-manage-projects">project token</a> as its value.
            </step>
            <step>On the <ui-path>Actions</ui-path> tab of the GitHub UI, set up a new workflow and create the
                <code>.github/workflows/code_quality.yml</code> file. This file will be used for running %product% as shown in further examples.
            </step>
        </procedure>
    </tab>
    <tab title="Jenkins" group-key="jenkins">
        <procedure>
            <step>
              <p>Make sure that these plugins are installed on your Jenkins instance:</p>
              <list>
              <li><a href="%Dplugin%">Docker</a> and <a href="%DPplugin%">Docker Pipeline</a> are required for running Docker images,</li>
              <li><a href="%Gplugin%">git</a> is required for git operations in Jenkins projects.</li>
              </list>
              <p>Make sure that Docker is installed and accessible by Jenkins.</p>
              <p>If applicable, make sure that Docker is accessible by the <code>jenkins</code> user as described in the
              <a href="%Dockeraccess%">Manage Docker as a non-root user</a> section of the Docker documentation.</p>
            </step>
            <step>
              <p>Create a Multibranch Pipeline project as described on the <a href="%MultipipeCreate%">Jenkins documentation portal</a>.</p>
            </step>
            <step>
              <p>In the root directory of your project repository, save the <code>Jenkinsfile</code>.
                This file will be used for running %product% as shown in further examples.</p>
            </step>
        </procedure>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab">
        <procedure>
            <step><p>Make sure that your project repository is accessible by GitLab CI/CD.</p></step>
            <step><p>In the root directory of your project, create the <code>.gitlab-ci.yml</code> file that will contain configurations for running %product%.</p></step>
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

<p>You can run all linters described in this section in two modes:</p>
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
          <p>You can configure the native mode by adding this line to the <a href="qodana-yaml.md"><code>qodana.yaml</code></a> file:</p>
      <code-block lang="yaml">
          ide: QDNET
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
                                      args: --ide,QDNET
                                  env:
                                    QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
                      </code-block>
                    <p>This configuration invokes the native mode using:</p>
                        <code-block lang="yaml">
                           with:
                           &nbsp;&nbsp;&nbsp;args: --ide,QDNET
                        </code-block>
                  </step>
              </procedure>
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
                              // Uncomment the linter you would like to employ
                              // image '%qp-linter%' // Qodana for JVM
                              // image '%qp-co-linter%' // Qodana Community for JVM
                              // image '%qp-a-linter%' // Qodana Community for Android
                              // image '%qp-an-linter%' // Qodana for Android
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
              <code-block lang="yaml">
                  qodana:
                     image:
                      # Uncomment the linter you would like to employ
                      # name: %qp-linter% # Qodana for JVM
                      # name: %qp-co-linter% # Qodana Community for JVM
                      # name: %qp-a-linter% # Qodana Community for Android
                      # name: %qp-an-linter% # Qodana for Android
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
                     artifacts:
                        paths:
                           - qodana/report/
                        expose_as: 'Qodana report'
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
          <tab title="TeamCity" group-key="teamcity">
            <include from="teamcity.md" element-id="teamcity-add-a-qodana-runner"/>
            <p>More configuration examples are available in the <a href="teamcity.md"/>section.</p>
          </tab>
          <tab title="Command line" group-key="command-line">
              <p>Run this command in the project root directory:</p>
              <code-block lang="shell" prompt="$">
                  qodana scan \
                  &nbsp;&nbsp;&nbsp;--ide QDNET
              </code-block>
              <p>Here, the <code>--ide</code> option downloads and employs the JetBrains IDE binary file.</p>
              <p>Alternatively, in the <code>qodana.yaml</code> file save <code>ide: QDNET</code>, and then run %instance% 
                  using the following command:</p>
              <code-block lang="shell" prompt="$">
                  qodana scan
              </code-block>
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
                          <li>Options used by %product% and configured by the <a href="qodana-yaml.md"><code>qodana.yaml</code></a> file. 
                            You can see that the native mode is already configured.</li>
                           <li>The <a href="cloud-forward-reports.topic"><ui-path>Send inspection results to Qodana Cloud</ui-path></a> option 
                            using a <a href="cloud-projects.topic" anchor="cloud-manage-projects">project token</a>.</li>
                           <li>The <a href="baseline.topic"><ui-path>Use Qodana analysis baseline</ui-path></a> option to run %product% with a baseline.</li>
                        </list>
                     <img src="ide-plugin-dotnet-run-qodana.png" width="793" alt="Configuring Qodana in the Run Qodana dialog" border-effect="line"/>
                      <p>Click <ui-path>Run</ui-path> for analyzing your code.</p>
                  </step>
                  <step>
                     <p>In the <ui-path>Server-Side Analysis</ui-path> tool window, see the <a href="qodana-ide-plugin.md" anchor="ide-plugin-study-reports">inspection results</a>.</p>
                  </step>
              </procedure>
          </tab>
      </tabs>
  </tab>
  <tab title="Container mode" group-key="container-mode">
      <p>The container mode is available for all linters; however, we recommend that you use the native mode.</p>
      <tabs group="software">
          <tab title="GitHub Actions" group-key="github">
              <procedure>
                  <step>On the <ui-path>Settings</ui-path> tab of the GitHub UI, create the <code>QODANA_TOKEN</code>
                      <a href="https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository">encrypted secret</a>
                      and save the <a href="cloud-projects.topic" anchor="cloud-manage-projects">project token</a> as its value.
                  </step>
                  <step>On the <ui-path>Actions</ui-path> tab of the GitHub UI, set up a new workflow and create the
                      <code>.github/workflows/code_quality.yml</code> file.</step>
                  <step>To analyze the <code>main</code> branch, release branches and the pull requests coming
                  to your repository in the container mode, save this workflow configuration to the <code>.github/workflows/code_quality.yml</code> file:
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
                  </step>
              </procedure>
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
                              // Uncomment the linter you would like to employ
                              // image '%qp-linter%' // Qodana for JVM
                              // image '%qp-co-linter%' // Qodana Community for JVM
                              // image '%qp-a-linter%' // Qodana Community for Android
                              // image '%qp-an-linter%' // Qodana for Android
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
              <code-block lang="yaml">
                  qodana:
                     image:
                      # Uncomment the linter you would like to employ
                      # name: %qp-linter% # Qodana for JVM
                      # name: %qp-co-linter% # Qodana Community for JVM
                      # name: %qp-a-linter% # Qodana Community for Android
                      # name: %qp-an-linter% # Qodana for Android
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
                     artifacts:
                        paths:
                           - qodana/report/
                        expose_as: 'Qodana report'
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
              <code-block lang="shell" prompt="$">
                  docker run \
                  &nbsp;&nbsp;&nbsp;-v &lt;source-directory&gt;/:/data/project/ \
                  &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                  &nbsp;&nbsp;&nbsp;&lt;linter&gt;
              </code-block>
              <p>Here, <code>&lt;linter&gt;</code> denotes the following linters:</p>
              <table>
                <tr>
                  <td>Image</td>
                  <td>Linter</td>
                </tr>
                <tr>
                  <td><code>%qp-linter%</code></td>
                  <td>Qodana for JVM</td>
                </tr>
                <tr>
                  <td><code>%qp-co-linter%</code></td>
                  <td>Qodana Community for JVM</td>
                </tr>
                <tr>
                  <td><code>%qp-a-linter%</code></td>
                  <td>Qodana Community for Android</td>
                </tr>
                <tr>
                  <td><code>%qp-an-linter%</code></td>
                  <td>Qodana for Android</td>
                </tr>
              </table>
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
                          <li>Options used by %product% and configured by the <a href="qodana-yaml.md"><code>qodana.yaml</code></a> file. 
                            You can see that the native mode is already configured.</li>
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
  </tab>
</tabs>

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
      <img src="qc-report-example.png" dark-src="qc-report-example_dark.png" alt="Analysis report example" width="720" border-effect="line"/>
      <p>To learn more about %instance% report UI, see the <a href="ui-overview.md"/> section.</p>
    </tab>
</tabs> 


## Extend %product% configuration

### Adjusting the scope of analysis

Out of the box, Qodana provides two predefined profiles hosted on
[GitHub](https://github.com/JetBrains/qodana-profiles/tree/master/.idea/inspectionProfiles):

* `qodana.starter` is the default profile and a subset of the more comprehensive `qodana.recommended` profile,
* `qodana.recommended` is suitable for running in CI/CD pipelines and mostly implements the default %ide% profile, see the
  [%ide-a%](https://www.jetbrains.com/help/idea/customizing-profiles.html) documentation for details.

You can customize %product% profiles using configurations in [YAML](custom-profiles.md) and [XML](custom-xml-profiles.md) formats.

<!-- The example of profile configuring needs to be added here -->

To learn more about configuration basics, visit the [](override-a-profile.md) section. Complete guides are
available in the [](custom-profiles.md) and [](custom-xml-profiles.md) sections.

### Enabling the baseline

You can skip analysis for specific problems using the [baseline](baseline.topic) feature. Information about a baseline is contained
in a SARIF-formatted file.

<tabs group="native-container">
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
                          args: --ide,QDNET,--baseline,&lt;path/to/qodana.sarif.json&gt;
                        env:
                          QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
            </code-block>
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
                              // Uncomment the linter you would like to employ
                              // image '%qp-linter%' // Qodana for JVM
                              // image '%qp-co-linter%' // Qodana Community for JVM
                              // image '%qp-a-linter%' // Qodana Community for Android
                              // image '%qp-an-linter%' // Qodana for Android
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
              <code-block lang="yaml">
                  qodana:
                     image:
                      # Uncomment the linter you would like to employ
                      # name: %qp-linter% # Qodana for JVM
                      # name: %qp-co-linter% # Qodana Community for JVM
                      # name: %qp-a-linter% # Qodana Community for Android
                      # name: %qp-an-linter% # Qodana for Android
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
                     artifacts:
                        paths:
                           - qodana/report/
                        expose_as: 'Qodana report'
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
          <tab title="TeamCity" group-key="teamcity">
            <include from="teamcity.md" element-id="teamcity-add-a-qodana-runner"/>
            <p>More configuration examples are available in the <a href="teamcity.md"/>section.</p>
          </tab>
          <tab title="Command line" group-key="command-line">
              <p>Run this command in the project root directory:</p>
              <code-block lang="shell" prompt="$">
                  qodana scan \
                  &nbsp;&nbsp;&nbsp;--ide QDNET
              </code-block>
              <p>Here, the <code>--ide</code> option downloads and employs the JetBrains IDE binary file.</p>
              <p>Alternatively, in the <code>qodana.yaml</code> file save <code>ide: QDNET</code>, and then run %instance% 
                  using the following command:</p>
              <code-block lang="shell" prompt="$">
                  qodana scan
              </code-block>
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
                          <li>Options used by %product% and configured by the <a href="qodana-yaml.md"><code>qodana.yaml</code></a> file. 
                            You can see that the native mode is already configured.</li>
                           <li>The <a href="cloud-forward-reports.topic"><ui-path>Send inspection results to Qodana Cloud</ui-path></a> option 
                            using a <a href="cloud-projects.topic" anchor="cloud-manage-projects">project token</a>.</li>
                           <li>The <a href="baseline.topic"><ui-path>Use Qodana analysis baseline</ui-path></a> option to run %product% with a baseline.</li>
                        </list>
                     <img src="ide-plugin-dotnet-run-qodana.png" width="793" alt="Configuring Qodana in the Run Qodana dialog" border-effect="line"/>
                      <p>Click <ui-path>Run</ui-path> for analyzing your code.</p>
                  </step>
                  <step>
                     <p>In the <ui-path>Server-Side Analysis</ui-path> tool window, see the <a href="qodana-ide-plugin.md" anchor="ide-plugin-study-reports">inspection results</a>.</p>
                  </step>
              </procedure>
          </tab>
      </tabs>
  </tab>
  <tab title="Container mode" group-key="container-mode">
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
                    // Uncomment the linter you would like to employ
                    // image '%qp-linter%' // Qodana for JVM
                    // image '%qp-co-linter%' // Qodana Community for JVM
                    // image '%qp-a-linter%' // Qodana Community for Android
                    // image '%qp-an-linter%' // Qodana for Android
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
      <p>You can use the  <code>--baseline &lt;path/to/qodana.sarif.json&gt;</code> line in the <code>script</code> block to
      invoke the baseline feature.</p>
      <code-block lang="yaml">
        qodana:
           image:
            # Uncomment the linter you would like to employ
            # name: %qp-linter% # Qodana for JVM
            # name: %qp-co-linter% # Qodana Community for JVM
            # name: %qp-a-linter% # Qodana Community for Android
            # name: %qp-an-linter% # Qodana for Android
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
           artifacts:
              paths:
                 - qodana/report/
              expose_as: 'Qodana report'
      </code-block>
    </tab>
        <tab title="TeamCity" group-key="teamcity">
      <p>Based on the information from the <a anchor="jvm-run-qodana-teamcity">previous section</a>, use the <ui-path>Additional Qodana arguments</ui-path> field
      to configure the <a href="baseline.topic">baseline</a> feature by specifying the <code>--baseline &lt;path/to/qodana.sarif.json&gt;</code>
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
                   -l &lt;linter&gt; \
                   --baseline /data/base/&lt;path-relative-to-project-dir&gt;/qodana.sarif.json
            </code-block>
        </tab>
        <tab group-key="docker-image" title="Docker image">
            <code-block lang="shell" prompt="$">
                docker run \
                   -v &lt;source-directory&gt;/:/data/project/ \
                   -v &lt;path_to_baseline&gt;:/data/base/ \
                   -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                   &lt;linter&gt; \
                   --baseline /data/base/&lt;path-relative-to-project-dir&gt;/qodana.sarif.json
            </code-block>
        </tab>
    </tabs>
      <p>Here, <code>&lt;linter&gt;</code> denotes the following linters:</p>
        <table>
          <tr>
            <td>Image</td>
            <td>Linter</td>
          </tr>
          <tr>
            <td><code>%qp-linter%</code></td>
            <td>Qodana for JVM</td>
          </tr>
          <tr>
            <td><code>%qp-co-linter%</code></td>
            <td>Qodana Community for JVM</td>
          </tr>
          <tr>
            <td><code>%qp-a-linter%</code></td>
            <td>Qodana Community for Android</td>
          </tr>
          <tr>
            <td><code>%qp-an-linter%</code></td>
            <td>Qodana for Android</td>
          </tr>
        </table>
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
  </tab>
</tabs>


### Enabling the quality gate

Depending on the linter, you can configure the quality gate for: 

* The total number of project problems, available for all linters,
* Multiple quality gates for <a href="faq.topic" anchor="faq-severities">problem severities</a>, available for all linters,
* <a href="code-coverage.md">Code coverage</a> thresholds, available for the %qp% and %qp-an% linters.

You can configure [quality gates](quality-gate.topic) by saving this snippet to the [`qodana.yaml`](qodana-yaml.md) file:

```yaml
failureConditions:
  severityThresholds:
    any: 50 # Total number of problems in all severities
    critical: 1 # Severities
    high: 2
    moderate: 3
    low: 4
    info: 5
  testCoverageThresholds: # Only Qodana for JVM 
    fresh: 6 # Fresh code coverage
    total: 7 # Total percentage
```


### Analyzing pull requests

<tabs group="native-container">
  <tab title="Native mode" group-key="native-mode">
    <tabs group="software">
      <tab title="GitHub Actions" group-key="github">
        <procedure>
          <step>On the <ui-path>Settings</ui-path> tab of the GitHub UI, create the <code>QODANA_TOKEN</code>
            <a href="https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository">encrypted secret</a>
            and save the <a href="cloud-projects.topic" anchor="cloud-manage-projects">project token</a> as its value.
          </step>
          <step>On the <ui-path>Actions</ui-path> tab of the GitHub UI, set up a new workflow and create the
            <code>.github/workflows/code_quality.yml</code> file.</step>
          <step><p>Add this snippet to the <code>.github/workflows/code_quality.yml</code> file:</p>
            <code-block lang="yaml">
              &nbsp;&nbsp;&nbsp;&nbsp;name: Qodana
              &nbsp;&nbsp;&nbsp;&nbsp;on:
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;workflow_dispatch:
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pull_request:
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;push:
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;branches: # Specify your branches here
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- main # The 'main' branch
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 'releases/*' # The release branches
              &nbsp;&nbsp;&nbsp;&nbsp;jobs:
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qodana:
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;runs-on: ubuntu-latest
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;permissions:
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;contents: write
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pull-requests: write
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;checks: write
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;steps:
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- uses: actions/checkout@v3
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;with:
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ref: ${{ github.event.pull_request.head.sha }}  # to check out the actual pull request commit, not the merge commit
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fetch-depth: 0  # a full history is required for pull request analysis
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name: 'Qodana Scan'
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uses: JetBrains/qodana-action@v2024.2
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;env:
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
              </code-block>
          </step>
        </procedure>
      </tab>
      <tab title="GitLab CI/CD" group-key="gitlab">
        <p>In the root directory of your project, save the <code>.gitlab-ci.yml</code> file containing the following snippet:</p>
        <code-block lang="yaml">
         qodana:
           image:
            # Uncomment the linter you would like to employ
            # name: %qp-linter% # Qodana for JVM
            # name: %qp-co-linter% # Qodana Community for JVM
            # name: %qp-a-linter% # Qodana Community for Android
            # name: %qp-an-linter% # Qodana for Android
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
        <a href="%TeamCityPullRequests%">TeamCity</a> documentation portal.</p>
      </tab>
      <tab title="Command line" group-key="command-line">
        <p>To analyze changes in your code, employ the <code>--diff-start</code> option and specify a hash of the commit 
        that will act as a base for comparison:</p>
        <code-block lang="shell" prompt="$">
            docker run \
            &nbsp;&nbsp;&nbsp;-v $(pwd):/data/project/ \
            &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
            &nbsp;&nbsp;&nbsp;&lt;linter&gt; \
            &nbsp;&nbsp;&nbsp;--diff-start=&lt;GIT_START_HASH&gt;
        </code-block>
        <p>Here, <code>&lt;linter&gt;</code> denotes the following linters:</p>
        <table>
          <tr>
            <td>Image</td>
            <td>Linter</td>
          </tr>
          <tr>
            <td><code>%qp-linter%</code></td>
            <td>Qodana for JVM</td>
          </tr>
          <tr>
            <td><code>%qp-co-linter%</code></td>
            <td>Qodana Community for JVM</td>
          </tr>
          <tr>
            <td><code>%qp-a-linter%</code></td>
            <td>Qodana Community for Android</td>
          </tr>
          <tr>
            <td><code>%qp-an-linter%</code></td>
            <td>Qodana for Android</td>
          </tr>
        </table>
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
  </tab>
  <tab title="Container mode" group-key="container-mode">
  <tabs group="software">
    <tab title="GitHub Actions" group-key="github">
    <procedure>
      <step>On the <ui-path>Settings</ui-path> tab of the GitHub UI, create the <code>QODANA_TOKEN</code>
        <a href="https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository">encrypted secret</a>
        and save the <a href="cloud-projects.topic" anchor="cloud-manage-projects">project token</a> as its value.
      </step>
      <step>On the <ui-path>Actions</ui-path> tab of the GitHub UI, set up a new workflow and create the
        <code>.github/workflows/code_quality.yml</code> file.</step>
      <step><p>Add this snippet to the <code>.github/workflows/code_quality.yml</code> file:</p>
        <code-block lang="yaml">
          &nbsp;&nbsp;&nbsp;&nbsp;name: Qodana
          &nbsp;&nbsp;&nbsp;&nbsp;on:
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;workflow_dispatch:
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pull_request:
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;push:
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;branches: # Specify your branches here
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- main # The 'main' branch
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- 'releases/*' # The release branches
          &nbsp;&nbsp;&nbsp;&nbsp;jobs:
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qodana:
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;runs-on: ubuntu-latest
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;permissions:
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;contents: write
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pull-requests: write
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;checks: write
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;steps:
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- uses: actions/checkout@v3
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;with:
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ref: ${{ github.event.pull_request.head.sha }}  # to check out the actual pull request commit, not the merge commit
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fetch-depth: 0  # a full history is required for pull request analysis
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name: 'Qodana Scan'
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uses: JetBrains/qodana-action@v2024.2
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;env:
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
          </code-block>
      </step>
    </procedure>
  </tab>
    <tab title="GitLab CI/CD" group-key="gitlab">
    <p>In the root directory of your project, save the <code>.gitlab-ci.yml</code> file containing the following snippet:</p>
    <code-block lang="yaml">
     qodana:
       image:
        # Uncomment the linter you would like to employ
        # name: %qp-linter% # Qodana for JVM
        # name: %qp-co-linter% # Qodana Community for JVM
        # name: %qp-a-linter% # Qodana Community for Android
        # name: %qp-an-linter% # Qodana for Android
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
    <code-block lang="shell" prompt="$">
        docker run \
        &nbsp;&nbsp;&nbsp;-v $(pwd):/data/project/ \
        &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
        &nbsp;&nbsp;&nbsp;&lt;linter&gt; \
        &nbsp;&nbsp;&nbsp;--diff-start=&lt;GIT_START_HASH&gt;
    </code-block>
    <p>Here, <code>&lt;linter&gt;</code> denotes the following linters:</p>
    <table>
      <tr>
        <td>Image</td>
        <td>Linter</td>
      </tr>
      <tr>
        <td><code>%qp-linter%</code></td>
        <td>Qodana for JVM</td>
      </tr>
      <tr>
        <td><code>%qp-co-linter%</code></td>
        <td>Qodana Community for JVM</td>
      </tr>
      <tr>
        <td><code>%qp-a-linter%</code></td>
        <td>Qodana Community for Android</td>
      </tr>
      <tr>
        <td><code>%qp-an-linter%</code></td>
        <td>Qodana for Android</td>
      </tr>
    </table>
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
</tab>
</tabs>

## Supported technologies and features
{id="jvm-feature-matrix"}

<!-- This list needs to be re-checked -->

<table>
    <tr>
      <td>Support for</td>
      <td>Name</td>
      <td>%qp% and %qp-an%</td>
      <td>%qp-co%</td>
      <td>%qp-a%</td>  
    </tr>
    <tr>
        <td>Programming languages</td>
        <td>
            <p>Java</p>
            <p>Kotlin</p>
            <p>Groovy</p>
        </td>
        <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
        </td>
        <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
        </td>
        <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
        </td>
    </tr>
    <tr>
        <td>Frameworks and libraries</td>
        <td>
            <p>JavaBeans</p>
            <p>JUnit</p>
            <p>Lombok</p>
            <p>TestNG</p>
            <p>JPA</p>
            <p>Reactive&nbsp;Streams</p>
            <p>JavaFX</p>
            <p>Java EE</p>
            <p>JAX-RS</p>
            <p>JSP</p>
            <p>Spring</p>
        </td>
        <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&nbsp;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
        </td>
        <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
        </td>
        <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&nbsp;</p>
            <p>&#x2714;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&#x2714;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
        </td>
    </tr>
        <tr>
        <td>Databases and ORM</td>
        <td>
            <p>Hibernate ORM</p>
            <p>MongoDB</p>
            <p>Oracle</p>
            <p>MySQL</p>
            <p>PostgreSQL</p>
            <p>SQL</p>
            <p>SQL server</p>
        </td>
       <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
        </td>
        <td>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
        </td>
        <td>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
        </td>
    </tr>
    <tr>
        <td>Markup languages</td>
        <td>
            <p>CSS</p>
            <p>FreeMarker</p>
            <p>HTML</p>
            <p>JSON and JSON5</p>
            <p>RELAX NG</p>
            <p>XML</p>
            <p>XPath</p>
            <p>XSLT</p>
            <p>YAML</p>
            <p>TOML</p>
        </td>
        <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
        </td>
        <td>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
        </td>
        <td>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
        </td>
    </tr>
    <tr>
        <td>Scripting languages</td>
        <td>
            <p>Shell script</p>
            <p>Expression&nbsp;Language&nbsp;(EL)</p>
        </td>
       <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
        </td>
        <td>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
        </td>
       <td>
            <p>&#x2714;</p>
            <p>&nbsp;</p>
        </td>
    </tr>
    <tr>
        <td>Build management</td>
        <td>
            <p>Ant</p>
            <p>Gradle</p>
            <p>Maven</p>
        </td>
       <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
        </td>
       <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
        </td>
       <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
        </td>
    </tr>
    <tr>
      <td>%product% features</td>
      <td>
        <p><a href="baseline.topic">Baseline</a></p>
        <p><a href="quality-gate.topic">Quality gate</a></p>
        <p><a href="code-coverage.md">Code coverage</a></p>
        <p><a href="license-audit.topic">License audit</a></p>
        <p><a href="quick-fix.md">Quick-fix</a></p>
        <p><a href="vulnerability-checker.md">Vulnerability checker</a></p>
      </td>
      <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
      </td>
      <td>
         <p>&#x2714;</p>
         <p>&#x2714;</p>
         <p>&nbsp;</p>
         <p>&nbsp;</p>
         <p>&nbsp;</p>
         <p>&nbsp;</p>
      </td>
      <td>
         <p>&#x2714;</p>
         <p>&#x2714;</p>
         <p>&nbsp;</p>
         <p>&nbsp;</p>
         <p>&nbsp;</p>
         <p>&nbsp;</p>
      </td>
    </tr>
</table>
