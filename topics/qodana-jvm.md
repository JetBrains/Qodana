[//]: # (title: Qodana for JVM)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<var name="linter" value="Qodana JVM"/>
<var name="ide" value="IntelliJ IDEA Ultimate"/>
<var name="tech" value="jvm"/>
<var name="docker-image" value="jetbrains/qodana-jvm:2021.3-eap"/>

%linter% is based on [%ide%](https://www.jetbrains.com/idea/) and provides static analysis for Java and Kotlin for Server Side projects, and related frameworks and technologies. <include src="lib_qd.xml" include-id="linter-intro"/>

## Try it now

### Analyze a project locally

<p><include src="lib_qd.xml" include-id="qodana-cli-quickstart" use-filter="jvm-only,jvm-php,non-gs,other,empty"/></p>

## Next steps

- <a href="qodana-jvm-docker-readme.xml">Configure %linter% Docker image</a>
- <a href="qodana-github-action.md">Run %linter% on GitHub</a>
- <a href="qodana-github-application.md">Run %linter% as a GitHub App</a>
- <a href="service.md">Use %linter% as a Service</a>
- <a href="ci.md">Extend your CI/CD with %linter% plugins</a>
