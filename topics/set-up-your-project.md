# How to set up your project in Qodana Cloud

To be able to run analysis with any of our paid [linters](linters.md), you need to set up your project in Qodana Cloud 
first, because this will provide you with a [token](project-token.md) that paid linters require. Qodana Cloud guides you 
through the project setup, you can follow all instructions right in the [Qodana Cloud](cloud-get-access.topic) user 
interface. Also, %product% requires a connection to your repositories for counting [active contributors](contributors.md), 
as required by our license agreement.

Using the setup wizard, you can configure %product% for running in CI/CD pipelines using the GitHub integration and
a [public repository key](repository-key.md), or run %product% locally using 
[Qodana CLI](https://github.com/JetBrains/qodana-cli) and [JetBrains IDEs](qodana-ide-plugin.md).

<note>If you do not have access to the repository that you are going to inspect, then you should request this access and 
wait until you receive it.</note>

In case of CI/CD, whatever option you choose, you need to provide the URL to your repository, and the %product% wizard 
will let you choose the linter to analyze your repository, show the [project token](project-token.md) and provide a 
configuration snippet for your CI/CD solution. For GitHub, the wizard provides a separate workflow compared to other
VCS.

<!--If your repostiroy is hosted on GitHub, this will be easier. -->



<!-- Probably mention that all wizards have the same functionality where a user can choose a linter and so on -->

## GitHub integration


To enable the GitHub integration, navigate to your repository, and then install and authorize the `QA Test Qodana App` 
OAuth App for the repository you would like to analyze using %product%. After that, you will be able select the linter
for inspecting your repository, as well as save the GitHub Actions configuration to your repository automatically or
manually.

