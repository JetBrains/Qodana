[//]: # (title: Prepare your project)

When %instance% runs on your project, it tries to figure out the build system and project structure by itself. 
If %instance% cannot figure out the project structure, it will run the inspections nevertheless, but some inspections may 
report that they cannot find classes, packages, files or cannot resolve references. In these cases, %instance% needs a 
bit of help. Typical actions to prepare the project for Qodana are:

* Install third-party packages or libraries
* Run a program that sets up the build environment 

These actions are carried out using the `bootstrap` [option](qodana-yaml.md#Run+custom+commands) of the `qodana.yaml` file:

```yaml
bootstrap: |+
  set -eu
  # For PHP projects that use Laravel:
  #composer require --dev barryvdh/laravel-ide-helper

  # For JavaScript projects that use Node.js:
  #npm install
```

To be able to use syntax highlighting and validation in your IDE, you can create the `prepare-qodana.sh` shell script 
and save it to the root directory of your project:

```shell
#! /bin/sh
# Example bootstrap steps, see https://jetbrains.com/help/qodana/before-running-qodana.html
set -eu

# For PHP projects that use Laravel:
#composer require --dev barryvdh/laravel-ide-helper

# For JavaScript projects that use Node.js:
#npm install
```

Run the script within a %instance% Docker container using the `bootstrap` option:

```shell
bootstrap: sh ./prepare-qodana.sh
```

## Examples

This configuration tells %instance% to install a specific version of Node.JS and project dependencies:

```yaml
bootstrap: |+
  set -eu
   
  # Sets the node version to be used
  nodenv install 18.14.2
  nodenv global 18.14.2
  npm install -g yarn
  
  # Install project dependencies
  yarn install --frozen-lockfile
```

Here, the Node.JS version can be retrieved from either an environment variable or `package.json`.

<note>
If you run the Dockerized version of %instance%, you will need to specify the <code>-u 0</code> Docker 
<a href="docker-image-configuration.topic" anchor="docker-config-reference-docker-environment-run-non-root">option</a> 
because <code>nodenv</code> requires root privileges.
</note>
