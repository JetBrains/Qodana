[//]: # (title: Overview of CI integration)

<tip>To learn more about available %product% licenses, visit the
    <a href="https://www.jetbrains.com/qodana/buy/?billing=yearly">Subscription Options and Pricing</a> page.
    Also, <a href="https://www.jetbrains.com/qodana/request-a-demo/">request a demo</a> to explore %product% capabilities.
</tip>

All Qodana [linters](linters.md) are available for integration in CI/CD pipelines. Depending on a tool, %product% can be
integrated either as a native solution or a Docker image.

| CI/CD tool                                              | Integration type |
|---------------------------------------------------------|------------------|
| [Azure Pipelines](qodana-azure-pipelines.md)            | Native solution  |
| [Bitbucket Cloud](bitbucket.md)                         | Docker image     |
| [CircleCI](circleci.md)                                 | Native solution  |
| [GitHub Actions](github.md)                             | Native solution  |
| [GitLab CI/CD](gitlab.md)                               | Native solution  |
| [Jenkins](jenkins.md)                                   | Docker image     |
| [TeamCity](teamcity.md)                                 | Native solution  |

All integration guides require that you get a [project token](project-token.md) before running %product%. 