[//]: # (title: GitLab CI/CD)

### Basic Example

To add a Qodana runner to a GitLab CI/CD pipeline, use the following configuration example: (`.gitlab-ci.yml`):

```yaml
    qodana:
     image:
       name: jetbrains/qodana-<linter>
       entrypoint: ['']
     script:
       - /opt/idea/bin/entrypoint --results-dir=$CI_PROJECT_DIR/qodana --save-report --report-dir=$CI_PROJECT_DIR/qodana/report
     artifacts:
       paths:
         - qodana
```

### Exposing a Qodana report

In order for a report to be available in any given merge request, you need to make use of the [`expose_as`](https://docs.gitlab.com/ee/ci/yaml/#artifactsexpose_as)-keyword
and change the path to the artifacts. This will render the report available in any affiliated merge request: (`.gitlab-ci.yml`):

```yaml
    qodana:
     image:
       name: jetbrains/qodana-<linter>
       entrypoint: ['']
     script:
       - /opt/idea/bin/entrypoint --results-dir=$CI_PROJECT_DIR/qodana --save-report --report-dir=$CI_PROJECT_DIR/qodana/report
     artifacts:
       paths:
         - qodana/report/
       expose_as: 'Qodana report'
```

Assuming you have configured your pipeline in a similar manner, this is what it may look like:

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