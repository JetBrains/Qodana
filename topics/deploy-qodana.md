# Deployment

<show-structure for="chapter" depth="3"/>

<link-summary>Learn how to deploy %product% using various deployment options.</link-summary>

This section describes all deployment options available for %product%.

## Native mode

<link-summary>Native mode lets you run this linter without Docker.</link-summary>

By default, %instance% runs its linters using Docker based on Linux images.
In specific cases, you have to deal with private packages or run %instance% on the operating systems that
provide incomplete support for Docker.

To overcome this, %instance% supports native mode for the %jvm%, %jvm-co%, %php%, %js%, and %dotnet% linters.
You can run native mode on Linux, macOS, and Microsoft Windows.

In this case, %instance% reuses its execution environment, which lets you execute %instance% in exactly the same
environment as you use for building the projects, use the correct operating system, have access to all repository
credentials, and resolve dependencies.

<note>
    Native mode is currently in Early Access, which means it may not be reliable, may not work as intended, and may contain errors.
</note>

### Before you start

> Native mode is incompatible with Docker containers of %product%, which means that you run
> %product% either as a Docker container or in native mode.
> {style="note"}

#### General steps for all supported linters

In your operating system, save the `QODANA_TOKEN` environment variable containing the %instance% Cloud
[project token](project-token.md).

If you wish to run %instance% using a command line, then install [Qodana CLI](Quick-start.topic#quickstart-run-using-cli) on the machine where you will run it.

Starting from version 2023.3 of %instance%, the sanity inspection will report in case the `qodana.yaml` file
containing the `bootstrap` key is missing in your project directory. You can disable this inspection using the
`--disable-sanity` option, or add this inspection to a [baseline](baseline.topic).

#### %dotnet%

In addition to general steps, make sure that you have a proper version of the .NET SDK and all required
dependencies installed on your machine.

Build the project before inspecting it using %instance%. You can do it by using the [`bootstrap`](before-running-qodana.md) key of the
[`qodana.yaml`](qodana-yaml.md) file. The project building and artifact
packaging stages should occur before %instance% or simultaneously with it. Because running %instance% may affect the
project state and its files, it is advised to avoid reusing the same directory in your build pipelines any further.

You can also provide %instance% a pre-built project, or specify the build steps in your CI/CD pipeline. To remove
warnings related to project building, in your repository create the empty `qodana.yaml` file.

### How it works

> Native mode is incompatible with several Docker image-related options like `-l, --linter`,
`-e, --env`, and `-v, --volume`.
{style="note"}

> We recommend running the [%dotnet%](dotnet.md) linter in native mode on the same machine where you build a project
> because this can guarantee that %instance% has access to private NuGet feeds.
{style="note"}

You can enable native mode by using the `ide` option in the [`qodana.yaml`](qodana-yaml.md) file:

```yaml
ide: <linter>
```

This table contains the list of `<linter>` values:

| Linter name                | Linter code |
|----------------------------|-------------|
| [%jvm%](jvm.md)            | `QDJVM`     |
| [%jvm-co%](jvm.md)         | `QDJVMC`    |
| [%dotnet%](dotnet.md)      | `QDNET`     |
| [%php%](php.md)            | `QDPHP`     |
| [%js%](js.md)              | `QDJS`      |


This configuration tells %product% to download and employ the required JetBrains IDE binary file while running the
%product% linter.

Below are the examples showing how you can run %product% in native mode:

<tabs group="cli-settings">
    <tab title="Qodana CLI" group-key="native-mode-qodana-cli">
                <procedure>
                    <step>
                        <p>Make sure that the <code>QODANA_TOKEN</code> variable is defined in the environment and refers to a proper 
                        <a href="project-token.md">project token</a>. If necessary, you can define it:</p>
                        <code-block lang="shell" prompt="$">
                            QODANA_TOKEN=&lt;cloud-project-token&gt;
                        </code-block>
                    </step>
                    <step>
                        <p>If you have already enabled native mode using the <code>qodana.yaml</code> file, use this 
                        command:</p>
                        <code-block lang="shell" prompt="$">qodana scan</code-block>
                        <p>You can also run %product% without configuring the <code>qodana.yaml</code> file:</p>
                        <code-block lang="shell" prompt="$">
                            qodana scan \
                            &nbsp;&nbsp;&nbsp;--ide &lt;linter&gt;
                        </code-block>
                    </step>
                </procedure>
    </tab>
    <tab title="GitHub Actions" group-key="native-mode-github">
        <p>If you have already enabled native mode using the <code>qodana.yaml</code> file, you can use a 
        <a href="github.md" anchor="Basic+configuration">basic configuration</a> sample from the GitHub Actions section.</p>
        <p>To run %product% without configuring the <code>qodana.yaml</code> file, in your GitHub repository navigate to 
        a <a href="github.md" anchor="Basic+configuration">workflow configuration</a> file and specify the <code>--ide,&lt;linter&gt;</code> option:</p>
        <code-block lan="yaml">
        name: Qodana
        on:
          workflow_dispatch:
          pull_request:
          push:
            branches:
              - master
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
                uses: JetBrains/qodana-action@v2025.1
                with:
                  args: --ide,&lt;linter&gt;
                env:
                  QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
        </code-block>
    </tab>
</tabs>

## IDE integration

You can run %product% in several JetBrains IDEs, Visual Studio Code, and Visual Studio. See the
[](ide-integration.md) section for details.

## Qodana CLI 

%product% CLI is a simple cross-platform command-line tool that lets you run %product% linters with minimum effort.

<p>To run Qodana CLI in the default mode, you must have Docker or Podman installed and running locally.
    If you are using Linux, you should be able to run Docker under your current
    <a href="https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user">non-root user</a>.</p>
                <procedure id="qodana-cli-tab-procedure">
                    <step><p>Install Qodana CLI on your machine using available options:</p>
                        <tabs group="gs-cli">
                            <tab title="macOS and Linux" group-key="gs-macos-linux">
                                <p>Install with <a href="https://brew.sh/">Homebrew</a> (recommended):</p>
                                <code-block lang="shell" prompt="$">
                                    brew install jetbrains/utils/qodana
                                </code-block>
                                <p>Alternatively, you can install Qodana CLI using our installer:</p>
                                <code-block lang="shell" prompt="$">
                                    curl -fsSL https://jb.gg/qodana-cli/install | bash
                                </code-block>
                                <p>You can install a <code>nightly</code> or any other version the following way:</p>
                                <code-block lang="shell" prompt="$">
                                    curl -fsSL https://jb.gg/qodana-cli/install | bash -s -- nightly
                                </code-block>
                                <p>On Linux, you can also install %instance% using <a href="https://go.dev/doc/install">Go</a>:</p>
                                <code-block lang="shell" prompt="$">
                                    go install github.com/JetBrains/qodana-cli@latest
                                </code-block>
                            </tab>
                            <tab title="Microsoft Windows" group-key="gs-windows">
                                <p>Install with <a href="https://learn.microsoft.com/en-us/windows/package-manager/winget/">Windows Package Manager</a> (recommended):</p>
                                <code-block lang="shell">
                                    winget install -e --id JetBrains.QodanaCLI
                                </code-block>
                                <p>Install with <a href="https://chocolatey.org/">Chocolatey</a>:</p>
                                <code-block>
                                    choco install qodana
                                </code-block>
                                <p>Install with <a href="https://scoop.sh/">Scoop</a>:</p>
                                <code-block lang="shell">
                                    scoop bucket add jetbrains https://github.com/JetBrains/scoop-utils
                                    scoop install qodana
                                </code-block>
                            </tab>
                        </tabs>
                    </step>
                    <step>
                        <p>In the project root directory, declare the <code>QODANA_TOKEN</code> variable containing a 
                            <a href="project-token.md">project token</a>:</p>
                        <tabs group="gs-cli">
                            <tab title="macOS and Linux" group-key="gs-macos-linux">
                                <code-block lang="shell" prompt="$">
                                    QODANA_TOKEN=&lt;cloud-project-token&gt;
                                </code-block>
                            </tab>
                            <tab title="Microsoft Windows" group-key="gs-windows">
                                <code-block>
                                    set QODANA_TOKEN=&lt;cloud-project-token&gt;
                                </code-block>
                            </tab>
                        </tabs>
                    </step>
                    <step>
                        <p>Run %instance%:</p>
                        <tabs group="gs-cli">
                            <tab title="macOS and Linux" group-key="gs-macos-linux">
                                <code-block lang="shell" prompt="$">
                                    qodana scan
                                </code-block>
                            </tab>
                            <tab title="Microsoft Windows" group-key="gs-windows">
                                <code-block lang="shell">
                                    qodana scan
                                </code-block>
                            </tab>
                        </tabs>
                    </step>
                </procedure>

## Docker images

%product% is distributed across multiple Docker images. Essentially, the names of these Docker images are similar to the 
names of the linters. Details and configuration examples are available in the [](linters.md) section and other sections 
dedicated to specific linters referenced from that section.

## CI integration

You can run %product% using various CI/CD pipelines, as explained in the [](ci.md) section. 

For Azure Pipelines, CircleCI, GitHub Actions, GitLab CI/CD, and TeamCity, %product% provides native solutions.
To run %product% using Bitbucket Cloud, Jenkins, and Space Automation, you can use Docker images.

## Gradle plugin

The [Gradle Qodana plugin](https://plugins.gradle.org/plugin/org.jetbrains.qodana) provides the Gradle interface for running
code inspections provided by %instance%. To start, apply the Gradle plugin `org.jetbrains.qodana` in the Gradle
configuration file.

 <tabs group="languages">
  <tab title="Groovy" group-key="groovy">

Add the following to the `build.gradle` configuration file.

  ```groovy
  plugins {
      id "org.jetbrains.qodana" version "<plugin-version>"
  }
  ```

  </tab>
  <tab title="Kotlin DSL" group-key="kotlin-dsl">

Add the following to the `build.gradle.kts` configuration file:

  ```kotlin
  plugins {
      id("org.jetbrains.qodana") version "<plugin-version>"
  }
  ```

  </tab>
 </tabs>

<var name="qodana-label">Gradle Plugin Portal</var>
<note>

The latest version is: [![](https://img.shields.io/gradle-plugin-portal/v/org.jetbrains.qodana?color=green&label=%qodana-label%&logo=gradle)](https://plugins.gradle.org/plugin/org.jetbrains.qodana)

</note>


<tip>

For details on working with Gradle in IntelliJ IDEA, see the [IntelliJ IDEA Gradle documentation](https://www.jetbrains.com/help/idea/?Gradle).

</tip>

### `qodana { }` extension configuration
Properties available for configuration in the `qodana { }` top-level configuration closure:

| Name             | Description                                          | Type      | Default Value                           |
|------------------|------------------------------------------------------|-----------|-----------------------------------------|
| `projectPath`    | Path to the project folder to analyze.               | `String`  | `project.projectDir`                    |
| `resultsPath`    | Path to the directory to store task results.         | `String`  | `"${projectPath}/build/qodana/results"` |
| `cachePath`      | Path to the directory to store the generated report. | `String`  | `"${projectPath}/build/qodana/cache/"`  |

### Gradle Qodana Tasks

#### `qodanaScan`

Start Qodana in the project directory.

The task relies on the `qodana { }` extension configuration. However, it is also controlled by provided `arguments`.


#### Example

Add this to your Gradle configuration file:

- Groovy – `build.gradle`

  ```groovy
  plugins {
      // applies Gradle Qodana plugin to use it in project
      id "org.jetbrains.qodana" version "..."
  }
  
  qodana {
      // by default result path is $projectPath/build/results
      resultsPath = "some/output/path"
  }
  
  qodanaScan {
      arguments = ["--fail-threshold", "0"]
  }
  ```

- Kotlin – `build.gradle.kts`

  ```kotlin
  plugins {
      // applies Gradle Qodana plugin to use it in a project
      id("org.jetbrains.qodana") version "..."
  }
  
  qodana {
      // by default, the result path is $projectPath/build/results
      resultsPath.set("some/output/path")
  }
  
  qodanaScan {
      resultsPath.set("some/output/path")
      arguments.set(listOf("--fail-threshold", "0"))
  }
  ```

> **Note:** Docker requires at least 4GB of memory. Set it in the Docker `Preferences > Resources > Memory` section.

Now you can run analyses using the `qodanaScan` Gradle task:

```bash
gradle qodanaScan 
// or
./gradlew qodanaScan
```

A complete guide for options and configuration of `arguments` parameters can be found on [Qodana CLI docs page](https://github.com/JetBrains/qodana-cli#scan).

