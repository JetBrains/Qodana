[//]: # (title: GitHub Actions & Application)

![official JetBrains project](https://jb.gg/badges/official-flat-square.svg)

![EAP](eap-alert.png)

Tools created by JetBrains are capable of detecting dozens of error-types and inconsistencies in your repository. 
Their flexible mechanisms of resolving problems allow you to easier improve the code structure, conform your code to numerous guidelines and standards, detect performance issues, and so on. 
And now with the Qodana App and Actions available in GitHub, all these features are just around the corner!

## Qodana Github App

![Qodana Github App](qodana-app-banner.png)

**Qodana Github App** is a great way to improve the code quality of your Github repository. It can be installed to specific repositories or whole organizations by an organization owner or a repository admin.  
Once you install the app to your repository, it starts monitoring all its pull requests.

If there is a problem in your pull request, Qodana App will add a comment to each problematic line.
To get a deep summary, you can open the Qodana analytics results' page.

Explore the Qodana results in this [pull request](https://github.com/JetBrains/qodana-examples/pull/1/checks?check_run_id=1523719524) to the qodana-examples repository.

### How to start

1. Install Qodana App from Marketplace to your repository: [Qodana Github App](https://github.com/marketplace/qodana).
2. Make sure you are a public member of JetBrains or the Qodana-demo organization.
    * [How to become a public member of a Github Organization](https://docs.github.com/en/free-pro-team@latest/github/setting-up-and-managing-your-github-user-account/publicizing-or-hiding-organization-membership)
    * [JetBrains Github Organization](https://github.com/JetBrains)
    * [Qodana-demo Github Organization](https://github.com/Qodana-demo)
3. Create a new pull request and wait for the results.
    * The build output will be accessible within a *Checks* tab on your pull request.
    * See [this GitHub blog post](https://github.blog/2018-05-07-introducing-checks-api/) for more examples of Checks API.

## Qodana Github Action

Qodana Github Action is a more general tool for easier continuous code inspection.
Anyone with the write permission to a repository can set up a continuous code inspection with Qodana using GitHub Actions. 

### How to start

Read the guidelines in [this repository](https://github.com/JetBrains/qodana-action).

![Qodana Github Action](qodana-github-action-result.png)


## Contact

We are just beginning our journey and, as in case with any new project, we are eager to hear your feedback!
Please, contact us at [qodana-support@jetbrains.com](mailto:qodana-support@jetbrains.com) or via [our issue tracker](https://youtrack.jetbrains.com/newIssue?project=QD).