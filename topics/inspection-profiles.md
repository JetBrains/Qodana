[//]: # (title: Inspection profiles)

<var name="code-inspection-profiles-ide-help-url" value="https://www.jetbrains.com/help/idea/?Customizing_Profiles"/>
<var name="ide" value="IDE"/>
<var name="qodana.recommended" value="https://github.com/JetBrains/qodana-profiles/blob/master/.idea/inspectionProfiles/qodana.recommended.yaml"/>
<var name="java-glob" value="https://docs.oracle.com/javase/8/docs/api/java/nio/file/FileSystem.html#getPathMatcher-java.lang.String-"/>

Inspection profiles let you configure the inspections, the scope of files that these inspections analyze, 
and inspection severity settings. %product% uses inspection profiles to know how and what to inspect in a codebase.

You can employ profiles either using CLI or configuring the `qodana.yaml` file as shown in the [](#Set+up+a+profile) section.

## Default profiles

Out of the box, Qodana provides several predefined profiles hosted on 
[GitHub](https://github.com/JetBrains/qodana-profiles/tree/master/.idea/inspectionProfiles):

* `qodana.starter` is the default profile and a subset of `qodana.recommended` triggering the [3-phase analysis](#three-phase-analysis) 
* `qodana.recommended` is suitable for CI/CD pipelines and mostly implements the default IDE profiles, see the 
[IntelliJ IDEA](https://www.jetbrains.com/help/idea/customizing-profiles.html) documentation for details

> If you run Qodana in a [CI/CD pipeline](ci.md), make sure the file containing the profile resides in the working
directory where the VCS stores your project before building it.

### How to choose a proper profile

If you want a fresh start, you have two options:

1. Use Qodana in the default mode to execute the [three-phase analysis](#three-phase-analysis). You do not need to 
create the [`qodana.yaml`](qodana-yaml.md) file in this case, but you can add it later to amend the set of inspections.
2. Run %product% using the `qodana.recommended` profile. In this case, you need to create the `qodana.yaml` file with a 
reference to the [`qodana.recommended`](#Default+profiles) profile. This profile contains the 
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


## Set up a profile

You can set up a profile using either the `qodana.yaml` file or the [Shell commands](docker-image-configuration.xml). 

### Profile name

This is how you can configure the profile name using `qodana.yaml`:

```yaml
  name: &lt;name&gt;
```

<include src="lib_qd.xml" include-id="inspection-profiles-profile-name"/>

### Profile path

This is how you can configure the profile path using `qodana.yaml`:

```yaml
profile:
    path: relative/path/in/your/project.xml
```

You can also use it for [custom profiles](custom-profiles.md).

<include src="lib_qd.xml" include-id="inspection-profiles-profile-path"/>
