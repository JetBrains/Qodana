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
reference to the [`qodana.recommended`](qodana-yaml.md#set-up-a-profile-by-the-name) profile. This profile contains the 
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
