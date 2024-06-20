[//]: # (title: Native mode)

<link-summary>The Qodana for .NET linter supports the native mode, which lets you run this linter without Docker.</link-summary>

By default, %instance% runs its linters using Docker based on Linux images. 
In specific cases, you have to deal with private packages or run %instance% on the operating systems that
provide incomplete support for Docker. 

To overcome this, %instance% supports the native mode for the [](qodana-dotnet.md) linter. 
In this case, %instance% reuses its execution environment, which lets you execute %instance% in exactly the same 
environment as you use for building the projects, use the correct operating system, have access to all repository
credentials, and resolve dependencies. 

## Before you start

> The native mode is incompatible with Docker containers of %product%, which means that you run
> the [](qodana-dotnet.md) linter either as a Docker container or in a native mode.
> {style="note"}

Make sure that you have a proper version of the .NET SDK and all required dependencies installed on your machine.

Build the project before inspecting it using %instance%. You can do it by using the [`bootstrap`](before-running-qodana.md)
key of the [`qodana.yaml`](qodana-yaml.md) file.

The project building and artifact packaging stages should occur before %instance% or simultaneously with it. Because 
running %instance% may affect the project state and its files, we recommend that you avoid reusing the same directory 
in your build pipelines any further. 

You can also provide %instance% with a pre-built project, or specify the build steps in your CI/CD pipeline. In this 
case, in your repository create the empty `qodana.yaml` file to eliminate warnings related to project building.

In your operating system, save the `QODANA_TOKEN` environment variable containing the %instance% Cloud
[project token](project-token.md).

[Install Qodana CLI](Quick-start.topic#quickstart-run-using-cli) on the machine where you plan to run %instance% locally.

Starting from the version 2023.3 of %instance%, the sanity inspection will report in case the `qodana.yaml` file 
containing the `bootstrap` key is missing in your project directory. The [`bootstrap`](before-running-qodana.md) 
key should contain instructions for building the project. If you do not wish to build the project, disable
this inspection using the `--disable-sanity` option, add this inspection to a [baseline](baseline.topic), or create the `qodana.yaml`
file that will contain the `ide: QDNET` configuration. 

We recommend running the native mode on the same machine where you build a project because this can guarantee
that %instance% has access to private NuGet feeds.

## How it works

> The native mode is incompatible with several Docker image-related options like `-l, --linter`,
`-e, --env`, and `-v, --volume`.
> {style="note"}

You can enable the native mode ba saving this configuration in the [`qodana.yaml`](qodana-yaml.md) file: 

```yaml
ide: QDNET
```

This configuration tells %product% to download and employ the required JetBrains IDE binary file while running.

Below are the examples showing how you can run %product% in the native mode:

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
                        <p>If you have already enabled the native mode using the <code>qodana.yaml</code> file, use this 
                        command:</p>
                        <code-block lang="shell" prompt="$">qodana scan</code-block>
                        <p>You can also run %product% without configuring the <code>qodana.yaml</code> file:</p>
                        <code-block lang="shell" prompt="$">
                            qodana scan \
                            &nbsp;&nbsp;&nbsp;--ide QDNET
                        </code-block>
                    </step>
                </procedure>
    </tab>
    <tab title="GitHub Actions" group-key="native-mode-github">
        <p>If you have already enabled the native mode using the <code>qodana.yaml</code> file, you can use a 
        <a href="github.md" anchor="Basic+configuration">basic configuration</a> sample from the GitHub Actions section.</p>
        <p>To run %product% without configuring the <code>qodana.yaml</code> file, in your GitHub repository navigate to 
        a <a href="github.md" anchor="Basic+configuration">workflow configuration</a> file and specify the <code>--ide,QDNET</code> option:</p>
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
                uses: JetBrains/qodana-action@v2024.1
                with:
                  args: --ide,QDNET
                env:
                  QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
        </code-block>
    </tab>
</tabs>
