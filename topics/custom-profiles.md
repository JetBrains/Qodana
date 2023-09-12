[//]: # (title: Custom YAML profiles)

<var name="code-inspection-profiles-ide-help-url" value="https://www.jetbrains.com/help/idea/?Customizing_Profiles"/>
<var name="ide" value="IDE"/>
<var name="qodana.starter" value="https://github.com/JetBrains/qodana-profiles/blob/master/.idea/inspectionProfiles/qodana.starter.yaml"/>
<var name="qodana.recommended" value="https://github.com/JetBrains/qodana-profiles/blob/master/.idea/inspectionProfiles/qodana.recommended.yaml"/>
<var name="java-glob" value="https://docs.oracle.com/javase/8/docs/api/java/nio/file/FileSystem.html#getPathMatcher-java.lang.String-"/>
<var name="wiki-glob" value="https://en.wikipedia.org/wiki/Glob_(programming)"/>
<var name="idea-scopes" value="https://www.jetbrains.com/help/idea/scope-language-syntax-reference.html"/>

Starting from version 2023.2, you can create and configure %product% profiles using YAML. %product% also provides 
several improvements related to profile configuration, such as:

* Support for file paths and [scopes](%idea-scopes%)
* Support for inspection parameters
* Profile relationship, so profiles can be extended and included

This sample shows how you can fine-tune %product% for your needs.

```yaml
name: "My custom profile" # Profile name

baseProfile: empty # Use the 'empty' profile as initial configuration of this profile

include:
  - ".qodana/profiles/other-profile.yaml" # The included file becomes part of this profile

groups: # List of configured groups
  - groupId: InspectionsToInclude
    groups:
      - "category:PHP/General" # Inspection category from the linter
      - "JSCategories" # Include the JSCategories group from below
      - "PHPInspections" # Include the PHPInspections group from below
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

This sample consists of several nodes:

| Section                             | Description                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [`baseProfile`](#baseProfile)       | The profile that will serve as a basis for your profile configuration                                     |
| [`name`](#name)                     | Name of the inspection profile                                                                            |
| [`include`](#include)               | Include an existing file-based profile into your profile                                                  |
| [`groups`](#groups)                 | Inspection groups that need to included or excluded in your profile                                       |
| [`inspections`](#inspections-group) | List of changes applied for `baseProfile`. These changes could be applied to groups or single inspections |

## baseProfile

The `baseProfile` block lets you specify the profile that will serve as a basis for your profile configuration. It
can accept the following values: 

| `baseProfile` value   | Description                                                                                                                                                                                                           |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Default`             | The [default profile](#custom-profiles-default-profile-tip) taken from the JetBrains IDE                                                                                                                              |
| `Project Default`     | The profile is basically similar to `Default`, but contains user changes stored in the `.idea/inspectionProfiles/Project_Default.xml` file                                                                            |
| `Custom profile name` | Any name of an XML or YAML profile contained in the `.idea/inspectionProfiles` directory                                                                                                                              |
| `qodana.starter`      | The [default](inspection-profiles.md#Default+profiles) %product% profile, a subset of the `qodana.recommended` profile                                                                                                |
| `qodana.recommended`  | The [default](inspection-profiles.md#Default+profiles) %product% profile implementing the default profiles of JetBrains IDEs                                                                                          |
| `empty`               | Severities and parameters of inspections are taken from `Project Default`, but none of the inspections are included. Using `empty`, you can you can build your profile [from scratch](#Create+a+profile+from+scratch) |

If this parameter is missing, %product% will employ the `Project Default` profile, so all settings applied in your custom 
profile will override such settings contained in `Project Default`. 

{id="custom-profiles-default-profile-tip"}

<tip>You can overview the default IDE profile by navigating to <menupath>Settings | Editor | Inspections</menupath>.</tip>

## name

Arbitrary name for your profile.

```yaml
name: "Name of your profile"
```

## groups

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


### groups.groupId
{id="groups-groupid"}

Unique group identifier. 

```yaml
  - groupId: IncludedInspections
```

In case two groups are defined under the same `groupId`, the latest group met in the file will be employed. This rule 
also works for all included files because the settings contained in the included files are considered prior to the settings 
laid out in the current file.

### groups.inspections
{id="groups-inspections"}

The list of inspections included in the group.

```yaml
inspections:
    - RedundantIf
    - UnnecessaryLocalVariable
```

### groups.groups
{id="groups-groups"}

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

| [`groupId`](#groups-groupid) value | Description                                                                                                                                                                                                                        |
|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ALL`                              | Include all inspections. Besides that, you can also use `LOCAL` to inspect your code using inspections available locally, or `GLOBAL` to inspect your code using the **Inspect code** action of the JetBrains IDE                  |
| `category:Java/Probable bugs`      | Name of the inspection category in the `category:categoryname` notation, matches the name from the **Editor &#124; Settings &#124; Inspections** section of the JetBrains IDE                                                      |
| `IncludedInspections`              | Name of the existing user-defined group, or a group from an included profile                                                                                                                                                       |
| `!ExcludedInspections`             | Negate the existing `ExcludedInspections` inspection group, either user-defined or included from another profile                                                                                                                   |
| `severity:WEAK WARNING`            | Include or exclude inspections by a certain [severity](#profile-severity-levels) level. Because the severity value is taken from the `Default` [profile](#baseProfile), %product% is not aware of the changes made in your profile |

{id="profile-severity-levels"}

By default, %product% uses severity levels inherited from the JetBrains IDEs shown in this table:

| IDE severity   | [SARIF](qodana-sarif-output.md) severity | [Qodana report](html-report.md) severity |
|----------------|------------------------------------------|------------------------------------------|
| `ERROR`        | `ERROR`                                  | `Critical`                               |
| `WARNING`      | `WARNING`                                | `High`                                   |
| `WEAK WARNING` | `NOTE`                                   | `Moderate`                               |
| `TYPO`         | `NOTE`                                   | `Low`                                    |
| `INFORMATION`  | `NOTE`                                   | `Info`                                   |
| `OTHER`        | `NOTE`                                   | `Info`                                   |

## inspections
{id="inspections-group"}

Using `inspections`, you can:

* Enable or disable a specific group or an inspection
* Define the order of applying these settings
* Define the paths or scopes to be ignored by the specific group or the inspection
* Change severity levels of the specific group or the inspection
* Configure inspection options

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

## include

Contains the list of relative paths to included profiles.

```yaml
include:
    - "firstprofile.yaml" 
    - "relative/path/to/anotherprofile.yaml"
```

The `include` block is not related to [`baseProfile`](#baseProfile). If `baseProfile` contains no values, it is set to `Default`.

To overview the default profile, in the JetBrains IDE navigate to **Settings | Editor | Inspections** and select the 
`Default` profile in the **Profile** drop-down selector.

File contents are included in the order of appearance, thus becoming part of your profile. This means that the settings
of the included files are used prior to the settings specified in your custom profile.

### Example

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

In this case, the effective profile configuration read by %product% will look like this:

```yaml
inspections:
  - inspection: Inspection1
    enabled: false # "bar.yaml" was included later than "foo.yaml"
  - inspection: Inspection2
    enabled: false # it was applied in the custom profile last
  - inspection: Inspection3
    enabled: true
```

## Configuration examples

Here you can find several examples of profile configuration. The [](inspection-profiles.md#Set+up+a+profile) section
explains how to run your profile while inspecting code.

### Exclude an inspection

This sample shows how you can exclude the `PhpDeprecationInspection` inspection from the [Qodana for PHP](qodana-php.md) 
linter:

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

### Exclude paths

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

### Create a profile from scratch

Using `baseProfile`, this configuration defines the empty profile, and then it includes only the `Java/Data flow`
inspection group from the [Qodana for JVM](qodana-jvm.md) linter.

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

### Override the existing profile

You can exclude inspection categories from the [`qodana.starter`](%qodana.starter%) profile
that are not related to the [Qodana for .NET](qodana-dotnet.md) linter.

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

### Filter by severity

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

You can also apply severity level to a specific inspection:

```yaml
name: "My custom profile"
            
inspections:  
  - inspection: JavadocReference
    severity: WARNING
```

### Configure inspection options
{id="custom-profiles-examples-inspection-options"}

Several inspections provide configuration options. You can find the list of available options on
[GitHub](https://github.com/JetBrains/qodana-profiles/blob/master/.idea/inspectionProfiles/qodana.recommended.full.xml).

For example, in case of the `MissingOverrideAnnotation` inspection you can find the `ignoreObjectMethods` and
`ignoreAnonymousClassMethods` options:

```xml
<inspection_tool class="MissingOverrideAnnotation" enabled="true" level="INFORMATION" enabled_by_default="true">
    <option name="ignoreObjectMethods" value="true" />
    <option name="ignoreAnonymousClassMethods" value="false" />
</inspection_tool>
```

This is how you can override these options in your profile:

```yaml
name: "My custom profile" # Profile name

baseProfile: qodana.recommended

inspections:
  - inspection: MissingOverrideAnnotation
    options:
      ignoreObjectMethods: false
      ignoreAnonymousClassMethods: true
```
