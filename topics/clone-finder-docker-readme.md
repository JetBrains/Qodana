[//]: # (title: Qodana Clone Finder Image)
![official JetBrains project](https://jb.gg/badges/official-flat-square.svg) ![Docker Stars](https://img.shields.io/docker/stars/jetbrains/qodana.svg) ![Docker Pulls](https://img.shields.io/docker/pulls/jetbrains/qodana.svg)

![EAP](eap-alert.png)

Supported tags:  [`2021.1-eap`](https://hub.docker.com/r/jetbrains/qodana-clone-finder/tags?page=1&ordering=last_updated&name=2021.1-eap),  [`latest`](https://hub.docker.com/r/jetbrains/qodana-clone-finder/tags?page=1&ordering=last_updated&name=latest) (points to `2021.1-eap`)

The Qodana Clone Finder Docker image lets you check a queried project against a number of reference projects and lists all duplicate functions ranked by their importance.
The current version [supports PHP, Java, and Kotlin for Server Side](supported-technologies.md); support for more languages and technologies is on its way.

We provide two options optimized for different scenarios:
- Running the analysis on a regular basis as a part of your continuous integration (*CI-based execution*)
- Single-shot analysis (for example, performed *locally*)

If you prefer the first option and have established continuous integration (CI) support for your project, this page
will describe all available possibilities.  
If you don't have any CI for your project, we encourage you to try a free version of JetBrains [TeamCity](https://www.jetbrains.com/teamcity/), either in-cloud (currently in Beta) or on-premise. In this case, you can switch to our [TeamCity plugin](https://github.com/JetBrains/Qodana/tree/main/TeamCity%20Plugin) as it gives more options.

## Quick start

### Run analysis locally

1) Pull the image from Docker Hub (only necessary to update the `latest` version):

   ```shell
   docker pull jetbrains/qodana-clone-finder
   ```

2) Run the following command:

   ```shell
   docker run --rm -it -p 8080:8080 \
      -v <source-directory>/:/data/project/ \
      -v <queried-projects-directory>/:/data/versus/ \ 
      -v <output-directory>/:/data/results/ \
      jetbrains/qodana-clone-finder --show-report
   ```

where `source-directory`, `output-directory` and `queried-projects-directory` are full local paths to, respectively, the project source code directory, the analysis results directory and the directory that contains one or many projects to compare aginst them.

Example of project structure:
```
/
├── project
│   └── project_working_directory (sources, downloaded dependencies etc)
└── versus
    ├── project1
    │   └── source_code
    └── project2
    │   └── source_code
```

This command will run the analysis on your source code and start the web server to provide a convenient view of the results. Open [`http://localhost:8080`](http://localhost:8080) in your browser to examine the found problems and performed checks. Here, you can also reconfigure the analysis. See the [UI section](ui-overview.md) of this guide for details. When done, you can stop the web server by pressing `Ctrl-C` in the Docker console.

In case you don't need the user interface and prefer to study raw data, use the following command:

   ```shell
   docker run --rm -it \
      -v <source-directory>/:/data/project/ \
      -v <queried-projects-directory>/:/data/versus/ \ 
      -v <output-directory>/:/data/results/ \
      jetbrains/qodana-clone-finder 
   ```

The `output-directory` will contain [all the necessary results](clone-finder-output.md#Basic+output). You can further tune the command as described in the [technical guide](clone-finder-docker-techs.md).

If you run the analysis several times in a row, make sure you've cleaned the results' directory before using it in `docker run` again.

By default, Qodana Clone finder searches clones in all [supported languages](supported-technologies.md) but you can explicitly specify languages to search. See [technical guide](clone-finder-docker-techs.md) for details.

If queried projects are not located under the same root directory, you can use the following options to map them inside the container:
``` -v "<local path to project for comparison>/<project name>:/data/versus/<project name>" ```

Example: 
```shell 
docker run --rm -it -p 8080:8080\
  -v "/project:/data/project" \
  -v "/somepath/versus_project1:/data/versus/project1" \
  -v "/anotherpath/versus_project2:/data/versus/project2" \
  jetbrains/qodana-clone-finder  --show-report
```

### Run analysis in CI

- Use the following command as the task in generic Shell executor:

   ```shell
   docker run --rm -it \
      -v <source-directory>/:/data/project/ \
      -v <queried-projects-directory>/:/data/versus/ \ 
      -v <output-directory>/:/data/results/ \
      jetbrains/qodana-clone-finder 
   ```

  where `source-directory`, `output-directory` and `queried-projects-directory` are full paths to, respectively, the project source code directory, the analysis results directory and the directory that contains one or many projects to compare aginst them.
  
  The output of `output-directory` is described [here](clone-finder-output.md#Basic+output). Consider using [fail-thresold](qodana-yaml.md#Fail+threshold) to make the build fail on a certain number of problems reached. [Running as non-root](docker-techs.md#Run+as+non-root) is also supported.

- Example for GitHub Workflow (`.github/workflows/clone-finder-qodana.yml`):
--- to be provided ---


- Example for GitLab CI (`.gitlab-ci.yml`):

`--- to be provided ---


## Usage statistics

According to the [JetBrains EAP user agreement](https://www.jetbrains.com/legal/agreements/user_eap.html), we can use third-party services to analyze the usage of our features to further improve the user experience. All data will be collected [anonymously](https://www.jetbrains.com/company/privacy.html). You can disable the reporting of usage statistics by adjusting the options of the Docker command you use. Refer to [this guide](docker-techs.md) for details.

## License

By using the Qodana Clone Finder Docker image, you agree to the [JetBrains EAP user agreement](https://www.jetbrains.com/legal/agreements/user_eap.html) and [JetBrains privacy policy](https://www.jetbrains.com/company/privacy.html).  
The Docker image includes the evaluation license, which will expire in 30 days. Please ensure you pull a new image on time.

## Contact

Contact us at [qodana-support@jetbrains.com](mailto:qodana-support@jetbrains.com) or via [our issue tracker](https://youtrack.jetbrains.com/newIssue?project=QD). We are eager to receive your feedback on the existing Qodana functionality and learn what other features you miss in it.
