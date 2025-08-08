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

| Native solutions              | [Docker images](deploy-qodana.md#Docker+images) |
|-------------------------------|------------------------------------|
| [](qodana-azure-pipelines.md) | [](bitbucket.md)                   |
| [](circleci.md)               | [](jenkins.md)                     |
| [](github.md)                 |                                    |
| [](gitlab.md)                 |                                    |
| [](teamcity.md)               |                                    |

This section shows how you can configure %product% for GitHub Actions and Jenkins pipelines. The complete 
guides for other CI systems including basic configuration examples are available in the [](ci.md) section. 

## GitHub Actions

<include from="lib_qd.topic" element-id="github-basic-configuration"/>

## Jenkins

Jenkins is a good example of how you can use Docker images of %product%. 

<include from="jenkins.md" element-id="Prepare+your+project"/>

<include from="jenkins.md" element-id="jenkins-for-use-case"/>

## What's next

You can extend the existing CI configurations. For example, you can employ the [quality gate](quality-gate.topic) or 
[baseline](baseline.topic) features. 