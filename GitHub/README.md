# Qodana GitHub Actions & Application

![official JetBrains project](https://jb.gg/badges/official-flat-square.svg)

![EAP](../resources/eap-alert.png)

## General

Tools created by JetBrains are capable of detecting dozens of error-types and inconsistencies in your repository. 
Its flexible mechanism of resolving problems allows you to easily improve the code structure, conform your code to numerous guidelines and standards, detect performance issues and so on. 
And now with Qodana  App and Actions available in GitHub, all these features are just around the corner!

## Qodana Github App

Qodana Github App is a great way to improve the code quality of your Github repository. It can be installed on specific repositories or whole organizations by an organization owner or a repository admin.
Once you install the app in your repository, it starts with monitoring all pull-requests in it.

If there is a problem in your pull request, Qodana App will add a comment to each problematic line.
In addition, Qodana analytics result page is available for deeper summary.

Look at Qodana results in this [pull request](https://github.com/JetBrains/qodana-examples/pull/1/checks?check_run_id=1523719524) to qodana-examples repository.

### How to start

##### 1. Install Qodana App from Marketplace to your repository: [Qodana Github App](https://github.com/marketplace/qodana)

##### 2. Make sure you are a public member of JetBrains or Qodana-demo organization.

* [How to become a public member of a Github Organization](https://docs.github.com/en/free-pro-team@latest/github/setting-up-and-managing-your-github-user-account/publicizing-or-hiding-organization-membership)
* [JetBrains Github Organization](https://github.com/JetBrains)
* [Qodana-demo Github Organization](https://github.com/Qodana-demo)

##### 3. Create new pull request and wait for results 

* Build output will be accessible within a *Checks* tab on your pull request. 
* Look at [this Github blog post](https://github.blog/2018-05-07-introducing-checks-api/) for more examples of Checks API.

## Qodana Github Action

Qodana Github Action is more general tool, which makes easier continuous code inspection.
Anyone with write permission to a repository can set up continuous code inspection with Qodana using GitHub Actions. 

### How to start

Check out how to guideline in [this repository](https://github.com/JetBrains/qodana-action).

![Qodana Github Action](../resources/qodana-github-action-result.png)


#### Contact
 We are in the beginning of our journey and, as any new project, we are eager to hear your feedback!
Please, contact us at [qodana-support@jetbrains.com](mailto:qodana-support@jetbrains.com) or via [our issue tracker](https://youtrack.jetbrains.com/newIssue?project=QD).