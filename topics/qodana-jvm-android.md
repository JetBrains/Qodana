[//]: # (title: Qodana Community for Android)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<img src="jvm.png" dark-src="jvm_dark.png" alt="JVM languages" width="296"/>

<var name="linter" value="Qodana Community for Android"/>
<var name="ide" value="IntelliJ IDEA"/>
<var name="tech" value="jvm"/>
<var name="docker-image" value="jetbrains/qodana-jvm-android:2023.3-eap"/>
<var name="config-file" value="qodana-jvm-android-docker-readme.xml"/>

%linter% is based on [%ide%](https://www.jetbrains.com/idea/) with the [Android Support](https://plugins.jetbrains.com/plugin/1792-android-support) plugin and provides static analysis for Android projects. <include src="lib_qd.xml" include-id="linter-intro"/>

%linter% provides inspections for Java, Kotlin, and Groovy.

## Supported technologies

%linter% provides inspections for the following technologies.

<table header-style="none">
    <tr>
        <td>Programming languages</td>
        <td>
            <p>Android</p>
            <p>Java</p>
            <p>Kotlin</p>
            <p>Groovy</p>
        </td>
    </tr>
    <tr>
        <td>Markup languages</td>
        <td>
            <p>HTML</p>
            <p>JSON and JSON5</p>
            <p>RELAX NG</p>
            <p>TOML</p>
            <p>XML</p>
            <p>XPath</p>
            <p>XSLT</p>
            <p>YAML</p>
        </td>
    </tr>
    <tr>
        <td>Scripting languages</td>
        <td>Shell script</td>
    </tr>
    <tr>
        <td>Build management</td>
        <td>
            <p>Ant</p>
            <p>Gradle</p>
            <p>Maven</p>
        </td>
    </tr>
    <tr>
        <td>Frameworks and libraries</td>
        <td>
            <p>JavaBeans</p>
            <p>JavaFX</p>
            <p>JUnit</p>
            <p>Lombok</p>
            <p>TestNG</p>
        </td>
    </tr>
</table>

## Supported features

<include src="lib_qd.xml" include-id="linters-supported-features" use-filter="empty,community"/>

## Try it now

### Analyze a project locally

<note>Before running %product%, you can <a href="configure-jdk.md">configure the JDK</a> for your project.</note>

<p><include src="lib_qd.xml" include-id="qodana-cli-quickstart" use-filter="non-php,jvm-only,jvm-php,non-gs,other,empty"/></p>

## Next steps

<include src="lib_qd.xml" include-id="linter-next-steps-footer" use-filter="empty"/>