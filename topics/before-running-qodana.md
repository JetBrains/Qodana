[//]: # (title: Before inspecting your code)

%product% can perform specific steps before inspecting your code. For example, it can install a software package, run 
scripts, or otherwise prepare your project for inspection. For these purposes, you can develop a script to run within a 
%product% Docker container that can be adapted to your needs, for example:

```shell
#! /bin/sh
# Example bootstrap steps
set -eu

# For PHP projects that use Laravel:
#composer require --dev barryvdh/laravel-ide-helper

# For JavaScript projects that use Node.js:
#npm install
```

You can tell %product% to run such script using the `bootstrap` [option](qodana-yaml.md#Run+custom+commands):

```shell
bootstrap: sh ./script.sh
```

After running the script, %product% will inspect your codebase.