[//]: # (title: Inspection profiles)

<show-structure for="chapter" depth="3"/>

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

An inspection profile is a set of pre-configured [inspections](override-a-profile.md), including their state, configuration
options, scopes of their analyses, and [severities](ui-overview.md#Severity+levels).

%product% inspection profiles configure the inspections that you are going to use. If you enable too few inspections, you may
miss critical problems, which will affect your project overall. On the other hand, enabling too many inspections
can negatively affect inspection performance and can result in using inspections that are irrelevant to your project.

> %instance% inspection profiles are the same as IntelliJ IDEA inspection profiles.
{style="tip"}

This section explains how you can use 
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
        <td>The subset of the <code>qodana.recommended</code> profile, enabled by default</td>
    </tr>
    <tr>
        <td><code>qodana.recommended</code></td>
        <td><p>Provides the most usable inspections and implements default profiles of JetBrains IDEs like 
        <a href="https://www.jetbrains.com/help/idea/customizing-profiles.html">IntelliJ IDEA</a> with the following 
        exceptions:</p> 
        <list>
            <li>
                By default, Qodana provides analysis only for specific languages and frameworks. This means that, for 
                example, Groovy or JavaScript inspections are available but disabled by default. Inspections
                of the <code>INFORMATION</code> <a href="ui-overview.md" anchor="Severity+levels">severity</a> 
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
    once and then reuse it for running %product% with Docker, GitHub, JetBrains IDEs, or any other <a href="ci.md">software</a> currently
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
                      args: --profile-name qodana.recommended
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
scratch. 

This snippet demonstrates how you can fine-tune %instance% to fit your needs using the YAML format:

```yaml
version: "1.0"

profile:  
  base: 
    name: empty # Use the 'empty' profile as an initial configuration of this profile

  # name: "My custom profile" # Name of existing profile, overlaps with base.name
    
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

imports:
  - ".qodana/profiles/other-profile.yaml" # The imported file becomes part of this profile
```
{id="custom-profiles-profile-example-general"}

This snippet contains the following keys:

| Node name             | Description                                                  |
|-----------------------|--------------------------------------------------------------|
| [`profile`](#profile)        | The main node for profile configuration                      |
| [`imports`](#imports) | The list of relative paths to imported profiles              |


### profile

```yaml
profile:
  base: 
    name: empty

  # name: "My custom profile" # Name of existing profile, overlaps with base.name

  groups:
    - groupId: InspectionsToInclude
      groups:
        - "category:PHP/General" 

  inspections: 
    - group: InspectionsToInclude
      enabled: true
```

The `profile` key consists of the following elements:

| Section                             | Description                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| [`base`](#base)       | The profile that will serve as a basis for your profile configuration                              |
| [`name`](#name)                     | Name of the inspection profile, overlaps with `base.name`                                           |
| [`groups`](#groups)                 | Inspection groups that need to included or excluded in your profile                                |
| [`inspections`](#inspections-group) | List of changes applied for `base`. These changes could be applied to groups or single inspections |

#### base

<link-summary>This block lets you specify the profile that will serve as a basis for your profile configuration. </link-summary>

The `base` node lets you specify the profile that will serve as a basis for your profile configuration. 
You can use either a file path or a name: 

```yaml
base: # Use either path or name
  # path: .qodana/profiles/base-profile.yaml
  # name: qodana.starter
```

> The `base.name` key overlaps with the [`name`](#name) setting, so these keys cannot be used together.
{style="note"}

The `name` key supports the following values: 

| `base.name` values    | Description                                                                                                                                                                               |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Default`             | The [default profile](#custom-profiles-default-profile-tip) taken from the JetBrains IDE                                                                                                  |
| `Project Default`     | The profile is basically similar to `Default`, but contains user changes stored in the `.idea/inspectionProfiles/Project_Default.xml` file                                                |
| `Custom profile name` | Any name of an XML or YAML profile contained in the `.idea/inspectionProfiles` directory                                                                                                  |
| `qodana.starter`      | The [default](inspection-profiles.md#inspection-profiles-existing-profiles) %instance% profile, a subset of the `qodana.recommended` profile                                              |
| `qodana.recommended`  | The [default](inspection-profiles.md#inspection-profiles-existing-profiles) %instance% profile implementing the default profiles of JetBrains IDEs                                        |
| `empty`               | Severities and parameters of inspections are taken from `Project Default`, but none of the inspections are included. Using `empty`, you can you can build your profile [from scratch](#Create+profile) |

If the `name` declaration is missing, %instance% will employ the `Project Default` profile, so all settings applied in your custom
profile will override such settings contained in `Project Default`.

{id="custom-profiles-default-profile-tip"}

<tip>You can view the default IDE profile by navigating to <ui-path>Settings | Editor | Inspections</ui-path>.</tip>

#### name

<link-summary>Name of a profile which settings you would like to use as a base.</link-summary>

> The `name` key overlaps with the [`base.name`](#base) setting, so these keys cannot be used together.
{style="note"} 

Name of a profile from the `.idea/inspectionProfiles` directory which settings you would like to use as a base.

```yaml
name: "Name of your profile"
```

This key overlaps with the [`base.name`](#base) setting and cannot be used together with it.  


#### groups

<link-summary>This node contains a list of user-defined groups for combining inspection categories and single inspections.</link-summary>

The `groups` node is a list of user-defined groups. Here, you can combine inspection categories and
single inspections, and then configure their usage in the [`inspections`](#inspections-group) node.

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

This sample contains the following elements:

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

<link-summary>This node contains a list of user-defined groups for combining inspection categories and single inspections.</link-summary>

The list of group IDs with possible exclamation mark character (`!`):

```yaml
groups:
    - "ALL"
    - "category:Java/Probable bugs"
    - "IncludedInspections" 
    - "!ExcludedInspections"
    - "severity:WEAK WARNING"
```

Here, `groups` accepts several values:

| [`groupId`](#groups-groupid) value | Description                                                                                                                                                                                                                         |
|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ALL`                              | Include all inspections. Besides that, you can also use `LOCAL` to analyze your code using inspections available locally, or `GLOBAL` to analyze your code using the **Inspect code** action of the JetBrains IDE                   |
| `category:Java/Probable bugs`      | Name of the inspection category in the `category:categoryname` notation, matches the name from the **Editor &#124; Settings &#124; Inspections** section of the JetBrains IDE                                                       |
| `IncludedInspections`              | Name of the existing user-defined group, or a group from an included profile                                                                                                                                                        |
| `!ExcludedInspections`             | Negate the existing `ExcludedInspections` inspection group, either user-defined or included from another profile                                                                                                                    |
| `severity:WEAK WARNING`            | Include or exclude inspections by a certain [severity](#profile-severity-levels) level. Because the severity value is taken from the `Default` [profile](#base), %instance% is not aware of the changes made in your profile |

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

This sample contains several elements:

| Property     | Description                                                                                                                                      |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| `group`      | The ID of the group from the [`groupId`](#groups-groupid) property of an embedded or a user-defined group                                        |
| `inspection` | The ID of the inspection                                                                                                                         |
| `severity`   | Severity level that will be assigned to a group of inspections or a single inspection. For example, you can specify `WARNING` instead of `ERROR` |
| `ignore`     | List of paths using the [glob patterns](%wiki-glob%) and [scopes](%idea-scopes%) that will be ignored during inspection                          |
| `enabled`    | Specify whether the group or the inspection is enabled in the profile. Accepts either `true` or `false`                                          |
| `options`    | List of options that you can [configure for a specific inspection](#custom-profiles-examples-inspection-options)                                                                            |

### imports

Configure the list of imported profiles relative to the project root. This feature is useful when you need to merge 
specific profile configurations and then adjust the result to meet your requirements, As an example, see 
the [](global-configuration.md#Merging+configurations) section.

```yaml
imports:
    - ".qodana/profiles/firstprofile.yaml" 
    - ".qodana/profiles/anotherprofile.yaml"
```

The `imports` node is not related to [`base`](#base). If `base` contains no values, it is set to `Default`.

To view the default profile, in the JetBrains IDE navigate to **Settings | Editor | Inspections** and select the
`Default` profile in the **Profile** drop-down selector.

File contents are included in the order of appearance, thus becoming part of your profile. This means that the settings
of the included files are used prior to the settings specified in your custom profile.

#### Example of import

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
imports:
  - "foo.yaml"
  - "bar.yaml"

profile:
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

### Configuration examples

Here you can find several examples of profile configuration.

#### Exclude inspection

This lets you exclude the `PhpDeprecationInspection` inspection available in the [%php%](php.md) linter:

```yaml
profile:
  base: 
    name: qodana.starter
    
  inspections:
    - inspection: PhpDeprecationInspection
      enabled: false 
```

Alternatively, you can exclude the `PhpDeprecationInspection` inspection using `groups`:

```yaml
profile:
  base: 
    name: qodana.starter
  
  groups:
    - groupId: Inspection
      inspections:
        -  PhpDeprecationInspection # Specify the PhpDeprecationInspection inspection   
  
  inspections:  
    - group: Inspection 
      enabled: false # Disable the PhpDeprecationInspection inspection
```

#### Exclude paths

You can use the `ignore` key to ignore specific [scopes](%idea-scopes%) and paths while inspecting your code.

In the sample below, the `vendor/**` value employs [glob patterns](%wiki-glob%) for ignoring the contents
of the `vendor` directory contained in your project root.

The scope definition `scope#file:*.js:testData//*` ignores all files with the `.js` extension
recursively contained in the `testData/` directory.

```yaml
profile:
  inspections:
    - inspection: NpmUsedModulesInstalled
      ignore:
        - "vendor/**" # Ignore a path
    - group: "category:JavaScript and TypeScript/General"
      ignore:
        - "scope#file:*.js:testData//*" # Ignore a scope
```

#### Create profile

Using `base`, this configuration defines the empty profile, and then it includes only the `Java/Data flow`
inspection group from the [Qodana for JVM](jvm.md) linter.

```yaml
profile:
  base: 
    name: empty
                 
  inspections:  
    - group: "category:Java/Data flow"
      enabled: true # Enable the 'Java/Data flow' category
```

As an alternative to [`base`](#base), you can use `ALL` in the [`groups`](#groups-groups) property:

```yaml
profile:
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

#### Override profile

You can exclude inspection categories from the [`qodana.starter`](%qodana.starter%) profile
that are not related to the [Qodana for .NET](dotnet.md) linter.

```yaml
profile:
  base: 
    name: qodana.starter # Use the 'qodana.starter' profile
  
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

#### Filter by severity
{id="custom-profiles-filter-by-severity"}

This sample includes all inspections with the `WEAK WARNING` severity level while inspecting Java code:

```yaml
profile:
  groups:
    - groupId: IncludedInspections
      groups:
        - "category:Java"
        - "severity:WEAK WARNING"
              
  inspections:  
    - group: IncludedInspections
      enabled: true
```

#### Override severity

You can override the severity levels for existing inspections. Here’s how you can assign the `WARNING` severity level to
the `JavadocReference` inspection:

```yaml
profile:
  inspections:  
    - inspection: JavadocReference
      severity: WARNING
```

> If you override severity levels, it will affect all functionalities where severity is used, such as [filtering by
> severity](#custom-profiles-filter-by-severity) or [quality gate](quality-gate.topic) settings.
{style="note"}

#### Override options
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

> For several inspections, Inspectopedia provides a detailed description of available options. For example, see
> the [`RubyParameterNamingConvention`](%ruby-inspection%) inspection.

This sample demonstrates how you can configure the inspection options in your custom profile:

```yaml
profile:
  base: 
    name: qodana.recommended
  
  inspections:
    - inspection: JvmCoverageInspection
      options:
        classThreshold: 51
        methodThreshold: 51
        warnMissingCoverage: true
```

### Custom XML profiles

You can create XML-formatted inspection profiles using your IDE. For example, for IntelliJ IDEA this is explained
on the [Configure profiles](https://www.jetbrains.com/help/idea/customizing-profiles.html) page.  After you create a
profile, you can [export](https://www.jetbrains.com/help/idea/customizing-profiles.html#export-and-import-a-profile) it
to a file.

To run %instance% with the custom profile, you can follow the recommendations from the
[](inspection-profiles.md#inspection-profiles-setup-a-profile) section. In this case, the profile name does not necessarily
match the name of the containing file. The actual name is stored as the `%\profileName%` value in the profile file.

#### Specify SQL dialect

<p>To analyze SQL code, enabling SQL-related
    <a href="qodana-yaml.md" anchor="Include+an+inspection+in+the+analysis+scope">inspections</a> is not enough.
    In this case, you also have to specify an SQL dialect that you would like to analyze. To do this, in your
    project root save the <code>.idea/sqldialects.xml</code> containing the following contents:</p>
<code-block lang="xml">
    &lt;?xml version="1.0" encoding="UTF-8"?&gt;
    &lt;project version="4"&gt;
        &lt;component name="SqlDialectMappings"&gt;
            &lt;file url="PROJECT" dialect="&lt;SQLDialectName&gt;" /&gt;
        &lt;/component&gt;
    &lt;/project&gt;
</code-block>
<p>To find a name of a concrete SQL dialect for this snippet, in your IDE navigate to
    <ui-path>Settings | Languages & Frameworks | SQL Dialects | Project SQL Dialect</ui-path>. In the upper part
of the <ui-path>Settings</ui-path>, expand either the <ui-path>Global SQL Dialect</ui-path> or
    <ui-path>Project SQL Dialect</ui-path> dropdown list.</p>


### Use your profile

<p>A YAML configuration serves as a universal %product% configuration method. This means that you can configure %product% using the <a href="qodana-yaml.md"><code>qodana.yaml</code></a> file
    once and then reuse it for running %product% with Docker, GitHub, JetBrains IDEs, or any other <a href="ci.md">software</a> currently
    supported by %product%. In this case, no additional configuration is required, and all settings will remain consistent 
    across all these platforms, see the example below:</p>

<code-block lang="yaml">
version: "1.0"
&nbsp;
profile:
&nbsp;&nbsp;base:
&nbsp;&nbsp;&nbsp;&nbsp;path: .qodana/profiles/&lt;custom-profile.yaml&gt;
</code-block>

The following examples show how you can invoke your custom profiles using the 
[`--profile-path`](docker-image-configuration.topic#docker-config-reference-qodana-scan-linter-profile-path) option:

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
                          args: --profile-path .qodana/profiles/&lt;custom-profile.yaml&gt;
                        env:
                          QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
            </code-block>
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
