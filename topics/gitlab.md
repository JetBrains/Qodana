[//]: # (title: GitLab CI/CD)

<var name="GitLabLink" value="docs.gitlab.com/ee/ci/variables/"/>
<var name="GitLabPredefined" value="docs.gitlab.com/ee/ci/variables/predefined_variables.html#predefined-variables-reference"/>
<var name="GitLabExpose" value="docs.gitlab.com/ee/ci/yaml/#artifactsexpose_as"/>

[GitLab CI/CD](https://docs.gitlab.com/ee/ci/) is a tool for software development that uses various CI/CD methodologies. This 
section explains how you can run %product% [Docker images](docker-images.md) within GitLab CI/CD 
[pipelines](https://docs.gitlab.com/ee/ci/pipelines/) and covers the following cases:

* Inspecting specific branches and merge requests
* Forwarding inspection reports to [Qodana Cloud](cloud-about.xml)
* Exposing %product% reports in the GitLab CI/CD user interface

## Prepare your project

Make sure that your project repository is accessible by GitLab CI/CD.

In the root directory of your project, save the `.gitlab-ci.yml` file. This file will contain pipeline configuration 
that will be used by GitLab CI/CD. 

## Basic configuration

This is the basic pipeline configuration.

```yaml
qodana:
   image:
      name: jetbrains/qodana-<linter>
      entrypoint: [""]
   script:
      - qodana --save-report --results-dir=$CI_PROJECT_DIR/qodana
         --report-dir=$CI_PROJECT_DIR/qodana/report
   artifacts:
      paths:
         - qodana
```

In this configuration, the [`image`](https://docs.gitlab.com/ee/ci/yaml/#image) option of this configuration pulls and runs the %product% [Docker image](docker-images.md) of your choice.

The [`script`](https://docs.gitlab.com/ee/ci/yaml/#script) option enumerates the %product% configuration options:

* `--save-report` and `--report-dir` to generate and save reports to a specific folder
* `--results-dir` to save the generated [SARIF file](qodana-sarif-output.md) to a specific folder

You can read the [Docker image configuration](docker-image-configuration.xml) section of this documentation to learn more 
about available configuration options.

The [`artifacts`](https://docs.gitlab.com/ee/ci/yaml/#artifacts) option configures job artifacts.

## Inspect specific branches

Using the [`only`](https://docs.gitlab.com/ee/ci/yaml/index.html#only--except) keyword, %product% can inspect specific 
branches. To inspect the `main` branch and incoming merge requests, you can use this configuration:

```yaml
qodana:
   only:
      - main
      - merge_requests
   image:
      name: jetbrains/qodana-<linter>
      entrypoint: [""]
   script:
      - qodana --save-report --results-dir=$CI_PROJECT_DIR/qodana
         --report-dir=$CI_PROJECT_DIR/qodana/report
   artifacts:
      paths:
         - qodana
```

## Forward reports to Qodana Cloud

Once the inspection step is complete, inspection reports can be forwarded to [Qodana Cloud](cloud-about.xml) for 
storage and overview. 

This configuration defines the `QODANA_TOKEN` [variable](https://%GitLabLink%) containing the
[project token](cloud-projects.xml). Besides that, Qodana Cloud also requires the values from the
[predefined variables](https://%GitLabPredefined%) of GitLab CI/CD assigned to the following variables:  

* `QODANA_REMOTE_URL`
* `QODANA_BRANCH`
* `QODANA_REPO_URL`
* `QODANA_JOB_URL`

```yaml
qodana:
   image:
      name: jetbrains/qodana-<linter>
      entrypoint: [""]
   variables:
      QODANA_TOKEN: <your-project-token>
      QODANA_REMOTE_URL: git@$CI_SERVER_HOST:$CI_PROJECT_PATH.git
      QODANA_BRANCH: $CI_COMMIT_BRANCH
      QODANA_REPO_URL: $CI_PROJECT_URL
      QODANA_JOB_URL: $CI_JOB_URL
   script:
      - qodana --save-report --results-dir=$CI_PROJECT_DIR/qodana
         --report-dir=$CI_PROJECT_DIR/qodana/report
   artifacts:
      paths:
         - qodana
```

## Expose Qodana reports

To make a report available in any given merge request, you can use the [`expose_as`](https://%GitLabExpose%) keyword
and change the path to the artifacts:

```yaml
qodana:
   image:
      name: jetbrains/qodana-<linter>
      entrypoint: [""]
   script:
      - qodana --save-report --results-dir=$CI_PROJECT_DIR/qodana
         --report-dir=$CI_PROJECT_DIR/qodana/report
   artifacts:
      paths:
         - qodana/report/
      expose_as: 'Qodana report'
```

Assuming that you have configured your pipeline in a similar manner, this is what it may look like:

1. Qodana report affiliated with a pipeline in a merge request
   <img src="gitlab-exposed-artifacts.png" alt="Qodana report affiliated with a pipeline in a merge request" width="706" border-effect="line"/>

2. Available actions for a given exposed Qodana artifact
   <img src="gitlab-exposed-artifacts-expanded.png" alt="Available actions for a given exposed Qodana artifact" width="706" border-effect="line"/>

## Combined configuration

This configuration combines all approaches mentioned in this section. 

```yaml
qodana:
   only:
      - main
      - merge_requests
   image:
      name: jetbrains/qodana-<linter>
      entrypoint: [""]
   variables:
      QODANA_TOKEN: <your-project-token>
      QODANA_REMOTE_URL: git@$CI_SERVER_HOST:$CI_PROJECT_PATH.git
      QODANA_BRANCH: $CI_COMMIT_BRANCH
      QODANA_REPO_URL: $CI_PROJECT_URL
      QODANA_JOB_URL: $CI_JOB_URL
   script:
      - qodana --save-report --results-dir=$CI_PROJECT_DIR/qodana
         --report-dir=$CI_PROJECT_DIR/qodana/report
   artifacts:
      paths:
         - qodana/report/
      expose_as: 'Qodana report'
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
