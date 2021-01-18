# CHANGELOG

### v2020.3.64-eap
- QD-641 fix wrong `-1` exitcode. Now in case of OOM exitcode is 137 and warning is logged
- QD-638 add cli args to better support [gitlab-ci](Docker/README.md#quick-start-with-recommended-profile)

### v2020.3.59-eap
- fix signal handling (`Ctrl-C`) for webserver ( `--show-report`)