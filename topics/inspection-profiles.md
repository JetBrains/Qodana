[//]: # (title: Inspection profiles)

<show-structure for="chapter" depth="4"/>

<var name="code-inspection-profiles-ide-help-url" value="https://www.jetbrains.com/help/idea/?Customizing_Profiles"/>
<var name="ide" value="IDE"/>
<var name="qodana.recommended" value="https://github.com/JetBrains/qodana-profiles/blob/master/.idea/inspectionProfiles/qodana.recommended.yaml"/>
<var name="java-glob" value="https://docs.oracle.com/javase/8/docs/api/java/nio/file/FileSystem.html#getPathMatcher-java.lang.String-"/>
<var name="code-inspection-profiles-ide-help-url" value="https://www.jetbrains.com/help/idea/?Customizing_Profiles"/>
<var name="ide" value="IDE"/>
<var name="qodana.starter" value="https://github.com/JetBrains/qodana-profiles/blob/master/.idea/inspectionProfiles/qodana.starter.yaml"/>
<var name="qodana.recommended" value="https://github.com/JetBrains/qodana-profiles/blob/master/.idea/inspectionProfiles/qodana.recommended.yaml"/>
<var name="java-glob" value="https://docs.oracle.com/javase/8/docs/api/java/nio/file/FileSystem.html#getPathMatcher-java.lang.String-"/>
<var name="wiki-glob" value="https://en.wikipedia.org/wiki/Glob_(programming)"/>
<var name="idea-scopes" value="https://www.jetbrains.com/help/idea/scope-language-syntax-reference.html"/>
<var name="jvmcoverageinspection" value="https://www.jetbrains.com/help/inspectopedia/JvmCoverageInspection.html#inspection-options"/>
<var name="export-profile" value="https://www.jetbrains.com/help/idea/customizing-profiles.html#export-and-import-a-profile"/>
<var name="ruby-inspection" value="https://www.jetbrains.com/help/inspectopedia/RubyParameterNamingConvention.html#inspection-options"/>

<link-summary>Inspection profiles configure inspections, file scopes that these inspections analyze, 
and severities.</link-summary>

Inspection profiles define [inspections](code-inspections.topic), file scopes that these inspections analyze, and 
inspection [severities](troubleshooting.topic#troubleshooting-severities). This section explains how you can use 
existing %product% profiles, create your own profiles, and set up profiles for analyzing your projects using %product%.

## Existing %product% profiles
{id="inspection-profiles-existing-profiles"}

<link-summary>Out of the box, Qodana provides the qodana.starter, qodana.recommended, and qodana.sanity profiles.</link-summary>

Out of the box, you can use the following %product% profiles: 

<table>
    <tr>
        <td>Profile name</td>
        <td>Description</td>
    </tr>
    <tr>
        <td><code>qodana.starter</code></td>
        <td>The subset of the <code>qodana.recommended</code> profile, enabled in %product% by default</td>
    </tr>
    <tr>
        <td><code>qodana.recommended</code></td>
        <td><p>Implements default profiles of JetBrains IDEs like 
        <a href="https://www.jetbrains.com/help/idea/customizing-profiles.html">IntelliJ IDEA</a> with the following 
        exceptions:</p> 
        <list>
            <li>
                By default, Qodana provides analysis only for specific languages and frameworks. This means that, for 
                example, Groovy or JavaScript inspections are available but disabled by default. Inspections
                of the <code>INFORMATION</code> <a href="troubleshooting.topic" anchor="troubleshooting-severities">severity</a> 
                in the IDE are also disabled.</li>
            <li>
                Several inspections that affect code highlighting in IDEs and global inspections were removed from %product% linters.  
            </li>
            <li>
                Flaky inspections that are still available in IDEs were removed from %product% linters.
            </li>
        </list>
        </td>
    </tr>
    <tr>
        <td><code>qodana.sanity</code></td>
        <td><p>This profile is enabled by default to analyze whether a project is configured properly. If 
        <code>qodana.sanity</code> inspections detect problems, this means that all other %product% inspections may work 
        improperly and the project should be reconfigured.</p> 
        <p>To learn how disable inspections of this profile, see the <a href="qodana-yaml.md" anchor="Disable+sanity+checks"/> and 
            <a href="docker-image-configuration.topic" anchor="docker-config-reference-profile"/> sections.</p>
        </td>
    </tr>
</table>

These profiles are hosted on 
[GitHub](https://github.com/JetBrains/qodana-profiles/tree/master/.idea/inspectionProfiles), so you can learn them in detail.

### Set up an existing profile
{id="inspection-profiles-setup-a-profile"}

<link-summary>Learn how to set up existing %product% profiles.</link-summary>

<note>You can disable the <code>qodana.sanity</code> profile using recommendations from the 
<a href="qodana-yaml.md" anchor="Disable+sanity+checks"/> and 
<a href="docker-image-configuration.topic" anchor="docker-config-reference-profile"/> sections.</note>

<p>A YAML configuration serves as a universal %product% configuration method. This means that you can configure %product% using the <a href="qodana-yaml.md"><code>qodana.yaml</code></a> file
    once and then reuse it for running %product% with Docker, GitHub, JetBrains IDEs or any other <a href="ci.md">software</a> currently
    supported by %product%. The settings will remain consistent across all these platforms.</p>

<tabs>
    <tab id="inspection-profiles-yaml-file" title="YAML configuration">
        <p>To set up the <code>qodana.recommended</code> profile, in the project root save the <code>qodana.yaml</code> file 
        containing the following configuration:</p>
            <code-block lang="yaml">
            version: "1.0"
            &nbsp;
            profile:
            &nbsp;&nbsp;&nbsp;&nbsp;name: qodana.recommended
            </code-block>
    </tab>
    <tab id="inspection-profiles-ide" title="JetBrains IDE">
    <procedure>
        <step>
           <p>In your IDE, navigate to <ui-path>Tools | Qodana | Try Code Analysis with Qodana</ui-path>.</p> 
        </step>
        <step>
           <p>On the <code>profile</code> section of the <ui-path>Run Qodana</ui-path> dialog, paste the profile configuration:</p>
                    <code-block lang="yaml">
                        profile:
                        &nbsp;&nbsp;name: qodana.recommended
                    </code-block>
        <img src="inspection-profiles-ide-default-profile.png" width="793" alt="Configuring a Qodana profile" border-effect="line"/>
        </step>
        <step><p>On the <ui-path>Run Qodana</ui-path> dialog, check the <ui-path>Save qodana.yaml in project root</ui-path> option.</p>
           <img src="inspection-profiles-ide-save-file.png" width="793" alt="Saving qodana.yaml to a project root" border-effect="line"/>
        </step>
        <step>
            <p>Click <ui-path>Run</ui-path> to start analyzing your code.</p>
        </step>
        </procedure>
    </tab>
    <tab id="inspection-profiles-github" title="GitHub Actions">
    <note>Running %product% using GitHub Actions requires a <a href="project-token.md">project token</a>.</note>

<procedure>
    <step>On the <ui-path>Settings</ui-path> tab of the GitHub UI, create the <code>QODANA_TOKEN</code>
        <a href="https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository">encrypted secret</a>
        and save the <a href="cloud-projects.topic" anchor="cloud-manage-projects">project token</a> as its value.
    </step>
    <step>On the <ui-path>Actions</ui-path> tab of the GitHub UI, set up a new workflow and create the
        <code>.github/workflows/code_quality.yml</code> file.</step>
    <step><p>To analyze the <code>main</code> branch, release branches and the pull requests coming
    to your repository, save the workflow configuration to the <code>.github/workflows/code_quality.yml</code> file:</p>
        <code-block lang="yaml">
            name: Qodana
            on:
              workflow_dispatch:
              pull_request:
              push:
                branches: # Specify your branches here
                  - main # The 'main' branch
                  - 'releases/*' # The release branches
            jobs:
              qodana:
                runs-on: ubuntu-latest
                permissions:
                  contents: write
                  pull-requests: write
                  checks: write
                steps:
                  - uses: actions/checkout@v3
                    with:
                      ref: ${{ github.event.pull_request.head.sha }}  # to check out the actual pull request commit, not the merge commit
                      fetch-depth: 0  # a full history is required for pull request analysis
                  - name: 'Qodana Scan'
                    uses: %action-version%
                    with:
                      args: --profile-name,qodana.recommended
                    env:
                      QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
        </code-block>
            <p>Here, the <code>--profile-name</code> option specifies the <code>qodana.recommended</code> profile.</p>
    </step>
</procedure>
    </tab>
    <tab id="inspection-profiles-local-run" title="Command line">
<note>Running %product% using a command-line tool requires a <a href="project-token.md">project token</a>.</note>
<p>You can set up the <code>qodana.recommended</code> profile using the <code>--profile-name</code> option:</p>
<tabs group="cli-settings">
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$">
            docker run \
               -v $(pwd):/data/project/ \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               jetbrains/qodana-&lt;image&gt; \
               --profile-name qodana.recommended
        </code-block>
    </tab>
    <tab title="Qodana CLI" group-key="qodana-cli">
        <code-block lang="shell" prompt="$">
            qodana scan \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               --profile-name qodana.recommended
        </code-block>
    </tab>
</tabs>
</tab>
</tabs>

## Custom profiles
{id="inspection-profiles-custom-profiles"}

<link-summary>You can create custom profiles in YAML and XML formats, and then run %product% using them.</link-summary>

You can create custom profiles using the following formats:

* YAML is the preferred format
* [XML](#Custom+XML+profiles) can be used as an alternative to YAML

Custom profiles can either override [existing profiles](#inspection-profiles-existing-profiles) or be created from
scratch. For example, to use the existing `qodana.recommended` profile and additionally enable the
`Java/Java language level migration aids` inspection category, save this [YAML](inspection-profiles.md#inspection-profiles-custom-profiles) configuration in the profile file:

```yaml
version: "1.0"

profile:
    name: "Configuring Qodana" 
    baseProfile: qodana.recommended
    
    inspections:
       - group: "category:Java/Java language level migration aids" # Specify the inspection category
         enabled: true # Enable the inspection category
```

You can also store profile configurations in dedicated files and attach them using the [`imports`](#imports) block.
In this case, it is advised to save them in the `.qodana/profiles` directory of your project. If you run Qodana in a 
[CI/CD pipeline](ci.md) and store profile configurations in a separate file, make sure that such file resides in the 
working directory where the VCS stores your project before building it.

### Create your profile

This snippet demonstrates how you can fine-tune %instance% to fit your needs.

```yaml
version: "1.0"

profile:
  name: "My custom profile" # Profile name
  
  baseProfile: empty # Use the 'empty' profile as an initial configuration of this profile
  
  imports:
    - ".qodana/profiles/other-profile.yaml" # The included file becomes part of this profile
  
  groups: # List of configured groups
    - groupId: InspectionsToInclude
      groups:
        - "category:PHP/General" # Inspection category from the linter
        - "JSCategories" # Include the JSCategories group below
        - "PHPInspections" # Include the PHPInspections group below
    - groupId: JSCategories
      groups:
        - "category:JavaScript and TypeScript/ES2015 migration aids"
    - groupId: PHPInspections 
      inspections: #  Inspection IDs
        - PhpDeprecationInspection 
        - PhpReturnDocTypeMismatchInspection
        
  inspections: # Group invocation
    - group: InspectionsToInclude
      enabled: true # Enable the InspectionsToInclude group
    - inspection: PhpNonCompoundUseInspection
      severity: WARNING # Overriding the severity level for PhpNonCompoundUseInspection
    - inspection: MissortedModifiers
      options:
        m_requireAnnotationsFirst: false # Overriding the configuration option
```

This snippet consists of several nodes:

| Section                             | Description                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [`baseProfile`](#baseProfile)       | The profile that will serve as a basis for your profile configuration                                     |
| [`name`](#name)                     | Name of the inspection profile                                                                            |
| [`imports`](#imports)                     | Include an existing file-based profile into your profile                                                  |
| [`groups`](#groups)                 | Inspection groups that need to included or excluded in your profile                                       |
| [`inspections`](#inspections-group) | List of changes applied for `baseProfile`. These changes could be applied to groups or single inspections |

#### baseProfile

<link-summary>This block lets you specify the profile that will serve as a basis for your profile configuration. </link-summary>

The `baseProfile` block lets you specify the profile that will serve as a basis for your profile configuration. It
can accept the following values:

| `baseProfile` value   | Description                                                                                                                                                                               |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Default`             | The [default profile](#custom-profiles-default-profile-tip) taken from the JetBrains IDE                                                                                                  |
| `Project Default`     | The profile is basically similar to `Default`, but contains user changes stored in the `.idea/inspectionProfiles/Project_Default.xml` file                                                |
| `Custom profile name` | Any name of an XML or YAML profile contained in the `.idea/inspectionProfiles` directory                                                                                                  |
| `qodana.starter`      | The [default](inspection-profiles.md#inspection-profiles-existing-profiles) %instance% profile, a subset of the `qodana.recommended` profile                                              |
| `qodana.recommended`  | The [default](inspection-profiles.md#inspection-profiles-existing-profiles) %instance% profile implementing the default profiles of JetBrains IDEs                                        |
| `empty`               | Severities and parameters of inspections are taken from `Project Default`, but none of the inspections are included. Using `empty`, you can you can build your profile [from scratch](#Create+profile) |

If this parameter is missing, %instance% will employ the `Project Default` profile, so all settings applied in your custom
profile will override such settings contained in `Project Default`.

{id="custom-profiles-default-profile-tip"}

<tip>You can view the default IDE profile by navigating to <ui-path>Settings | Editor | Inspections</ui-path>.</tip>

#### name

Arbitrary name for your profile.

```yaml
name: "Name of your profile"
```

#### imports

Contains the list of relative paths to imported profiles.

```yaml
imports:
    - ".qodana/profiles/firstprofile.yaml" 
    - ".qodana/profiles/anotherprofile.yaml"
```

The `imports` block is not related to [`baseProfile`](#baseProfile). If `baseProfile` contains no values, it is set to `Default`.

To view the default profile, in the JetBrains IDE navigate to **Settings | Editor | Inspections** and select the
`Default` profile in the **Profile** drop-down selector.

File contents are included in the order of appearance, thus becoming part of your profile. This means that the settings
of the included files are used prior to the settings specified in your custom profile.

##### Example

Suppose, you have the `foo.yaml` and `bar.yaml` profiles.

The `foo.yaml` profile enables the `Inspection1`, `Inspection2` and `Inspection3` [inspections](#inspections-group):

```yaml
inspections:
  - inspection: Inspection1
    enabled: true
  - inspection: Inspection2
    enabled: true
  - inspection: Inspection3
    enabled: true
```

The `bar.yaml` profile disables the `Inspection1` inspection:

```yaml
inspections:
  - inspection: Inspection1
    enabled: false
```

You can include these two files in the custom profile and disable `Inspection2`:

```yaml
include:
  - "foo.yaml"
  - "bar.yaml"
inspections:
  - inspection: Inspection2
    enabled: false
```

In this case, the effective profile configuration read by %instance% will look like this:

```yaml
inspections:
  - inspection: Inspection1
    enabled: false # "bar.yaml" was included later than "foo.yaml"
  - inspection: Inspection2
    enabled: false # it was applied in the custom profile last
  - inspection: Inspection3
    enabled: true
```

#### groups

<link-summary>This block contains a list of user-defined groups for combining inspection categories and single inspections.</link-summary>

The `groups` block is a list of user-defined groups. Here, you can combine inspection categories and
single inspections, and then configure their usage in the [`inspections`](#inspections-group) block.

Each group definition can include or exclude other groups or single inspections.

You can use the exclamation mark character (`!`) to negate a group or a category. For example, you can exclude a
specific category usage in a group that will be included.

Here is the sample containing the `EnabledInspections` group defined by a user:

```yaml
groups:
  - groupId: EnabledInspections
    groups:
      - "category:Java/Probable bugs"
    inspections:
      - RedundantIf
```

This sample contains the following properties:

| Property                             | Description                                                                                                       |
|--------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| [`groupId`](#groups-groupid)         | ID of the group                                                                                                   |
| [`inspections`](#groups-inspections) | List of included and excluded inspections in this group                                                           |
| [`groups`](#groups-groups)           | List of included and excluded groups in this group |


##### groups.groupId
{id="groups-groupid"}

Unique group identifier.

```yaml
  - groupId: IncludedInspections
```

In case two groups are defined under the same `groupId`, the latest group met in the file will be employed. This rule
also works for all included files because the settings contained in the included files are considered prior to the settings
laid out in the current file.

##### groups.inspections
{id="groups-inspections"}

The list of inspections included in the group.

```yaml
inspections:
    - RedundantIf
    - UnnecessaryLocalVariable
```

##### groups.groups
{id="groups-groups"}

<link-summary>This block contains a list of user-defined groups for combining inspection categories and single inspections.</link-summary>

The list of group IDs with possible exclamation mark character (`!`):

```yaml
groups:
    - "ALL"
    - "category:Java/Probable bugs"
    - "IncludedInspections" 
    - "!ExcludedInspections"
    - "severity:WEAK WARNING"
```

Here, `groups` lists several values:

| [`groupId`](#groups-groupid) value | Description                                                                                                                                                                                                                         |
|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ALL`                              | Include all inspections. Besides that, you can also use `LOCAL` to analyze your code using inspections available locally, or `GLOBAL` to analyze your code using the **Inspect code** action of the JetBrains IDE                   |
| `category:Java/Probable bugs`      | Name of the inspection category in the `category:categoryname` notation, matches the name from the **Editor &#124; Settings &#124; Inspections** section of the JetBrains IDE                                                       |
| `IncludedInspections`              | Name of the existing user-defined group, or a group from an included profile                                                                                                                                                        |
| `!ExcludedInspections`             | Negate the existing `ExcludedInspections` inspection group, either user-defined or included from another profile                                                                                                                    |
| `severity:WEAK WARNING`            | Include or exclude inspections by a certain [severity](#profile-severity-levels) level. Because the severity value is taken from the `Default` [profile](#baseProfile), %instance% is not aware of the changes made in your profile |

{id="profile-severity-levels"}

By default, %instance% uses severity levels inherited from the JetBrains IDEs shown in this table:

<include from="lib_qd.topic" element-id="qodana-severity-levels" use-filter="for-profile,empty"/>

#### inspections
{id="inspections-group"}

<link-summary>This block configures inspection runs, paths and scopes, severities, and others.</link-summary>

Using `inspections`, you can:

* Enable or disable a specific group or an inspection,
* Define the order of applying these settings,
* Define the paths or scopes to be ignored by the specific group or the inspection,
* Customise severity for specific inspections or inspection groups,
* Configure inspection options.

```yaml
inspections:
  - group: InspectionGroup
  - inspection: JavadocReference
    severity: WARNING
  - group: ALL
    ignore:
      - "vendor/**" 
      - "scope#file[*test*]:src/*"
  - group: DisabledInspections
    enabled: false
  - inspection: MissortedModifiers
    options:
      m_requireAnnotationsFirst: false
```

This sample contains several properties:

| Property     | Description                                                                                                                                      |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| `group`      | The ID of the group from the [`groupId`](#groups-groupid) property of an embedded or a user-defined group                                        |
| `inspection` | The ID of the inspection                                                                                                                         |
| `severity`   | Severity level that will be assigned to a group of inspections or a single inspection. For example, you can specify `WARNING` instead of `ERROR` |
| `ignore`     | List of paths using the [glob patterns](%wiki-glob%) and [scopes](%idea-scopes%) that will be ignored during inspection                          |
| `enabled`    | Specify whether the group or the inspection is enabled in the profile. Accepts either `true` or `false`                                          |
| `options`    | List of options that you can [configure for a specific inspection](#custom-profiles-examples-inspection-options)                                                                            |

#### Examples

Here you can find several examples of profile configuration.

##### Exclude inspection

This lets you exclude the `PhpDeprecationInspection` inspection available in the [%php%](php.md) linter:

```yaml
name: "PHP/General without PhpDeprecationInspection"

baseProfile: qodana.starter
inspections:
  - inspection: PhpDeprecationInspection
    enabled: false 
```

Alternatively, you can exclude the `PhpDeprecationInspection` inspection using `groups`:

```yaml
name: "PHP/General without PhpDeprecationInspection"

baseProfile: qodana.starter

groups:
  - groupId: Inspection
    inspections:
      -  PhpDeprecationInspection # Specify the PhpDeprecationInspection inspection   

inspections:  
  - group: Inspection 
    enabled: false # Disable the PhpDeprecationInspection inspection
```

##### Exclude paths

You can use the `ignore` block to ignore specific [scopes](%idea-scopes%) and paths while inspecting your code.

In the sample below, the `vendor/**` value employs [glob patterns](%wiki-glob%) for ignoring the contents
of the `vendor` directory contained in your project root.

The scope definition `scope#file:*.js:testData//*` ignores all files with the `.js` extension
recursively contained in the `testData/` directory.

```yaml
name: "Ignoring paths"

inspections:
  - inspection: NpmUsedModulesInstalled
    ignore:
      - "vendor/**" # Ignore a path
  - group: "category:JavaScript and TypeScript/General"
    ignore:
      - "scope#file:*.js:testData//*" # Ignore a scope
```

##### Create profile

Using `baseProfile`, this configuration defines the empty profile, and then it includes only the `Java/Data flow`
inspection group from the [Qodana for JVM](jvm.md) linter.

```yaml
name: "Java/Data flow only"

baseProfile: empty
               
inspections:  
  - group: "category:Java/Data flow"
    enabled: true # Enable the 'Java/Data flow' category
```

As an alternative to [`baseProfile`](#baseProfile), you can use `ALL` in the [`groups`](#groups-groups) property:

```yaml
name: "Java/Data flow only"

groups:
  - groupId: ExcludedInspections
    groups:
      - "ALL"
  - groupId: IncludedInspections
    groups:
      - "category:Java/Data flow" # Specify the 'Java/Data flow' category
               
inspections:  
  - group: ExcludedInspections
    enabled: false # Disable all inspections    
  - group: IncludedInspections
    enabled: true # Enable the 'Java/Data flow' category
```

##### Override profile

You can exclude inspection categories from the [`qodana.starter`](%qodana.starter%) profile
that are not related to the [Qodana for .NET](dotnet.md) linter.

```yaml
name: "My custom profile"

baseProfile: qodana.starter # Use the 'qodana.starter' profile

groups:
  - groupId: ExcludedInspections
    groups:
      - "category:Java"
      - "category:Kotlin"
      - "category:JVM languages"
      - "category:Spring"
      - "category:CDI (Contexts and Dependency Injection)"
      - "category:Bean Validation"
      - "category:Reactive Streams"
      - "category:RegExp"
      - "category:PHP"
      - "category:Go"
      - "category:Python"
      - "category:General"
      - "category:TOML"
      
inspections:  
  - group: ExcludedInspections
    enabled: false
```

##### Filter by severity
{id="custom-profiles-filter-by-severity"}

This sample includes all inspections with the `WEAK WARNING` severity level while inspecting Java code:

```yaml
name: "My custom profile"

groups:
  - groupId: IncludedInspections
    groups:
      - "category:Java"
      - "severity:WEAK WARNING"
            
inspections:  
  - group: IncludedInspections
    enabled: true
```

##### Override severity

You can override the severity levels for existing inspections. Here’s how you can assign the `WARNING` severity level to
the `JavadocReference` inspection:

```yaml
name: "My custom profile"
            
inspections:  
  - inspection: JavadocReference
    severity: WARNING
```

> If you override severity levels, it will affect all functionalities where severity is used, such as [filtering by
> severity](#custom-profiles-filter-by-severity) or [quality gate](quality-gate.topic) settings.
{style="note"}

##### Override options
{id="custom-profiles-examples-inspection-options"}

Specific [inspections](https://jetbrains.com/help/inspectopedia) offer configurable options.
For example, the [`JvmCoverageInspection`](%jvmcoverageinspection%) inspection offers the `classThreshold`,
`methodThreshold`, and `warnMissingCoverage` options.

To discover this, configure this inspection in IntelliJ IDEA and then [export the profile](%export-profile%).
Here is a profile example for the `JvmCoverageInspection` inspection:

```xml
<component name="InspectionProjectProfileManager">
    <profile version="1.0">
        <option name="myName" value="Project Default" />
        <inspection_tool class="JvmCoverageInspection" enabled="true" level="WARNING" enabled_by_default="true">
            <option name="classThreshold" value="51" />
            <option name="methodThreshold" value="51" />
            <option name="warnMissingCoverage" value="true" />
        </inspection_tool>
    </profile>
</component>
```

> For several inspections, Inspectopedia provides the detailed description of available options. For example, see
> the [`RubyParameterNamingConvention`](%ruby-inspection%) inspection.

This sample demonstrates how to configure the inspection options in your custom profile:

```yaml
name: "My custom profile" # Profile name

baseProfile: qodana.recommended

inspections:
  - inspection: JvmCoverageInspection
    options:
      classThreshold: 51
      methodThreshold: 51
      warnMissingCoverage: true
```

#### Custom XML profiles

You can create XML-formatted inspection profiles using your IDE. For example, for IntelliJ IDEA this is explained
on the [Configure profiles](https://www.jetbrains.com/help/idea/customizing-profiles.html) page.  After you create a
profile, you can [export](https://www.jetbrains.com/help/idea/customizing-profiles.html#export-and-import-a-profile) it
to a file.

To run %instance% with the custom profile, you can follow the recommendations from the
[](inspection-profiles.md#inspection-profiles-setup-a-profile) section. In this case, the profile name does not necessarily
match the name of the containing file. The actual name is stored as the `%\profileName%` value in the profile file.

### Use your profile

<p>A YAML configuration serves as a universal %product% configuration method. This means that you can configure %product% using the <a href="qodana-yaml.md"><code>qodana.yaml</code></a> file
    once and then reuse it for running %product% with Docker, GitHub, JetBrains IDEs or any other <a href="ci.md">software</a> currently
    supported by %product%. The settings will remain consistent across all these platforms.</p>

<p>Depending on your needs, specify a profile configuration or path to a file containing the profile configuration:</p>
<code-block lang="yaml">
version: "1.0"
&nbsp;
profile:
# Direct profile configuration example
&nbsp;&nbsp;&nbsp;&nbsp;name: "Configuring Qodana"
&nbsp;&nbsp;&nbsp;&nbsp;baseProfile: qodana.recommended
# Invoke the profile file
&nbsp;&nbsp;&nbsp;&nbsp;path: .qodana/profiles/&lt;custom-profile.yaml&gt;
</code-block>

Alternatively, you can use a profile configuration stored in files as shown below.

<tabs>
    <!--<tab title="JetBrains IDE">
        <procedure>
        <step>
           <p>In your IDE, navigate to <ui-path>Tools | Qodana | Try Code Analysis with Qodana</ui-path>.</p> 
        </step>
        <step>
           <p>On the <code>profile</code> section of the <ui-path>Run Qodana</ui-path> dialog, paste the profile configuration.</p>
        </step>
        <step><p>On the <ui-path>Run Qodana</ui-path> dialog, check the <ui-path>Save qodana.yaml in project root</ui-path> option.</p>
           <img src="inspection-profiles-ide-save-file.png" width="793" alt="Saving qodana.yaml to a project root" border-effect="line"/>
        </step>
        <step>
            <p>Click <ui-path>Run</ui-path> to start analyzing your code.</p>
        </step>
        </procedure>
    </tab>-->
    <tab title="GitHub Actions">
        <note>Running %product% using GitHub Actions requires a <a href="project-token.md">project token</a>.</note>
    <procedure>
        <step>On the <ui-path>Settings</ui-path> tab of the GitHub UI, create the <code>QODANA_TOKEN</code>
            <a href="https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository">encrypted secret</a>
            and save the <a href="cloud-projects.topic" anchor="cloud-manage-projects">project token</a> as its value.
        </step>
        <step>On the <ui-path>Actions</ui-path> tab of the GitHub UI, set up a new workflow and create the
            <code>.github/workflows/code_quality.yml</code> file.</step>
        <step>To analyze the <code>main</code> branch, release branches and the pull requests coming
        to your repository, save the workflow configuration to the <code>.github/workflows/code_quality.yml</code> file:
            <code-block lang="yaml">
                name: Qodana
                on:
                  workflow_dispatch:
                  pull_request:
                  push:
                    branches: # Specify your branches here
                      - main # The 'main' branch
                      - 'releases/*' # The release branches
                jobs:
                  qodana:
                    runs-on: ubuntu-latest
                    permissions:
                      contents: write
                      pull-requests: write
                      checks: write
                    steps:
                      - uses: actions/checkout@v3
                        with:
                          ref: ${{ github.event.pull_request.head.sha }}  # to check out the actual pull request commit, not the merge commit
                          fetch-depth: 0  # a full history is required for pull request analysis
                      - name: 'Qodana Scan'
                        uses: %action-version%
                        with:
                          args: --profile-path,.qodana/profiles/&lt;custom-profile.yaml&gt;
                        env:
                          QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
            </code-block>
                <p>Here, the <code>--profile-path</code> option specifies the relative path to the file containing a custom profile.</p>
        </step>
    </procedure>
    </tab>
    <tab title="Command line">
<link-summary>You can configure profiles before running %product% locally.</link-summary>
<note>Running %product% using a command-line tool requires a <a href="project-token.md">project token</a>.</note>
<p>You can set up your custom profile using the <code>--profile-path</code> option:</p>
<tabs group="cli-settings" filter="for-inspection-profiles">
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$">
            docker run \
               -v $(pwd):/data/project/ \
               -v $(pwd)/.qodana/&lt;custom-profile.yaml&gt;:/data/project/myprofiles/&lt;custom-profile.yaml&gt; \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               jetbrains/qodana-&lt;image&gt; \
               --profile-path /data/project/myprofiles/&lt;custom-profile.yaml&gt;
        </code-block>
    </tab>
    <tab title="Qodana CLI" group-key="qodana-cli">
        <code-block lang="shell" prompt="$">
            qodana scan \
               -v .qodana/&lt;custom-profile.yaml&gt;:/data/project/myprofiles/&lt;custom-profile.yaml&gt; \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               --profile-path .qodana/&lt;custom-profile.yaml&gt;
        </code-block>
    </tab>
</tabs>
</tab>
</tabs>

## Order of resolving a profile

%instance% checks the configuration parameters for resolving the inspection profile in this order:

* Profile with the name `%\name%` from the command-line option `--profile-name %\name%`
* Profile by the path `%\path%` from the command-line option `--profile-path %\path%`
* Profile with the name `%\name%` from `qodana.yaml`
* Profile by the path `%\path%` from `qodana.yaml`
* Profile mounted to `/data/profile.xml`
* Fall back to using the default `qodana.recommended` profile.
