[//]: # (title: Unity)

<var name="qp-linter" value="jetbrains/qodana-dotnet:2024.2"/>


You can analyze your Unity project using %product% as explained in this section. 

## Prerequisites

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

### Solution and required packages

Unity projects typically don’t include a C# solution and project files, and these need to be generated in order for 
Qodana to process them. We installed the corresponding .NET SDK in the build environment and executed the following 
script on each build:

```Bash
#!/usr/bin/env bash

${UNITY_EXECUTABLE:-xvfb-run --auto-servernum --server-args='-screen 0 640x480x24' unity-editor} \
 -batchmode -quit -projectPath $UNITY_DIR -executeMethod Packages.Rider.Editor.RiderScriptEditor.SyncSolution
```

### Qodana configuration

In the [`qodana.yaml`](qodana-yaml.md) file, save the following configuration to employ the %dotnet% linter in the 
native mode and use the [`qodana.recommended`](inspection-profiles.md) inspection profile:

```yaml
ide: QDNET # Enbaling the native mode

baseProfile: qodana.recommended # Specifying the profile
```

### Prepare your software

<tabs group="software">
    <tab title="GitHub Actions" group-key="github">
        <p>On the <ui-path>Settings</ui-path> tab of the GitHub UI, create the <code>QODANA_TOKEN</code>
            <a href="https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository">encrypted secret</a>
            and save the <a href="project-token.md">project token</a> as its value.
        </p>
    </tab>
    <tab title="Command line" group-key="command-line">
        <p>Install Docker on the machine were you are going to run %product%.</p>  
        <p>If you are using Linux, you should be able to run Docker under your current non-root user.</p>
      <tabs group="cli-settings">
          <tab group-key="qodana-cli" title="Qodana CLI">
              <p>Follow the instructions from the
              <a href="https://github.com/JetBrains/qodana-cli">Qodana CLI</a> page on GitHub.</p>
          </tab>
          <tab group-key="docker-image" title="Docker image">
            <p>Run this command to pull the Docker image of the %dotnet% linter:</p>
               <code-block lang="shell" prompt="$">
                   docker pull %qp-linter%
               </code-block>
          </tab>
      </tabs>
    </tab>
</tabs>

## Run %product% 

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
                            uses: JetBrains/qodana-action@v2024.2
                            env:
                              QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
                </code-block>
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
    </tab>
    <tab title="JetBrains IDEs" group-key="ides">
        <procedure>
            <step>
               <p>In your IDE, navigate to <ui-path>Tools | Qodana | Try Code Analysis with Qodana</ui-path>.</p> 
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


## Customize your analysis

