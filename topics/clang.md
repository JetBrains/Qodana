# C / C++

<show-structure for="chapter" depth="3"/>

<!-- Linter-related variables -->
<var name="qp" value="Qodana for C/C++"/>
<var name="qp-linter" value="jetbrains/qodana-clang:2024.2-eap"/>
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
<var name="clang-tidy" value="https://clang.llvm.org/extra/clang-tidy"/>
<var name="clang-config" value="https://gist.github.com/fbaeuerlein/2895f889e451a817d7b2b36fd60e2873"/>
<var name="dockerfile" value="https://github.com/JetBrains/qodana-docker/blob/main/2024.2/base/cpp.Dockerfile"/>
<var name="dockerfile-internal" value="https://github.com/JetBrains/qodana-docker/blob/main/2024.2/cpp/internal.Dockerfile"/>
<var name="clang-website" value="https://clang.llvm.org/extra/clang-tidy/checks/list.html"/>
<var name="clion-inspections-general" value="https://www.jetbrains.com/help/clion/list-of-c-cpp-inspections.html#general"/>
<var name="misra-inspections" value="https://www.jetbrains.com/help/clion/list-of-c-cpp-inspections.html#stat-analysis-tools"/>
<var name="compdb-generate" value="https://www.jetbrains.com/help/clion/compilation-database.html#compdb_generate"/>

<var name="linter-shell" value="qodana-clang:2024.2-eap"/>
<var name="code-inspection-ide-help-url" value="https://www.jetbrains.com/help/clion/list-of-c-cpp-inspections.html#general"/>
<var name="code-inspection-profiles-ide-help-url" value="https://www.jetbrains.com/help/idea/?Customizing_Profiles"/>
<var name="GitHubLink" value="https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository"/>
<var name="teamcity-linter-list" value="Here, select Custom and in the field below specify the %qp% linter."/>

<link-summary>%qp% lets you analyze C and C++ projects containing compilation databases. </link-summary>

<note>
%qp% is currently in Early Access, which means it may not be reliable, may not work as intended, and may contain errors.
Any use of the EAP product is at your own risk. Your feedback is very welcome in our 
<a href="https://youtrack.jetbrains.com/newIssue?project=QD">issue tracker</a> or at
<a href="mailto:qodana-support@jetbrains.com">qodana-support@jetbrains.com</a>.
</note>

%qp% lets you analyze C and C++ projects containing
[compilation databases](https://clang.llvm.org/docs/JSONCompilationDatabase.html). This linter is based on the
[Clang-Tidy](%clang-tidy%) linter and works on the AMD64 and ARM64 architectures.

%qp% extends the existing Clang-Tidy inspections by supplying the `Clang-Tidy` and `MISRA checks` inspections provided by
CLion.

%qp% is available under the Community, Ultimate, and Ultimate Plus licenses. However, the `Clang-Tidy` and
`MISRA checks` inspections from CLion are available only under the Ultimate and Ultimate Plus licenses.

<tip>
<p>You can learn more inspections using these links:</p>
<list>
<li><a href="%clang-website%">Standard Clang-Tidy inspections</a>,</li>
<li><a href="%clion-inspections-general%">CLion's Clang-Tidy inspections</a>,</li>
<li><a href="%misra-inspections%">CLion's MISRA checks</a>.</li>
</list>
</tip>

To see the list of supported features, navigate to the [](#clang-feature-matrix) section.

## How it works

The Docker image of %qp% employs Clang 16.0.0 and LLVM 16. You can see the
[`Dockerfile`](%dockerfile%) for the detailed description of all software employed by the linter.

The linter searches for the compilation database file contained in the `build/compile_commands.json` file of the
project directory and reads this file, analyzes the project, generates analysis reports, and saves them locally or
uploads to Qodana Cloud.

## Before you start
{id="clang-before-you-start"}

### Prepare your project

<procedure>
    <step>Make sure that Clang-Tidy is deployed on your system. If necessary, install it using the 
        <a href="https://releases.llvm.org/download.html">LLVM website</a>.
    </step>
    <step>
        <p>You can configure inspections in the <code>.clang-tidy</code> file, see the configuration example on the
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
        <p>To obtain the list of all inspections enabled in Clang-Tidy by default, you can run the following command:</p>
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
    <step><p>Open the <code>.clang-tidy</code> file and configure the list of files and paths that will be analyzed by %qp%.</p>
        <tip>If you already have the <code>compile_commands.json</code> file, you can also configure files and paths in this file.</tip>
    </step>
    <step>
        <p>Generate the <code>compile_commands.json</code> file as explained in the <a href="%compdb-generate%">CLion documentation portal</a>, 
        and save it to the <code>build</code> directory under the project root.</p>
        <p>If you use CMake, you can also generate a compilation database by specifying the following 
        <a href="before-running-qodana.md"><code>bootstrap</code></a> option in the <code>qodana.yaml</code> file, for example:</p>
        <code-block lang="yaml">
        bootstrap: mkdir -p build; cd build;cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=ON .. || true
        </code-block>
    </step>
    <step>
        <p>If your project requires specific packages not previously mentioned in the 
        <a href="%dockerfile%"><code>Dockerfile</code></a>, add the following <code>bootstrap</code> command to your 
        <code>qodana.yaml</code> file to install the required packages:</p>
        <code-block lang="yaml">
        bootstrap: sudo apt-get update; sudo apt-get install -y &lt;list of required packages&gt; |
        &nbsp;&nbsp;rm -rf build;  mkdir -p build; cd build;cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=ON .. || true
        </code-block>
    </step>
</procedure>

### Qodana Cloud

<note>
Clang-Tidy and MISRA checks inspections from CLion are available only under the Ultimate and Ultimate Plus licenses.
</note>

<include from="lib_qd.topic" element-id="before-start-qodana-cloud" use-filter="empty,clang"/>


### Prepare your software

<include from="lib_qd.topic" element-id="before-start-prepare-software" use-filter="empty,generic"/>

## Run %product%

<note><include from="lib_qd.topic" element-id="docker-ram-note"/></note>

<include from="lib_qd.topic" element-id="root-and-non-root-users-info-bubble"></include>

Based on the [prerequisites](#Prepare+your+project), linter reads the `build/compile_commands.json` file and runs the Clang-Tidy tool.

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
      <note>This feature is in experimental mode, which means that its operation can be unstable.</note>
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
                      uses: JetBrains/qodana-action@v2024.2
                      with:
                        args: --linter,%qp-linter%
                      env:
                        QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
          </code-block>
        <p>Here, <code>fetch-depth: 0</code> is required for checkout in case Qodana works in pull request mode
                (reports issues that appeared only in that pull request).</p>
        <p>To override the location of a compilation command database, you can specify the location for the
            <code>compile_commands.json</code> file relatively to the project root, so the configuration will look like:
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
                        args: --linter,%qp-linter%,--compile-commands,&lt;path-to-compile_commands.json&gt;
                      env:
                        QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
          </code-block>


  <p>More configuration examples are available in the <a href="github.md"/> section.</p>
    </tab>
    <tab title="Jenkins" group-key="jenkins">
        <note>This feature is in experimental mode, which means that its operation can be unstable.</note>
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
        <p>To override the location of a compilation command database, you can specify the location for the
            <code>compile_commands.json</code> file relatively to the project root, so the configuration will look like:
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
                        image '%qp-linter%'
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
        <p>More configuration examples are available in the <a href="jenkins.md"/>section.</p>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab">
        <note>This feature is in experimental mode, which means that its operation can be unstable.</note>
        <p>In the root directory of your project, save this snippet to the <code>.gitlab-ci.yml</code> file:</p>
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
        <p>To override the location of a compilation command database, you can specify the location for the
            <code>compile_commands.json</code> file relatively to the project root, so the configuration will look like:
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
                  QODANA_TOKEN: $qodana_token           - 
               script:
                  - qodana --cache-dir=$CI_PROJECT_DIR/.qodana/cache --compile-commands &lt;path-to-compile_commands.json&gt;
        </code-block>
    <p>More configuration examples are available in the <a href="gitlab.md"/>section.</p>
    </tab>
    <tab title="TeamCity" group-key="teamcity" id="jvm-run-qodana-teamcity">
      <include from="lib_qd.topic" element-id="teamcity-add-a-qodana-runner" use-filter="empty,clang,clang-compilation-override"/>
      <p>More configuration examples are available in the <a href="teamcity.md"/>section.</p>
    </tab>
    <tab title="Command line" group-key="command-line">
        <note> Running analysis is a resource-intensive operation. If you experience issues, consider increasing the Docker
                Desktop runtime memory limit, which by default is set to 2 GB. See the Docker Desktop documentation for 
                <a href="https://docs.docker.com/desktop/windows/#resources">Windows</a> and 
                <a href="https://docs.docker.com/desktop/mac/#resources">macOS</a>.
        </note>
        <p>Run this command:</p>
        <code-block lang="shell" prompt="$">
            docker run \
            &nbsp;&nbsp;&nbsp;-v &lt;source-directory&gt;/:/data/project/ \
            &nbsp;&nbsp;&nbsp;-v &lt;output-directory&gt;/:/data/results/ \
            &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
            &nbsp;&nbsp;&nbsp;%qp-linter%
        </code-block>
        <p>
            In this command, <code>source-directory</code> and <code>output-directory</code> are full local paths
            to the project source code directory and the 
            <a href="qodana-inspection-output.md" anchor="Basic+output">analysis result</a> directory, respectively. The
            <code>QODANA_TOKEN</code> variable refers to the <a href="project-token.md">project token</a>
            required by the
            <a href="pricing.md" anchor="pricing-linters-licenses">Ultimate and Ultimate Plus</a> linters.
            If you omit the <code>QODANA_TOKEN</code> variable, the inspection results will be available in the
            <code>qodana.sarif.json</code> file saved in the <code>output-directory</code> of your project root.
        </p>
        <p>To override the location of a compilation command database, you can specify the location for the
            <code>compile_commands.json</code> file relatively to the project root, so the Docker command will look like:
        </p>
        <code-block lang="shell" prompt="$">
            docker run \
            &nbsp;&nbsp;&nbsp;-v &lt;source-directory&gt;/:/data/project/ \
            &nbsp;&nbsp;&nbsp;-v &lt;output-directory&gt;/:/data/results/ \
            &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
            &nbsp;&nbsp;&nbsp;%qp-linter% \
            &nbsp;&nbsp;&nbsp;--compile-commands &lt;path-to-compile_commands.json&gt;
        </code-block>
        <p>In your browser, open <a href="https://qodana.cloud">Qodana Cloud</a> to examine analysis results and
          reconfigure the analysis, see the <a href="ui-overview.md"/> section for
            details.</p>
        <p>If you run the analysis several times in a row, make sure you've cleaned the results directory before using it in 
        <code>docker run</code> again.</p>
    </tab>
</tabs>
  <!--</tab>-->
<!--</tabs>-->

## Explore analysis results

<p>Once %product% analyzed your project and uploaded the analysis results to Qodana Cloud, in
<a href="https://qodana.cloud">Qodana Cloud</a> navigate to your project and review the analysis results report.</p>
<img src="qc-report-example-clang.png" alt="Analysis report example" width="720" border-effect="line"/>
<p>To learn more about %instance% report UI, see the <a href="ui-overview.md"/> section.</p>

<!-- Here add about observing locally generated files -->

## Extend %product% configuration

### Adjusting the scope of analysis

<p>
    %product% recognizes the <code>qodana.yaml</code> file for the analysis configuration,
    so that you don't need to pass any additional parameters. For %qp%, you can configure:</p>
<list>
    <li>Inspections using the <code>include</code> and <code>exclude</code> options. See the
        <a href="qodana-yaml.md" anchor="Example+of+different+configuration+options">YAML file</a> section for details.</li>
    <li>Commands that will run before the linter using the <a href="before-running-qodana.md"><code>boostrap</code></a>
        option.</li>
    <li><a anchor="Enabling+the+baseline">Baseline</a> and <a anchor="Enabling+the+quality+gate">quality gate</a> features.</li>
</list>


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
                  uses: JetBrains/qodana-action@v2024.2
                  with:
                    args: --linter,%qp-linter%,--baseline,&lt;path/to/qodana.sarif.json&gt;
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
        <include from="lib_qd.topic" element-id="teamcity-add-a-qodana-runner" use-filter="empty,clang,baseline"/>
    </tab>
    <tab title="Command line" group-key="command-line">
          <p>Run this command invoking the <code>--baseline</code> option:</p>
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
<!--  </tab>
</tabs>-->


### Enabling the quality gate

<link-summary>You can configure quality gates for the total number of problems and for specific severities.</link-summary>

You can configure [quality gates](quality-gate.topic) for:

* The total number of project problems, 
* Multiple quality gates for <a href="faq.topic" anchor="faq-severities">problem severities</a>.

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


## Supported features
{id="clang-feature-matrix"}

The %qp% linter provides the following %product% features:

<table>
    <tr>
        <td>Feature</td>
        <td>Available under licenses</td>
    </tr>
    <tr>
        <td><a href="baseline.topic"/></td>
        <td>Community, Ultimate and Ultimate Plus</td>
    </tr>
    <tr>
        <td><a href="quality-gate.topic"/></td>
        <td>Community, Ultimate and Ultimate Plus</td>
    </tr>
</table>

## Usage statistics

<p>
    According to the <a href="https://www.jetbrains.com/legal/agreements/user_eap.html">JetBrains EAP user
    agreement</a>, we can use third-party services to analyze the usage of our features to further improve the
    user experience. All data is collected <a href="https://www.jetbrains.com/company/privacy.html">
    anonymously</a>. To disable the statistics, use the <code>--no-statistics=true</code> CLI option.
</p>
