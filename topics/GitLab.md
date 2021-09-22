[//]: # (title: GitLab CI)

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

<p><include src="lib_qd.xml" include-id="docker-options-tip"/></p>