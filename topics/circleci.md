[//]: # (title: CircleCI)

<link-summary>You can build Qodana into your CircleCI pipelines using the CircleCI Qodana orb.</link-summary>
<var name="stanza" value="https://circleci.com/docs/orb-concepts#using-orbs-within-your-orb-and-register-time-resolution"/>
<var name="uncertified-orbs" value="https://circleci.com/docs/orbs-faq#using-uncertified-orbs"/>

CircleCI is a cloud-based CI/CD system. You can build %instance% into your CircleCI 
[pipelines](https://circleci.com/docs/concepts#pipelines) using the CircleCI Qodana 
[orb](https://circleci.com/docs/orb-concepts) as described in this section.

## Before you start

<include from="lib_qd.topic" element-id="cicd-cloud-intro"/>

## Basic configuration

<procedure>
    <step>
        <p>Create the <code>.circleci/config.yml</code> file and specify the CircleCI version:</p>
        <code-block lang="yaml">version: 2.1</code-block>
    </step>
    <step>
        <p>Below the CircleCI version, add the <code>orbs</code> 
        <a href="%stanza%">stanza</a>, and then specify the <code>qodana</code> element along with the %instance% version:</p>
        <code-block lang="yaml">
            orbs: 
                qodana: jetbrains/qodana@2024.3
        </code-block>
        <p>If necessary, repeat this step for all required workflows and jobs.</p>
    </step>
    <step>
        <p>In the CircleCI UI, opt in to use <a href="%uncertified-orbs%">uncertified orbs</a>.</p>
    </step>
</procedure>

> To learn more, visit the [CircleCI Qodana orb](https://circleci.com/developer/orbs/orb/jetbrains/qodana) page on
> the CircleCI developer portal.

## Examples

Using this configuration sample, you can scan your project with %instance% with the default configuration parameters:

```yaml
version: '2.1'
orbs:
  qodana: jetbrains/qodana@2024.3
jobs:
  code-quality:
    machine:
      image: 'ubuntu-2004:current'
    steps:
      - checkout
      - qodana/scan
workflows:
  main:
    jobs:
      - code-quality:
          context: qodana
```

This configuration sample invokes the `args` parameter to run the specific linter like `jetbrains/qodana-jvm`:

```yaml
version: 2.1
orbs:
  qodana: jetbrains/qodana@2024.3
jobs:
  code-quality:
    machine:
      image: 'ubuntu-2004:current'
    steps:
      - checkout
      - qodana/scan:
          args: -l jetbrains/qodana-jvm # use space to separate arguments
workflows:
  main:
    jobs:
      - code-quality:
          context: qodana
```

## Commands and parameters

The CircleCI Qodana orb provides the `scan` command to let you inspect your project and report the results.

This table contains the list of optional string parameters that can be additionally used with the `scan` command.

[//]: # (TODO What are other options for additional-cache-hash?)
[//]: # (TODO What other options are available for artifact-name?)

| Parameter              | Description                                                                                                      | Default value                                                           |
|------------------------|------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| `primary-cache-key`    | Customize the generated cache hash                                                                               | `qodana-2024.3-<< pipeline.git.branch >>-<< pipeline.git.revision >>`   |
| `additional-cache-key` | Customize the generated cache hash                                                                               | `qodana-2024.3-<< pipeline.git.branch >>`                               |
| `args`                 | Additional arguments of the [Qodana CLI](https://github.com/jetbrains/qodana-cli#scan) `scan` command            | No default value                                                        |
| `artifact-name`        | Name of the artifact resulting from scanning project with %instance%, used for uploading of scan results         | `qodana-report`                                                         |
| `cache-dir`            | Directory for %instance% caches                                                                                  | `/tmp/cache/qodana`                                                     |
| `results-dir`          | Directory for storing the results of scanning                                                                    | `/tmp/qodana/results`                                                   |