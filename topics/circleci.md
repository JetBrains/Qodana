[//]: # (title: CircleCI)

CircleCI is a cloud-based CI/CD system. You can build %product% into your CircleCI 
[pipelines](https://circleci.com/docs/concepts#pipelines) using the CircleCI Qodana 
[orb](https://circleci.com/docs/orb-concepts) as described in this procedure:

1. Create the `.circleci/config.yml` file and specify the CircleCI version:

```yaml
version: 2.1
```

2. Below the CircleCI version, add the <code>orbs</code> 
<a href="https://circleci.com/docs/orb-concepts#using-orbs-within-your-orb-and-register-time-resolution">stanza</a>, and 
then specify the <code>qodana</code> element along with the %product% version:

```yaml
orbs: 
    qodana: jetbrains/qodana@2023.3
```

If necessary, repeat this step for all required workflows and jobs.

3. In the CircleCI UI, opt in to use [uncertified orbs](https://circleci.com/docs/orbs-faq#using-uncertified-orbs). 

> To learn more, visit the [CircleCI Qodana orb](https://circleci.com/developer/orbs/orb/jetbrains/qodana) page on
> the CircleCI developer portal.

## Examples

Using this configuration sample, you can scan your project with %product% with the default configuration parameters:

```yaml
version: '2.1'
orbs:
  qodana: jetbrains/qodana@2023.3
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
  qodana: jetbrains/qodana@2023.3
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

### Qodana Cloud

<chunk id="circleci-qodana-cloud">

To forward inspection results to Qodana Cloud, all you need to do is to create the `QODANA_TOKEN` [project variable](https://circleci.com/docs/set-environment-variable/#set-an-environment-variable-in-a-project) and
   save the [project token](cloud-projects.topic#cloud-manage-projects) as its value.

After the token is set for analysis, all Qodana job results will be uploaded to your Qodana Cloud project.

</chunk>

![Qodana Cloud](https://user-images.githubusercontent.com/13538286/214899046-572649db-fe62-49b2-a368-b5d07737c1c1.gif)

## Commands and parameters

The CircleCI Qodana orb provides the `scan` command to let you inspect your project and report the results.

This table contains the list of optional string parameters that can be additionally used with the `scan` command.

[//]: # (TODO What are other options for additional-cache-hash?)
[//]: # (TODO What other options are available for artifact-name?)

| Parameter              | Description                                                                                             | Default value                                                         |
|------------------------|---------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| `primary-cache-key`    | Customize the generated cache hash                                                                      | `qodana-2023.3-<< pipeline.git.branch >>-<< pipeline.git.revision >>` |
| `additional-cache-key` | Customize the generated cache hash                                                                      | `qodana-2023.3-<< pipeline.git.branch >>`                             |
| `args`                 | Additional arguments of the [Qodana CLI](https://github.com/jetbrains/qodana-cli#scan) `scan` command   | No default value                                                      |
| `artifact-name`        | Name of the artifact resulting from scanning project with %product%, used for uploading of scan results | `qodana-report`                                                       |
| `cache-dir`            | Directory for %product% caches                                                                          | `/tmp/cache/qodana`                                                   |
| `results-dir`          | Directory for storing the results of scanning                                                           | `/tmp/qodana/results`                                                 |