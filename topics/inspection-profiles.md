[//]: # (title: Inspection profiles)

<var name="code-inspection-profiles-ide-help-url" value="https://www.jetbrains.com/help/idea/?Customizing_Profiles"/>
<var name="ide" value="IDE"/>
<var name="qodana.recommended" value="https://github.com/JetBrains/qodana-profiles/blob/master/.idea/inspectionProfiles/qodana.recommended.yaml"/>

Inspection profiles let you configure the inspections, the scope of files that these inspections analyze, 
and inspection severity settings. %product% uses inspection profiles to know how and what to inspect in a codebase.

You can employ profiles using either [CLI commands](docker-image-configuration.xml#docker-config-reference-profile),
or configuring the [`qodana.yaml`](qodana-yaml.md#Set+up+a+profile) file.

## Default profiles

Out of the box, Qodana provides several predefined profiles hosted on 
[GitHub](https://github.com/JetBrains/qodana-profiles/tree/master/.idea/inspectionProfiles):
* `qodana.starter` is the default profile that triggers the [3-phase analysis](#three-phase-analysis).
* `qodana.recommended` contains the preselected set of IntelliJ inspections.
* `qodana.sanity` contains a small set of preselected inspections. If these inspections fail, the project is probably 
misconfigured, and further inspection will not produce meaningful results. See the [](linters.md) section for details 
on configuring a project for the desired linter.

> If you run Qodana in a [CI/CD pipeline](ci.md), make sure the file containing the profile resides in the working
directory where the VCS stores your project before building it.

### How to choose a proper profile

If you want a fresh start, you have two options:

<!-- The qodana.recommended needs to be checked in this case -->

1. Use Qodana in the default mode to execute the [three-phase analysis](#three-phase-analysis). You do not need to 
create the [`qodana.yaml`](qodana-yaml.md) file in this case, but you can add it later to amend the set of inspections.
2. Run %product% using the `qodana.recommended` profile. In this case, you need to create the `qodana.yaml` file with a 
reference to the [`qodana.recommended`](qodana-yaml.md#Set+up+a+profile+by+the+name) profile. This profile contains the 
inspections for critical or severe issues in the codebase. This profile does not contain any style checks, and 
non-critical folders, such as `tests`, are ignored.

### Three-phase analysis
{id="three-phase-analysis"}

Sometimes it may be challenging to set up analysis for a big project even with the `qodana.recommended` profile due to 
large number of errors reported. To solve this, Qodana offers a 3-phase analysis, where each phase is focused on a 
certain type of results.

- The first phase is based on the `qodana.starter` profile that contains vital checks only. Non-critical folders, such as `tests`, are ignored.

- The second phase reports the conditions that could affect truthfulness or completeness of the results. For example, if your project relies on external resources or generated code, and they are not available during the analysis, the final results could be compromised. Qodana notifies you about such suspicious results.

- The last phase suggests additional checks that are not so vital for the project but still beneficial. To avoid overwhelming, Qodana analyzes only a fraction of the code, just enough to show you the possible outcome.

[//]: # (We recommend the following Qodana UI guidance to create the most effective profile you can support for your project.)

## Custom profiles

<!-- ALL inspections and inspections from the default IDE profile need to be explained here -->

%product% provides flexible profile configuration capabilities using the YAML format, such as:

* Human-readable format, so you can use any editor of your choice to edit profiles
* Clear profile structure
* Support for file paths and scopes 
* Extendability, so profiles can be extended using other profiles

<!-- Is this really required here?-->

All %product% profiles inherit either the default IDE profile settings or the settings of the included profiles. 

<tip>You can overview the default IDE profile by navigating to <menupath>Settings | Editor | Inspections</menupath>.</tip>

This is the sample profile configuration. 

```yaml
name: "My custom profile" # Profile name

include:
  - "./profiles/other-profile.yaml" # Extend profile and employ its settings

groups: # List of configured groups
  - groupId: InspectionsToInclude
    groups:
      - "category:PHP/General" # Inspection category from the linter
      - "JSCategories" # Include the JSCategories category from below
      - "PHPInspections" # Include inspections from PHPInspections
      - "!severity:TEXT ATTRIBUTES" # Exclude inspections with the specific severity 

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
```

This sample consists of several basic blocks: 

<!-- I need to check the YAML terminology about groups -->

| Section                       | Description                                                        |
|-------------------------------|--------------------------------------------------------------------|
| [`name`](#name)               | Name of the inspection profile                                     |
| [`include`](#include)         | Include an existing file-based profile into your profile           |
| [`groups`](#groups)           | Inspection groups that need to enabled or disabled in your profile |
| [`inspections`](#inspections-group) | Sequence of `groups` setting application                           |

### name

Name of the inspection profile in the quotes: 

```yaml
name: "Name of your profile"
```

This name does not have to correspond with the name of the file containing the profile. 

### include

<!-- How does it work in case group names coincide? -->

Specifies paths to the existing YAML profiles that you need to include in your profile, in the given order.
You can use and override the [groups](#groups) from the included profiles like they are part of your profile.

```yaml
include:
    - "./profiles/qodana.recommended.yaml"
    - "qodana.anotherprofile.yaml"
```

Before including, save the file containing the profile to the root directory of your project or its subdirectories.

<!-- Alexey: How are these files merged to the profile? In what sequence are they applied? -->
<!-- What happens if one profile supports, and the second does not? This needs to be tested or read -->
<!-- Mention that all groups from the extended file are automatically supported here -->

<!-- If used, the included profile files override the default IDE profile. -->
<!-- These ALL and default IDE inspections should be explained -->
<!-- Alexey: If the profile file is not found, the default IDEA profile is employed? This needs to be addressed -->

If your profile does not include any other profiles like the [default](#Default+profiles), it extends the default 
profile of your IDE and includes all its settings. To overview this profile, in your IDE navigate 
to **Settings | Editor | Inspections**. 

### groups

<!-- I need to mention exclamation marks and they are used in case of groups, not inspections -->
<!-- I need to mention here ALL -->
<!-- I need to mention that groups and separate inspections can be configured here -->
<!-- List of severities needs to be provided here -->

The `groups` block contains a bunch of groups, whereas each group can contain existing inspection categories, single
inspections, and include existing groups. After grouping, you can configure their invocation in 
the [`inspections`](#inspections-group) block.

This is the sample `groups` block.

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
      - "!ExcludedInspectionGroups"
      - "IncludedInspections"
      - "!severity:TEXT ATTRIBUTES"


```

This sample contains several groups, and each group contains these fields: 

| Group name                           | Description                                                   |
|--------------------------------------|---------------------------------------------------------------|
| [`groupId`](#groups-groupid)         | ID of the group                                               |
| [`inspections`](#groups-inspections) | List of inspections                                           |
| [`groups`](#groups-groups)           | Group of inspection categories and included inspection groups |


<anchor name="groups-groupid"/>

#### groupId

<!-- Where should it be unique? Only inside the profile, or also inside all profiles it extends from? -->

Identifier for the group required for both inspections and groups.

```yaml
  - groupId: IncludedInspections
```

<anchor name="groups-inspections"/>

#### inspections

The list of inspections that need to be configured by the profile.

```yaml
inspections:
    - JavaAnnotator
    - JSAnnotator
```

<anchor name="groups-groups"/>

#### groups

<!-- What happens if group names coincide? -->

Contains a list of inspection categories and included inspection groups:

```yaml
groups:
    - "ALL"
    - "category:Java"
    - "IncludedInspections"
    - "!ExcludedInspections"
    - "!severity:TEXT ATTRIBUTES"
```

This sample contains several lines:

| Configuration example       | Description                                                                                                                                                                         |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ALL`                       | Use this while creating [profiles from scratch](#Create+a+profile+from+scratch)                                                                                                     |
| `category:Java`             | Name of the inspection category in the `category:categoryname` notation, matches the name from the <menupath> Editor &#124; Settings &#124; Inspections</menupath> section of your IDE |
| `IncludedInspections`       | Name of the existing group from the profile, either the current or an extended                                                                                                      |
| `!ExcludedInspections`      | Negate the existing `ExcludedPaths` inspection group, either the current or an extended                                                                                             |
| `!severity:TEXT ATTRIBUTES` | Negate all inspections with the specific severity, which lets you filter inspections by severity levels                                                                         |


<!-- Severity levels should be mentioned here -->

<anchor name="inspections-group"/>

### inspections

Using the `inspections` block, you can specify: 

* Which inspection groups to enable or disable
* Order of group invocation
* Which files or scopes to ignore
* Set the severity level

the actions that should be taken towards [inspection groups](#groups).  

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
    severity: WARNING # It has default ERROR severity. It's understandable for unresolved references in javadocs for editor but not on CI.
```

<!-- ignore, inspection, and severity need to be checked -->

| Group name   | Description                                                                                           |
|--------------|-------------------------------------------------------------------------------------------------------|
| `group`      | Group name from [`groupId`](#groupId)                                                                 |
| `enabled`    | Specify whether the group is enabled in the profile. Accepts either `true` or `false`                 |
| `ignore`     | Specify the paths that should be excluded from inspection. Currently, this does not support wildcards |
| `inspection` ||
| `severity`   ||


<!-- The link to Inspectopedia needs to be provided here -->
<!-- For each group here, I need to provide small separate examples -->
<!-- Here needs to be added how to bind the profile file to the CLI command -->
<!-- I need to provide here basic examples of how to configure profiles -->
<!-- How do two groups prevent collision in settings? -->
<!-- The last setting overrides the previous settings in the inspections settings -->
<!-- What do these groups do besides enabled and disabled? -->


### Examples

<!-- An example with severity needs to be provided here too -->

#### Create a profile from scratch

<!-- This needs to be replaced with Java or Kotlin -->

This profile configuration disables all inspections, and then enables only the `PHP/General` inspection group from the 
[Qodana for PHP](qodana-php.md) linter. 

```yaml
name: "My custom profile"

groups:
  - groupId: IncludedInspections
    groups:
      - "category:PHP/General" # Specify the PHP/General category
      
  - groupId: ExcludedInspections
    groups:
      -  ALL
         
inspections:  
  - group: ExcludedInspections
    enabled: false # Disable all inspections

  - group: IncludedInspections
    enabled: true # Enable the PHP/General category
    
```

#### Exclude an inspection

This is how you can exclude the `PhpDeprecationInspection` inspection from the [Qodana for PHP](qodana-php.md) linter 
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

#### Override the existing profile

<tip>To start with, we recommend you to use the <code>qodana.starter</code> profile.</tip>

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

#### Filter by severity

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

<!-- File exclusion needs to be mentioned here -->