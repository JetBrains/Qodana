[//]: # (title: Before inspecting your code)

%product% can perform specific steps before inspecting your code. For example, it can install a software package, run 
scripts, or otherwise prepare your project for inspection. This can be done using a script that can be run within 
a %product% Docker container. For example, it can be a script that can be extended and adapted to your needs:

```shell
#! /bin/sh
# Example bootstrap steps
set -eu

# For PHP projects that use Laravel:
#composer require --dev barryvdh/laravel-ide-helper

# For JavaScript projects that use Node.js:
#npm install
```

You can configure %product% for running the script using the `bootstrap` [option](qodana-yaml.md#Run+custom+commands):

```shell
bootstrap: sh ./script.sh
```

After this step is complete, %product% will inspect your codebase.