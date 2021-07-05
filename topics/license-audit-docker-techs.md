[//]: # (title: Docker Image Paths and Configuration Options)

## Docker image paths

- **/data/project**&nbsp;&mdash; root directory of the project to be analyzed
- **/data/results**&nbsp;&mdash; directory to store the analysis results, needs to be empty before each Qodana run

## Configuration

Available arguments:

```shell
$ docker run jetbrains/qodana-license-audit

Usage:
 entrypoint [OPTIONS]

Application & help options:
 -i, --project-dir DIRECTORY     Project to run License Audit on
 -o, --results-dir PATH          Save results to the folder
 -s, --save-report               Generate an HTML report
 -w, --show-report               Serve an HTML report on port 8080
 -t  --tools-versions            Show available tools versions to install
```

### Examples of execution tuneup

- Display a report in HTML. After the License Audit analysis is finished, the container will not exit and will listen to port `8080`. You can connect to [`http://localhost:8080`](http://localhost:8080) to see the results. When done, you can stop the webserver by pressing `Ctrl-C` in the Docker console.

```shell
   docker run ... -p 8080:8080 <image-name> --show-report
```

### Specify tools versions required by your project
{id="specify-project-tools-version"}

The default installed versions of tools (languages SDKs or build systems) in the License Audit image are:
```shell
JAVA_VERSION="11.0.11.hs-adpt"
KOTLIN_VERSION="1.5.10"
GRADLE_VERSION="6.8.3"
PHP_VERSION="7.4.16"
PYTHON_VERSION="3.8.10"
NODE_VERSION="15.7.0"
```

If your project requires other tool version, pass the environment variable with the tool name and it's version to `docker run`:

```shell
docker run --rm -it -p 8080:8080 \
    -v /project/:/data/project \
    -v /results/:/data/results/ \
    -e PYTHON_VERSION=3.7.10 \
    jetbrains/qodana-license-audit:latest --show-report
```

Then it will be installed on the container launch and used to obtain dependencies.

#### Find available tools versions

Run the command to find available versions for the wanted tool

```shell
docker run --rm -it jetbrains/qodana-license-audit:latest --tools-versions <tool>
```

where `<tool>` is a tool name, which can be `java`, `kotlin`, `gradle`, `php`, `python` or `node`.

### Known issues with Gradle projects
{id="gradle-known-issues"}

1. In case if your project has no [Gradle Wrapper](https://docs.gradle.org/current/userguide/gradle_wrapper.html) included  and your project requires a Gradle version other than the default `6.8.3`, set `GRADLE_VERSION` image environment variable:

```shell
docker run --rm -it -p 8080:8080 \
    -v /project/:/data/project \
    -v /results/:/data/results/ \
    -e GRADLE_VERSION=5.6.1   
    jetbrains/qodana-license-audit:latest --show-report
```

2. In case of error, `Could not find or load main class org.gradle.wrapper.GradleWrapperMain`, push [the Gradle Wrapper](https://docs.gradle.org/current/userguide/gradle_wrapper.html) to the project repository.

## Run as non-root

By default, the container is run as the `root` user so that Qodana can read any volumes bind-mounted with the project and write the results. As a result, files in the `results/` folder are owned by the `root` after the run.  
To avoid this, you can run the container as a regular user:

```shell
docker run -u $UID ...
# or
docker run -u $(id -u):$(id -g) ...
```
Note that in this case, the `results/` folder on the host should already be created and owned by you. Otherwise, Docker will create it as `root,` and Qodana will not be able to write to it.

## Turn off user statistics

To disable the [reporting of usage statistics](clone-finder-docker-readme.md#Usage+statistics), add ```DISABLE_STAT_COLLECTION``` environment variable:

```shell
docker run -e DISABLE_STAT_COLLECTION=true <image-name> 
```
