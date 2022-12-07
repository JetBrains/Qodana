[//]: # (title: GitLab CI/CD)

### Basic Example

To add a Qodana runner to a GitLab CI/CD pipeline, use the following configuration sample (`.gitlab-ci.yml`):

```yaml
stages:
  - qodana

qodana:
  stage: qodana
  only:
    - main
    - merge_requests
  image:
    name: jetbrains/qodana-js:2022.3-eap
    entrypoint: [""]
  variables:
    QODANA_REMOTE_URL: git@$CI_SERVER_HOST:$CI_PROJECT_PATH.git
    QODANA_BRANCH: $CI_COMMIT_BRANCH
    QODANA_REPO_URL: $CI_PROJECT_URL
    QODANA_JOB_URL: $CI_JOB_URL
  script:
    - qodana --save-report --results-dir=$CI_PROJECT_DIR/qodana --report-dir=$CI_PROJECT_DIR/qodana/report
  artifacts:
    paths:
      - qodana
```

Using this configuration, %product% will inspect the main branch and all merge requests coming to your repository.

### Exposing a Qodana report

To make a report available in any given merge request, you can use the [`expose_as`](https://docs.gitlab.com/ee/ci/yaml/#artifactsexpose_as) keyword
and change the path to the artifacts (`.gitlab-ci.yml`):

```yaml
stages:
  - qodana

qodana:
  stage: qodana
  only:
    - main
    - merge_requests
  image:
    name: jetbrains/qodana-<linter>
    entrypoint: [""]
  variables:
    QODANA_REMOTE_URL: git@$CI_SERVER_HOST:$CI_PROJECT_PATH.git
    QODANA_BRANCH: $CI_COMMIT_BRANCH
    QODANA_REPO_URL: $CI_PROJECT_URL
    QODANA_JOB_URL: $CI_JOB_URL
  script:
    - qodana --save-report --results-dir=$CI_PROJECT_DIR/qodana --report-dir=$CI_PROJECT_DIR/qodana/report
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


<p><include src="lib_qd.xml" include-id="docker-options-tip"/></p>

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
