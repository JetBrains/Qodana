[//]: # (title: Jenkins)

<var name="JenkinsLink" value="https://www.jenkins.io/doc/book/pipeline/jenkinsfile/#using-environment-variables"/>
<var name="Multipipe" value="https://www.jenkins.io/doc/book/pipeline/multibranch/#branches-and-pull-requests"/>
<var name="MultipipeCreate" value="https://www.jenkins.io/doc/book/pipeline/multibranch/#creating-a-multibranch-pipeline"/>
<var name="Dockeraccess" value="https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user"/>
<var name="Dplugin" value="https://plugins.jenkins.io/docker-plugin/"/>
<var name="DPplugin" value="https://plugins.jenkins.io/docker-workflow/"/>
<var name="Gplugin" value="https://plugins.jenkins.io/git/"/>
<var name="JPullRequests" value="https://www.jenkins.io/doc/book/pipeline/multibranch/#supporting-pull-requests" />
<var name="JenkinsCred" value="https://www.jenkins.io/doc/book/using/using-credentials/#adding-new-global-credentials"/>

<link-summary>This section explains how you can configure %instance%
Docker images in Jenkins Multibranch Pipelines.</link-summary>

[Jenkins](https://www.jenkins.io/doc/) is a self-contained, open-source server that automates software-related tasks 
including building, testing, and deploying software. This section explains how you can configure %instance%
[Docker images](deploy-qodana.md#Docker+images) in Jenkins [Multibranch Pipelines](%Multipipe%).

## Before you start

### Qodana Cloud

<include from="lib_qd.topic" element-id="cicd-cloud-intro"/>

### Prepare your project

<link-summary>Preparation steps you need to perform before running %product% in a Jenkins Pipeline.</link-summary>

Make sure that these plugins are installed on your Jenkins instance:

* [Docker](%Dplugin%) and [Docker Pipeline](%DPplugin%) are required for running Docker images
* [git](%Gplugin%) is required for git operations in Jenkins projects

Make sure that Docker is installed and accessible to Jenkins. 

If applicable, make sure that Docker is accessible to the `jenkins` user as described in the 
[Manage Docker as a non-root user](%Dockeraccess%) section of the Docker documentation.

Create a Multibranch Pipeline project as described on the [Jenkins documentation portal](%MultipipeCreate%).

In the root directory of your project repository, create the `Jenkinsfile`. This file will contain Jenkins 
configuration scripts described in this section. 

## Basic configuration

<link-summary>This section shows the basic configuration of the Jenkins Pipeline.</link-summary>

<include from="lib_qd.topic" element-id="major-version-note"/>

This is the basic configuration of the Jenkins Pipeline.

```groovy
pipeline {
    environment {
        QODANA_TOKEN=credentials('qodana-token')
    }
    agent {
        docker {
            args '''
              -v "${WORKSPACE}":/data/project
              --entrypoint=""
              '''
            image 'jetbrains/qodana-<linter>'
        }
    }
    stages {
        stage('Qodana') {
            steps {
                sh '''qodana'''
            }
        }
    }
}
```

In this configuration, the `environment` block defines any environment variables to be used in the pipeline.
The `QODANA_TOKEN` variable refers to the [project token](project-token.md) generated in Qodana Cloud and is contained in 
the `qodana-token` [global credentials](%JenkinsCred%). 

This configuration uses the `docker` agent to invoke %instance% [Docker images](deploy-qodana.md#Docker+images). Using the 
`WORKSPACE` variable, the `args` block mounts the local checkout directory to the project directory of a Docker image, 
and `image` specifies the Docker image invoked.  

The `stage` block calls %instance%. Here, you can also specify the [options](docker-image-configuration.topic) 
you would like to configure %instance% with like the [quality gate and baseline](#Quality+gate+and+baseline) features.

## Analyze specific branches

<link-summary>Using the `when` block, you can tell %instance% which branches of your project to analyze.</link-summary>

Using the `when` block, you can tell %instance% which branches of your project to analyze. For example, this configuration 
lets you analyze only the `feature` branch. 

```groovy
pipeline {
    environment {
        QODANA_TOKEN=credentials('qodana-token')
    }
   agent {
      docker {
         args '''
              -v "${WORKSPACE}":/data/project
              --entrypoint=""
              '''
         image 'jetbrains/qodana-<linter>'
      }
   }
   stages {
      stage('Qodana') {
         when {
            branch 'feature'
         }
         steps {
            sh '''qodana'''
         }
      }
   }    
}
```

You can analyze pull requests as described in the [Supporting Pull Requests](%JPullRequests%) section
of the Jenkins documentation.

## Quality gate and baseline

<link-summary>You can use the quality gate and baseline features by invoking the --fail-threshold and 
--baseline path/to/qodana.sarif.json options specified in the `steps` block.</link-summary>

This configuration invokes the [quality gate](quality-gate.topic) and [baseline](baseline.topic) features using the 
`--fail-threshold <number>` and `--baseline <path/to/qodana.sarif.json>` lines specified in the `steps` block.

```groovy
pipeline {
    environment {
        QODANA_TOKEN=credentials('qodana-token')
    }
    agent {
        docker {
            args '''
              -v "${WORKSPACE}":/data/project
              --entrypoint=""
              '''
            image 'jetbrains/qodana-<linter>'
        }
    }
    stages {
        stage('Qodana') {
            steps {
                sh '''
                qodana \
                --fail-threshold <number> \
                --baseline <path/to/qodana.sarif.json>
                '''
            }
        }
    }
}
```
