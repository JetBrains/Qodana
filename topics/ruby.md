# Ruby

<show-structure for="chapter" depth="3"/>

<!-- Human-readable linter names -->
<var name="qd" value="%ruby%"/>
<!-- Docker images -->
<var name="qd-image" value="%ruby-image%"/>
<!-- Linter names -->
<var name="qd-linter" value="%ruby-linter%"/>

<var name="JenkinsCred" value="https://www.jenkins.io/doc/book/using/using-credentials/#adding-new-global-credentials"/>
<var name="ide" value="RubyMine"/>

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
<var name="ide-documentation" value="https://www.jetbrains.com/help/go/customizing-profiles.html"/>
<var name="teamcity-linter-list" value="Here, select Custom and in the field below specify the %qd% linter."/>

<link-summary>%qd% is based on %ide% and provides static analysis for Ruby projects.</link-summary>

<note>
%qd% is currently in Early Access, which means that it may not be reliable, may not work as intended, and may contain errors.
Any use of the EAP product is at your own risk. Your feedback is very welcome in our 
<a href="https://youtrack.jetbrains.com/newIssue?project=QD">issue tracker</a> or at
<a href="mailto:qodana-support@jetbrains.com">qodana-support@jetbrains.com</a>.
</note>

All %product% linters are based on JetBrains IDEs designed for particular programming languages and frameworks. To analyze
Ruby projects, you can use the following linter:

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
        <td><code>%qd-image%&lt;-ruby3.X&gt;&lt;-privileged&gt;</code>*</td>
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
        <td>Ruby, JavaScript and TypeScript</td>
    </tr>
</table>

\* Here, the optional `-ruby3.X` tag lets you specify the Ruby language version, ranging from 3.1 to 3.4. If not specified, the default Ruby version will be 3.4.
The optional `-privileged` tag lets you run %product% in the privileged mode to execute commands that require root access. In this case,
%product% comes with a default `qodana` user that possesses root privileges and does not require a password.

To see the list of supported technologies and features, you can navigate to the [](#ruby-feature-matrix) chapter of this section.

## Before you start
{id="ruby-before-you-start"}

### Install project dependencies

For a basic Ruby project that has no external dependencies, no preliminary steps are required.

In case a project has external dependencies, you can set them up using the `bootstrap` key in the `qodana.yaml` file:

```yaml
bootstrap: | 
  sudo apt-get update && 
  sudo apt-get install -y <list of libraries> && 
  bundle install
```
The command will be automatically executed before the analysis to install dependencies using the `bundle install` command.

### %cloud%

<include from="lib_qd.topic" element-id="before-start-qodana-cloud" use-filter="empty,generic"/>

### Prepare your software

<include from="lib_qd.topic" element-id="before-start-prepare-software" use-filter="empty,generic"/>

## Run Qodana

<include from="lib_qd.topic" element-id="run-qodana" use-filter="empty,ruby"/>
<include from="lib_qd.topic" element-id="run-qodana-container-mode-config-examples" use-filter="empty,generic"/>

## Explore analysis reports

<include from="lib_qd.topic" element-id="explore-analysis-results-qodana-cloud" use-filter="empty,ruby"/>

## Extend Qodana configuration

### Adjusting the scope of analysis

<include from="lib_qd.topic" element-id="adjust-scope-of-analysis"/>

### Enabling the baseline feature

<include from="lib_qd.topic" element-id="enabling-baseline-config-examples" use-filter="empty,generic"/>

### Enabling the quality gate

<include from="lib_qd.topic" element-id="enabling-quality-gate"/>

### Analyzing pull requests

<include from="lib_qd.topic" element-id="analyzing-pull-requests-for-temp-non-native-mode" use-filter="empty,generic,golang"/>

## Supported technologies and features
{id="ruby-feature-matrix"}

%qd% provides inspections for the following technologies.

<table style="none">
    <tr>
        <td>Programming languages</td>
        <td>
            <p>Ruby</p>
            <p>JavaScript&nbsp;and&nbsp;TypeScript</p>
        </td>
    </tr>
    <tr>
        <td>Frameworks and libraries</td>
        <td>
            <p>Cucumber</p>
            <p>Node.js</p>
            <p>RBS</p>
            <p>React</p>
            <p>Ruby on Rails</p>
            <p>Sass/SCSS</p>
            <p>Vue</p>
            <p>YARD</p>
        </td>
    </tr>
    <tr>
        <td>Databases and ORM</td>
        <td>
            <p>MongoDB</p>
            <p>MySQL</p>
            <p>Oracle</p>
            <p>PostgreSQL</p>
            <p>SQL</p>
            <p>SQL Server</p>
        </td>
    </tr>
    <tr>
        <td>Markup languages</td>
        <td>
            <p>CSS</p>
            <p>HTML</p>
            <p>JSON and JSON5</p>
            <p>JSONPath</p>
            <p>Less</p>
            <p>PostCSS</p>
            <p>RELAX NG</p>
            <p>XML</p>
            <p>YAML</p>
        </td>
    </tr>
    <tr>
        <td>Scripting languages</td>
        <td>
            <p>Shell script</p>
        </td>
    </tr>
    <tr>
        <td>Other</td>
        <td>
            <p>HTTP Client</p>
            <p>Regular expressions</p>
            <p>Structural search</p>
        </td>
    </tr>
</table>

<include from="lib_qd.topic" element-id="linters-supported-features" use-filter="empty,ruby"/>