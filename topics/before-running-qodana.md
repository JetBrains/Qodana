[//]: # (title: Prepare your project)

When %product% runs on your project, it tries to figure out the build system and project structure by itself. 
If %product% cannot figure out the project structure, it will run the inspections nevertheless, but some inspections may 
report that they cannot find classes, packages, files or cannot resolve references. In these cases, %product% needs a 
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

Run the script within a %product% Docker container using the `bootstrap` option:

```shell
bootstrap: sh ./prepare-qodana.sh
```
