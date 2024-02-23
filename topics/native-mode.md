[//]: # (title: Native mode)

<link-summary>The Qodana for .NET linter supports the native mode, which lets you run this linter without Docker.</link-summary>

By default, %instance% runs its linters using Docker based on Linux images. 
In specific cases, you have to deal with private packages or run %instance% on the operating systems that
provide incomplete support for Docker. 

To overcome this, starting from version 2023.3 %instance% supports the native mode for the [](qodana-dotnet.md) mode by default. 
In this case, %instance% reuses its execution environment, which lets you execute %instance% in exactly the same 
environment as you use for building the projects, use the correct operating system, have access to all repository
credentials, and resolve dependencies. 

## Before you start

<note>The native mode is incompatible with several Docker image-related options like <code>-l, --linter</code>, 
<code>-e, --env</code>, and <code>-v, --volume</code>. </note>

Make sure that you have a proper version of the .NET SDK and all required dependencies installed on your machine.

Build the project before inspecting it using %instance%. You can do it by using the [`bootstrap`](before-running-qodana.md)
option of the [`qodana.yaml`](qodana-yaml.md) file.

The project building and artifact packaging stages should occur before %instance% or simultaneously with it. Because 
running %instance% may affect the project state and its files, we recommend that you avoid reusing the same directory 
in your build pipelines any further. 

You can also provide %instance% with a pre-built project, or specify the build steps in your CI/CD pipeline. In this 
case, in your repository create the empty `qodana.yaml` file to eliminate warnings related to project building.

In your operating system, save the `QODANA_TOKEN` environment variable containing the %instance% Cloud
[project token](project-token.md).

[Install Qodana CLI](Quick-start.topic#quickstart-run-using-cli) on the machine where you plan to run %instance%.

Starting from the version 2023.3 of %instance%, the sanity inspection will report in case the `qodana.yaml` file 
containing the `bootstrap` option is missing in your project directory. The [`bootstrap`](before-running-qodana.md) 
option should contain instructions for building the project. If you do not wish to build the project, you can disable
this inspection using the `--disable-sanity` option, add this inspection to a [baseline](baseline.topic), or create the `qodana.yaml`
file that will contain the `ide: QDNET` configuration. 

We recommend running the native mode on the same machine where you build a project because this can guarantee
that %instance% has access to private NuGet feeds.

## How it works

Assuming that you have already installed [Qodana CLI](https://github.com/JetBrains/qodana-cli) and followed the instructions
from the [previous section](#Before+you+start), you have two options for running %instance% in the native mode:  

<tabs group="cli-settings">
    <tab title="Qodana CLI" group-key="native-mode-qodana-cli">
        <code-block lang="shell" prompt="$">
            qodana scan \
            &nbsp;&nbsp;&nbsp;--ide QDNET
        </code-block>
        <p>This command will download the required JetBrains IDE binary file and start %instance%.</p>
        <p>If you have already specified <code>ide: QDNET</code> in the <code>qodana.yaml</code> file, you do not have
        to use it in this command, so this command is already sufficient:</p>
        <code-block lang="shell" prompt="$">qodana scan</code-block>
    </tab>
    <tab title="qodana.yaml" group-key="native-mode-qodana-yaml">
    <p>In the <code>qodana.yaml</code> file, save the <code>ide: QDNET</code> configuration. Run %instance% using this 
    command:</p> 
    <code-block lang="shell" prompt="$">qodana scan</code-block>
    </tab>
</tabs>
