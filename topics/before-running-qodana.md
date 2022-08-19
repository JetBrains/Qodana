[//]: # (title: Before inspecting your code)

%product% can perform specific steps before inspecting your code. For example, it can install a software package, run 
scripts, or otherwise prepare your project for inspection. For this reason, you can prepare a script that can be run 
within a %product% Docker container as shown below:

```shell
#! /bin/sh
# Example bootstrap steps
set -eu

# For PHP projects that use Laravel:
#composer require --dev barryvdh/laravel-ide-helper

# For JavaScript projects that use Node.js:
#npm install
```

You can tell %product% to run this script using the `bootstrap` [option](qodana-yaml.md#Run+custom+commands), for example:

```shell
bootstrap: sh ./script.sh
```