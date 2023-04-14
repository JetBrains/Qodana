[//]: # (title: Custom profiles)

<var name="code-inspection-profiles-ide-help-url" value="https://www.jetbrains.com/help/idea/?Customizing_Profiles"/>
<var name="ide" value="IDE"/>
<var name="qodana.recommended" value="https://github.com/JetBrains/qodana-profiles/blob/master/.idea/inspectionProfiles/qodana.recommended.yaml"/>
<var name="java-glob" value="https://docs.oracle.com/javase/8/docs/api/java/nio/file/FileSystem.html#getPathMatcher-java.lang.String-"/>
<var name="idea-scopes" value="https://www.jetbrains.com/help/idea/scope-language-syntax-reference.html"/>

%product% provides flexible profile configuration capabilities using the YAML format, such as:

* Support for file paths and [scopes](%idea-scopes%)
* Support for inspection parameters
* Profile relationship, so profiles can be extended and included

This is the sample profile configuration showing how you can fine-tune %product% for your needs.

```yaml
name: "My custom profile" # Profile name

baseProfile:
  - empty # Use the 'empty' profile as initial configuration of this profile

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

The `baseProfile` parameter lets you specify the profile that will serve as a basis for your profile configuration. It
can accept the following values: 

| `baseProfile` value  | Description                                                                                                                                                                                           |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Default`            | The [default profile](#custom-profiles-default-profile-tip) of your IDE                                                                                                                               |
| `Project Default`    | The profile is similar to `Default`, but contains user changes stored in the `.idea/inspectionProfiles/Project_Default.xml` file                                                                      |
| `qodana.starter`     | The [default](inspection-profiles.md#Default+profiles) %product% profile, a subset of the `qodana.recommended` profile                                                                                |
| `qodana.recommended` | The [default](inspection-profiles.md#Default+profiles) %product% profile implementing the default profiles of JetBrains IDEs                                                                          |
| `empty`              | Severities and parameters of inspections are taken from `Default`, but none inspections are included. Using `empty`, you can you can build your profile [from scratch](#Create+a+profile+from+scratch) |

If this parameter is missing, %product% will employ the IDE default profile, so all settings applied to your custom 
profile will override such settings contained in the IDE default profile. 

{id="custom-profiles-default-profile-tip"}

<tip>You can overview the default IDE profile by navigating to <menupath>Settings | Editor | Inspections</menupath>.</tip>

## name

Arbitrary name for your profile.

```yaml
name: "Name of your profile"
```

## groups

The `groups` block contains descriptions of user-defined groups. Using groups, you can combine inspection categories and
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
      - "ALL"
      - "!ExcludedInspectionGroups"
      - "IncludedInspections"
      - "severity:WEAK WARNING"
  - inspections:
    - JavaAnnotator
```

This sample also contains the following properties:

| Property                             | Description                                                                                                       |
|--------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| [`groupId`](#groups-groupid)         | ID of the group                                                                                                   |
| [`inspections`](#groups-inspections) | List of included and excluded inspections in this group                                                           |
| [`groups`](#groups-groups)           | List of included and excluded groups in this group |

### groups.groupId
{id="groups-groupid"}

Identifier for the group of inspections or groups.

```yaml
  - groupId: IncludedInspections
```

Because a profile file is parsed from top to bottom, in case two groups are defined under the same
`groupId`, the latest group met in the file will be employed. This rule also works for all included files because
the settings from included files are parsed prior to the local settings.

### groups.inspections
{id="groups-inspections"}

Contains the list of inspections included in the group.

```yaml
inspections:
    - JavaAnnotator
    - JSAnnotator
```

### groups.groups
{id="groups-groups"}

Contains a list of group IDs with possible exclamation mark character (`!`):

```yaml
groups:
    - "ALL"
    - "category:Java/Probable bugs"
    - "IncludedInspections" 
    - "!ExcludedInspections"
    - "severity:WEAK WARNING"
```

Here, `groups` lists several values:

| [`groupId`](#groups-groupid) value | Description                                                                                                                                                                                          |
|------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ALL`                              | Include all inspections. Besides that, you can also use `LOCAL` to inspect your code using inspections from your IDE, or `GLOBAL` to inspect your code using the **Inspect code** action of your IDE |
| `category:Java/Probable bugs`      | Name of the inspection category in the `category:categoryname` notation, matches the name from the **Editor &#124; Settings &#124; Inspections** section of your IDE                                 |
| `IncludedInspections`              | Name of the existing group from the profile, also applicable for included groups                                                                                                                     |
| `!ExcludedInspections`             | Negate the existing `ExcludedInspections` inspection group, also applicable for included groups                                                                                                      |
| `severity:WEAK WARNING`            | Filter inspections by [severity](#profile-severity-levels) levels. Using this example, you can filter by the `!DEFAULT!` severity with the `Weak Warning` name                                       |

{id="profile-severity-levels"}

By default, %product% supports the following severity levels inherited from the JetBrains IDEs that you can use while
configuring your profile:

* Error
* Warning
* Weak Warning



## inspections
{id="inspections-group"}

Using `inspections`, you can:

* Enable or disable a specific group or an inspection
* Define the order of applying these settings
* Define the paths or scopes to be ignored by the specific group or the inspection
* Change severity levels of the specific group or the inspection

```yaml
inspections:
  - group: IncludedInspections
    enabled: false
  - group: ALL
    ignore:
      - "vendor/**"
      - "build/**"
      - "buildSrc/**"
  - inspection: JavadocReference
    severity: WARNING
```

This sample contains several properties:

| Property     | Description                                                                                                                                                           |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `group`      | The group ID value of a group from the [`groupId`](#groups-groupid) property. This is also applicable for embedded groups                                             |
| `enabled`    | Specify whether the group or the inspection is enabled in the profile. Accepts either `true` or `false`                                                               |
| `ignore`     | List of paths and scopes relative to the project root that will be ignored during inspection. Employs the patterns described in the [Java](%java-glob%) documentation |
| `inspection` | Name of the inspection or the inspection group that needs to be configured.                                                                                           |
| `severity`   | Severity level that will be assigned to a group of inspections or a single inspection. For example, you can specify `WARNING` instead of `ERROR`                      |


## include

Contains the list of relative paths to included profiles.

```yaml
include:
    - "firstprofile.yaml" 
    - "relative/path/to/anotherprofile.yaml"
```

If your profile does not include any other profiles, the [`baseProfile`](#baseProfile) field is set to `Default`. 

To overview the default profile, in your IDE navigate to **Settings | Editor | Inspections**.

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

In this case, the custom profile configuration parsed by %product% will look like this:

```yaml
inspections:
  - inspection: Inspection1
    enabled: false # "bar.yaml" was included later than "foo.yaml"
  - inspection: Inspection2
    enabled: false # it was applied in the custom profile last
  - inspection: Inspection3
    enabled: true
```

## Examples

Here you can find several examples of profile configuration. The [](inspection-profiles.md#Set+up+a+profile) section
explains how to run your profile while inspecting code.

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

### Exclude an inspection

This sample shows how you can exclude the `PhpDeprecationInspection` inspection from the [Qodana for PHP](qodana-php.md) linter
while inspecting your code using the `PHP/General` inspection category.

```yaml
name: "PHP/General without PhpDeprecationInspection"

inspections:
  - group: "category:PHP/General"
    enabled: true # Enable the 'PHP/General' category
  - inspection: PhpDeprecationInspection
    enabled: false # Disable the PhpDeprecationInspection inspection
```

Alternatively, you can exclude the `PhpDeprecationInspection` inspection using two groups:

```yaml
name: "PHP/General without PhpDeprecationInspection"

groups:
  - groupId: IncludedInspections
    groups:
      - "category:PHP/General" # Specify the 'PHP/General' category
            
  - groupId: Inspection
    inspections:
      -  PhpDeprecationInspection # Specify the PhpDeprecationInspection inspection   

inspections:  
  - group: IncludedInspections
    enabled: true # Enable the 'PHP/General' category
    
  - group: Inspection 
    enabled: false # Disable the PhpDeprecationInspection inspection
```

### Override the existing profile

<tip>At the beginning, we recommend using the <code>qodana.starter</code> profile.</tip>

Using this profile, you can exclude inspection categories from the [`qodana.recommended`](%qodana.recommended%)
that are not related to the [Qodana for .NET](qodana-dotnet.md) linter.

<note> Remember to save the profile file to the root directory of your project.</note> 

```yaml
name: "My custom profile"

include:
  - "qodana.starter.yaml" # Include the qodana.starter profile

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
      - "category:JavaScript and TypeScript"
      - "category:Angular"
      - "category:Vue"
      - "category:Go"
      - "category:Python"
      - "category:General"
      - "category:TOML"
      
inspections:  
  - group: ExcludedInspections
    enabled: false
```

### Filter by severity

This sample includes all inspections with the `WEAK WARNING` severity level while inspecting Java code.

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
