[//]: # (title: Frequently asked questions)

Here is the collection of questions that may let you understand %product% better.

## What can I read about %product?

You can study the [](about-qodana.md) section for better understanding of what %product% is.

## Can I use Qodana right away, or is customization required?

You can use various ways to run %product% as described on the [](Quick-start.xml) page. All of them require the 
minimum number of preparation steps.

## Are there any plans to support other technologies?

The list of technologies already supported by %product% is available on the [](linters.md) page.

All technologies supported by JetBrains IDEs are going to be eventually covered by %product%. You can create an issue on 
our tracker or vote for an existing one to let us know what technology we should focus on, for example:

* [Scala](https://youtrack.jetbrains.com/issue/QD-1031) 
* [Dart](https://youtrack.jetbrains.com/issue/QD-2226)
* [C/C++](https://youtrack.jetbrains.com/issue/QD-2153)
* [Code Coverage](https://youtrack.jetbrains.com/issue/QD-2122) support for a bunch of technologies

## How do I integrate Qodana with <CI/CD name>?

Any %product% linter is a Linux Docker image, so any CI/CD that supports Docker should be able to run it. 
We are working on [extending our documentation](ci.md) to provide the best examples on how to integrate it with 
different CI/CD platforms. If you experience any difficulties, feel free to contact our support at 
`qodana-support@jetbrains.com`.

## Can I import SARIF of another analysis tool to Qodana?

No. At this time, there is no opportunity to show the results of external analysis tools in Qodana UI, though we're working on it.

## What is a profile?

A %product% profile is a set of pre-configured inspections including their state, configuration options, and 
the path they are applied to. %product% inspection profiles are the same as IntelliJ IDEA inspection profiles and can be 
[reused](custom-xml-profiles.md).

## What inspection profiles does Qodana offer?

You can find the list of the default %product% inspection profiles on the [](inspection-profiles.md#Default+profiles) page.
On that page, you can also study how to set up the default profiles.

## How can I select the best profile for my project?

You can use either the [`qodana.recommended`](inspection-profiles.md#Default+profiles) profile, or 
[create](custom-profiles.md) your own profile that will best fit your goals.

## How can I customize the checks performed by Qodana?

You can configure your inspection profile as described on the [](custom-profiles.md) page.

## Qodana reports 0 errors, though I know it is not true.

Use the `qodana.recommended` inspection [profile](inspection-profiles.md#Default+profiles). 

If the problem persists, please create an issue in our tracker or contact us at `qodana-support@jetbrains.com` and 
attach logs from the `/data/results` directory that you can get access to by mounting your directory to the path.

## Is there a way to reduce analysis time?

Yes, you can use [caching](docker-image-configuration.xml#docker-config-reference-cache-dependencies), and this
is available by default in the [Qodana Scan](github.md) GitHub action.  If this does not help, create an issue in 
our tracker or contact us at `qodana-support@jetbrains.com` and attach logs from the `/data/results` directory that you 
can access them mounting your directory to the path or if you are using GitHub actions, they are uploaded to the 
workflow artifacts.

## How to make Qodana check formatting rules for Kotlin?

All you need to do is to add IncorrectFormatting inspection to `qodana.yaml`.

## Does Qodana support custom checks?

At the moment, you can add your [structural search inspections](extending-qodana-structural-search.xml) to the inspection 
profile or use [plugins](extending-qodana-plugins.xml) that will extend inspection capabilities of %product%. 

Alternatively, you can [develop your own plugin](https://plugins.jetbrains.com/docs/intellij/github-template.html) and 
use its inspections with %product%. 

## Qodana fails with the Out of Memory error.

Try to set more memory in Docker Desktop preferences, as some projects and build tools inside them like Gradle could 
require more memory than the default 2GB. 

## Qodana can't download Gradle because I use proxy.

Please run the `./gradlew` command in the root folder before starting %product%. The downloaded Gradle will be used by 
%product%.

If your project was created on Windows, be sure to run `git update-index --chmod=+x gradlew` to make the file executable 
in your CI.

## Why is there a need to set up SSH keys in my repository?

The SSH key lets %product% identify the repository of the inspected project and calculate the number of contributors, 
which is a requirement for the Ultimate and Ultimate Plus [license](pricing.md) use. If you plan to run %product%
under the Community license, you do not need to set up SSH keys.  

## Is there an option for a self-hosted or on-premises version of Qodana?

You can run %product% under the Community license, which will not require from you to create a Qodana Cloud account.

## Do I really need Qodana Cloud if I want to use Qodana?

You do not need to use Qodana Cloud if you plan to run %product% in your [IDE](qodana-ide-plugin.md), or in case
you need only the [Community license](pricing.md) features.

## How can I use multiple linters in one project?

You can use multiple linters as described in the [](monorepo-project.md) section.

## What does each %product% linter represent?

A linter is a %product% component representing a specific technology covered by it. For example, the 
[Qodana for JVM](qodana-jvm.md) linter lets you inspect the codebase containing the Java, Kotlin, and Groovy code, while
using the [Qodana for JS](qodana-js.md) linter you can check the JavaScript and TypeScript code. The detailed information
about all supported technologies is provided on the respective linter pages. 

## Where can I run %product%?

You can run %product% locally using either the [JetBrains IDEs](qodana-ide-plugin.md) or the [Docker images](docker-images.md), 
or you can inspect your code in [CI pipelines](ci.md). 

## What alternatives do I have if I prefer not to use Qodana Cloud?
