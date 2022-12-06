[//]: # (title: Jenkins)

[Jenkins](https://www.jenkins.io/doc/) is a self-contained, open source server for automation of software-related tasks 
such as building, testing, and deployment of software. To perform tasks, Jenkins uses the
[Pipeline](https://www.jenkins.io/doc/book/pipeline/) functionality.

To run Qodana in Jenkins, make sure that the [Docker](https://plugins.jenkins.io/docker-plugin/) and 
[Docker Pipeline](https://plugins.jenkins.io/docker-workflow/) plugins are installed on your Jenkins instance.

Here is the Jenkins Pipeline script that invokes the `docker` agent for running %product%:

```groovy
pipeline {
    agent {
        docker {
            args '''
                -v /opt/qodana/reports:/data/reports
                -v /opt/qodana/results:/data/results
                -v /opt/qodana/cache:/data/cache
                -v /opt/qodana/qodana.sarif.json:/data/qodana.sarif.json
                -v <path-to-project>:/data/project
                --entrypoint=""
            '''
            image 'jetbrains/qodana-<linter>'
        }
    } 
    stages {
        stage('Qodana') {
            steps {
                sh "qodana --save-report --project-dir=/data/project"
            }
        }
    }
}
```

In this script:

* `args` instructs to bind several paths to the %product% Docker image
* `image` specifies the required Qodana [linter](linters.md)
