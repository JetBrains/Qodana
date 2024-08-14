[//]: # (title: .NET)

<show-structure for="chapter" depth="3"/>

<var name="qp" value="Qodana for .NET"/>
<var name="qp-co" value="Qodana Community for .NET"/>
<var name="qp-linter" value="jetbrains/qodana-dotnet:2024.2-eap"/>
<var name="qp-co-linter" value="jetbrains/qodana-cdnet:2024.2-eap"/>
<var name="qd-image" value="jetbrains/qodana-&lt;dotnet/cdnet&gt;:2024.2&lt;-eap&gt;"/>
<var name="JenkinsCred" value="https://www.jenkins.io/doc/book/using/using-credentials/#adding-new-global-credentials"/>
<var name="ide" value="Rider"/>
<var name="ide-co" value="ReSharper"/>
<var name="Dplugin" value="https://plugins.jenkins.io/docker-plugin/"/>
<var name="DPplugin" value="https://plugins.jenkins.io/docker-workflow/"/>
<var name="Gplugin" value="https://plugins.jenkins.io/git/"/>
<var name="Dockeraccess" value="https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user"/>
<var name="MultipipeCreate" value="https://www.jenkins.io/doc/book/pipeline/multibranch/#creating-a-multibranch-pipeline"/>
<var name="dotsettings" value="https://www.jetbrains.com/help/resharper/Sharing_Configuration_Options.html#solution-team-shared-layer"/>
<var name="TeamCityProject" value="https://www.jetbrains.com/help/teamcity/configure-and-run-your-first-build.html#Create+your+first+project"/>
<var name="TeamCityBuildConfig" value="https://www.jetbrains.com/help/teamcity/creating-and-editing-build-configurations.html"/>
<var name="TeamCityBuildSteps" value="https://www.jetbrains.com/help/teamcity/configuring-build-steps.html"/>
<var name="TeamCityCommandLine" value="https://www.jetbrains.com/help/teamcity/command-line.html#General+Settings"/>
<var name="TeamCityPullRequests" value="https://www.jetbrains.com/help/teamcity/pull-requests.html"/>
<var name="TeamCityBranches" value="https://www.jetbrains.com/help/teamcity/configuring-finish-build-trigger.html#Trigger+Settings"/>
<var name="non-root-user" value="https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user"/>
<var name="rider-link" value="https://www.jetbrains.com/help/rider/Introduction.html"/>
<var name="rs-link" value="https://www.jetbrains.com/help/resharper/Introduction__Index.html"/>
<var name="tfms" value="https://learn.microsoft.com/en-us/dotnet/standard/frameworks#net-5-os-specific-tfms"/>
<var name="cpp-links" value="https://jetbrains.com/help/resharper/Introduction__Index.html#supported_langs"/>

<link-summary>You can analyze your .NET code using the %qp% and %qp-co% linters.</link-summary>

<p>All %product% linters are based on JetBrains IDEs designed for particular programming languages and frameworks. To analyze
.NET projects, you can use the following %product% linters:</p>

| Linter name | Based on                         | Licensed under the [licenses](pricing.md)  | Shipped as                                             | [Supported languages](#dotnet-feature-matrix)            |
|-------------|----------------------------------|--------------------------------------------|--------------------------------------------------------|----------------------------------------------------------|
| %qp%        | [JetBrains Rider](%rider-link%)  | Ultimate and Ultimate Plus                 | A [native solution](native-mode.md) and a Docker image | C#, [C/C++](%cpp-links%), VB.NET, JavaScript, TypeScript 
| %qp-co%     | [JetBrains ReSharper](%rs-link%) | Community                                  | A Docker image                                         | C#, [C++](%cpp-links%), VB.NET                           |


<p>You can compare these linters by programming languages and other supported technologies by navigating to the <a anchor="dotnet-feature-matrix">feature matrix</a>.</p>

## Before your start
{id="dotnet-before-you-start"}

### Qodana Cloud
{id="dotnet-before-you-start-qodana-cloud"}

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

A project token is required for the %qp% linter and optional for the %qp-co% linter.

### SDK version
{id="dotnet-sdk-version"}

If you project targets the .NET framework or [OS-specific TFMs](%tfms%), the only option in this case is to run the
%qp% linter in the [native mode](native-mode.md).

If you run %qp% in the native mode, you should install the SDK to the default location in your operating system so that 
%ide% can have access to it.

<!-- This table should be made for both linters -->
The Dockerized version of %qp% provides versions 6.0, 7.0, and 8.0 of SDK.

<p>All SDK versions are stored in the <code>/usr/share/dotnet/sdk</code> directory of the 
    %product% container filesystem.</p>

<!-- This needs to be moved to a Dockerized version of a linter -->

<p>In case a project requires a different version of the SDK, you can set it  using the
<a href="before-running-qodana.md"><code>bootstrap</code></a> key in the <code>qodana.yaml</code> file.
For example, this command will install the required version of the SDK that is specified in the
<code>global.json</code> file and located in the root of your project:</p>

<code-block lang="yaml">
    bootstrap: curl -fsSL https://dot.net/v1/dotnet-install.sh |
      bash -s -- --jsonfile /data/project/global.json -i /usr/share/dotnet
</code-block>


### Prepare your software
{id="dotnet-software-prerequisites"}

This shows how to configure software from this section to %product% analysis. All configuration samples
use a [project token](project-token.md), see the [](#dotnet-before-you-start-qodana-cloud) for details.

<tabs group="software">
    <tab title="GitHub Actions" group-key="github">
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
                             with:
                               # args: --linter,%qp-linter%
                               # args: --linter,%qp-co-linter% 
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
              <a href="project-token.md">project token</a> as its value.
            </step>
            <step>
              <p>In Jenkins, create a Multibranch Pipeline project as described on the <a href="%MultipipeCreate%">Jenkins documentation portal</a>.</p>
            </step>
        </procedure>
    </tab> 
    <tab title="GitLab CI/CD" group-key="gitlab">
        <procedure>
            <step><p>Make sure that your project repository is accessible by GitLab CI/CD.</p></step>
            <step>In GitLab CI/CD, create the <a href="https://docs.gitlab.com/ee/ci/variables/"><code>$qodana_token</code></a> 
            variable and save the <a href="project-token.md">project token</a> as its value.</step>
        </procedure>
    </tab>
    <tab title="TeamCity" group-key="teamcity">
        <p>In TeamCity, Create a 
        <a href="https://www.jetbrains.com/help/teamcity/configure-and-run-your-first-build.html#Create+your+first+project">project</a> 
        and a <a href="https://www.jetbrains.com/help/teamcity/creating-and-editing-build-configurations.html">build configuration</a>.</p>
    </tab>
    <tab title="Command line" group-key="command-line">
        <p>Install Docker on the machine were you are going to run %product%.</p>  
        <p>If you are using Linux, you should be able to run Docker under your current <a href="%non-root-user%">non-root user</a>.</p>
      <tabs group="cli-settings">
          <tab group-key="qodana-cli" title="Qodana CLI">
              <p>Follow the instructions from the
              <a href="https://github.com/JetBrains/qodana-cli">Qodana CLI</a> page on GitHub.</p>
          </tab>
          <tab group-key="docker-image" title="Docker image">
            <p>Run this command to pull the Docker image of the %qp% or %qp-co% linters:</p>
            <tabs group="linter-tabs">
                <tab group-key="linter-tabs-dotnet" title="%qp%">
                    <code-block lang="shell" prompt="$">
                        docker pull %qp-linter%
                    </code-block>
                </tab>
                <tab group-key="linter-tabs-cdnet" title="%qp-co%">
                    <code-block lang="shell" prompt="$">
                        docker pull %qp-co-linter%
                    </code-block>
                </tab>
            </tabs>
          </tab>
      </tabs>
    </tab>
</tabs>

## Build the project
{id="dotnet-build-project"}

<tabs group="linter-tabs">
    <tab group-key="linter-tabs-dotnet" title="%qp%">
        <p>We recommend that you build a project before %product% analyzes it. To build it, you can use the 
        <a href="before-running-qodana.md"><code>bootstrap</code></a> key 
        of the <a href="qodana-yaml.md"><code>qodana.yaml</code></a> file contained in your project directory. This is especially 
        recommended if you employ source generators.</p>
        <p>If the project build fails, code analysis cannot be performed.</p>
    </tab>
    <tab group-key="linter-tabs-cdnet" title="%qp-co%">
        <p>The %qp-co% linter builds your project by default before analysis. If you wish to run your custom build, use the 
        <code>--no-build</code> %product% option:</p>
        <tabs group="software">
            <tab title="GitHub Actions" group-key="github">
                <p>Use this workflow configuration to invoke the <code>--no-build</code> option:</p>
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
                                args: --no-build
                            env:
                              QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
                </code-block>
            </tab>
            <tab title="Jenkins" group-key="jenkins">
                <p>In the root directory of your project repository, save this configuration to the <code>Jenkinsfile</code>:</p>
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
                                image '%qp-co-linter%'
                            }
                        }
                        stages {
                            stage('Qodana') {
                                steps {
                                    sh '''
                                    qodana \
                                    --no-build
                                    '''
                                }
                            }
                        }
                    }
                </code-block>
            </tab>
            <tab title="GitLab CI/CD" group-key="gitlab">
                <code-block lang="yaml">
                    qodana:
                       image:
                          name: %qp-co-linter%
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
                          - qodana --cache-dir=$CI_PROJECT_DIR/.qodana/cache --no-build
                       artifacts:
                          paths:
                             - qodana/report/
                          expose_as: 'Qodana report'
                </code-block>
            </tab>
            <tab title="TeamCity" group-key="teamcity">
                <include from="lib_qd.topic" element-id="teamcity-add-a-qodana-runner" filter="empty,dotnet-no-build"/>
            </tab>
            <tab title="Command line" group-key="command-line">
                <tabs>
                    <tab title="Qodana CLI">
                        <code-block lang="shell" prompt="$">
                          qodana scan \
                          &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                          &nbsp;&nbsp;&nbsp;%qp-co-linter% \
                          &nbsp;&nbsp;&nbsp;--no-build
                        </code-block>
                    </tab>
                    <tab title="Docker image" prompt="$">
                        <code-block lang="shell" prompt="$">
                          docker run \
                          &nbsp;&nbsp;&nbsp;-v &lt;source-directory&gt;/:/data/project/ \
                          &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                          &nbsp;&nbsp;&nbsp;%qp-co-linter% \
                          &nbsp;&nbsp;&nbsp;--no-build
                        </code-block>
                    </tab>
                </tabs>
            </tab>
        </tabs>
    </tab>
</tabs>

## Run %product%
{id="dotnet-run-qodana"}

<note><include from="lib_qd.topic" element-id="docker-ram-note"/></note>

<include from="lib_qd.topic" element-id="root-and-non-root-users-info-bubble"></include>

> Before running %product%, make sure that you [prepared](#dotnet-before-you-start) and [built](#dotnet-build-project) your project.
> {style="note"}

<tabs group="linter-tabs">
    <tab group-key="linter-tabs-dotnet" title="%qp%">
      <p>You can run the %qp% linter in two modes:</p>
      <list>
        <li>The <a href="native-mode.md">native mode</a> is the recommended method for running the %qp% linter that lets you run 
        the linter without using Docker containers,</li>
        <li>Container mode is an alternative that involves Docker containers of the %qp% linter.</li>
      </list>
      <tabs>
        <tab title="Native mode">
          <note>
            If you plan to use private NuGet feeds, we recommend running the native mode on the same machine where
            you build a project because this can guarantee that %instance% has access to private NuGet feeds.
          </note>
          <snippet id="dotnet-run-qodana-native-mode-yaml">
            <p>Using a YAML configuration is the preferred method of configuring the linter because it lets you use such configuration
                across all software that runs %product% without additional configuration.</p>
                <p>You can configure the native mode by adding this line to the <a href="qodana-yaml.md"><code>qodana.yaml</code></a> file:</p>
            <code-block lang="yaml">
                ide: QDNET
            </code-block>
          </snippet>
            <p>Alternatively, you can implement the native mode configuration as shown in examples below.</p>
            <tabs group="software">
                <tab title="GitHub Actions" group-key="github">
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
                </tab>
<!--                <tab title="Jenkins" group-key="jenkins">
                    <p>In the root directory of your project repository, save this snippet to the <code>Jenkinsfile</code>:</p>
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
                </tab>
                <tab title="GitLab CI/CD" group-key="gitlab">
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
                           artifacts:
                              paths:
                                 - qodana/report/
                              expose_as: 'Qodana report'
                    </code-block>
                </tab>
                <tab title="TeamCity" group-key="teamcity">
                    <p>See the <a anchor="dotnet-software-prerequisites"/> section for details.</p>
                </tab>-->
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
        <tab title="Container mode">
            <p>The container mode is available for the %qp% linter; however, we recommend that you use the native mode.</p>
            <tabs>
                <tab title="GitHub Actions" group-key="github">
                          <p>To analyze the <code>main</code> branch, release branches and the pull requests coming
                            to your repository in the container mode, save this workflow configuration to the 
                            <code>.github/workflows/code_quality.yml</code> file:</p>
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
                <tab title="Jenkins" group-key="jenkins">
                    <p>In the root directory of your project repository, save the <code>Jenkinsfile</code> containing 
                        the following configuration:</p>
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
                </tab>
                <tab title="GitLab CI/CD" group-key="gitlab">
                    <p>In the root directory of your project, create the <code>.gitlab-ci.yml</code> and save the 
                    following configuration in it:</p>
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
                           artifacts:
                              paths:
                                 - qodana/report/
                              expose_as: 'Qodana report'
                    </code-block>
                </tab>
                <tab title="TeamCity" group-key="teamcity">
                  <include from="lib_qd.topic" element-id="teamcity-add-a-qodana-runner" use-filter="empty,dotnet"/>
                </tab>
                <tab title="Command line" group-key="command-line">
                    <p>Start local analysis with <code>source-directory</code>
                        pointing to the root of your project and
                        <code>QODANA_TOKEN</code> referring to the <a href="project-token.md">project token</a>:</p>
                    <code-block lang="shell" prompt="$">
                        docker run \
                        &nbsp;&nbsp;&nbsp;-v &lt;source-directory&gt;/:/data/project/ \
                        &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                        &nbsp;&nbsp;&nbsp;%qp-linter%
                    </code-block>
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
                                    Here, comment out the line containing <code>ide: QDNET</code>.</li>
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
      </tabs>
    </tab>
    <tab group-key="linter-tabs-cdnet" title="%qp-co%">
        <p>You can run the %qp-co% linter in a container mode as shown in the examples below.</p>
            <tabs group="software">
                <tab title="GitHub Actions" group-key="github">
                        To analyze the <code>main</code> branch, release branches and the pull requests coming
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
                </tab>
                <tab title="Jenkins" group-key="jenkins">
                    <p>In the root directory of your project repository, save this snippet to the <code>Jenkinsfile</code>:</p>
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
                                    image '%qp-co-linter%'
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
                </tab>
                <tab title="GitLab CI/CD" group-key="gitlab">
                    <p>In the root directory of your project, create the <code>.gitlab-ci.yml</code> and save the 
                        following configuration in it:</p>
                    <code-block lang="yaml">
                        qodana:
                           image:
                              name: %qp-co-linter%
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
                </tab>
                <tab title="TeamCity" group-key="teamcity">
                  <include from="lib_qd.topic" element-id="teamcity-add-a-qodana-runner" use-filter="empty,dotnet-co"/>
                </tab>
                <tab title="Command line" group-key="command-line">
                    <p>Start local analysis with <code>source-directory</code>
                        pointing to the root of your project and
                        <code>QODANA_TOKEN</code> referring to the <a href="project-token.md">project token</a>:</p>
                    <code-block lang="shell" prompt="$">
                        docker run \
                        &nbsp;&nbsp;&nbsp;-v &lt;source-directory&gt;/:/data/project/ \
                        &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                        &nbsp;&nbsp;&nbsp;%qp-co-linter%
                    </code-block>
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
</tabs>

### Analyze a specific solution

By default, %product% tries to locate and employ a single solution file, or, if no solution file is present,
it tries to find a project file. If your project contains multiple solution files, you need to specify the exact
filename as shown below.

<tabs group="dotnet-solutions">
    <tab id="specify-solution" title="Specify a solution">
        <p>You can specify a solution in various ways. Using a <a href="qodana-yaml.md">YAML</a> configuration is the most
        convenient method because you can configure it once and use the configuration across all software 
        that runs %product%. Alternatively, you can use Docker options.</p>
        <tabs group="specify-solution-options">
            <tab id="specify-solution-yaml" title="YAML file">
                <p>Specify the relative path to the solution file from the project root:</p>
                <code-block lang="yaml">
                    dotnet:
                    &nbsp;&nbsp;solution: &lt;relative-path-to-solution-file&gt;
                </code-block>
                <p>If your project contains no solution files and multiple project files, you need to employ a project file:</p>
                <code-block lang="yaml">
                    dotnet:
                    &nbsp;&nbsp;project: &lt;relative-path-to-project-file&gt;
                </code-block>
            </tab>
            <tab id="specify-solution-docker" title="Docker">
                <p>The %qp% linter uses the <code>--property</code> option, while the %qp-co% linter uses the 
                    <code>--solution</code> and <code>--project</code> options to specify a path to a solution file:
                </p>
                <tabs group="linter-tabs">
                  <tab title="%qp%" group-key="linter-tabs-dotnet">
                    <code-block lang="shell">
                      docker run \
                      &nbsp;&nbsp;&nbsp;-v &lt;source-directory&gt;/:/data/project/ \
                      &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                      &nbsp;&nbsp;&nbsp;%qp-linter% \
                      &nbsp;&nbsp;&nbsp;--property=qodana.net.solution=&lt;relative-path-to-solution-file&gt;
                    </code-block>
                  </tab>
                  <tab title="%qp-co%" group-key="linter-tabs-cdnet">
                    <code-block lang="shell">
                      docker run \
                      &nbsp;&nbsp;&nbsp;-v &lt;source-directory&gt;/:/data/project/ \
                      &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                      &nbsp;&nbsp;&nbsp;%qp-co-linter% \
                      &nbsp;&nbsp;&nbsp;--solution=&lt;relative-path-to-solution-file&gt;
                    </code-block>
                    </tab>
                </tabs>
                <p>If your project contains no solution files and multiple project files, you need to employ a project file 
                    using the <code>--property</code> and <code>--project</code> options:
                </p>
                <tabs group="linter-tabs">
                    <tab title="%qp%" group-key="linter-tabs-dotnet">
                        <code-block lang="shell">
                            docker run \
                            &nbsp;&nbsp;&nbsp;-v &lt;source-directory&gt;/:/data/project/ \
                            &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                            &nbsp;&nbsp;&nbsp;%qp-linter% \
                            &nbsp;&nbsp;&nbsp;--property=qodana.net.project=&lt;relative-path-to-project-file&gt;
                        </code-block>
                    </tab>
                    <tab title="%qp-co%" group-key="linter-tabs-cdnet">
                        <code-block lang="shell">
                            docker run \
                            &nbsp;&nbsp;&nbsp;-v &lt;source-directory&gt;/:/data/project/ \
                            &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                            &nbsp;&nbsp;&nbsp;%qp-co-linter% \
                            &nbsp;&nbsp;&nbsp;--project=&lt;relative-path-to-project-file&gt;
                        </code-block>
                    </tab>
                </tabs>
            </tab>
        </tabs>
    </tab>
    <tab id="configure-solution" title="Configure a solution">
        <p>A solution configuration defines which projects in the solution to build, and which project configurations to 
            use for specific projects within the solution.
        </p>
        <p>
            Every solution contains the <code>Debug</code> and <code>Release</code> configurations that you can employ 
            as shown below.
        </p>
        <tabs id="configure-solution-options">
            <tab id="configure-solution-yaml" title="YAML file">
                <p>You can switch configurations of the current solution in the <code>qodana.yaml</code> file:</p>
                <code-block lang="yaml">
                    dotnet:
                    &nbsp;&nbsp;configuration: Release
                </code-block>
                <p>
                    By default, the solution platform is set to <code>Any CPU</code>, and you can override it, for example:
                </p>
                <code-block lang="yaml">
                    dotnet:
                    &nbsp;&nbsp;platform: x86
                </code-block>
            </tab>
            <tab id="configure-solution-docker" title="Docker">
                <p>
                    You can apply a configuration using the <code>--property</code> and <code>--configuration</code> options:
                </p>
                <tabs group="linter-tabs">
                    <tab title="%qp%" group-key="linter-tabs-dotnet">
                        <code-block lang="shell">
                            docker run \
                            &nbsp;&nbsp;&nbsp;-v &lt;source-directory&gt;/:/data/project/ \
                            &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                            &nbsp;&nbsp;&nbsp;%qp-linter% \
                            &nbsp;&nbsp;&nbsp;--property=qodana.net.configuration=Release
                        </code-block>
                    </tab>
                    <tab title="%qp-co%" group-key="linter-tabs-cdnet">
                        <code-block lang="shell">
                            docker run \
                            &nbsp;&nbsp;&nbsp;-v &lt;source-directory&gt;/:/data/project/ \
                            &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                            &nbsp;&nbsp;&nbsp;%qp-co-linter% \
                            &nbsp;&nbsp;&nbsp;--configuration=Release
                        </code-block>
                    </tab>
                </tabs>
                <p>
                    By default, the solution platform is set to <code>Any CPU</code>, and you can override it as shown below:
                </p>
                <tabs group="linter-tabs">
                    <tab title="%qp%" group-key="linter-tabs-dotnet">
                        <code-block lang="shell">
                            docker run \
                            &nbsp;&nbsp;&nbsp;-v &lt;source-directory&gt;/:/data/project/ \
                            &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                            &nbsp;&nbsp;&nbsp;%qp-linter% \
                            &nbsp;&nbsp;&nbsp;--property=qodana.net.platform=x86
                        </code-block>
                    </tab>
                    <tab title="%qp-co%" group-key="linter-tabs-cdnet">
                        <code-block lang="shell">
                            docker run \
                            &nbsp;&nbsp;&nbsp;-v &lt;source-directory&gt;/:/data/project/ \
                            &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                            &nbsp;&nbsp;&nbsp;%qp-co-linter% \
                            &nbsp;&nbsp;&nbsp;--platform=x86
                        </code-block>
                    </tab>
                </tabs>
            </tab>
        </tabs>
    </tab>
</tabs>

### Private NuGet repositories

Depending on the linter, you can run them using private NuGet repositories as shown below.

<tabs group="linter-tabs">
    <tab title="%qp%" group-key="linter-tabs-dotnet">
        <p>If you run %qp% using private NuGet repositories, the native mode of this linter is the recommended method of running. 
        In this case, you do not have to additionally configure the linter, and if you run it on the same machine where you have 
        built the project, it will be able to have access to the same feeds. </p>
        <p>Alternatively, use this configuration to employ a Docker image of the %qp% linter:</p>
        <code-block lang="shell" prompt="$">
            docker run \
            &nbsp;&nbsp;&nbsp;-v &lt;source-directory&gt;/:/data/project/ \
            &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
            &nbsp;&nbsp;&nbsp;-e QODANA_NUGET_URL=&lt;private-NuGet-feed-URL&gt; \
            &nbsp;&nbsp;&nbsp;-e QODANA_NUGET_USER=&lt;login&gt; \
            &nbsp;&nbsp;&nbsp;-e QODANA_NUGET_PASSWORD=&lt;plaintext-password&gt; \
            &nbsp;&nbsp;&nbsp;%qp-linter% \
        </code-block>
        <p>Another method is to add credentials to the <code>nuget.config</code> file before analyzing a project. You can 
            do this by executing a NuGet source update using: </p>
        <code-block>
            -Name "MySourceName” -username "User" -password "Password" -configFile "pathToNugetConfigInRepo"
        </code-block>
        <p>Other configuration examples are available on our <a href="https://github.com/qodana/qodanaprivateFeed/">GitHub repository</a>.</p>
    </tab>
    <tab title="%qp-co%" group-key="linter-tabs-cdnet">
        <p>Add credentials to the <code>nuget.config</code> file before analyzing a project. You can do this by 
        executing a NuGet source update using: </p>
        <code-block>
            -Name "MySourceName” -username "User" -password "Password" -configFile "pathToNugetConfigInRepo"
        </code-block>
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
      <img src="dotnet-report-example.png" alt="Analysis report example" width="720" border-effect="line"/>
      <p>To learn more about %instance% report UI, see the <a href="ui-overview.md"/> section.</p>
    </tab>
</tabs> 


## Extend the configuration
{id="dotnet-extend-configuration"}

### Adjusting the scope of analysis

<tabs group="linter-tabs">
        <tab group-key="linter-tabs-dotnet" title="%qp%">
            <p>Out of the box, Qodana provides two predefined profiles hosted on
                <a href="https://github.com/JetBrains/qodana-profiles/tree/master/.idea/inspectionProfiles">GitHub</a>.
            The <code>qodana.starter</code> profile is the default profile and a subset of the more comprehensive 
                <code>qodana.recommended</code> profile that in turn is suitable for running in CI/CD pipelines and mostly 
                implements the default %ide% profile.
            </p>
            <tip>You can customize %product% profiles using configurations in <a href="custom-profiles.md">YAML</a> and 
                <a href="custom-xml-profiles.md">XML</a> formats. To learn more about configuration basics, visit the <a href="override-a-profile.md"/> section.
            </tip>
            <p>%qp% reads configuration from the <a href="qodana-yaml.md"><code>qodana.yaml</code></a> file located in the 
                root directory of your project. For example, add this configuration to run the linter using the 
                <a href="inspection-profiles.md"><code>qodana.recommended</code></a> inspection profile:
            </p>
            <code-block lang="yaml">
                version: "1.0"
                profile:
                    name: qodana.recommended
            </code-block>
            <p>You can analyze your code using Roslyn analyzers with each analyzer considered as a separate 
                inspection. This is an experimental feature, so use them at your own risk.</p>
            <p>To disable Roslyn analyzers, you can <a href="custom-profiles.md">configure the %instance% profile</a> using
                the <code>qodana.yaml</code> file, for example:</p>
            <code-block lang="yaml">
                name: "Custom profile"
                &nbsp;
                baseProfile: qodana.starter
                &nbsp;
                groups: # List of configured groups
                - groupId: InspectionsToExclude
                  groups:
                    - "category:C#/Roslyn Analyzers"
                &nbsp;
                inspections: # Group invocation
                - group: InspectionsToExclude
                  enabled: false # Disable the InspectionsToExclude group
            </code-block>            
            <p>Configuration examples are available 
                <a href="https://github.com/hybloid/fluentassertions/blob/develop/qodana.yaml">on GitHub</a>.
            </p>
            <p>If you are familiar with configuring code analysis via 
               <a href="https://www.jetbrains.com/help/rider/Code_Analysis__Code_Inspections.html">%ide% inspection profiles</a>, 
                    you can pass the reference to the existing profile by mapping the profile:</p>
            <code-block lang="shell" prompt="$">
                docker run \
                &nbsp;&nbsp;&nbsp;-v $(pwd):/data/project/ \
                &nbsp;&nbsp;&nbsp;-v $(pwd)/.qodana/&lt;inspection-profile.xml&gt;:/data/project/myprofiles/&lt;inspection-profile.xml&gt; \
                &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                &nbsp;&nbsp;&nbsp;%qp-linter% \
                &nbsp;&nbsp;&nbsp;--profile-path /data/project/myprofiles/&lt;inspection-profile.xml&gt;
            </code-block>
        </tab>
        <tab group-key="linter-tabs-cdnet" title="%qp-co%">
            <p>If you have previously worked on the target solution with ReSharper, you may have already
                <a href="https://www.jetbrains.com/help/resharper/Code_Analysis__Configuring_Warnings.html">configured code inspections settings</a>.
                If so, InspectCode will find your <a href="https://www.jetbrains.com/help/resharper/Sharing_Configuration_Options.html">custom settings</a>
                in <code>.DotSettings</code> files and apply them. If there are no settings files, then the default severity levels will be used
                for all analyses. Besides custom severity levels for code inspections, InspectCode will look for the following settings in
                <code>.DotSettings</code> files:
            </p>
            <list>
                <li>Whether the solution-wide analysis is enabled.</li>
                <li><a href="https://www.jetbrains.com/help/resharper/Coding_Assistance__Naming_Style.html">Naming rules</a> (this can only be configured using <code>.DotSettings</code> files).</li>
                <li><a href="https://www.jetbrains.com/help/resharper/Code_Analysis__Configuring_Warnings.html#exclude_items">Files, folders, and file masks excluded from code analysis</a>.</li>
                <li><a href="https://www.jetbrains.com/help/resharper/Code_Analysis__Configuring_Warnings.html#exclude_generated">Files, file masks, and regions with generated code, where the code analysis is partly disabled</a> (this can only be configured using <code>.DotSettings</code> files).</li>
                <li>A place where the code analysis engine should store caches. You can specify it on the <ui-path>Environment | General</ui-path> page of ReSharper options.</li>
                <li>Target languages (<ui-path>ReSharper | Options | Environment | Products — Features</ui-path>).</li>
            </list>
            <p>To configure InspectCode on a CI server, make all configurations locally with ReSharper, save the settings to the
                <a href="https://www.jetbrains.com/help/resharper/Sharing_Configuration_Options.html#saveTo">Solution Team-Shared layer</a>,
                and then commit the resulting <code>YourSolution.sln.DotSettings</code> file in the solution directory to your VCS. 
                InspectCode on the server will find and apply these settings.
            </p>
            <p>By default, InspectCode also runs Roslyn analyzers on the target solution. To disable Roslyn analyzers, in the 
                solution <code>.DotSettings</code> file add the following configuration:
            </p>
            <code-block lang="xml">
                &lt;wpf:ResourceDictionary xml:space="preserve"
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;xmlns:s="clr-namespace:System;assembly=mscorlib"
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;xmlns:ss="urn:shemas-jetbrains-com:settings-storage-xaml"
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;xmlns:wpf="http://schemas.microsoft.com/winfx/2006/xaml/presentation"&gt;
                &nbsp;
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;!-- Enable/disable Roslyn analyzers and Source Generators --&gt;
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;s:Boolean x:Key="/Default/CodeInspection/Roslyn/RoslynEnabled/@EntryValue"&gt;False&lt;/s:Boolean&gt;
                &nbsp;
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;!-- Include/exclude Roslyn analyzers in Solution-Wide Analysis --&gt;
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;s:Boolean x:Key="/Default/CodeInspection/Roslyn/UseRoslynInSwea/@EntryValue"&gt;False&lt;/s:Boolean&gt;
                &nbsp;
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;/wpf:ResourceDictionary&gt;
            </code-block>
        </tab>
</tabs>

### Using EditorConfig
{id="dotnet-extend-configuration-editorconfig"}

<p>If you use <a href="https://www.jetbrains.com/help/resharper/Using_EditorConfig.html">EditorConfig</a> to
    maintain code styles for your project, you can also configure code inspections from
    <code>.editorconfig</code> files.</p>

<p>As EditorConfig convention suggests, InspectCode will apply inspection settings defined in files named
    <code>.editorconfig</code> in the directory of the current file and in all its parent directories until
    it reaches the root filepath or finds an EditorConfig file with <code>root=true</code>. File masks specified in
    <code>.editorconfig</code> files, for example <code>*Test.cs</code> are also taken into account.</p>

<p>Inspection settings in <code>.editorconfig</code> files are configured similarly to other properties —
    by adding the corresponding lines:</p>

<code-block lang="shell">
    [inspection_property]=[error | warning | suggestion | hint | none]
</code-block>

<p>For example, you can change the
    <a href="https://www.jetbrains.com/help/resharper/Code_Analysis__Code_Inspections.html#severity">severity level</a>
    of the <code>Possible 'System.NullReferenceException'</code> inspection to <code>Error</code> with the
    following line:</p>

<code-block lang="shell">
    resharper_possible_null_reference_exception_highlighting=error
</code-block>

<p>or you can disable the <code>Redundant argument with default value</code> inspection with the following line:</p>

<code-block lang="shell">
    resharper_redundant_argument_default_value_highlighting=none
</code-block>

<tip>Inspection settings from <code>.editorconfig</code> files have higher priority than the settings
    configured on the <ui-path>Code Inspection | Inspection Severity</ui-path> page of InspectCode options.</tip>

<p>You can find EditorConfig property for each inspection on pages in the
    <a href="https://www.jetbrains.com/help/resharper/Reference_Code_Inspection_Index.html">Code inspection index</a>
    section as well as on the
    <a href="https://www.jetbrains.com/help/resharper/EditorConfig_Index.html">Index of EditorConfig properties</a> page. —
    just use the browser search to find the property for the desired inspection.</p>

### Enabling the baseline

You can skip analysis for specific problems using the [baseline](baseline.topic) feature. Information about a baseline is contained
in a SARIF-formatted file.

<tabs group="linter-tabs">
        <tab group-key="linter-tabs-dotnet" title="%qp%">
            <p>Select how you would like to run the %qp% linter with the <a href="baseline.topic">baseline</a> feature:</p>
            <tabs group="native-container">
                <tab title="Native mode" group-key="native-mode">
            <p>You can run the %qp% linter in the 
                <a href="native-mode.md">native mode</a>:</p>
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
                                        args: --ide,&lt;QDNET&gt;,--baseline,&lt;path/to/qodana.sarif.json&gt;
                                      env:
                                        QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
                          </code-block>
                        </tab>
                        <tab title="Command line" group-key="command-line">
                            <p>Run this command in the project root directory:</p>
                            <code-block lang="shell" prompt="$">
                                qodana scan \
                                &nbsp;&nbsp;&nbsp;--ide &lt;QDNET&gt; \
                                &nbsp;&nbsp;&nbsp;--baseline &lt;path/to/qodana.sarif.json&gt;
                            </code-block>
                            <p>Here, the <code>--baseline,&lt;path/to/qodana.sarif.json&gt;</code> option specifies the <a href="baseline.topic">baseline</a> feature.</p>
                            <p>Alternatively, in the <code>qodana.yaml</code> file save <code>ide: &lt;QDNET&gt;</code>, and then run %instance% 
                                using the following command:</p>
                            <code-block lang="shell" prompt="$">
                                qodana scan \
                                &nbsp;&nbsp;&nbsp;--baseline &lt;path/to/qodana.sarif.json&gt;
                            </code-block>
                            <p>In your browser, open <a href="https://qodana.cloud">Qodana Cloud</a> to examine analysis results and
                              reconfigure the analysis, see the <a href="ui-overview.md"/> section for
                              details.</p>
                        </tab>
                    </tabs>
                </tab>
                <tab title="Container mode" group-key="container-mode">
            <p>Select how you would like to run the <a href="baseline.topic">baseline</a> feature in the 
                container mode:</p>
                    <tabs group="software">
                        <tab title="GitHub Actions" group-key="github">
                          <p>This snippet contains the <code>args: --baseline,qodana.sarif.json</code> line that 
                            specifies the path to the SARIF-formatted baseline file:</p>
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
                                        args: --baseline,&lt;path/to/qodana.sarif.json&gt;,--linter,%qp-linter%
                                      env:
                                        QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
                          </code-block>
                        </tab>
                        <tab title="Jenkins" group-key="jenkins">
                          <p>In the root directory of your project repository, save the <code>Jenkinsfile</code> containing the 
                          <code>--baseline &lt;path/to/qodana.sarif.json&gt;</code> line that specifies the path to the SARIF-formatted baseline file:</p>
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
                          <p>The <code>--baseline &lt;path/to/qodana.sarif.json&gt;</code> line in the <code>script</code> 
                            block invokes the baseline feature:</p>
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
                            <include from="lib_qd.topic" element-id="teamcity-add-a-qodana-runner" use-filter="empty,dotnet,baseline"/>
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
                </tab>
            </tabs>
        </tab>
        <tab group-key="linter-tabs-cdnet" title="%qp-co%">
            <p>Select how you would like to run the %qp-co% linter with the <a href="baseline.topic">baseline</a> feature:</p>
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
                                args: --baseline,&lt;path/to/qodana.sarif.json&gt;,--linter,%qp-co-linter%
                              env:
                                QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
                  </code-block>
                </tab>
                <tab title="Jenkins" group-key="jenkins">
                  <p>In the root directory of your project repository, save the <code>Jenkinsfile</code> containing the 
                  <code>--baseline &lt;path/to/qodana.sarif.json&gt;</code> line that specifies the path to the SARIF-formatted baseline file:</p>
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
                                image '%qp-co-linter%'
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
                          name: %qp-co-linter% 
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
                    <include from="lib_qd.topic" element-id="teamcity-add-a-qodana-runner" use-filter="empty,dotnet-co,baseline"/>
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
        </tab>
</tabs>

### Enabling the quality gate

<tabs group="linter-tabs">
    <tab group-key="linter-tabs-dotnet" title="%qp%">
        <p>You can configure <a href="quality-gate.topic">quality gates</a> for the total number of project problems, 
            specific problem severities, and code coverage by saving this snippet to the 
            <a href="qodana-yaml.md"><code>qodana.yaml</code></a> file:
        </p>
        <code-block lang="yaml">
            failureConditions:
            &nbsp;&nbsp;severityThresholds:
            &nbsp;&nbsp;&nbsp;&nbsp;any: 50 # Total number of problems in all severities
            &nbsp;&nbsp;&nbsp;&nbsp;critical: 1 # Severities
            &nbsp;&nbsp;&nbsp;&nbsp;high: 2
            &nbsp;&nbsp;&nbsp;&nbsp;moderate: 3
            &nbsp;&nbsp;&nbsp;&nbsp;low: 4
            &nbsp;&nbsp;&nbsp;&nbsp;info: 5
            &nbsp;&nbsp;testCoverageThresholds:
            &nbsp;&nbsp;&nbsp;&nbsp;fresh: 6 # Fresh code coverage
            &nbsp;&nbsp;&nbsp;&nbsp;total: 7 # Total percentage
        </code-block>
    </tab>
    <tab group-key="linter-tabs-cdnet" title="%qp-co%">
        <p>You can configure <a href="quality-gate.topic">quality gates</a> for the total number of project problems by 
            saving this snippet to the <a href="qodana-yaml.md"><code>qodana.yaml</code></a> file:
        </p>
        <code-block lang="yaml">
            failureConditions:
            &nbsp;&nbsp;severityThresholds:
            &nbsp;&nbsp;&nbsp;&nbsp;any: 50 # Total number of problems in all severities
        </code-block> 
    </tab>
</tabs>

### Analyzing pull requests

<tabs group="linter-tabs">
    <tab group-key="linter-tabs-dotnet" title="%qp%">
        <tabs group="software">
            <tab title="GitHub Actions" group-key="github">
                <p>
                    The <a href="https://github.com/marketplace/actions/qodana-scan">Qodana Scan GitHub action</a> automatically 
                    analyzes all pull requests, so you do not have to provide any additional configuration:
                </p>
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
                                  args: --linter,%qp-linter%
                                env:
                                  QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
                </code-block>
            </tab>
            <tab title="GitLab CI/CD" group-key="gitlab">
                <p>
                    In the root directory of your project, save the <code>.gitlab-ci.yml</code> file containing the 
                    following snippet and then uncomment the required linter:
                </p>
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
                <p>
                    Here, the <code>--diff-start</code> option specifies a hash of the commit that will act as a 
                    base for comparison.
                </p>
            </tab>
            <tab title="TeamCity" group-key="teamcity">
                <p>Information about configuring TeamCity for analyzing pull and merge requests is available on the 
                    <a href="%TeamCityPullRequests%">TeamCity</a> documentation portal.
                </p>
            </tab>
            <tab title="Command line" group-key="command-line">
                <p>
                    To analyze changes in your code, employ the <code>--diff-start</code> option and specify a hash of the commit 
                    that will act as a base for comparison:
                </p>
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
        </tabs>
    </tab>
    <tab group-key="linter-tabs-cdnet" title="%qp-co%">
            <tabs group="software">
            <tab title="GitHub Actions" group-key="github">
                <p>
                    The <a href="https://github.com/marketplace/actions/qodana-scan">Qodana Scan GitHub action</a> automatically 
                    analyzes all pull requests, so you do not have to provide any additional configuration:
                </p>
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
                                  args: --linter,%qp-co-linter%
                                env:
                                  QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
                </code-block>
            </tab>
            <tab title="GitLab CI/CD" group-key="gitlab">
                <p>
                    In the root directory of your project, save the <code>.gitlab-ci.yml</code> file containing the 
                    following snippet and then uncomment the required linter:
                </p>
                <code-block lang="yaml">
                    qodana:
                      image:
                         name: %qp-co-linter% 
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
                <p>
                    Here, the <code>--diff-start</code> option specifies a hash of the commit that will act as a 
                    base for comparison.
                </p>
            </tab>
            <tab title="TeamCity" group-key="teamcity">
                <p>Information about configuring TeamCity for analyzing pull and merge requests is available on the 
                    <a href="%TeamCityPullRequests%">TeamCity</a> documentation portal.
                </p>
            </tab>
            <tab title="Command line" group-key="command-line">
                <p>
                    To analyze changes in your code, employ the <code>--diff-start</code> option and specify a hash of the commit 
                    that will act as a base for comparison:
                </p>
                <tabs group="cli-settings">
                    <tab group-key="qodana-cli" title="Qodana CLI">
                        <code-block prompt="$">
                            qodana scan \
                               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                               -l %qp-co-linter% \
                               --diff-start=&lt;GIT_START_HASH&gt;
                        </code-block>
                    </tab>
                    <tab group-key="docker-image" title="Docker image">
                        <code-block lang="shell" prompt="$">
                          docker run \
                          &nbsp;&nbsp;&nbsp;-v $(pwd):/data/project/ \
                          &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                          &nbsp;&nbsp;&nbsp;%qp-co-linter% \
                          &nbsp;&nbsp;&nbsp;--diff-start=&lt;GIT_START_HASH&gt;
                        </code-block>
                    </tab>
                </tabs>
            </tab>
        </tabs>
    </tab>
</tabs>

## Usage statistics

According to the [JetBrains EAP user
agreement](https://www.jetbrains.com/legal/agreements/user_eap.html), we can use third-party services to analyze the 
usage of our features to further improve the user experience. All data will be collected 
[anonymously](https://www.jetbrains.com/company/privacy.html). You can disable statistics by using the 
`--no-statistics=true` CLI option, for example:

```Shell
docker run \
   -v <source-directory>/:/data/project/ \
   -e QODANA_TOKEN="<cloud-project-token>" \
   %qd-image% \
   --no-statistics=true
```

## Supported technologies and features
{id="dotnet-feature-matrix"}

<!-- These need to be compared for both linters because now it's not clear what is what -->

<link-summary>Comparison matrix of the .NET linters.</link-summary>

<table>
    <tr>
      <td>Support for</td>
      <td>Name</td>
      <td>%qp%</td>
      <td>%qp-co%</td>
    </tr>
    <tr>
        <td>Programming languages</td>
        <td>
            <p>C#</p>
            <p>C++ <b>*</b></p>
            <p>VB.NET <b>**</b></p>
            <p>C <b>*</b></p>
            <p>JavaScript</p>
            <p>TypeScript</p>
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
            <p>&#x2714;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
        </td>
    </tr>
    <tr>
        <td>Frameworks and libraries</td>
        <td>
            <p>.NET Framework</p>
            <p>.NET Core</p>
            <p>Handlebars/Mustache</p>
            <p>Less</p>
            <p>Node.JS</p>
            <p>NUnit</p>
            <p>Pug/Jade</p>
            <p>Sass/SCSS</p>
            <p>Unity</p>
            <p>Unreal Engine</p>
            <p>Vue</p>
            <p>Xunit</p>
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
            <p>&#x2714;</p>
            <p>&#x2714;</p>
        </td>
        <td>
            <p>&nbsp;</p>
        </td>
    </tr>
        <tr>
        <td>Databases and ORM</td>
        <td>
            <p>MongoDB</p>
            <p>MySQL</p>
            <p>Oracle</p>
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
        </td>
        <td>
            <p>&nbsp;</p>
        </td>
    </tr>
    <tr>
        <td>Markup languages</td>
        <td>
            <p>HTML</p>
            <p>XML</p>
            <p>CSS</p>
            <p>JSON and JSON5</p>
            <p>RELAX NG</p>
            <p>T4</p>
            <p>XPath</p>
            <p>XSLT</p>
            <p>YAML</p>
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
        </td>
        <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
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
        <td>Scripting languages</td>
        <td>
            <p>Shell script</p>
        </td>
       <td>
            <p>&#x2714;</p>
        </td>
        <td>
            <p>&nbsp;</p>
        </td>
    </tr>
    <tr>
        <td>Build management</td>
        <td>
            <p>MSBuild</p>
        </td>
       <td>
            <p>&#x2714;</p>
        </td>
        <td>
            <p>&nbsp;</p>
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
      </td>
      <td>
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
      </td>
    </tr>
</table>

\* C and C++ inspections are applicable for projects containing `.sln` files.

** Supports Visual Basic inspections  only.
