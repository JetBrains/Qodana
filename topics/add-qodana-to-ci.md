[//]: # (title: Add Qodana to your CI pipeline)

<var name="github" value="https://github.com/marketplace/actions/qodana-scan"/>
<var name="JenkinsLink" value="https://www.jenkins.io/doc/book/pipeline/jenkinsfile/#using-environment-variables"/>
<var name="Multipipe" value="https://www.jenkins.io/doc/book/pipeline/multibranch/#branches-and-pull-requests"/>
<var name="MultipipeCreate" value="https://www.jenkins.io/doc/book/pipeline/multibranch/#creating-a-multibranch-pipeline"/>
<var name="Dockeraccess" value="https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user"/>
<var name="Dplugin" value="https://plugins.jenkins.io/docker-plugin/"/>
<var name="DPplugin" value="https://plugins.jenkins.io/docker-workflow/"/>
<var name="Gplugin" value="https://plugins.jenkins.io/git/"/>
<var name="JPullRequests" value="https://www.jenkins.io/doc/book/pipeline/multibranch/#supporting-pull-requests" />
<var name="JenkinsCred" value="https://www.jenkins.io/doc/book/using/using-credentials/#adding-new-global-credentials"/>

%product% provides solutions for various CI systems; several of them are implemented as native solutions, while 
for several others you can run Docker images of %product%, see the table below: 

| Native solutions                | [Docker images](docker-images.md) |
|---------------------------------|-----------------------------------|
| [](qodana-azure-pipelines.md)   | [](bitbucket.md)                  |
| [](circleci.md)                 | [](gitlab.md)                     |
| [](github.md)                   | [](jenkins.md)                    |
| [](teamcity.md)                 | [](space-automation.md)           |

This section shows how you can configure %product% for GitHub Actions and Jenkins pipelines. The complete 
guides for other CI systems including basic configuration examples are available in the [](ci.md) section. 

## GitHub Actions

<include src="lib_qd.xml" include-id="github-basic-configuration"/>

## Jenkins

Jenkins is a good example of how you can use Docker images of %product%. 

<include src="jenkins.md" include-id="jenkins-prepare-project"/>

<include src="jenkins.md" include-id="jenkins-basic-config"/>

## What's next

You can extend the existing CI configurations. For example, you can employ the [quality gate](quality-gate.xml) or 
[baseline](baseline.xml) features. 