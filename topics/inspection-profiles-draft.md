[//]: # (title: Inspection profiles)

<no-index/>

<show-structure for="chapter" depth="3"/>

<var name="code-inspection-profiles-ide-help-url" value="https://www.jetbrains.com/help/idea/?Customizing_Profiles"/>
<var name="ide" value="IDE"/>
<var name="qodana.recommended" value="https://github.com/JetBrains/qodana-profiles/blob/master/.idea/inspectionProfiles/qodana.recommended.yaml"/>
<var name="java-glob" value="https://docs.oracle.com/javase/8/docs/api/java/nio/file/FileSystem.html#getPathMatcher-java.lang.String-"/>

<link-summary>Inspection profiles configure inspections, file scopes that these inspections analyze, 
and severities.</link-summary>

Inspection profiles configure [inspections](code-inspections.topic), file scopes that these inspections analyze, and 
[severities](troubleshooting.topic#troubleshooting-severities). Using inspection profiles, you tell %instance% about
a scope and methods of inspection.

## %product% profiles
{id="Default+profiles"}

<link-summary>Out of the box, Qodana provides the qodana.starter and qodana.recommended profiles.</link-summary>

Out of the box, you can employ these %product% profiles: 

<table>
    <tr>
        <td>Profile name</td>
        <td>Description</td>
        <td>How to configure</td>
    </tr>
    <tr>
        <td><code>qodana.starter</code></td>
        <td>The default %product% profile, subset of the <code>qodana.recommended</code> profile</td>
        <td>No configuration is required</td>
    </tr>
    <tr>
        <td><code>qodana.recommended</code></td>
        <td>Implements default profiles of JetBrains IDEs like <a href="https://www.jetbrains.com/help/idea/customizing-profiles.html">IntelliJ IDEA</a> and others. Contains 
        inspections for critical or severe issues in the codebase. Does not perform style checks and ignores 
        non-critical folders like <code>tests</code></td>
        <td>See <a anchor="profiles-set-up-a-qodana-profile"/></td>
    </tr>
</table>

Both profiles are hosted on [GitHub](https://github.com/JetBrains/qodana-profiles/tree/master/.idea/inspectionProfiles), so you can learn them in details.

You can override these profiles as explained in the [](#Custom+profiles) section.

### Set up a %product% profile
{id="profiles-set-up-a-qodana-profile"}

<link-summary>This explains how you can apply an existing %product% profile.</link-summary>

This section shows how you can apply the `qodana.recommended` profile. 

#### YAML file
{id="inspection-default-profiles-yaml-file"}

<!-- Add a link-summary here -->
<link-summary>YAML configuration is the universal method for applying an existing inspection profile.</link-summary>

Using [`qodana.yaml`](qodana-yaml.md) is the most convenient configuration method that you can apply across
all software products that run %product%. 

<procedure>
<step>In the root directory of your project, create the <code>qodana.yaml</code> file.</step>
<step><p>In the <code>qodana.yaml</code> file, save the following configuration:</p>
<code-block lang="yaml">
version: "1.0"
profile:
&nbsp;&nbsp;&nbsp;&nbsp;name: qodana.recommended
</code-block>
</step>
</procedure>

#### JetBrains IDE
{id="inspection-default-profiles-ide"}

If you have already configured the [`qodana.yaml`](#inspection-default-profiles-yaml-file) file, you can skip 
this step and [run Qodana](qodana-ide-plugin.md#ide-plugin-run-qodana). Otherwise, follow this procedure.

<procedure>
<step>
   <p>In your IDE, navigate to <ui-path>Tools | Qodana | Try Code Analysis with Qodana</ui-path>.</p> 
</step>
<step>
   <p>In the <ui-path>profile</ui-path> section of the <ui-path>Run Qodana</ui-path> dialog, replace the <code>qodana.starter</code> profile name with <code>qodana.recommended</code>.</p>
</step>
<step><p>In the lower part of the dialog, check the <ui-path>Save qodana.yaml to project root</ui-path> option.</p>
   <img src="ide-plugin-configure-profile.png" width="793" alt="Configuring a Qodana profile" border-effect="line"/>
</step>
<step>
    <p>Click <ui-path>Run</ui-path> for inspecting your code using the <code>qodana.recommended</code> profile.</p>
</step>
</procedure>

#### GitHub Actions
{id="inspection-default-profiles-github"}

If you have already configured the [`qodana.yaml`](#inspection-default-profiles-yaml-file) file, you can skip this step.
Otherwise, you can configure the [Qodana Scan](github.md) GitHub action as shown below.

<procedure>
    <step>On the <ui-path>Settings</ui-path> tab of the GitHub UI, create the <code>QODANA_TOKEN</code>
        <a href="https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository">encrypted secret</a>
        and save the <a href="cloud-projects.topic" anchor="cloud-manage-projects">project token</a> as its value.
    </step>
    <step>On the <ui-path>Actions</ui-path> tab of the GitHub UI, set up a new workflow and create the
        <code>.github/workflows/code_quality.yml</code> file.</step>
    <step>To inspect the <code>main</code> branch, release branches and the pull requests coming
    to your repository, save this workflow configuration to the <code>.github/workflows/code_quality.yml</code> file:
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
        <p>Here, the line <code>--profile-name</code> option specifies the <code>qodana.recommended</code> profile.</p>
    </step>
</procedure>

<!-- Are the Jenkins and GitLab config examples required here? -->

#### Local run
{id="inspection-default-profiles-local-run"}

If you have already configured the [`qodana.yaml`](#inspection-default-profiles-yaml-file) file, you can skip this step.
Otherwise, you can use `--profile-name` CLI option to configure the `qodana.recommended` profile.

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

## Custom profiles
{id="Custom+profiles"}

<link-summary>Learn how you can create custom Qodana configurations in the YAML and XML formats.</link-summary>

You can create your own profile either by overriding the existing [Qodana profiles](#Default+profiles) or creating it from
scratch. Currently, %product% supports the following formats: 

* [YAML format](custom-profiles.md) is the preferable format,
* [XML format](custom-xml-profiles.md) can be used as an alternative to YAML.

### Set up your profile

After you created your own profile, you can specify either the profile name or the path to the file containing it.

> If you run Qodana in a [CI/CD pipeline](ci.md), make sure the file containing the profile resides in the working
directory where the VCS stores your project before building it.
{style="note"}


#### YAML file
{id="inspection-custom-profiles-yaml-file"}

<!-- This needs to be tested -->

Using [`qodana.yaml`](qodana-yaml.md) is the most convenient configuration method that you can apply across
all software products that run %product%.

This is how you can use the profile name. Make sure that the profile file is contained
in the project root directory.

<procedure>
<step>In the root directory of your project, create the <code>qodana.yaml</code> file.</step>
<step><p>In the <code>qodana.yaml</code> file, save the following configuration:</p>
<code-block lang="yaml">
version: "1.0"
profile:
&nbsp;&nbsp;&nbsp;&nbsp;name: your.custom.profile.name
</code-block>
</step>
</procedure>

In case you would like to store the profile file somewhere outside the project directory, you can specify the path to it:

<procedure>
<step>In the root directory of your project, create the <code>qodana.yaml</code> file.</step>
<step><p>In the <code>qodana.yaml</code> file, save the following configuration:</p>
<code-block lang="yaml">
version: "1.0"
profile:
&nbsp;&nbsp;&nbsp;&nbsp;path: relative/path/to/the/profile
</code-block>
</step>
</procedure>


#### Local run
{id="inspection-custom-profiles-local-run"}

To run %instance% with a custom profile, use its actual profile name. This command lets you bind a
custom profile:

<tabs group="cli-settings" filter="for-inspection-profiles">
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$">
            docker run \
               -v $(pwd):/data/project/ \
               -v &lt;path-to-profile-file&gt;/&lt;file-name&gt;:/data/project/.idea/inspectionProfiles/&lt;file-name&gt; \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               jetbrains/qodana-&lt;linter&gt; \
               --profile-name &lt;profile-name-from-file&gt;
        </code-block>
    </tab>
    <tab title="Qodana CLI" group-key="qodana-cli">
        <code-block lang="shell" prompt="$">
            qodana scan \
               -v &lt;path-to-profile-file&gt;/&lt;file-name&gt;:/data/project/.idea/inspectionProfiles/&lt;file-name&gt; \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               --profile-name &lt;profile-name-from-file&gt;
        </code-block>
    </tab>
</tabs>

The `--profile-path` CLI option lets you override the path to the file containing the profile.

This command lets you bind the file to the profile directory, and the `--profile-path` option tells %instance% which
profile file to read:

<tabs group="cli-settings">
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$">
            docker run \
               -v $(pwd):/data/project/ \
               -v &lt;path-to-profile-file&gt;/&lt;file-name&gt;:/data/project/myprofiles/&lt;file-name&gt; \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               jetbrains/qodana-&lt;linter&gt; \
               --profile-path /data/project/myprofiles/&lt;file-name&gt;
        </code-block>
    </tab>
    <tab title="Qodana CLI" group-key="qodana-cli">
        <code-block lang="shell" prompt="$">
            qodana scan \
               -v &lt;path-to-profile-file&gt;/&lt;file-name&gt;:/data/project/myprofiles/&lt;file-name&gt; \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               --profile-path /data/project/myprofiles/&lt;file-name&gt;
        </code-block>
    </tab>
</tabs>
