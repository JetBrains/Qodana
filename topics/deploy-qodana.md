# Deployment options

<show-structure for="chapter" depth="3"/>

<link-summary>Learn how to deploy %product% using various deployment options.</link-summary>

This section describes all deployment options available for %product%.

## System requirements

<table>
  <tr>
    <td>Requirement</td>
    <td>Minimum</td>
    <td>Recommended</td>
  </tr>
  <tr>
    <td>RAM</td>
    <td>2 GB of free RAM</td>
    <td>8 GB of total system RAM</td>
  </tr>
  <tr>
    <td>CPU</td>
    <td>Any modern CPU</td>
    <td>Multicore CPU. %product% supports multithreading for different operations and processes
        making it faster the more CPU cores it can use.</td>
  </tr>
  <tr>
    <td>Disk space</td>
    <td>2.5 GB + space for all dependencies and cache</td>
    <td>At least 5 GB of free space + space for all dependencies and cache</td>
  </tr>
  <tr>
    <td>Operating system</td>
    <td><p>Officially released versions of the following:</p>
      <list>
        <li>Microsoft Windows 10 1809 64-bit or later</li>
        <li>Windows Server 2019 64-bit or later</li>
        <li>macOS 12.0 or later</li>
        <li>Two latest versions of Ubuntu LTS or Fedora Linux distributions that meet the following requirements:
          <list>
            <li>Linux kernel version 6.x</li>
            <li><a href="https://ftp.gnu.org/gnu/libc/">GLIBC</a> 2.28 or later</li>
          </list>
          <p>Pre-release versions are not supported.</p>
        </li>
      </list>
    </td>
    <td><p>The latest versions of the following:</p>
      <list>
        <li>Microsoft Windows 64-bit</li>
        <li>macOS</li>
        <li>Ubuntu LTS or Fedora Linux</li>
      </list>
    </td>
  </tr>
</table>

## Native mode
{id="deploy-qodana-native-mode"}

<link-summary>Native mode lets you run this linter without Docker.</link-summary>

By default, %instance% runs its linters using Docker based on Linux images.
In specific cases, you have to deal with private packages or run %instance% on the operating systems that
provide incomplete support for Docker.

To overcome this, %instance% supports native mode for the following linters: 

| Linter                   | Linter name          |
|--------------------------|----------------------|
| [%jvm%](jvm.md)          | `%jvm-linter%`       |  
| [%jvm-co%](jvm.md)       | `%jvm-co-linter%`    |  
| [%php%](php.md)          | `%php-linter%`       |  
| [%js%](js.md)            | `%js-linter%`        |  
| [%dotnet%](dotnet.md)    | `%dotnet-linter%`    |  
| [%python%](python.md)    | `%python-linter%`    |  
| [%python-co%](python.md) | `%python-co-linter%` |  
| [%go%](golang.md)        | `%go-linter%`        |  

You can run native mode on Linux, macOS, and Microsoft Windows.

In this case, %instance% reuses its execution environment, which lets you execute %instance% in exactly the same
environment as you use for building the projects, use the correct operating system, have access to all repository
credentials, and resolve dependencies.

<note>
    Native mode is currently in Early Access, which means it may not be reliable, may not work as intended, and may contain errors.
</note>

### Before you start

> Native mode is incompatible with Docker containers of %product%, which means that you can run
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

Build the project before inspecting it using %instance%. You can do it by using the [`bootstrap`](qodana-yaml.md#Run+custom+commands) key of the
[`qodana.yaml`](qodana-yaml.md) file. The project building and artifact
packaging stages should occur before %instance% or simultaneously with it. Because running %instance% may affect the
project state and its files, it is advised to avoid reusing the same directory in your build pipelines any further.

You can also provide %instance% a pre-built project, or specify the build steps in your CI/CD pipeline. To remove
warnings related to project building, in your repository create the empty `qodana.yaml` file.

### How native mode works

> Native mode is incompatible with several Docker image-related options like `--image`,
`-e, --env`, and `-v, --volume`.
{style="note"}

> We recommend running the [%dotnet%](dotnet.md) linter in native mode on the same machine where you build a project
> because this can guarantee that %instance% has access to private NuGet feeds.
{style="note"}

You can enable native mode by using the `--within-docker false` [option](docker-image-configuration.topic#docker-config-reference-qodana-scan)
in combination with the `--linter <linter-name>` option. These options tell %product% to download and employ the required JetBrains 
IDE binary file while running a %product% linter.  

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
                        <p>Run the <code>qodana scan</code> command:</p>
                        <code-block lang="shell" prompt="$">
                            qodana scan \
                            &nbsp;&nbsp;&nbsp;--linter &lt;linter-name&gt; \
                            &nbsp;&nbsp;&nbsp;--within-docker false
                        </code-block>
                    </step>
                </procedure>
    </tab>
    <tab title="GitHub Actions" group-key="native-mode-github">
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
                uses: %action-version%
                with:
                  args: | 
                    --linter,&lt;linter-name&gt;,
                    --within-docker,false
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

%product% is also distributed across multiple Docker images listed in the table below:

<table>
    <tr>
        <td>Linter</td>
        <td>Docker image</td>
    </tr>
    <tr>
      <td>
            <p><a href="jvm.md">%jvm%</a></p>
      </td>
        <td>
            <p><code>%jvm-image%</code></p>
        </td>
    </tr>
    <tr>
      <td>
            <p><a href="jvm.md">%jvm-co%</a></p>
      </td>
        <td>
            <p><code>%jvm-co-image%</code></p>
        </td>
    </tr>
    <tr>
      <td>
            <p><a href="jvm.md">%jvm-co-a%</a></p>
      </td>
        <td>
            <p><code>%jvm-co-a-image%</code></p>
        </td>
    </tr>
    <tr>
      <td>
            <p><a href="jvm.md">%jvm-a%</a></p>
      </td>
        <td>
            <p><code>%jvm-a-image%</code></p>
        </td>
    </tr>
    <tr>
      <td>
            <p><a href="php.md">%php%</a></p>
      </td>
        <td>
            <p><code>%php-image%</code></p>
        </td>
    </tr>
    <tr>
      <td>
            <p><a href="js.md">%js%</a></p>
      </td>
        <td>
            <p><code>%js-image%</code></p>
        </td>
    </tr>
    <tr>
      <td>
            <p><a href="dotnet.md">%dotnet%</a></p>
      </td>
        <td>
            <p><code>%dotnet-image%&lt;-privileged&gt;</code>*</p>
        </td>
    </tr>
    <tr>
      <td>
            <p><a href="dotnet.md">%dotnet-co%</a></p>
      </td>
        <td>
            <p><code>%dotnet-co-image%&lt;-privileged&gt;</code>*</p>
        </td>
    </tr>
    <tr>
      <td>
            <p><a href="python.md">%python%</a></p>
      </td>
        <td>
            <p><code>%python-image%</code></p>
        </td>
    </tr>
    <tr>
      <td>
            <p><a href="python.md">%python-co%</a></p>
      </td>
        <td>
            <p><code>%python-co-image%</code></p>
        </td>
    </tr>
    <tr>
      <td>
            <p><a href="golang.md">%go%</a></p>
      </td>
        <td>
            <p><code>%go-image%</code></p>
        </td>
    </tr>
    <tr>
      <td>
            <p><a href="ruby.md">%ruby%</a></p>
      </td>
        <td>
            <p><code>%ruby-image%&lt;-ruby3.X&gt;&lt;-privileged&gt;</code>*</p>
        </td>
    </tr>
    <tr>
      <td>
            <p><a href="clang.md">%clang%</a></p>
      </td>
        <td>
            <p><code>%clang-image%&lt;-clangXX&gt;</code>*</p>
        </td>
    </tr>
    <tr>
      <td>
            <p><a href="clang.md">%cpp%</a></p>
      </td>
        <td>
            <p><code>%cpp-image%&lt;-clangXX&gt;&lt;-privileged&gt;</code>*</p>
        </td>
    </tr>
</table>

\* Using optional tags, you can pull pre-configured %product% images:

* For the %cpp% and %clang% linters, use the `-clangXX` tag to specify the [Clang-Tidy](https://clang.llvm.org/extra/clang-tidy) version from 15 to 18.
* For the %ruby% linter, use the `-ruby3.X` tag to specify the Ruby version from 3.1 to 3.4. If not specified, version 3.4 will be used.

  Using the `-privileged` tag, you can run %product% in the privileged mode to execute commands that require root access. 
  In this case, Qodana comes with a default `qodana` user that possesses root privileges and does not require a password.
  To use this mode with the %cpp%, %clang%, and %ruby% linters, the `-clangXX` and `-ruby3.X` tags should be specified, respectively.

To specify Docker images from the table, use the `--image` [option](docker-image-configuration.topic#docker-config-reference-qodana-scan). 

### Different Docker contexts or Podman

%product% uses Docker CLI to communicate with the container engine and employs a Docker context enabled at the time of execution. 
For example, to use Podman as your container engine, you will need to either:

* In Podman Desktop, enable Docker compatability mode and disable Docker so that Podman listens on `/var/run/docker.sock`, or
* Use the Podman socket to create a Docker context. If you are using Podman Desktop, you can find the socket path under **Settings > Resources**

You can confirm which engine is activated by running the `docker version` command.

## CI integration

You can run %product% using various CI/CD pipelines, as explained in the [](ci.md) section. 

For Azure Pipelines, CircleCI, GitHub Actions, GitLab CI/CD, and TeamCity, %product% provides native solutions.
To run %product% using Bitbucket Cloud, and Jenkins, you can use Docker images.

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

