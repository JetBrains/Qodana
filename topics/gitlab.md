[//]: # (title: GitLab CI/CD)

<var name="GitLabLink" value="https://docs.gitlab.com/ee/ci/variables/"/>
<var name="GitLabPredefined" value="https://docs.gitlab.com/ee/ci/variables/predefined_variables.html#predefined-variables-reference"/>
<var name="GitLabExpose" value="https://docs.gitlab.com/ee/ci/yaml/#artifactsexpose_as"/>

<link-summary>You can run %instance% Docker images within GitLab CI/CD pipelines.</link-summary>

[GitLab CI/CD](https://docs.gitlab.com/ee/ci/) is a tool for software development that uses various CI/CD methodologies. This 
section explains how you can run %instance% [Docker images](docker-images.md) within GitLab CI/CD 
[pipelines](https://docs.gitlab.com/ee/ci/pipelines/) and covers the following cases:

* Inspecting specific branches and merge requests
* Forwarding inspection reports to [Qodana Cloud](cloud-about.topic)
* Exposing %instance% reports in the GitLab CI/CD user interface
* Using the [quality gate](quality-gate.topic) and [baseline](baseline.topic) features
* Generating Code Quality reports

## Prepare your project

<link-summary>Make sure that your project repository is accessible by GitLab CI/CD, and in the root directory of your 
project save the pipeline configuration file.</link-summary>

Make sure that your project repository is accessible by GitLab CI/CD.

In the root directory of your project, save the `.gitlab-ci.yml` file. This file will contain the pipeline configuration 
that will be used by GitLab CI/CD. 

## Basic configuration

<link-summary>This section shows the basic pipeline configuration.</link-summary>

This is the basic pipeline configuration.

```yaml
qodana:
   image:
      name: jetbrains/qodana-<linter>
      entrypoint: [""]
   cache:
      - key: qodana-2023.3-$CI_DEFAULT_BRANCH-$CI_COMMIT_REF_SLUG
        fallback_keys:
           - qodana-2023.3-$CI_DEFAULT_BRANCH-
           - qodana-2023.3-
        paths:
           - .qodana/cache
   variables:
      QODANA_TOKEN: $qodana_token
   script:
      - qodana --cache-dir=$CI_PROJECT_DIR/.qodana/cache
```

In this configuration, the [`image:name`](https://docs.gitlab.com/ee/ci/yaml/#image) keyword pulls the %instance% 
[Docker image](docker-images.md) of your choice.

The [`cache`](https://docs.gitlab.com/ee/ci/caching/) keyword configures GitLab caches to store the %instance% cache,
so subsequent runs will be faster. 

The [`script`](https://docs.gitlab.com/ee/ci/yaml/#script) keyword runs the `qodana` command and enumerates the %instance% 
configuration options described in the [](docker-image-configuration.topic) section. 

The `variables` keyword defines the `QODANA_TOKEN` [variable](https://docs.gitlab.com/ee/ci/variables/#define-a-cicd-variable-in-the-ui)
referring to the [project token](project-token.md) generated in Qodana Cloud. This token is required by the paid %instance% 
[linters](pricing.md#pricing-linters-licenses), and is optional for using with the Community linters.

You can see these sections to learn how to generate the project token:

* The [](cloud-onboarding.md) section explains how to get the project token generated while first working with Qodana Cloud
* The [](cloud-projects.topic#cloud-manage-projects) section explains how to create a project in the existing Qodana Cloud organization

## Inspect specific branches

<link-summary>This section explains how you can tell %instance% which branches of your project to inspect.</link-summary>

Using the [`only`](https://docs.gitlab.com/ee/ci/yaml/index.html#only--except) keyword, you can tell %instance% which 
branches to inspect. To inspect only the `main` branch and incoming merge requests, you can use this configuration:

```yaml
qodana:
   only:
      - main
      - merge_requests
   image:
      name: jetbrains/qodana-<linter>
      entrypoint: [""]
   cache:
      - key: qodana-2023.3-$CI_DEFAULT_BRANCH-$CI_COMMIT_REF_SLUG
        fallback_keys:
           - qodana-2023.3-$CI_DEFAULT_BRANCH-
           - qodana-2023.3-
        paths:
           - .qodana/cache
   variables:
      QODANA_TOKEN: $qodana_token
   script:
      - qodana --results-dir=$CI_PROJECT_DIR/.qodana/results --cache-dir=$CI_PROJECT_DIR/.qodana/cache
```

## Expose Qodana reports

<link-summary>To make a report available in any given merge request without using Qodana Cloud, you can change the path 
to the artifacts.</link-summary>

To make a report available in any given merge request without using Qodana Cloud,
you can use the `artifacts` [`expose_as`](%GitLabExpose%) keywords
and change the path to the artifacts:

```yaml
qodana:
   image:
      name: jetbrains/qodana-<linter>
      entrypoint: [""]
   cache:
      - key: qodana-2023.3-$CI_DEFAULT_BRANCH-$CI_COMMIT_REF_SLUG
        fallback_keys:
           - qodana-2023.3-$CI_DEFAULT_BRANCH-
           - qodana-2023.3-
        paths:
           - .qodana/cache
   variables:
      QODANA_TOKEN: $qodana_token           - 
   script:
      - qodana --save-report --results-dir=$CI_PROJECT_DIR/.qodana/results
         --cache-dir=$CI_PROJECT_DIR/.qodana/cache
   artifacts:
      paths:
         - qodana/results/
      expose_as: 'Qodana report'
```

Assuming that you have configured your pipeline in a similar manner, this is what it may look like:

1. Qodana report affiliated with a pipeline in a merge request

   <img src="gitlab-exposed-artifacts.png" alt="Qodana report affiliated with a pipeline in a merge request" width="706" border-effect="line"/>

2. Available actions for a given exposed Qodana artifact
   
   <img src="gitlab-exposed-artifacts-expanded.png" alt="Available actions for a given exposed Qodana artifact" width="706" border-effect="line"/>

## Quality gate and baseline

<link-summary>You can use the --fail-threshold number and --baseline path/to/qodana.sarif.json lines in the script block 
to invoke the quality gate and baseline features.</link-summary>

You can use the `--fail-threshold <number>` and `--baseline <path/to/qodana.sarif.json>` lines in the `script` block to 
invoke the [quality gate](quality-gate.topic) and [baseline](baseline.topic) features.

```yaml
qodana:
   image:
      name: jetbrains/qodana-<linter>
      entrypoint: [""]
   cache:
      - key: qodana-2023.3-$CI_DEFAULT_BRANCH-$CI_COMMIT_REF_SLUG
        fallback_keys:
           - qodana-2023.3-$CI_DEFAULT_BRANCH-
           - qodana-2023.3-
        paths:
           - .qodana/cache
   variables:
      QODANA_TOKEN: $qodana_token           - 
   script:
      - qodana --fail-threshold <number> --baseline <path/to/qodana.sarif.json> --results-dir=$CI_PROJECT_DIR/.qodana/results
         --cache-dir=$CI_PROJECT_DIR/.qodana/cache
   artifacts:
      paths:
         - qodana/report/
      expose_as: 'Qodana report'
```

## Generate Code Quality reports
{id="gitlab-generate-code-quality-reports"}

<link-summary>By default, %product% lets you use the merge request UI of GitLab CI/CD to view specific lines of code 
that contain problems along with their description and recommendations for improvement.</link-summary>

Starting from version 2024.1 of %product%, using the merge request UI of GitLab CI/CD you can view specific lines of 
code that contain problems along with their description and recommendations for improvement. 

To implement this feature, %product% generates JSON-formatted inspection reports supported by 
[Code Quality](https://docs.gitlab.com/ee/ci/testing/code_quality.html) and contained in the `gl-code-quality-report.json` file. To configure this, to the `artifacts` block 
of the GitLab CI/CD configuration add the `codequality`keyword and specify the path to the `gl-code-quality-report.json` 
file, for example:

```yaml
   image:
        name: jetbrains/qodana-<linter>
        entrypoint: [""]
   cache:
       - key: qodana-2024.1-$CI_DEFAULT_BRANCH-$CI_COMMIT_REF_SLUG
         fallback_keys:
             - qodana-2024.1-$CI_DEFAULT_BRANCH-
             - qodana-2024.1-
         paths:
             - .qodana/cache
   variables:
       QODANA_TOKEN: $qodana_token
   script:
       - qodana --results-dir=$CI_PROJECT_DIR/.qodana/results
           --cache-dir=$CI_PROJECT_DIR/.qodana/cache
   artifacts:  
       reports:
           codequality: .qodana/results/gl-code-quality-report.json # Path to the report
```

<seealso>
    <category ref="external">
        <a href="https://rpadovani.com/gitlab-jetbrains-qodana">'Integrating JetBrains Qodana with GitLab
            pipelines' by Riccardo Padovani
        </a>
        <a href="https://blog.griefed.de/2022/04/30/qodana-and-gitlab/">'Qodana, GitLab and Discord'
            by Griefed
        </a>
    </category>
</seealso>
