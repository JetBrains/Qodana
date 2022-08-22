[//]: # (title: Prepare your project)

You can configure %product% to prepare your project for inspection. For example, it can be package installation, 
running scripts, or any other actions that help reduce the number of false positives. For this reason, in the root 
directory of your project you can create the `prepare-qodana.sh` script as shown below:

```shell
#! /bin/sh
# Example bootstrap steps, see https://jetbrains.com/help/qodana/before-running-qodana.html
set -eu

# For PHP projects that use Laravel:
#composer require --dev barryvdh/laravel-ide-helper

# For JavaScript projects that use Node.js:
#npm install
```

You can tell %product% to run this script within a %product% Docker container using the 
`bootstrap` [option](qodana-yaml.md#Run+custom+commands) of `qodana.yaml`:

```shell
bootstrap: sh ./prepare-qodana.sh
```

Alternatively, you can save the script commands under the `bootstrap` option of the `qodana.yaml` file:

```yaml
bootstrap: |+
  set -eu
  # For PHP projects that use Laravel:
  #composer require --dev barryvdh/laravel-ide-helper

  # For JavaScript projects that use Node.js:
  #npm install
```