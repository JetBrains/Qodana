# Configuration reference

<no-index/>

<show-structure for="chapter" depth="3"/>

<var name="code-inspection-profiles-ide-help-url" value="https://www.jetbrains.com/help/idea/?Customizing_Profiles"/>
<var name="ide" value="IDE"/>
<var name="incorrect-formatting" value="https://www.jetbrains.com/help/inspectopedia/IncorrectFormatting.html"/>

## Introduction

<link-summary>You can configure Qodana via a YAML-formatted file. By default, this file should have the qodana.yaml 
name and be contained in the root directory of your project.</link-summary>

You can configure %product% using YAML or command-line (CLI) options.

Configuring %product% via a YAML-formatted file typically named `qodana.yaml` and contained in the
root directory of your project is suitable for settings that require lengthy commands. For example, inspection configuration, 
[bootstrap](#Run+custom+commands), and other settings that are not convenient to configure otherwise.
Once a YAML configuration is saved, you can reuse it across different instances of Qodana.

CLI options are suitable for immediate configuration of applications that run %product% like the Docker engine,
[Qodana CLI](Quick-start.topic#quickstart-run-using-cli), [IDEs](ide-integration.md), and [CI/CD tools](ci.md). 
Besides that, some CLI options do not have YAML equivalents.

You can configure [linter](linters.md) and [quality gates](quality-gate.topic) via both YAML and CLI.
In such cases, CLI options take precedence over their YAML equivalents if both methods are used.

<note>The <a href="pricing.md" anchor="pricing-linters-licenses">Ultimate and Ultimate Plus</a> linters require the
    <code>QODANA_TOKEN</code> variable to refer to a <a href="project-token.md">project token</a>. Community linters only require a 
    <code>QODANA_TOKEN</code> to view analysis reports in %cloud%.</note>

### YAML configuration

<note>
The configuration saved in the <code>qodana.yaml</code> file affects only %product% linters and does not impact other 
products, such as IntelliJ IDEA or PhpStorm.
</note>

<warning>
It is highly recommended not to store tokens, passwords, or any other secret information in the <code>qodana.yaml</code> file.
</warning>

By default, this configuration capability will be referred to as the `qodana.yaml` configuration.
To start, in the root directory of your project save the `qodana.yaml` file. 

To override the `qodana.yaml` filename and its location, follow the recommendations of the [](#docker-config-reference-custom-yaml-config) chapter.

The JSON schema for `qodana.yaml` is published in the [SchemaStore](https://www.schemastore.org/qodana-1.0.json) project, which provides completion and basic validation in IDEs.

<!--Configurations applied in `qodana.yaml` override the default inspection profile settings and default configurations of
Qodana linters, you can configure it using the [HTML report](ui-overview.md) section, and all changes will be applied
automatically. -->

### CLI options

> The comprehensive list of CLI options is available in the [](docker-image-configuration.topic) section.

<p>You can configure %product% using three types of CLI options as shown below.</p>

<table>
    <tr>
        <td>Option type</td>
        <td>Example</td>
    </tr>
    <tr>
        <td>Requires the equal sign (<code>=</code>) between the option name and its argument</td>
        <td><code>--property=idea.log.config.file=info.xml</code></td>
    </tr>
    <tr>
        <td>Requires the space character (<code> </code>) between the option name and its argument</td>
        <td><code>--baseline /path/to/sarif/file</code></td>
    </tr>
    <tr>
        <td>Requires no argument</td>
        <td><code>--apply-fixes</code></td>
    </tr>
</table>

<p>Here are the examples that invoke all these option types:</p>

<tabs group="cli-settings">
    <tab title="Docker image" group-key="docker-image">
    <code-block lang="shell" prompt="$" emphasize-lines="5-7">
        docker run \
           -v $(pwd):/data/project/ \
           -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
           &lt;image-name&gt; \
           --property=idea.log.config.file=info.xml \
           --baseline &lt;baseline-path&gt; \
           --apply-fixes
    </code-block>
    </tab>
    <tab title="Qodana CLI" group-key="qodana-cli">
    <code-block lang="shell" prompt="$" emphasize-lines="3-5">
        qodana scan \
           -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
           --property=idea.log.config.file=info.xml \
           --baseline &lt;baseline-path&gt; \
           --apply-fixes
    </code-block>
    </tab>
    <tab title="GitHub Actions" group-key="github-actions">
    <code-block lang="yaml" emphasize-lines="26-28">
        name: Qodana
        on:
            workflow_dispatch:
            pull_request:
            push:
                branches: # Specify your branches here
                    - main # The 'main' branch
                    - master # The 'master' branch
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
                      uses: %action-version%
                      with:
                          args: |
                              --property=idea.log.config.file=info.xml
                              --baseline &lt;baseline-path&gt;
                              --apply-fixes
                      env:
                          QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
    </code-block>
    </tab>
    <tab title="Jenkins" group-key="jenkins">
        <code-block lang="groovy" emphasize-lines="19-21">
            pipeline {
                environment {
                    QODANA_TOKEN=credentials('qodana-token')
                }
                agent {
                    docker {
                        args '''
                          -v "${WORKSPACE}":/data/project
                          --entrypoint=""
                          '''
                        image 'jetbrains/qodana-&lt;image&gt;'
                    }
                }
                stages {
                    stage('Qodana') {
                        steps {
                            sh '''
                            qodana \
                            --property=idea.log.config.file=info.xml \
                            --baseline &lt;baseline-path&gt; \
                            --apply-fixes
                            '''
                        }
                    }
                }
            }
        </code-block>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
        <code-block lang="yaml" emphasize-lines="5-7">
            include:
                - component: %gitlab-version%
                  inputs:
                      args: |
                          --property=idea.log.config.file=info.xml
                          --baseline &lt;baseline-path&gt;
                          --apply-fixes
                          --image &lt;image&gt;
        </code-block>
    </tab>
    <tab title="TeamCity" group-key="teamcity">
        <p>In the runner configuration, find the <ui-path>Additional Qodana arguments</ui-path> field and
            specify the path to the plugin file:</p>
        <code-block lang="shell">
            --property=idea.log.config.file=info.xml --baseline &lt;baseline-path&gt; --apply-fixes
        </code-block>
    </tab>
</tabs>

## Run custom commands

<link-summary>Using the bootstrap key of qodana.yaml, %instance% can perform actions before running analysis.</link-summary>

> Some commands may require root user privileges. For more details, see the
> [](#docker-config-reference-docker-environment-run-non-root) chapter.
> {style="tip"}

During analyses, %product% linters may report that some inspections cannot find classes, packages, files or cannot resolve references,
although linters related to [JVM](jvm.md), [.NET,](dotnet.md) and [Golang](golang.md) try to figure out the
build system and project structure automatically. In these cases, %instance% needs a bit of help:

* Install third-party packages or libraries
* Run a program that sets up the build environment

These actions are carried out using the `bootstrap` key:

```yaml
version: "1.0"

linter: <linter>

bootstrap: |+
  set -eu
  # For PHP projects that use Laravel:
  #composer require --dev barryvdh/laravel-ide-helper

  # For JavaScript projects that use Node.js:
  #npm install

  # For Python projects
  #pip install -r requirements.txt 
```

> You can investigate %product% behavior using files contained in the
> [`/data/results`](#docker-config-reference-overview-logs) directory.

> The sanity inspection will report unexpected problems in case the `qodana.yaml` file
> containing the `bootstrap` key is missing from your project directory. You can disable this inspection using the
> `--disable-sanity` option, or add this inspection to a [baseline](baseline.topic).
> {style="note"}


To be able to use syntax highlighting and validation in your IDE, you can create the `prepare-qodana.sh` shell script
and save it in the root directory of your project:

```shell
#! /bin/sh

set -eu

# For PHP projects that use Laravel:
#composer require --dev barryvdh/laravel-ide-helper

# For JavaScript projects that use Node.js:
#npm install
```

Run the script in a %instance% Docker container using the `bootstrap` key:

```shell
bootstrap: sh ./prepare-qodana.sh
```

To run %product% as the root user, you may need to invoke the ` --user=root` [option](docker-image-configuration.topic#docker-config-reference-qodana-scan).

In CI/CD environments like GitLab CI/CD, you may need to prepare a complex environment before the analysis starts.
Here is an example of a monorepo setup with a `frontend` directory (Node.js) and a `backend` directory (C#):

```yaml
version: "1.0"

linter: %dotnet-linter%

bootstrap: |+
  set -eu

  # Install frontend dependencies
  echo "Installing frontend dependencies..."
  cd frontend && npm install && cd ..

  # Build backend C# projects
  echo "Building C# projects..."
  dotnet restore backend/MySolution.sln
  dotnet build backend/MySolution.sln --no-restore
```

You can also see the [](monorepo-project.md) section.

## Specify a linter

<link-summary>You can specify a linter that you are going to employ.</link-summary>

Using the `linter` YAML key, you can specify a [linter](linters.md) that you are going to employ. For example:

```yaml
version: "1.0"

linter: %jvm-co-a-linter%
```

Alternatively, you can use the `--linter` CLI option as shown below:

<tabs group="cli-settings">
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$" emphasize-lines="5"><![CDATA[
            docker run \
               -v $(pwd):/data/project/ \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               jetbrains/qodana-&lt;image&gt; \
               --linter <linter>
        ]]>
</code-block>
    </tab>
    <tab title="Qodana CLI" group-key="qodana-cli">
        <code-block lang="shell" prompt="$" emphasize-lines="3"><![CDATA[
            qodana scan \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               --linter <linter>
        ]]>
</code-block>
    </tab>
    <tab title="GitHub Actions" group-key="github-actions">
        <code-block lang="yaml" emphasize-lines="25"><![CDATA[
            name: Qodana
            on:
                workflow_dispatch:
                pull_request:
                push:
                    branches: # Specify your branches here
                        - main # The 'main' branch
                        - master # The 'master' branch
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
                          uses: %action-version%
                          with:
                              args: --linter <linter>
                          env:
                              QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
        ]]>
</code-block>
    </tab>
    <tab title="Jenkins" group-key="jenkins">
            <code-block lang="groovy" emphasize-lines="19"><![CDATA[
                pipeline {
                    environment {
                        QODANA_TOKEN=credentials('qodana-token')
                    }
                    agent {
                        docker {
                            args '''
                              -v "${WORKSPACE}":/data/project
                              --entrypoint=""
                              '''
                            image 'jetbrains/qodana-&lt;image&gt;'
                        }
                    }
                    stages {
                        stage('Qodana') {
                            steps {
                                sh '''
                                qodana \
                                --linter <linter>
                                '''
                            }
                        }
                    }
                }
            ]]>
</code-block>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
            <code-block lang="yaml" emphasize-lines="5"><![CDATA[
                include:
                    - component: %gitlab-version%
                      inputs:
                          args: |
                              --linter <linter>
            ]]>
</code-block>
    </tab>
    <tab title="TeamCity" group-key="teamcity">
        <p>In the runner configuration, find the <ui-path>Additional Qodana arguments</ui-path> field and
            specify the script:</p>
        <code-block lang="shell"><![CDATA[
                --linter <linter>
            ]]>
</code-block>
    </tab>
</tabs>

## Configure native mode

The native mode lets you run %product% without the Docker engine and is available for the following [linters](linters.md):

<table>
    <tr>
        <td>
            Linter name
        </td>
        <td>
            Description
        </td>
    </tr>
    <tr>
        <td>
            <code>%jvm-linter%</code>
        </td>
        <td>
            <a href="jvm.md">%jvm%</a>
        </td>
    </tr>
    <tr>
        <td>
            <code>%jvm-co-linter%</code>
        </td>
        <td>
            <a href="jvm.md">%jvm-co%</a>
        </td>
    </tr>
    <tr>
        <td>
            <code>%php-linter%</code>
        </td>
        <td>
            <a href="php.md">%php%</a>
        </td>
    </tr>
    <tr>
        <td>
            <code>%js-linter%</code>
        </td>
        <td>
            <a href="js.md">%js%</a>
        </td>
    </tr>
    <tr>
        <td>
            <code>%dotnet-linter%</code>
        </td>
        <td>
            <a href="dotnet.md">%dotnet%</a>
        </td>
    </tr>
    <tr>
        <td>
            <code>%go-linter%</code>
        </td>
        <td>
            <a href="golang.md">%go%</a>
        </td>
    </tr>
    <tr>
        <td>
            <code>%python-linter%</code>
        </td>
        <td>
            <a href="python.md">%python%</a>
        </td>
    </tr>
    <tr>
        <td>
            <code>%python-co-linter%</code>
        </td>
        <td>
            <a href="python.md">%python-co%</a>
        </td>
    </tr>
    <!--<tr>
        <td>
            <code>qodana-cpp:2025.2-eap</code>
        </td>
        <td>
            <a href="clang.md">%clang%</a>
        </td>
    </tr>-->
</table>

You can configure [native mode](deploy-qodana.md#deploy-qodana-native-mode) by specifying a [linter](linters.md), as well as 
set the `withinDocker` setting to `false`. 

In case of a YAML configuration, this may look as follows:

```yaml
version: "1.0"

linter: <linter-name>

withinDocker: false # Setting Docker mode to false
```

> The `ide` notation available in previous versions of %product% is deprecated and will be removed in future versions of the product.
> {style="note"}

The `--linter` and `--within-docker false` CLI options also let you configure the native mode:

<tabs group="cli-settings">
    <tab title="Qodana CLI" group-key="qodana-cli">
        <code-block lang="shell" prompt="$" emphasize-lines="3-4"><![CDATA[
            qodana scan \
               -e QODANA_TOKEN="<cloud-project-token>" \
               --linter <linter> \
               --within-docker false    
        ]]>
</code-block>
    </tab>
    <tab title="GitHub Actions" group-key="github-actions">
        <code-block lang="yaml" emphasize-lines="26-27"><![CDATA[
            name: Qodana
            on:
                workflow_dispatch:
                pull_request:
                push:
                    branches: # Specify your branches here
                        - main # The 'main' branch
                        - master # The 'master' branch
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
                          uses: %action-version%
                          with:
                              args: |
                                --linter <linter>
                                --within-docker false
                          env:
                              QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
        ]]>
</code-block>
    </tab>
</tabs>

## Override YAML configuration file
{id="docker-config-reference-custom-yaml-config"}

<link-summary>You can save %product% settings in your custom YAML-formatted file. You can then invoke this file
    using the --config option and a path to a file relative to the project root.</link-summary>

<p>Your project can have several %product% configurations contained in
    YAML-formatted files. This comes in handy if you analyze monorepo projects or
    run a single CI job.</p>

<p>You can use the <code>--config</code> CLI option and a path
to a file relative to the project root:</p>
<tabs group="cli-settings">
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$" emphasize-lines="5">
            docker run \
            &nbsp;&nbsp;&nbsp;-v $(pwd):/data/project \
            &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
            &nbsp;&nbsp;&nbsp;jetbrains/qodana-&lt;image&gt; \
            &nbsp;&nbsp;&nbsp;--config relative/path/to/config.yaml
        </code-block>
    </tab>
    <tab title="Qodana CLI" group-key="qodana-cli">
        <code-block lang="shell" prompt="$" emphasize-lines="3">
        qodana scan \
        &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
        &nbsp;&nbsp;&nbsp;--config relative/path/to/config.yaml
        </code-block>
    </tab>
    <tab title="GitHub Actions" group-key="github-actions">
        <code-block lang="yaml" emphasize-lines="25">
            name: Qodana
            on:
                workflow_dispatch:
                pull_request:
                push:
                    branches: # Specify your branches here
                        - main # The 'main' branch
                        - master # The 'master' branch
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
                          uses: %action-version%
                          with:
                              args: --config relative/path/to/config.yaml
                          env:
                              QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
        </code-block>
    </tab>
    <tab title="Jenkins" group-key="jenkins">
            <code-block lang="groovy" emphasize-lines="19">
                pipeline {
                    environment {
                        QODANA_TOKEN=credentials('qodana-token')
                    }
                    agent {
                        docker {
                            args '''
                              -v "${WORKSPACE}":/data/project
                              --entrypoint=""
                              '''
                            image 'jetbrains/qodana-&lt;image&gt;'
                        }
                    }
                    stages {
                        stage('Qodana') {
                            steps {
                                sh '''
                                qodana \
                                --config relative/path/to/config.yaml
                                '''
                            }
                        }
                    }
                }
            </code-block>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
            <code-block lang="yaml" emphasize-lines="5">
                include:
                    - component: %gitlab-version%
                      inputs:
                          args: |
                              --config relative/path/to/config.yaml
                              --linter &lt;linter&gt;
            </code-block>
    </tab>
    <tab title="TeamCity" group-key="teamcity">
        <p>In the runner configuration, find the <ui-path>Additional Qodana arguments</ui-path> field and
            specify the path to your custom configuration file:</p>
        <code-block lang="shell">
                --config relative/path/to/config.yaml
            </code-block>
    </tab>
</tabs>

## Inspection profile
{id="configuration-reference-inspection-profile"}

<link-summary>Learn more about available profile-related %product% options.</link-summary>

By default, %instance% analyzes your code using the `qodana.starter` profile.
You can switch to another existing profile using the recommendations from the [](inspection-profiles.md#inspection-profiles-existing-profiles) chapter. 
To set up your own profile, use available configuration options described in the [](inspection-profiles.md#inspection-profiles-custom-profiles) chapter.

### YAML configuration
{id="configuration-reference-inspection-profile-yaml-configuration"}

Using the `profile` YAML key, you can import an existing configuration from a dedicated file, as well as customize the configuration once it is imported:

<tabs>
<tab title="Invoking by profile name">
<p>Use the <code>profile.path</code> key to invoke an existing profile by its name, for example:</p>
    <code-block lang="yaml" emphasize-lines="5-6"><![CDATA[
        version: "1.0"

        linter: <linter>
    
        profile:
            name: qodana.recommended
            inspections: # Configuring the invoked profile
                — group: "category:Java/Probable bugs"
                  enabled: true # Enabling the inspection category
                — inspection: RedundantIf
                  enabled: false # Disabling the inspection
        ]]>
    </code-block>
</tab>
<tab title="Importing from dedicated profiles">
<p>After you set up a profile in a dedicated file as described in the <a href="inspection-profiles.md"/> section, you can
invoke it in the <code>qodana.yaml</code> file using the <code>profile.path</code> key, for example:</p>
    <code-block lang="yaml" emphasize-lines="5-6"><![CDATA[
        version: "1.0"
        
        linter: <linter>
    
        profile:
            path: .qodana/profiles/<custom-profile.yaml>
            inspections: # Configuring the invoked profile
                — group: "category:Java/Probable bugs"
                  enabled: true # Enabling the inspection category
                — inspection: RedundantIf
                  enabled: false # Disabling the inspection
        ]]>
    </code-block>
</tab>
</tabs>

### CLI options
{id="configuration-reference-inspection-profile-cli-options"}

You can use the following profile-related CLI options:

<table>
    <tr>
        <td>Option</td>
        <td>Description</td>
        <td>Default setting</td>
    </tr>
    <tr>
        <td><code>--disable-sanity</code></td>
        <td>Skip running the inspections configured by the <a href="inspection-profiles.md" anchor="inspection-profiles-existing-profiles"><code>qodana.sanity</code></a> profile</td>
        <td>Enabled</td>
    </tr>
    <tr>
        <td><code>-n</code>, <code>--profile-name</code></td>
        <td><p>The profile name from the list of 
            <a href="inspection-profiles.md" anchor="inspection-profiles-existing-profiles">existing %instance% profiles</a>.</p> 
            <p>Alternatively, you can use a profile name from a custom profile
            file. To do it, you will need to mount a profile file to %product%.</p>
        </td>
        <td><code>qodana.starter</code></td>
    </tr>
    <tr>
        <td><code>-p</code>, <code>--profile-path</code></td>
        <td>
            <p>The absolute path to the profile file.</p>
        </td>
        <td>None</td>
    </tr>
    <tr>
        <td><code>--run-promo</code></td>
        <td><p>Run promo inspections as a part of the <code>qodana.starter</code> profile</p>
            <note>This option is not available in the <a href="dotnet.md">%dotnet%</a> linter.</note>
        </td>
        <td>Enabled only if %instance% is configured for the <code>qodana.starter</code> profile, and the <code>--run-promo true</code> option is invoked</td>
    </tr>
</table>

Below are the configuration snippets containing the `-profile-name` option for invoking a profile by its name, 
as well as the `--profile-path` CLI option for invoking a profile configuration from a dedicated file:

<tabs group="cli-settings" filter="for-inspection-profiles">
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$" emphasize-lines="5-7"><![CDATA[
            docker run \
               -v $(pwd):/data/project/ \
               -e QODANA_TOKEN="<cloud-project-token>" \
               jetbrains/qodana-<image> \
               -v <path-to-profile-file> \ # Mount the file containing custom profile
               --profile-name qodana.recommended | <profile-name-from-file> \ # Existing profile name | Name from mounted file 
               --profile-path /data/project/myprofiles/<file-name> # Importing profile file
        ]]>
</code-block>
    </tab>
    <tab title="Qodana CLI" group-key="qodana-cli">
        <code-block lang="shell" prompt="$" emphasize-lines="3-5"><![CDATA[
            qodana scan \
               -e QODANA_TOKEN="<cloud-project-token>" \
               -v <path-to-profile-file> \ # Mount the file containing custom profile
               --profile-name qodana.recommended | <profile-name-from-file> \ # Existing profile name | Name from mounted file
               --profile-path /data/project/myprofiles/<file-name> # Importing profile file
        ]]>
</code-block>
    </tab>
    <tab title="GitHub Actions" group-key="github-actions">
    <code-block lang="yaml" emphasize-lines="26-28"><![CDATA[
        name: Qodana
        on:
            workflow_dispatch:
            pull_request:
            push:
                branches: # Specify your branches here
                    - main # The 'main' branch
                    - master # The 'master' branch
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
                      uses: %action-version%
                      with:
                          args: |
                            -v <path-to-profile-file> # Mount the file containing custom profile
                            --profile-name qodana.recommended | <profile-name-from-file> # Existing profile name | Name from mounted file
                            --profile-path /data/project/myprofiles/<file-name> # Importing profile file
                      env:
                          QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
    ]]>
</code-block>
    </tab>
    <tab title="Jenkins" group-key="jenkins">
        <code-block lang="groovy" emphasize-lines="19-21"><![CDATA[
            pipeline {
                environment {
                    QODANA_TOKEN=credentials('qodana-token')
                }
                agent {
                    docker {
                        args '''
                          -v "${WORKSPACE}":/data/project
                          -v <path-to-profile-file> // Mount the file containing custom profile
                          --entrypoint=""
                          '''
                        image 'jetbrains/qodana-<image>
                    }
                }
                stages {
                    stage('Qodana') {
                        steps {
                            sh '''
                            qodana \
                                --profile-name qodana.recommended | <profile-name-from-file> // Existing profile name | Name from mounted file
                                --profile-path /data/project/myprofiles/<file-name> // Importing profile file
                            '''
                        }
                    }
                }
            }
        ]]>
</code-block>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
        <code-block lang="yaml" emphasize-lines="6-8"><![CDATA[
            include:
                - component: %gitlab-version%
                  inputs:
                      args: |
                          --linter <linter>
                          -v <path-to-profile-file> \ # Mount the file containing custom profile
                          --profile-name qodana.recommended | <profile-name-from-file> \ # Existing profile name | Name from mounted file
                          --profile-path /data/project/myprofiles/<file-name> # Importing profile file
        ]]>
</code-block>
    </tab>
    <tab title="TeamCity" group-key="teamcity">
        <p>Configure the runner as described in the <a href="teamcity.md" anchor="teamcity-qodana-runner"/> chapter.</p>
    </tab>
</tabs>

<!--<p filter="for-inspection-profiles">To run %instance% with a custom profile, use its actual
    profile name.</p>

<p filter="for-inspection-profiles">The following lets you bind a custom profile:</p>

<tabs group="cli-settings" filter="for-inspection-profiles">
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$">
            docker run \
               -v $(pwd):/data/project/ \
               -v &lt;path-to-profile-file&gt;/&lt;file-name&gt;:/data/project/.idea/inspectionProfiles/&lt;file-name&gt; \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               jetbrains/qodana-&lt;image&gt; \
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
    <tab title="GitHub Actions" group-key="github-actions">
    <code-block lang="yaml">
        name: Qodana
        on:
            workflow_dispatch:
            pull_request:
            push:
                branches: # Specify your branches here
                    - main # The 'main' branch
                    - master # The 'master' branch
                    - 'releases/*' # The release branches
            &nbsp;
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
                      uses: %action-version%
                      with:
                          args: --profile-name &lt;profile-name-from-file&gt;
                      env:
                          QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
    </code-block>
    </tab>
    <tab title="Jenkins" group-key="jenkins">
        <code-block lang="groovy">
            pipeline {
                environment {
                    QODANA_TOKEN=credentials('qodana-token')
                }
                agent {
                    docker {
                        args '''
                          -v "${WORKSPACE}":/data/project
                          --entrypoint=""
                          '''
                        image 'jetbrains/qodana-&lt;image&gt;'
                    }
                }
                stages {
                    stage('Qodana') {
                        steps {
                            sh '''
                            qodana \
                            --profile-name &lt;profile-name-from-file&gt;
                            '''
                        }
                    }
                }
            }
        </code-block>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
        <code-block lang="yaml">
            include:
                - component: %gitlab-version%
                  inputs:
                      args: |
                          --profile-name &lt;profile-name-from-file&gt;
                          --linter &lt;linter&gt;
        </code-block>
    </tab>
    <tab title="TeamCity" group-key="teamcity">
        <p>In the runner configuration, find the <ui-path>Additional Qodana arguments</ui-path> field and
            specify the custom profile name:</p>
        <code-block lang="shell">
            --profile-name &lt;profile-name-from-file&gt;
        </code-block>
    </tab>
</tabs>

#### Profile path
{id="docker-config-reference-profile-profile-path"}

<p>The <code>--profile-path</code> option lets you override the path to the file containing the profile.</p>

<tip>You can also configure this option using the <a href="inspection-profiles.md" anchor="inspection-profiles-yaml-file"><code>qodana.yaml</code></a> file.</tip>

<p>This command lets you bind the file to the profile directory,
    and the <code>--profile-path</code> option tells %instance% which profile file to read:</p>

<tabs group="cli-settings">
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$">
            docker run \
               -v $(pwd):/data/project/ \
               -v &lt;path-to-profile-file&gt;/&lt;file-name&gt;:/data/project/myprofiles/&lt;file-name&gt; \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               jetbrains/qodana-&lt;image&gt; \
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
    <tab title="GitHub Actions" group-key="github-actions">
    <code-block lang="yaml">
        name: Qodana
        on:
            workflow_dispatch:
            pull_request:
            push:
                branches: # Specify your branches here
                    - main # The 'main' branch
                    - master # The 'master' branch
                    - 'releases/*' # The release branches
            &nbsp;
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
                      uses: %action-version%
                      with:
                          args: --profile-path /data/project/myprofiles/&lt;file-name&gt;
                      env:
                          QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
    </code-block>
    </tab>
    <tab title="Jenkins" group-key="jenkins">
        <code-block lang="groovy">
            pipeline {
                environment {
                    QODANA_TOKEN=credentials('qodana-token')
                }
                agent {
                    docker {
                        args '''
                          -v "${WORKSPACE}":/data/project
                          --entrypoint=""
                          '''
                        image 'jetbrains/qodana-&lt;image&gt;'
                    }
                }
                stages {
                    stage('Qodana') {
                        steps {
                            sh '''
                            qodana \
                            --profile-path /data/project/myprofiles/&lt;file-name&gt;
                            '''
                        }
                    }
                }
            }
        </code-block>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
        <code-block lang="yaml">
            include:
                - component: %gitlab-version%
                  inputs:
                      args: |
                          --profile-path /data/project/myprofiles/&lt;file-name&gt;
                          --linter &lt;linter&gt;
        </code-block>
    </tab>
    <tab title="TeamCity" group-key="teamcity">
        <p>In the runner configuration, find the <ui-path>Additional Qodana arguments</ui-path> field and
            specify the path your custom profile:</p>
        <code-block lang="shell">
            --profile-path /data/project/myprofiles/&lt;file-name&gt;
        </code-block>
    </tab>
</tabs>-->

### Disable sanity inspections

<link-summary>By default, sanity inspections are enabled in %instance%, but you can disable them.</link-summary>

Sanity problems refer to problems in the project configuration. By default, sanity inspections are enabled in %instance%. You can disable them using this snippet:

```yaml
version: "1.0"

linter: <linter>

disableSanityInspections: true
```

Alternatively, you can use the `--disable-sanity` CLI option: 

<tabs group="cli-settings">
    <tab title="Docker image" group-key="docker-image">
    <code-block lang="shell" prompt="$" emphasize-lines="5">
        docker run \
           -v $(pwd):/data/project/ \
           -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
           &lt;image-name&gt; \
           --disable-sanity
    </code-block>
    </tab>
    <tab title="Qodana CLI" group-key="qodana-cli">
    <code-block lang="shell" prompt="$" emphasize-lines="3">
        qodana scan \
           -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
           --disable-sanity
    </code-block>
    </tab>
    <tab title="GitHub Actions" group-key="github-actions">
    <code-block lang="yaml" emphasize-lines="26">
        name: Qodana
        on:
            workflow_dispatch:
            pull_request:
            push:
                branches: # Specify your branches here
                    - main # The 'main' branch
                    - master # The 'master' branch
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
                      uses: %action-version%
                      with:
                          args: |
                              --disable-sanity
                      env:
                          QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
    </code-block>
    </tab>
    <tab title="Jenkins" group-key="jenkins">
        <code-block lang="groovy" emphasize-lines="19">
            pipeline {
                environment {
                    QODANA_TOKEN=credentials('qodana-token')
                }
                agent {
                    docker {
                        args '''
                          -v "${WORKSPACE}":/data/project
                          --entrypoint=""
                          '''
                        image 'jetbrains/qodana-&lt;image&gt;'
                    }
                }
                stages {
                    stage('Qodana') {
                        steps {
                            sh '''
                            qodana \
                            --disable-sanity
                            '''
                        }
                    }
                }
            }
        </code-block>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
        <code-block lang="yaml" emphasize-lines="5">
            include:
                - component: %gitlab-version%
                  inputs:
                      args: |
                          --disable-sanity
                          --image &lt;image&gt;
        </code-block>
    </tab>
    <tab title="TeamCity" group-key="teamcity">
        <p>In the runner configuration, find the <ui-path>Additional Qodana arguments</ui-path> field and
            specify the <code>--disable-sanity</code> option.</p>
    </tab>
</tabs>


## Inspections

### Including inspections

<link-summary>You can tell %product% to analyze files of a certain directory using an inspection that is not contained in the selected profile.</link-summary>

You can tell %product% to analyze files of a certain directory using an inspection that is not contained in the selected profile.
This can be done on a per-analysis basis. To include all paths in a project into the inspection scope, omit the `paths` node.
Information about inspection IDs is available on the [Inspectopedia](https://www.jetbrains.com/help/inspectopedia/) website.

{id="include-example"}

In this YAML configuration example, the `empty` profile, which contains no inspections, is specified, and the `SomeInspectionId` inspection
is explicitly included in the analysis scope for the `tools` directory. As a result, only the analysis performed by
the `SomeInspectionId` inspection the `tools` directory contents will be included in the %product% analysis scope.

```yaml
version: "1.0"

linter: <linter>

profile:
  name: empty
  
  inspections:
    - inspection: SomeInspectionId
      ignore:
        - "!tools"
      enabled: true
```

Here, each `inspections` entry should reference an inspection registered in an active
[inspection profile](inspection-profiles.md), either enabled or disabled. If an inspection ID is not registered, it becomes silently 
ignored and no inspection is added.

For example, the `profile.name: empty` configuration implies that plugin-provided inspections like `CppClangTidy*` are
not registered. To enable specific plugin inspections, you can start from an
[existing inspection profile](inspection-profiles.md#inspection-profiles-existing-profiles) like `qodana.starter`and suppress the inspections that you do not need. Also, add inspections using plugin-specific config like
`.clang-tidy` in case of the [](clang.md) linter.

### Excluding inspections

<link-summary>Learn how you can disable inspections for a specific file.</link-summary>

To disable inspections for a specific file, use the following YAML configuration:

````yaml
version: "1.0"

linter: <linter>

profile:
  inspections:
    - inspection: SomeInspectionId
      ignore:
        - "!<path/to/the/file/from/project/root>"
      enabled: false
````

<p>You can also suppress the inspection only for a class by adding the <code>noinspection</code> comment above the class:</p>
<code-block lang="typescript">
    // noinspection &lt;inspection-name&gt;
    export class WorkflowJobSubject {
        private static subject: Observable&lt;GithubEvent&lt;WorkflowJobEvent&gt;&gt; | null =
            null;
    private static GithubWebhookEventSubject: any;
</code-block>

## Linter paths

<link-summary>List of paths available in Qodana linters.</link-summary>

<p>This table lists the paths available in %product% linters.</p>

<table>
    <tr>
        <td>Path</td>
        <td>Description</td>
    </tr>
    <tr>
        <td><code>/data/project</code></td>
        <td>Root directory of the project</td>
    </tr>
    <tr>
        <td><code>/data/results</code></td>
        <td>Directory to store analysis reports. It should be empty before running %instance%</td>
    </tr>
    <tr>
        <td><code>/opt/idea</code></td>
        <td>IDE distributive directory</td>
    </tr>
    <tr>
        <td><code>/root/.config/idea</code></td>
        <td>IDE configuration directory</td>
    </tr>
    <tr>
        <td><code>/data/profile.xml</code></td>
        <td>The default profile file containing the <code>qodana.starter</code> profile configuration. This file
            is used if a profile was not previously configured either via the CLI or the <code>qodana.yaml</code> file.
            See <a href="inspection-profiles.md" anchor="Order+of+resolving+a+profile"/> for details</td>
    </tr>
    <tr>
        <td><code>/data/project/.idea/inspectionProfiles/</code></td>
        <td>Directory for binding profile files</td>
    </tr>
    <tr>
        <td><code>/data/cache/.m2</code></td>
        <td>Maven project dependencies</td>
    </tr>
    <tr>
        <td><code>/root/.m2/</code></td>
        <td>Directory for overriding the <code>settings.xml</code> configuration file for Maven</td>
    </tr>
    <tr>
        <td><code>/data/cache/gradle</code></td>
        <td>Gradle project dependencies</td>
    </tr>
    <tr>
        <td><code>/data/cache/nuget</code></td>
        <td>NuGet project dependencies</td>
    </tr>
    <tr>
        <td><code>/data/coverage</code></td>
        <td>Directory for mapping <a href="code-coverage.md">code coverage</a> files</td>
    </tr>
</table>

<p>You can find below several examples of how these paths can be applied.</p>

<!--### Override the default inspection profile
{id="docker-config-reference-override-inspection-profile"}

<link-summary>Learn how you can override the default inspection profile.</link-summary>

> You can also see the [](#configuration-reference-inspection-profile) chapter for profiles.

<p>By default, %instance% employs the <code>qodana.starter</code> profile, but you can
    <a anchor="docker-config-reference-image-paths">bind</a> and use your own profile instead:</p>

<tabs group="cli-settings">
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$">
            docker run \
               -v $(pwd):/data/project/ \
               -v $(pwd)/&lt;profile-file&gt;:/data/profile.xml \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               jetbrains/qodana-&lt;image&gt;
        </code-block>
    </tab>
    <tab title="Qodana CLI" group-key="qodana-cli">
        <code-block lang="shell" prompt="$">
            qodana scan \
               -v $(pwd)/&lt;profile-file&gt;:/data/profile.xml \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;"
        </code-block>
    </tab>
    <tab title="GitHub Actions" group-key="github-actions">
    <code-block lang="yaml">
        name: Qodana
        on:
            workflow_dispatch:
            pull_request:
            push:
                branches: # Specify your branches here
                    - main # The 'main' branch
                    - master # The 'master' branch
                    - 'releases/*' # The release branches
        &nbsp;
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
                      uses: %action-version%
                      with:
                          args: -v &lt;profile-file&gt;:/data/profile.xml
                      env:
                          QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
    </code-block>
    </tab>
    <tab title="Jenkins" group-key="jenkins">
        <code-block lang="groovy">
            pipeline {
                environment {
                    QODANA_TOKEN=credentials('qodana-token')
                }
                agent {
                    docker {
                        args '''
                          -v "${WORKSPACE}":/data/project
                          -v "${WORKSPACE}"/&lt;profile-file&gt;:/data/profile.xml
                          --entrypoint=""
                          '''
                        image 'jetbrains/qodana-&lt;image&gt;'
                    }
                }
                stages {
                    stage('Qodana') {
                        steps {
                            sh '''qodana'''
                        }
                    }
                }
            }
        </code-block>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
        <code-block lang="yaml">
            include:
            - component: %gitlab-version%
              inputs:
                 args: |
                    -v &lt;profile-file&gt;:/data/profile.xml
                    --linter &lt;linter&gt;
        </code-block>
    </tab>
    <tab title="TeamCity" group-key="teamcity">
        <p>In the runner configuration, find the <ui-path>Inspection profile</ui-path> dropdown list and select the <ui-path>Profile path</ui-path> option.
        In the field that appears below the dropdown list, specify the path to your profile file relative to the project root.</p>
    </tab>
</tabs>

<p>To learn more about profiles, see the
    <a href="inspection-profiles.md" anchor="Order+of+resolving+a+profile">order of resolving a profile</a> and
    <a href="inspection-profiles.md" anchor="inspection-profiles-setup-a-profile"/> sections in this documentation.</p>
-->
### Configure Maven

<include from="jvm.md" element-id="jvm-maven" />

### Override Gradle settings

<link-summary>Learn how you can override the default Gradle settings.</link-summary>

<p>For JVM linters, you can override the default Gradle settings:</p>

<tabs group="cli-settings">
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$" emphasize-lines="3">
            docker run \
               -v $(pwd):/data/project/ \
               -v $(pwd)/gradle.properties:/data/cache/gradle/gradle.properties \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               jetbrains/qodana-&lt;image&gt;
        </code-block>
    </tab>
    <tab title="Qodana CLI" group-key="qodana-cli">
        <code-block lang="shell" prompt="$" emphasize-lines="2">
            qodana scan \
               -v $(pwd)/gradle.properties:/data/cache/gradle/gradle.properties \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;"
        </code-block>
    </tab>
    <tab title="GitHub Actions" group-key="github-actions">
    <code-block lang="yaml" emphasize-lines="25">
        name: Qodana
        on:
            workflow_dispatch:
            pull_request:
            push:
                branches: # Specify your branches here
                    - main # The 'main' branch
                    - master # The 'master' branch
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
                      uses: %action-version%
                      with:
                          args: -v gradle.properties:/data/cache/gradle/gradle.properties
                      env:
                          QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
    </code-block>
    </tab>
    <tab title="Jenkins" group-key="jenkins">
        <code-block lang="groovy" emphasize-lines="9">
            pipeline {
                environment {
                    QODANA_TOKEN=credentials('qodana-token')
                }
                agent {
                    docker {
                        args '''
                          -v "${WORKSPACE}":/data/project
                          -v "${WORKSPACE}"/gradle.properties:/data/cache/gradle/gradle.properties
                          --entrypoint=""
                          '''
                        image 'jetbrains/qodana-&lt;image&gt;'
                    }
                }
                stages {
                    stage('Qodana') {
                        steps {
                            sh '''qodana'''
                        }
                    }
                }
            }
        </code-block>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
        <code-block lang="yaml" emphasize-lines="5">
            include:
                - component: %gitlab-version%
                  inputs:
                      args: |
                          -v gradle.properties:/data/cache/gradle/gradle.properties
                          --linter &lt;linter&gt;
        </code-block>
    </tab>
    <tab title="TeamCity" group-key="teamcity">
        <p>In the runner configuration, find the <ui-path>Additional Docker arguments</ui-path> field and
            specify the path to the file containing new Gradle settings:</p>
        <code-block lang="shell">
            -v gradle.properties:/data/cache/gradle/gradle.properties
        </code-block>
    </tab>
</tabs>

### Mount JDK

<include from="jvm.md" element-id="jvm-mount-jdk" />

### View Qodana logs
{id="docker-config-reference-overview-logs"}

<link-summary>Learn how you can view log files generated by %product%.</link-summary>

<p>Depending on the tool, you can view log files generated by Qodana:</p>

<tabs group="cli-settings">
    <tab title="Docker image" group-key="docker-image">
        <p>You can mount the <code>$(pwd)/.qodana/results/</code> directory to the <code>/data/results</code>
        directory of the Docker image:</p>
        <code-block lang="shell" prompt="$" emphasize-lines="3">
            docker run \
               -v $(pwd):/data/project/ \
               -v $(pwd)/.qodana/results/:/data/results \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               jetbrains/qodana-&lt;image&gt;
        </code-block>
        <p>Once the Qodana run is complete, you can view log files in the
            <code>$(pwd)/.qodana/results/</code> directory.</p>
    </tab>
    <tab title="Qodana CLI" group-key="qodana-cli">
        <p>After running Qodana, in the project root run the <code>$ qodana show -d</code> command
            for opening the directory containing log files.</p>
    </tab>
</tabs>

<p>There are several options for examining %instance% behavior using the <code>/data/results</code> directory:</p>
<list>
    <li><p>The <code>/data/results/projectStructure</code> directory.</p>
        <p>The <code>Modules.json</code> file in this directory contains a list of all modules detected by
            %instance%. It should be identical to the list that you expect to see while opening your project in
            IntelliJ IDEA. If this is no longer the case, check <code>pom.xml</code> for Maven or the
            <code>build.gradle</code> file for Gradle configurations.</p>
        <p>The <code>SDKs.json</code> file in this directory contains the interpreter paths in case of Python.</p>
    </li>
    <li>In the <code>/data/results/</code> directory, each inspection that detected a possible problem creates
        its own file named <code>ID.json</code>, where <code>ID</code> is the inspection name that can be used in
        <code>qodana.yaml</code> for including or excluding inspections. You can find the complete list of
        inspection IDs in the <code>/data/results/.descriptions.json</code> file using the
        <code>/groups/*/inspections/*/shortName</code> pattern.</li>
    <li>In <code>/data/results/log/idea.log</code>, you can investigate suspicious warnings.</li>
</list>

## Analysis directories
{id="docker-config-reference-directories"}

<link-summary>Learn available CLI options for overriding default paths. </link-summary>

<p>Using these CLI options, you can override the paths described in the
    <a anchor="Linter+paths"/> section.</p>

<table>
    <tr>
        <td>Option</td>
        <td>Description</td>
        <td>Default setting</td>
    </tr>
    <tr id="docker-config-reference-directories-repository-root">
        <td>
            <code>--repository-root &lt;string&gt;</code>
        </td>
        <td>
            <p>Specify the VCS root directory for your project. This option is required for Git-related operations</p>
        </td>
        <td>None</td>
    </tr>
    <tr>
        <td><code>-i</code>, <code>--project-dir</code></td>
        <td><p>Root directory of the inspected project can be either a subdirectory of
            <a anchor="docker-config-reference-directories-repository-root"><code>--repository-root</code></a> or identical to it.</p>
            <p>Files and directories contained in the outside directory are not used while running %instance%</p>
        </td>
        <td><code>/data/project</code></td>
    </tr>
    <tr>
        <td><code>-o</code>, <code>--results-dir</code></td>
        <td>Directory to save %instance% inspection results to</td>
        <td><code>/data/results</code></td>
    </tr>
    <tr>
        <td><code>-r</code>, <code>--report-dir</code></td>
        <td><p>Directory for saving the generated HTML report. To open the report, you will need to add the
            <a anchor="docker-config-reference-report"><code>--save-report</code></a> option</p>
            <note>This option is not available in Qodana CLI.</note>
        </td>
        <td><code>/data/results/report</code></td>
    </tr>
    <tr>
        <td><code>--cache-dir</code></td>
        <td>Directory to store <a anchor="docker-config-reference-cache-dependencies">cache</a></td>
        <td><code>/data/cache</code></td>
    </tr>
    <tr>
        <td><code>-d</code>, <code>--source-directory</code></td>
        <td>
            <note>This option is deprecated and will be removed in future versions of the product.
                See the <code>--only-directory</code> option for details.</note>
            <p>Directory inside <code>--project-dir</code>. If missing, the whole project is inspected.</p>
            <p>Files and directories contained in the outside directory like <code>.git</code> and
                <code>build.gradle</code> are used by %instance% while inspecting code</p>
        </td>
        <td>None</td>
    </tr>
    <tr>
        <td>
            <code>--only-directory &lt;string&gt;</code>
        </td>
        <td>
            <p>Specify the directory inside the <code>project-dir</code> directory that must be analyzed. If not specified,
                the whole project will be analyzed</p>
            <p>Files and directories contained in the outside directory like <code>.git</code> and
                <code>build.gradle</code> are used by %instance% while inspecting code</p>
        </td>
        <td>None</td>
    </tr>
</table>

### Override the report directory
{id="docker-config-reference-directories-save-report"}

<link-summary>Override the directory containing %product% analysis reports.</link-summary>

<tip><p>During analysis, Qodana CLI automatically saves analysis reports in the
    <code>./&lt;userCacheDir&gt;/JetBrains/Qodana/&lt;linter&gt;/&lt;project-id&gt;/results/report</code> directory.</p>
    <p>Here, the <code>linter</code> and <code>project-id</code> directories have the hash format.</p>
</tip>

<p>This Docker command overrides the default report directory using the <code>--report-dir</code>
    option, and saves the generated report to the local filesystem using the
    <a anchor="docker-config-reference-report"><code>--save-report</code></a> option:</p>

<code-block lang="shell" prompt="$" emphasize-lines="6-7">
    docker run \
       -v $(pwd):/data/project/ \
       -v &lt;html-report-directory&gt;:/data/results/newreportdir/ \
       -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
       jetbrains/qodana-&lt;image&gt; \
       --report-dir /data/results/newreportdir/ \
       --save-report
</code-block>

<p>The generated report is saved to the local filesystem as configured by the
    <code>-v &lt;html-report-directory&gt;:/data/results/newreportdir/</code> line in this command.</p>

### Analyze a specific project directory within a repository
{id="troubleshooting-inspect-specific-directory"}

<link-summary>A typical project structure can have a directory structure explained in this section.</link-summary>

<p>A typical project structure can have a directory structure similar to this:</p>

<code-block lang="bash">
  repo/
  .git/
  project/
  ...
</code-block>

<p>Here, the <code>repo/.git</code> directory contains information that should be accessible to %instance%, and
    the <code>repo/project</code> directory contains the project that needs to be inspected by %instance%. All
    these samples mount the <code>repo/project</code> directory using the
    <a anchor="docker-config-reference-directories"><code>--project-dir</code></a>
    option, while the <code>QODANA_TOKEN</code> variable refers to the %cloud%
    <a href="project-token.md">project token</a>:</p>

<tabs>
    <tab title="Docker image">
    <code-block lang="bash" prompt="$" emphasize-lines="5">
        docker run \
        -v repo/:/data/project/ \
        -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
        jetbrains/qodana-&lt;image&gt; \
        --project-dir=/data/project/project/
    </code-block>
    </tab>
    <tab title="Qodana CLI">
    <code-block lang="bash" prompt="$" emphasize-lines="3">
        qodana scan \
        -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
        --project-dir=/data/project/project/
    </code-block>
    </tab>
    <tab title="GitHub Actions">
    <code-block lang="yaml" emphasize-lines="24">
        name: Qodana
        on:
            workflow_dispatch:
            pull_request:
            push:
                branches:
                    - main
                    - 'releases/*'
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
                      uses: %action-version%
                      with:
                          args: --project-dir project
                      env:
                          QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
    </code-block>
    </tab>
</tabs>

### Exclude paths from the analysis scope
{id="exclude-paths"}

<link-summary>You can exclude files and paths from analysis.</link-summary>

You can exclude files and paths from analyses on a per-analysis basis and for all inspections at once.
Information about inspection IDs is available on the [Inspectopedia](https://www.jetbrains.com/help/inspectopedia/) website.

To exclude all paths in a project from the analysis scope, omit the `paths` node.

<note>While using the <code>qodana.recommended</code> and <code>qodana.starter</code> 
profiles, Qodana reads <code>.gitignore</code> files of your project and defines the files and directories to be ignored 
during the analysis.</note>


{id="exclude-example"}

<link-summary>You can exclude paths from analyses for all inspections, as well as for specific inspections. </link-summary>

Exclude all inspections for specified project paths using the following YAML configuration:

```yaml
version: "1.0"

linter: <linter>

profile:
  inspections:
    - group: ALL
      ignore:
        - "asm-test/src/main/java/org"
        - "asm/Visitor.java"
        - "benchmarks"
        - "vendor/**"
        - "scope#file[*test*]:src/*"
```

Exclude inspections specified by ID for specified project paths:
{id="exclude-inspection"}

```yaml
version: "1.0"

linter: <linter>

profile:      
  inspections:
  - inspection: InspectionId
    ignore:
      - "relative/path"
      - "another/relative/path"
  - group: ALL
    ignore:
      - "asm-test/src/main/java/org"
      - "asm"
      - "benchmarks"
      - "tools"
```

You can find specific inspection IDs in the Profile settings in the HTML report or in the `.xml` file with your inspection profile.

### Specify directory in your project

Use the `onlyDirectory` YAML option to specify a project directory to analyze.
This should be relative to the project root, for example:

```yaml
version: "1.0"

linter: <linter>

onlyDirectory: project-a
```
{emphasize-lines="5"}

Alternatively, you can use the `--only-directory` CLI option, for example:

<tabs>
    <tab title="Docker image">
    <code-block lang="bash" prompt="$" emphasize-lines="5">
        docker run \
          -v repo/:/data/project/ \
          -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
          jetbrains/qodana-&lt;image&gt; \
          --only-directory project-a
    </code-block>
    </tab>
    <tab title="Qodana CLI">
    <code-block lang="bash" prompt="$" emphasize-lines="3">
        qodana scan \
          -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
          --only-directory project-a
    </code-block>
    </tab>
    <tab title="GitHub Actions">
    <code-block lang="yaml" emphasize-lines="24">
        name: Qodana
        on:
            workflow_dispatch:
            pull_request:
            push:
                branches:
                    - main
                    - 'releases/*'
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
                      uses: %action-version%
                      with:
                          args: --only-directory project-a
                      env:
                          QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
    </code-block>
    </tab>
</tabs>


This is useful while analyzing [monorepo projects](monorepo-project.md).


### Cache dependencies
{id="docker-config-reference-cache-dependencies"}

<link-summary>You can improve Qodana performance by persisting cache between analyses. For example, package and
    dependency management tools such as Maven, Gradle, npm, Yarn, and NuGet keep a local cache of
    downloaded dependencies.</link-summary>

<tip><p><a href="https://github.com/JetBrains/qodana-cli">Qodana CLI</a> automatically manages cache and requires no action.</p>
<p>After the first run, Qodana CLI stores cache in the <code>./&lt;userCacheDir&gt;/JetBrains/&lt;linter&gt;/cache</code>
    directory.</p></tip>

<p>You can improve %instance% performance by persisting cache between analyses. For example, package and
    dependency management tools such as Maven, Gradle, npm, Yarn, and NuGet keep a local cache of downloaded dependencies.</p>

<p>By default, %instance% save caches to the <code>/data/cache</code> directory inside a container. You can override
    this location using the <a anchor="docker-config-reference-directories"><code>--cache-dir</code></a> option.
    This data is per-repository, so you can pass cache from <code>branch-a</code> to build checking
    <code>branch-b</code>. In this case, only new dependencies would be downloaded if they were added.</p>

<p>In a GitHub workflow, you can use
    <a href="https://docs.github.com/en/actions/guides/caching-dependencies-to-speed-up-workflows">dependency caching</a>.
    GitLab CI/CD also has the <a href="https://docs.gitlab.com/ee/ci/caching/">cache</a> that can be stored
    <a href="https://docs.gitlab.com/ee/ci/yaml/README.html#cachepaths">only inside</a> the project directory.
    In this case, you can exclude the cache directory from inspection via
    <a href="configuration-reference.md" anchor="Excluding+inspections"><code>qodana.yaml</code></a>.</p>

<p>This command maps the local directory with the <code>/data/cache</code> directory of the
    Docker image, which saves cache to your local filesystem: </p>

<code-block lang="shell" prompt="$" emphasize-lines="3">
    docker run \
       -v $(pwd):/data/project/ \
       -v &lt;local-cache-directory&gt;:/data/cache/ \
       -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
       jetbrains/qodana-&lt;image&gt;
</code-block>

<p>Using the <code>--cache-dir</code> option, you can override the cache directory:</p>

<tabs group="cli-settings">
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$" emphasize-lines="3,6">
            docker run \
               -v $(pwd):/data/project/ \
               -v &lt;local-cache-directory&gt;:/data/newcachedir/ \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               jetbrains/qodana-&lt;image&gt; \
               --cache-dir /data/newcachedir
        </code-block>
    </tab>
    <tab title="Qodana CLI" group-key="qodana-cli">
        <code-block lang="shell" prompt="$" emphasize-lines="3">
            qodana scan \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               --cache-dir /opt/newcachedir
        </code-block>
    </tab>
    <tab title="GitHub Actions" group-key="github-actions">
    <code-block lang="yaml" emphasize-lines="25">
        name: Qodana
        on:
            workflow_dispatch:
            pull_request:
            push:
                branches: # Specify your branches here
                    - main # The 'main' branch
                    - master # The 'master' branch
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
                      uses: %action-version%
                      with:
                          args: --cache-dir /data/newcachedir
                      env:
                          QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
    </code-block>
    </tab>
    <tab title="Jenkins" group-key="jenkins">
        <code-block lang="groovy" emphasize-lines="19">
            pipeline {
                environment {
                    QODANA_TOKEN=credentials('qodana-token')
                }
                agent {
                    docker {
                        args '''
                          -v "${WORKSPACE}":/data/project
                          --entrypoint=""
                          '''
                        image 'jetbrains/qodana-&lt;image&gt;'
                    }
                }
                stages {
                    stage('Qodana') {
                        steps {
                            sh '''
                            qodana \
                            --cache-dir /data/newcachedir
                            '''
                        }
                    }
                }
            }
        </code-block>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
        <code-block lang="yaml" emphasize-lines="5">
            include:
                - component: %gitlab-version%
                  inputs:
                      args: |
                          --cache-dir /data/newcachedir
                          --linter &lt;linter&gt;
        </code-block>
    </tab>
    <tab title="TeamCity" group-key="teamcity">
        <p>In the runner configuration, find the <ui-path>Additional Qodana arguments</ui-path> field and
            specify the path to the cache directory:</p>
        <code-block lang="shell">
            --cache-dir /data/newcachedir
        </code-block>
    </tab>
</tabs>


## Analysis reports
{id="docker-config-reference-report"}

<link-summary>Learn more about available profile-related %product% options.</link-summary>

<p>%product% provides the following CLI options for managing reports:</p>

<table>
    <tr>
        <td>Option</td>
        <td>Description</td>
    </tr>
    <tr>
        <td><code>-s</code>, <code>--save-report</code></td>
        <td>Generate and save HTML-formatted reports</td>
    </tr>
    <tr>
        <td><code>-w</code>, <code>--show-report</code></td>
        <td>Serve HTML-formatted reports. By default, %product% uses port <code>8080</code> on its side</td>
    </tr>
</table>


{id="docker-config-reference-report-save-report"}

<link-summary>The --save-report option lets you save the generated HTML report to your
     local filesystem.</link-summary>

<tip><p>During inspection, Qodana CLI automatically saves analysis reports in the
    <code>./&lt;userCacheDir&gt;/JetBrains/Qodana/&lt;linter&gt;/&lt;project-id&gt;/results/report</code> directory.</p>
    <p>Here, the <code>linter</code> and <code>project-id</code> directories have the hash format.</p>
    <p>To view the generated report in your browser, in the project root run the <code>qodana show</code> command.</p>
</tip>

<p>The <code>--save-report</code> option in the Docker command lets you save the generated HTML report to your
    local filesystem: </p>

<code-block lang="shell" prompt="$" emphasize-lines="3,6">
    docker run \
       -v $(pwd):/data/project/ \
       -v &lt;directory-to-save-report-to&gt;:/data/results/report \
       -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
       jetbrains/qodana-&lt;image&gt; \
       --save-report
</code-block>


{id="docker-config-reference-report-show-report"}

<link-summary>The --show-report option runs a local web server to show an analysis report.</link-summary>

<p>The <code>--show-report</code> option runs a local web server on port 4040 of a host machine, so your report will be available on
    <a href="http://localhost:4040">http://localhost:4040</a>:</p>

<tabs group="cli-settings">
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$" emphasize-lines="2,6">
            docker run \
               -p 4040:8080 \
               -v $(pwd):/data/project/ \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               jetbrains/qodana-&lt;image&gt; \
               --show-report
        </code-block>
    </tab>
    <tab title="Qodana CLI" group-key="qodana-cli">
        <code-block lang="shell" prompt="$" emphasize-lines="3-4">
            qodana scan \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               --port 4040 \
               --show-report
        </code-block>
        <p>Alternatively, in the project root you can run the <code>qodana show</code> command.</p>
    </tab>
</tabs>

<p>To stop the web server, press <shortcut>Ctrl-C</shortcut> in the Docker console.</p>

## Qodana features

### Quality gates
{id="docker-config-reference-quality-gate"}

<link-summary>You have several options for configuring a quality gate.</link-summary>

You have several options to configure [quality gates](quality-gate.topic).

In your YAML configuration, you can add a fail threshold to control the total number of problems in a project, which is supported by
all linters:

```yaml
version: "1.0"

linter: <linter>

failThreshold: <number>
```
{emphasize-lines="5"}

> When running in the baseline mode, a threshold is calculated as the sum of new and absent problems. Unchanged results are ignored.
> {style="note"}

All linters except [%dotnet-co%](dotnet.md) and [%clang%](clang.md) let you use the following configuration:

```yaml
version: "1.0"

linter: <linter>

failureConditions:
  severityThresholds:
    any: <number> # Total problems
    critical: <number> # Critical and other severities
    high: <number>
    moderate: <number>
    low: <number>
    info: <number>
  testCoverageThresholds:
    fresh: <number> # Fresh code coverage
    total: <number> # Total code coverage
  dependencyLicenses:
    failOnProhibited: <true|false> # Prohibited licenses
    failOnUnknown: <true|false> # Unknown licenses
```
{emphasize-lines="5"}

In this configuration, exceeding just one setting limitation will make the build fail.

The `severityThresholds:any` key lets you configure the total number of problems. The
`severityThresholds:critical` key lets you configure quality gates for each [problem severity](ui-overview.md#Severity+levels).
The `testCoverageThresholds:fresh` and `testCoverageThresholds:total` keys let you configure the total and fresh code
coverage supported by [several linters](quality-gate.topic#quality-gate-code-coverage). 
The `dependencyLicenses` key lets you configure quality gates for prohibited or unknown licenses.

Also, you can configure quality gates for the total number of problems using the `--fail-threshold` CLI option.
Here is the command that tells %instance% to fail the build in case the number of problems exceeds 10:

<tabs group="cli-settings">
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$" emphasize-lines="5">
            docker run \
               -v $(pwd):/data/project/ \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               jetbrains/qodana-&lt;image&gt; \
               --fail-threshold 10
        </code-block>
    </tab>
    <tab title="Qodana CLI" group-key="qodana-cli">
        <code-block lang="shell" prompt="$" emphasize-lines="3">
            qodana scan \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               --fail-threshold 10
        </code-block>
    </tab>
    <tab title="GitHub Actions" group-key="github-actions">
        <code-block lang="yaml" emphasize-lines="25">
            name: Qodana
            on:
                workflow_dispatch:
                pull_request:
                push:
                    branches: # Specify your branches here
                        - main # The 'main' branch
                        - master # The 'master' branch
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
                          uses: %action-version%
                          with:
                              args: --fail-threshold 10
                          env:
                              QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
        </code-block>
    </tab>
    <tab title="Jenkins" group-key="jenkins">
            <code-block lang="groovy" emphasize-lines="19">
                pipeline {
                    environment {
                        QODANA_TOKEN=credentials('qodana-token')
                    }
                    agent {
                        docker {
                            args '''
                              -v "${WORKSPACE}":/data/project
                              --entrypoint=""
                              '''
                            image 'jetbrains/qodana-&lt;image&gt;'
                        }
                    }
                    stages {
                        stage('Qodana') {
                            steps {
                                sh '''
                                qodana \
                                --fail-threshold 10
                                '''
                            }
                        }
                    }
                }
            </code-block>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
            <code-block lang="yaml" emphasize-lines="5">
                include:
                    - component: %gitlab-version%
                      inputs:
                          args: |
                              --fail-threshold 10
                              --linter &lt;linter&gt;
            </code-block>
    </tab>
    <tab title="TeamCity" group-key="teamcity">
        <p>In the runner configuration, find the <ui-path>Additional Qodana arguments</ui-path> field and
            specify a quality gate:</p>
        <code-block lang="shell">
                --fail-threshold 10
            </code-block>
    </tab>
</tabs>

<p>If you run %instance% with the <a anchor="docker-config-reference-baseline">baseline mode</a> enabled, a
    threshold is calculated as the sum of new and absent problems. The unchanged results are ignored.</p>

### Baseline
{id="docker-config-reference-baseline"}

<link-summary>In the baseline mode, each new %product% run is compared to some initial run, which helps when you
    have no possibility to fix old problems and rather want to prevent the appearance of new ones.</link-summary>

<p>In the <a href="baseline.topic">baseline</a> run mode, each new %instance% run is compared to some initial run. This can help in
    situations when you have no possibility to fix old problems and rather want to prevent the appearance of new ones.</p>

<p>To use the baseline feature, first run %instance%, and in the report UI select the problems that will be considered as baseline.
Finally, save the <a href="qodana-inspection-output.md" anchor="SARIF+Output">SARIF-formatted file</a> containing the baseline problems. </p>

<p>This is the list of baseline-related options:</p>

<table>
    <tr>
        <td>Option</td>
        <td>Description</td>
    </tr>
    <tr>
        <td><code>-b</code>, <code>--baseline</code></td>
        <td>Run %instance% in the <a href="baseline.topic">baseline</a> mode. Provide the path to an existing SARIF report to be used in the baseline state calculation</td>
    </tr>
    <tr>
        <td><code>--baseline-include-absent</code></td>
        <td>Include in the output report the results from the baseline run that are absent during the current analysis</td>
    </tr>
</table>

<p>This command invokes all baseline options:</p>

<tabs group="cli-settings">
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$" emphasize-lines="5-6">
            docker run \
               -v $(pwd):/data/project/ \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               jetbrains/qodana-&lt;image&gt; \
               --baseline &lt;path-to-the-SARIF-file&gt; \
               --baseline-include-absent
        </code-block>
    </tab>
    <tab title="Qodana CLI" group-key="qodana-cli">
        <code-block lang="shell" prompt="$" emphasize-lines="3-4">
            qodana scan \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               --baseline &lt;path-to-the-SARIF-file&gt; \
               --baseline-include-absent
        </code-block>
    </tab>
    <tab title="GitHub Actions" group-key="github-actions">
        <code-block lang="yaml" emphasize-lines="26-27">
            name: Qodana
            on:
                workflow_dispatch:
                pull_request:
                push:
                    branches: # Specify your branches here
                        - main # The 'main' branch
                        - master # The 'master' branch
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
                          uses: %action-version%
                          with:
                              args: |
                                  --baseline &lt;path-to-the-SARIF-file&gt;
                                  --baseline-include-absent
                          env:
                              QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
        </code-block>
    </tab>
    <tab title="Jenkins" group-key="jenkins">
            <code-block lang="groovy" emphasize-lines="19-20">
                pipeline {
                    environment {
                        QODANA_TOKEN=credentials('qodana-token')
                    }
                    agent {
                        docker {
                            args '''
                              -v "${WORKSPACE}":/data/project
                              --entrypoint=""
                              '''
                            image 'jetbrains/qodana-&lt;image&gt;'
                        }
                    }
                    stages {
                        stage('Qodana') {
                            steps {
                                sh '''
                                qodana \
                                --baseline &lt;path-to-the-SARIF-file&gt; \
                                --baseline-include-absent
                                '''
                            }
                        }
                    }
                }
            </code-block>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
            <code-block lang="yaml" emphasize-lines="5-6">
                include:
                    - component: %gitlab-version%
                      inputs:
                          args: |
                              --baseline &lt;path-to-the-SARIF-file&gt;
                              --baseline-include-absent --linter &lt;linter&gt;
            </code-block>
    </tab>
    <tab title="TeamCity" group-key="teamcity">
        <p>In the runner configuration, find the <ui-path>Additional Qodana arguments</ui-path> field and
            configure a baseline:</p>
        <code-block lang="shell">
              --baseline &lt;path-to-the-SARIF-file&gt; --baseline-include-absent --linter &lt;linter&gt;
            </code-block>
    </tab>
</tabs>

<p>Here, the <code>&lt;path-to-the-SARIF-file&gt;</code> is the path to a <code>qodana.sarif.json</code> file relative
    to the project root and taken from a previous %instance% run. If <code>--baseline-include-absent</code>
    is invoked, the inspection results will include absent problems or the problems detected only in the
    baseline run but not in the current run. </p>

<p>Based on this run, the <a href="qodana-inspection-output.md" anchor="SARIF+Output">SARIF output report</a> will contain the per-problem information on the
    baseline state.</p>

### License audit
{id="configure-license-audit"}

<link-summary>You can configure the license audit feature by configuring the CheckDependencyLicenses inspection.</link-summary>

The [license audit](license-audit.topic) feature is enabled by default. You can disable it by
excluding the [`CheckDependencyLicenses`](https://www.jetbrains.com/help/inspectopedia/CheckDependencyLicenses.html) inspection:

```yaml
version: "1.0"

linter: <linter>

profile:
  inspections:
    - inspection: CheckDependencyLicenses
      enabled: false
```
{emphasize-lines="7-8"}

#### Ignore a dependency

<link-summary>You can ignore a dependency to hide the related problems from the report.</link-summary>

Ignore a dependency to hide the related problems from the report:

```yaml
version: "1.0"

linter: <linter>

dependencyIgnores:
  - name: "enry"
```
{emphasize-lines="5-6"}

where `name` is the dependency name to ignore.

In the example above, the `enry` dependency is completely excluded from the analysis. Because any possible license-related problems are dismissed, the dependency won't be included in the report at all. This is useful to quickly hide internal dependencies that do not need to be mentioned in the report.

#### Allow or prohibit a license

<link-summary>You can override the license compatibility matrix predefined in %product% by allowing or prohibiting licenses.</link-summary>

Override the predefined license compatibility matrix:

```yaml
version: "1.0"

linter: <linter>

licenseRules:
  - keys:
      - "PROPRIETARY-LICENSE"
      - "MIT"
    prohibited:
      - "BSD-3-CLAUSE-NO-CHANGE"
    allowed:
      - "ISC"

  - keys: [ "Apache-2.0" ]
    prohibited:
      - "MIT"
```

In this configuration,  `keys` is the project license(s) and the dependency licenses identifiers are specified in `allowed` or `prohibited`.

#### Override a dependency license

<link-summary>You can override a dependency license identifier.</link-summary>

Override a dependency license identifier:

```yaml
version: "1.0"

linter: <linter>

dependencyOverrides:
  - name: "jaxb-runtime"
    version: "2.3.1"
    url: "https://github.com/javaee/jaxb-v2"
    licenses:
      - key: "CDDL-1.1"
        url: "https://github.com/javaee/jaxb-v2/blob/master/LICENSE"
      - key: "GPL-2.0-with-classpath-exception"
        url: "https://github.com/javaee/jaxb-v2/blob/master/LICENSE"
```

where `name` is the dependency name, `version` is the dependency version, and `licenses` is the list of redefined dependency licenses.

In the example above, you 'tell' Qodana to detect CDDL-1.1, GPL-2.0-with-classpath-exception, and no other licenses for jaxb-runtime (only 2.3.1). This is useful when a dependency is dual-licensed, and you want to omit some license or when it's not possible to detect the license from the dependency sources correctly.

#### Custom dependencies

<link-summary>You can include a custom dependency in the license compatibility matrix.</link-summary>

Currently, the license audit with %instance% is possible only for JPS, Maven, Gradle, npm, yarn, and composer projects. To include the dependency that should be mentioned in the report but is impossible to detect from the project sources, use `customDependencies` to specify it:

```yaml
version: "1.0"

linter: <linter>

customDependencies:
  - name: ".babelrc JSON Schema (.babelrc-schema.json)"
    version: "JSON schema for Babel 6+ configuration files"
    licenses:
      - key: "Apache-2.0"
        url: "https://github.com/SchemaStore/schemastore/blob/master/LICENSE"
```
{emphasize-lines="5"}

### Quick-Fixes
{id="docker-config-reference-quick-fix"}

<link-summary>You can apply the cleanup or apply Quick-Fix strategies.</link-summary>

This table describes the available [Quick-Fix strategies](quick-fix.md#How+Quick-Fix+works):

<table>
    <tr>
        <td>CLI option / YAML key</td>
        <td>Description</td>
    </tr>
    <tr>
        <td>
            <code>
                --apply-fixes / apply
            </code>
        </td>
        <td>
            Apply all available Quick-Fix strategies including cleanup, see the <a href="quick-fix.md"/>
            section for details
        </td>
    </tr>
    <tr>
        <td>
            <code>
                --cleanup / cleanup
            </code>
        </td>
        <td>
            Run the <code>CLEANUP</code> Quick-Fix strategy, see the
            <a href="quick-fix.md" anchor="How+Quick-Fix+works">Quick-Fix</a> for details
        </td>
    </tr>
</table>

Using the `fixesStrategy` YAML key, you can choose among the available strategies:

```yaml
version: "1.0"

linter: <linter>

fixesStrategy: cleanup/apply
```
{emphasize-lines="5"}

Alternatively, you can employ the `--apply-fixes` or `--cleanup` command-line options:

<tabs group="cli-settings">
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$" emphasize-lines="5">
            docker run \
               -v $(pwd):/data/project/ \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               jetbrains/qodana-&lt;image&gt; \
               --apply-fixes/cleanup
        </code-block>
    </tab>
    <tab title="Qodana CLI" group-key="qodana-cli">
        <code-block lang="shell" prompt="$" emphasize-lines="3">
            qodana scan \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               --apply-fixes/cleanup
        </code-block>
    </tab>
    <tab title="GitHub Actions" group-key="github-actions">
        <code-block lang="yaml" emphasize-lines="25">
            name: Qodana
            on:
                workflow_dispatch:
                pull_request:
                push:
                    branches: # Specify your branches here
                        - main # The 'main' branch
                        - master # The 'master' branch
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
                          uses: %action-version%
                          with:
                              args: --apply-fixes/cleanup
                          env:
                              QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
        </code-block>
    </tab>
    <tab title="Jenkins" group-key="jenkins">
            <code-block lang="groovy" emphasize-lines="19">
                pipeline {
                    environment {
                        QODANA_TOKEN=credentials('qodana-token')
                    }
                    agent {
                        docker {
                            args '''
                              -v "${WORKSPACE}":/data/project
                              --entrypoint=""
                              '''
                            image 'jetbrains/qodana-&lt;image&gt;'
                        }
                    }
                    stages {
                        stage('Qodana') {
                            steps {
                                sh '''
                                qodana \
                                --apply-fixes/cleanup
                                '''
                            }
                        }
                    }
                }
            </code-block>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
            <code-block lang="yaml" emphasize-lines="5">
                include:
                    - component: %gitlab-version%
                      inputs:
                          args: |
                              --apply-fixes/cleanup
                              --linter &lt;linter&gt;
            </code-block>
    </tab>
    <tab title="TeamCity" group-key="teamcity">
        <p>In the runner configuration, find the <ui-path>Additional Qodana arguments</ui-path> field and
            specify the option:</p>
        <code-block lang="shell">
                --apply-fixes
            </code-block>
    </tab>
</tabs>

### Taint analysis
{id="configure-taint-analysis"}

<link-summary>Learn how you can configure the taint analysis feature.</link-summary>

<include from="taint-analysis.md" element-id="running-taint-analysis"/>

### Vulnerability checker

<link-summary>Learn how you can configure the vulnerability checker feature.</link-summary>

To start using the [](vulnerability-checker.md) feature, enable
the [`VulnerableLibrariesGlobal`](https://www.jetbrains.com/help/inspectopedia/VulnerableLibrariesGlobal.html) inspection:

<include from="vulnerability-checker.md" element-id="package-checking-enable"/>

### Code coverage

By default, [code coverage](code-coverage.md) is enabled in %product%.

Using the `coverage.reportProblems` key, you can configure it in a YAML file.
The `codeCoverageLocations` key lets you override the default code coverage directories, for example:

```yaml
version: "1.0"

linter: <linter>

coverage:
  reportProblems: true # Code coverage is enabled
  codeCoverageLocations: # Directories containing coverage reports
    - "custom-directory-1"
    - "custom-directory-2"
```
{emphasize-lines="5-9"}

{id="docker-config-reference-code-coverage"}
<link-summary>You can run the code coverage by mapping the directory containing code coverage files to
    the /data/coverage directory of a %instance% linter image.</link-summary>

<note>
    For the <a href="golang.md">%go%</a> linter, including code coverage requires that a project contains no <code>.idea</code> directory.
</note>

<p>You can run the <a href="code-coverage.md">code coverage</a> by mapping the directory containing code coverage files to
    the <code>/data/coverage</code> directory of a %instance% linter image:</p>

<tabs group="cli-settings">
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$" emphasize-lines="2">
            docker run \
               -v /my/dir/with/coverage:/data/coverage \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               jetbrains/qodana-&lt;image&gt;
        </code-block>
    </tab>
    <tab title="Qodana CLI" group-key="qodana-cli">
        <code-block lang="shell" prompt="$" emphasize-lines="2">
            qodana scan \
               -v /my/dir/with/coverage:/data/coverage \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;"
        </code-block>
    </tab>
    <tab title="GitHub Actions" group-key="github-actions">
        <code-block lang="yaml" emphasize-lines="25">
            name: Qodana
            on:
                workflow_dispatch:
                pull_request:
                push:
                    branches: # Specify your branches here
                        - main # The 'main' branch
                        - master # The 'master' branch
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
                          uses: %action-version%
                          with:
                              args: -v /my/dir/with/coverage:/data/coverage
                          env:
                              QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
        </code-block>
    </tab>
    <tab title="Jenkins" group-key="jenkins">
            <code-block lang="groovy" emphasize-lines="19">
                pipeline {
                    environment {
                        QODANA_TOKEN=credentials('qodana-token')
                    }
                    agent {
                        docker {
                            args '''
                              -v "${WORKSPACE}":/data/project
                              --entrypoint=""
                              '''
                            image 'jetbrains/qodana-&lt;image&gt;'
                        }
                    }
                    stages {
                        stage('Qodana') {
                            steps {
                                sh '''
                                qodana \
                                -v /my/dir/with/coverage:/data/coverage
                                '''
                            }
                        }
                    }
                }
            </code-block>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
            <code-block lang="yaml" emphasize-lines="5">
                include:
                    - component: %gitlab-version%
                      inputs:
                          args: |
                              -v /my/dir/with/coverage:/data/coverage
                              --linter &lt;linter&gt;
            </code-block>
    </tab>
    <tab title="TeamCity" group-key="teamcity">
        <p>In the runner configuration, find the <ui-path>Additional Docker arguments</ui-path> field and
            specify the path the file containing code coverage results:</p>
        <code-block lang="shell">
                -v /my/dir/with/coverage:/data/coverage
            </code-block>
    </tab>
</tabs>


## Override the run scenario

You can use the following run scenarios: 

<table>
    <tr>
        <td>Scenario name</td>
        <td>Description</td>
    </tr>
    <tr>
        <td><code>default</code></td>
        <td>The default %product% scenario, enabled by default</td>
    </tr>
    <tr>
        <td><code>php-migration</code></td>
        <td><a href="php-language-upgrade.topic">PHP version migration</a> scenario</td>
    </tr>
    <tr>
        <td><code>local-changes</code></td>
        <td>Analyze only uncommitted changes. You can see the <a href="analyze-pr.md"/> section to learn more about incremental analysis</td>
    </tr>
</table>

Using the `script` of a YAML configuration, you can specify a run scenario:

```yaml
version: "1.0"

linter: <linter>

script:
  name: <script-name>
  parameters:
      <parameter>: <value>
```
{emphasize-lines="5"}

By default, %instance% employs the `default` scenario, which means the normal %instance% run equivalent to this setting:

```yaml
version: "1.0"

linter: <linter>

script:
  name: default
```

You can also use the `--script` CLI option to configure a run scenario: 

<tabs group="cli-settings">
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$" emphasize-lines="5">
            docker run \
               -v $(pwd):/data/project/ \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               jetbrains/qodana-&lt;image&gt; \
               --script default
        </code-block>
    </tab>
    <tab title="Qodana CLI" group-key="qodana-cli" emphasize-lines="3">
        <code-block lang="shell" prompt="$">
            qodana scan \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               --script default
        </code-block>
    </tab>
    <tab title="GitHub Actions" group-key="github-actions" emphasize-lines="26">
        <code-block lang="yaml">
            name: Qodana
            on:
                workflow_dispatch:
                pull_request:
                push:
                    branches: # Specify your branches here
                        - main # The 'main' branch
                        - master # The 'master' branch
                        - 'releases/*' # The release branches
                &nbsp;
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
                          uses: %action-version%
                          with:
                              args: --script default
                          env:
                              QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
        </code-block>
    </tab>
    <tab title="Jenkins" group-key="jenkins" emphasize-lines="19">
            <code-block lang="groovy">
                pipeline {
                    environment {
                        QODANA_TOKEN=credentials('qodana-token')
                    }
                    agent {
                        docker {
                            args '''
                              -v "${WORKSPACE}":/data/project
                              --entrypoint=""
                              '''
                            image 'jetbrains/qodana-&lt;image&gt;'
                        }
                    }
                    stages {
                        stage('Qodana') {
                            steps {
                                sh '''
                                qodana \
                                --script default
                                '''
                            }
                        }
                    }
                }
            </code-block>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
            <code-block lang="yaml">
                include:
                    - component: %gitlab-version%
                      inputs:
                          args: |
                              --script default
                              --linter &lt;linter&gt;
            </code-block>
    </tab>
    <tab title="TeamCity" group-key="teamcity">
        <p>In the runner configuration, find the <ui-path>Additional Qodana arguments</ui-path> field and
            specify the script:</p>
        <code-block lang="shell">
                --script default
            </code-block>
    </tab>
</tabs>

## JDK version

<link-summary>For JVM-based linters, you can configure the JDK version.</link-summary>

You can configure the JDK version for these linters:

* [%jvm%](jvm.md)
* [%jvm-co%](jvm.md)
* [%jvm-co-a%](jvm.md)

<include from="lib_qd.topic" element-id="configure-jdk-qodana-yaml" use-filter="configure-jdk-qodana-yaml,empty"/>

To learn more about configuring JDK, see the [](jvm.md#Configuring+the+JDK) section.

## PHP version

<link-summary>You can configure the PHP version while using the %php% linter.</link-summary>

You can configure the PHP version before running the [%php%](php.md) linter:

```yaml
version: "1.0"

linter: %php-linter%

php:
  version: "X.x"
```

## Properties
{id="docker-config-reference-properties"}

<link-summary>Learn how you can override %product% settings using properties.</link-summary>

<p>Using the <code>--property=</code> option, you can override various %instance% parameters:</p>

* [Logging messages to STDOUT](#docker-config-reference-properties-stdout)
* [Disabling user statistics](#docker-config-reference-properties-user-statistics)
* [Configuring plugins](#docker-config-reference-properties-config-plugins)
* [Setting up configuration timeout](#docker-config-reference-properties-config-timeout)

<table>
    <tr>
        <td>Option</td>
        <td>Description</td>
    </tr>
    <tr>
        <td><code>--property=</code></td>
        <td><p>Set a JVM property using this notation:</p>
            <code-block lang="shell">--property=property.name=value1,...,valueN</code-block>
            <p>This option can be repeated multiple times for setting multiple JVM properties.</p>
        </td>
    </tr>
</table>

### Log INFO messages to STDOUT
{id="docker-config-reference-properties-stdout"}

<note>This feature is not available in the <a href="dotnet.md">%dotnet%</a> linter.</note>

<!-- What does this command mean?-->

<p>The default log level for STDOUT is <code>WARN</code>. You can override it using the
    <code>idea.log.config.file</code> property.</p>

<tabs group="cli-settings">
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$" emphasize-lines="5">
            docker run \
               -v $(pwd):/data/project/ \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               jetbrains/qodana-&lt;image&gt; \
               --property=idea.log.config.file=info.xml
        </code-block>
    </tab>
    <tab title="Qodana CLI" group-key="qodana-cli">
        <code-block lang="shell" prompt="$" emphasize-lines="3">
            qodana scan \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               --property=idea.log.config.file=info.xml
        </code-block>
    </tab>
    <tab title="GitHub Actions" group-key="github-actions">
    <code-block lang="yaml" emphasize-lines="25">
        name: Qodana
        on:
            workflow_dispatch:
            pull_request:
            push:
                branches: # Specify your branches here
                    - main # The 'main' branch
                    - master # The 'master' branch
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
                      uses: %action-version%
                      with:
                          args: --property=idea.log.config.file=info.xml
                      env:
                          QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
    </code-block>
    </tab>
    <tab title="Jenkins" group-key="jenkins">
        <code-block lang="groovy" emphasize-lines="19">
            pipeline {
                environment {
                    QODANA_TOKEN=credentials('qodana-token')
                }
                agent {
                    docker {
                        args '''
                          -v "${WORKSPACE}":/data/project
                          --entrypoint=""
                          '''
                        image 'jetbrains/qodana-&lt;image&gt;'
                    }
                }
                stages {
                    stage('Qodana') {
                        steps {
                            sh '''
                            qodana \
                            --property=idea.log.config.file=info.xml
                            '''
                        }
                    }
                }
            }
        </code-block>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
        <code-block lang="yaml" emphasize-lines="5">
            include:
                - component: %gitlab-version%
                  inputs:
                      args: |
                          --property=idea.log.config.file=info.xml
                          --linter &lt;linter&gt;
        </code-block>
    </tab>
    <tab title="TeamCity" group-key="teamcity">
        <p>In the runner configuration, find the <ui-path>Additional Qodana arguments</ui-path> field and
            specify the preferred Quick-Fix strategy:</p>
        <code-block lang="shell">
            --property=idea.log.config.file=info.xml
        </code-block>
    </tab>
</tabs>


### Disable user statistics
{id="docker-config-reference-properties-user-statistics"}

<link-summary>You can disable reporting of usage statistics by adjusting the idea.headless.enable.statistics
    value of the --property option.</link-summary>

<p>To disable reporting of usage statistics, adjust the <code>idea.headless.enable.statistics</code>
    value of the <code>--property</code> option:</p>

<tabs group="cli-settings">
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$" emphasize-lines="5">
            docker run \
               -v $(pwd):/data/project/ \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               jetbrains/qodana-&lt;image&gt; \
               --property=idea.headless.enable.statistics=false
        </code-block>
    </tab>
    <tab title="Qodana CLI" group-key="qodana-cli">
        <code-block lang="shell" prompt="$" emphasize-lines="3">
            qodana scan \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               --property=idea.headless.enable.statistics=false
        </code-block>
    </tab>
    <tab title="GitHub Actions" group-key="github-actions">
    <code-block lang="yaml" emphasize-lines="25">
        name: Qodana
        on:
            workflow_dispatch:
            pull_request:
            push:
                branches: # Specify your branches here
                    - main # The 'main' branch
                    - master # The 'master' branch
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
                      uses: %action-version%
                      with:
                          args: --property idea.headless.enable.statistics=false
                      env:
                          QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
    </code-block>
    </tab>
    <tab title="Jenkins" group-key="jenkins">
        <code-block lang="groovy" emphasize-lines="19">
            pipeline {
                environment {
                    QODANA_TOKEN=credentials('qodana-token')
                }
                agent {
                    docker {
                        args '''
                          -v "${WORKSPACE}":/data/project
                          --entrypoint=""
                          '''
                        image 'jetbrains/qodana-&lt;image&gt;'
                    }
                }
                stages {
                    stage('Qodana') {
                        steps {
                            sh '''
                            qodana \
                            --property=idea.headless.enable.statistics=false
                            '''
                        }
                    }
                }
            }
        </code-block>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
        <code-block lang="yaml" emphasize-lines="5">
            include:
                - component: %gitlab-version%
                  inputs:
                      args: |
                          --property idea.headless.enable.statistics=false
                          --image &lt;image&gt;
        </code-block>
    </tab>
    <tab title="TeamCity" group-key="teamcity">
        <p>In the runner configuration, find the <ui-path>Additional Qodana arguments</ui-path> field and
            specify the required property:</p>
        <code-block lang="shell">
            --property=idea.headless.enable.statistics=false
        </code-block>
    </tab>
</tabs>

### Configure plugins
{id="docker-config-reference-properties-config-plugins"}

<link-summary>Using the idea.required.plugins.id and idea.suppressed.plugins.id properties,
    you can specify the plugins required for a specific run, and the list of plugins that will
    be suppressed.</link-summary>

<p>Using the <code>idea.required.plugins.id</code> and <code>idea.suppressed.plugins.id</code> properties,
    you can specify the plugins required for a specific run, and the list of plugins that will
    be suppressed: </p>

<tabs group="cli-settings">
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$" emphasize-lines="5-6">
            docker run \
               -v $(pwd):/data/project/ \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               jetbrains/qodana-&lt;image&gt; \
               --property=idea.required.plugins.id=JavaScript,org.intellij.grails \
               --property=idea.suppressed.plugins.id=com.intellij.spring.security
        </code-block>
    </tab>
    <tab title="Qodana CLI" group-key="qodana-cli">
        <code-block lang="shell" prompt="$" emphasize-lines="3-4">
            qodana scan \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               --property=idea.required.plugins.id=JavaScript,org.intellij.grails \
               --property=idea.suppressed.plugins.id=com.intellij.spring.security
        </code-block>
    </tab>
    <tab title="GitHub Actions" group-key="github-actions">
    <code-block lang="yaml" emphasize-lines="26-27">
        name: Qodana
        on:
            workflow_dispatch:
            pull_request:
            push:
                branches: # Specify your branches here
                    - main # The 'main' branch
                    - master # The 'master' branch
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
                      uses: %action-version%
                      with:
                          args: |
                              --property=idea.required.plugins.id=JavaScript,org.intellij.grails
                              --property=idea.suppressed.plugins.id=com.intellij.spring.security
                      env:
                          QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
    </code-block>
    </tab>
    <tab title="Jenkins" group-key="jenkins">
        <code-block lang="groovy" emphasize-lines="19-20">
            pipeline {
                environment {
                    QODANA_TOKEN=credentials('qodana-token')
                }
                agent {
                    docker {
                        args '''
                          -v "${WORKSPACE}":/data/project
                          --entrypoint=""
                          '''
                        image 'jetbrains/qodana-&lt;image&gt;'
                    }
                }
                stages {
                    stage('Qodana') {
                        steps {
                            sh '''
                            qodana \
                            --property=idea.required.plugins.id=JavaScript,org.intellij.grails \
                            --property=idea.suppressed.plugins.id=com.intellij.spring.security
                            '''
                        }
                    }
                }
            }
        </code-block>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
        <code-block lang="yaml" emphasize-lines="5-6">
            include:
                - component: %gitlab-version%
                  inputs:
                      args: |
                          --property=idea.required.plugins.id=JavaScript,org.intellij.grails
                          --property=idea.suppressed.plugins.id=com.intellij.spring.security
                          --image &lt;image&gt;
        </code-block>
    </tab>
    <tab title="TeamCity" group-key="teamcity">
        <p>In the runner configuration, find the <ui-path>Additional Qodana arguments</ui-path> field and
            specify the required properties:</p>
        <code-block lang="shell">
               --property=idea.required.plugins.id=JavaScript,org.intellij.grails \
               --property=idea.suppressed.plugins.id=com.intellij.spring.security
        </code-block>
    </tab>
</tabs>

### Setting up configuration timeout
{id="docker-config-reference-properties-config-timeout"}

<note>These properties are available only for the <a href="rust.md">%rust%</a>, <a href="clang.md">%cpp% and %clang%</a> linters.</note>
<p>Using the following properties, you can configure the <a href="inspect-your-code.md" anchor="Analysis+stages">configuration stage timeout</a>:</p>
<table>
    <tr>
        <td>Property</td>
        <td>Available for the linters</td>
    </tr>
    <tr>
        <td><code>qd.cpp.startup.timeout.minutes</code></td>
        <td><a href="clang.md">%cpp% and %clang%</a></td>
    </tr>
    <tr>
        <td><code>qd.rust.configuration.timeout.minutes</code></td>
        <td><a href="rust.md">%rust%</a></td>
    </tr>
</table>
<p>Here are the examples of property usage:</p>
<tabs group="software">
  <tab title="GitHub Actions" group-key="github">
        <code-block lang="yaml" emphasize-lines="24">
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
                          uses: %action-version%
                          with:
                              args: --property qd.&lt;cpp|rust&gt;.startup.timeout.minutes=10
                          env:
                              QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
        </code-block>
   </tab>
                <!--<tab title="GitLab CI/CD" group-key="gitlab">
                    <p>In the root directory of your project, save the <code>.gitlab-ci.yml</code> file containing the following snippet:</p>
                    <code-block lang="yaml" filter="cpp">
                      include:
                          - component: %gitlab-version%
                            inputs:
                                args: --linter %qd-linter%
                    </code-block>
                    <code-block lang="yaml" filter="rust">
                      include:
                          - component: %gitlab-version%
                            inputs:
                                args: --linter %qd-linter%
                    </code-block>
                </tab>-->
  <tab title="Command line" group-key="command-line">
      <tabs group="cli-settings">
          <tab group-key="qodana-cli" title="Qodana CLI">
      <code-block prompt="$" lang="shell" emphasize-lines="4">
        qodana scan \
        &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
        &nbsp;&nbsp;&nbsp;--linter &lt;linter&gt; \
        &nbsp;&nbsp;&nbsp;--property qd.&lt;cpp|rust&gt;.configuration.timeout.minutes=10
      </code-block>
          </tab>
      <tab group-key="docker-image" title="Docker image">
      <code-block lang="shell" prompt="$" emphasize-lines="5">
      docker run \
      &nbsp;&nbsp;&nbsp;-v $(pwd):/data/project/ \
      &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
      &nbsp;&nbsp;&nbsp;jetbrains/qodana-&lt;image&gt; \
      &nbsp;&nbsp;&nbsp;--property qd.&lt;cpp|rust&gt;.configuration.timeout.minutes=10
  </code-block>
          </tab>
      </tabs>
  </tab>
</tabs>

## Analyze changed code
{id="docker-config-reference-changes"}

<link-summary>For all linters except Qodana Community for .NET, you can run incremental analysis on a change set like
    merge or pull requests, as well as inspect changes between two commits.</link-summary>

<note>This feature is not supported by the <a href="dotnet.md">%dotnet-co%</a> and <a href="clang.md">%clang%</a> linters.</note>

<table>
    <tr>
        <td>Option</td>
        <td>Description</td>
    </tr>
    <tr>
        <td><code>--diff-start</code> and <code>--diff-end</code></td>
        <td>
            Run incremental analysis on a change set like merge or pull requests
        </td>
    </tr>
</table>

<snippet id="docker-config-reference-changes-examples">

<p>If you just finished work and would like to analyze the changes, you
    can employ the <code>--diff-start</code> option and specify a hash of the commit that will act as a base
    for comparison, see the <a href="analyze-pr.md"/> section for details:</p>

<tabs group="cli-settings">
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$" emphasize-lines="5">
            docker run \
            &nbsp;&nbsp;&nbsp;-v $(pwd):/data/project/ \
            &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
            &nbsp;&nbsp;&nbsp;jetbrains/qodana-&lt;image&gt; \
            &nbsp;&nbsp;&nbsp;--diff-start=&lt;GIT_START_HASH&gt;
        </code-block>
    </tab>
    <tab title="Qodana CLI" group-key="qodana-cli">
        <code-block lang="shell" prompt="$" emphasize-lines="3">
            qodana scan \
            &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
            &nbsp;&nbsp;&nbsp;--diff-start=&lt;GIT_START_HASH&gt;
        </code-block>
    </tab>
    <tab title="GitHub Actions" group-key="github-actions">
        <code-block lang="yaml" emphasize-lines="25">
            name: Qodana
            on:
                workflow_dispatch:
                pull_request:
                push:
                    branches: # Specify your branches here
                        - main # The 'main' branch
                        - master # The 'master' branch
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
                          uses: %action-version%
                          with:
                              args: --diff-start=&lt;GIT_START_HASH&gt;
                          env:
                              QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
        </code-block>
    </tab>
    <tab title="Jenkins" group-key="jenkins">
            <code-block lang="groovy" emphasize-lines="19">
                pipeline {
                    environment {
                        QODANA_TOKEN=credentials('qodana-token')
                    }
                    agent {
                        docker {
                            args '''
                              -v "${WORKSPACE}":/data/project
                              --entrypoint=""
                              '''
                            image 'jetbrains/qodana-&lt;image&gt;'
                        }
                    }
                    stages {
                        stage('Qodana') {
                            steps {
                                sh '''
                                qodana \
                                --diff-start=&lt;GIT_START_HASH&gt;
                                '''
                            }
                        }
                    }
                }
            </code-block>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
            <code-block lang="yaml" emphasize-lines="5">
                include:
                    - component: %gitlab-version%
                      inputs:
                          args: |
                              --diff-start=&lt;GIT_START_HASH&gt;
                              --image &lt;image&gt;
            </code-block>
    </tab>
    <tab title="TeamCity" group-key="teamcity">
        <p>In the runner configuration, find the <ui-path>Additional Qodana arguments</ui-path> field and
            specify the commit hash:</p>
        <code-block lang="shell">
                --diff-start=&lt;GIT_START_HASH&gt;
            </code-block>
    </tab>
</tabs>

<p>To analyze a set of changes between two commits, employ both <code>--diff-start</code>
and <code>--diff-end</code> options:</p>

<tabs group="cli-settings">
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$" emphasize-lines="5-6">
            docker run \
            &nbsp;&nbsp;&nbsp;-v $(pwd):/data/project/ \
            &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
            &nbsp;&nbsp;&nbsp;jetbrains/qodana-&lt;image&gt; \
            &nbsp;&nbsp;&nbsp;--diff-start=&lt;GIT_START_HASH&gt; \
            &nbsp;&nbsp;&nbsp;--diff-end=&lt;GIT_END_HASH&gt;
        </code-block>
    </tab>
    <tab title="Qodana CLI" group-key="qodana-cli">
        <code-block lang="shell" prompt="$" emphasize-lines="3-4">
            qodana scan \
            &nbsp;&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
            &nbsp;&nbsp;&nbsp;--diff-start=&lt;GIT_START_HASH&gt; \
            &nbsp;&nbsp;&nbsp;--diff-end=&lt;GIT_END_HASH&gt;
        </code-block>
    </tab>
    <tab title="GitHub Actions" group-key="github-actions">
        <code-block lang="yaml" emphasize-lines="26-27">
            name: Qodana
            on:
                workflow_dispatch:
                pull_request:
                push:
                    branches: # Specify your branches here
                        - main # The 'main' branch
                        - master # The 'master' branch
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
                          uses: %action-version%
                          with:
                              args: |
                                  --diff-start=&lt;GIT_START_HASH&gt;
                                  --diff-end=&lt;GIT_END_HASH&gt;
                          env:
                              QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
        </code-block>
    </tab>
    <tab title="Jenkins" group-key="jenkins">
            <code-block lang="groovy" emphasize-lines="19-20">
                pipeline {
                    environment {
                        QODANA_TOKEN=credentials('qodana-token')
                    }
                    agent {
                        docker {
                            args '''
                              -v "${WORKSPACE}":/data/project
                              --entrypoint=""
                              '''
                            image 'jetbrains/qodana-&lt;image&gt;'
                        }
                    }
                    stages {
                        stage('Qodana') {
                            steps {
                                sh '''
                                qodana \
                                --diff-start=&lt;GIT_START_HASH&gt; \
                                --diff-end=&lt;GIT_END_HASH&gt;
                                '''
                            }
                        }
                    }
                }
            </code-block>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
            <code-block lang="yaml" emphasize-lines="5-6">
                include:
                    - component: %gitlab-version%
                      inputs:
                          args: |
                              --diff-start=&lt;GIT_START_HASH&gt;
                              --diff-end=&lt;GIT_END_HASH&gt;
                              --image &lt;image&gt;
            </code-block>
    </tab>
    <tab title="TeamCity" group-key="teamcity">
        <p>In the runner configuration, find the <ui-path>Additional Qodana arguments</ui-path> field and
            specify the commit hashes:</p>
        <code-block lang="shell">
                --diff-start=&lt;GIT_START_HASH&gt; --diff-end=&lt;GIT_END_HASH&gt;
            </code-block>
    </tab>
</tabs>

</snippet>


## Change the Heap size
{id="docker-config-reference-docker-environment-heap-size"}

<link-summary>By default, the Heap size is set to 80% of the host RAM. You can configure this setting using the
    _JAVA_OPTIONS variable.</link-summary>

<p>By default, the Heap size is set to 80% of the host RAM. You can configure this setting using the
    <code>_JAVA_OPTIONS</code> variable: </p>

<tabs group="cli-settings">
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$" emphasize-lines="3">
            docker run \
               -v $(pwd):/data/project/ \
               -e _JAVA_OPTIONS=-Xmx6g \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               jetbrains/qodana-&lt;image&gt;
        </code-block>
    </tab>
    <tab title="Qodana CLI" group-key="qodana-cli">
        <code-block lang="shell" prompt="$" emphasize-lines="2">
            qodana scan \
               -e _JAVA_OPTIONS=-Xmx6g \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;"
        </code-block>
    </tab>
    <tab title="GitHub Actions" group-key="github-actions">
    <code-block lang="yaml" emphasize-lines="25">
        name: Qodana
        on:
            workflow_dispatch:
            pull_request:
            push:
                branches: # Specify your branches here
                    - main # The 'main' branch
                    - master # The 'master' branch
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
                      uses: %action-version%
                      with:
                          args: -e _JAVA_OPTIONS=-Xmx6g
                      env:
                          QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
    </code-block>
    </tab>
    <tab title="Jenkins" group-key="jenkins">
        <code-block lang="groovy" emphasize-lines="9">
            pipeline {
                environment {
                    QODANA_TOKEN=credentials('qodana-token')
                }
                agent {
                    docker {
                        args '''
                          -v "${WORKSPACE}":/data/project
                          -e _JAVA_OPTIONS=-Xmx6g
                          --entrypoint=""
                          '''
                        image 'jetbrains/qodana-&lt;image&gt;'
                    }
                }
                stages {
                    stage('Qodana') {
                        steps {
                            sh '''
                            qodana
                            '''
                        }
                    }
                }
            }
        </code-block>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
        <code-block lang="yaml" emphasize-lines="5">
            include:
                - component: %gitlab-version%
                  inputs:
                      args: |
                          -e _JAVA_OPTIONS=-Xmx6g
                          --image &lt;image&gt;
        </code-block>
    </tab>
    <tab title="TeamCity" group-key="teamcity">
        <p>In the runner configuration, find the <ui-path>Additional Docker arguments</ui-path> field and
            configure the heap size using the <code>_JAVA_OPTIONS</code> variable:</p>
        <code-block lang="shell">
            -e _JAVA_OPTIONS=-Xmx6g
        </code-block>
    </tab>
</tabs>

<p>To learn more about configuring the Heap, see the
    <a href="https://docs.oracle.com/cd/E19900-01/819-4742/abeik/index.html">Heap Tuning Parameters</a>
    of the Oracle documentation.</p>

## Override the idea.properties file
{id="docker-config-reference-docker-environment-idea-properties"}

<link-summary>The idea.properties file configures the default locations of the IDE files. You can override
    this file using the IDEA_PROPERTIES variable. </link-summary>

<note>This feature is not available in the <a href="dotnet.md">%dotnet%</a> linter.</note>

<p>The <code>idea.properties</code> configures the default locations of the IDE files.</p>

<p>You can override the <code>idea.properties</code> file using the <code>IDEA_PROPERTIES</code> variable:</p>

<tabs group="cli-settings">
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$" emphasize-lines="3">
            docker run \
               -v $(pwd):/data/project/ \
               -e IDEA_PROPERTIES=/data/project/idea.properties \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               jetbrains/qodana-&lt;image&gt;
        </code-block>
    </tab>
    <tab title="Qodana CLI" group-key="qodana-cli">
        <code-block lang="shell" prompt="$" emphasize-lines="2">
            qodana scan \
               -e IDEA_PROPERTIES=/data/project/idea.properties \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;"
        </code-block>
    </tab>
    <tab title="GitHub Actions" group-key="github-actions">
    <code-block lang="yaml" emphasize-lines="25">
        name: Qodana
        on:
            workflow_dispatch:
            pull_request:
            push:
                branches: # Specify your branches here
                    - main # The 'main' branch
                    - master # The 'master' branch
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
                      uses: %action-version%
                      with:
                          args: -e IDEA_PROPERTIES=/data/project/idea.properties
                      env:
                          QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
    </code-block>
    </tab>
    <tab title="Jenkins" group-key="jenkins">
        <code-block lang="groovy" emphasize-lines="9">
            pipeline {
                environment {
                    QODANA_TOKEN=credentials('qodana-token')
                }
                agent {
                    docker {
                        args '''
                          -v "${WORKSPACE}":/data/project
                          -e IDEA_PROPERTIES=/data/project/idea.properties
                          --entrypoint=""
                          '''
                        image 'jetbrains/qodana-&lt;image&gt;'
                    }
                }
                stages {
                    stage('Qodana') {
                        steps {
                            sh '''
                            qodana
                            '''
                        }
                    }
                }
            }
        </code-block>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
        <code-block lang="yaml" emphasize-lines="5">
            include:
                - component: %gitlab-version%
                  inputs:
                      args: |
                          -e IDEA_PROPERTIES=/data/project/idea.properties
                          --image &lt;image&gt;
        </code-block>
    </tab>
    <tab title="TeamCity" group-key="teamcity">
        <p>In the runner configuration, find the <ui-path>Additional Docker arguments</ui-path> field and
            configure the <code>IDEA_PROPERTIES</code> variable:</p>
        <code-block lang="shell">
            -e IDEA_PROPERTIES=/data/project/idea.properties
        </code-block>
    </tab>
</tabs>

## Configure root and non-root users
{id="docker-config-reference-docker-environment-run-non-root"}

<link-summary>Learn how to set up %product% for running as root and non-root users.</link-summary>

<tip>You can build your own Docker image with the required dependencies using our
    <a href="https://github.com/JetBrains/qodana-docker/blob/main/2025.2/python-community/Dockerfile">Dockerfile</a>.
</tip>

<tabs group="cli-settings">
    <tab id="docker-config-reference-docker-environment-docker" group-key="docker-image" title="Docker">
        <p>By default, a Docker container runs under the <code>root</code> user, so %instance% can
            read project information and write inspection results. Therefore, all files in the <code>results/</code>
            directory are owned by the <code>root</code> user after the run.</p>
        <p>To overcome this, you can run the container as a regular user:</p>
        <code-block lang="shell" prompt="$" emphasize-lines="2">
            docker run \
            -u $(id -u):$(id -g) \
            -v $(pwd):/data/project/ \
            -v &lt;results-directory&gt;:/data/results/ \
            -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
            jetbrains/qodana-&lt;image&gt;
        </code-block>
        <p>In this case, the <code>results/</code> directory on the host should already be created and owned by you.
            Otherwise, Docker will create it as the <code>root</code> user, and %instance% will not be able to write
            to it.</p>
    </tab>
    <tab id="docker-config-reference-docker-environment-teamcity-qodana-cli" group-key="qodana-cli" title="TeamCity and Qodana CLI">
        <p>TeamCity and <a href="https://github.com/JetBrains/qodana-cli">Qodana CLI</a> run %instance%
            using a current non-root user. This can be inconvenient if you wish to install dependencies
            using the <code>apt</code> tool invoked in the
            <a href="configuration-reference.md" anchor="Run+custom+commands"><code>bootstrap</code></a> section.</p>
        <p>To run %product% as a root user in TeamCity, add the <code>-u root</code> option in the
            <a href="teamcity.md" anchor="teamcity-qodana-runner"><ui-path>Additional Docker arguments</ui-path></a>
            field of the %product% runner configuration.</p>
        <p>To run Qodana CLI as a root user, you can append <code>-u root</code>
            option to the <code>qodana scan</code> command:</p>
        <code-block lang="shell" prompt="$">
            qodana scan -u root
        </code-block>
    </tab>
    <tab title="GitHub Actions" group-key="github-actions">
    <code-block lang="yaml" emphasize-lines="25">
        name: Qodana
        on:
            workflow_dispatch:
            pull_request:
            push:
                branches: # Specify your branches here
                    - main # The 'main' branch
                    - master # The 'master' branch
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
                      uses: %action-version%
                      with:
                          args: -u root
                      env:
                          QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
    </code-block>
    </tab>
    <tab title="Jenkins" group-key="jenkins">
        <code-block lang="groovy" emphasize-lines="9">
            pipeline {
                environment {
                    QODANA_TOKEN=credentials('qodana-token')
                }
                agent {
                    docker {
                        args '''
                          -v "${WORKSPACE}":/data/project
                          -u root
                          --entrypoint=""
                          '''
                        image 'jetbrains/qodana-&lt;image&gt;'
                    }
                }
                stages {
                    stage('Qodana') {
                        steps {
                            sh '''
                            qodana
                            '''
                        }
                    }
                }
            }
        </code-block>
    </tab>
    <tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
        <code-block lang="yaml" emphasize-lines="5">
            include:
                - component: %gitlab-version%
                  inputs:
                      args: |
                          -u root
                          --image &lt;image&gt;
        </code-block>
    </tab>
</tabs>


## Git submodules
{id="docker-config-reference-git-submodules"}

<p>To analyze repositories that use Git submodules accessed via SSH, you must authenticate Git
    operations within the Qodana Docker container. In this case, you need to configure an SSH agent and
    pass an SSH key with access to the submodule into the container as shown in the snippets below:</p>
<tabs group="cli-settings">
    <tab title="Docker image" group-key="docker-image">
        <code-block lang="shell" prompt="$" emphasize-lines="3-6">
            docker run \
               -v $(pwd):/data/project/ \
               -v "$SSH_AUTH_SOCK:/tmp/ssh_agent.sock" \
               -e SSH_AUTH_SOCK=/tmp/ssh_agent.sock \
               -e GIT_SSH_COMMAND=&quot;ssh -o StrictHostKeyChecking=no&quot; \
               -e QODANA_SKIP_SUBMODULE_UPDATE=true \
               jetbrains/qodana-&lt;image&gt; \
               --diff-start=&lt;GIT_START_HASH&gt;
        </code-block>
        <p>This command contains the following options:</p>
        <table>
            <tr>
                <td>Option</td>
                <td>Description</td>
            </tr>
            <tr>
                <td><code>-v "$SSH_AUTH_SOCK:/tmp/ssh_agent.sock"</code></td>
                <td>Mount the SSH agent socket into the container</td>
            </tr>
            <tr>
                <td><code>-e SSH_AUTH_SOCK=/tmp/ssh_agent.sock</code></td>
                <td>Set the SSH agent socket environment variable</td>
            </tr>
            <tr>
                <td><code>-e GIT_SSH_COMMAND=&quot;ssh -o StrictHostKeyChecking=no&quot;</code></td>
                <td>Disable strict host key checking for SSH operations</td>
            </tr>
            <tr>
                <td><code>-e QODANA_SKIP_SUBMODULE_UPDATE=true</code></td>
                <td>Skip Git submodule checkout, can be useful if the submodule checkout fails</td>
            </tr>
            <tr>
                <td><code>--diff-start=&lt;GIT_START_HASH&gt;</code></td>
                <td>Commit hash, see the <a href="analyze-pr.md" anchor="Analyze+pull+and+merge+requests"/> chapter for details</td>
            </tr>
        </table>
</tab>
    <tab title="Qodana CLI" group-key="qodana-cli">
        <code-block lang="shell" prompt="$" emphasize-lines="2-5">
            qodana scan \
               -v "$SSH_AUTH_SOCK:/tmp/ssh_agent.sock" \
               -e SSH_AUTH_SOCK=/tmp/ssh_agent.sock \
               -e GIT_SSH_COMMAND=&quot;ssh -o StrictHostKeyChecking=no&quot; \
               -e QODANA_SKIP_SUBMODULE_UPDATE=true \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               --diff-start=&lt;GIT_START_HASH&gt;
        </code-block>
        <p>This command contains the following options:</p>
        <table>
            <tr>
                <td>Option</td>
                <td>Description</td>
            </tr>
            <tr>
                <td><code>-v "$SSH_AUTH_SOCK:/tmp/ssh_agent.sock"</code></td>
                <td>Mount the SSH agent socket into the container</td>
            </tr>
            <tr>
                <td><code>-e SSH_AUTH_SOCK=/tmp/ssh_agent.sock</code></td>
                <td>Set the SSH agent socket environment variable</td>
            </tr>
            <tr>
                <td><code>-e GIT_SSH_COMMAND=&quot;ssh -o StrictHostKeyChecking=no&quot;</code></td>
                <td>Disable strict host key checking for SSH operations</td>
            </tr>
            <tr>
                <td><code>-e QODANA_SKIP_SUBMODULE_UPDATE=true</code></td>
                <td>Skip Git submodule checkout, can be useful if the submodule checkout fails</td>
            </tr>
            <tr>
                <td><code>--diff-start=&lt;GIT_START_HASH&gt;</code></td>
                <td>Commit hash, see the <a href="analyze-pr.md" anchor="Analyze+pull+and+merge+requests"/> chapter for details</td>
            </tr>
        </table>
    </tab>
    <tab title="GitHub Actions" group-key="github-actions">
    <code-block lang="yaml" emphasize-lines="19-21"><![CDATA[
        jobs:
            qodana-job:
                runs-on: ubuntu-latest
                steps:
                    - name: Checkout Repository
                      uses: actions/checkout@v4
                      with:
                          submodules: recursive  # clones submodules recursively

                    - name: Setup SSH Agent
                      uses: webfactory/ssh-agent@v0.9.0
                      with:
                          ssh-private-key: ${{ secrets.SUBMODULE_SSH_KEY }}
                
                    - name: 'Qodana Scan'
                      uses: %action-version%
                      with:
                          args: |
                              -v ${{ env.SSH_AUTH_SOCK }}:/tmp/ssh_agent.sock
                              -e SSH_AUTH_SOCK=/tmp/ssh_agent.sock
                              -e GIT_SSH_COMMAND=&quot;ssh -o StrictHostKeyChecking=no&quot;
                              -e QODANA_SKIP_SUBMODULE_UPDATE=true
                          upload-result: true
                          pr-mode: 'true'
                      env:
                          QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
        ]]>
    </code-block>
<p>Here, the <code>args</code> block contains the following options:</p>
<table>
    <tr>
        <td>Option</td>
        <td>Description</td>
    </tr>
    <tr>
        <td><code>-v ${{ env.SSH_AUTH_SOCK }}:/tmp/ssh_agent.sock</code></td>
        <td>Mount the SSH agent socket into the container</td>
    </tr>
    <tr>
        <td><code>-e SSH_AUTH_SOCK=/tmp/ssh_agent.sock</code></td>
        <td>Set the SSH agent socket environment variable</td>
    </tr>
    <tr>
        <td><code>-e GIT_SSH_COMMAND=ssh -o StrictHostKeyChecking=no</code></td>
        <td>Disable strict host key checking for SSH operations</td>
    </tr>
    <tr>
        <td><code>-e QODANA_SKIP_SUBMODULE_UPDATE=true</code></td>
        <td>Skip Git submodule checkout, can be useful if the submodule checkout fails</td>
    </tr>
</table>
</tab>
<tab title="GitLab CI/CD" group-key="gitlab-ci-cd">
<code-block lang="yaml" emphasize-lines="6-9">
    include:
        - component: %gitlab-version%
          inputs:
              image: &lt;image&gt;
              args: |
                  -v ${{ env.SSH_AUTH_SOCK }}:/tmp/ssh_agent.sock
                  -e SSH_AUTH_SOCK=/tmp/ssh_agent.sock
                  -e GIT_SSH_COMMAND=&quot;ssh -o StrictHostKeyChecking=no&quot;
                  -e QODANA_SKIP_SUBMODULE_UPDATE=true
</code-block>
    <p>Here, the <code>args</code> block contains the following options:</p>
    <table>
        <tr>
            <td>Option</td>
            <td>Description</td>
        </tr>
        <tr>
            <td><code>-v ${{ env.SSH_AUTH_SOCK }}:/tmp/ssh_agent.sock</code></td>
            <td>Mount the SSH agent socket into the container</td>
        </tr>
        <tr>
            <td><code>-e SSH_AUTH_SOCK=/tmp/ssh_agent.sock</code></td>
            <td>Set the SSH agent socket environment variable</td>
        </tr>
        <tr>
            <td><code>-e GIT_SSH_COMMAND=ssh -o StrictHostKeyChecking=no</code></td>
            <td>Disable strict host key checking for SSH operations</td>
        </tr>
        <tr>
            <td><code>-e QODANA_SKIP_SUBMODULE_UPDATE=true</code></td>
            <td>Skip Git submodule checkout, can be useful if the submodule checkout fails</td>
        </tr>
    </table>
</tab>
</tabs>

## Cache in Qodana CLI
{id="docker-config-reference-qodana-cli"}

<p><a href="https://github.com/JetBrains/qodana-cli">Qodana CLI</a> stores files in the
    <code>&lt;userCacheDir&gt;</code> directory, which is mentioned several times throughout this section. Here
    is the list of <code>&lt;userCacheDir&gt;</code> directory locations depending on the operating system:
</p>

<table>
    <tr>
        <td>Operating System</td>
        <td>Path</td>
    </tr>
    <tr>
        <td>macOS</td>
        <td><code>~/Library/Caches/</code></td>
    </tr>
    <tr>
        <td>Linux</td>
        <td><code>~/.cache/</code></td>
    </tr>
    <tr>
        <td>Windows</td>
        <td><code ignore-vars="true">%LOCALAPPDATA%\</code></td>
    </tr>
</table>

<p>If you run the <code>qodana init</code> command in the project directory, Qodana CLI will let you choose
    the <a href="linters.md">linter</a> that will be run during inspection, and save the choice in
    <code>qodana.yaml</code>. Once done, you do not need to specify the linter in the commands, which is
    shown throughout this section.</p>

<p>The detailed description of the <code>qodana init</code> command is available in the
    <a href="docker-image-configuration.topic" anchor="docker-config-reference-qodana-init"/> section.</p>

## Manage plugins

<link-summary>You can specify the plugins that will be downloaded and invoked during inspection.</link-summary>

You can specify the plugins that will be downloaded and invoked during inspection using the following YAML configuration:

```yaml
version: "1.0"

linter: <linter>

plugins:
  - id: <plugin.id>
```
{emphasize-lines="5-6"}

Here, `<plugin-id>` denotes the Plugin ID from [JetBrains Marketplace](https://plugins.jetbrains.com/). For example,
for [Grazie Professional](https://plugins.jetbrains.com/plugin/16136-grazie-professional), the Plugin ID will be `com.intellij.grazie.pro`. To find the Plugin ID, on the plugin
page click the **Overview** tab and then navigate to the **Additional Information** section.

Plugin cache is stored in the `/data/cache/plugins` directory.

To install third-party software required for your plugins, you can:

* Use the [`bootstrap`](configuration-reference.md#Run+custom+commands) key.
* Develop your custom `Dockerfile` that starts with `FROM jetbrains/qodana...`. You can use %instance% `Dockerfile`
  examples available on [GitHub](https://github.com/jetbrains/qodana-docker).

## Incorrect Formatting inspection

The  [`IncorrectFormatting`](%incorrect-formatting%) inspection consolidates multiple formatting errors contained in
a file into a single problem instead of listing every issue separately. Now, a single problem per file is displayed with
example snippets to help you fix issues faster.

This feature is available for all [linters](linters.md) except %cpp%, %clang%, and %dotnet-co%.

To start using it, enable the [`IncorrectFormatting`](https://www.jetbrains.com/help/inspectopedia/IncorrectFormatting.html) inspection in your %product%
[inspection profile](inspection-profiles.md) configuration, for example:

```yaml
version: "1.0"

linter: <linter>

profile:
  inspections:
    - inspection: IncorrectFormatting
      enabled: true
```
{emphasize-lines="7-8"}

## Specify a CMake preset

Customize the %cpp% linter by using [CMake presets](clang.md#Configure+compilers+and+environments). Invoke presets using
the `cpp` and `cmakePreset` options:

```yaml
version: "1.0"

linter: <linter>

cpp:
  cmakePreset: my-qodana-preset
```
{emphasize-lines="5-6"}

## Configure Java and Kotlin projects in monorepo

Using the `rootJavaProjects` key, you can specify which projects should be included in the analysis, for example:

```yaml
version: "1.0"

linter: <linter>

rootJavaProjects:
- "./gradleProject"
- "./mavenModule/pom.xml"
```
{emphasize-lines="5-7"}

By default, %product% recursively collects projects from subdirectories and imports them for analysis.
This change enables incremental analysis and fixes for projects where the analyzed project and VCS root are different.

## Comprehensive configuration examples

<link-summary>Navigate to the section to see the combination of different configuration options.</link-summary>

```yaml
version: "1.0"

linter: <linter>

failThreshold: 0
profile:
  name: qodana.recommended
  inspections:
    - inspection: SomeInspectionId
      enabled: true
    - inspection: AnotherInspectionId
      enabled: true
      ignore:
        - "relative/path"
        - "another/relative/path"
    - group: ALL
      enabled: true
      ignore: 
        - "asm-test/src/main/java/org"
        - "benchmarks"
        - "tools"
```

In the example above,
* `SomeInspectionId` inspection is explicitly enabled for all paths, although it is disabled in the profile
* `AnotherInspectionId` inspection is disabled for `relative/path` and `another/relative/path`
* no inspections are conducted over these paths: `asm-test/src/main/java/org`, `benchmarks`, `tools`


The following example combines multiple settings, including a quality gate, inspection profile customization, and path exclusions,
which are common in .NET project setups:

```yaml
version: "1.0"

# Run the %dotnet% linter in native mode
linter: qodana-dotnet
withinDocker: false

# Set a quality gate: fail if the number of problems exceeds 10
failThreshold: 10

# Use the qodana.recommended profile
profile:
  name: qodana.recommended

# Exclude specific paths from the analysis
  inspections:
    - group: ALL
      ignore:
        - "tests/"
        - "bin/"
        - "obj/"
    # Include an inspection not contained in the qodana.recommended profile
    - inspection: SomeSpecificInspectionId
      enabled: true

# Restore .NET dependencies
bootstrap: |+
  dotnet restore
```

Use this example while configuring the [%jvm%](jvm.md) linter:

```yaml
version: "1.0"

# Run the %jvm% linter
linter: qodana-jvm

# Set the JDK version
jdk:
  version: "17"

# Include Java projects for analysis
rootJavaProjects:
  - "./gradle-project"
  - "./maven-module/pom.xml"

# Quality gate settings
failureConditions:
  severityThresholds:
    any: 50       # Fail if total number of problems exceeds 50
    critical: 1   # Fail if there is at least 1 critical problem
    high: 2       # Fail if there are more than 2 high-severity problems
  testCoverageThresholds:
    fresh: 80     # Fail if fresh code coverage is below 80%
    total: 90     # Fail if total code coverage is below 90%

# Disable specific inspections
profile:
  inspections:
    - inspection: CheckDependencyLicenses 
      enabled: false # Disable license audit if not needed

# Include custom plugins
plugins:
  - id: com.intellij.grazie.pro

```



