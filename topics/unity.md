[//]: # (title: .NET Unity)

<var name="qp-linter" value="jetbrains/qodana-dotnet:2025.3"/>

<show-structure for="chapter" depth="3"/>

You can analyze Unity project using the [%dotnet%](dotnet.md) linter in the 
[native mode](deploy-qodana.md#deploy-qodana-native-mode) as explained in this section. 

## Before your start

Before running %product%, you need to take several steps to prepare your project.

### Qodana Cloud

To run %product%, you need to obtain a [project token](project-token.md) that  will be used by %product% for identifying and verifying a license.

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

### Solution and packages

Make sure that you have already built your Unity project, see the [](dotnet.md#dotnet-build-project)
chapter of the .NET section for details. 

Unity projects typically don’t include a C# solution and project files, and these should be generated. 
Install the corresponding .NET SDK in the build environment by executing the following 
script on each build:

```Bash
#!/usr/bin/env bash

${UNITY_EXECUTABLE:-xvfb-run --auto-servernum --server-args='-screen 0 640x480x24' unity-editor} \
 -batchmode -quit -projectPath $UNITY_DIR -executeMethod Packages.Rider.Editor.RiderScriptEditor.SyncSolution
```

### Qodana configuration

In the [`qodana.yaml`](qodana-yaml.md) file, save the following configuration to employ the [%dotnet%](dotnet.md) linter in the 
native mode and use the [`qodana.recommended`](inspection-profiles.md) inspection profile:

```yaml
linter: qodana-dotnet # Specifying the linter
withinDocker: false # Enabling native mode

baseProfile: qodana.recommended # Specifying the profile
```

Native mode is the recommended mode for running the [%dotnet%](dotnet.md) linter.

### Prepare your software

Choose the software that you would like to use for running %product%, for example:

<tabs group="software">
    <tab title="GitHub Actions" group-key="github">
        <p>On the <ui-path>Settings</ui-path> tab of the GitHub UI, create the <code>QODANA_TOKEN</code>
            <a href="https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository">encrypted secret</a>
            and save the <a href="project-token.md">project token</a> as its value.
        </p>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab">
        <p>In the root directory of your project, save the <code>.gitlab-ci.yml</code> file. This file will contain a 
            pipeline configuration that will be used by GitLab CI/CD in this use case.
        </p>
    </tab>
    <tab title="Qodana CLI" group-key="command-line">
        <p>Follow the instructions from the <a href="https://github.com/JetBrains/qodana-cli">Qodana CLI</a> page on GitHub.</p>
    </tab>
</tabs>

## Run Qodana 

<tabs group="software">
    <tab title="GitHub Actions" group-key="github">
            <p>To inspect the <code>main</code> branch, release branches and the pull requests coming
            to your repository in the native mode, save this workflow configuration to the <code>.github/workflows/code_quality.yml</code> file:</p>
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
                            env:
                              QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
                </code-block>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab">
        <code-block lang="yaml">
            include:
                - component: $CI_SERVER_FQDN/qodana/qodana/qodana-gitlab-ci@v%version-current%
        </code-block>
    </tab>
    <tab title="Qodana CLI" group-key="command-line">
        <p>Run this command in the project root directory:</p>
        <code-block lang="shell" prompt="$">
            qodana scan 
        </code-block>
        <p>This command tells %product% to generate the output and report in the <code>/report</code> directory inside
a project directory.</p>
    </tab>
    <tab title="JetBrains IDEs" group-key="ides">
        <procedure>
            <step>
               <p>In your IDE, navigate to <ui-path>Tools | Qodana | Try Code Analysis with Qodana</ui-path>.</p> 
            </step>
            <step>
               <p>On the dialog that opens, make necessary configurations to the <code>qodana.yaml</code> file.</p>
               <img src="ide-plugin-dotnet-run-qodana.png" width="793" alt="Configuring Qodana in the Run Qodana dialog" border-effect="line"/>
                <p>Click <ui-path>Run</ui-path> for analyzing your code.</p>
            </step>
            <step>
               <p>In the <ui-path>Server-Side Analysis</ui-path> tool window, see the <a href="qodana-ide-plugin.md" anchor="ide-plugin-study-reports">inspection results</a>.</p>
            </step>
        </procedure>
    </tab>
</tabs>


## Customize your analysis

Using recommendations from the [](ui-overview.md) and [](inspection-profiles.md) sections, you can adjust 
%product% analysis of your project. For example, using the [**Configuration**](ui-overview.md#ui-overview-configuration) tab of a %product% report, you can select
the inspections that will be used during the analysis or exclude them from the analysis. Also, you can exclude directories 
of your project that you do not wish %product% to analyze. To adjust the existing profile, you can use the recommendations 
from the [](inspection-profiles.md#inspection-profiles-custom-profiles) section.
