[//]: # (title: Inspection profiles)

<var name="code-inspection-profiles-ide-help-url" value="https://www.jetbrains.com/help/idea/?Customizing_Profiles"/>
<var name="ide" value="IDE"/>

Inspection profiles keep information about the enabled inspections, the scope of files that these inspections analyze, 
and inspection severity settings. %product% uses inspection profiles to know how and what to inspect in a codebase.

## Default profiles

Out of the box, Qodana provides several predefined profiles:
* `empty` contains no inspections, which can be used as a basis for manual configuration.
* `qodana.starter`is the default profile that triggers the [3-phase analysis](#three-phase-analysis).
* `qodana.recommended` contains the preselected set of IntelliJ inspections.
* `qodana.sanity` contains a small set of preselected inspections. If these inspections fail, the project is probably 
misconfigured, and further examining it will not produce meaningful results. See the [](linters.md) section for details 
on configuring a project for the desired linter.

> Profile files are available on [GitHub](https://github.com/JetBrains/qodana-profiles/tree/master).

You can employ custom profiles using either [CLI commands](docker-image-configuration.xml#docker-config-reference-profile), 
or configuring the [`qodana.yaml`](qodana-yaml.md#Set+up+a+profile) file.

If you use a [CI/CD system](ci.md), make sure the XML-formatted file containing the profile resides in the working 
directory where the VCS stores your project before building it.

## How to choose a proper profile

If you want a fresh start, you have two options:

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

## Supported profile formats 

Currently, %product% supports two formats of profiles:

* XML-formatted profiles
* YAML-formatted profiles

Apart from the default profiles, XML-formatted profiles can be generated using your IDE. 

Compared to XML, the YAML-formatted profiles come as a replacement and provide the following advantages:

* YAML-formatted files are human-readable
* They implement the enhanced structure
* They provide scopes or paths to files. XML-formatted profiles provide only support for scopes. 

YAML-formatted profiles are human-readable, implement the enhanced structure, and come as a replacement for 
XML-formatted profiles. 

<!-- The file name convention can be added here as well -->
<!-- I need to add the main reason for using profiles. It can be done probably at the beginning of the section -->
<!-- I need to mention that all profiles are configured relatively to the default IDEA profile -->
<!-- Do I need to store all files the current profile extends from?-->
<!-- This requires an introduction from the doc why XML format is not convenient -->

Here is the sample of the `qodana.recommended` profile:

<!-- The custom profile needs to be tested -->

```yaml
name: "qodana.mycustomprofile"

include:
  - "qodana.recommended.yaml"

groups:
  - groupId: IncludedPaths # Qodana can run any inspections, but these groups are tested and monitored by Qodana team
    groups:
      - "ALL"
      - "category:Java"
      - "category:Kotlin"
      - "category:JVM languages"
    inspections:
      - Annotator # substituted by JavaAnnotator in sanity
      - KotlinAnnotator # works in "sanity" inspections
      - JavaAnnotator # works in "sanity" inspections


  - groupId: Excluded
    groups:
      - "ALL"
      - "!IncludedPaths"
      - "category:Java/Java language level migration aids" # Migration aids - only on explicit request, due to possible spam

  - groupId: ExcludedInspections # list of inspections disabled by specific reason
    inspections:
      - Annotator # substituted by JavaAnnotator in sanity
      - KotlinAnnotator # works in "sanity" inspections
      - JavaAnnotator # works in "sanity" inspections

inspections:
  - group: Excluded
    enabled: false
  - group: ALL
    ignore:
      - "vendor/**"
      - "build/**"
      - "buildSrc/**"
  - inspection: JavadocReference
    severity: WARNING # It has default ERROR severity. It's understandable for unresolved references in javadocs for editor but not on CI.


```

<!-- Are there really sections? -->
This sample contains several sections described below.

Groups groups the inspections, and inspections configures groups as I understand it.

## name

Contains the name of the inspection profile in the quotes.

## include

Specifies which existing profile file the current profile overrides. 
In case this group is missing in the file, it means that the profile extends the IDEA default profile. 
<!-- I need to provide the link where I can observe the default IDEA profile -->

The paths to YAML profiles that are merged into the current profile, in the given order.
When including a profile, its groups are added to the defined groups. Then, its inspections are processed.
After processing the included profiles, the groups and inspections from this profile are processed.

<!-- I need to train exclamation marks with profiles -->
<!-- If the profile file is not found, the default IDEA profile is employed? This needs to be addressed -->

## groups

This contains the list of groups where each group helps you get together and separate inspection groups that you would like 
to configure. This includes both inspection groups and separate inspections. 

This lets you move include or exclude inspections by addressing them to various groups. You can then apply 
configuration rules to such groups using the [`inspections`](#inspections) groups. 

It contains the following nested groups: 

* `groupId` is the group ID
* `groups` contains the list of inspection groups included or excluded by this group. This list can contain both groups from the 
current profile and the groups from the profile the current profile extends from. This group can also accept the groups 
in the `category:groupname` notation and thus override the group provided by the IDE (The link to the IDE documentation 
with IDEA as an example where I can find it). The category name starts with the technology name
<!-- Here should be the examples of technologies that need to be mentioned for clarity -->
* `inspections` specifies the inspections that need to be included in the group.

## inspections

Using this group, you can manage the inspections that are collected in the groups, and you can 
override from the profiles. 

It contains the following groups inside it:

* `group` is the name of the [group](#groups) that needs to be configured from 
* `enabled` configures whether this group is enabled. Accepts two values: `true` and `false`
* `ignore` uses paths relatively to the project root, it applies the IDEA scopes
* `inspection`
* `severity`

<!-- The link to Inspectopedia needs to be provided here -->
<!-- For each group here, I need to provide small separate examples -->

It contains the following 

This group 

Each YAML-formatted profile adheres to the following structure:

name - contains the profile name
groups - 

* Groups that can or cannot be included in the profile
  category:groupname is a group provided by IDEA.

<!-- Here needs to be added how to bind the profile file to the CLI command -->
<!-- I need to provide here basic examples of how to configure profiles -->
<!-- How do two groups prevent collision in settings? -->
<!-- The last setting overrides the previous settings in the inspections settings -->
<!-- What do these groups do besides enabled and disabled? -->