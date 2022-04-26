[//]: # (title: Qodana License audit)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<var name="linter" value="Qodana License audit"/>

<include src="lib_qd.xml" include-id="license-audit-deprecation-note"/>

<note>

<include src="lib_qd.xml" include-id="supported-techs">
    <var name="linter" value="Qodana License audit"/>
    <var name="supported-techs" value="PHP Composer, npm, pip (requirements.txt or setup.py is required) pipenv, poetry, yarn"/>
</include>

</note>


Qodana License audit helps software projects avoid problems with incompatible third-party licenses. More than 1600 licenses are detected. Users can create their own include and ignore lists as well as other overrides of the default detector’s logic.

<tip>

<include src="lib_qd.xml" include-id="qodana-playground-tip">
    <var name="qodana-playground-url" value="https://qodana.teamcity.com/project/Hosted_Root_LicenseAuditExamples?mode=builds#all-projects"/>
    <var name="linter" value="Qodana License audit"/>
</include>

</tip>

## Try it now

### Analyze a project locally

To start, pull the image from Docker Hub (only necessary to get the latest version):

```shell
docker pull jetbrains/qodana-license-audit
```

and run the analysis locally:

```shell
docker run --rm -it -v <source-directory>/:/data/project/ \ 
  -p 8080:8080 jetbrains/qodana-license-audit --show-report
```

where `source-directory` should point to the root of your project.

Check the results in your browser at [`http://localhost:8080`](http://localhost:8080).

Read our [Docker guide](license-audit-docker-readme.md) for more options and details related to the License audit execution.

## Next steps

- <a href="license-audit-docker-readme.md">Configure %linter% Docker image</a>