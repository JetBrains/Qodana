[//]: # (title: Inspection profiles)

<var name="code-inspection-profiles-ide-help-url" value="https://www.jetbrains.com/help/idea/?Customizing_Profiles"/>
<var name="ide" value="IDE"/>

Inspection profiles let you configure the inspections, the scope of files that these inspections analyze, 
and inspection severity settings. %product% uses inspection profiles to know how and what to inspect in a codebase.

## Default profiles

Out of the box, Qodana provides several predefined profiles:
* `empty` contains no inspections, which can be used as a basis for [manual configuration](#Create+your+profile).
* `qodana.starter` is the default profile that triggers the [3-phase analysis](#three-phase-analysis).
* `qodana.recommended` contains the preselected set of IntelliJ inspections.
* `qodana.sanity` contains a small set of preselected inspections. If these inspections fail, the project is probably 
misconfigured, and further inspection will not produce meaningful results. See the [](linters.md) section for details 
on configuring a project for the desired linter.

Except `empty`, all these profiles override the default profile settings available under 
**Settings | Editor | Inspections** of your IDE.

> Profile files are available on [GitHub](https://github.com/JetBrains/qodana-profiles/tree/master/.idea/inspectionProfiles).

You can employ custom profiles using either [CLI commands](docker-image-configuration.xml#docker-config-reference-profile), 
or configuring the [`qodana.yaml`](qodana-yaml.md#Set+up+a+profile) file.

If you use a [CI/CD system](ci.md), make sure the file containing the profile resides in the working 
directory where the VCS stores your project before building it.

## How to choose a proper profile

If you want a fresh start, you have two options:

<!-- The qodana.recommended needs to be checked in this case -->

1. Use Qodana in the default mode to execute the [three-phase analysis](#three-phase-analysis). You do not need to 
create the [`qodana.yaml`](qodana-yaml.md) file in this case, but you can add it later to amend the set of inspections.
2. Run %product% using the `qodana.recommended` profile. In this case, you need to create the `qodana.yaml` file with a 
reference to the [`qodana.recommended`](qodana-yaml.md#Set+up+a+profile+by+the+name) profile. This profile contains the 
inspections for critical or severe issues in the codebase. This profile does not contain any style checks, and 
non-critical folders, such as `tests`, are ignored.

## Three-phase analysis
{id="three-phase-analysis"}

Sometimes it may be challenging to set up analysis for a big project even with the `qodana.recommended` profile due to 
large number of errors reported. To solve this, Qodana offers a 3-phase analysis, where each phase is focused on a 
certain type of results.

- The first phase is based on the `qodana.starter` profile that contains vital checks only. Non-critical folders, such as `tests`, are ignored.

- The second phase reports the conditions that could affect truthfulness or completeness of the results. For example, if your project relies on external resources or generated code, and they are not available during the analysis, the final results could be compromised. Qodana notifies you about such suspicious results.

- The last phase suggests additional checks that are not so vital for the project but still beneficial. To avoid overwhelming, Qodana analyzes only a fraction of the code, just enough to show you the possible outcome.

[//]: # (We recommend the following Qodana UI guidance to create the most effective profile you can support for your project.)

## Create your profile

Currently, %product% lets you configure %product% profiles in the XML and YAML formats.

Configuring XML-formatted profiles is outside the scope of this section.

YAML-formatted profiles come as a replacement to XML and provide the following advantages:

* Human-readable format, so you can use any editor of your choice
* Enhanced structure
* Support for paths to files in addition to scopes  

Profiles override the default profile of your IDE. To overview the set of inspections 
comprising the default profile, in your IDE navigate to **Settings | Editor | Inspections**.

Here is the sample profile:

<!-- This needs to be shortened and simplified for containing more information. Probably, the comments can be deleted too -->

```yaml
name: "My custom profile" # Profile name

include:
  - "general-profile.yaml" # Profile to use settings from

groups: # List of groups configured in this profile 
  - groupId: ExcludedInspections
    groups:
      - "ALL" # All available inspections
      
  - groupId: IncludedInspections
    groups:
      - "category:PHP/General" # Category configured by this group
      - "IncludeJS" # Including the IncludeJS group from this profile 

  - groupId: IncludeJS
    groups: 
      - "category:JavaScript and TypeScript/ES2015 migration aids"
    inspections:
      - JSAnnotator # A separate inspection from the Qodana for JS linter

inspections: # Configuring what to do with the groups
  - group: ExcludedInspections
    enabled: false # Disabling the group
  
  - group: IncludedInspections
    enabled: true # Enabling the group
    ignore:
      - "vendor/**"
      - "build/**"
      - "buildSrc/**"
  - inspection: JavadocReference
    severity: WARNING # It has default ERROR severity. It's understandable for unresolved references in javadocs for editor but not on CI.


```

This sample consists of several blocks: 

<!-- I need to check the YAML terminology about groups -->

| Section                       | Description                                                        |
|-------------------------------|--------------------------------------------------------------------|
| [`name`](#name)               | Name of the inspection profile                                     |
| [`include`](#include)         | Include an existing file-based profile into the profile            |
| [`groups`](#groups)           | Inspection groups that need to enabled or disabled in your profile |
| [`inspections`](#inspections) | Configuration applied to the inspections mentioned in `groups`     |

### name

Contains the name of the inspection profile in the quotes. For example, it can be:

```yaml
name: "qodana.mycustomprofile"
```

### include

Specifies the existing YAML profiles that can be extended by your profile, in the given order.

<!-- How are these files merged to the profile? How does the order affect here? -->
<!-- What happens if one profile supports, and the second does not? This needs to be tested or read -->

```yaml
include:
  - "qodana.recommended.yaml"
  - "qodana.anotherprofile.yaml"
```

<!-- Does it have to be stored in the same directory with the current profile file? -->

<!-- Is the first sentence from this paragraph true? -->
If used, the included profile files override the default IDE profile. 

When including a profile, its [groups](#groups) are added to the groups of your profile and used for inspections.

<!-- I need to test exclamation marks with profiles -->
<!-- Alexey: If the profile file is not found, the default IDEA profile is employed? This needs to be addressed -->

### groups

This group contains the list of custom inspection groups, which lets you configure inspections in bulk.  

```yaml
groups:
  - groupId: IncludedInspections
    groups:
      - "ALL"
      - "category:Java"
      - "IncludedInspections"
      - "!ExcludedPaths"
    inspections:
      - JavaAnnotator
```

After grouping, you can apply configuration rules using the [`inspections`](#inspections-group) groups. 

It contains several nested groups listed in this table: 

| Group name                           | Description                                      |
|--------------------------------------|--------------------------------------------------|
| [`groupId`](#groups-groupid)         | ID of the group                                  |
| [`groups`](#groups-groups)           | Inspection groups managed by the current group   |
| [`inspections`](#groups-inspections) | Certain inspections managed by the current group |


<!-- Can I exchange the places for groups and inspections? This needs to be tested -->

<anchor name="groups-groupid"/>

#### groupId

<!-- Where should it be unique? Only inside the profile, or also inside all profiles it extends from? -->

Identifier for the group. 

```yaml
groups:
  - groupId: IncludedInspections
```

<anchor name="groups-groups"/>

#### groups

List of inspection groups managed by the group. This sample covers all possible cases:

```yaml
groups:
    groups:
      - "ALL"
      - "category:Java"
      - "IncludedInspections"
      - "!ExcludedPaths"
```

Here is the description of each case from the sample:

| Configuration example | Description                                                                                                          |
|-----------------------|----------------------------------------------------------------------------------------------------------------------|
| `ALL`                 | <!-- The description here needs to be provided -->                                                                   |
| `category:Java`       | Name of the inspection category in the `category:categoryname` notation, matches the name from the <menupath> Editor &#124; Settings &#124; Inspections</menupath> section of your IDE |
| `IncludedInspections` | Name of the group already mentioned in in the profile                                                                |
| `!ExcludedPaths`      | Inverted values from the `ExcludedPaths` group                                                                       |

<!-- IncludedInspections - is it only about the current profile file, or the merged files too? -->
<!-- !ExcludedPaths - is this correct in this case? Needs to be tested -->

<anchor name="groups-inspections"/>

#### inspections

The list of certain inspections that need to be included or excluded using the group. 

```yaml
groups:
    inspections:
      - JavaAnnotator
```

<anchor name="inspections-group"/>

### inspections

Using `inspections`, you can specify the actions that should be taken towards [inspection groups](#groups).  

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