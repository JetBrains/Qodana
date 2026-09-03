[//]: # (title: Preparing your project)

<link-summary>You can use the bootstrap key to prepare your project for analyzing by Qodana.</link-summary>

During analyses, %product% linters may report that some inspections cannot find classes, packages, files or cannot resolve references
although linters related to [JVM](jvm.md), [.NET](dotnet.md) and [Golang](golang.md) try to figure out the 
build system and project structure automatically.

When you run %product% on a CI/CD platform, project dependencies are not installed automatically, except for the
JVM/Android, Go, and .NET linters that resolve them from the project build system. For all other technologies, you need
to install the dependencies yourself. In these cases, %instance% needs a bit of help:

* Install third-party packages or libraries
* Run a program that sets up the build environment 

These actions are carried out using the `bootstrap` [key](qodana-yaml.md#Run+custom+commands) of the `qodana.yaml` file
contained in the root directory of your project:

```yaml
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
> [`/data/results`](docker-image-configuration.topic#docker-config-reference-overview-logs) directory.

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
