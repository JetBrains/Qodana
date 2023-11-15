[//]: # (title: Integration with CI systems)

<var name="azure" value="https://marketplace.visualstudio.com/items?itemName=JetBrains.qodana"/>
<var name="circleci" value="https://circleci.com/developer/orbs/orb/jetbrains/qodana"/>
<var name="github" value="https://github.com/marketplace/actions/qodana-scan"/>

You can build %product% into virtually any Continuous Integration (CI) system. Below is the list of %product% solutions
for several CI products that %product% already provides: 

| CI integration guide          | %product% solution                          |
|-------------------------------|---------------------------------------------|
| [](qodana-azure-pipelines.md) | [Qodana Azure Pipelines extension](%azure%) |
| [](bitbucket.md)              | [Docker images](docker-images.md)           |
| [](circleci.md)               | [CircleCI Qodana orb](%circleci%)           |
| [](github.md)                 | [Qodana Scan GitHub action](%github%)       |
| [](gitlab.md)                 | [Docker images](docker-images.md)           |
| [](jenkins.md)                | [Docker images](docker-images.md)           |
| [](space-automation.md)       | [Docker images](docker-images.md)           |
| [](teamcity.md)               | Built in TeamCity starting from 2022.04     |

If you don't find your CI in this table, you can configure and run %product% [Docker images](docker-images.md) in your pipeline. 

