[//]: # (title: Inspect a monorepo project)

<var name="github-secret" value="https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository"/>

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

This section explains how to prepare the projects from this example monorepo so that %product% can inspect them using:

* [Qodana CLI](https://github.com/JetBrains/qodana-cli)
* [Docker images](docker-images.md) of %product%
* [Qodana Scan](github.md) GitHub Action

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
Using Qodana CLI and Docker images, %product% needs to be run twice over the repository, once for each project.

### qodana.yaml file

To configure %product% for inspecting two projects, you need to create two separate [`qodana.yaml`](qodana-yaml.md) 
files. %product% also expects `qodana.yaml` to be contained in the root folder of the monorepo project. This means that 
before running %product% on the project from the `backend/` folder, that project's `qodana.yaml` file needs to be copied to 
the root folder. If you run %product% using [Docker](#Run+Qodana), you can copy files using the 
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

<tabs>
    <tab id="monorepo-yaml-backend-tab" title="The backend project">
        <code style="block" lang="shell" prompt="$">
            bootstrap: cp qodana-backend.yaml qodana.yaml            
        </code>
    </tab>
    <tab id="monorepo-yaml-frontend-tab" title="The frontend project">
        <code style="block" lang="shell" prompt="$">
            bootstrap: cp qodana-frontend.yaml qodana.yaml
        </code>
    </tab>
</tabs>

When %product% runs, it uses the `.git/` folder for linking detected problems to the corresponding
source code in a Git repository, and for exploring inspection reports [from within your IDE](qodana-ide-plugin.md).

Here are the contents of the `root/` folder: 

<!-- Alternative: put each qodana.yaml in its corresponding project directory. -->
```text
root/
    backend/
    frontend/
    .git/
    qodana-backend.yaml
    qodana-frontend.yaml
```

### Qodana Cloud

You can view inspection reports using [Qodana Cloud](https://qodana.cloud). On the Qodana Cloud website, create two 
[projects](cloud-projects.xml) for storing inspection reports for the `frontend` and `backend` projects. 

After you create the projects, you can use their [project tokens](project-token.md) to get project reports uploaded to
Qodana Cloud.

## Run Qodana

<tabs>
<tab id="monorepo-cli-tab" title="Qodana CLI">
<note>You can use %product% CLI only with Azure and CircleCI.</note>
<p>These snippets use the <code>QODANA_TOKEN</code> variables that refer to specific project tokens created at Qodana Cloud.
The <a href="docker-image-configuration.xml" anchor="docker-config-reference-directories"><code>--source-directory</code></a> option specifies which project directory to inspect.</p>
<code style="block" lang="shell" prompt="$">
qodana scan \
&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token-for-backend-project&gt;" \
&nbsp;&nbsp;--source-directory backend
</code>
<code style="block" lang="shell" prompt="$">
qodana scan \
&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token-for-frontend-project&gt;" \
&nbsp;&nbsp;--source-directory frontend
</code>
</tab>
<tab id="monorepo-docker-image-tab" title="Docker">
<p>These snippets use the <code>QODANA_TOKEN</code> variables that refer to specific project tokens created at Qodana Cloud.
The <a href="docker-image-configuration.xml" anchor="docker-config-reference-directories"><code>--source-directory</code></a> option specifies which project directory to inspect.</p>
<code style="block" lang="shell" prompt="$">
docker run \ 
&nbsp;&nbsp;-v "$PWD":/data/project/ \
&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token-for-backend-project&gt;" \
&nbsp;&nbsp;jetbrains/qodana-jvm:latest \
&nbsp;&nbsp;--source-directory backend
</code>
<code style="block" lang="shell" prompt="$">
docker run \ 
&nbsp;&nbsp;-v "$PWD":/data/project/ \
&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token-for-frontend-project&gt;" \
&nbsp;&nbsp;jetbrains/qodana-js:latest \
&nbsp;&nbsp;--source-directory frontend
</code>
</tab>
<tab id="monorepo-github-tab" title="GitHub Actions">
<p>You can use the <a href="github.md">Qodana Scan</a> GitHub action for running %product% on GitHub as explained 
in this procedure.</p>
<procedure>
<step>On the <menupath>Settings</menupath> tab of the GitHub UI, create the <code>QODANA_TOKEN_BACKEND</code> and
<code>QODANA_TOKEN_FRONTEND</code> <a href="%github-secret%">encrypted secrets</a> and save the project tokens 
<a anchor="Qodana+Cloud">generated</a> at Qodana Cloud as their values.
</step>
<step>On the <menupath>Actions</menupath> tab of the GitHub UI, set up a new workflow and create the
<code>.github/workflows/code_quality.yml</code> file.</step>
<step>
<p>Save this workflow configuration to the <code>.github/workflows/code_quality.yml</code> file:</p>
<code style="block" lang="yaml">
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
        run: cp ./qodana-backend.yaml ./qodana.yaml
      - name: 'Qodana Backend'
        uses: JetBrains/qodana-action@v2023.3
        with:
          args: |
            --source-directory,backend,
          artifact-name: qodana-backend
        env:
            QODANA_TOKEN: ${{ secrets.QODANA_TOKEN_BACKEND }}
  qodana-frontend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
      - name: 'Use qodana-frontend config'
        run: cp ./qodana-frontend.yaml ./qodana.yaml
      - name: 'Qodana Frontend'
        uses: JetBrains/qodana-action@v2023.3
        with:
          args: |
            --source-directory,frontend,
          artifact-name: qodana-frontend
        env:
            QODANA_TOKEN: ${{ secrets.QODANA_TOKEN_FRONTEND }}
</code>
</step>
</procedure>
</tab>
</tabs>

### Inspection result overview

Congratulations, now you can navigate to [Qodana Cloud](https://qodana.cloud) and study inspection results for each project 
inside your monorepo project.