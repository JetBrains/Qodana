[//]: # (title: Configuration overview)

You have the following configuration approaches:

1. Configuring %product% via a [YAML-formatted](configuration-reference.md) file, typically named `qodana.yaml`, is suitable for settings that require lengthy 
commands, such as inspection configuration, [bootstrap](configuration-reference.md#Run+custom+commands), and other settings that are not convenient to configure otherwise. 
Once a YAML configuration is saved, you can reuse it across different instances of Qodana.

1. Using [configuration capabilities](configuration-reference.md) of the tools that are running %product% like Docker, 
[Qodana CLI](Quick-start.topic#quickstart-run-using-cli), [IDEs](ide-integration.md), and [CI/CD tools](ci.md). 

    Settings like [linter](linters.md) or [quality gate](quality-gate.topic) can be set up using both methods.
    In this case, tool configurations override configurations saved in a YAML-formatted file.  

    > The configured major version of a %product% linter (20**.*) should match the configured linter version specified in the `qodana.yaml` file.
    {style="note"}

1. Configuring inspection profiles lets you specify inspections and paths in your codebase that should be used for analysis by %product%. 
You can configure and use the [existing inspection profiles](inspection-profiles.md#inspection-profiles-existing-profiles) or create [your custom profiles](inspection-profiles.md#inspection-profiles-custom-profiles) from scratch.

1. If the existing inspections do not fit your needs, you can develop your own inspections using the
[](flexinspect.md) feature, [Roslyn analyzers](use-roslyn-analyzer.md), or [structural search patterns](extending-qodana-structural-search.topic),
which you can apply in your inspection profile. Alternatively, you can use [plugins](extending-qodana-plugins.topic)
that will extend the inspection capabilities of %instance% or develop
[your own plugin](https://plugins.jetbrains.com/docs/intellij/github-template.html).

1. Finally, you can override the default JDK versions shipped with %product%, see the [](jvm.md#Configuring+the+JDK) section for details.

## Performance optimization

To make %product% work better during the project setup stage, you can follow the recommendations below.

First, specify the [`--cache-dir`](configuration-reference.md#docker-config-reference-cache-dependencies) option,
the `use-caches` input argument in case of [CI/CD support](ci.md), or the `/data/caches` directory in
the Docker container of a linter after the first linter analysis. Cache contains data related to project structure, indexes,
dependencies, which makes subsequent analyses faster. However, in case of significant and disruptive changes of your
project or %product% version updates, it may be beneficial to reset cache.

You can also store your IntelliJ IDEA setting files in the `.idea` directory, for example:
* The `modules.xml` file improves project structure parsing
* The language-specific files like `kotlinc.xml` or `php.xml` provide information about compiler versions and options
* The `*.iml` files contain information about directories

Make sure that your project is correctly configured by looking at the
`<results-dir-artifact>/projectStructure` directory after the first analysis. Also, make sure that:

* The project imports work correctly
* The tooling that you use matches the configured versions
* Project dependency pooling works correctly, as it should be done only once if you are using cache
* Analyses do not show [unexpected problems](inspection-profiles.md#inspection-profiles-existing-profiles) because they are a key indicator of configuration issues

## Docker image paths

<link-summary>See the list of Docker image paths.</link-summary>

<table>
    <tr>
        <td>Path</td>
        <td>Description</td>
    </tr>
    <tr>
        <td>
            <code>/data/project</code>
        </td>
        <td>Root directory of the project to be analyzed</td>
    </tr>
    <tr>
        <td>
            <code>/data/results</code>
        </td>
        <td>Directory to store the analysis reports</td>
    </tr>
    <tr>
        <td>
            <code>/opt/idea</code>
        </td>
        <td>Directory containing the IDE distribution</td>
    </tr>
    <tr>
        <td>
            <code>/root/.config/idea</code>
        </td>
        <td>Directory where the IDE contains configuration</td>
    </tr>
    <tr>
        <td>
            <code>/data/profile.xml</code>
        </td>
        <td><p>Used if a profile was not previously configured either via the CLI or the <code>qodana.yaml</code>
            file.</p>
        </td>
    </tr>
</table>

<p>For Maven and Gradle projects, %instance% uses the following directories to access third-party libraries:</p>

<table>
    <tr>
        <td>Path</td>
        <td>Description</td>
    </tr>
    <tr>
        <td><code>/data/cache/.m2</code></td>
        <td>Maven project dependencies</td>
    </tr>
    <tr>
        <td><code>/data/cache/gradle</code></td>
        <td>Gradle project dependencies</td>
    </tr>
</table>

<p>Mounting these directories saves %instance% from downloading all dependencies again while using these linters:</p>
    <list>
        <li><a href="jvm.md">%jvm%</a></li>
        <li><a href="jvm.md">%jvm-co%</a></li>
        <li><a href="jvm.md">%jvm-a%</a></li>
    </list>
