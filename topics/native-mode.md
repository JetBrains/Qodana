[//]: # (title: Native mode)

Starting from version 2023.3, %product% supports the native mode for the [](qodana-dotnet.md) mode by default. 
It means that you can run %product% without its Docker image. Besides that, the native mode lets you inspect .NET 
framework projects and have access to private NuGet feeds.   

The native mode is incompatible with several Docker image-related commands like `-l, --linter`, ` -e, --env`, and 
`-v, --volume`. 

Besides that, you cannot use the `QODANA_TOKEN` Docker environment variable. 

## Before you start

Make sure that you have a proper version of the .NET SDK installed on your machine. 

Build the project before inspecting it using %product%. You can do it by using the [`bootstrap`](before-running-qodana.md)
option of the [`qodana.yaml`](qodana-yaml.md) file.

The project and artifact packaging stages should occur before %product% or simultaneously with it, and %product% should 
not share the same directory because it can overwrite the data contained in it.

In your operating system, save the `QODANA_CLOUD` environment variable containing the %product% Cloud
[project token](project-token.md).

Install [Qodana CLI](https://github.com/JetBrains/qodana-cli) on the machine where you plan to run %product%.

Starting from the version 2023.3 of %product%, the sanity inspection will report in case the `qodana.yaml` file 
containing the `bootstrap` option is missing in your project directory. The [`bootstrap`](before-running-qodana.md) 
option should contain instructions for building the project. If you do not wish to build the project, you can disable
this inspection using the `--disable-sanity` option, or add this inspection to a [baseline](baseline.xml). 

We recommend running the native mode on the same machine where you build a project because this can guarantee
that %product% has access to private NuGet feeds.

## How it works

Assuming that you have already installed [Qodana CLI](https://github.com/JetBrains/qodana-cli) and followed the instructions
from the [previous section](#Before+you+start), in the project directory run this command: 

```shell
qodana scan \
   --ide QDNET
```

This command will download the required JetBrains IDE binary file and start %product%. Instead of `--ide QDNET`, you can
specify the absolute path to the JetBrains IDE binary file. 