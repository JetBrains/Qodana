[//]: # (title: Qodana GitHub Action and Application)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

![EAP](eap-alert.png)

Tools created by JetBrains are capable of detecting dozens of error-types and inconsistencies in your repository.
Their flexible mechanisms of resolving problems allow you to easier improve the code structure, conform your code to numerous guidelines and standards, detect performance issues, and so on.

And now with the Qodana App and Actions available in GitHub, all these features are just around the corner!

The [Qodana GitHub App](github-overview.md#Qodana+GitHub+App) supports only public repositories. For private repositories use the [Qodana GitHub Action](github-overview.md#Qodana+GitHub+Action).

## Qodana GitHub App

![Qodana Github App](qodana-app-banner.png)

**Qodana Github App** is a great way to improve the code quality of your Github repository. It can be installed to specific repositories or whole organizations by an organization owner or a repository admin.  
Once you install the app to your repository, it starts monitoring all its pull requests.

If there is a problem in your pull request, Qodana App will add a comment to each problematic line.
To get a deep summary, you can open the Qodana analytics results' page.

Explore the Qodana results in this [pull request](https://github.com/JetBrains/qodana-examples/pull/2/checks?check_run_id=1776577456) to the qodana-examples repository.

### How to start
{id="how-to-start-github-app"}

1. The Qodana Github App is currently available to a limited number of users.
   If you want to get access to the Qodana Github App analysis, contact us at [qodana-support@jetbrains.com](mailto:qodana-support@jetbrains.com) or via [our issue tracker](https://youtrack.jetbrains.com/newIssue?project=QD).
2. Make sure you are a [public member](https://docs.github.com/en/github/setting-up-and-managing-your-github-user-account/publicizing-or-hiding-organization-membership) of the [Qodana-demo organization](https://github.com/Qodana-demo).
3. Install [Qodana Github App](https://github.com/apps/qodana/) to your repository.
4. Create a new pull request and wait for the results.
   * The build output will be displayed on the *Checks* tab of your pull request.


## Qodana GitHub Action

**Qodana Github Action** is a more general tool for easier continuous code inspection.
Anyone with the write permission to a repository can set up a continuous code inspection with Qodana using GitHub Actions.

### How to start
{id="how-to-start-github-action"}

Follow the guidelines for the [Qodana Github Action](https://github.com/marketplace/actions/qodana-code-inspection) on Github Marketplace.

## Contact

We are just beginning our journey and, as in case with any new project, we are eager to hear your feedback!
Please, contact us at [qodana-support@jetbrains.com](mailto:qodana-support@jetbrains.com) or via [our issue tracker](https://youtrack.jetbrains.com/newIssue?project=QD).