[//]: # (title: Changelog)

## v2021.2.11-eap
- based on the IntelliJ IDEA 2021.2
- [QD-1157](https://youtrack.jetbrains.com/issue/QD-1157) fix qodana.yaml multi-linter parsing
- [QD-1063](https://youtrack.jetbrains.com/issue/QD-1063) fix Kotlin language version configuration
- [QD-739](https://youtrack.jetbrains.com/issue/QD-739) fix the build freeze on 1 CPU
- reduce unwanted logs output in CLI

## v2021.1.17-eap
- based on the IntelliJ IDEA 2021.1
- [QD-729](https://youtrack.jetbrains.com/issue/QD-729) add --cache-dir support

## v2020.3.72-eap
- [QD-675](https://youtrack.jetbrains.com/issue/QD-675) fix for gradle cache in project folder

## v2020.3.68-eap
- [QD-651](https://youtrack.jetbrains.com/issue/QD-651) support for running containers as non-root

## v2020.3.64-eap
- [QD-641](https://youtrack.jetbrains.com/issue/QD-641) fix wrong `-1` exitcode. Now in case of OOM exitcode is 137 and warning is logged
- [QD-638](https://youtrack.jetbrains.com/issue/QD-638) add cli args to better support [gitlab-ci](qodana-intellij-docker-readme.md#quick-start-recommended-profile)
- improve the CLI results output. Now we provide a summary of all the problems grouped by severity level.

## v2020.3.59-eap
- fix signal handling (`Ctrl-C`) for webserver ( `--show-report`)