[//]: # (title: About Qodana IntelliJ)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

License Audit is designed to help software projects avoid problems with incompatible third-party licenses. More than 1600 licenses are detected. Users can create their own black and white lists and other overrides of the default detector’s logic.


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

### Run at GitHub

You can set up a workflow in your GitHub repository using the [GitHub actions](license-audit-github-action.md) we published.

### Supported inspections

Read our [License Audit Output](license-audit-output.md) to find information about all inspections and ways to resolve problem.

### Supported languages

PHP Composer, npm, pip (requirements.txt or setup.py is required), pipenv, poetry, yarn are already supported.

## License

<include src="lib_qd.xml" include-id="license-info">
    <var name="product" value="Qodana linters"/>
</include>
