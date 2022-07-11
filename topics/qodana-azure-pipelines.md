[//]: # (title: Azure Pipelines)

# Qodana Scan

Qodana Scan is an Azure Pipelines task packed inside [Qodana Azure Pipelines extension](https://marketplace.visualstudio.com/items?itemName=JetBrains.qodana) to scan your code with Qodana.

## Usage

### Basic configuration

After you've installed [Qodana Azure Pipelines extension](https://marketplace.visualstudio.com/items?itemName=JetBrains.qodana) to your organization, to configure the Qodana Scan task, edit your `azure-pipelines.yml` file:

```yaml
# Start with a minimal pipeline that you can customize to build and deploy your code.
# Add steps that build, run tests, deploy, and more:
# https://aka.ms/yaml

trigger:
  - main

pool:
  vmImage: ubuntu-latest

steps:
  - task: Cache@2  # Not required, but Qodana will open projects with cache faster.
    inputs:
      key: '"$(Build.Repository.Name)" | "$(Build.SourceBranchName)" | "$(Build.SourceVersion)"'
      path: '$(Agent.TempDirectory)/qodana/cache'
      restoreKeys: |
        "$(Build.Repository.Name)" | "$(Build.SourceBranchName)"
        "$(Build.Repository.Name)"
  - task: QodanaScan@2022
```

Triggering this job depends on [what type of repository you are using in Azure Pipelines](https://docs.microsoft.com/en-us/azure/devops/pipelines/build/triggers?view=azure-devops#classic-build-pipelines-and-yaml-pipelines).

The task can be run on any OS and x86_64/arm64 CPUs, but it requires the agent to have Docker installed. And since most of Qodana Docker images are Linux-based, the docker daemon must run Linux containers.

### SARIF SAST Scans Tab

To display Qodana report summary in Azure DevOps UI in 'Scans' tab, install Microsoft DevLabs’ [SARIF SAST Scans Tab](https://marketplace.visualstudio.com/items?itemName=sariftools.scans) extension.

![Azure Scans Tab](https://user-images.githubusercontent.com/13538286/160094802-df9b86b6-be53-45c1-a70c-8edfcde9412a.png)

## Configuration

You probably won't need other options than `args`: all other options can be helpful if you are configuring multiple Qodana Scan jobs in one workflow.

| Name           | Description                                                                                                                                                                 | Default Value                           |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| `args`         | Additional [Qodana CLI `scan` command](https://github.com/jetbrains/qodana-cli#scan) arguments, split the arguments with commas (`,`), for example `-i,frontend`. Optional. | -                                       |
| `resultsDir`   | Directory to store the analysis results. Optional.                                                                                                                          | `$(Agent.TempDirectory)/qodana/results` |
| `uploadResult` | Upload Qodana results as an artifact to the job. Optional.                                                                                                                  | `true`                                  |
| `artifactName` | Specify Qodana results artifact name, used for results uploading. Optional.                                                                                                 | `qodana-report`                         |
| `cacheDir`     | Directory to store Qodana caches. Optional.                                                                                                                                 | `$(Agent.TempDirectory)/qodana/cache`   |

[gh:qodana]: https://github.com/JetBrains/qodana-action/actions/workflows/code_scanning.yml
[youtrack]: https://youtrack.jetbrains.com/issues/QD
[youtrack-new-issue]: https://youtrack.jetbrains.com/newIssue?project=QD&c=Product%20Azure%20extension
[jb:confluence-on-gh]: https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub
[jb:discussions]: https://jb.gg/qodana-discussions
[jb:twitter]: https://twitter.com/Qodana
[jb:docker]: https://hub.docker.com/r/jetbrains/qodana
