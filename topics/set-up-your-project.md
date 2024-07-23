# How to set up your project in Qodana Cloud

<no-index/>

<warning>This is a draft document, so we do not recommend that you use it.</warning>

To be able to run analysis with any of our paid [linters](linters.md), you need to set up your project in Qodana Cloud 
first, because this will provide you with a [token](project-token.md) that paid linters require. Qodana Cloud guides you 
through the project setup, you can follow all instructions right in the [Qodana Cloud](cloud-get-access.topic) user 
interface. Also, %product% requires a connection to your repositories for [active contributors](contributors.md) counting, 
as required by our license agreement.

During the project setup, you can configure %product% for running in various [CI/CD pipelines](ci.md) for repositories hosted on
GitHub or any other VCS using a [public repository key](repository-key.md) or the `QA Test Qodana App` OAuth App in case
of GitHub, as well as running locally using [Qodana CLI](https://github.com/JetBrains/qodana-cli) and 
[JetBrains IDEs](qodana-ide-plugin.md).

To be able to run %product% in CI/CD pipelines, you need to provide the URL to your repository, and the project setup wizard 
will let you choose the linter to analyze your repository, generate a [project token](project-token.md), and provide a 
configuration snippet for your CI/CD software. 

## GitHub integration

If you plan to run the [Qodana Scan](github.md) GitHub action for a repository hosted on GitHub, you can authorize the 
`QA Test Qodana App` OAuth App for your repository or repositories that you would like to analyze. After that, you will 
be able to select the linter and save the GitHub Actions configuration to your repository.

If you do not have access to the repository that you are going to analyze, then you should request this access and
wait until you receive it.