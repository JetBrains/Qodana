[//]: # (title: Qodana Community for Android)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<img src="jvm.png" dark-src="jvm_dark.png" alt="JVM languages" width="296"/>

<var name="linter" value="Qodana Community for Android"/>
<var name="ide" value="IntelliJ IDEA"/>
<var name="tech" value="jvm"/>
<var name="docker-image" value="jetbrains/qodana-jvm-android:2024.2"/>
<var name="config-file" value="qodana-jvm-android-docker-readme.topic"/>
<var name="android-developers-website" value="https://developer.android.com/build/releases/gradle-plugin#android_gradle_plugin_and_android_studio_compatibility"/>
<link-summary>%linter% is based on %ide% and provides static analysis for Android projects based on 
Java, Kotlin, and Groovy.</link-summary>


%linter% is based on [%ide%](https://www.jetbrains.com/idea/) with the [Android Support](https://plugins.jetbrains.com/plugin/1792-android-support) plugin and provides static analysis for Android projects. <include from="lib_qd.topic" element-id="linter-intro"/>

%linter% provides inspections for Java, Kotlin, and Groovy.

## Supported technologies

%linter% provides inspections for the following technologies.

<table style="none">
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

<include from="lib_qd.topic" element-id="linters-supported-features" use-filter="empty,community"/>

## Try it now

### Analyze a project locally

<note>Before running %instance%, you can <a href="configure-jdk.md">configure the JDK</a> for your project.</note>

<include from="lib_qd.topic" element-id="root-and-non-root-users-info-bubble"></include>

<p><include from="lib_qd.topic" element-id="qodana-cli-quickstart" use-filter="non-php,jvm-only,jvm-php,non-gs,other,empty"/></p>

## Android Gradle plugin compatibility

The compatibility table is available on the [Android Developers](%android-developers-website%) website.
However, %product% and Android Studio may differ. For example, %product% 2023.2 used version 2022.3 of Android Studio, 
so you need to choose the Android Gradle plugin version that will be suitable in this case.

## Next steps

<include from="lib_qd.topic" element-id="linter-next-steps-footer" use-filter="empty"/>