[//]: # (title: Bitbucket Cloud)

<var name="repository" value="https://support.atlassian.com/bitbucket-cloud/docs/create-a-repository-in-bitbucket-cloud/"/>
<var name="pipeline" value="https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-pipelines/"/>

<link-summary>Learn how to run %instance% Docker images within Bitbucket Cloud pipelines.</link-summary>

[Bitbucket Cloud](https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-cloud/) is a tool that
gives teams one place to plan, collaborate, test, and deploy their code. This
section explains how you can run %instance% [Docker images](docker-images.md) within Bitbucket Cloud 
[pipelines](%pipeline%) and covers 
application of the [quality gate](quality-gate.topic) and [baseline](baseline.topic) features.

## Prepare your project

<link-summary>Create a repository and a pipeline in the Bitbucket Cloud UI.</link-summary>

1. Using the Bitbucket Cloud UI, create a [repository](%repository%).
2. In the Bitbucket Cloud repository, create a [pipeline](%pipeline%). This will generate the `bitbucket-pipelines.yml` file 
for storing a pipeline configuration.

## Basic configuration

<include from="lib_qd.topic" element-id="bitbucket-basic-configuration"/>

This configuration will be used as a basis for all examples in this section.

## Quality gate

<link-summary>Using the --fail-threshold option, you can configure the limit of problems accepted in your project.</link-summary>

Using the [`--fail-threshold`](docker-image-configuration.topic#docker-config-reference-quality-gate) option, you can 
configure the limit of problems accepted in your project:  

```yaml
image: atlassian/default-image:4

pipelines:
  branches:
    main:
      - step:
          name: Qodana
          caches:
            - qodana
          image: jetbrains/qodana-<linter> # Specify a Qodana linter here. For example, jetbrains/qodana-jvm:latest
          script:
            - export QODANA_TOKEN=$QODANA_TOKEN  # Export the environment variable
            - qodana --fail-threshold <number-of-problems> --results-dir=$BITBUCKET_CLONE_DIR/.qodana --report-dir=$BITBUCKET_CLONE_DIR/.qodana/report --cache-dir=~/.qodana/cache
          artifacts:
            - .qodana/report

definitions:
  caches:
    qodana: .qodana/cache
```

## Baseline

<link-summary>Use the --baseline path/to/qodana.sarif.json option to 
specify the path to the SARIF-formatted file used as a baseline.</link-summary>

Use the [`--baseline <path/to/qodana.sarif.json>`](docker-image-configuration.topic#docker-config-reference-baseline) option to 
specify the path to the SARIF-formatted file used as a [baseline](baseline.topic):

```yaml
image: atlassian/default-image:4

pipelines:
  branches:
    main:
      - step:
          name: Qodana
          caches:
            - qodana
          image: jetbrains/qodana-<linter> # Specify a Qodana linter here. For example, jetbrains/qodana-jvm:latest
          script:
            - export QODANA_TOKEN=$QODANA_TOKEN  # Export the environment variable
            - qodana --baseline <path/to/qodana.sarif.json> --results-dir=$BITBUCKET_CLONE_DIR/.qodana --report-dir=$BITBUCKET_CLONE_DIR/.qodana/report --cache-dir=~/.qodana/cache
          artifacts:
            - .qodana/report

definitions:
  caches:
    qodana: ~/.qodana/cache
```

## Generate Code Insights reports

<link-summary>By default, %product% lets you use the pull request UI of Bitbucket Cloud to view specific lines of code 
that contain problems along with their description and recommendations for improvement.</link-summary>

Starting from version 2024.1 of %product%, using the pull request UI of Bitbucket Cloud you can view specific lines of
code that contain problems along with their description and recommendations for improvement. By default, %product% 
generates [Code Insights](https://support.atlassian.com/bitbucket-cloud/docs/code-insights/) reports, 
forwards them using the Bitbucket Code Insights API, and does not require any configuration.
