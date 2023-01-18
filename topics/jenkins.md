[//]: # (title: Jenkins)

<var name="JenkinsLink" value="www.jenkins.io/doc/book/pipeline/jenkinsfile/#using-environment-variables"/>
<var name="Multipipe" value="www.jenkins.io/doc/book/pipeline/multibranch/#branches-and-pull-requests"/>
<var name="MultipipeCreate" value="www.jenkins.io/doc/book/pipeline/multibranch/#creating-a-multibranch-pipeline"/>
<var name="Dockeraccess" value="docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user"/>
<var name="Dplugin" value="plugins.jenkins.io/docker-plugin/"/>
<var name="DPplugin" value="plugins.jenkins.io/docker-workflow/"/>
<var name="Gplugin" value="plugins.jenkins.io/git/"/>
<var name="JPullRequests" value="www.jenkins.io/doc/book/pipeline/multibranch/#supporting-pull-requests" />
<var name="JenkinsCred" value="www.jenkins.io/doc/book/using/using-credentials/#adding-new-global-credentials"/>

[Jenkins](https://www.jenkins.io/doc/) is a self-contained, open-source server that automates software-related tasks 
including building, testing, and deploying software. This section explains how you can configure 
[Docker images](docker-images.md) of %product% in Jenkins [Multibranch Pipelines](https://%Multipipe%), and covers the
following cases:

* Inspecting a specific branch
* Forwarding inspection results to [Qodana Cloud](cloud-about.xml) 

## Prepare your project

Make sure that these plugins are installed on your Jenkins instance:

* [Docker](https://%Dplugin%) and [Docker Pipeline](https://%DPplugin%) are required for running Docker images
* [git](https://%Gplugin%) is required for carrying out git operations in Jenkins projects

Make sure that Docker is installed and accessible by Jenkins. 

If applicable, make sure that Docker accessible by the `jenkins` user as described in the 
[Manage Docker as a non-root user](https://%Dockeraccess%) section of the Docker documentation.

Create a Multibranch Pipeline project as described on the [Jenkins documentation portal](https://%MultipipeCreate%).

In the root directory of your project repository, create the `Jenkinsfile`. This file will contain Jenkins 
configuration scripts described in this section. 

## Basic configuration

This is the basic configuration of the Jenkins Pipeline.

```groovy
pipeline {
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

This configuration uses the `docker` agent to invoke %product% [Docker images](docker-images.md). Using the 
`WORKSPACE` variable, the `args` block mounts the local checkout directory to the project directory of a Docker image, 
and `image` specifies the Docker image invoked.  

The `stage` block calls %product%. Here, you can also specify the [options](docker-image-configuration.xml) 
you would like to configure %product% with.  

## Inspect specific branches

Using the `when` block, you can tell %product% which branches of your project to inspect. For example, this configuration 
lets you inspect only the `feature` branch. 

```groovy
pipeline {
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

You can inspect pull requests as described in the [Supporting Pull Requests](https://%JPullRequests%) section
of the Jenkins documentation.

## Forward reports to Qodana Cloud

The `environment` block lets you specify the variables and values that are required by Qodana Cloud:

* `QODANA_TOKEN` is a [Qodana Cloud project token](cloud-projects.xml#cloud-manage-projects) contained as the value for 
   the `qodana-token` credentials, see the [Adding new global credentials](https://%JenkinsCred%) section of the Jenkins documentation for details
* `QODANA_REMOTE_URL` is the repository URL referring to the `GIT_URL` [environment variable](https://%JenkinsLink%)
* `QODANA_BRANCH` is the branch name referring to the `GIT_BRANCH` environment variable
* `QODANA_REVISION` is the commit hash referring to the `GIT_COMMIT` environment variable
* `QODANA_JOB_URL` is the job URL referring to the `JOB_DISPLAY_URL` environment variable

```groovy
pipeline {
   environment {
      QODANA_TOKEN=credentials('qodana-token')
      QODANA_REMOTE_URL="${GIT_URL}"
      QODANA_BRANCH="${GIT_BRANCH}"
      QODANA_REVISION="${GIT_COMMIT}"
      QODANA_JOB_URL="${JOB_DISPLAY_URL}"
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

## Combined configuration

Here is the Jenkins configuration that covers all approaches described in this section. 

```groovy
pipeline {
   environment {
      QODANA_TOKEN=credentials('qodana-token')
      QODANA_REMOTE_URL="${GIT_URL}"
      QODANA_BRANCH="${GIT_BRANCH}"
      QODANA_REVISION="${GIT_COMMIT}"
      QODANA_JOB_URL="${JOB_DISPLAY_URL}" 
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
            sh '''
               qodana \
               --fail-threshold <number>
               '''
         }
      }
   }
}
```