[//]: # (title: Qodana Community for JVM)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<img src="jvm.png" dark-src="jvm_dark.png" alt="JVM languages" width="296"/>

<var name="linter" value="Qodana Community for JVM"/>
<var name="ide" value="IntelliJ IDEA Community"/>
<var name="tech" value="jvm"/>
<var name="docker-image" value="jetbrains/qodana-jvm-community:2023.3"/>
<var name="config-file" value="qodana-jvm-community-docker-readme.topic"/>

%linter% is based on [%ide%](https://www.jetbrains.com/idea/).  <include from="lib_qd.topic" element-id="linter-intro"/>

## Supported technologies

%linter% provides inspections for the following technologies.

<table header-style="none">
    <tr>
        <td>Programming languages</td>
        <td>
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
            <p>XML</p>
            <p>XPath</p>
            <p>XSLT</p>
        </td>
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
            <p>JPA</p>
            <p>JUnit</p>
            <p>Lombok</p>
            <p>Reactive Streams</p>
            <p>TestNG</p>
        </td>
    </tr>
</table>

## Supported features

<include from="lib_qd.topic" element-id="linters-supported-features" use-filter="empty,community"/>

## Try it now

### Analyze a project locally

<note>Before running %instance%, you can <a href="configure-jdk.md">configure the JDK</a> for your project.</note>

<p><include from="lib_qd.topic" element-id="qodana-cli-quickstart" use-filter="non-php,jvm-only,jvm-php,non-gs,other,empty"/></p>

## Next steps

<include from="lib_qd.topic" element-id="linter-next-steps-footer" use-filter="empty"/>