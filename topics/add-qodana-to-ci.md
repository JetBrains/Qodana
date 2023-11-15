[//]: # (title: Add Qodana to your CI)

<var name="github" value="https://github.com/marketplace/actions/qodana-scan"/>

Currently, %product% provides solutions for various CI systems; several of them are native, while for several others we 
have developed the guides explaining how to run %product% Docker images as shown in this table: 

| Native solutions                | [Docker images](docker-images.md) |
|---------------------------------|-----------------------------------|
| [](qodana-azure-pipelines.md)   | [](bitbucket.md)                  |
| [](circleci.md)                 | [](gitlab.md)                     |
| [](github.md)                   | [](jenkins.md)                    |
| [](teamcity.md)                 | [](space-automation.md)           |

This use case explains how you can configure %product% for running in GitHub Actions and Jenkins pipelines. The complete 
guides for other CI systems including basic configuration examples are available in the [](ci.md) section. 

## GitHub Actions

<include src="lib_qd.xml" include-id="github-basic-configuration"/>

## Jenkins

Jenkins is a good example of the Docker image integration. 

<include src="jenkins.md" include-id="jenkins-prepare-project"/>

<include src="jenkins.md" include-id="jenkins-basic-config"/>

