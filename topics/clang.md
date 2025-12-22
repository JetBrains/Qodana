# C / C++

<show-structure for="chapter" depth="3"/>

<!-- Human-readable linter names -->
<var name="qdcpp" value="%cpp%"/>
<var name="qdcppc" value="%clang%"/>
<!-- Docker images -->
<var name="qdcpp-image" value="%cpp-image%"/>
<var name="qdcppc-image" value="%clang-image%"/>
<!-- Linter names -->
<var name="qdcpp-linter" value="%cpp-linter%"/>
<var name="qdcppc-linter" value="%clang-linter%"/>

<var name="qd-linter" value="%cpp-linter%"/>

<var name="qdcpp-privileged" value="jetbrains/%cpp-linter%&lt;-clangXX&gt;-privileged"/>
<var name="qd-image" value="jetbrains/qodana-&lt;cpp|clang&gt;:%version-for-combined-cpp%&lt;-clangXX&gt;&lt;-privileged&gt;"/>
<var name="common-image" value="jetbrains/qodana-&lt;cpp|clang&gt;:%version-for-combined-cpp%&lt;-clangXX&gt;&lt;-privileged&gt;"/>
<var name="JenkinsCred" value="https://www.jenkins.io/doc/book/using/using-credentials/#adding-new-global-credentials"/>
<var name="ide" value="CLion"/>

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

<!-- The variables from the first version of the page -->
<var name="linter" value="Qodana for C/C++"/>
<var name="config-file" value="qodana-clang-docker-readme.topic"/>
<var name="clang-config" value="https://gist.github.com/fbaeuerlein/2895f889e451a817d7b2b36fd60e2873"/>
<var name="dockerfile" value="https://github.com/JetBrains/qodana-docker/blob/main/2025.3/base/cpp.Dockerfile"/>
<var name="dockerfile-internal" value="https://github.com/JetBrains/qodana-docker/blob/main/2025.3/cpp/internal.Dockerfile"/>
<var name="clang-website" value="https://clang.llvm.org/extra/clang-tidy/checks/list.html"/>
<var name="clion-inspections-general" value="https://www.jetbrains.com/help/clion/list-of-c-cpp-inspections.html#general"/>
<var name="misra-inspections" value="https://www.jetbrains.com/help/clion/list-of-c-cpp-inspections.html#stat-analysis-tools"/>
<var name="compdb-generate" value="https://www.jetbrains.com/help/clion/compilation-database.html#compdb_generate"/>


<var name="code-inspection-ide-help-url" value="https://www.jetbrains.com/help/clion/list-of-c-cpp-inspections.html#general"/>
<var name="code-inspection-profiles-ide-help-url" value="https://www.jetbrains.com/help/idea/?Customizing_Profiles"/>
<var name="GitHubLink" value="https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository"/>
<var name="teamcity-linter-list" value="Here, select Custom and in the field below specify the %qdcpp% linter."/>

<var name="build-system" value="https://intellij-support.jetbrains.com/hc/en-us/articles/207252755-Which-build-systems-are-supported-Do-you-plan-to-support-any-other-build-systems"/>

<var name="cmake-presets" value="https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html"/>
<var name="cmake-preset-docs" value="https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html#configure-preset"/>

<link-summary>%qdcpp% and %qdcppc% linters let you analyze C and C++ projects that provide a `compile_commands.json` file.</link-summary>

<note>
%qdcpp% and %qdcppc% are currently in Early Access, which means that they may not be reliable, may not work as intended, and may contain errors.
Any use of the EAP product is at your own risk. Your feedback is very welcome in our 
<a href="https://youtrack.jetbrains.com/newIssue?project=QD">issue tracker</a> or at
<a href="mailto:qodana-support@jetbrains.com">qodana-support@jetbrains.com</a>.
</note>

The C/C++ family of linters lets you analyze C and C++ projects that support any common build system like CMake 
or provide a [`compile_commands.json` file](https://clang.llvm.org/docs/JSONCompilationDatabase.html). There are two different linters that provide this functionality:

<tabs>
    <tab title="%qdcpp%">
        <table>
            <tr>
                <td>Characteristic</td>
                <td>Description</td>
            </tr>
            <tr>
                <td>Linter name</td>
                <td><code>%qdcpp-linter%</code></td>
            </tr>
            <tr>
                <td>Docker image</td>
                <td><code>%qdcpp-image%&lt;-clangXX&gt;&lt;-privileged&gt;</code>*</td>
            </tr>
            <tr>
                <td>Available under licenses</td>
                <td>Ultimate and Ultimate Plus <a href="pricing.md">licenses</a></td>
            </tr>
            <tr>
                <td>Shipped as</td>
                <td>A Docker image</td>
            </tr>
            <tr>
                <td>Supports</td>
                <td><p>The full set of inspections provided by <a href="https://www.jetbrains.com/help/clion/">CLion</a>:</p>
                    <list>
                      <li><a href="https://clang.llvm.org/extra/clang-tidy">Clang-Tidy</a> inspections supported by the %qdcppc% linter</li>
                      <li><a href="https://en.wikipedia.org/wiki/MISRA_C">MISRA</a> inspections</li>
                      <li>Inspections based on dataflow analysis</li>
                    </list>
                </td>
            </tr>
        </table>
        <p>* Use the optional <code>-clangXX</code> tag to specify the <a href="https://clang.llvm.org/extra/clang-tidy">Clang-Tidy</a> version from 15 to 18.
        Using the <code>-privileged</code> tag, you can run %product% in the privileged mode to execute commands that require root access. 
        In this case, Qodana comes with a default <code>qodana</code> user that possesses root privileges and does not require a password.
        To use this mode, the <code>-clangXX</code> tag should be specified too.</p>
    </tab>
    <tab title="%qdcppc%">
        <table>
            <tr>
                <td>Characteristic</td>
                <td>Description</td>
            </tr>
            <tr>
                <td>Linter name</td>
                <td><code>%qdcppc-linter%</code></td>
            </tr>
            <tr>
                <td>Docker image</td>
                <td><code>%qdcppc-image%&lt;-clangXX&gt;</code>*</td>
            </tr>
            <tr>
                <td>Available under licenses</td>
                <td>Community <a href="pricing.md">license</a></td>
            </tr>
            <tr>
                <td>Shipped as</td>
                <td>A Docker image</td>
            </tr>
            <tr>
                <td>Supports</td>
                <td><a href="https://clang.llvm.org/extra/clang-tidy">Clang-Tidy</a>-based inspections</td>
            </tr>
        </table>
        <p>* Using the optional <code>-clangXX</code> tag, specify the <a href="https://clang.llvm.org/extra/clang-tidy">Clang-Tidy</a> version from 15 to 18.</p>
    </tab>
</tabs>

Both linters support AMD64 and ARM64 architectures.

<tip>
<p>You can learn more about inspections using these links:</p>
<list>
  <li><a href="%clang-website%">Standard Clang-Tidy inspections</a></li>
  <li><a href="%clion-inspections-general%">CLion's Clang-Tidy inspections</a></li>
  <li><a href="%misra-inspections%">CLion's MISRA inspections</a></li>
</list>
</tip>

To see the list of supported features, navigate to the [](#clang-feature-matrix) section.

## Implementation details

The Docker image of %qdcppc% employs Clang 16. You can see the [`Dockerfile`](%dockerfile%) for the detailed description of all software used by the linter.

%qdcppc% searches for compile commands in the `build/compile_commands.json` file of the project directory. 
This file is usually generated by your build system. After reading the `compile_commands.json` file, the linter analyzes 
the project, generates analysis reports and saves them locally or uploads to %cloud%.

## Before you start

{id="clang-before-you-start"}

### Prepare your project

<procedure>
    <step>
        <p>You can configure Clang-Tidy-based inspections in the <code>.clang-tidy</code> file, see the configuration example on the
        <a href="%clang-config%">GitHub</a> website. After configuring, save this file under the project root.</p>
        <tip>
        <p>You can get the list of all available Clang-Tidy inspections using the following command:</p>
        <tabs group="clang-tidy-commands">
        <tab id="qodana-clang-full-linux" title="Linux" group-key="clang-linux">
        <code-block>clang-tidy -list-checks -checks="*"</code-block>
        </tab>
        <tab id="qodana-clang-full-windows" title="Windows" group-key="clang-windows">
        <code-block>./clang-tidy.exe -list-checks -checks="*"</code-block>
        </tab>
        </tabs>
        <p>To get the list of all inspections enabled in Clang-Tidy by default, you can run the following command:</p>
        <tabs group="clang-tidy-commands">
        <tab id="qodana-clang-enabled-linux" title="Linux" group-key="clang-linux">
        <code-block>clang-tidy -list-checks</code-block>
        </tab>
        <tab id="qodana-clang-enabled-windows" title="Windows" group-key="clang-windows">
        <code-block>./clang-tidy.exe -list-checks</code-block>
        </tab>
        </tabs>
        </tip>
    </step>
    <step><p>Open the <code>.clang-tidy</code> file and configure the list of files and paths that will be analyzed by Qodana.</p>
        <tip>If you already have the <code>compile_commands.json</code> file, you can also configure files and paths in this file.</tip>
    </step>
    <step>
        <p>
          For %qdcppc%, you need to generate <code>compile_commands.json</code> as explained in the <a href="%compdb-generate%">CLion documentation portal</a>, and save it to the <code>build</code> directory under the project root.</p>
        <p>
          If you use CMake, you can also generate a compilation database by specifying the following <a href="before-running-qodana.md"><code>bootstrap</code></a> option in the <code>qodana.yaml</code> file, for example:
        </p>
        <code-block lang="yaml">
            bootstrap: |
            &nbsp;&nbsp;set -eux
            &nbsp;&nbsp;cmake -S . -B build -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
        </code-block>
        <p>
          You can skip this step for the %qdcpp% linter. Assuming that you have a <a href="%build-system%">build system supported by CLion</a>, 
          the project will be configured automatically. This includes <code>compile_commands.json</code> files placed at the project root, not in the <code>build/</code> directory.
        </p>
    </step>
    <step>
        <p>
          If your project requires specific packages not previously mentioned in the <a href="%dockerfile%"><code>Dockerfile</code></a>, add the following <code>bootstrap</code> command to your <code>qodana.yaml</code> file to install the required packages:
        </p>
        <code-block lang="yaml">
          bootstrap: |
          &nbsp;&nbsp;set -eux
          &nbsp;&nbsp;sudo apt-get update
          &nbsp;&nbsp;sudo apt-get install -y &lt;required-packages&gt;
          &nbsp;&nbsp;cmake -S . -B build -DCMAKE_EXPORT_COMPILE_COMMANDS=ON        
        </code-block>
            <tip>
              By default, Docker images run commands as a non-root user, and <code>sudo</code> is not available for security reasons. 
              To overcome this, use alternative images with the <code>-privileged</code> tag like <code>%qdcpp-privileged%</code>, 
              or set a user using the <a href="https://docs.docker.com/reference/cli/docker/container/run/#options"><code>docker run --user</code> parameter</a>.
            </tip>
    </step>
    <step>
        <p>
            To modify analysis paths in the <code>compile_commands.json</code> file while running the %qdcppc% linter or 
            the %qdcpp% linter using the raw <code>compile_commands.json</code> file, follow the instructions from 
            the <a anchor="Modifying+paths+for+analysis"/> section.
        </p>
    </step>
</procedure>

### %cloud%

<include from="lib_qd.topic" element-id="before-start-qodana-cloud" use-filter="empty,clang"/>

### Prepare your software

<include from="lib_qd.topic" element-id="before-start-prepare-software" use-filter="empty,generic"/>

## Run %product%

<note><include from="lib_qd.topic" element-id="docker-ram-note"/></note>
<include from="lib_qd.topic" element-id="major-version-note"/>
<include from="lib_qd.topic" element-id="root-and-non-root-users-info-bubble"/>

<!--<p>You can run all linters described in this section in two modes:</p>
<list>
  <li><a href="deploy-qodana.md#deploy-qodana-native-mode">Native mode</a> is the recommended method that lets you run
    linters without using Docker containers,</li>
  <li>Container mode is an alternative that involves Docker containers the linters.</li>
</list>
 <tabs group="native-container">
  <tab title="Native mode" group-key="native-mode">
    <snippet id="dotnet-run-qodana-native-mode-yaml">
      <tabs group="software">
          <tab title="GitHub Actions" group-key="github">
      <p>You can run %product% using the <a href="https://github.com/marketplace/actions/qodana-scan">Qodana Scan GitHub action</a>.</p>
      <p>To analyze the <code>main</code> branch, release branches and the pull requests coming to your repository in 
        native mode, save this workflow configuration to the <code>.github/workflows/code_quality.yml</code> file:</p>
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
                                      args: |
                                          --linter,%qd-linter%,
                                          --within-docker,false
                                  env:
                                    QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
                      </code-block>
                        <p>This configuration uses the <code>--linter</code>
                            <a href="docker-image-configuration.topic" anchor="docker-config-reference-qodana-scan">option</a>
                            to specify a <a href="linters.md">linter</a>. The
                            <code>--within-docker</code> option in the <code>false</code> state is used for enabling native mode.</p>
              <p>More configuration examples are available in the <a href="github.md"/> section.</p>
          </tab>
          <tab title="Command line" group-key="command-line">
              <p>Run this command in the project root directory:</p>
              <code-block lang="shell" prompt="$">
                   qodana scan \
                   &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;qodana-cloud-token&gt;" \
                   &nbsp;&nbsp;&nbsp;--linter %qd-linter% \
                   &nbsp;&nbsp;&nbsp;--within-docker false
              </code-block>
              <p>This configuration uses the <code>--linter</code>
                  <a href="docker-image-configuration.topic" anchor="docker-config-reference-qodana-scan">option</a>
                  to specify a <a href="linters.md">linter</a>. The
                  <code>--within-docker</code> option in the <code>false</code> state is used for enabling native mode.</p>
              <p>If you are using another %cloud% instance than https://qodana.cloud/, override it by declaring the <code>QODANA_ENDPOINT</code> environment variable.</p>
              <p>In your browser, open <a href="https://qodana.cloud">%cloud%</a> to examine the analysis results and
                  reconfigure the analysis. See the <a href="ui-overview.md"/> section of the documentation for full details.</p>
          </tab>
      </tabs>
  </tab>
  <tab title="Container mode" group-key="container-mode">
      <p>Container mode is available for all linters; however, we recommend that you use native mode.</p>-->
<tabs group="software">
    <tab title="GitHub Actions" group-key="github">
      <note>This feature is experimental and is being actively developed, which means that it should not be used in a production environment.</note>
      <p>To analyze the <code>main</code> branch, release branches and the pull requests coming
      to your repository, save this workflow configuration to the <code>.github/workflows/code_quality.yml</code> file:</p>
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
                        args: --image,%qdcpp-image%
                        # args: --image,%qdcppc-image%  # Community version
                      env:
                        QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
          </code-block>
        <p>Here, <code>fetch-depth: 0</code> is required for checkout in case Qodana works in pull request mode
                (reports issues that appeared only in that pull request).</p>
        <p>To override the location of <code>compile_commands.json</code> (%qdcppc% only), you can specify the location relative to the project root, so the configuration would look like:
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
                      uses: %action-version%
                      with:
                        args: | 
                            --image,%qdcppc-image%,
                            --compile-commands,&lt;path-to-compile_commands.json&gt;
                      env:
                        QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
          </code-block>

  <p>More configuration examples are available in the <a href="github.md"/> section.</p>
    </tab>
    <tab title="Jenkins" group-key="jenkins">
        <note>This feature is experimental and is being actively developed, which means that it should not be used in a production environment.</note>
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
                        image '%qdcpp-image%'
                        // image '%qdcppc-image%'  # Community version
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
        <p>To override the location of <code>compile_commands.json</code> (%qdcppc% only), you can specify the location relative to the project root, so the configuration would look like:
        </p>
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
                        image '%qdcppc-image%'
                    }
                }
                stages {
                    stage('Qodana') {
                        steps {
                            sh '''
                            qodana \
                            --compile-commands &lt;path-to-compile_commands.json&gt;
                            '''
                        }
                    }
                }
            }
        </code-block>
        <p>More configuration examples are available in the <a href="jenkins.md"/> section.</p>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab">
        <note>This feature is experimental and is being actively developed, which means that it should not be used in a production environment.</note>
        <p>In the root directory of your project, save this snippet to the <code>.gitlab-ci.yml</code> file:</p>
        <code-block lang="yaml">
          include:
            - component: %gitlab-version%
                args: --image,%common-image%
        </code-block>
        <p>To override the location of the <code>compile_commands.json</code> file for the  %qdcppc% linter, specify the location relative to the project root, so the configuration would look like:
        </p>
        <code-block lang="yaml">
          include:
            - component: %gitlab-version%
              inputs:
                 args: |
                    --compile-commands,&lt;path-to-compile_commands.json&gt;,
                    --image,%qdcppc-image%
        </code-block>
    <p>More configuration examples are available in the <a href="gitlab.md"/> section.</p>
    </tab>
    <tab title="TeamCity" group-key="teamcity" id="jvm-run-qodana-teamcity">
      <include from="lib_qd.topic" element-id="teamcity-add-a-qodana-runner" use-filter="empty,clang,clang-compilation-override"/>
      <p>More configuration examples are available in the <a href="teamcity.md"/> section.</p>
    </tab>
    <tab title="Command line" group-key="command-line">
        <note> Running analysis is a resource-intensive operation. If you experience issues, consider increasing the Docker
                Desktop runtime memory limit, which is set to 2 GB by default. See the Docker Desktop documentation for 
                <a href="https://docs.docker.com/desktop/windows/#resources">Windows</a> and 
                <a href="https://docs.docker.com/desktop/mac/#resources">macOS</a>.
        </note>
        <p>Run this command:</p>
        <code-block lang="shell" prompt="$">
            docker run \
            &nbsp;&nbsp;&nbsp;-v &lt;source-directory&gt;/:/data/project/ \
            &nbsp;&nbsp;&nbsp;-v &lt;output-directory&gt;/:/data/results/ \
            &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
            &nbsp;&nbsp;&nbsp;%qdcpp-image%
            &nbsp;&nbsp;&nbsp;# %qdcppc-image%  # Community version
        </code-block>
        <p>
            In this command, <code>source-directory</code> and <code>output-directory</code> are full local paths
            to the project source code directory and the 
            <a href="qodana-inspection-output.md" anchor="Output+structure">analysis result</a> directory, respectively. The
            <code>QODANA_TOKEN</code> variable refers to the <a href="project-token.md">project token</a>
            required by the
            <a href="pricing.md" anchor="pricing-linters-licenses">Ultimate and Ultimate Plus</a> linters.
            If you omit the <code>QODANA_TOKEN</code> variable, the analysis results will be available in the
            <code>qodana.sarif.json</code> file saved in the <code>output-directory</code> of your project root.
        </p>
        <p>To override the location of the <code>compile_commands.json</code> file for the %qdcppc% linter, you can 
          specify the location relative to the project root, so the configuration would look like:
        </p>
        <code-block lang="shell" prompt="$">
            docker run \
            &nbsp;&nbsp;&nbsp;-v &lt;source-directory&gt;/:/data/project/ \
            &nbsp;&nbsp;&nbsp;-v &lt;output-directory&gt;/:/data/results/ \
            &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
            &nbsp;&nbsp;&nbsp;%qdcppc-image% \
            &nbsp;&nbsp;&nbsp;--compile-commands &lt;path-to-compile_commands.json&gt;
        </code-block>
        <p>In your browser, open <a href="https://qodana.cloud">%cloud%</a> to examine the analysis results and
          reconfigure the analysis. See the <a href="ui-overview.md"/> section of the documentation for full details.</p>
        <p>If you run the analysis several times in a row, make sure you've cleaned the results directory before using it in 
        <code>docker run</code> again.</p>
    </tab>
</tabs>
  <!--</tab>
</tabs>-->

## Explore analysis results

<p>Once %product% analyzed your project and uploaded the analysis results to %cloud%, you can navigate to your 
project <a href="https://qodana.cloud">%cloud%</a> and review the analysis results report.</p>
<img src="qc-report-example-clang.png" alt="Analysis report example" width="720" border-effect="line"/>
<p>To learn more about %instance% report UI, see the <a href="ui-overview.md"/> section.</p>

<!-- Here add about observing locally generated files -->

## Extend %product% configuration

### Adjusting the scope of analysis

<p>
    %product% recognizes the <code>qodana.yaml</code> file for the analysis configuration,
    so that you don't need to pass any additional parameters. For the %qdcpp% linter, you can configure:</p>
<list>
    <li>Commands that will run before the linter using the <a href="before-running-qodana.md"><code>boostrap</code></a>
        option. Using this, you can <a anchor="Modifying+paths+for+analysis">modify the list of paths</a> in the <code>compile_commands.json</code> file.</li>
    <li><a anchor="Enabling+the+baseline+feature">Baseline</a> and <a anchor="Enabling+the+quality+gate">quality gate</a> features.</li>
</list>

<note>The %qdcppc% linter does not support <a href="qodana-yaml.md" anchor="Include+an+inspection+into+the+analysis+scope">including</a> 
and <a href="qodana-yaml.md" anchor="exclude-paths">excluding</a> paths for specific inspections using the <code>qodana.yaml</code> file.</note>

### Modifying paths for analysis


Recommendations from this section are applicable only to the %qdcppc% linter and specific cases where the %qdcpp% linter 
is analyzing a project configured with a raw `compile_commands.json` file.

To modify analysis paths in the `compile_commands.json` file contained in the Docker container of the linter, 
you can run a script during the bootstrap stage of analysis. For example, the Python scripts below use glob 
patterns and regular expressions that modify paths in the `compile_commands.json` file inside the Docker container of %product%.

<tabs>
    <tab title="Including glob patterns">
        <code-block lang="Python">
            #!/usr/bin/env python3
            import json
            from pathlib import Path
            &nbsp;            
            # Read existing compile_commands.json ------------------------------------------
            REPO_ROOT = Path.cwd()
            COMPILE_COMMANDS_PATH = REPO_ROOT / "build/compile_commands.json"
            &nbsp;
            with open(COMPILE_COMMANDS_PATH, "r", encoding="utf-8") as fd:
            &nbsp;&nbsp;&nbsp;&nbsp;compile_commands = json.load(fd)
            &nbsp;
            # Filter source files ----------------------------------------------------------
            from itertools import chain
            &nbsp;
            INCLUDE_GLOBS = [
            &nbsp;&nbsp;&nbsp;&nbsp;"src/**/*",
            &nbsp;&nbsp;&nbsp;&nbsp;"include/**/*",
            ]
            allowed_paths = (REPO_ROOT.glob(pattern) for pattern in INCLUDE_GLOBS)
            allowed_paths = set(chain.from_iterable(allowed_paths))
            &nbsp;
            def keep_condition(cc_entry: dict):
            &nbsp;&nbsp;&nbsp;&nbsp;path = Path(cc_entry["file"])
            &nbsp;&nbsp;&nbsp;&nbsp;return path in allowed_paths
            &nbsp;
            compile_commands = list(filter(keep_condition, compile_commands))
            &nbsp;
            # Save the updated list of source files ----------------------------------------
            COMPILE_COMMANDS_PATH.rename(COMPILE_COMMANDS_PATH.with_suffix(".old.json"))
            with open(COMPILE_COMMANDS_PATH, "w", encoding="utf-8") as fd:
            &nbsp;&nbsp;&nbsp;&nbsp;json.dump(compile_commands, fd, ensure_ascii=False, indent="\t")
        </code-block>
    </tab>
    <tab title="Excluding glob patterns">
        <code-block lang="Python">
            #!/usr/bin/env python3
            import json
            from pathlib import Path
            &nbsp;
            # Read existing compile_commands.json ------------------------------------------
            REPO_ROOT = Path.cwd()
            COMPILE_COMMANDS_PATH = REPO_ROOT / "build/compile_commands.json"
            &nbsp;
            with open(COMPILE_COMMANDS_PATH, "r", encoding="utf-8") as fd:
            &nbsp;&nbsp;&nbsp;&nbsp;compile_commands = json.load(fd)
            &nbsp;
            # Filter source files ----------------------------------------------------------
            from itertools import chain
            &nbsp;
            EXCLUDE_GLOBS = [
            &nbsp;&nbsp;&nbsp;&nbsp;"src/**/*",
            &nbsp;&nbsp;&nbsp;&nbsp;"include/**/*",
            ]
            allowed_paths = (REPO_ROOT.glob(pattern) for pattern in EXCLUDE_GLOBS)
            allowed_paths = set(chain.from_iterable(allowed_paths))
            &nbsp;
            # Invert the list of paths -----------------------------------------------------
            allowed_paths = set(REPO_ROOT.rglob("*")) - allowed_paths
            &nbsp;
            def keep_condition(cc_entry: dict):
            &nbsp;&nbsp;&nbsp;&nbsp;path = Path(cc_entry["file"])
            &nbsp;&nbsp;&nbsp;&nbsp;return path in allowed_paths
            &nbsp;
            compile_commands = list(filter(keep_condition, compile_commands))
            &nbsp;
            # Save the updated list of source files ----------------------------------------
            COMPILE_COMMANDS_PATH.rename(COMPILE_COMMANDS_PATH.with_suffix(".old.json"))
            with open(COMPILE_COMMANDS_PATH, "w", encoding="utf-8") as fd:
            &nbsp;&nbsp;&nbsp;&nbsp;json.dump(compile_commands, fd, ensure_ascii=False, indent="\t")
        </code-block>
    </tab>
    <tab title="Including regex pattern">
        <code-block lang="Python">
            #!/usr/bin/env python3
            import json
            from pathlib import Path
            &nbsp;
            # Read existing compile_commands.json ------------------------------------------
            REPO_ROOT = Path.cwd()
            COMPILE_COMMANDS_PATH = REPO_ROOT / "build/compile_commands.json"
            &nbsp;
            with open(COMPILE_COMMANDS_PATH, "r", encoding="utf-8") as fd:
            &nbsp;&nbsp;&nbsp;&nbsp;compile_commands = json.load(fd)
            &nbsp;
            # Filter source files using the regex ------------------------------------------
            import re
            &nbsp;
            INCLUDE_REGEX = re.compile(r"src\/(core|engine)\/.*$")
            &nbsp;
            def keep_condition(cc_entry: dict):
            &nbsp;&nbsp;&nbsp;&nbsp;path = cc_entry["file"]
            &nbsp;&nbsp;&nbsp;&nbsp;return re.fullmatch(INCLUDE_REGEX, path)
            &nbsp;
            compile_commands = list(filter(keep_condition, compile_commands))
            &nbsp;
            # Save the updated list of source files ----------------------------------------
            COMPILE_COMMANDS_PATH.rename(COMPILE_COMMANDS_PATH.with_suffix(".old.json"))
            with open(COMPILE_COMMANDS_PATH, "w", encoding="utf-8") as fd:
            &nbsp;&nbsp;&nbsp;&nbsp;json.dump(compile_commands, fd, ensure_ascii=False, indent="\t")
        </code-block>    
    </tab>
</tabs>

To run a script, use the `bootstrap` section of the [`qodana.yaml`](qodana-yaml.md) file, for example:

```yaml
bootstrap: |
  set -eux
  cmake -S . -B build -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
  python3 filter-script.py
```

### Enabling the baseline feature

You can skip analysis for specific problems by using the [baseline](baseline.topic) feature. Information about a baseline is contained in a SARIF-formatted file.

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
                        uses: JetBrains/qodana-action@v2024.3
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
        <p>In your browser, open <a href="https://qodana.cloud">%cloud%</a> to examine the analysis results and
          reconfigure the analysis. See the <a href="ui-overview.md"/> section of the documentation for full details.</p>
          </tab>
      </tabs>
  </tab>
  <tab title="Container mode" group-key="container-mode">-->
<tabs group="software">
    <tab title="GitHub Actions" group-key="github">
                <p>Save this snippet to the <code>.github/workflows/code_quality.yml</code> file:</p>
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
                  uses: %action-version%
                  with:
                    args: | 
                        --image,%qdcpp-image%,
                        --baseline,&lt;path/to/qodana.sarif.json&gt;
                    # args: --image,%qdcppc-image%,--baseline,&lt;path/to/qodana.sarif.json&gt;  # Community version
                  env:
                    QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
      </code-block>
      <p>This snippet has the <code>args: --baseline,&lt;path/to/qodana.sarif.json&gt;</code> line that specifies
        the path to the SARIF file containing a baseline.</p>
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
                    image '%qdcpp-image%'
                    // image '%qdcppc-image%'  // Community version
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
        include:
           - component: %gitlab-version%
             inputs:
                args: | 
                    --baseline,qodana.sarif.json,
                    --fail-threshold,&lt;number-of-accepted-problems&gt;,
                    --image,%common-image%
      </code-block>
    </tab>
    <tab title="TeamCity" group-key="teamcity">
        <include from="lib_qd.topic" element-id="teamcity-add-a-qodana-runner" use-filter="empty,clang,baseline"/>
    </tab>
    <tab title="Command line" group-key="command-line">
          <p>Run this command invoking the <code>--baseline</code> option:</p>
          <code-block lang="shell" prompt="$">
              docker run \
                 -v &lt;source-directory&gt;/:/data/project/ \
                 -v &lt;path_to_baseline&gt;:/data/base/ \
                 -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                 %qdcpp-image% \
                 --baseline /data/base/&lt;path-relative-to-project-dir&gt;/qodana.sarif.json
                 # Replace image with %qdcppc-image% for community version
          </code-block>
    </tab>
</tabs>
<!--  </tab>
</tabs>-->

### Enabling the quality gate

<link-summary>You can configure quality gates for the total number of problems and for specific severities.</link-summary>

You can configure [quality gates](quality-gate.topic) for:

- The total number of project problems
- Multiple quality gates for <a href="faq.topic" anchor="faq-severities">problem severities</a>.

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
```

### Analyzing pull requests

You can analyze pull requests using the %cpp% linter.

<tabs group="software">
    <tab title="GitHub Actions" group-key="github">
        <p>
            The <a href="https://github.com/marketplace/actions/qodana-scan">Qodana Scan GitHub action</a> automatically 
            analyzes all pull requests, so you do not have to provide any additional configuration. Save this configuration
            to the <code>.github/workflows/code_quality.yml</code> file:
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
                        uses: %action-version%
                        with:
                          args: --image,%qdcpp-image%
                        env:
                          QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
        </code-block>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab">
        <p>
            In the root directory of your project, save the <code>.gitlab-ci.yml</code> file containing the 
            following snippet:
        </p>
        <code-block lang="yaml">
            include:
               - component: %gitlab-version%
                 inputs:
                   args: --image,%qdcpp-image%
        </code-block>
        <p>
            This configuration enables merge request analysis.
        </p>
    </tab>
    <tab title="TeamCity" group-key="teamcity">
        <p>Information about configuring TeamCity for analyzing pull and merge requests is available on the 
            <a href="%TeamCityPullRequests%">TeamCity</a> documentation portal.
        </p>
    </tab>
    <tab title="Command line" group-key="command-line">
        <p>
            To <a href="analyze-pr.md">analyze changes</a> in your code, employ the <code>--diff-start</code> option and specify a hash of the commit 
            that will act as a base for comparison:
        </p>
        <tabs group="cli-settings">
            <tab group-key="qodana-cli" title="Qodana CLI">
                <code-block prompt="$">
                    qodana scan \
                       -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                       -l %qdcpp-image% \
                       --diff-start=&lt;GIT_START_HASH&gt;
                </code-block>
            </tab>
            <tab group-key="docker-image" title="Docker image">
                <code-block lang="shell" prompt="$">
                  docker run \
                  &nbsp;&nbsp;&nbsp;-v $(pwd):/data/project/ \
                  &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                  &nbsp;&nbsp;&nbsp;%qdcpp-image% \
                  &nbsp;&nbsp;&nbsp;--diff-start=&lt;GIT_START_HASH&gt;
                </code-block>
            </tab>
        </tabs>
    </tab>
</tabs>


## Configure compilers and environments

<link-summary>CMake presets let you customize the %cpp% linter for specific compilers and environments.</link-summary>

[CMake presets](%cmake-presets%) let you customize the %cpp% linter for specific compilers and 
environments. Each preset lets you store CLI options like a target build directory, cache variables, 
preferred generator, compilers, and other `configurePresets` object options of the `CMakePresets.json` 
file contained in your project root.

> To learn more about CMake presets, visit the [CMake website](%cmake-preset-docs%).

Below is an example of the `my-qodana-preset` preset configuration:

```JSON
{
  "version": 3,
  "configurePresets": [
    {
      "name": "my-qodana-preset",
      "generator": "Ninja", 
      "binaryDir": "build",
      "cacheVariables": {
        "CMAKE_BUILD_TYPE": "Release",
        "CMAKE_C_COMPILER": "clang-16",
        "CMAKE_CXX_COMPILER": "clang++-16",
        "USE_OPENGL": true,
        "BUILD_EXTENSION": false
      }
    }
  ]
}
```

To run %product% invoking the `my-qodana-preset` preset, in the 
[`qodana.yaml`](qodana-yaml.md) file save the following configuration that uses the `cpp` and `cmakePreset` sections:

```yaml
cpp:
  cmakePreset: my-qodana-preset
```

> CLion scans CMake presets and creates an equivalent profile with the same name, and this profile overrides CMake presets.  
> However, CLion profiles are not explicitly supported by %product%.
{style="note"}

## Supported features

{id="clang-feature-matrix"}

<table>
    <tr>
        <td>Feature</td>
        <td>Supported by linter(s)</td>
        <td>Available under licenses</td>
    </tr>
    <tr>
        <td><a href="baseline.topic"/></td>
        <td>%cpp% <br/> %clang%</td>
        <td>Community, Ultimate and Ultimate Plus</td>
    </tr>
    <tr>
        <td><a href="quality-gate.topic"/></td>
        <td>%cpp% <br/> %clang%</td>
        <td>Community, Ultimate and Ultimate Plus</td>
    </tr>
    <tr>
        <td><a href="insights.md"/></td>
        <td>%cpp%</td>
        <td>Ultimate Plus</td>
    </tr>
    <tr>
        <td><a href="cloud-sso.md"/></td>
        <td>%cpp%</td>
        <td>Ultimate Plus</td>
    </tr>
</table>

## Usage statistics

<p>
    According to the <a href="https://www.jetbrains.com/legal/agreements/user_eap.html">JetBrains EAP user
    agreement</a>, we can use third-party services to analyze the usage of our features to further improve the
    user experience. All data is collected <a href="https://www.jetbrains.com/company/privacy.html">
    anonymously</a>. To disable the statistics, use the <code>--no-statistics=true</code> CLI option.
</p>
