[//]: # (title: About Qodana)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

**Qodana** is a code quality monitoring platform that allows you to evaluate the integrity of code you own, contract, 
or purchase. It brings into your CI/CD pipelines all the smart features you love in the JetBrains IDEs as well as 
project-level checks like clone detection and license audit. 

Qodana provides you an overview of the project quality, lets you set quality targets, and track progress on them. You 
can quickly adjust the list of checks applied for the project and include or remove directories from the analysis.

<!-- The below lines were commented out because the video contains the outdated UI -->
<!-- Watch this video to get a quick Qodana overview.

<video href="dgIw64OdjdU"/> -->

## Basic components 

Qodana consists of these basic components:

* <a href="static-analysis.xml">Static analysis</a> mechanism of Qodana means automated analysis of your codebase. 
* <a href="supported-technologies.md">Linters</a> are the components that let you analyze your code, find duplicate 
functions and incompatible licenses.
* <a href="code-inspections.xml">Code inspections</a> are the linter components that immediately analyze your code for 
specific issues.

The diagram below shows how all these components are combined in Qodana.

<img src="concepts.png" dark-src="concepts_dark.png" width="706" alt="Qodana concepts"/> 

## Qodana workflow

The diagram below provides an overview to a typical Qodana use-case.  

<img src="workflow.png" dark-src="workflow_dark.png" width="706" alt="Qodana workflow"/>

This diagram describes several steps:

1. Set up Qodana using [available options](#Setting+up+Qodana).

2. Take all necessary configuration steps:

   * Configure an inspection profile as described in the [](qodana-yaml.md) section
   * Configure Docker images using the [](docker-image-configuration.xml) section
   * Explore integration options using the [](ci.md) section

3. <a href="inspect-your-code.xml">Inspect your codebase</a> using available linters and 
<a href="features.xml">features</a>. You can run Qodana either [locally or within a CI/CD pipeline](#Running+Qodana). 

    Inspection results are available in these forms:

   * <a href="qodana-sarif-output.md">JSON files</a> formatted according to the SARIF specification
   * <a href="ui-overview.md">Interactive HTML reports</a>

4. Based on the inspection results, you can improve your code using your IDE, and run %product% again to track the 
progress.  

## Setting up Qodana

<include src="lib_qd.xml" include-id="qodana-deployment-options"/>

## Running Qodana

You can run %product% [locally](quickstart.md) in a standalone mode using a PC or a server. Alternatively, inspecting 
your code within a [CI/CD pipeline](ci.md) means that your code will be inspected by %product% as part of a 
building and/or deployment process.

## Qodana playground

[Qodana Playground](https://qodana.teamcity.com/overview?mode=builds) is a sandbox environment that runs in TeamCity, 
cloud-based CI system developed by JetBrains. You can use it to see Qodana in action and try various options yourself.

To view an example GitHub pull request verified by the [](qodana-github-application.md), see the JetBrains
[GitHub repository](https://github.com/JetBrains/qodana-examples/pull/2/checks).

## Contact us

If you encounter a bug or would like to suggest a new feature,
use the <a href="https://youtrack.jetbrains.com/newIssue?project=QD">issue tracker</a> or email the support team at 
<a href="mailto:qodana-support@jetbrains.com">qodana-support@jetbrains.com</a>. 

To actively participate in the Qodana community, join [Qodana Slack](http://qodana.slack.com/).

## Next steps

- <a href="quickstart.md">Quick start guide</a>
- <a href="components.xml">Qodana components</a>
- <a href="CHANGELOG.md">Changelog</a>
- <a href="deploy-qodana.xml">Deployment section</a>