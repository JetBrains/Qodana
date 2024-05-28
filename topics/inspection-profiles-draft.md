[//]: # (title: Inspection profiles)

<no-index/>

<show-structure for="chapter" depth="3"/>

<var name="code-inspection-profiles-ide-help-url" value="https://www.jetbrains.com/help/idea/?Customizing_Profiles"/>
<var name="ide" value="IDE"/>
<var name="qodana.recommended" value="https://github.com/JetBrains/qodana-profiles/blob/master/.idea/inspectionProfiles/qodana.recommended.yaml"/>
<var name="java-glob" value="https://docs.oracle.com/javase/8/docs/api/java/nio/file/FileSystem.html#getPathMatcher-java.lang.String-"/>

<link-summary>Inspection profiles configure inspections, file scopes that these inspections analyze, 
and severities.</link-summary>

Inspection profiles define [inspections](code-inspections.topic), file scopes that these inspections analyze, and 
[severities](troubleshooting.topic#troubleshooting-severities).

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
        <td><p>Implements default profiles of JetBrains IDEs like 
        <a href="https://www.jetbrains.com/help/idea/customizing-profiles.html">IntelliJ IDEA</a> with the following 
        exceptions:</p> 
        <list>
            <li>
                By default, Qodana provides analysis only for specific languages and frameworks. This means that, for 
                example, Groovy or JavaScript inspections are available but disabled by default. Inspections
                of the <code>INFORMATION</code> <a href="troubleshooting.topic" anchor="troubleshooting-severities">IDE severity</a> 
                are also disabled.</li>
            <li>
                Several inspections that affect code highlighting in IDEs and global inspections were removed from %product% linters.  
            </li>
            <li>
                Flaky inspections that are still available in IDEs were removed from %product% linters.
            </li>
        </list>
        </td>
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

The [`qodana.yaml`](qodana-yaml.md) file is the universal configuration method that you can use across
all software products. 

<procedure>
<step>In the root directory of your project, create the <code>qodana.yaml</code> file.</step>
<step><p>In the <code>qodana.yaml</code> file, save the following configuration:</p>
<code-block lang="yaml">
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
   <p>In the <ui-path>profile</ui-path> section of the <ui-path>Run Qodana</ui-path> dialog, replace this block:</p> 
<code-block lang="yaml">
profile:
&nbsp;&nbsp;name: qodana.starter
</code-block> 
<p>with:</p>
<code-block lang="yaml">
profile:
&nbsp;&nbsp;name: qodana.recommended
</code-block> 
   <img src="ide-plugin-configure-profile.png" width="793" alt="Configuring a Qodana profile" border-effect="line"/>
</step>
<step><p>Below the configuration field, check the <ui-path>Save qodana.yaml in project root</ui-path> option.</p>
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

After you created your own profile, you can specify a relative path to the file containing it. The recommendation is to
store custom profile configurations inside the `.qodana` directory of your project root because %product% does not
analyze this directory.

> If you run Qodana in a [CI/CD pipeline](ci.md), make sure the file containing the profile resides in the working
directory where the VCS stores your project before building it.
{style="note"}

#### YAML file
{id="inspection-custom-profiles-yaml-file"}

The [`qodana.yaml`](qodana-yaml.md) file is the universal configuration method that you can use across
all software products.

<procedure>
<step>In the root directory of your project, create the <code>qodana.yaml</code> file.</step>
<step><p>In the <code>qodana.yaml</code> file, save the following configuration:</p>
<code-block lang="yaml">
profile:
&nbsp;&nbsp;&nbsp;&nbsp;path: .qodana/&lt;custom-profile.yaml&gt;
</code-block>
</step>
</procedure>

#### JetBrains IDE
{id="inspection-custom-profiles-ide"}

If you have already configured the [`qodana.yaml`](#inspection-default-profiles-yaml-file) file, you can skip
this step and [run Qodana](qodana-ide-plugin.md#ide-plugin-run-qodana). Otherwise, follow this procedure.

<procedure>
<step>
   <p>In your IDE, navigate to <ui-path>Tools | Qodana | Try Code Analysis with Qodana</ui-path>.</p> 
</step>
<step>
   <p>In the <ui-path>profile</ui-path> section of the <ui-path>Run Qodana</ui-path> dialog, replace this block: </p>
<code-block lang="yaml">
    profile:
    &nbsp;&nbsp;name: qodana.starter
</code-block> 
<p>with:</p>
<code-block lang="yaml">
    profile:
    &nbsp;&nbsp;path: .qodana/&lt;custom-profile.yaml&gt;
</code-block> 
   <img src="ide-plugin-configure-profile-2.png" width="793" alt="Configuring a Qodana profile" border-effect="line"/>
</step>
<step><p>In the lower part of the dialog, check the <ui-path>Save qodana.yaml in project root</ui-path> option.</p>
</step>
<step>
    <p>Click <ui-path>Run</ui-path> for inspecting your code using the <code>qodana.recommended</code> profile.</p>
</step>
</procedure>

#### GitHub Actions
{id="inspection-custom-profiles-github"}

If you have already configured the [`qodana.yaml`](#inspection-custom-profiles-yaml-file) file, you can skip this step.
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
                      args: --profile-path,.qodana/&lt;custom-profile.yaml&gt;
                    env:
                      QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
        </code-block>
        <p>Here, the line <code>--profile-path</code> option specifies the relative path to the profile.</p>
    </step>
</procedure>

#### Local run
{id="inspection-custom-profiles-local-run"}

If you have already configured the [`qodana.yaml`](#inspection-custom-profiles-yaml-file) file, you can skip this step and
run %product% without additional configuration options. Otherwise, you can use the `--profile-path` option to specify 
the relative path to the directory containing the profile.

<!-- This needs to be tested once more -->

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