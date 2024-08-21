[//]: # (title: Java, Kotlin, and Groovy)

<show-structure for="chapter" depth="3"/>

<!--<img src="jvm.png" dark-src="jvm_dark.png" alt="JVM-based languages" width="296"/>-->

<!-- Linter-related variables -->
<var name="qp" value="Qodana for JVM"/>
<var name="qp-co" value="Qodana Community for JVM"/>
<var name="qp-a" value="Qodana Community for Android"/>
<var name="qp-an" value="Qodana for Android"/>
<var name="qp-linter" value="jetbrains/qodana-jvm:2024.2-eap"/>
<var name="qp-co-linter" value="jetbrains/qodana-jvm-community:2024.2-eap"/>
<var name="qp-a-linter" value="jetbrains/qodana-jvm-android:2024.2-eap"/>
<var name="qp-an-linter" value="jetbrains/qodana-android:2024.2-eap"/>
<var name="qd-image" value="jetbrains/qodana<-jvm><-community><-android>:2024.2-eap"/>
<var name="JenkinsCred" value="https://www.jenkins.io/doc/book/using/using-credentials/#adding-new-global-credentials"/>
<var name="ide" value="IntelliJ IDEA Ultimate"/>
<var name="ide-co" value="IntelliJ IDEA Community"/>
<var name="ide-a" value="IntelliJ IDEA"/>

<!-- Content-related variables -->
<var name="Dplugin" value="https://plugins.jenkins.io/docker-plugin/"/>
<var name="DPplugin" value="https://plugins.jenkins.io/docker-workflow/"/>
<var name="Gplugin" value="https://plugins.jenkins.io/git/"/>
<var name="Dockeraccess" value="https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user"/>
<var name="MultipipeCreate" value="https://www.jenkins.io/doc/book/pipeline/multibranch/#creating-a-multibranch-pipeline"/>
<var name="TeamCityProject" value="https://www.jetbrains.com/help/teamcity/configure-and-run-your-first-build.html#Create+your+first+project"/>
<var name="TeamCityBuildConfig" value="https://www.jetbrains.com/help/teamcity/creating-and-editing-build-configurations.html"/>
<var name="TeamCityBuildSteps" value="https://www.jetbrains.com/help/teamcity/configuring-build-steps.html"/>
<var name="TeamCityCommandLine" value="https://www.jetbrains.com/help/teamcity/command-line.html#General+Settings"/>
<var name="TeamCityPullRequests" value="https://www.jetbrains.com/help/teamcity/pull-requests.html"/>
<var name="TeamCityBranches" value="https://www.jetbrains.com/help/teamcity/configuring-finish-build-trigger.html#Trigger+Settings"/>
<var name="non-root-user" value="https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user"/>
<var name="ide-documentation" value="https://www.jetbrains.com/help/idea/customizing-profiles.html"/>
<var name="native-arg" value="&lt;linter-code&gt;"/>
<var name="teamcity-linter-list" value="Here, select either the %qp%, %qp-co%, %qp-a% or the %qp-an% linter."/>

<link-summary>You can analyze your Java code using the %qp% and %qp-co% linters.</link-summary>

All %product% linters are based on JetBrains IDEs designed for particular programming languages and frameworks. To analyze
Java projects, you can use the following linters:

* The %qp% and %qp-an% linters based on %ide% and licensed under the Ultimate and
  Ultimate Plus [licenses](pricing.md),
* The %qp-co% and %qp-a% linters based on %ide-co% and licensed under the Community license.

To see the list of supported technologies and features, you can navigate to the [](#jvm-feature-matrix) section.

## Before your start
{id="jvm-before-you-start"}

Before running %instance%, you may need to [configure the JDK](configure-jdk.md) for your project.

### Qodana Cloud

<include from="lib_qd.topic" element-id="before-start-qodana-cloud" use-filter="empty,jvm"/>

### Prepare your software

<include from="lib_qd.topic" element-id="before-start-prepare-software" use-filter="empty,jvm"/>

## Run %product%

<include from="lib_qd.topic" element-id="run-qodana" use-filter="empty,jvm"/>

## Explore analysis results

<include from="lib_qd.topic" element-id="explore-analysis-results" use-filter="empty,jvm"/>

## Extend %product% configuration

### Adjusting the scope of analysis

<include from="lib_qd.topic" element-id="adjust-scope-of-analysis"/>

### Enabling the baseline

<include from="lib_qd.topic" element-id="enabling-baseline" filter="empty,jvm"/>

### Enabling the quality gate

[Depending on the linter](quality-gate.topic), you can configure [quality gates](quality-gate.topic) for: 

* The total number of project problems, available for all linters,
* Multiple quality gates for <a href="faq.topic" anchor="faq-severities">problem severities</a>, available for all linters,
* <a href="code-coverage.md">Code coverage</a> thresholds, available for the %qp% and %qp-an% linters.

<tabs group="linter-tabs">
    <tab group-key="linter-tabs-ultimate" title="Qodana for JVM / Android">
        <p>You can configure <a href="quality-gate.topic">quality gates</a> for the total number of project problems, 
            specific problem severities and code coverage by saving this snippet to the 
            <a href="qodana-yaml.md"><code>qodana.yaml</code></a> file:
        </p>
        <code-block lang="yaml">
            failureConditions:
            &nbsp;&nbsp;severityThresholds:
            &nbsp;&nbsp;&nbsp;&nbsp;any: 50 # Total number of problems in all severities
            &nbsp;&nbsp;&nbsp;&nbsp;critical: 1 # Severities
            &nbsp;&nbsp;&nbsp;&nbsp;high: 2
            &nbsp;&nbsp;&nbsp;&nbsp;moderate: 3
            &nbsp;&nbsp;&nbsp;&nbsp;low: 4
            &nbsp;&nbsp;&nbsp;&nbsp;info: 5
            &nbsp;&nbsp;testCoverageThresholds:
            &nbsp;&nbsp;&nbsp;&nbsp;fresh: 6 # Fresh code coverage
            &nbsp;&nbsp;&nbsp;&nbsp;total: 7 # Total percentage
        </code-block>
    </tab>
    <tab group-key="linter-tabs-community" title="Qodana Community for JVM / Android">
        <p>You can configure <a href="quality-gate.topic">quality gates</a> for the total number of project problems 
            and specific problem severities by saving this snippet to the 
            <a href="qodana-yaml.md"><code>qodana.yaml</code></a> file:
        </p>
        <code-block lang="yaml">
            failureConditions:
            &nbsp;&nbsp;severityThresholds:
            &nbsp;&nbsp;&nbsp;&nbsp;any: 50 # Total number of problems in all severities
            &nbsp;&nbsp;&nbsp;&nbsp;critical: 1 # Severities
            &nbsp;&nbsp;&nbsp;&nbsp;high: 2
            &nbsp;&nbsp;&nbsp;&nbsp;moderate: 3
            &nbsp;&nbsp;&nbsp;&nbsp;low: 4
            &nbsp;&nbsp;&nbsp;&nbsp;info: 5
        </code-block> 
    </tab>
</tabs>

### Analyzing pull requests

<include from="lib_qd.topic" element-id="analyzing-pull-requests" use-filter="empty,jvm"/>

## Supported technologies and features
{id="jvm-feature-matrix"}

<!-- This list needs to be re-checked -->

<table>
    <tr>
      <td>Support for</td>
      <td>Name</td>
      <td>%qp% and %qp-an%</td>
      <td>%qp-co%</td>
      <td>%qp-a%</td>  
    </tr>
    <tr>
        <td>Programming languages</td>
        <td>
            <p>Java</p>
            <p>Kotlin</p>
            <p>Groovy</p>
        </td>
        <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
        </td>
        <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
        </td>
        <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
        </td>
    </tr>
    <tr>
        <td>Frameworks and libraries</td>
        <td>
            <p>JavaBeans</p>
            <p>JUnit</p>
            <p>Lombok</p>
            <p>TestNG</p>
            <p>JPA</p>
            <p>Reactive&nbsp;Streams</p>
            <p>JavaFX</p>
            <p>Java EE</p>
            <p>JAX-RS</p>
            <p>JSP</p>
            <p>Spring</p>
        </td>
        <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&nbsp;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
        </td>
        <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
        </td>
        <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&nbsp;</p>
            <p>&#x2714;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&#x2714;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
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
       <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
        </td>
        <td>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
        </td>
        <td>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
        </td>
    </tr>
    <tr>
        <td>Markup languages</td>
        <td>
            <p>CSS</p>
            <p>FreeMarker</p>
            <p>HTML</p>
            <p>JSON and JSON5</p>
            <p>RELAX NG</p>
            <p>XML</p>
            <p>XPath</p>
            <p>XSLT</p>
            <p>YAML</p>
            <p>TOML</p>
        </td>
        <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
        </td>
        <td>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
        </td>
        <td>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
        </td>
    </tr>
    <tr>
        <td>Scripting languages</td>
        <td>
            <p>Shell script</p>
            <p>Expression&nbsp;Language&nbsp;(EL)</p>
        </td>
       <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
        </td>
        <td>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
        </td>
       <td>
            <p>&#x2714;</p>
            <p>&nbsp;</p>
        </td>
    </tr>
    <tr>
        <td>Build management</td>
        <td>
            <p>Ant</p>
            <p>Gradle</p>
            <p>Maven</p>
        </td>
       <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
        </td>
       <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
        </td>
       <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
        </td>
    </tr>
    <tr>
      <td>%product% features</td>
      <td>
        <p><a href="baseline.topic">Baseline</a></p>
        <p><a href="quality-gate.topic">Quality gate</a></p>
        <p><a href="code-coverage.md">Code coverage</a></p>
        <p><a href="license-audit.topic">License audit</a></p>
        <p><a href="quick-fix.md">Quick-fix</a></p>
        <p><a href="vulnerability-checker.md">Vulnerability checker</a></p>
      </td>
      <td>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
            <p>&#x2714;</p>
      </td>
      <td>
         <p>&#x2714;</p>
         <p>&#x2714;</p>
         <p>&nbsp;</p>
         <p>&nbsp;</p>
         <p>&nbsp;</p>
         <p>&nbsp;</p>
      </td>
      <td>
         <p>&#x2714;</p>
         <p>&#x2714;</p>
         <p>&nbsp;</p>
         <p>&nbsp;</p>
         <p>&nbsp;</p>
         <p>&nbsp;</p>
      </td>
    </tr>
</table>
