# Python

<no-index/>

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

You can analyze your Python projects using the %qp% linter based on PyCharm Professional and licensed under the Ultimate and 
Ultimate Plus licenses, and the %qp-co% linter based on PyCharm Community and licensed under the Community license. 
To learn more about %product% licenses, navigate to the [](pricing.md) section. To see the list of supported features, you
can navigate to the [](#python-feature-matrix) section.

## Before your start

%qp% requires a valid %product% license for running, which can be identified and verified using a [project token](project-token.md) generated in 
Qodana Cloud. If you use the %qp-co% linter, the project token is optional.

If your project has external `pip` dependencies, set them up using the [`bootstrap`](before-running-qodana.md) 
field in the `qodana.yaml` file. For example, if your project dependencies are specified by the `requirements.txt` file 
in your project root, add the following line to [`qodana.yaml`](qodana-yaml.md#Run+custom+commands) that will be 
executed before the analysis:

```yaml
bootstrap: pip install -r requirements.txt
```

## Run %product%

<note><include from="lib_qd.topic" element-id="docker-ram-note"/></note>

### Run %product% locally

By default, you can run %product% using [Qodana CLI](https://github.com/JetBrains/qodana-cli). If necessary,
check the [installation page](https://github.com/JetBrains/qodana-cli/releases/latest) to install Qodana CLI.  To run it in the default mode, you must have Docker or Podman 
installed and running locally. If you are using Linux, you should be able to run Docker under your current
[non-root user](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user).

<include from="lib_qd.topic" element-id="root-and-non-root-users-info-bubble"></include>

Alternatively, you can use the Docker commands from the <ui-path>Docker image</ui-path> tab.

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
        <p>In your browser, open <a href="https://qodana.cloud">Qodana Cloud</a> to examine analysis results.
            Here, you can also reconfigure the analysis, see the <a href="ui-overview.md"/> section for
            details.</p>
    </tab>
</tabs>

### Run %product% in CI/CD pipelines

You can also set up analysis in various CI/CD tools. 

#### GitHub Actions

<include from="lib_qd.topic" element-id="github-basic-configuration"/>

#### Jenkins

Make sure that these plugins are installed on your Jenkins instance:

* [Docker](%Dplugin%) and [Docker Pipeline](%DPplugin%) are required for running Docker images
* [git](%Gplugin%) is required for git operations in Jenkins projects

Make sure that Docker is installed and accessible by Jenkins.

If applicable, make sure that Docker is accessible by the `jenkins` user as described in the
[Manage Docker as a non-root user](%Dockeraccess%) section of the Docker documentation.

Create a Multibranch Pipeline project as described on the [Jenkins documentation portal](%MultipipeCreate%).

In the root directory of your project repository, create the `Jenkinsfile`. 

Save this snippet to `Jenkinsfile`:

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
[project token](project-token.md) generated in Qodana Cloud.

#### GitLab CI/CD

Make sure that your project repository is accessible by GitLab CI/CD.

In the root directory of your project, create the `.gitlab-ci.yml` file. Save this configuration to the `.gitlab-ci-yml` 
file:

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
referring to the [project token](project-token.md) generated in Qodana Cloud. 

You can find more examples in the [](ci.md) section.

### Explore analysis results

#### View results in Qodana Cloud

Once %product% analyzed your project uploaded the analysis results to Qodana Cloud, in 
[Qodana Cloud](https://qodana.cloud) navigate to your project and study the analysis results report.

<img src="qc-report-example.png" dark-src="qc-report-example_dark.png" alt="Analysis report example" width="720" border-effect="line"/>

<p>To learn more about %instance% report UI, see the <a href="ui-overview.md"/> section.</p>

#### Receive analysis results in %ide%

You can get the latest %instance% report in your %ide% as explained below.

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
        <p>In this case, %ide% will search and fetch from Qodana Cloud the report that has the revision ID corresponding to the 
        current revision ID (HEAD). If this report was not found, %ide% will select the previous report with the revision
        closest to the current revision ID (HEAD). Otherwise, %ide% retrieves the latest available report from Qodana Cloud.</p>
    </step> 
    <step>
       <p>In the <ui-path>Server-Side Analysis</ui-path> tool window, view <a href="qodana-ide-plugin.md" anchor="ide-plugin-study-reports">analysis results</a>.</p>
    </step>
</procedure>

Using the **Server-Side Analysis** tool window of %ide%, you can view %instance% reports and navigate to the code fragments
containing such problems.

<img src="ide-plugin-report-navigating.png" dark-src="ide-plugin-report-navigating_dark.png" width="706" alt="Navigating to problems in the IDE" animated="true" border-effect="line"/>

The upper part of the **Server-Side Analysis** tool window contains information about the project and branch names, the 
analysis date, and the number of problems. The left part contains several buttons.

<img src="ide-plugin-report-navigating-buttons.png" dark-src="ide-plugin-report-navigating-buttons_dark.png" width="460" alt="Functionalities of the Server-Side Analysis tool window" border-effect="line"/>

This table explains each button from top to bottom:

<table>
   <tr>
      <td>Button</td>
      <td>Description</td>
   </tr>
   <tr>
      <td><ui-path>Close Report</ui-path></td>
      <td>Close the report that was previously opened</td>
   </tr>
   <tr>
      <td><ui-path>Refresh Report</ui-path></td>
      <td>Download the updated version of the report from Qodana Cloud. This requires that you first link your project with Qodana Cloud</td>
   </tr>
    <tr>
      <td><ui-path>Log in to Qodana / Logged in to Qodana</ui-path></td>
      <td>Log in Qodana Cloud, or log out. This action is a prerequisite for linking your project with Qodana Cloud-based reports
    </td>
   </tr>
   <tr>
      <td><ui-path>Link project with Cloud / Linked with Cloud</ui-path></td>
      <td>Link your project with a specific Qodana Cloud-based project, or unlink it. This requires that you first log in to Qodana Cloud </td>
   </tr>
   <tr>
      <td><ui-path>View Options</ui-path></td>
      <td>Filter out code issues by their severity and configure their sorting. When no grouping or sorting options are 
selected, the issues are listed in the order they appear in the file. You can also filter all issues by the <a href="baseline.topic">baseline</a></td>
   </tr>
   <tr>
      <td><ui-path>Open Editor Preview</ui-path></td>
      <td>Open the preview pane to view the selected issue in its source context. This preview lets you change the 
    code and apply available quick-fixes</td>
   </tr>
   <tr>
      <td><ui-path>Expand All</ui-path></td>
      <td>Expand all nodes to see all issues in the expanded form</td>
   </tr>
   <tr>
      <td><ui-path>Collapse All</ui-path></td>
      <td>Collapse all nodes that were previously expanded</td>
   </tr>
   <tr>
      <td><ui-path>Show Qodana in Browser</ui-path></td>
      <td>Open the report using your default browser</td>
   </tr>
   <tr>
      <td><ui-path>Other</ui-path></td>
      <td>Functionalities from the <ui-path>Tools | Qodana</ui-path> menu</td>
   </tr>
</table>

## Extend %product% configuration

### Adjust the scope of analysis

Out of the box, Qodana provides two predefined profiles hosted on
[GitHub](https://github.com/JetBrains/qodana-profiles/tree/master/.idea/inspectionProfiles):

* The `qodana.starter` profile is the default profile that triggers the [3-phase analysis](inspection-profiles.md#three-phase-analysis). This is a subset of the `qodana.recommended` profile,
* The `qodana.recommended` profile is suitable for CI/CD pipelines and mostly implements the default %ide% profile, see the
  [PyCharm](https://www.jetbrains.com/help/pycharm/customizing-profiles.html) documentation for details.

You can configure %product% profiles in [YAML](custom-profiles.md) and [XML](custom-xml-profiles.md) formats. For example, 
you can override the `qodana.recommended` profile by enabling JavaScript and TypeScript inspections. To do this, save 
this configuration to a YAML-formatted file in your project directory:

```yaml
name: "Enabling JavaScript and TypeScript" 
baseProfile: qodana.recommended

inspections:
   - group: "category:JavaScript and TypeScript" # Specify the inspection category
     enabled: true # Enable the JavaScript and TypeScript category
```

To enable your profile configuration, save this configuration in the [`qodana.yaml`](qodana-yaml.md) file: 

```yaml
profile:
   path: <relative-path-to-yaml-config-file>
```

To learn more about configuration basics, visit the [](override-a-profile.md) section. Complete guides are 
available in the [](custom-profiles.md) and [](custom-xml-profiles.md) sections.

### Enable the baseline

[Baseline](baseline.topic) is a snapshot of the codebase problems taken at a specific %instance% run and contained in 
the `qodana.sarif.json` file. Using the baseline feature, you can compare your current code with its baseline state and 
see new, unchanged, and resolved problems.

Here are several examples showing how you can run %product% with the baseline enabled:

<tabs group="cli-settings">
    <tab title="Qodana CLI" group-key="qodana-cli">
        <code-block lang="shell" prompt="$">
            qodana scan \
               -v &lt;path_to_baseline&gt;:/data/base/ \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               -l %qd-image% \ 
               --baseline /data/base/qodana.sarif.json
        </code-block>
        <p>Here, the <code>-v &lt;path_to_baseline&gt;:/data/base/</code> line mounts the directory
            containing the SARIF-formatted baseline file to the <code>/data/base</code> directory of the %instance%
            Docker image. The <code>QODANA_TOKEN</code> variable refers to the
            <a href="project-token.md">project token</a>.
        </p>
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
                            uses: JetBrains/qodana-action@v2024.1
                            with:
                              args: --baseline,qodana.sarif.json
                            env:
                              QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
                </code-block>
<p>This snippet contains <code>args: --baseline,qodana.sarif.json</code> that specifies the path to the SARIF-formatted file containing
a baseline. </p>
    </tab>
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$">
            docker run \
               -v $(pwd):/data/project/ \
               -v &lt;path_to_baseline&gt;:/data/base/ \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               %qd-image% \
               --baseline /data/base/qodana.sarif.json
        </code-block>
        <p>In this snippet, the <code>-v &lt;path_to_baseline&gt;:/data/base/</code> line mounts the directory
            containing the SARIF-formatted baseline file to the <code>/data/base</code> directory of the %instance%
            Docker image. The <code>--baseline</code> option specifies the path to the baseline file from the
            Docker filesystem. The <code>QODANA_TOKEN</code> variable refers to the
            <a href="project-token.md">project token</a>.
        </p>
    </tab>
    <tab title="JetBrains IDEs" group-key="jetbrains-ide">
        <procedure>
            <step>In your IDE, navigate to the <ui-path>Problems</ui-path> tool window. </step>
            <step>In the <ui-path>Problems</ui-path> tool window, click the <ui-path>Server-Side Analysis</ui-path> tab.</step>
            <step>On the <ui-path>Server-Side Analysis</ui-path> tab, click the <ui-path>Try Locally</ui-path> button.</step>
            <step>In the dialog that opens, expand the <ui-path>Advanced configuration</ui-path> section and specify the path to the baseline file, and then click <ui-path>Run</ui-path>.</step>
        </procedure>
        <p>This animation shows how the baseline feature works.</p>
        <img src="baseline-jetbrains-ides-intro.gif" width="793" alt="Running the baseline in the IDE"/>
    </tab>
    <tab title="Jenkins">
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
<p>The <code>stages</code> block contains the <code>--baseline &lt;path/to/qodana.sarif.json&gt;</code> line that specifies
the path to the SARIF-formatted file containg information about a baseline.</p>
    </tab>
</tabs>

### Enable the quality gate

[Quality gates](quality-gate.topic) let you control your code quality and build software that meets your quality 
expectations. If a quality gate condition fails, Qodana terminates. Using the [`qodana.yaml`](qodana-yaml.md) file, you 
can configure quality gates for the total number of project problems, specific problem severities, and code coverage. 

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

This table contains the list of technologies supported by the %qp% and %qp-co% linters.

<table style="none">
    <tr>
        <td>Programming languages</td>
        <td>
            <p>Python</p>
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
        <td>Frameworks and libraries</td>
        <td>
            <p>Django</p>
            <p>Google App Engine</p>
            <p>Jupyter</p>
            <p>Pyramid</p>
        </td>
    </tr>
</table>

This table shows %product% features supported by both linters.

| Feature                       | %qp-co%  | %qp%      |
|-------------------------------|----------|-----------|
| [](baseline.topic)            | &#x2714; | &#x2714;  |
| [](quality-gate.topic)        | &#x2714; | &#x2714;  |
| [](code-coverage.md)          | &#x274c; | &#x2714;  |
| [](license-audit.topic)       | &#x274c; | &#x2714;  |
| [](quick-fix.md)              | &#x274c; | &#x2714;  |
| [](vulnerability-checker.md)  | &#x274c; | &#x2714;  |




