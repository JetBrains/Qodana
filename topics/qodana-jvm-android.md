[//]: # (title: Qodana Community for Android)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<var name="linter" value="Qodana Community for Android"/>
<var name="ide" value="IntelliJ IDEA"/>
<var name="tech" value="jvm"/>
<var name="docker-image" value="jetbrains/qodana-jvm-android:2022.2-eap"/>

%linter% is based on [%ide%](https://www.jetbrains.com/idea/) with the [Android Support](https://plugins.jetbrains.com/plugin/1792-android-support) plugin and provides static analysis for Android projects. <include src="lib_qd.xml" include-id="linter-intro"/>

## Try it now

### Analyze a project locally

<p><include src="lib_qd.xml" include-id="qodana-cli-quickstart" use-filter="jvm-only,jvm-php,non-gs,other,empty"/></p>

## Next steps

- <a href="qodana-jvm-android-docker-readme.xml">Configure %linter% Docker image</a>
- <a href="github.md">Run %linter% on GitHub</a>
- <a href="service.md">Use %linter% as a Service</a>
- <a href="ci.md">Extend your CI/CD with %linter% plugins</a>
