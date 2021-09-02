[//]: # (title: About Qodana License Audit)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<note>

<include src="lib_qd.xml" include-id="supported-techs">
    <var name="linter" value="Qodana License Audit"/>
    <var name="supported-techs" value="PHP Composer, npm, pip (requirements.txt or setup.py is required) pipenv, poetry, yarn"/>
</include>

</note>


Qodana License Audit is designed to help software projects avoid problems with incompatible third-party licenses. More than 1600 licenses are detected. Users can create their own include and ignore lists as well as other overrides of the default detector’s logic.

For details about all inspections and ways to resolve problem, see [License Audit Output](license-audit-output.md).


## Try it now

### Analyse a project locally

To start, pull the image from Docker Hub (only necessary to get the latest version):

```shell
docker pull jetbrains/qodana-license-audit
```

and run the analysis locally:

```shell
docker run --rm -it -v <source-directory>/:/data/project/ -p 8080:8080 jetbrains/qodana-license-audit --show-report
```

where `source-directory` should point to the root of your project.

Check the results in your browser at [`http://localhost:8080`](http://localhost:8080).

Read our [Docker guide](license-audit-docker-readme.md) for more options and details related to the License Audit execution.

  <seealso>
  <category ref="next_steps">
   <a href="license-audit-docker-readme.md"/>
   <a href="license-audit-github-action.md"/>
   <a href="license-audit-teamcity-plugin.md"/>
  </category>
 </seealso>

