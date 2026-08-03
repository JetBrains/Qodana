[//]: # (title: Java, Kotlin, and Groovy)

<show-structure for="chapter" depth="3"/>

<!--<img src="jvm.png" dark-src="jvm_dark.png" alt="JVM-based languages" width="296"/>-->

<!-- Human-readable linter names -->
<var name="qd" value="%jvm%"/>
<var name="qd-co" value="%jvm-co%"/>
<var name="qd-a" value="%jvm-co-a%"/>
<var name="qd-an" value="%jvm-a%"/>
<!-- Docker images -->
<var name="qd-image" value="%jvm-image%"/>
<var name="qd-co-image" value="%jvm-co-image%"/>
<var name="qd-a-image" value="%jvm-co-a-image%"/>
<var name="qd-an-image" value="%jvm-a-image%"/>
<!-- Linter names -->
<var name="qd-linter" value="%jvm-linter%"/>
<var name="qd-co-linter" value="%jvm-co-linter%"/>
<var name="qd-a-linter" value="%jvm-co-a-linter%"/>
<var name="qd-an-linter" value="%jvm-a-linter%"/>

<var name="qd-image-combined" value="jetbrains/qodana-&lt;jvm|android&gt;&lt;-community|-android&gt;:%version-for-combined%"/>
<var name="qd-linter-combined" value="qodana-&lt;jvm|android&gt;&lt;-community|-android&gt;"/>
<var name="JenkinsCred" value="https://www.jenkins.io/doc/book/using/using-credentials/#adding-new-global-credentials"/>

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
<var name="teamcity-linter-list" value="Here, select either the %qd%, %qd-co%, or %qd-a% linter."/>
<var name="jbr-sdk" value="https://github.com/JetBrains/JetBrainsRuntime/tree/jbr25"/>

<!-- IDE-related variables -->
<var name="ide" value="IntelliJ IDEA Ultimate"/>
<var name="ide-co" value="IntelliJ IDEA Community Edition"/>
<var name="ide-a" value="IntelliJ IDEA"/>

<link-summary>You can analyze your Java code using the %qd%, %qd-co%, %qd-a%, and %qd-an% linters.</link-summary>

All %product% linters are based on JetBrains IDEs designed for particular programming languages and frameworks. To analyze
Java projects, you can use the following linters:

<tabs>
    <tab title="%qd%">
        <table>
            <tr>
                <td>Characteristic</td>
                <td>Description</td>
            </tr>
            <tr>
                <td>Linter name</td>
                <td><code>%qd-linter%</code></td>
            </tr>
            <tr>
                <td>Docker image</td>
                <td><code>%jvm-image%</code></td>
            </tr>
            <tr>
                <td>Based on</td>
                <td>%ide%</td>
            </tr>
            <tr>
                <td>Available under licenses</td>
                <td>Ultimate and Ultimate Plus <a href="pricing.md">licenses</a></td>
            </tr>
            <tr>
                <td>Shipped as</td>
                <td>A <a href="deploy-qodana.md" anchor="deploy-qodana-native-mode">native solution</a> and a Docker image</td>
            </tr>
            <tr>
                <td>Supported languages</td>
                <td>Java, Kotlin, Groovy, JavaScript, TypeScript</td>
            </tr>
        </table>
    </tab>
    <tab title="%qd-an%">
                <table>
            <tr>
                <td>Characteristic</td>
                <td>Description</td>
            </tr>
            <tr>
                <td>Linter name</td>
                <td><code>%qd-an-linter%</code></td>
            </tr>
            <tr>
                <td>Docker image</td>
                <td><code>%jvm-a-image%</code></td>
            </tr>
            <tr>
                <td>Based on</td>
                <td>%ide%</td>
            </tr>
            <tr>
                <td>Available under licenses</td>
                <td>Ultimate and Ultimate Plus <a href="pricing.md">licenses</a></td>
            </tr>
            <tr>
                <td>Shipped as</td>
                <td>A Docker image</td>
            </tr>
            <tr>
                <td>Supported languages</td>
                <td>Java, Kotlin, Groovy, JavaScript, TypeScript</td>
            </tr>
        </table>
    </tab>
    <tab title="%qd-co%">
        <table>
            <tr>
                <td>Characteristic</td>
                <td>Description</td>
            </tr>
            <tr>
                <td>Linter name</td>
                <td><code>%qd-co-linter%</code></td>
            </tr>
            <tr>
                <td>Docker image</td>
                <td><code>%jvm-co-image%</code></td>
            </tr>
            <tr>
                <td>Based on</td>
                <td>%ide-co%</td>
            </tr>
            <tr>
                <td>Available under licenses</td>
                <td>Community <a href="pricing.md">license</a></td>
            </tr>
            <tr>
                <td>Shipped as</td>
                <td>A <a href="deploy-qodana.md" anchor="deploy-qodana-native-mode">native solution</a> and a Docker image</td>
            </tr>
            <tr>
                <td>Supported languages</td>
                <td>Java, Kotlin, Groovy</td>
            </tr>
        </table>
    </tab>
    <tab title="%qd-a%">
        <table>
            <tr>
                <td>Characteristic</td>
                <td>Description</td>
            </tr>
            <tr>
                <td>Linter name</td>
                <td><code>%qd-a-linter%</code></td>
            </tr>
            <tr>
                <td>Docker image</td>
                <td><code>%jvm-co-a-image%</code></td>
            </tr>
            <tr>
                <td>Based on</td>
                <td>%ide-co%</td>
            </tr>
            <tr>
                <td>Available under licenses</td>
                <td>Community <a href="pricing.md">license</a></td>
            </tr>
            <tr>
                <td>Shipped as</td>
                <td>A Docker image</td>
            </tr>
            <tr>
                <td>Supported languages</td>
                <td>Java, Kotlin, Groovy</td>
            </tr>
        </table>
    </tab>
</tabs>

To see the list of supported technologies and features, you can navigate to the [](#jvm-feature-matrix) chapter of this section.

## Before you start
{id="jvm-before-you-start"}

### Qodana Cloud

<include from="lib_qd.topic" element-id="before-start-qodana-cloud" use-filter="empty,jvm"/>

### Preparing your software

<include from="lib_qd.topic" element-id="before-start-prepare-software" use-filter="empty,jvm"/>

### K2 Mode

The K2 mode is by default enabled for the %qd% and %qd-co% linters.

To revert the K2 mode, in your linter configuration set the `idea.kotlin.plugin.use.k2`
[property](docker-image-configuration.topic#docker-config-reference-properties) to `false`.

### Configuring the JDK

If your project uses Gradle, make sure that you have configured a JDK version for your project. 

#### Default versions

This table shows the JDK versions that are by default used by %instance%:

|---------|-----------|
|Linter | JDK version |
|%jvm%|[JBR SDK 25](%jbr-sdk%) |
|%jvm-co%|[JBR SDK 25](%jbr-sdk%) |
|%jvm-co-a%|[Amazon Corretto 11](https://docs.aws.amazon.com/corretto/latest/corretto-11-ug/what-is-corretto-11.html) |
|%jvm-a%|[Amazon Corretto 11](https://docs.aws.amazon.com/corretto/latest/corretto-11-ug/what-is-corretto-11.html)|

Using the default version of the JDK does not require any special configuration.

#### Available versions

<link-summary>List of available JDK versions.</link-summary>

<anchor name="configure-jdk-available-versions"/>

Apart from the versions available [by default](#Default+versions), %instance% can automatically download and use these versions of JBR SDK
for all JVM linters: 8, 11, 13, 15, 16, 17, 18, 19, 21.

Otherwise, you can download the required JDK version and [mount it](#Mount+JDK) to %instance%.

#### Configuring Qodana

<link-summary>List of available JDK versions.</link-summary>

<include from="lib_qd.topic" element-id="configure-jdk-qodana-yaml" use-filter="configure-jdk,empty"/>

If you specify here any JDK from the [list of available versions](#Available+versions), it will be automatically
downloaded by %instance%. If you would like to use the JDK beyond this list, you will have to download it and then
[mount it](#Mount+JDK) to %instance%.

#### Gradle

Gradle runs scripts based on the [Compatibility Matrix](https://docs.gradle.org/current/userguide/compatibility.html)
meaning that the latest supported and downloadable version of the JDK will be set up as the Gradle JDK. Using the
Compatibility Matrix in combination with the list of [available JDK versions](#Available+versions),
you can find the JDK that will be used by %instance%. For example, %instance% will
download and employ JDK 13 with Gradle 6.6.

#### Maven

<snippet id="jvm-maven">

In Maven, you can configure the [source and target](https://maven.apache.org/plugins/maven-compiler-plugin/examples/set-compiler-source-and-target.html) versions of the Java compiler. %instance% compares these values and selects the latest version. This version of the JDK is
then searched in the list of available versions. If found, %instance% will download and use it.
Otherwise, %instance% will download the subsequent version from this list.

You can specify the path to a custom Maven settings file, which lets you use custom repositories, 
mirrors, credentials, and local repository settings: 

<tabs>
<tab title="YAML configuration" lang="yaml">
<code-block lang="yaml"><![CDATA[
    version: "1.0"

    linter: <linter>

    mavenSettingsPath: /path/to/settings.xml
]]>
</code-block>

</tab>
    <tab title="Qodana CLI" lang="shell" prompt="$">
<code-block lang="shell" prompt="$"><![CDATA[
    qodana scan \
       -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
       --maven-settings-path /path/to/settings.xml
]]>
</code-block>
    </tab>
</tabs>

This setting lets %product% parse the path, resolve relative paths against the project root, expose it in the YAML schema, 
and apply the configured `settings.xml` file prior to Maven project import or reimport.
It also ensures the correct workflow order: Maven reimport (if requested) runs only after Maven settings are 
configured, which then updates module dependencies.

</snippet>

#### Mount JDK

<snippet id="jvm-mount-jdk">

<link-summary>You can mount JDK from your local filesystem to the /root/.jdks directory of the %instance% Docker image.</link-summary>

You can mount JDK from your local filesystem to the `/root/.jdks` directory of the %instance% Docker image:

```shell
$ docker run \
  -v /path/to/jdk:/root/.jdks/jdk \
  jetbrains/qodana-<linter>
```
{emphasize-lines="2"}

</snippet>

## Run Qodana

<include from="lib_qd.topic" element-id="run-qodana" use-filter="empty,jvm,native,non-ruby"/>

## Explore analysis reports

<include from="lib_qd.topic" element-id="explore-analysis-results" use-filter="empty,jvm"/>

## Extend Qodana configuration

### Adjusting the scope of analysis

<include from="lib_qd.topic" element-id="adjust-scope-of-analysis"/>

### Enabling the baseline feature

<include from="lib_qd.topic" element-id="enabling-baseline" use-filter="empty,jvm,native"/>

### Enabling the quality gate

[Depending on the linter](quality-gate.topic), you can configure [quality gates](quality-gate.topic) for: 

* The total number of project problems, available for all linters
* Multiple quality gates for <a href="ui-overview.md" anchor="Severity+levels">problem severities</a>, available for all linters
* <a href="code-coverage.md">Code coverage</a> thresholds, available for the %qd% and %qd-an% linters

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

<include from="lib_qd.topic" element-id="analyzing-pull-requests" use-filter="empty,jvm,native"/>

### Enabling PQC inspections

In your YAML configuration file (`qodana.yaml`), add the following configuration and specify the `PqcMinLevel` 
[inspection level](post-quantum-cryptography.md) from 1 to 5:

```yaml
version: "1.0"

profile:
  name: qodana.recommended
  inspections:
    - group: PqcMinLevel<number>
      enabled: true
```

## Supported technologies and features
{id="jvm-feature-matrix"}

<table>
    <tr>
      <td>Support for</td>
      <td>Name</td>
      <td>%qd% and %qd-an%</td>
      <td>%qd-co%</td>
      <td>%qd-a%</td>  
    </tr>
    <tr>
        <td>Programming languages</td>
        <td>
            <p>Java</p>
            <p>Kotlin</p>
            <p>Groovy</p>
            <p>JavaScript&nbsp;and&nbsp;TypeScript</p>
        </td>
        <td>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
        </td>
        <td>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
            <p>&nbsp;</p>
        </td>
        <td>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
            <p>&nbsp;</p>
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
            <p>Node.js</p>
            <p>React</p>
            <p>Ktor</p>
            <p>Vue</p>
            <p>Apache Velocity</p>
            <p>Android Room</p>
        </td>
        <td>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
            <p>&nbsp;</p>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
        </td>
        <td>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
        </td>
        <td>
            <p>✔ </p>
            <p>✔ </p>
            <p>&nbsp; </p>
            <p>✔ </p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>✔ </p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
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
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
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
            <p>Less</p>
            <p>SASS/SCSS</p>
            <p>PostCSS</p>
            <p>JSONPath</p>
        </td>
        <td>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
        </td>
        <td>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
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
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>✔ </p>
            <p>✔ </p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
        </td>
    </tr>
    <tr>
        <td>Scripting languages</td>
        <td>
            <p>Shell script</p>
            <p>Expression&nbsp;Language&nbsp;(EL)</p>
        </td>
       <td>
            <p>✔ </p>
            <p>✔ </p>
        </td>
        <td>
            <p>&nbsp;</p>
            <p>&nbsp;</p>
        </td>
       <td>
            <p>✔ </p>
            <p>&nbsp;</p>
        </td>
    </tr>
    <tr>
        <td>Build management</td>
        <td>
            <p>Gradle</p>
            <p>Maven</p>
        </td>
       <td>
            <p>✔ </p>
            <p>✔ </p>
        </td>
       <td>
            <p>✔ </p>
            <p>✔ </p>
        </td>
       <td>
            <p>✔ </p>
            <p>✔ </p>
        </td>
    </tr>
    <tr>
        <td>Other</td>
        <td>
            <p>Regular expressions</p>
            <p>Structural search</p>
            <p>HTTP Client</p>
        </td>
       <td>
            <p>✔ </p>
            <p>✔ </p>
            <p>✔ </p>
        </td>
       <td>
            <p>✔ </p>
            <p>✔ </p>
            <p>&nbsp;</p>
        </td>
       <td>
            <p>✔</p>
            <p>✔</p>
            <p>&nbsp;</p>
        </td>
    </tr>
    <tr>
      <td>%product% features</td>
      <td>
        <p><a href="baseline.topic"/></p>
        <p><a href="quality-gate.topic"/></p>
        <p><a href="code-coverage.md"/></p>
        <p><a href="flexinspect.md"/></p>
        <p><a href="insights.md"/><b>*</b></p>
        <p><a href="license-audit.topic"/><b>*</b></p>
        <p><a href="quick-fix.md"/></p>
        <p><a href="cloud-sso.md"/><b>*</b></p>
        <p><a href="vulnerability-checker.md"/><b>*</b></p>
        <p><a href="taint-analysis.md"/><b>**</b></p>
      </td>
      <td>
            <p>✔</p>
            <p>✔</p>
            <p>✔</p>
            <p>✔</p>
            <p>✔</p>
            <p>✔</p>
            <p>✔</p>
            <p>✔</p>
            <p>✔</p>
            <p>✔</p>
      </td>
      <td>
         <p>✔</p>
         <p>✔</p>
         <p>&nbsp;</p>
         <p>&nbsp;</p>
         <p>&nbsp;</p>
         <p>&nbsp;</p>
         <p>&nbsp;</p>
      </td>
      <td>
         <p>✔</p>
         <p>✔</p>
         <p>&nbsp;</p>
         <p>&nbsp;</p>
         <p>&nbsp;</p>
         <p>&nbsp;</p>
         <p>&nbsp;</p>
      </td>
    </tr>
</table>


\* Available only under the Ultimate Plus [license](pricing.md).

** Supported only by the %jvm% linter. Available only under the Ultimate Plus [license](pricing.md).

