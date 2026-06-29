[//]: # (title: Inspections)

<show-structure for="chapter" depth="3"/>

<var name="wiki-glob" value="https://en.wikipedia.org/wiki/Glob_(programming)"/>
<var name="idea-scopes" value="https://www.jetbrains.com/help/idea/scope-language-syntax-reference.html"/>


<link-summary>Each inspection is a set of conditions to analyze the code, detect and correct abnormal fragments in it. Qodana
    inspections can find and highlight various problems, locate dead code, find probable bugs, spelling problems,
    and thus facilitate improving the overall code structure.</link-summary>

Each inspection is a set of conditions to analyze the code, detect and correct abnormal fragments in it. Qodana
    inspections can find and highlight various problems, locate dead code, find probable bugs, spelling problems,
    and thus facilitate improving the overall code structure. 

All inspections are highly configurable, so you can configure:

* Which inspections to analyze your codebase with. You can also enable and disable inspections in %cloud%, on the [**Inspections**](ui-overview.md#ui-overview-configuration) tab.
* What directories and files to include in your code analysis. If you feel that you do not need to analyze
  any file or group of files, you can exclude them from code analysis.
* How you can configure and use [inspection profiles](#Inspection+profiles). You can use the preset combinations
  of inspections specified by inspection profiles aimed at solving specific tasks or create your custom profile
  that would meet your unique needs.

You can carry out all these configurations using a YAML-formatted file typically named `qodana.yaml`,
see the [](configure-qodana.md) section for details.

## Available inspections

You can explore available %product% inspections using the [Inspectopedia](https://www.jetbrains.com/help/inspectopedia/) website.
This website provides details about inspections: descriptions, severity levels, languages covered, etc.

Use the table of contents to explore all available inspections:

<img src="inspectopedia-toc.png" alt="Table of contents on the Inspectopedia website" width="296" border-effect="line"/>

Alternatively, you can search for particular inspections by their names, or identifiers:

<img src="inspectopedia-search.png" alt="Searching for an inspection" width="706" border-effect="line"/>

## Configure paths and inspections

Depending on your needs, save the following configurations to the `qodana.yaml` file.

### Exclude paths from the analysis scope
{id="exclude-paths"}

<link-summary>You can exclude files and paths from analysis.</link-summary>

You can exclude files and paths from analyses on a per-analysis basis and for all inspections at once.
Information about inspection IDs is available on the [Inspectopedia](https://www.jetbrains.com/help/inspectopedia/) website.

To exclude all paths in a project from the analysis scope, omit the `paths` node.

<note>While using the <code>qodana.recommended</code> and <code>qodana.starter</code> 
profiles, Qodana reads <code>.gitignore</code> files of your project and defines the files and folders to be ignored 
during the analysis.</note>

#### Examples
{id="exclude-example"}

<link-summary>You can exclude paths from analyses for all inspections, as well as for specific inspections. </link-summary>

Exclude all inspections for specified project paths:

```yaml
version: "1.0"

linter: <linter>

exclude:
  - name: All
    paths:
      - asm-test/src/main/java/org
      - asm/Visitor.java
      - benchmarks
```

Exclude inspections specified by ID for specified project paths:
{id="exclude-inspection"}

```yaml
version: "1.0"

linter: <linter>

exclude:
  - name: Annotator
  - name: AnotherInspectionId
    paths:
      - relative/path
      - another/relative/path
  - name: All
    paths:
      - asm-test/src/main/java/org
      - asm
      - benchmarks
      - tools
```

You can find specific inspection IDs in the Profile settings in the HTML report or in the `.xml` file with your inspection profile.

### Include an inspection in the analysis scope

<link-summary>You can tell %product% to analyze files of a certain directory using an inspection that is not contained in the selected profile.</link-summary>

You can tell %product% to analyze files of a certain directory using an inspection that is not contained in the selected profile.
This can be done on a per-analysis basis. To include all paths in a project into the inspection scope, omit the `paths` node.
Information about inspection IDs is available on the [Inspectopedia](https://www.jetbrains.com/help/inspectopedia/) website.

#### Example
{id="include-example"}

In this example, the `empty` profile, which contains no inspections, is specified, and the `SomeInspectionId` inspection
is explicitly included in the analysis scope for the `tools` directory. As a result, only the analysis performed by
the `SomeInspectionId` inspection the `tools` directory contents will be included in the %product% analysis scope.

```yaml
version: "1.0"

linter: <linter>

profile:
  name: empty
include:
  - name: SomeInspectionId
    paths:
    - tools
```

Here, each `include` entry should reference an inspection registered in an active
[inspection profile](inspection-profiles.md), either enabled or disabled. If an inspection ID is not registered, the
`ìnclude` entry becomes silently ignored and no inspection is added.

For example, the `profile.name: empty` configuration implies that plugin-provided inspections like `CppClangTidy*` are
not registered. To enable specific plugin inspections, you can start from an
[existing inspection profile](inspection-profiles.md#inspection-profiles-existing-profiles) like `qodana.starter`and use
`exclude` to suppress inspections that you do not need. Also, add inspections using plugin-specific config like
`.clang-tidy` in case of the [](clang.md) linter.

### Disable a specific inspection for a specific file

<link-summary>Learn how you can disable inspections for a specific file.</link-summary>

<p>To disable inspections for a specific file, in the project root save the
    <a href="qodana-yaml.md" anchor="exclude-paths"><code>qodana.yaml</code></a> file containing this configuration:</p>
<code-block lang="yaml">
<![CDATA[

    version: "1.0"

    linter: <linter>

    exclude:
      - name: <inspection-name>
    paths:
      - <path/to/the/file/from/project/root>
]]>
</code-block>
<p>You can also suppress the inspection only for a class by adding the <code>noinspection</code> comment above the class:</p>
<code-block lang="typescript">
    // noinspection &lt;inspection-name&gt;
    export class WorkflowJobSubject {
        private static subject: Observable&lt;GithubEvent&lt;WorkflowJobEvent&gt;&gt; | null =
            null;
    private static GithubWebhookEventSubject: any;
</code-block>

## Comprehensive configuration examples

<link-summary>Navigate to the section to see the combination of different configuration options.</link-summary>

```yaml
version: "1.0"

linter: <linter>

failThreshold: 0
profile:
  name: qodana.recommended
include:
  - name: SomeInspectionId
exclude:
  - name: Annotator
  - name: AnotherInspectionId
    paths:
      - relative/path
      - another/relative/path
  - name: All
    paths:
      - asm-test/src/main/java/org
      - benchmarks
      - tools
```

In the example above,
* `SomeInspectionId` inspection is explicitly enabled for all paths, although it is disabled in the profile
* `Annotator` inspection is disabled for all paths
* `AnotherInspectionId` inspection is disabled for `relative/path` and `another/relative/path`
* no inspections are conducted over these paths: `asm-test/src/main/java/org`, `benchmarks`, `tools`


The following example combines multiple settings, including a quality gate, inspection profile customization, and path exclusions,
which are common in .NET project setups:

```yaml
version: "1.0"

# Run the %dotnet% linter in native mode
linter: qodana-dotnet
withinDocker: false

# Set a quality gate: fail if the number of problems exceeds 10
failThreshold: 10

# Use the qodana.recommended profile
profile:
  name: qodana.recommended

# Exclude specific paths from the analysis
exclude:
  - name: All
    paths:
      - tests/
      - bin/
      - obj/

# Include an inspection not contained in the qodana.recommended profile
include:
  - name: SomeSpecificInspectionId
    paths:
      - src/

# Restore .NET dependencies
bootstrap: |+
  dotnet restore
```

Use this example while configuring the [%jvm%](jvm.md) linter:

```yaml
version: "1.0"

# Run the %jvm% linter
linter: qodana-jvm

# Set the JDK version
jdk:
  version: "17"

# Include Java projects for analysis
rootJavaProjects:
  - "./gradle-project"
  - "./maven-module/pom.xml"

# Quality gate settings
failureConditions:
  severityThresholds:
    any: 50       # Fail if total number of problems exceeds 50
    critical: 1   # Fail if there is at least 1 critical problem
    high: 2       # Fail if there are more than 2 high-severity problems
  testCoverageThresholds:
    fresh: 80     # Fail if fresh code coverage is below 80%
    total: 90     # Fail if total code coverage is below 90%

# Disable specific inspections
exclude:
  - name: CheckDependencyLicenses # Disable license audit if not needed

# Include custom plugins
plugins:
  - id: com.intellij.grazie.pro

```

## Inspection profiles

Inspection profiles let you combine and configure inspections that you would like %product% to use. The detailed description
of inspection profiles is available in the [](inspection-profiles.md) section.

