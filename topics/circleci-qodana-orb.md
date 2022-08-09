[//]: # (title: CircleCI Qodana orb)

<!--- I need to rephrase this. ---> 
CircleCI is a cloud-based continuous integration system. You can build %product% into a CircleCI 
<a href="https://circleci.com/docs/concepts#pipelines">pipeline</a> using the <a href="https://circleci.com/docs/orb-concepts">orbs concept</a>.

To inspect your codebase with %product%, follow this procedure:

1. Create the `.circleci/config.yml` file, and add the CircleCI version in the first line:

```yaml
version: 2.1
```

2. Right below the CircleCI version, add the <code>orbs</code> 
<a href="https://circleci.com/docs/orb-concepts#using-orbs-within-your-orb-and-register-time-resolution">stanza</a>, and 
then specify the <code>qodana</code> element and the version of %product%:

```yaml
orbs: 
    qodana: jetbrains/qodana@2022.2.1
```

If necessary, repeat this step for all required workflows and jobs.

3. Opt in to use uncertified orbs in the Security page of your organization settings, see the [The orb registry](https://circleci.com/docs/orb-intro#the-orb-registry) section of the CircleCI documentation portal for details. 

<!--- ## Commands and parameters  - this header needs to be here -->

## Commands and parameters

The `qodana` orb provides the `scan` command for scanning your project and reporting the results.

This table contains the list of optional string parameters that can be additionally used with the `scan` command.

> You can check whether these parameters can be configured using `qodana.yaml`. For more information, see the [Configure profile](https://www.jetbrains.com/help/qodana/qodana-yaml.html) section of the Qodana documentation portal.

<!--- What are other options for additional-cache-hash? --->
<!--- What other options are available for artifact-name? --->

|-----|------|------|
|Parameter|Description|Default value|
|`additional-cache-hash`|Customize the generated cache hash|`<< pipeline.git.revision >>`|
|`args`|Additional arguments of the [Qodana CLI](https://github.com/jetbrains/qodana-cli#scan) `scan` command| No default value|
|`artifact-name`|Name of the artifact resulting from scanning project with %product%, used for uploading of scan results|`qodana-report`|
|`cache-dir`|Directory for %product% caches|`/tmp/cache/qodana`|
|`results-dir`|Directory for storing the results of scanning|`/tmp/qodana/results`|

<!--- ## Examples --->

## Examples

Using this configuration sample, you can scan your project with %product% using the default configuration parameters.

```yaml
version: '2.1'
orbs:
  qodana: jetbrains/qodana@2022.2.1
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

<!--- The second example of using parameters is required here --->