# CHANGELOG

### v2021.1.x-eap
-  [QD-729](https://youtrack.jetbrains.com/issue/QD-729) add --cache-dir support

### v2020.3.72-eap
-  [QD-675](https://youtrack.jetbrains.com/issue/QD-675) fix for gradle cache in project folder

### v2020.3.68-eap
-  [QD-651](https://youtrack.jetbrains.com/issue/QD-651) support running container as non-root

### v2020.3.64-eap
- [QD-641](https://youtrack.jetbrains.com/issue/QD-641) fix wrong `-1` exitcode. Now in case of OOM exitcode is 137 and warning is logged
- [QD-638](https://youtrack.jetbrains.com/issue/QD-638) add cli args to better support [gitlab-ci](Docker/README.md#quick-start-with-recommended-profile)
- improve the cli results output. Now we provide brief summary of all the problems grouped by severity level. 

### v2020.3.59-eap
- fix signal handling (`Ctrl-C`) for webserver ( `--show-report`)