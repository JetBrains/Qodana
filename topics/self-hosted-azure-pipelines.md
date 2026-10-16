# Azure Pipelines

<var name="visual-studio-marketplace" value="https://marketplace.visualstudio.com/items?itemName=JetBrains.qodana"/>
<var name="ci-product" value="Azure Pipelines"/>

## Prerequisites

This guide assumes that you already have Azure DevOps Server installed and running offline, with its collection. 
<!--The Marketplace extension only adds the Qodana Scan task to Pipelines. On a machine with internet access, that task downloads the Qodana CLI and a container image when the job runs. In an air-gapped environment that download can't happen, so the CLI and the linters have to be installed on the agent beforehand, from the archive attached to the guide. The task is then told to use what's already there, with "Use preinstalled Qodana CLI" and --within-docker=false.
-->

Also, your server should also have Podman installed to be able to run %product% Docker images.

<include from="lib_qd.topic" element-id="before-start-qodana-cloud" use-filter="empty"/>

On Azure Pipelines, install the Qodana Scan version 2026.2.2 or later from the [Visual Studio Marketplace](%visual-studio-marketplace%).

### Configure a build agent

Because of no access to the internet, the machine where the build agent runs the Qodana Scan task must be on the same network as the Qodana Self-Hosted instance. 
Before running, the agent has to reach %premlite%. While starting, it connects to that address to authenticate with the project token and upload the report.


<!-- Where should it be configured?-->

For a build agent, add a user capability such as `qodana = true` 
under **Project settings | Agent pools | (agent) | Capabilities**, and add the line `- qodana -equals true` to the 
demands section of the pipeline.

### Install %product% 

Depending on the operating system of the agent, install %product% as shown below.

<tabs>
    <tab title="Linux">
        <p>Copy the <code>azure-pipelines/qodana-2026.2-linux-x86_64.tar.gz</code> file and extract it, for example:</p>
        <code-block lang="shell">
            sudo tar -xzf qodana-2026.2-linux-x86_64.tar.gz -C /opt 
            sudo chmod -R a+rX /opt/qodana
        </code-block>
        <p>Verify that %product% is running:</p>
        <code-block lang="shell">
            /opt/qodana/cli/qodana --version 
            ls /opt/qodana/dist
        </code-block>  
    </tab>
    <tab title="Windows">
        <p>Copy <code>azure-pipelines/qodana-2026.2-windows-x86_64.zip</code> file and extract it, for example:</p>
            <code-block lang="PowerShell">
                Expand-Archive qodana-2026.2-windows-x86_64.zip -DestinationPath C:\
            </code-block>
        <p>Verify that %product% is running:</p>
        <code-block lang="PowerShell">
            C:\qodana\cli\qodana.exe --version 
            Get-ChildItem C:\qodana\dist
        </code-block>
    </tab>
</tabs>

### Install the build tools

Because %product% reuses the environment of the host machine, the agent needs the same build tools that the project uses for building. 

#### %dotnet%

If your agent runs on Microsoft Windows, nothing is required.

For agents running on Linux, install the required version of the SDK using the binary archive. Use `/usr/share/dotnet` i.e. the default 
location on Linux, where %product% expects to find the SDK.

Verify the installation:

```PowerShell
dotnet --list-sdks
```

## Run %product% using %ci-product%

### Create a pipeline

This is a pipeline configuration example: 

```YAML
# Qodana for .NET, running natively on an offline Azure DevOps agent.
#
# Setup instructions: see Qodana-setup.pdf.
# Replace every REPLACE_WITH value below.

# Manual runs: Pipelines > Run pipeline.
# Pull request runs: configured with a branch policy, see the guide.
trigger: none

jobs:
  - job: qodana_dotnet
    displayName: 'Qodana .NET'
    timeoutInMinutes: 60

    pool:
      name: 'REPLACE_WITH_AGENT_POOL'
      demands:
        # On a Windows agent, replace Linux with Windows_NT.
        - Agent.OS -equals Linux
        - Agent.OSArchitecture -equals X64

    variables:
      QODANA_ENDPOINT: 'REPLACE_WITH_QODANA_URL'
      # On a Windows agent, use the Windows paths instead:
      #   QODANA_ROOT: 'C:\qodana'
      #   QODANA_CLI_BINARY: '$(QODANA_ROOT)\cli\qodana.exe'
      #   QODANA_DIST: '$(QODANA_ROOT)\dist\dotnet'
      QODANA_ROOT: '/opt/qodana'
      QODANA_CLI_BINARY: '$(QODANA_ROOT)/cli/qodana'
      QODANA_DIST: '$(QODANA_ROOT)/dist/dotnet'
      # Leave empty for a repository containing a single project.
      # In a monorepo, name the folder and the configuration file:
      #   '--only-directory api --config qodana-dotnet.yaml'
      EXTRA_ARGS: ''
      # The solution to restore before the analysis.
      SOLUTION: 'REPLACE_WITH_SOLUTION.sln'

    steps:
      - checkout: self
        fetchDepth: 0

      # In a pull request build, Azure checks out the merge commit. Qodana must
      # analyse the pull request's own commit, otherwise it reports problems
      # from the target branch as well. Ignored in manual runs.
      - script: git checkout $(System.PullRequest.SourceCommitId)
        condition: eq(variables['Build.Reason'], 'PullRequest')
        displayName: 'Check out the pull request source commit'

      # Checks the installation and puts the Qodana CLI on PATH.
      # On a Windows agent, replace this step with the PowerShell one below.
      - bash: |
          set -eu
          test -x "$QODANA_CLI_BINARY"
          test -d "$QODANA_DIST"
          echo "##vso[task.prependpath]$(dirname "$QODANA_CLI_BINARY")"
        displayName: 'Verify the Qodana installation'

      # - powershell: |
      #     if (-not (Test-Path $env:QODANA_CLI_BINARY)) {
      #       throw "Qodana CLI not found at $env:QODANA_CLI_BINARY"
      #     }
      #     if (-not (Test-Path $env:QODANA_DIST)) {
      #       throw "Qodana linter not found at $env:QODANA_DIST"
      #     }
      #     $cliDir = Split-Path $env:QODANA_CLI_BINARY
      #     Write-Host "##vso[task.prependpath]$cliDir"
      #   displayName: 'Verify the Qodana installation'

      # A solution whose projects use packages.config rather than
      # PackageReference is not restored by dotnet. Replace this step with
      # msbuild -t:restore -p:RestorePackagesConfig=true "$(SOLUTION)", which
      # needs MSBuild 16.5 or newer. If msbuild is on the path of the agent,
      # use it here; otherwise use the MSBuild task instead of this step, with
      # those arguments.
      - script: dotnet restore "$(SOLUTION)"
        displayName: 'Restore NuGet dependencies'

      - task: QodanaScan@2026
        displayName: 'Qodana scan'
        env:
          QODANA_TOKEN: $(QODANA_TOKEN)
          QODANA_ENDPOINT: $(QODANA_ENDPOINT)
          QODANA_DIST: $(QODANA_DIST)
          # Authenticated NuGet feed. Uncomment the lines for your case,
          # together with the matching bootstrap block in qodana.yaml, and add
          # the feed address as a pipeline variable.
          # QODANA_NUGET_URL: $(QODANA_NUGET_URL)
          #
          # (A) Azure Artifacts feed in the same collection:
          # SYSTEM_ACCESSTOKEN: $(System.AccessToken)
          #
          # (B) Any other feed. Add both as secret pipeline variables:
          # QODANA_NUGET_USER: $(QODANA_NUGET_USER)
          # QODANA_NUGET_PASSWORD: $(QODANA_NUGET_PASSWORD)
        inputs:
          # Use the CLI already on the agent instead of downloading one.
          useInstalledCli: true
          # Analyse only the changes when triggered by a pull request.
          # Manual runs always scan the whole project.
          prMode: true
          # Run natively. Without this the task downloads a container image.
          args: '--within-docker=false $(EXTRA_ARGS)'
```
{collapsible="true"}


You can configure pipelines using YAML files or the classic editor. 

Each analysis reports to its own Qodana project, so each pipeline needs its own token. The variable name stays the same in every pipeline, because variables are scoped to the pipeline they are defined in.

<tabs>
<tab title="YAML file">
<procedure>
<step>In the root directory of your project, create the <code>azure-pipelines.yml</code> file.</step>
<step>In the Azure DevOps project, navigate to <ui-path>Pipelines | New pipeline | Azure Repos Git</ui-path>, select the repository, and then select <ui-path>Existing Azure Pipelines YAML file</ui-path>, 
and then select the <code>/azure-pipelines.yml</code> file.</step>
<step>In the Azure DevOps project, navigate to <ui-path>Edit | Variables | New variable</ui-path> and create a variable named <code>QODANA_TOKEN</code>. 
This will hold the project token from %premlite% and Keep this value secret selected.</step>
<step><p>Replace the values from the <code>azure-pipelines.yml</code> file as per this table:</p>
<table>
<tr>
<td><code>REPLACE_WITH_QODANA_URL</code></td>
<td>The address of your Qodana Self-Hosted instance.</td>
</tr>
<tr>
<td><code>REPLACE_WITH_AGENT_POOL</code></td>
<td>The agent pool name taken from <ui-path>Project settings | Agent pools</ui-path>.</td>
</tr>
<tr>
<td><code>REPLACE_WITH_SOLUTION.sln</code></td>
<td>Path to the solution file.</td>
</tr>
</table>
</step>
</procedure>
<p>Qodana contacts the address when it starts, so it must be reachable from the build agent. This can be something like <code>https://qodana.internal.example</code>.</p>
</tab>
<tab title="Classic editor">
<procedure>
<step>Navigate to <ui-path>Pipelines | New pipeline | Use the classic editor</ui-path>, select the repository, and start from an empty job.</step> 
<step>On the agent job, select the agent pool, and, if the qodana capability was added to the agent, add qodana equals true under Demands. 
Under Get sources, leave shallow fetch off.</step>
<step>
    <p>On the <ui-path>Variables</ui-path>tab, define the following variables:</p>
    <table>
        <tr>
            <td><ui-path>QODANA_TOKEN</ui-path></td>
            <td>the project token, with Keep this value secret</td>
        </tr>
        <tr>
            <td><ui-path>QODANA_ENDPOINT</ui-path></td>
            <td>the address of the Qodana Self-Hosted instance</td>
        </tr>
        <tr>
            <td><ui-path>QODANA_ROOT</ui-path></td>
            <td>the directory Qodana was extracted into in section 4.2.1, /opt/qodana on Linux or C:\qodana on Windows</td>
        </tr>
        <tr>
            <td><ui-path>QODANA_DIST</ui-path></td>
            <td>the linter installed on the agent, for example $(QODANA_ROOT)/dist/dotnet on Linux or $(QODANA_ROOT)\dist\dotnet on Windows</td>
        </tr>
    </table>
</step>
<step><p>On the Classic editor UI, add the following tasks:</p>


</step>
</procedure>
</tab>
</tabs>


Those steps are only for the classic editor. Azure DevOps lets you define a pipeline in two ways. One is a YAML file, and we already provide one as an example in the shared drive files (azure-pipelines.yml), with all the steps already in it. The other is the classic editor in the UI, where there's no file: you add the tasks by hand to the agent job, in that order. So for the UI they're not config to write, they're the tasks to add in the editor.
You're right, it's never introduced. Qodana Scan is the pipeline task the Qodana extension adds to Azure DevOps (QodanaScan@2026 in YAML), and it's what actually starts the analysis. It would be worth adding it to the Definitions table and naming it in the resources row "Qodana task for Azure Pipelines".
On the Qodana Scan task, in the classic editor: tick "Use preinstalled Qodana CLI", leave "PR Mode" ticked, and set "Qodana CLI arguments" to --within-docker=false. In the YAML file it's already set with prMode: true, so there's nothing to tick. PR Mode only controls what the scan analyses: a build started by a pull request analyses only the changes, a manual run analyses the whole project. It doesn't create the pull request trigger. For Azure Repos that's a branch policy, under Repos > Branches > Branch policies > Build validation, pointing at this pipeline. That's why the YAML file has trigger: none.


Let me know if anything's still unclear.