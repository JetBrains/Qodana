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

<chapter id="faq-integrate-cicd" title="How can I integrate Qodana into <CI/CD name> pipelines?" initial-collapse-state="collapsed">

<p>Any %product% linter is a Linux Docker image, so any CI/CD that supports Docker should be able to run it.
We are working on <a href="ci.md">extending our documentation</a> to provide the best examples on how to integrate it with
different CI/CD platforms. If you experience any difficulties, feel free to contact our support at
<code>qodana-support@jetbrains.com</code>.</p>

</chapter>

<chapter id="faq-integrate-custom-checks" title="Does Qodana support custom checks?" initial-collapse-state="collapsed">

<p>At the moment, you can add your <a href="extending-qodana-structural-search.xml">structural search inspections</a> to 
the inspection profile or use <a href="extending-qodana-plugins.xml">plugins</a> that will extend inspection 
capabilities of %product%.
</p>

<p>Alternatively, you can develop <a href="https://plugins.jetbrains.com/docs/intellij/github-template.html">your own plugin</a> and
use its inspections with %product%.
</p>

</chapter>

<chapter id="faq-self-hosted-on-premises" title="Is there an option for a self-hosted or on-premises version of Qodana?" initial-collapse-state="collapsed">

<p>You can run %product% under the Community license, which will not require from you to create a Qodana Cloud account.</p>

</chapter>

## Deployment and configuration

<chapter id="faq-customization-required" title="Can I use Qodana right away, or is customization required?" initial-collapse-state="collapsed">

<p>You can use various ways to run %product% as described on the <a href="Quick-start.xml"/> page. All of them require the
minimum number of preparation steps.
</p>

</chapter>

<chapter id="faq-linter-description" title="What does each %product% linter represent?" initial-collapse-state="collapsed">

<p>A linter is a %product% component representing a specific technology. For example, the
<a href="qodana-jvm.md"/> linter lets you inspect the codebase containing the Java, Kotlin, and Groovy code, while
using the <a href="qodana-js.md"/> linter you can check the JavaScript and TypeScript code. On the <a href="linters.md"/> 
page, you can find the list of all available linters and the links to the detailed description of each linter.
</p>

</chapter>

<chapter id="faq-multiple-linters" title="Can I use multiple linters in one project?" initial-collapse-state="collapsed">

<p>You can use multiple linters as described in the <a href="monorepo-project.md"/> section.</p>

</chapter>

<chapter id="faq-check-customization" title="How can I customize the checks performed by Qodana?" initial-collapse-state="collapsed">

<p>You can configure your inspection profile as described on the <a href="custom-profiles.md"/> page.</p>

</chapter>

<chapter id="faq-ssh-key-setup" title="Why is there a need to set up SSH keys in my repository?" initial-collapse-state="collapsed">

<p>The SSH key lets %product% identify the repository of the inspected project and calculate the number of contributors,
which is a requirement for all types of <a href="pricing.md">licenses</a>.
</p>

</chapter>

<chapter id="faq-qodana-cloud-use" title="Do I really need Qodana Cloud if I want to use Qodana?" initial-collapse-state="collapsed">

<p>Using Qodana Cloud, you can get access to all 
<a href="pricing.md" anchor="Features+and+third-party+software+support">features</a> provided
by %product% <a href="linters">linters</a>. You can also open %product% reports using your 
<a href="qodana-ide-plugin.md">IDE</a>, and you need Qodana Cloud for these purposes.</p>

</chapter>

## Inspection profiles

<chapter id="faq-profile-explained" title="What is a profile?" initial-collapse-state="collapsed">

<p>A %product% profile is a set of pre-configured inspections including their state, configuration options, and
the path they are applied to. %product% inspection profiles are the same as IntelliJ IDEA inspection profiles and they 
can be <a href="custom-xml-profiles.md">reused</a>.
</p>

</chapter>

<chapter id="faq-what-profiles-offered" title="What inspection profiles does Qodana offer?" initial-collapse-state="collapsed">

<p>You can find the list of the default %product% inspection profiles on the <a href="inspection-profiles.md" anchor="Default+profiles"/> page.
On that page, you can also study how to set up the default profiles.
</p>

</chapter>

<chapter id="faq-how-select-profile" title="How can I select the best profile for my project?" initial-collapse-state="collapsed">

<p>
You can use the <a href="inspection-profiles.md" anchor="Default+profiles"><code>qodana.recommended</code></a> profile 
because it already provides the most usable inspections invoked by the default JetBrains IDEs profiles, so no additional configuration
is required.
</p>

<p>Alternatively, you can <a href="custom-profiles.md">create</a> your own profile that will best fit your goals.
</p>

</chapter>

<chapter id="faq-sarif-import" title="Can I import SARIF of another analysis tool to Qodana?" initial-collapse-state="collapsed">

<p>No, currently there is no opportunity to show the results of external analysis tools in %product% UI, though we are working on it.</p>

</chapter>

## Licensing

<!-- The licensing section needs to be pasted here -->

<chapter id="faq-minimum-contributors" title="I work solo on my project, can I still use Qodana?" initial-collapse-state="collapsed">

<p>Yes, but the minimum billing is set for 3 (three) contributors.</p>

</chapter>

<chapter id="faq-count-contributors" title="Is there a way to determine the number of contributors in my repositories prior to initiating Qodana?" initial-collapse-state="collapsed">

<p>Yes, you can use this command to check the number of contributors:</p>

<code style="block" lang="shell" prompt="$">
git log --format='%aN' | sort -u | wc -l
</code>

</chapter>


## Troubleshooting

<chapter id="faq-zero-errors-report" title="Qodana reports zero errors, though I know it is not true." initial-collapse-state="collapsed">

<p>Use the <code>qodana.recommended</code> inspection <a href="inspection-profiles.md" anchor="Default+profiles">profile</a>.</p>

<p>
If the problem persists, please create an issue in our tracker or contact us at <code>qodana-support@jetbrains.com</code> and
attach logs from the <code>/data/results</code> directory that you can get access to by mounting your directory to the path.
</p>

</chapter>

<chapter id="faq-reduce-analysis-time" title="Is there a way to reduce analysis time?" initial-collapse-state="collapsed">

<p>
Yes, you can use <a href="docker-image-configuration.xml" anchor="docker-config-reference-cache-dependencies">caching</a>, and this
is available by default in the <a href="github.md">Qodana Scan</a> GitHub action.  If this does not help, create an issue in
our tracker or contact us at <code>qodana-support@jetbrains.com</code> and attach logs from the <code>/data/results</code> 
directory that you can access them mounting your directory to the path or if you are using GitHub actions, they are 
uploaded to the workflow artifacts.
</p>

</chapter>

<chapter id="faq-out-of-memory-error" title="Qodana fails with the Out of Memory error." initial-collapse-state="collapsed">

<p>Try to set more memory in Docker Desktop preferences, as some projects and build tools inside them like Gradle could
require more memory than the default 2GB.
</p>

</chapter>

<chapter id="faq-cannot-download-gradle" title="Qodana can't download Gradle because I use proxy." initial-collapse-state="collapsed">

<p>Please run the <code>./gradlew</code> command in the root folder before starting %product%. The downloaded Gradle 
will be used by %product%.
</p>

<p>If your project was created on Windows, be sure to run <code>git update-index --chmod=+x gradlew</code> to make the 
file executable in your CI.
</p>

</chapter>










