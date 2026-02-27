# Starting the analysis

<show-structure for="chapter" depth="3"/>

## Analysis stages

To analyze projects, %product% performs the project configuration and project analysis stages.

The project configuration stage consists of the following steps:

* Project opening. During this step, %product% converts a project into an internal representation, identifies the project
  structure and configures various services like specific language support, file parsing, and VCS handling.
* Project configuration. During this step, %product% enumerates project files, pulls dependencies, creates indexes and
  performs language-specific configuration (e.g. identifies where to look for the Python SDK).

During the project analysis stage, %product% iterates through all enumerated files, filters them based on the scope,
matches inspections with files and executes these inspections.

## Analysis modes

%product% can analyze codebases using the [regular](#Regular+analysis) and [incremental](#Incremental+analysis) modes
described below.

### Regular analysis

Regular analysis is the default mode that reports all problems found in a codebase and includes all project files in the 
analysis scope except directories like `node_modules` or `build`. You can adjust the analysis scope by 
[configuring inspections](qodana-yaml.md#exclude-paths) using the `qodana.yaml` file. 

The advantages of the regular mode are as follows:

* It detects all problems across the whole codebase, including the problems produced by changes in other files
* It opens a project only once and can be more favourable for small projects from a performance point of view than incremental analyses
* It gives insights into code quality trends

The disadvantages of the regular mode are as follows:

* It can be time-consuming for large projects
* Analysis reports may contain problems that are not produced by current changes
* It requires a configured [baseline](baseline.topic) to eliminate the effect of false positives

### Incremental analysis

> You can learn how to run incremental analyses using the [](analyze-pr.md) section. 

Incremental analysis limits a regular analysis scope to the files changed between two commits, which are 
by default the merge-base and source branch head commit files. 

This mode reports only problems introduced by changes. 

To perform incremental analyses, %product% is executed twice: 

* The first analysis uses the merge-base commit
* The second analysis uses the source branch head commit

The report contains all problems found in the head commit that were not found in the merge base commit. 

The advantages of the incremental analyses are as follows:

* It provides faster analysis for mid-to-large codebases
* It reports only problems related to the developer’s changes, providing clear feedback

The disadvantages of the incremental analyses are as follows:

* It may ignore problems introduced by the changes in other files
* It may have inconsistent results when %product% configuration is changed between states

## Start analysis

To analyze your project using %product%, follow the steps listed below.

<procedure>
<step>Choose the %product% <a href="linters.md">linter</a> that you would like to use. </step>
<step>Decide which <a href="deploy-qodana.md">deployment method</a> of %product% you would like to use.</step>   
<step>Configure %product% as described in the <a href="configure-qodana.md"/> section.</step>
<step>If necessary, set up the list of commands that will be executed before %product%, see the <a href="qodana-yaml.md" anchor="Run+custom+commands"/> section for details.</step>
<step>In %cloud%, <a href="cloud-quickstart.md">set up an account</a> and obtain a <a href="project-token.md">project token</a>.</step> 
<step>Follow recommendations from a linter page that you would like to use (see Step 1 here).</step>
<step>If necessary, follow recommendations from the <a href="troubleshooting.topic"/> section.</step>
</procedure>

## Performance optimization

To improve performance during the project analysis stage, follow these recommendations:

* [Exclude files](qodana-yaml.md#exclude-paths) from analysis that are not required for the analysis
* Save in the VCS information about the excluded directories stored in `.*iml` files
* Use [incremental analysis](analyze-pr.md) to reduce the scope of files

## List of exit codes

<p>%product% provides the following exit codes:</p>

<table>
    <tr>
        <td>Exit code</td>
        <td>Description</td>
    </tr>
    <tr>
        <td><code>7</code></td>
        <td>The EAP license of a linter has expired. Please change the Docker tag either to the next EAP version like
            <code>20xx.x-eap</code> or to a stable version like <code>20xx.x</code>.</td>
    </tr>
    <tr>
        <td><code>137</code></td>
        <td>Qodana or Docker has crashed due to excessive memory usage. Please increase the amount of RAM available for Docker.</td>
    </tr>
    <tr>
        <td><code>255</code></td>
        <td>The number of problems detected by Qodana exceeds a <a href="quality-gate.topic">threshold</a> configured by a quality gate.</td>
    </tr>
</table>

## List of files for investigating Qodana behavior

<link-summary>There are several options for examining %instance% behavior using the /data/results directory.</link-summary>

<p>There are several options for examining %instance% behavior using the <code>/data/results</code> directory:</p>
<list>
    <li><p>The <code>/data/results/projectStructure</code> directory.</p>
        <p>The <code>Modules.json</code> file in this directory contains a list of all modules detected by
            %instance%. It should be identical to the list that you expect to see while opening your project in
            IntelliJ IDEA. If this is no longer the case, check <code>pom.xml</code> for Maven or the
            <code>build.gradle</code> file for Gradle configurations.</p>
        <p>The <code>SDKs.json</code> file in this directory contains the interpreter paths in case of Python.</p>
    </li>
    <li>In the <code>/data/results/</code> directory, each inspection that detected a possible problem creates
        its own file named <code>ID.json</code>, where <code>ID</code> is the inspection name that can be used in
        <code>qodana.yaml</code> for including or excluding inspections. You can find the complete list of
        inspection IDs in the <code>/data/results/.descriptions.json</code> file using the
        <code>/groups/*/inspections/*/shortName</code> pattern.</li>
    <li>In <code>/data/results/log/idea.log</code>, you can investigate suspicious warnings.</li>
</list>


## Frequently asked questions

<chapter id="faq-zero-errors-report" title="Qodana reports zero errors, but this doesn’t seem correct." default-state="collapsed" collapsible="true">
<p>Use the <code>qodana.recommended</code> inspection <a href="inspection-profiles.md" anchor="inspection-profiles-existing-profiles">profile</a>.</p>
    <p>If the <code>qodana.recommended</code> profile does not help, try to run another <a href="linters.md">linter</a>.</p>
<p>If the problem persists, please create an issue in our tracker or contact us at <code>qodana-support@jetbrains.com</code> and
attach logs from the <code>/data/results</code> directory that you can get access to by mounting your directory to the path.</p>
</chapter>

<chapter id="faq-reduce-analysis-time" title="Is there a way to reduce analysis time?" default-state="collapsed" collapsible="true">
    <p>
        Yes, you can use
        <a href="docker-image-configuration.topic" anchor="docker-config-reference-cache-dependencies">caching</a>,
        and this is available by default in the <a href="github.md">Qodana Scan</a> GitHub action. If this does
        not help, create an issue in our tracker or contact us at <code>qodana-support@jetbrains.com</code> and
        attach logs from the <code>/data/results</code> directory. To access logs, mount your directory. If you are
        using GitHub actions, they are uploaded to the workflow artifacts.
    </p>
</chapter>

<chapter id="faq-out-of-memory-error" title="Qodana fails with the Out of Memory error." default-state="collapsed" collapsible="true">
    <p>
        Try to set more memory in Docker Desktop preferences, as some projects and build tools inside them, like
        Gradle, could require more memory than the default 2 GB.
    </p>
</chapter>

<chapter id="faq-cannot-download-gradle" title="Qodana can't download Gradle because I use proxy." default-state="collapsed" collapsible="true">
    <p>
        Before starting %instance%, please run the <code>./gradlew</code> command in the root folder. This will let
        %instance% use this downloaded version of Gradle.
    </p>
    <p>
        If your project was created on Windows, make sure to run <code>git update-index --chmod=+x gradlew</code> to
        make the file executable in your CI.
    </p>
</chapter>

<chapter id="faq-sensitive-data-uploading" title="I have accidentally uploaded sensitive data to %cloud%, what should I do?" collapsible="true">
    <p>All your data is always encrypted at rest and in transit. If you remain concerned, you can delete the report containing sensitive
        data using the %cloud% UI.</p>
</chapter>

