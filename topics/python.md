[//]: # (title: Python)

<no-index/>

<show-structure for="chapter" depth="3"/>

<var name="qp" value="Qodana for Python"/>
<var name="qp-co" value="Qodana Community for Python"/>
<var name="qp-linter" value="jetbrains/qodana-python:2024.2-eap"/>
<var name="qp-co-linter" value="jetbrains/qodana-python-community:2024.2-eap"/>
<var name="qd-image" value="jetbrains/qodana-python<-community>:2024.2-eap"/>
<var name="JenkinsCred" value="https://www.jenkins.io/doc/book/using/using-credentials/#adding-new-global-credentials"/>
<var name="ide" value="PyCharm"/>
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

<link-summary>You can analyze your Python code using the %qp% and %qp-co% linters.</link-summary>

<warning>This is a draft document, so we do not recommend that you use it.</warning>

All %product% linters are based on IDEs designed for particular programming languages and frameworks. To analyze 
Python projects, you can use the following linters:

* %qp% is based on PyCharm Professional and licensed under the Ultimate and 
Ultimate Plus [licenses](pricing.md), 
* %qp-co% is based on PyCharm Community and licensed under the Community license.

To see the list of supported features, you can navigate to the [](#python-feature-matrix) section.

## Before your start
{id="python-before-you-start"}

If your project has external `pip` dependencies, set them up using the [`bootstrap`](before-running-qodana.md) 
key in the [`qodana.yaml`](qodana-yaml.md) file. For example, if your project dependencies are specified 
by the `requirements.txt` file in your project root, in the configuration file add the following line:

```yaml
bootstrap: pip install -r requirements.txt
```

## Run %product%

<note><include from="lib_qd.topic" element-id="docker-ram-note"/></note>

### JetBrains IDEs
{id="python-run-qodana-ides"}

You can run %instance% in %ide% and send inspection reports to [Qodana Cloud](cloud-about.topic) for storage and analysis purposes. 

<procedure>
<step>
   <p>In %ide%, navigate to <ui-path>Tools | Qodana | Try Code Analysis with Qodana</ui-path>.</p> 
</step>
<step>
   <p>On the <ui-path>Run Qodana</ui-path> dialog, you can configure %product%.</p>
   <img src="ide-plugin-run-qodana-2.png" width="793" alt="Configuring Qodana in the Run Qodana dialog" border-effect="line"/>
    <p>This dialog contains the following components:</p>
      <table>
        <tr>        
          <td>Name</td>
          <td>Description</td>
        </tr>
        <tr>
          <td>The <code>qodana.yaml</code> file</td>
          <td>In the text field, you can set up code analysis used by Qodana in this file. You can learn more about available <a href="qodana-yaml.md">configuration options</a></td>
        </tr>
        <tr>
          <td>The <ui-path>Send inspection results to Qodana Cloud</ui-path> option</td>
          <td>If you want to <a href="cloud-forward-reports.topic">send reports to Qodana Cloud</a>, you can check this option and paste the <a href="project-token.md">project token</a> generated in <a href="cloud-projects.topic" anchor="cloud-manage-projects">Qodana Cloud</a></td>
        </tr>
        <tr>
          <td>The <ui-path>Save qodana.yaml in project root</ui-path> option</td>
          <td>By checking this option, you can save the %product% configuration made on this dialog to the <a href="qodana-yaml.md"><code>qodana.yaml</code></a> file in the project root of your project</td>
        </tr>
        <tr>
          <td>The <ui-path>Use Qodana analysis baseline</ui-path> option</td>
          <td>Using the <a href="baseline.topic">baseline</a> feature, you can skip analysis for specific problems</td>
        </tr>
      </table>
    <p>Click <ui-path>Run</ui-path> for analyzing your code.</p>
</step>
<step>
   <p>On the <ui-path>Server-Side Analysis</ui-path> tab of the <ui-path>Problems</ui-path> tool window, see the <a href="qodana-ide-plugin.md" anchor="ide-plugin-study-reports">inspection results</a>.</p>
</step>
</procedure>

<!--The examples below require a [project token](project-token.md) related to
%product% license. To generate a project token, you need to [create a Qodana Cloud account](cloud-get-access.topic), and then 
follow the instructions from the [](cloud-quickstart.md) section.--> 

### CI/CD
{id="python-run-qodana-cicd"}

Before running %product%, create a [Qodana Cloud account](cloud-quickstart.md). In Qodana Cloud, generate a
[project token](project-token.md) that will be used by %product% for identifying and verifying a license. In Qodana Cloud,
you can review [inspection reports](#python-explore-results-qodana-cloud).

<tabs>
<tab title="GitHub Actions">
<p>You can run %product% using the <a href="https://github.com/marketplace/actions/qodana-scan">Qodana Scan GitHub action</a> 
as shown below.</p>

<include from="lib_qd.topic" element-id="github-basic-configuration"/>

<p>More configuration examples are available in the <a href="github.md"/> section.</p>
</tab>
<tab title="Jenkins">
<p>Make sure that these plugins are installed on your Jenkins instance:</p>
<list>
<li><a href="%Dplugin%">Docker</a> and <a href="%DPplugin%">Docker Pipeline</a> are required for running Docker images,</li>
<li><a href="%Gplugin%">git</a> is required for git operations in Jenkins projects.</li>
</list>
<p>Make sure that Docker is installed and accessible by Jenkins.</p>
<p>If applicable, make sure that Docker is accessible by the <code>jenkins</code> user as described in the
<a href="%Dockeraccess%">Manage Docker as a non-root user</a> section of the Docker documentation.</p>
<p>Create a Multibranch Pipeline project as described on the <a href="%MultipipeCreate%">Jenkins documentation portal</a>.</p>
<p>In the root directory of your project repository, create the <code>Jenkinsfile</code>.</p>
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
            image '%qd-image%'
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
<tab title="GitLab CI/CD">
<p>Make sure that your project repository is accessible by GitLab CI/CD.</p>
<p>In the root directory of your project, create the <code>.gitlab-ci.yml</code> file and save this configuration in it:</p>
<code-block lang="yaml">
qodana:
   image:
      name: %qd-image%
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
</tab>
<tab title="TeamCity">
  <include from="teamcity.md" element-id="teamcity-add-a-qodana-runner"/>
</tab>
</tabs>

### Command line
{id="python-run-qodana-locally"}

>Before running %product%, create a [Qodana Cloud account](cloud-quickstart.md). In Qodana Cloud, generate a
[project token](project-token.md) that will be used by %product% for identifying and verifying a license. In Qodana Cloud,
you can review [inspection reports](#python-explore-results-qodana-cloud).
{style="note"}

You have two options to run %product% locally: you can either run [Qodana CLI](https://github.com/JetBrains/qodana-cli) or directly use the Docker image of %product%.
As %product% linters are distributed in Docker containers, Docker needs to be installed on your local machine.  
If you are using Linux, you should be able to run Docker under your current [non-root user](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user), check 
the [installation page](https://github.com/JetBrains/qodana-cli/releases/latest) for details.

Here are the examples of how you can run %product% locally. 

<tabs group="cli-settings">
    <tab group-key="qodana-cli" title="Qodana CLI">
        <code-block prompt="$">
            qodana scan \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               -l %qd-image%
        </code-block>
        <p>Here, the <code>QODANA_TOKEN</code> variable refers to the <a href="project-token.md">project token</a>.</p>
        <p>If you omit the <code>-l</code> option, the %qp% linter will run by default.</p>
    </tab>
    <tab group-key="docker-image" title="Docker image">
        <p>To start, pull the image from Docker Hub (only necessary to get the latest version):</p>
        <code-block lang="shell" prompt="$">
            docker pull %qd-image%
        </code-block>
        <p>Start local analysis with <code>source-directory</code> pointing to the root of your project and
            <code>QODANA_TOKEN</code> referring to the <a href="project-token.md">project token</a>:</p>
        <code-block lang="shell" prompt="$">
            docker run \
               -v &lt;source-directory&gt;/:/data/project/ \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               %qd-image%
        </code-block>
        <p>In your browser, open <a href="https://qodana.cloud">Qodana Cloud</a> to examine analysis results and
reconfigure the analysis, see the <a href="ui-overview.md"/> section for
            details.</p>
    </tab>
</tabs>

## Explore analysis results

### JetBrains IDEs
{id="python-explore-results-ides"}

You can load the latest %instance% report from [Qodana Cloud](#python-explore-results-qodana-cloud) to your IDE as explained below.

<procedure>
   <step>
      <p>In your IDE, navigate to <ui-path>Tools | Qodana | Log in to Qodana</ui-path>.</p>
   </step>
   <step>
      <p>
         In the <ui-path>Settings</ui-path> dialog, click <ui-path>Log in</ui-path>.
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

### Qodana Cloud
{id="python-explore-results-qodana-cloud"}

Once %product% analyzed your project and uploaded the analysis results to Qodana Cloud, in 
[Qodana Cloud](https://qodana.cloud) navigate to your project and review the analysis results report.

<img src="qc-report-example.png" dark-src="qc-report-example_dark.png" alt="Analysis report example" width="720" border-effect="line"/>

<p>To learn more about %instance% report UI, see the <a href="ui-overview.md"/> section.</p>

## Extend %product% configuration

### Adjusting the scope of analysis

Out of the box, Qodana provides two predefined profiles hosted on
[GitHub](https://github.com/JetBrains/qodana-profiles/tree/master/.idea/inspectionProfiles):

* `qodana.starter` is the default profile and a subset of the more comprehensive `qodana.recommended` profile,
* `qodana.recommended` is suitable for running in CI/CD pipelines and mostly implements the default %ide% profile, see the
  [PyCharm](https://www.jetbrains.com/help/pycharm/customizing-profiles.html) documentation for details.

You can customize %product% profiles using configurations in [YAML](custom-profiles.md) and [XML](custom-xml-profiles.md) formats.
To learn more about configuration basics, visit the [](override-a-profile.md) section.

### Enabling the baseline

You can skip analysis for specific problems using the [baseline](baseline.topic) feature. Information about a baseline is contained
in a SARIF-formatted file.

#### JetBrains IDEs
{id="python-enable-baseline-ides"}

<procedure>
    <step>In your IDE, navigate to the <ui-path>Problems</ui-path> tool window. </step>
    <step>In the <ui-path>Problems</ui-path> tool window, click the <ui-path>Server-Side Analysis</ui-path> tab.</step>
    <step>On the <ui-path>Server-Side Analysis</ui-path> tab, click the <ui-path>Try Locally</ui-path> button.</step>
    <step>On the dialog that opens, expand the <ui-path>Advanced configuration</ui-path> section and specify the path to the baseline file, and then click <ui-path>Run</ui-path>.</step>
</procedure>

#### CI/CD
{id="python-enable-baseline-cicd"}

<tabs>
<tab title="GitHub Actions">
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
            uses: JetBrains/qodana-action@v2024.1
            with:
              args: --baseline,qodana.sarif.json
            env:
              QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
</code-block>
</tab>
<tab title="Jenkins">
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
            image '%qd-image%'
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
<tab title="GitLab CI/CD">
<p>You can use the  <code>--baseline &lt;path/to/qodana.sarif.json&gt;</code> line in the <code>script</code> block to
invoke the baseline feature.</p>
<code-block lang="yaml">
qodana:
   image:
      name: %qd-image%
      entrypoint: [""]
   cache:
      - key: qodana-2024.1-$CI_DEFAULT_BRANCH-$CI_COMMIT_REF_SLUG
        fallback_keys:
           - qodana-2024.1-$CI_DEFAULT_BRANCH-
           - qodana-2024.1-
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
<tab title="TeamCity">

Using the **Additional Qodana arguments** field of the [`Qodana`](teamcity.md#teamcity-qodana-runner) runner configuration, 
you can configure the [baseline](baseline.topic) feature by adding the `--baseline <path/to/qodana.sarif.json>` option. 

</tab>
</tabs>

#### Command line
{id="python-enable-baseline-local-run"}

In these snippets, the `--baseline` option configures the path to the SARIF-formatted file containin a baseline: 

<tabs group="cli-settings">
    <tab group-key="qodana-cli" title="Qodana CLI">
        <code-block prompt="$">
            qodana scan \
               -v &lt;path_to_baseline&gt;:/data/base/ \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               -l %qd-image% \
               --baseline /data/base/qodana.sarif.json
        </code-block>
    </tab>
    <tab group-key="docker-image" title="Docker image">
        <code-block lang="shell" prompt="$">
            docker run \
               -v &lt;source-directory&gt;/:/data/project/ \
               -v &lt;path_to_baseline&gt;:/data/base/ \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               %qd-image% \
               --baseline /data/base/qodana.sarif.json
        </code-block>
    </tab>
</tabs>

### Enabling the quality gate

You can configure [quality gates](quality-gate.topic) for the total number of project problems and specific problem 
severities in both linters, and code coverage thresholds available only in the %qp% linter, by saving this snippet to 
the [`qodana.yaml`](qodana-yaml.md) file: 

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

#### CI/CD
{id="python-pull-requests-cicd"}

<tabs>
<tab title="GitHub Actions">
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
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;uses: JetBrains/qodana-action@v2024.1
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;env:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
</code-block>
</step>
</procedure>
</tab>
<tab title="GitLab CI/CD">
<p>In the root directory of your project, save the <code>.gitlab-ci.yml</code> file containing the following snippet:</p>
<code-block lang="yaml">
            qodana:
   image:
      name: %qd-image%
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
<p>Here, the <code>--diff-start</code> option specifies a hash of the commit that will act as a base for comparison.</p>
</tab>
<tab title="TeamCity">
<p>Information about configuring TeamCity for analyzing pull and merge requests is available on the 
<a href="%TeamCityPullRequests%">TeamCity</a> documentation portal.
</p>
</tab>
</tabs>

#### Command line
{id="python-pull-requests-local-run"}

To analyze changes in your code, employ the `--diff-start` option and specify a hash of the commit that will act as a
base for comparison:

<code-block lang="shell" prompt="$">
    docker run \
    &nbsp;&nbsp;&nbsp;-v $(pwd):/data/project/ \
    &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
    &nbsp;&nbsp;&nbsp;%qd-image% \
    &nbsp;&nbsp;&nbsp;--diff-start=&lt;GIT_START_HASH&gt;
</code-block>

## Supported technologies and features
{id="python-feature-matrix"}

This table contains the list of technologies supported by both linters.

<table style="none">
    <tr>
        <td>Programming languages</td>
        <td>
            <p>Python</p>
        </td>
    </tr>
    <tr>
        <td>Frameworks and libraries</td>
        <td>
            <p>Django</p>
            <p>Google App Engine</p>
            <p>Jupyter</p>
            <p>Pyramid</p>
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
            <p>SQL Server</p>
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

Here is the list of %product% features supported per each linter.

| Feature                       | %qp-co%  | %qp%      |
|-------------------------------|----------|-----------|
| [](baseline.topic)            | &#x2714; | &#x2714;  |
| [](quality-gate.topic)        | &#x2714; | &#x2714;  |
| [](code-coverage.md)          | &nbsp;   | &#x2714;  |
| [](license-audit.topic)       | &nbsp;   | &#x2714;  |
| [](quick-fix.md)              | &nbsp;   | &#x2714;  |
| [](vulnerability-checker.md)  | &nbsp;   | &#x2714;  |



