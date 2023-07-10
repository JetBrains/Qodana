[//]: # (title: Qodana Community for JVM)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<img src="jvm.png" dark-src="jvm_dark.png" alt="JVM languages" width="296"/>

<var name="linter" value="Qodana Community for JVM"/>
<var name="ide" value="IntelliJ IDEA Community"/>
<var name="tech" value="jvm"/>
<var name="docker-image" value="jetbrains/qodana-jvm-community:2023.2"/>

%linter% is based on [%ide%](https://www.jetbrains.com/idea/).  <include src="lib_qd.xml" include-id="linter-intro"/>

%linter% provides inspections for Java, Kotlin, and Groovy.

## Try it now

### Analyze a project locally

<note>Before running %product%, you can <a href="configure-jdk.md">configure the JDK</a> for your project.</note>

<p><include src="lib_qd.xml" include-id="qodana-cli-quickstart" use-filter="non-php,jvm-only,jvm-php,non-gs,other,empty"/></p>

## Next steps

- <a href="qodana-jvm-community-docker-readme.xml">Configure %linter% Docker image</a>
- <a href="github.md">Run %linter% on GitHub</a>
- <a href="service.md">Use %linter% as a Service</a>
- <a href="ci.md">Extend your CI/CD with %linter% plugins</a>
