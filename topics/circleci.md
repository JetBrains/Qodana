[//]: # (title: CircleCI)

<show-structure for="chapter" depth="3"/>

<link-summary>You can build Qodana into your CircleCI pipelines using the qodana orb.</link-summary>
<var name="stanza" value="https://circleci.com/docs/orb-concepts#using-orbs-within-your-orb-and-register-time-resolution"/>
<var name="uncertified-orbs" value="https://circleci.com/docs/orbs-faq#using-uncertified-orbs"/>
<var name="context" value="https://circleci.com/docs/contexts/#create-and-use-a-context"/>

CircleCI is a cloud-based CI/CD system. You can build %instance% into your CircleCI 
[pipelines](https://circleci.com/docs/concepts#pipelines) using the CircleCI Qodana [orb](https://circleci.com/docs/orb-concepts) as described in this section.

> To learn more about the CircleCI Qodana orb, visit the [CircleCI Qodana orb](https://circleci.com/developer/orbs/orb/jetbrains/qodana) page on
> the CircleCI developer portal.

## Before you start

### %cloud%

<include from="lib_qd.topic" element-id="cicd-cloud-intro"/>

### Prepare your project

<procedure>
    <step>In your CircleCI organization settings, navigate to the <ui-path>Contexts</ui-path> section and define the <code>qodana</code> <a href="%context%">context</a>.</step>
    <step>In the <ui-path>Contexts</ui-path> section, click the <code>qodana</code> context. In this context, define 
            the <code>QODANA_TOKEN</code> environment variable and save the <a href="project-token.md">project token</a> as its value.</step>
    <step>In your CircleCI organization settings, navigate to the <ui-path>Security</ui-path> section. In this section, 
            opt in to allow using <a href="%uncertified-orbs%">uncertified public orbs</a>. </step>
    <step>If necessary, in your repository create the <code>.circleci/config.yml</code> file that will contain a CircleCI configuration.</step>
</procedure>


## Basic configuration

<include from="lib_qd.topic" element-id="major-version-note"/>

In the `.circleci/config.yml` file, save the following configuration: 

```yaml
version: 2.1

orbs:
  qodana: jetbrains/qodana@2025.2

jobs:
  code-quality:
    machine:
      image: 'ubuntu-2004:current'
    environment: $QODANA_TOKEN
    steps:
      - checkout
      - qodana/scan

workflows:
  main:
    jobs:
      - code-quality:
          context: qodana
```

This table describes configuration elements: 

| Configuration block | Description                                                                            |
|---------------------|----------------------------------------------------------------------------------------|
| `orbs`              | Invokes the CircleCI Qodana orb and configures its version                             |
| `jobs`              | Refers to the `QODANA_TOKEN` variable defined in the [](#Prepare+your+project) chapter |
| `workflows`         | Invokes the `qodana` context that contains the `QODANA_TOKEN` variable                 |


This configuration will be extended in the sections below.

## Baseline and quality gate

This configuration uses the [`args` parameter](#Commands+and+parameters) to invoke the 
[baseline](baseline.topic) and [quality gate](quality-gate.topic) features:

```yaml
version: 2.1

orbs:
  qodana: jetbrains/qodana@2025.2

jobs:
  code-quality:
    machine:
      image: 'ubuntu-2004:current'
    environment: $QODANA_TOKEN
    steps:
      - checkout
      - qodana/scan:
          args: > # Use space to separate arguments
            --baseline <path-relative-to-project-dir>
            --fail-threshold <number-of-problems> 

workflows:
  main:
    jobs:
      - code-quality:
          context: qodana

```

## Specific linter

This configuration sample uses the [`args` parameter](#Commands+and+parameters) to run the specific linter like `jetbrains/qodana-jvm`:

```yaml
version: 2.1

orbs:
  qodana: jetbrains/qodana@2025.2

jobs:
  code-quality:
    machine:
      image: 'ubuntu-2004:current'
    environment: $QODANA_TOKEN
    steps:
      - checkout
      - qodana/scan:
          args: -l jetbrains/qodana-jvm # Use space to separate arguments

workflows:
  main:
    jobs:
      - code-quality:
          context: qodana
```

## Specific branch

This configuration instructs %product% to analyze changes only on the `main` branch: 


```yaml
version: 2.1

orbs:
  qodana: jetbrains/qodana@2025.2

jobs:
  code-quality:
    machine:
      image: 'ubuntu-2004:current'
    environment: $QODANA_TOKEN
    steps:
      - checkout
      - qodana/scan

workflows:
  main:
    jobs:
      - code-quality:
          context: qodana
          filters:
            branches:
              only:
                - main  # Specify your branch here 
```

## Commands and parameters

The CircleCI Qodana orb provides the `scan` command to let you analyze your project and report the results.

This table contains the list of optional string parameters that can be additionally used with the `scan` command.

[//]: # (TODO What are other options for additional-cache-hash?)
[//]: # (TODO What other options are available for artifact-name?)

| Parameter              | Description                                                                                           | Default value                                                         |
|------------------------|-------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| `primary-cache-key`    | Customize the generated cache hash                                                                    | `qodana-2025.2-<< pipeline.git.branch >>-<< pipeline.git.revision >>` |
| `additional-cache-key` | Customize the generated cache hash                                                                    | `qodana-2025.2-<< pipeline.git.branch >>`                             |
| `args`                 | Additional arguments of the [Qodana CLI](https://github.com/jetbrains/qodana-cli#scan) `scan` command | No default value                                                      |
| `artifact-name`        | Name of the analysis artifact, used for uploading analysis results                                    | `qodana-report`                                                       |
| `cache-dir`            | Directory for %instance% caches                                                                       | `/tmp/cache/qodana`                                                   |
| `results-dir`          | Directory for storing the results of scanning                                                         | `/tmp/qodana/results`                                                 |