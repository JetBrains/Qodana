[//]: # (title: Qodana for JVM)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<img src="jvm.png" dark-src="jvm_dark.png" alt="Java, Kotlin, Groovy" width="296"/>

<var name="linter" value="Qodana for JVM"/>
<var name="ide" value="IntelliJ IDEA Ultimate"/>
<var name="tech" value="jvm"/>
<var name="docker-image" value="jetbrains/qodana-jvm:2024.1"/>
<var name="config-file" value="qodana-jvm-docker-readme.topic"/>

<link-summary>%linter% is based on %ide% and provides inspections for 
Java, Kotlin, and Groovy.</link-summary>

%linter% is based on [%ide%](https://www.jetbrains.com/idea/). <include from="lib_qd.topic" element-id="linter-intro"/>

%linter% provides inspections for Java, Kotlin, and Groovy.

<note>This linter requires the Qodana Cloud <a href="project-token.md">project token</a>.</note>

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
            <p>CSS</p>
            <p>FreeMarker Template Language</p>
            <p>HTML</p>
            <p>JSON and JSON5</p>
            <p>RELAX NG</p>
            <p>XML</p>
            <p>XPath</p>
            <p>XSLT</p>
            <p>YAML</p>
        </td>
    </tr>
    <tr>
        <td>Scripting languages</td>
        <td>
            <p>Expression Language (EL)</p>
            <p>Shell script</p>
        </td>
    </tr>
    <tr>
        <td>Databases and ORM</td>
        <td>
            <p>Hibernate ORM</p>
            <p>MongoDB</p>
            <p>Oracle</p>
            <p>MySQL</p>
            <p>PostgreSQL</p>
            <p>SQL</p>
            <p>SQL server</p>
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
            <p>Jakarta EE</p>
            <p>Java EE</p>
            <p>JavaBeans</p>
            <p>JAX-RS</p>
            <p>JPA</p>
            <p>JSP</p>
            <p>JUnit</p>
            <p>Lombok</p>
            <p>Reactive Streams</p>
            <p>Spring</p>
            <p>TestNG</p>
        </td>
    </tr>
</table>

## Supported features

<include from="lib_qd.topic" element-id="linters-supported-features" use-filter="empty,jvm"/>

## Try it now

### Analyze a project locally

<note>Before running %instance%, you can <a href="configure-jdk.md">configure the JDK</a> for your project.</note>

<include from="lib_qd.topic" element-id="root-and-non-root-users-info-bubble"></include>

<p><include from="lib_qd.topic" element-id="qodana-cli-quickstart" use-filter="non-php,jvm-only,jvm-php,non-gs,other,empty"/></p>

## Next steps

<include from="lib_qd.topic" element-id="linter-next-steps-footer" use-filter="empty"/>