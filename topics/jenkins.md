[//]: # (title: Jenkins)

[Jenkins](https://www.jenkins.io/doc/) is a self-contained, open source server for automation of software-related tasks 
such as building, testing, and deployment of software. To perform tasks, Jenkins uses the
[Pipeline](https://www.jenkins.io/doc/book/pipeline/) functionality.

To be able to run Qodana in Jenkins, make sure that the [Docker](https://plugins.jenkins.io/docker-plugin/) and 
[Docker Pipeline](https://plugins.jenkins.io/docker-workflow/) plugins are installed on your Jenkins instance.

Below is the Pipeline stage that invokes the `docker` agent with the following configuration:

* `image` instructs to pull the Qodana Docker image, and `qodana-<linter>` here specifies the required Qodana [linter](linters.md).
* `args` provide arguments for binding the project root and report directories to the Qodana image.

```groovy
stage('Qodana') {
    agent {
        docker {
            args '''
           -v /opt/qodana/reports:/data/reports 
           -v /opt/qodana/cache:/data/cache
           -v /opt/qodana/results:/data/results
           -v /opt/qodana/qodana.sarif.json:/data/qodana.sarif.json
           --entrypoint=""
           '''
            image 'jetbrains/qodana-<linter>'
        }
    }
    steps {
        sh "qodana --save-report"
    }
}
```