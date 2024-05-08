# Python

<no-index/>

<show-structure for="chapter" depth="3"/>

<var name="qp" value="Qodana for Python"/>
<var name="qp-co" value="Qodana Community for Python"/>
<var name="qp-linter" value="jetbrains/qodana-python:2024.1"/>
<var name="qp-co-linter" value="jetbrains/qodana-python-community:2024.1"/>
<var name="qd-image" value="jetbrains/qodana-python<-community>:2024.1"/>
<var name="JenkinsCred" value="https://www.jenkins.io/doc/book/using/using-credentials/#adding-new-global-credentials"/>
<var name="ide" value="PyCharm"/>
<var name="Dplugin" value="https://plugins.jenkins.io/docker-plugin/"/>
<var name="DPplugin" value="https://plugins.jenkins.io/docker-workflow/"/>
<var name="Gplugin" value="https://plugins.jenkins.io/git/"/>
<var name="Dockeraccess" value="https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user"/>
<var name="MultipipeCreate" value="https://www.jenkins.io/doc/book/pipeline/multibranch/#creating-a-multibranch-pipeline"/>

<link-summary>You can analyze your code using the %qp% and %qp-co% linters.</link-summary>

<!-- Add a note about draft status -->

<warning>This is a draft document, so we do not recommend that you use it.</warning>

All %product% linters are based on IDEs designed for particular programming languages and frameworks. To analyze 
Python projects, you can use the following linters:

* %qp% is based on PyCharm Professional and licensed under the Ultimate and 
Ultimate Plus [licenses](pricing.md), 
* %qp-co% is based on PyCharm Community and licensed under the Community license.

To see the list of supported features, you can navigate to the [](#python-feature-matrix) section.

## Before your start

Create a [Qodana Cloud account](cloud-quickstart.md). In Qodana Cloud, obtain a [project token](project-token.md) that
will be used by %product% for identifying and verifying a license. 

If your project has external `pip` dependencies, set them up using the [`bootstrap`](before-running-qodana.md) 
key in the [`qodana.yaml`](qodana-yaml.md) file. For example, if your project dependencies are specified 
by the `requirements.txt` file in your project root, in the configuration file add the following line:

```yaml
bootstrap: pip install -r requirements.txt
```

## Run %product%

<note><include from="lib_qd.topic" element-id="docker-ram-note"/></note>

### JetBrains IDEs
{id="run-qodana-ides"}

You can run %instance% in IDE and forward inspection reports to [Qodana Cloud](cloud-about.topic) for storage and analysis purposes.

<procedure>
<step>
   <p>In the IDE, navigate to <ui-path>Tools | Qodana | Try Code Analysis with Qodana</ui-path>.</p> 
</step>
<step>
   <p>In the <ui-path>Run Qodana</ui-path> dialog, you can configure:</p>
      <list>
        <li>Options used by %product% in the <a href="qodana-yaml.md"><code>qodana.yaml</code></a> file</li>
         <li>The <a href="cloud-forward-reports.topic"><ui-path>Send inspection results to Qodana Cloud</ui-path></a> option using a <a href="cloud-projects.topic" anchor="cloud-manage-projects">project token</a></li>
         <li>The <a href="qodana-yaml.md"><ui-path>Save qodana.yaml in project root</ui-path></a> option</li>
         <li>The <a href="baseline.topic"><ui-path>Use Qodana analysis baseline</ui-path></a> option to run %product% with a baseline</li>
      </list>
   <img src="ide-plugin-run-qodana-2.png" width="793" alt="Configuring Qodana in the Run Qodana dialog" border-effect="line"/>
    <p>Click <ui-path>Run</ui-path> for inspecting your code.</p>
</step>
<step>
   <p>In the <ui-path>Server-Side Analysis</ui-path> tool window, see the <a href="qodana-ide-plugin.md" anchor="ide-plugin-study-reports">inspection results</a>.</p>
</step>
</procedure>

### GitHub Actions
{id="run-qodana-github"}

You can run %product% using the [Qodana Scan GitHub action](https://github.com/marketplace/actions/qodana-scan) as shown 
below.

<include from="lib_qd.topic" element-id="github-basic-configuration"/>

More configuration examples are available in the [](github.md) section.

### Jenkins
{id="run-qodana-jenkins"}

Make sure that these plugins are installed on your Jenkins instance:

* [Docker](%Dplugin%) and [Docker Pipeline](%DPplugin%) are required for running Docker images
* [git](%Gplugin%) is required for git operations in Jenkins projects

Make sure that Docker is installed and accessible by Jenkins.

If applicable, make sure that Docker is accessible by the `jenkins` user as described in the
[Manage Docker as a non-root user](%Dockeraccess%) section of the Docker documentation.

Create a Multibranch Pipeline project as described on the [Jenkins documentation portal](%MultipipeCreate%).

In the root directory of your project repository, create the `Jenkinsfile`. 

Save this snippet to the `Jenkinsfile`:

```groovy
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
```

In this configuration, the `environment` block defines the `QODANA_TOKEN` variable to invoke the
[project token](project-token.md).

More configuration examples are available in the [](jenkins.md) section.

### GitLab CI/CD
{id="run-qodana-gitlab"}

Make sure that your project repository is accessible by GitLab CI/CD.

In the root directory of your project, create the `.gitlab-ci.yml` file and save this configuration in it:

```yaml
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
```
Here: 
* The [`cache`](https://docs.gitlab.com/ee/ci/caching/) keyword configures GitLab CI/CD caches to store the %instance% cache,
so subsequent runs will be faster,
* The [`script`](https://docs.gitlab.com/ee/ci/yaml/#script) keyword runs the `qodana` command and enumerates the %instance%
configuration options described in the [](docker-image-configuration.topic) section,
* The `variables` keyword defines the `QODANA_TOKEN` [variable](https://docs.gitlab.com/ee/ci/variables/#define-a-cicd-variable-in-the-ui)
referring to the [project token](project-token.md). 

You can find more configuration examples in the [](gitlab.md) section.

### Local run
{id="run-qodana-locally"}

Because %product% linters are distributed in Docker containers, to run %product% locally you must have Docker installed and 
running locally. If you are using Linux, you should be able to run Docker under your current [non-root user](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user), check 
the [installation page](https://github.com/JetBrains/qodana-cli/releases/latest) for details.

You can run %product% locally using [Qodana CLI](https://github.com/JetBrains/qodana-cli) or Docker:

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
{id="explore-results-ides"}

You can get the latest %instance% report in your IDE as explained below.

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
        <p>By enabling the <ui-path>Always load most relevant Qodana report</ui-path> option, you get actual reports automatically retrieved from Qodana Cloud.</p>
      <img src="ide-plugin-connect-3.png" dark-src="ide-plugin-connect-3_dark.png" width="706" alt="Enabling to load the most relevant reports" border-effect="line"/>
        <p>In this case, the IDE will search and fetch from Qodana Cloud the report that has the revision ID corresponding to the 
        current revision ID (HEAD). If this report was not found, the IDE will select the previous report with the revision
        closest to the current revision ID (HEAD). Otherwise, the IDE retrieves the latest available report from Qodana Cloud.</p>
    </step> 
    <step>
       <p>In the <ui-path>Server-Side Analysis</ui-path> tool window, view <a href="qodana-ide-plugin.md" anchor="ide-plugin-study-reports">analysis results</a>.</p>
    </step>
</procedure>

### Qodana Cloud

Once %product% analyzed your project and uploaded the analysis results to Qodana Cloud, in 
[Qodana Cloud](https://qodana.cloud) navigate to your project and study the analysis results report.

<img src="qc-report-example.png" dark-src="qc-report-example_dark.png" alt="Analysis report example" width="720" border-effect="line"/>

<p>To learn more about %instance% report UI, see the <a href="ui-overview.md"/> section.</p>

## Extend %product% configuration

### Adjust the scope of analysis

Out of the box, Qodana provides two predefined profiles hosted on
[GitHub](https://github.com/JetBrains/qodana-profiles/tree/master/.idea/inspectionProfiles):

* `qodana.starter` is the default profile and a subset of the `qodana.recommended` profile,
* `qodana.recommended` is best for running in CI/CD pipelines and mostly implements the default %ide% profile, see the
  [PyCharm](https://www.jetbrains.com/help/pycharm/customizing-profiles.html) documentation for details.

You can customize %product% profiles using configurations in [YAML](custom-profiles.md) and [XML](custom-xml-profiles.md) formats. 

For example, you can enable JavaScript and TypeScript inspections by overriding the `qodana.recommended` profile as shown
below.

<procedure>
<step>
  <p>In the project directory, create a <a href="qodana-yaml.md"><code>qodana.yaml</code></a> file and save this profile configuration to it:</p>
<code-block lang="yaml">
name: "Enabling JavaScript and TypeScript" 
baseProfile: qodana.recommended
inspections:
   - group: "category:JavaScript and TypeScript" # Specify the inspection category
     enabled: true # Enable the JavaScript and TypeScript category
</code-block>
</step>
<step>
<p>In the <code>qodana.yaml</code> file, save this configuration to enable your profile:</p>
<code-block lang="yaml">
profile:
  path: &lt;relative-path-to-yaml-config-file&gt;
</code-block>
</step>
</procedure>

To learn more about configuration basics, visit the [](override-a-profile.md) section. Complete guides are 
available in the [](custom-profiles.md) and [](custom-xml-profiles.md) sections.

### Enable the baseline

You can skip analysis for specific problems using the [baseline](baseline.topic) feature. 

#### JetBrains IDEs
{id="enable-baseline-ides"}

<procedure>
    <step>In your IDE, navigate to the <ui-path>Problems</ui-path> tool window. </step>
    <step>In the <ui-path>Problems</ui-path> tool window, click the <ui-path>Server-Side Analysis</ui-path> tab.</step>
    <step>On the <ui-path>Server-Side Analysis</ui-path> tab, click the <ui-path>Try Locally</ui-path> button.</step>
    <step>In the dialog that opens, expand the <ui-path>Advanced configuration</ui-path> section and specify the path to the baseline file, and then click <ui-path>Run</ui-path>.</step>
</procedure>

#### GitHub Actions
{id="enable-baseline-github"}

This snippet contains the `args: --baseline,qodana.sarif.json` line that specifies the path to the SARIF-formatted file containing
a baseline:

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
              args: --baseline,qodana.sarif.json
            env:
              QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
</code-block>

#### Jenkins
{id="enable-baseline-jenkins"}

The `stages` block contains the `--baseline <path/to/qodana.sarif.json>` line that specifies
the path to the SARIF-formatted file containg information about a baseline:

```groovy
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
                --baseline <path/to/qodana.sarif.json>
                '''
            }
        }
    }
}
```

#### GitLab CI/CD
{id="enable-baseline-gitlab"}

You can use the  `--baseline <path/to/qodana.sarif.json>` line in the `script` block to
invoke the baseline feature.

```yaml
qodana:
   image:
      name: jetbrains/qodana-<linter>
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
      - qodana --baseline <path/to/qodana.sarif.json> --results-dir=$CI_PROJECT_DIR/.qodana/results
         --cache-dir=$CI_PROJECT_DIR/.qodana/cache
   artifacts:
      paths:
         - qodana/report/
      expose_as: 'Qodana report'
```


#### Local run
{id="enable-baseline-local-run"}

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

### Enable the quality gate

You can configure [quality gates](quality-gate.topic) for the total number of project problems, specific problem severities, and code 
coverage by saving this snippet to the [`qodana.yaml`](qodana-yaml.md) file: 

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

### Analyze pull requests

#### GitHub Actions
{id="pull-requests-github"}

In GitHub Actions, `--diff-start` can be omitted because it will be added automatically while running
%product%, so you can follow this procedure:
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


#### GitLab CI/CD
{id="pull-requests-gitlab"}

In the root directory of your project, save the `.gitlab-ci.yml` file containing the following snippet:

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

Here, the `--diff-start` option specifies a hash of the commit that will act as a base for comparison.

#### Local run
{id="pull-requests-local-run"}

To analyze changes in your code, employ the `--diff-start` option and specify a hash of the commit that will act as a
base for comparison:

<tabs group="cli-settings">
    <tab title="Qodana CLI" group-key="qodana-cli">
        <code-block lang="shell" prompt="$">
            qodana scan \
            &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
            &nbsp;&nbsp;&nbsp;-l %qd-image% \
            &nbsp;&nbsp;&nbsp;--diff-start=&lt;GIT_START_HASH&gt;
        </code-block>
    </tab>
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$">
            docker run \
            &nbsp;&nbsp;&nbsp;-v $(pwd):/data/project/ \
            &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
            &nbsp;&nbsp;&nbsp;%qd-image% \
            &nbsp;&nbsp;&nbsp;--diff-start=&lt;GIT_START_HASH&gt;
        </code-block>
    </tab>
</tabs>

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
            <p>MongoJS</p>
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
| [](code-coverage.md)          | &#x274c; | &#x2714;  |
| [](license-audit.topic)       | &#x274c; | &#x2714;  |
| [](quick-fix.md)              | &#x274c; | &#x2714;  |
| [](vulnerability-checker.md)  | &#x274c; | &#x2714;  |




