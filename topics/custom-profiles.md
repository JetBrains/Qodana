[//]: # (title: Custom profiles)

%product% provides flexible profile configuration capabilities using the YAML format, such as:

* Support for file paths and scopes
* Support for inspection parameters
* Profile relationship, so profiles can be extended and included

This is the sample profile configuration showing how you can fine-tune %product% for your needs.

```yaml
name: "My custom profile" # Profile name

baseProfile:
  - empty # Reset the default IDE profile

include:
  - ".qodana/profiles/other-profile.yaml" # Extend profile and employ its settings

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
inspections:
  - inspection: PhpNonCompoundUseInspection
    severity: WARNING # Overriding the severity level for PhpNonCompoundUseInspection
```

This sample consists of several nodes:

| Section                     | Description                                                       |
|-----------------------------|-------------------------------------------------------------------|
| `baseProfile`               | Reset the default IDE profile |
| [`name`](#name)             | Name of the inspection profile                                    |
| [`include`](#include)       | Include an existing file-based profile into your profile          |
| [`groups`](#groups)         | Inspection groups that need to enabled or disabled in your profile |
| [`inspections`](#inspections-group) | Sequence of `groups` setting application                          |


By default, %product% supports the following severity levels inherited from the JetBrains IDEs that you can use while
configuring your profile:

{id="profile-severity-levels"}

* Error
* Warning
* Weak Warning

## baseProfile

%product% profiles employ the default IDE profile, so all settings applied to your custom profile override such
settings contained in the default IDE profile. If your custom profile [includes](#include) another profile that
completely overrides the default IDE profile, then your profile also contains nothing of it.

<tip>You can overview the default IDE profile by navigating to <menupath>Settings | Editor | Inspections</menupath>.</tip>

If you set `baseProfile` to `empty`, you will clear your profile from any configuration including the default IDE profile.
This can be useful if you are going to build your profile [from scratch](#Create+a+profile+from+scratch) rather than
extend from the existing profile.

## name

Arbitrary name for your profile.

```yaml
name: "Name of your profile"
```

## include

Paths to the existing profiles which are included in your profile.

```yaml
include:
    - ".qodana/profiles/qodana.recommended.yaml"
    - ".qodana/profiles/qodana.anotherprofile.yaml"
```

Before including a profile, save the file containing it to the root directory of your project or its subdirectories.

If your profile does not include any profiles, it employs the default profile of your
IDE and includes all its settings. To overview the default profile, in your IDE navigate to **Settings | Editor | Inspections**.

File contents are included in the order of appearance, thus becoming part of your profile. This means that the settings
of the included files are used prior to the settings specified in the local profile.

### Example

Suppose, you have the `foo.yaml` and `bar.yaml` profiles.

The `foo.yaml` profile includes the `Java/Data Flow` inspection category:

```yaml
groups:
  - groupId: Included
  - "category:Java/Data Flow"

inspections:
  - group: Included
    enabled: true
```

The `bar.yaml` profile includes the `Java/Error handling` inspection category, and excludes the `Java/Data Flow` category:

```yaml
groups:
  - groupId: Included
  - "category:Java/Error handling"
  - groupId: Excluded
  - "category:Java/Data Flow"

inspections:
  - group: Included
    enabled: true
  - group: Excluded
    enabled: false
```

Depending on the sequence that these profiles are included, you can have different results:

| Sequence of inclusion       | Result                                                               |
|-----------------------------|----------------------------------------------------------------------|
| `foo.yaml` <br/> `bar.yaml` | `Java/Error handling` is included <br/> `Java/Data Flow` is excluded |
| `bar.yaml`<br/> `foo.yaml`  | Both `Java/Error handling` and `Java/Data Flow` are included         |


## groups

The `groups` block operates inspection groups and individual inspections, and can be either predefined by a linter or
defined by a user.

Each group can include existing inspection categories, single inspections, and existing groups. You can use the
exclamation mark character (`!`) to negate a group or a category.
For example, you can disable a specific category usage in a group that will be enabled.

After grouping, you can configure their invocation in the [`inspections`](#inspections-group) block.

This is the sample `groups` block containing the groups defined by a user.

```yaml
groups:

  - groupId: IncludedInspections
    inspections:
      - JavaAnnotator 
      - JSAnnotator 

  - groupId: ExcludedInspectionGroups
    groups:
      - "category:Gradle" 
      - "category:Groovy"

  - groupId: EnabledInspections
    groups:
      - "category:Java" 
      - "!ExcludedInspectionGroups" # Exclude the ExcludedInspectionGroups group
      - "IncludedInspections" # Include the IncludedInspections group
      - "!severity:WEAK WARNING"
```

Inside `groups`, this sample contains several groups, and each group contains these nodes:

| Group name                           | Description                                                   |
|--------------------------------------|---------------------------------------------------------------|
| [`groupId`](#groups-groupid)         | ID of the group                                               |
| [`inspections`](#groups-inspections) | List of inspections                                           |
| [`groups`](#groups-groups)           | Group of inspection categories and included inspection groups |

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

The list of inspections that need to be grouped.

```yaml
inspections:
    - JavaAnnotator
    - JSAnnotator
```

### groups.groups
{id="groups-groups"}

Contains a list of inspection categories and included inspection groups:

```yaml
groups:
    - "ALL"
    - "category:Java"
    - "IncludedInspections"
    - "!ExcludedInspections"
    - "!severity:TEXT ATTRIBUTES"
```

This sample includes several nodes:

| Configuration example       | Description                                                                                                                                                                            |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ALL`                       | Use this to specify all possible inspections. This can be an alternative to using `baseProfile` while creating [profiles from scratch](#Create+a+profile+from+scratch)                 |
| `category:Java`             | Name of the inspection category in the `category:categoryname` notation, matches the name from the <menupath> Editor &#124; Settings &#124; Inspections</menupath> section of your IDE |
| `IncludedInspections`       | Name of the existing group from the profile, either the current or an extended                                                                                                         |
| `!ExcludedInspections`      | Negate the existing `ExcludedPaths` inspection group, either the current or an extended                                                                                                |
| `!severity:TEXT ATTRIBUTES` | Negate all inspections with the specific [severity](#profile-severity-levels), which lets you filter inspections by severity levels                                                    |

## inspections
{id="inspections-group"}

Using `inspections`, you can specify:

* Which inspection groups to enable or disable
* The Order of [group](#groups) invocation
* Which files or scopes to ignore
* The severity level for specific inspections

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

This sample contains several nodes:

| Group name   | Description                                                                                                                                                                             |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `group`      | Group name from [`groupId`](#groups-groupid)                                                                                                                                            |
| `enabled`    | Specify whether the group is enabled in the profile. Accepts either `true` or `false`                                                                                                   |
| `ignore`     | Paths relative to the project root that will be ignored during inspection. Employs the patterns described in the [Java](%java-glob%) documentation |
| `inspection` | Name of the inspection which severity needs to be overridden. For example, if you consider a problem to be a `WARNING` instead of `ERROR`                                               |
| `severity`   | Severity level that will be assigned to `inspection`                                                                                                                                    |


## Examples

Here you can find several examples of profile configuration.

### Create a profile from scratch

Using `baseProfile`, this configuration defines the empty profile, and then it enables only the `Java/Data flow`
inspection group from the [Qodana for JVM](qodana-jvm.md) linter.

```yaml
name: "My custom profile"

baseProfile:
  - empty

groups:
  - groupId: IncludedInspections
    groups:
      - "category:Java/Data flow" # Specify the Java/Data flow category
               
inspections:  
  - group: IncludedInspections
    enabled: true # Enable the PHP/General category
    
```

As an alternative to `baseProfile`, you can use `ALL`:

```yaml
name: "My custom profile"

baseProfile:
  - empty

groups:
  - groupId: ExcludedInspections
    groups:
      - "ALL"

  - groupId: IncludedInspections
    groups:
      - "category:Java/Data flow" # Specify the Java/Data flow category
               
inspections:  
  - group: ExcludedInspections
    enabled: false # Disable all inspections
    
  - group: IncludedInspections
    enabled: true # Enable the Java/Data flow category
```

### Exclude an inspection

This sample shows how you can exclude the `PhpDeprecationInspection` inspection from the [Qodana for PHP](qodana-php.md) linter
while inspecting your code using the `PHP/General` inspection category.

```yaml
name: "My custom profile"

groups:
  - groupId: IncludedInspections
    groups:
      - "category:PHP/General"
      - "!Inspection" # Disable the Inspection group
            
  - groupId: Inspection 
    inspections:
      -  PhpDeprecationInspection # Specify the PhpDeprecationInspection inspection    

inspections:  
  - group: IncludedInspections
    enabled: true
```

Alternatively, you can explicitly disable the `PhpDeprecationInspection` inspection in the `inspections` group:

```yaml
name: "My custom profile"

groups:
  - groupId: IncludedInspections
    groups:
      - "category:PHP/General"
            
  - groupId: Inspection
    inspections:
      -  PhpDeprecationInspection # Specify the PhpDeprecationInspection inspection   

inspections:  
  - group: IncludedInspections
    enabled: true
    
  - group: Inspection 
    enabled: false # Disable the Inspection group
```

### Override the existing profile

<tip>At the beginning, we recommend using the <code>qodana.starter</code> profile.</tip>

Using this profile, you can exclude inspection categories from the [`qodana.recommended`](https://%qodana.recommended%)
that are not related to the [Qodana for .NET](qodana-dotnet.md) linter.

<note> Remember to save the profile file to the root directory of your project.</note> 

```yaml
name: "My custom profile"

include:
  - "qodana.recommended.yaml" # Extend the qodana.recommended profile

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

This sample excludes all inspections with the `WEAK WARNING` severity level while inspecting Java code.

```yaml
name: "My custom profile"

groups:
  - groupId: IncludedInspections
    groups:
      - "category:Java"
      - "!severity:WEAK WARNING"
            
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
