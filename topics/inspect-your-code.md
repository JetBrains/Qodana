# Analyze your code

<show-structure for="chapter" depth="3"/>

## Analysis stages

To analyze projects, %product% performs the project configuration and project analysis stages.

The project configuration stage consists of the following steps:

* Project opening. During this step, %product% converts a project into an internal representation, identifies the project
  structure and configures various services like specific language support, file parsing, and VCS handling.
* Project configuration. During this step, %product% enumerates project files, pulls dependencies, creates indexes and
  performs language-specific configuration (e.g. identifies where to look for the Python SDK). More information about 
  performance is available in the [](configure-qodana.md#Performance+optimization) chapter.

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
<step>If necessary, set up the list of commands that will be executed before %product%, see the <a href="before-running-qodana.md"/> section for details.</step>
<step>In %cloud%, <a href="cloud-quickstart.md">set up an account</a> and obtain a <a href="project-token.md">project token</a>.</step> 
<step>Follow recommendations from a linter page that you would like to use (see Step 1 here).</step>
<step>If necessary, follow recommendations from the <a href="troubleshooting.topic"/> section.</step>
</procedure>

## Performance optimization

To improve performance during the project analysis stage, follow these recommendations:

* [Exclude files](qodana-yaml.md#exclude-paths) from analysis that are not required for the analysis
* Save in the VCS information about the excluded directories stored in `.*iml` files
* Use [incremental analysis](analyze-pr.md) to reduce the scope of files

