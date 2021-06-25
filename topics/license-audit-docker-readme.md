[//]: # (title: Qodana License Audit Docker Image)
![official JetBrains project](https://jb.gg/badges/official-flat-square.svg) ![Docker Stars](https://img.shields.io/docker/stars/jetbrains/qodana.svg) ![Docker Pulls](https://img.shields.io/docker/pulls/jetbrains/qodana.svg)

><include src="lib_qd.xml" include-id="eap-warning"/>

<var name="product" value="Qodana Clone Finder"/>

Supported tags:  [`2021.1-eap`](https://hub.docker.com/r/jetbrains/qodana-clone-finder/tags?page=1&ordering=last_updated&name=2021.1-eap),  [`latest`](https://hub.docker.com/r/jetbrains/qodana-clone-finder/tags?page=1&ordering=last_updated&name=latest) (points to `2021.1-eap`)

[//]: # "incomplete! check and add info"

We provide a Docker image for the [License Audit linter](about-license-audit.md) to support different usage scenarios:
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
docker run --rm -it -v <source-directory>/:/data/project/ -p 8080:8080 -e <language-version> jetbrains/qodana-license-audit --show-report
```

where `source-directory` points to the root of your project, `language-version` [specifies your project's language version](license-audit-docker-techs.md#specify-project-language-version).

This command runs the analysis on your source code and starts the web server to provide a convenient view of the results. Open [`http://localhost:8080`](http://localhost:8080) in your browser to examine the found problems and performed checks. Here, you can also reconfigure the analysis. See the [UI section](ui-overview.md) of this guide for details. When done, you can stop the web server by pressing `Ctrl-C` in the Docker console.

If you don't need the user interface and prefer to study raw data, use the following command:

```shell
docker run --rm -it -v <source-directory>/:/data/project/ -p 8080:8080 -e <language-version> jetbrains/qodana-license-audit 
```

The `<output-directory>` will contain [all the necessary results](license-audit-output.md#license-audit-basic-output). You can further tune the command as described in the [technical guide](license-audit-docker-techs.md).

### Run analysis in CI

- Run the following command as a task in a generic Shell executor:

[//]: # "check the command and add info"

```shell
docker run --rm -it -v <source-directory>/:/data/project/ -p 8080:8080 -e <language-version> jetbrains/qodana-license-audit
```

where `source-directory` points to the root of your project, `language-version` [specifies your project's language version](license-audit-docker-techs.md#specify-project-language-version).

The content of `<output-directory>` is described in [License Audit Output](license-audit-output.md#license-audit-basic-output). Consider using...

....

- Example for GitHub Workflow 

.....

[//]: # "add info"

## Usage statistics

According to the [JetBrains EAP user agreement](https://www.jetbrains.com/legal/agreements/user_eap.html), we can use third-party services to analyze the usage of our features to further improve the user experience. All data will be collected [anonymously](https://www.jetbrains.com/company/privacy.html). You can disable the reporting of usage statistics by adjusting the options of the Docker command you use. Refer to the [technical guide](clone-finder-docker-techs.md) for details.

## License

<include src="lib_qd.xml" include-id="license-info">
    <var name="product" value="Qodana Clone Finder Docker image"/>
</include>