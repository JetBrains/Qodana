[//]: # (title: Bitbucket Cloud)

<var name="repository" value="https://support.atlassian.com/bitbucket-cloud/docs/create-a-repository-in-bitbucket-cloud/"/>
<var name="pipeline" value="https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-pipelines/"/>

[Bitbucket Cloud](https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-cloud/) is a tool that
gives teams one place to plan, collaborate, test, and deploy their code. This
section explains how you can run %product% [Docker images](docker-images.md) within Bitbucket Cloud 
[pipelines](%pipeline%) and covers 
application of the [quality gate](quality-gate.topic) and [baseline](baseline.topic) features.

## Prepare your project

1. Using the Bitbucket Cloud UI, create a [repository](%repository%).
2. In the Bitbucket Cloud repository, create a [pipeline](%pipeline%). This will generate the `bitbucket-pipelines.yml` file 
for storing a pipeline configuration.

## Basic configuration

<include from="lib_qd.topic" element-id="bitbucket-basic-configuration"/>

This configuration will be used as a basis for all examples in this section.

## Quality gate

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
          image: jetbrains/qodana-&lt;linter&gt;
          script:
            - export QODANA_TOKEN=$QODANA_TOKEN  # Export the environment variable
            - qodana --fail-threshold <number-of-problems> --results-dir=$BITBUCKET_CLONE_DIR/.qodana --report-dir=$BITBUCKET_CLONE_DIR/.qodana/report --cache-dir=$BITBUCKET_CLONE_DIR/.qodana/cache
          artifacts:
            - .qodana/report

definitions:
  caches:
    qodana: .qodana/cache
```

## Baseline

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
          image: jetbrains/qodana-&lt;linter&gt;
          script:
            - export QODANA_TOKEN=$QODANA_TOKEN  # Export the environment variable
            - qodana --baseline <path/to/qodana.sarif.json> --results-dir=$BITBUCKET_CLONE_DIR/.qodana --report-dir=$BITBUCKET_CLONE_DIR/.qodana/report --cache-dir=$BITBUCKET_CLONE_DIR/.qodana/cache
          artifacts:
            - .qodana/report

definitions:
  caches:
    qodana: .qodana/cache
```