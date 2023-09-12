[//]: # (title: Bitbucket Cloud)

<var name="repository" value="https://support.atlassian.com/bitbucket-cloud/docs/create-a-repository-in-bitbucket-cloud/"/>
<var name="pipeline" value="https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-pipelines/"/>

[Bitbucket Cloud](https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-cloud/) is a tool that
gives teams one place to plan, collaborate, test, and deploy their code. This
section explains how you can run %product% [Docker images](docker-images.md) within Bitbucket Cloud 
[pipelines](%pipeline%) and covers 
application of the [quick-fix](quick-fix.md), [quality gate](quality-gate.xml), and [baseline](baseline.xml) features.

## Prepare your project

1. Using the Bitbucket Cloud UI, create a [repository](%repository%).
2. In the Bitbucket Cloud repository, create a [pipeline](%pipeline%).This will generate the `bitbucket-pipelines.yml` file 
where you can contain the pipeline configuration.

## Basic configuration

Save this snippet to the `bitbucket-pipelines.yml` file to make %product% run in a Bitbucket Cloud pipeline:

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
            - qodana --results-dir=$BITBUCKET_CLONE_DIR/.qodana --report-dir=$BITBUCKET_CLONE_DIR/.qodana/report --cache-dir=$BITBUCKET_CLONE_DIR/.qodana/cache 
          artifacts:
            - .qodana/report

definitions:
  caches:
    qodana: .qodana/cache
```

Here, the `branches` block specifies which branches to inspect.

The `image` block specifies the %product% [linter](linters.md) that will be used in the pipeline.

The `script` block contains the `- export QODANA_TOKEN=$QODANA_TOKEN` line that specifies the 
[project token](project-token.md) required by Qodana Cloud and saved as the `$QODANA_TOKEN` 
[repository variable](https://support.atlassian.com/bitbucket-cloud/docs/use-multiple-ssh-keys-in-your-pipeline/).

The `- qodana ...` line tells Bitbucket which directories to use while running the pipeline and can also contain 
%product% [options](docker-image-configuration.xml).

This configuration will be used as a basis for all examples in this section. 

## Quick-fixes

This configuration uses the 
[`fixes-strategy <cleanup/apply>`](docker-image-configuration.xml#docker-config-reference-quick-fix) option to invoke 
the [quick-fix](quick-fix.md) feature using either the `CLEANUP` or the `APPLY` strategy:

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
            - qodana --fixes-strategy &lt;cleanup/apply&gt; --results-dir=$BITBUCKET_CLONE_DIR/.qodana --report-dir=$BITBUCKET_CLONE_DIR/.qodana/report --cache-dir=$BITBUCKET_CLONE_DIR/.qodana/cache
          artifacts:
            - .qodana/report

definitions:
  caches:
    qodana: .qodana/cache
```

## Quality gate

Using the [`fail-threshold`](docker-image-configuration.xml#docker-config-reference-quality-gate) option, you can 
configure the limit of problems accepted:  

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
            - qodana --fail-threshold &lt;number-of-problems&gt; --results-dir=$BITBUCKET_CLONE_DIR/.qodana --report-dir=$BITBUCKET_CLONE_DIR/.qodana/report --cache-dir=$BITBUCKET_CLONE_DIR/.qodana/cache
          artifacts:
            - .qodana/report

definitions:
  caches:
    qodana: .qodana/cache
```

## Baseline

Use the [`baseline <path-to-sarif-file>`](docker-image-configuration.xml#docker-config-reference-baseline) option to 
specify the path to the SARIF-formatted file used as a [baseline](baseline.xml):

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
            - qodana --baseline &lt;path/to/qodana.sarif.json&gt; --results-dir=$BITBUCKET_CLONE_DIR/.qodana --report-dir=$BITBUCKET_CLONE_DIR/.qodana/report --cache-dir=$BITBUCKET_CLONE_DIR/.qodana/cache
          artifacts:
            - .qodana/report

definitions:
  caches:
    qodana: .qodana/cache
```