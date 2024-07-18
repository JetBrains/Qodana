[//]: # (title: Inspection profiles)

<show-structure for="chapter" depth="3"/>

<var name="code-inspection-profiles-ide-help-url" value="https://www.jetbrains.com/help/idea/?Customizing_Profiles"/>
<var name="ide" value="IDE"/>
<var name="qodana.recommended" value="https://github.com/JetBrains/qodana-profiles/blob/master/.idea/inspectionProfiles/qodana.recommended.yaml"/>
<var name="java-glob" value="https://docs.oracle.com/javase/8/docs/api/java/nio/file/FileSystem.html#getPathMatcher-java.lang.String-"/>

<link-summary>Inspection profiles configure inspections, file scopes that these inspections analyze, 
and severities.</link-summary>

Inspection profiles define [inspections](code-inspections.topic), the file scopes that these inspections analyze, and 
inspection [severities](troubleshooting.topic#troubleshooting-severities). This section explains how you can use 
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
        <td>The subset of the <code>qodana.recommended</code> profile, enabled in %product% by default</td>
    </tr>
    <tr>
        <td><code>qodana.recommended</code></td>
        <td><p>Implements default profiles of JetBrains IDEs like 
        <a href="https://www.jetbrains.com/help/idea/customizing-profiles.html">IntelliJ IDEA</a> with the following 
        exceptions:</p> 
        <list>
            <li>
                By default, Qodana provides analysis only for specific languages and frameworks. This means that, for 
                example, Groovy or JavaScript inspections are available but disabled by default. Inspections
                of the <code>INFORMATION</code> <a href="troubleshooting.topic" anchor="troubleshooting-severities">severity</a> 
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

All profiles are hosted on 
[GitHub](https://github.com/JetBrains/qodana-profiles/tree/master/.idea/inspectionProfiles), so you can learn them in detail.

To learn how to set up existing %product% profiles, see the [](#inspection-profiles-setup-a-profile) section. 

## Custom profiles
{id="inspection-profiles-custom-profiles"}

<link-summary>You can create custom profiles in the YAML and XML formats, and then run %product% using them.</link-summary>

You can create custom profiles using the following formats:

* [YAML](custom-profiles.md) is the preferred format,
* [XML](custom-xml-profiles.md) can be used as an alternative to YAML.

Custom profiles can either override [existing profiles](#inspection-profiles-existing-profiles) or be created from 
scratch. Since profile configurations should be contained in dedicated files, we recommend saving them in the `.qodana` 
directory of your project.

For example, to use the existing `qodana.recommended` profile and additionally enable the 
`Java/Java language level migration aids` inspection category, save this [YAML](custom-profiles.md) configuration in the profile file:

```yaml
name: "Configuring Qodana" 
baseProfile: qodana.recommended

inspections:
   - group: "category:Java/Java language level migration aids" # Specify the inspection category
     enabled: true # Enable the inspection category
```

> A detailed reference guide is available in the [](custom-profiles.md) section. 

After you create your own profile, save the file in the `.qodana` directory of your project so that %product% can 
ignore this file during code analysis.

> If you run Qodana in a [CI/CD pipeline](ci.md), make sure the file containing the profile resides in the working
directory where the VCS stores your project before building it.
{style="note"}

To learn how to set up a custom profile, see the [](#inspection-profiles-setup-a-profile) section.

## Set up a profile
{id="inspection-profiles-setup-a-profile"}

<link-summary>Learn how to set up %product% and custom profiles.</link-summary>

<note>You can disable the <code>qodana.sanity</code> profile using recommendations from the 
<a href="qodana-yaml.md" anchor="Disable+sanity+checks"/> and 
<a href="docker-image-configuration.topic" anchor="docker-config-reference-profile"/> sections.</note>

### YAML configuration
{id="inspection-profiles-yaml-file"}

<link-summary>YAML configuration is the universal configuration method that works for all software.</link-summary>

A YAML file serves as a universal %product% configuration. This means that you can configure %product% using the [`qodana.yaml`](qodana-yaml.md) file
once and then reuse it for running %product% with Docker, GitHub, JetBrains IDEs or any other [software](ci.md) currently 
supported by %product%. The settings will remain consistent across all these platforms.

<tabs group="profile-setup">
    <tab title="Qodana profile" group-key="qodana-profile">
        <p>To set up the <code>qodana.recommended</code> profile, in the project root save the <code>qodana.yaml</code> file 
        containing the following configuration:</p>
            <code-block lang="yaml">
            profile:
            &nbsp;&nbsp;&nbsp;&nbsp;name: qodana.recommended
            </code-block>
    </tab>
    <tab title="Custom profile" group-key="custom-profile">
        <p>To set up your custom profile, in the <code>qodana.yaml</code> file save this configuration containing the relative 
        path to the profile file, for example:</p>
            <code-block lang="yaml">
            profile:
            &nbsp;&nbsp;&nbsp;&nbsp;path: .qodana/&lt;custom-profile.yaml&gt;
            </code-block>
    </tab>
</tabs>

### JetBrains IDE
{id="inspection-profiles-ide"}

<link-summary>You can configure profiles before running %product% in JetBrains IDEs.</link-summary>

<procedure>
<step>
   <p>In your IDE, navigate to <ui-path>Tools | Qodana | Try Code Analysis with Qodana</ui-path>.</p> 
</step>
<step>
   <p>On the <code>profile</code> section of the <ui-path>Run Qodana</ui-path> dialog, paste the profile configuration:</p>
    <tabs group="profile-setup">
        <tab title="Qodana profile" group-key="qodana-profile">
            <code-block lang="yaml">
            profile:
            &nbsp;&nbsp;name: qodana.recommended
            </code-block>
<p>This is an example of how the result will look:</p> 
<img src="inspection-profiles-ide-default-profile.png" width="793" alt="Configuring a Qodana profile" border-effect="line"/>
        </tab>
        <tab title="Custom profile" group-key="custom-profile">
            <code-block lang="yaml">
            profile:
            &nbsp;&nbsp;&nbsp;&nbsp;path: .qodana/&lt;custom-profile.yaml&gt;
            </code-block>
<p>This is an example of how the result will look:</p> 
 <img src="inspection-profiles-ide-custom-profile.png" width="793" alt="Configuring a custom profile" border-effect="line"/>
        </tab>
    </tabs>
</step>
<step><p>On the <ui-path>Run Qodana</ui-path> dialog, check the <ui-path>Save qodana.yaml in project root</ui-path> option.</p>
   <img src="inspection-profiles-ide-save-file.png" width="793" alt="Saving qodana.yaml to a project root" border-effect="line"/>
</step>
<step>
    <p>Click <ui-path>Run</ui-path> to start analyzing your code.</p>
</step>
</procedure>

### GitHub Actions
{id="inspection-profiles-github"}

<link-summary>You can configure profiles before running %product% in GitHub.</link-summary>

> Running %product% using GitHub requires a [project token](project-token.md).
{style="note"}

<procedure>
    <step>On the <ui-path>Settings</ui-path> tab of the GitHub UI, create the <code>QODANA_TOKEN</code>
        <a href="https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository">encrypted secret</a>
        and save the <a href="cloud-projects.topic" anchor="cloud-manage-projects">project token</a> as its value.
    </step>
    <step>On the <ui-path>Actions</ui-path> tab of the GitHub UI, set up a new workflow and create the
        <code>.github/workflows/code_quality.yml</code> file.</step>
    <step>To inspect the <code>main</code> branch, release branches and the pull requests coming
    to your repository, save the workflow configuration to the <code>.github/workflows/code_quality.yml</code> file:
        <tabs group="profile-setup">
            <tab title="Qodana profile" group-key="qodana-profile">
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
                    uses: JetBrains/qodana-action@v2024.1
                    with:
                      args: --profile-name,qodana.recommended
                    env:
                      QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
        </code-block>
            <p>Here, the <code>--profile-name</code> option specifies the <code>qodana.recommended</code> profile.</p>
        </tab>
            <tab title="Custom profile" group-key="custom-profile">
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
                    uses: JetBrains/qodana-action@v2024.1
                    with:
                      args: --profile-path,.qodana/&lt;custom-profile.yaml&gt;
                    env:
                      QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
        </code-block>
            <p>Here, the <code>--profile-path</code> option specifies the relative path to the file containing a custom profile.</p>
</tab>
        </tabs>
    </step>
</procedure>

### Command line
{id="inspection-profiles-local-run"}

<link-summary>You can configure profiles before running %product% locally.</link-summary>

> Running %product% using GitHub requires a [project token](project-token.md).
{style="note"}

<tabs group="profile-setup">
<tab title="Qodana profile" group-key="qodana-profile">
<p>You can set up the <code>qodana.recommended</code> profile using the <code>--profile-name</code> option:</p>
<tabs group="cli-settings">
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$">
            docker run \
               -v $(pwd):/data/project/ \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               jetbrains/qodana-&lt;linter&gt; \
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
<tab title="Custom profile" group-key="custom-profile">
<p>You can set up your custom profile using the <code>--profile-path</code> option:</p>
<tabs group="cli-settings" filter="for-inspection-profiles">
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$">
            docker run \
               -v $(pwd):/data/project/ \
               -v $(pwd)/.qodana/&lt;custom-profile.yaml&gt;:/data/project/myprofiles/&lt;custom-profile.yaml&gt; \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               jetbrains/qodana-&lt;linter&gt; \
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