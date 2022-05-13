[//]: # (title: License audit Docker image)
![official JetBrains project](https://jb.gg/badges/official-flat-square.svg) ![Docker Stars](https://img.shields.io/docker/stars/jetbrains/qodana-license-audit.svg) ![Docker Pulls](https://img.shields.io/docker/pulls/jetbrains/qodana-license-audit.svg)

<include src="lib_qd.xml" include-id="license-audit-deprecation-note"/>

We provide a Docker image for the [License audit linter](about-license-audit.md) to support different usage scenarios:
- Running the analysis on a regular basis as part of your continuous integration (*CI-based execution*).
- Single-shot analysis (for example, performed *locally*).

## Quick start

### Run analysis locally

1) Pull the image from Docker Hub (necessary to use the `latest` version):

```shell
docker pull jetbrains/qodana-license-audit
```

2) Run the following command:

```shell
docker run --pull always --rm -it -p 8080:8080 \
    -v <source-directory>/:/data/project \
    -v <output-directory>/:/data/results \
    jetbrains/qodana-license-audit --show-report
```

where `<source-directory<` and `<output-directory>` are full local paths to the directories that contain, respectively, the project source code and the analysis results. 

This command runs the analysis on your source code and starts the web server to provide a convenient view of the results. Open [`http://localhost:8080`](http://localhost:8080) in your browser to examine the found problems and performed checks. Here, you can also reconfigure the analysis. See the [UI section](ui-overview.md) of this guide for details. When done, you can stop the web server by pressing `Ctrl-C` in the Docker console.

If you don't need the user interface and prefer to study raw data, use the following command:

```shell
docker run --rm -it \
    -v <source-directory>/:/data/project/ \
    -v <output-directory>/:/data/results/ \
    jetbrains/qodana-license-audit
```

If you run the analysis several times in a row, make sure you've cleaned the results directory before using it in `docker run` again.

By default, Qodana License audit comes with a set of pre-installed tools versions (Java 11, Gradle 6, Python 3 and [others](license-audit-docker-techs.md#Configuration)), you can explicitly specify which tool versions to use for your project. 
```shell
docker run --rm -it \
    -e <language-version> =3.7.10
    -v <source-directory>/:/data/project/ \
    -v <output-directory>/:/data/results/ \
    jetbrains/qodana-license-audit
```
See [technical guide](license-audit-docker-techs.md) for details.

### Run analysis in CI

- Run the following command as a task in a generic Shell executor:

```shell
docker run --rm -it \
    -v <source-directory>/:/data/project/ \
    -v <output-directory>/:/data/results/ \
    jetbrains/qodana-license-audit
```

where `<source-directory<` and `<output-directory>` are full local paths to the directories that contain, respectively, the project source code and the analysis results.

Consider using [fail-threshold](qodana-yaml.md#Set+a+fail+threshold) to make the build fail on reaching a certain number of problems. [Running as non-root](license-audit-docker-techs.md#Run+as+non-root) is also supported.

- Example for GitHub Workflow (`.github/workflows/qodana-license-audit.yml`):

```shell
name: Qodana - License audit
on:
  workflow_dispatch:
jobs:
  qodana:
    runs-on: ubuntu-latest
    steps:
      # clone your project
      - uses: actions/checkout@v2
      # run qodana-license-audit
      - name: Qodana - License audit
        uses: jetbrains/qodana-license-audit-action@main
        with:
          options: PYTHON_VERSION=3.7.10
      # upload the results to GitHub artifacts
      - uses: actions/upload-artifact@v2
        with:
          path: ${{ github.workspace }}/qodana
```

## Usage statistics

According to the [JetBrains EAP user agreement](https://www.jetbrains.com/legal/agreements/user_eap.html), we can use third-party services to analyze the usage of our features to further improve the user experience. All data will be collected [anonymously](https://www.jetbrains.com/company/privacy.html). You can disable the reporting of usage statistics by adjusting the options of the Docker command you use. Refer to the [technical guide](license-audit-docker-techs.md) for details.

## License

<include src="lib_qd.xml" include-id="license-info">
    <var name="product" value="Qodana Clone Finder Docker image"/>
</include>