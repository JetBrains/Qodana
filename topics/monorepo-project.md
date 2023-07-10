[//]: # (title: Inspect a monorepo project)

A monorepo is a repository containing several projects, for example:

```text
root/
    backend/
    frontend/
    .git/
```

In this example,
the `backend/` folder contains a Java project,
the `frontend/` folder contains a JavaScript project,
and the `.git/` folder contains VCS-related information.

This section explains how to prepare the projects from this example monorepo so that %product% can inspect them using
either the [Docker images](docker-images.md) or the [Qodana Scan GitHub Action](github.md).

## Prepare your project

<!--
Placing the project-specific `qodana.yaml` files in the root folder
has these advantages:

* Any relative paths in the project-specific `qodana.yaml` files
  are resolved intuitively because the effective `qodana.yaml` is
  in the same directory as the project-specific `qodana.yaml` files.

And these disadvantages:

* In a monorepo containing many projects,
  the root folder gets cluttered with these files.
* https://github.com/SchemaStore/schemastore only recognizes a qodana.yaml
  file for completion and validation if it is named exactly `qodana.yaml`.
  Naming it `qodana-backend.yaml` disables all this editor support.

The alternative is to place each `qodana.yaml` in its own project directory,
which reverses the above advantages and disadvantages.
-->

%product% provides several [linters](linters.md), and each linter can inspect a specific set of programming languages.
Because there is no linter that can inspect Java and JavaScript at the same time, %product% needs to be run twice over
the repository, once for each project.

To configure %product% for inspecting two projects, you need to create two separate [`qodana.yaml`](qodana-yaml.md) 
files. %product% also expects `qodana.yaml` to be contained in the root folder. This means that before 
running %product% on the project from the `backend/` folder, that project's `qodana.yaml` file needs to be copied to 
the root folder. If you run %product% using [Docker](#Docker), you can copy files using the 
[`bootstrap`](before-running-qodana.md) configuration option in `qodana.yaml`, for example:

<!--
Implementation note: qodana.yaml is read by several programs:
1. By qodana-cli outside the Docker container, to determine the linter to use.
2. By Qodana inside the Docker container, to load the rest of the configuration.

Copying `qodana.yaml` happens between these two steps.
This means that the project's qodana.yaml cannot affect the linter to be chosen.
* In the case of Docker, the linter is specified on the command line,
  so the linter from `qodana.yaml` is ignored anyway.
* In the case of Qodana CLI, the project-specific `qodana.yaml` needs to be copied
  to the root folder before running `qodana scan`.
-->
```yaml
bootstrap: cp qodana-backend.yaml qodana.yaml
```

When %product% runs, it uses the `.git/` folder for linking detected problems to the corresponding
source code in a Git repository, and for exploring inspection reports [from within your IDE](qodana-ide-plugin.md).
<!--
TODO: Clarify whether the "from within your IDE" part really depends on `.git/`
or rather on the path that is mounted to `/data/project`.
-->

The `qodana-backend.sarif.json` and `qodana-frontend.sarif.json` files can contain [baseline](baseline.xml)
data for the `backend` and `frontend` projects.

Here are the contents of the `root/` folder: 

<!-- Alternative: put each qodana.yaml in its corresponding project directory. -->
```text
root/
    backend/
    frontend/
    .git/
    qodana-backend.yaml
    qodana-backend.sarif.json
    qodana-frontend.yaml
    qodana-frontend.sarif.json
```

## Run Qodana

After [preparing the project](#Prepare+your+project), you can inspect your code using Docker or 
GitHub Actions.

### Docker

You can inspect your monorepo in the `root/` folder using either [Docker](docker-images.md) or 
[%product% CLI](https://github.com/JetBrains/qodana-cli).

<note>You can use %product% CLI only with Azure and CircleCI.</note>

<tabs>
    <tab id="monorepo-docker-image-tab" title="Docker">
        <code style="block" lang="shell" prompt="$">
            docker run --rm \ 
              -v "$PWD":/data/project/ \
              jetbrains/qodana-jvm:latest-eap \
              --source-directory backend \
              --baseline qodana-backend.sarif.json
        </code>
        <code style="block" lang="shell" prompt="$">
            docker run --rm \ 
              -v "$PWD":/data/project/ \
              jetbrains/qodana-js:latest-eap \
              --source-directory frontend \
              --baseline qodana-frontend.sarif.json
        </code>
    </tab>
    <tab id="monorepo-cli-tab" title="Qodana CLI">
        <code style="block" lang="shell" prompt="$">
            qodana scan \
              --linter jetbrains/qodana-jvm:latest-eap \
              --source-directory backend \
              --baseline qodana-backend.sarif.json
        </code>
        <code style="block" lang="shell" prompt="$">
            qodana scan \
              --linter jetbrains/qodana-js:latest-eap \
              --source-directory frontend \
              --baseline qodana-frontend.sarif.json
        </code>
    </tab>

</tabs>

### GitHub Actions

You can use the [Qodana Scan](github.md) GitHub action for running %product% on GitHub. Here is the GitHub action
configuration for inspecting the monorepo:

```yaml
name: Qodana
on:
  workflow_dispatch:
  pull_request:
  push:
jobs:
  qodana-backend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
      - name: 'Use qodana-backend config'
        run: cp qodana-backend.yaml qodana.yaml

      - name: 'Qodana Backend'
        uses: JetBrains/qodana-action@v2023.2.0
        with:
          args: |
            --source-directory,backend,
            --baseline,qodana-backend.sarif.json
          artifact-name: qodana-backend
  qodana-frontend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
      - name: 'Use qodana-frontend config'
        run: cp qodana-frontend.yaml qodana.yaml

      - name: 'Qodana Frontend'
        uses: JetBrains/qodana-action@v2023.2.0
        with:
          args: |
            --source-directory,frontend,
            --baseline,qodana-frontend.sarif.json
          artifact-name: qodana-frontend
```