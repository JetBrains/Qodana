[//]: # (title: Inspect a monorepo project)

<var name="github-secret" value="https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository"/>

<link-summary>A use case explaining how you can use Qodana for inspecting monorepo projects.</link-summary>

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

This section explains how to prepare and inspect a monorepo using:

* [Qodana CLI](https://github.com/JetBrains/qodana-cli)
* [Docker images](docker-images.md) of %product%
* The [Qodana Scan](github.md) GitHub action

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

### Configuration files

To configure %product% for inspecting two projects, you need to create two YAML-formatted [configuration files](qodana-yaml.md), 
one for each linter. In this example, these will be the `qodana-backend.yaml` and `qodana-frontend.yaml` files.  

When %product% runs, it uses the `.git/` folder for linking detected problems to the corresponding
source code in a Git repository, and for exploring inspection reports [from within your IDE](qodana-ide-plugin.md).

Here are the contents of the `root/` folder: 

```text
root/
    backend/
    frontend/
    .git/
    qodana-backend.yaml
    qodana-frontend.yaml
```

### Qodana Cloud

You can view inspection reports using [Qodana Cloud](https://qodana.cloud). On the Qodana Cloud website, create one 
[project](cloud-projects.topic) for storing inspection reports for the `frontend` project, and another one for the `backend` project. 

After you create the projects, you can use their [project tokens](project-token.md) for running %product%.

## Run Qodana

Because each %product% [linter](linters.md) can inspect a specific set of programming languages, Qodana CLI and Docker 
images of %product% need to be run twice over the monorepo repository, once for each project contained in it.

<tabs>
<tab id="monorepo-cli-tab" title="Qodana CLI">
<note>You can only use %product% CLI with Azure and CircleCI.</note>
<p>These snippets use the <code>QODANA_TOKEN</code> variables that refer to <a href="project-token.md">project tokens</a>.
The <a href="docker-image-configuration.topic" anchor="docker-config-reference-directories"><code>--source-directory</code></a> option specifies which project folder to inspect.
The <a href="docker-image-configuration.topic" anchor="docker-config-reference-custom-yaml-config"><code>--config</code></a>
option specifies which %product% configuration file to employ. Here is the snippet for the <code>backend</code> project:</p>
<code-block lang="shell" prompt="$">
qodana scan \
&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token-for-backend-project&gt;" \
&nbsp;&nbsp;--source-directory backend \
&nbsp;&nbsp;--config qodana-backend.yaml
</code-block>
<p>Here is the snippet for the <code>frontend</code> project:</p>
<code-block lang="shell" prompt="$">
qodana scan \
&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token-for-frontend-project&gt;" \
&nbsp;&nbsp;--source-directory frontend \
&nbsp;&nbsp;--config qodana-frontend.yaml
</code-block>
</tab>
<tab id="monorepo-docker-image-tab" title="Docker">
<p>These snippets use the <code>QODANA_TOKEN</code> variables that refer to <a href="project-token.md">project tokens</a>.
The <a href="docker-image-configuration.topic" anchor="docker-config-reference-directories"><code>--source-directory</code></a> 
option specifies which project directory to inspect. 
The <a href="docker-image-configuration.topic" anchor="docker-config-reference-custom-yaml-config"><code>--config</code></a>
option specifies which %product% configuration file to employ. Here is the snippet for the <code>backend</code> project:</p>
<code-block lang="shell" prompt="$">
docker run \ 
&nbsp;&nbsp;-v "$PWD":/data/project/ \
&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token-for-backend-project&gt;" \
&nbsp;&nbsp;jetbrains/qodana-jvm:latest \
&nbsp;&nbsp;--source-directory backend \
&nbsp;&nbsp;--config qodana-backend.yaml
</code-block>
<p>Here is the snippet for the <code>frontend</code> project:</p>
<code-block lang="shell" prompt="$">
docker run \ 
&nbsp;&nbsp;-v "$PWD":/data/project/ \
&nbsp;&nbsp;-e QODANA_TOKEN="&lt;cloud-project-token-for-frontend-project&gt;" \
&nbsp;&nbsp;jetbrains/qodana-js:latest \
&nbsp;&nbsp;--source-directory frontend \
&nbsp;&nbsp;--config qodana-frontend.yaml
</code-block>
</tab>
<tab id="monorepo-github-tab" title="GitHub Actions">
<p>You can use the <a href="github.md">Qodana Scan</a> GitHub action for running %product% on GitHub as explained 
in this procedure.</p>
<procedure>
<step>On the <ui-path>Settings</ui-path> tab of the GitHub UI, create the <code>QODANA_TOKEN_BACKEND</code> and
<code>QODANA_TOKEN_FRONTEND</code> <a href="%github-secret%">encrypted secrets</a> and save the project tokens 
<a anchor="Qodana+Cloud">generated</a> in Qodana Cloud as their values.
</step>
<step>On the <ui-path>Actions</ui-path> tab of the GitHub UI, set up a new workflow and create the
<code>.github/workflows/code_quality.yml</code> file.</step>
<step>
<p>Save this workflow configuration to the <code>.github/workflows/code_quality.yml</code> file:</p>

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
      - name: 'Qodana Backend'
        uses: JetBrains/qodana-action@v2024.2
        with:
          args: |
            --source-directory,backend,--config,qodana-backend.yaml
          artifact-name: qodana-backend
        env:
            QODANA_TOKEN: ${{ secrets.QODANA_TOKEN_BACKEND }}
  qodana-frontend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
      - name: 'Qodana Frontend'
        uses: JetBrains/qodana-action@v2024.2
        with:
          args: |
            --source-directory,frontend,--config,qodana-frontend.yaml
          artifact-name: qodana-frontend
        env:
            QODANA_TOKEN: ${{ secrets.QODANA_TOKEN_FRONTEND }}
```
</step>
</procedure>
</tab>
</tabs>

## View inspection results

Congratulations, now you can navigate to [Qodana Cloud](https://qodana.cloud) and review the inspection results for each project 
inside your monorepo project!