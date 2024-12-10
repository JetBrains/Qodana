[//]: # (title: Azure Pipelines)

<var name="classic-ui-ref" value="https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/pipelines-get-started?view=azure-devops#define-pipelines-using-the-classic-interface"/>

<link-summary>You can use the Qodana Azure Pipelines extension to analyze your code using Qodana.</link-summary>

# Qodana Scan

Qodana Scan is an Azure Pipelines task
packed inside the [Qodana Azure Pipelines extension](https://marketplace.visualstudio.com/items?itemName=JetBrains.qodana)
to scan your code with Qodana.

## Usage

### Basic configuration

<link-summary>After you've installed the Qodana Azure Pipelines extension to your organization, edit your azure-pipelines.yml file as shown in this section.</link-summary>

After you've installed the [Qodana Azure Pipelines extension](https://marketplace.visualstudio.com/items?itemName=JetBrains.qodana) to your organization, to configure the Qodana Scan task, edit your `azure-pipelines.yml` file:

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
  - task: QodanaScan@2024
```

Triggering this job depends on the [repository type that you are using in Azure Pipelines](https://docs.microsoft.com/en-us/azure/devops/pipelines/build/triggers?view=azure-devops#classic-build-pipelines-and-yaml-pipelines).

If you use the classic editor to create pipelines, add the `Qodana Scan` task to the pipeline configuration and then 
click it. This will open the task configuration as shown below.

<img src="azure-pipelines-task-config.png" width="706" alt="The Qodana Scan task UI config" border-effect="line"/>

The description of these fields is available in the [](#Configuration) chapter of this section.

The task can be run on any OS and x86_64/arm64 CPUs, but it requires the agent to have Docker installed.
And since most of the Qodana Docker images are Linux-based, the docker daemon must be able to run Linux containers.

Alternatively, you can configure your pipelines using the Classic interface as explained on the 
[Microsoft documentation portal](%classic-ui-ref%).

### Qodana Cloud

To send analysis results to Qodana Cloud, all you need to do is to specify the `QODANA_TOKEN` environment variable in the build configuration.
If you are using a Qodana Cloud instance other than https://qodana.cloud/, use the `QODANA_ENDPOINT` variable instead.

<snippet id="azure-pipelines-qodana-cloud">

1. In the Azure Pipelines UI, create the `QODANA_TOKEN` [secret variable](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/set-secret-variables?view=azure-devops&tabs=yaml%2Cbash#secret-variable-in-the-ui) and
   save the [project token](cloud-projects.topic#cloud-manage-projects) as its value.
2. In the Azure pipeline file,
   add `QODANA_TOKEN` variable to the `env` section of the `QodanaScan` task:

```yaml
  - task: QodanaScan@2024
    env:
      QODANA_TOKEN: $(QODANA_TOKEN)
```

</snippet>

After the token is set for analysis, all Qodana Scan job results will be uploaded to your Qodana Cloud project.

![Qodana Cloud](qodana-cloud.gif)

### SARIF SAST Scans Tab

To display Qodana report summary in Azure DevOps UI in 'Scans' tab, install Microsoft DevLabs’ [SARIF SAST Scans Tab](https://marketplace.visualstudio.com/items?itemName=sariftools.scans) extension.

![Azure Scans Tab](https://user-images.githubusercontent.com/13538286/160094802-df9b86b6-be53-45c1-a70c-8edfcde9412a.png)

## Configuration

You won't probably need other options than `args`: all other options can be helpful if you are configuring multiple `Qodana Scan` jobs in one workflow.

| YAML option    | UI element of the classic editor | Description                                                                                                                                                                 | Default Value                           |
|----------------|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| `args`         | **Qodana CLI arguments**        | Additional [Qodana CLI `scan` command](https://github.com/jetbrains/qodana-cli#scan) arguments, split the arguments with commas (`,`), for example `-i,frontend`. Optional. | None                                    |
| `resultsDir`   | **Results Directory**           | Directory to store the analysis results. Optional.                                                                                                                          | `$(Agent.TempDirectory)/qodana/results` |
| `uploadResult` | **Upload Result**               | Upload Qodana results as an artifact to the job. Optional.                                                                                                                  | `false`                                 |
| `uploadSarif`  | **Upload SARIF**                | Upload qodana.sarif.json as an qodana.sarif artifact to the job. Optional.                                                                                                  | `true`                                  |
| `artifactName` | **Artifact Name**               | Specify Qodana results artifact name, used for results uploading. Optional.                                                                                                 | `qodana-report`                         |
| `cacheDir`     | **Cache Directory**             | Directory to store Qodana caches. Optional.                                                                                                                                 | `$(Agent.TempDirectory)/qodana/cache`   |

[gh:qodana]: https://github.com/JetBrains/qodana-action/actions/workflows/code_scanning.yml
[youtrack]: https://youtrack.jetbrains.com/issues/QD
[youtrack-new-issue]: https://youtrack.jetbrains.com/newIssue?project=QD&c=Product%20Azure%20extension
[jb:confluence-on-gh]: https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub
[jb:discussions]: https://jb.gg/qodana-discussions
[jb:twitter]: https://twitter.com/Qodana
[jb:docker]: https://hub.docker.com/r/jetbrains/qodana