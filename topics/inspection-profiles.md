[//]: # (title: Inspection profiles)

<var name="code-inspection-profiles-ide-help-url" value="https://www.jetbrains.com/help/idea/?Customizing_Profiles"/>
<var name="ide" value="IDE"/>
<var name="qodana.recommended" value="https://github.com/JetBrains/qodana-profiles/blob/master/.idea/inspectionProfiles/qodana.recommended.yaml"/>
<var name="java-glob" value="https://docs.oracle.com/javase/8/docs/api/java/nio/file/FileSystem.html#getPathMatcher-java.lang.String-"/>

Inspection profiles let you configure the inspections, the scope of files that these inspections analyze, 
and inspection severity settings. %product% uses inspection profiles to know how and what to inspect in a codebase.

You can employ profiles using either [CLI commands](docker-image-configuration.xml#docker-config-reference-profile),
or configuring the [`qodana.yaml`](qodana-yaml.md#Set+up+a+profile) file.

## Default profiles

Out of the box, Qodana provides several predefined profiles hosted on 
[GitHub](https://github.com/JetBrains/qodana-profiles/tree/master/.idea/inspectionProfiles):

* `qodana.starter` is the default profile and a subset of `qodana.recommended` triggering the [3-phase analysis](#three-phase-analysis) 
* `qodana.recommended` mostly implements the default IDE profiles, see the 
[IntelliJ IDEA](https://www.jetbrains.com/help/idea/customizing-profiles.html) documentation for details

> If you run Qodana in a [CI/CD pipeline](ci.md), make sure the file containing the profile resides in the working
directory where the VCS stores your project before building it.

### How to choose a proper profile

If you want a fresh start, you have two options:

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


## Set up a profile

You can set up a profile using either the `qodana.yaml` file or the [Shell commands](docker-image-configuration.xml). 

### Profile path

Invoking a profile by the profile path is the most convenient method for custom profiles.

<tabs group="inspecting-profile-tabs">
    <tab title="YAML" id="configure-profile-yaml" group-key="yaml">
    <code style="block" lang="yaml">
    profile:
        path: relative/path/in/your/project.yaml
    </code>
    </tab>
    <tab title="CLI" id="configure-profile-cli" group-key="cli">
    <include src="docker-image-configuration.xml" include-id="docker-config-reference-profile-profile-path"/>
    </tab>
</tabs>



### Profile name

This is how you can configure the profile name using `qodana.yaml`:

```yaml
  name: &lt;name&gt;
```

The `--profile-name` option lets you run %product% using either the 
[default profiles](inspection-profiles.md#Default+profiles) or the profile name from the custom profile.

<note>This feature is not available in the <a href="qodana-dotnet.md"/> linter.</note>

This command lets you override the default profile und run %product% using the
[`qodana.recommended`](inspection-profiles.md#Default+profiles) profile: </p>

<tabs group="cli-settings">
    <tab title="Docker image" group-key="docker-image">
        <code style="block" lang="shell" prompt="$">
            docker run \
               -v $(pwd):/data/project/ \
               jetbrains/qodana-&lt;linter&gt; \
               --profile-name qodana.recommended
        </code>
    </tab>
    <tab title="Qodana CLI" group-key="qodana-cli">
        <code style="block" lang="shell" prompt="$">
            qodana scan \
            -profile-name qodana.recommended
        </code>
    </tab>
</tabs>

If you need to run %product% with a custom profile, you can take its actual [profile name](custom-profiles.md#name).

This command lets you bind a custom profile:

<tabs group="cli-settings" filter="for-inspection-profiles">
    <tab title="Docker image" group-key="docker-image">
        <code style="block" lang="shell" prompt="$">
            docker run \
               -v $(pwd):/data/project/ \
               -v &lt;path-to-profile-file&gt;/&lt;file-name&gt;:/data/project/.idea/inspectionProfiles/&lt;file-name&gt; \
               jetbrains/qodana-&lt;linter&gt; \
               --profile-name &lt;profile-name-from-file&gt;
        </code>
    </tab>
    <tab title="Qodana CLI" group-key="qodana-cli">
        <code style="block" lang="shell" prompt="$">
            qodana scan \
            -v &lt;path-to-profile-file&gt;/&lt;file-name&gt;:/data/project/.idea/inspectionProfiles/&lt;file-name&gt; \
            --profile-name &lt;profile-name-from-file&gt;
        </code>
    </tab>
</tabs>

