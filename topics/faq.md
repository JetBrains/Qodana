[//]: # (title: Frequently asked questions)

Here is the collection of questions that may let you understand %product% better.


## Supported technologies

<chapter id="faq-how-can-i-run" title="How can I run %product%?" initial-collapse-state="collapsed">

<p>You can run %product% in your <a href="ci.md">CI pipelines</a>. You can inspect your code locally using either the
<a href="qodana-ide-plugin.md">JetBrains IDEs</a> or available <a href="docker-images.md">Docker images</a>.</p>

</chapter>

<chapter id="faq-support-other-techs" title="Are there any plans to support other technologies?" initial-collapse-state="collapsed">

<p>The list of technologies already supported by %product% is available on the <a href="linters.md"/> page.</p>

<p>All technologies supported by JetBrains IDEs are going to be eventually covered by %product%. You can create an issue on
our tracker or vote for an existing one to let us know what technology we should focus on, for example:</p>

<list>
<li><a href="https://youtrack.jetbrains.com/issue/QD-1031">Scala</a></li>
<li><a href="https://youtrack.jetbrains.com/issue/QD-2226">Dart</a></li>
<li><a href="https://youtrack.jetbrains.com/issue/QD-2153">C/C++</a></li>
<li><a href="https://youtrack.jetbrains.com/issue/QD-2122">Code coverage</a></li>
</list>

</chapter>

## How can I integrate Qodana into <CI/CD name> pipelines?

Any %product% linter is a Linux Docker image, so any CI/CD that supports Docker should be able to run it.
We are working on [extending our documentation](ci.md) to provide the best examples on how to integrate it with
different CI/CD platforms. If you experience any difficulties, feel free to contact our support at
`qodana-support@jetbrains.com`.

## Does Qodana support custom checks?

At the moment, you can add your [structural search inspections](extending-qodana-structural-search.xml) to the inspection
profile or use [plugins](extending-qodana-plugins.xml) that will extend inspection capabilities of %product%.

Alternatively, you can [develop your own plugin](https://plugins.jetbrains.com/docs/intellij/github-template.html) and
use its inspections with %product%.

## Is there an option for a self-hosted or on-premises version of Qodana?

You can run %product% under the Community license, which will not require from you to create a Qodana Cloud account.


## Deployment and configuration

## Can I use Qodana right away, or is customization required?

You can use various ways to run %product% as described on the [](Quick-start.xml) page. All of them require the
minimum number of preparation steps.

## What does each %product% linter represent?

A linter is a %product% component representing a specific technology. For example, the
[Qodana for JVM](qodana-jvm.md) linter lets you inspect the codebase containing the Java, Kotlin, and Groovy code, while
using the [Qodana for JS](qodana-js.md) linter you can check the JavaScript and TypeScript code. On the [](linters.md)
page, you can find the list of all available linters and the links to the detailed description of each linter.

## Can I use multiple linters in one project?

You can use multiple linters as described in the [](monorepo-project.md) section.

## How can I customize the checks performed by Qodana?

You can configure your inspection profile as described on the [](custom-profiles.md) page.

## Why is there a need to set up SSH keys in my repository?

The SSH key lets %product% identify the repository of the inspected project and calculate the number of contributors,
which is a requirement for all types of [licenses](pricing.md).

## Do I really need Qodana Cloud if I want to use Qodana?

Using Qodana Cloud, you can get access to all [features](pricing.md#Features+and+third-party+software+support) provided
by %product% [linters](linters.md). You can also open %product% reports using your [IDE](qodana-ide-plugin.md), and you
need to use Qodana Cloud for this.


## Inspection profiles

## What is a profile?

A %product% profile is a set of pre-configured inspections including their state, configuration options, and
the path they are applied to. %product% inspection profiles are the same as IntelliJ IDEA inspection profiles and can be
[reused](custom-xml-profiles.md).

## What inspection profiles does Qodana offer?

You can find the list of the default %product% inspection profiles on the [](inspection-profiles.md#Default+profiles) page.
On that page, you can also study how to set up the default profiles.

## How can I select the best profile for my project?

You can use the [`qodana.recommended`](inspection-profiles.md#Default+profiles) profile because it already contains
the most usable inspections invoked by the default JetBrains IDEs profiles, so no additional configuration
is required.

Alternatively, you can [create](custom-profiles.md) your own profile that will best fit your goals.

## Can I import SARIF of another analysis tool to Qodana?

No, currently there is no opportunity to show the results of external analysis tools in Qodana UI, though we're working on it.




## Licensing

<!-- The licensing section needs to be pasted here -->

## I work solo on my project, can I still use Qodana?

Yes, but the minimum billing is set for 3 contributors.

## Is there a way to determine the number of contributors in my repositories prior to initiating Qodana?

Yes, you can use this command to check the number of contributors:

```shell
git log --format='%aN' | sort -u | wc -l
```


## Troubleshooting

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

## Qodana fails with the Out of Memory error.

Try to set more memory in Docker Desktop preferences, as some projects and build tools inside them like Gradle could
require more memory than the default 2GB.

## Qodana can't download Gradle because I use proxy.

Please run the `./gradlew` command in the root folder before starting %product%. The downloaded Gradle will be used by
%product%.

If your project was created on Windows, be sure to run `git update-index --chmod=+x gradlew` to make the file executable
in your CI.










