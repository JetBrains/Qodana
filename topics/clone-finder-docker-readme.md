[//]: # (title: Qodana Clone Finder Docker Image)
![official JetBrains project](https://jb.gg/badges/official-flat-square.svg) ![Docker Stars](https://img.shields.io/docker/stars/jetbrains/qodana.svg) ![Docker Pulls](https://img.shields.io/docker/pulls/jetbrains/qodana.svg)

![EAP](eap-alert.png)

Supported tags:  [`2021.1-eap`](https://hub.docker.com/r/jetbrains/qodana-clone-finder/tags?page=1&ordering=last_updated&name=2021.1-eap),  [`latest`](https://hub.docker.com/r/jetbrains/qodana-clone-finder/tags?page=1&ordering=last_updated&name=latest) (points to `2021.1-eap`)

We provide a Docker image for the [Clone Finder linter](about-clone-finder.md) to support different usage scenarios:
- Running the analysis on a regular basis as part of your continuous integration (*CI-based execution*)
- Single-shot analysis (for example, performed *locally*).

## Quick start

### Run analysis locally

1) Pull the image from Docker Hub (necessary to use the `latest` version):

   ```shell
   docker pull jetbrains/qodana-clone-finder
   ```

2) Run the following command:

   ```shell
   docker run --rm -it -p 8080:8080 \
      -v <queried-project-directory>/:/data/project/ \
      -v <reference-projects-directory>/:/data/versus/ \ 
      -v <output-directory>/:/data/results/ \
      jetbrains/qodana-clone-finder --show-report
   ```

where `<queried-project-directory>`, `<reference-projects-directory>`,  and `<output-directory>` are full local paths to the directories that contain, respectively, the project source code, one or more projects to compare against, and the analysis results.

Example of project structure:
```shell
/
├── project
│   └── project_working_directory (sources, downloaded dependencies etc)
└── versus
    ├── project1
    │   └── source_code
    └── project2
    │   └── source_code
```

This command runs the analysis on your source code and starts the web server to provide a convenient view of the results. Open [`http://localhost:8080`](http://localhost:8080) in your browser to examine the found problems and performed checks. Here, you can also reconfigure the analysis. See the the [UI section](ui-overview.md) of this guide for details. When done, you can stop the web server by pressing `Ctrl-C` in the Docker console.

In case you don't need the user interface and prefer to study raw data, use the following command:

   ```shell
   docker run --rm -it \
      -v <source-directory>/:/data/project/ \
      -v <queried-projects-directory>/:/data/versus/ \ 
      -v <output-directory>/:/data/results/ \
      jetbrains/qodana-clone-finder 
   ```

The `<output-directory>` will contain [all the necessary results](clone-finder-output.md#Basic+output). You can further tune the command as described in the [technical guide](clone-finder-docker-techs.md).

If you run the analysis several times in a row, make sure you've cleaned the results directory before using it in `docker run` again.

By default, Qodana Clone Finder searches clones in all [supported languages](supported-technologies.md) but you can explicitly specify languages to search. See [technical guide](clone-finder-docker-techs.md) for details.

If reference projects are not located under the same root directory, you can use the following options to map them inside the container:
``` -v "<local path to project for comparison>/<project name>:/data/versus/<project name>" ```

Example: 
```shell 
docker run --rm -it -p 8080:8080\
  -v <project_folder>/project/:/data/project/ \
  -v somepath/versus_project1/:/data/versus/project1/ \
  -v anotherpath/versus_project2/:/data/versus/project2/ \
  jetbrains/qodana-clone-finder  --show-report
```

### Run analysis in CI

- Run the following command as a task in a generic Shell executor:

   ```shell
   docker run --rm -it \
      -v <queried-project-directory>/:/data/project/ \
      -v <reference-projects-directory>/:/data/versus/ \ 
      -v <output-directory>/:/data/results/ \
      jetbrains/qodana-clone-finder 
   ```

where `<queried-project-directory>`, `<reference-projects-directory>`,  and `<output-directory>` are full paths to the directories that contain, respectively, the project source code, one or more projects to compare against, and the analysis results.
  
The content of `<output-directory>` is described in [Clone Finder Output](clone-finder-output.md#Basic+output). Consider using [fail-threshold](qodana-yaml.md#Fail+threshold) to make the build fail on reaching a certain number of problems. [Running as non-root](clone-finder-docker-techs.md#Run+as+non-root) is also supported.

- Example for GitHub Workflow (`.github/workflows/clone-finder-qodana.yml`):

```shell
name: Qodana - Clone Finder
on:
  workflow_dispatch:
jobs:
  qodana:
    runs-on: ubuntu-latest
    steps:
      # clone your project to ./project/
      - uses: actions/checkout@v2
        with:
          path: ./project/
      # clone the repositories to ./versus/
      - uses: actions/checkout@v2
        with:
          repository: JetBrains-Research/buckwheat
          path: ./versus/buckwheat
      # run qodana-clone-finder
      - name: Qodana - Clone Finder
        uses: jetbrains/qodana-clone-finder-action@main
      - uses: actions/upload-artifact@v2
        with:
          path: ${{ github.workspace }}/qodana
```

## Usage statistics

According to the [JetBrains EAP user agreement](https://www.jetbrains.com/legal/agreements/user_eap.html), we can use third-party services to analyze the usage of our features to further improve the user experience. All data will be collected [anonymously](https://www.jetbrains.com/company/privacy.html). You can disable the reporting of usage statistics by adjusting the options of the Docker command you use. Refer to the [technical guide](clone-finder-docker-techs.md) for details.

## License

By using the Qodana Clone Finder Docker image, you agree to the [JetBrains EAP user agreement](https://www.jetbrains.com/legal/agreements/user_eap.html) and [JetBrains privacy policy](https://www.jetbrains.com/company/privacy.html).  
The Docker image includes the evaluation license, which will expire in 30 days. Please ensure you pull a new image on time.

## Contact

Contact us at [qodana-support@jetbrains.com](mailto:qodana-support@jetbrains.com) or via [our issue tracker](https://youtrack.jetbrains.com/newIssue?project=QD). We are eager to receive your feedback on the existing Qodana functionality and learn what other features you miss in it.
