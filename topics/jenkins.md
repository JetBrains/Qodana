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

[Jenkins](https://www.jenkins.io/doc/) is a self-contained, open-source server that automates software-related tasks 
including building, testing, and deploying software. This section explains how you can configure %product%
[Docker images](docker-images.md) in Jenkins [Multibranch Pipelines](%Multipipe%)

## Prepare your project

Make sure that these plugins are installed on your Jenkins instance:

* [Docker](%Dplugin%) and [Docker Pipeline](%DPplugin%) are required for running Docker images
* [git](%Gplugin%) is required for git operations in Jenkins projects

Make sure that Docker is installed and accessible by Jenkins. 

If applicable, make sure that Docker is accessible by the `jenkins` user as described in the 
[Manage Docker as a non-root user](%Dockeraccess%) section of the Docker documentation.

Create a Multibranch Pipeline project as described on the [Jenkins documentation portal](%MultipipeCreate%).

In the root directory of your project repository, create the `Jenkinsfile`. This file will contain Jenkins 
configuration scripts described in this section. 

## Basic configuration

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
                sh '''
                qodana \
                --fail-threshold <number>
                '''
            }
        }
    }
}
```

In this configuration, the `environment` block defines the `QODANA_TOKEN` variable to invoke the
[project token](project-token.md) generated in Qodana Cloud and contained in 
the `qodana-token` [global credentials](%JenkinsCred%). The project token is required by the paid %product%
[linters](pricing.md#pricing-linters-licenses), and is optional for using with the Community linters. You can see these sections 
to learn how to generate the project token in Qodana Cloud:

* The [](cloud-onboarding.md) section explains how to get the project token generated while first working with Qodana Cloud
* The [](cloud-projects.xml#cloud-manage-projects) section explains how to create a project in the existing Qodana Cloud organization

This configuration uses the `docker` agent to invoke %product% [Docker images](docker-images.md). Using the 
`WORKSPACE` variable, the `args` block mounts the local checkout directory to the project directory of a Docker image, 
and `image` specifies the Docker image invoked.  

The `stage` block calls %product%. Here, you can also specify the [options](docker-image-configuration.xml) 
you would like to configure %product% with. This configuration invokes the [quality gate](quality-gate.xml) feature 
using the `--fail-threshold <number>` line. 

## Inspect specific branches

Using the `when` block, you can tell %product% which branches of your project to inspect. For example, this configuration 
lets you inspect only the `feature` branch. 

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

You can inspect pull requests as described in the [Supporting Pull Requests](%JPullRequests%) section
of the Jenkins documentation.