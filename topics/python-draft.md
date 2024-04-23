# Python

<no-index/>

<var name="qp" value="Qodana for Python"/>
<var name="qp-co" value="Qodana Community for Python"/>
<var name="qp-linter" value="jetbrains/qodana-python:2024.1"/>
<var name="qp-co-linter" value="jetbrains/qodana-python-community:2024.1"/>
<var name="qd-image" value="jetbrains/qodana-python<-community>:2024.1"/>
<var name="JenkinsCred" value="https://www.jenkins.io/doc/book/using/using-credentials/#adding-new-global-credentials"/>
<var name="ide" value="PyCharm"/>

<link-summary>You can inspect your code using the %qp% and %qp-co% linters.</link-summary>

<!-- Add a note about draft status -->

<warning>This is a draft document, so we do not recommend that you use it.</warning>

You can inspect your code using the %qp% linter is based on PyCharm Professional and licensed under the Ultimate and 
Ultimate Plus licenses, and the %qp-co% linter is based on PyCharm Community and licensed under the Community license. 
To learn more about %product% licenses, navigate to the [](pricing.md) page. To see the list of supported features, you
can navigate to the [feature matrix](#Feature+matrix) in this section.

## Prerequisites

%qp% requires a [project token](project-token.md) generated in Qodana Cloud. If you use the %qp-co% linter, the project token is optional.

If your project has external `pip` dependencies, you can set them up using the [`bootstrap`](before-running-qodana.md) 
field in the `qodana.yaml` file. For example, if your project dependencies are specified by the `requirements.txt` file 
in your project root, add the following line to [`qodana.yaml`](qodana-yaml.md#Run+custom+commands) that will be 
executed before the analysis:

```yaml
bootstrap: pip install -r requirements.txt
```

## Basic use case

<note><include from="lib_qd.topic" element-id="docker-ram-note"/></note>

By default, you can run these linters using [Qodana CLI](https://github.com/JetBrains/qodana-cli). If necessary,
check the [installation page](https://github.com/JetBrains/qodana-cli/releases/latest) to install
Qodana CLI. Alternatively, you can use the Docker commands from the <ui-path>Docker image</ui-path> tab.

<include from="lib_qd.topic" element-id="root-and-non-root-users-info-bubble"></include>

<tabs>
    <tab id="qodana-cli-tab" title="Qodana CLI">
        <code-block prompt="$">
            qodana scan \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               -l %qd-image%
        </code-block>
        <p>Here, the <code>QODANA_TOKEN</code> variable refers to the <a href="project-token.md">project token</a>.</p>
        <p>If you omit the <code>-l</code> option, the %qp% linter will run by default.</p>
    </tab>
    <tab id="docker-image-tab" title="Docker image">
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
        <p>In your browser, open <a href="https://qodana.cloud">Qodana Cloud</a> to examine inspection results.
            Here, you can also reconfigure the analysis, see the <a href="ui-overview.md"/> section for
            details.</p>
    </tab>
</tabs>

Now you can set up analysis in CI/CD pipelines, for example [GitHub Actions](github.md).

<include from="lib_qd.topic" element-id="github-basic-configuration"/>

Here is the [Jenkins Pipeline](jenkins.md) configuration sample: 

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

Here is how you can configure [GitLab CI/CD](gitlab.md) for running %product%: 

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

## Study inspection reports

### Qodana Cloud

Once %product% inspected your project and the inspection report was uploaded to Qodana Cloud, you can study inspections.
To do it, navigate to [Qodana Cloud](https://qodana.cloud), and open your report.

<img src="qc-report-overview.png" dark-src="qc-report-overview_dark.png" alt="Report overview" width="706" border-effect="line"/>

<p>The upper part of the report page contains:</p>

<p>1. Branch selector. Using it, you can overview reports for each branch in your project.</p>
<p>2. Commit hash and time passed since the last inspection run.</p>
<p>3. Timeline describing the date of inspection, number of problems detected.</p>
<p>4. Buttons for navigating to the build page, downloading the report in <a href="qodana-sarif-output.md">SARIF format</a>, and opening the help guide.</p>
<p>5. Selector for overviewing either the absolute number of detected problems, or the number of problems
relatively to a <a href="baseline.topic">baseline</a> set for this project.</p>

<p>To learn more about %instance% report UI, see the <a href="ui-overview.md"/> section.</p>

### %ide%

You can log in to [Qodana Cloud](https://qodana.cloud) and connect your project opened in the IDE to a specific Qodana Cloud [project](cloud-projects.topic) to get the
latest %instance% report and view it.

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
        <p>By enabling the <ui-path>Always load most relevant Qodana report</ui-path> option, you can get actual reports automatically retrieved from Qodana Cloud.</p>
      <img src="ide-plugin-connect-3.png" dark-src="ide-plugin-connect-3_dark.png" width="706" alt="Enabling to load the most relevant reports" border-effect="line"/>
        <p>In this case, the IDE will search and fetch from Qodana Cloud the report that has the revision ID corresponding to the 
        current revision ID (HEAD). If this report was not found, the IDE will select the previous report with the revision
        closest to the current revision ID (HEAD). Otherwise, the IDE retrieves the latest available report from Qodana Cloud.</p>
    </step> 
    <step>
       <p>In the <ui-path>Server-Side Analysis</ui-path> tool window, overview <a href="qodana-ide-plugin.md" anchor="ide-plugin-study-reports">inspection results</a>.</p>
    </step>
</procedure>


Using the **Server-Side Analysis** tool window of your IDE, you can view %instance% reports and navigate to the code fragments
containing such problems.

<img src="ide-plugin-report-navigating.png" dark-src="ide-plugin-report-navigating_dark.png" width="706" alt="Navigating to problems in the IDE" animated="true" border-effect="line"/>

The upper part contains information about the project and branch names, the inspection date, and the number of problems.
The left part of the **Server-Side Analysis** tool window contains several buttons.

<img src="ide-plugin-report-navigating-buttons.png" dark-src="ide-plugin-report-navigating-buttons_dark.png" width="460" alt="Functionalities of the Server-Side Analysis tool window" border-effect="line"/>

This table describes each button from top to bottom:

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
      <td>Open the preview pane to view the selected issue in its source context. This preview lets you can change the 
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
      <td>Open the inspection report using your default browser</td>
   </tr>
   <tr>
      <td><ui-path>Other</ui-path></td>
      <td>Functionalities from the <ui-path>Tools | Qodana</ui-path> menu</td>
   </tr>
</table>

## Advanced configuration

### Adjust the scope of analyses

Out of the box, Qodana provides a couple of predefined profiles hosted on
[GitHub](https://github.com/JetBrains/qodana-profiles/tree/master/.idea/inspectionProfiles):

* `qodana.starter` is the default profile and a subset of `qodana.recommended` triggering the [3-phase analysis](#three-phase-analysis)
* `qodana.recommended` is suitable for CI/CD pipelines and mostly implements the default IDE profiles, see the
  [IntelliJ IDEA](https://www.jetbrains.com/help/idea/customizing-profiles.html) documentation for details

<!-- A couple of examples need to be added here -->

You can override settings from these default profiles. For example, 


To learn more about configuration basics, you can learn the [](override-a-profile.md) section. The complete reference manual
is available in the [](custom-profiles.md) and [](custom-xml-profiles.md) sections.


### Baseline

<p><a href="baseline.topic"><emphasis>Baseline</emphasis></a> is a snapshot of the codebase problems taken at a specific %instance% run and
    contained in the <code>qodana.sarif.json</code> file.</p>

<p>Using the baseline feature, you can compare your current code with its baseline state and see new, unchanged, and
    resolved problems.</p>

<!-- This needs to be accomplished -->

### Quality gate


<!-- At the end of the section, I can add info about how to view Qodana Cloud reports -->
<!-- List of features should be provided at the end of the section -->

## Feature matrix






