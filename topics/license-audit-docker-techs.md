[//]: # (title: Docker image configuration)

<include src="lib_qd.xml" include-id="license-audit-deprecation-note"/>

## Docker image paths

- **/data/project**: root directory of the project to be analyzed
- **/data/results**: directory to store the analysis results, needs to be empty before each Qodana run

## Configuration

Available arguments:

```shell
$ docker run jetbrains/qodana-license-audit

Usage:
 entrypoint [OPTIONS]

Application & help options:
 -i, --project-dir DIRECTORY     Project to run License audit on
 -o, --results-dir PATH          Save results to the folder
 -s, --save-report               Generate an HTML report
 -w, --show-report               Serve an HTML report on port 8080
```

Examples of execution tuneup:

- Display a report in HTML. After the License audit analysis is finished, the container will not exit and will listen to port `8080`. You can connect to [`http://localhost:8080`](http://localhost:8080) to see the results. When done, you can stop the web server by pressing `Ctrl-C` in the Docker console.

   ```shell
   docker run ... -p 8080:8080 <image-name> --show-report
   ```

Install and use a different version of a language:

The default installed versions of languages in the License audit image

```shell
PHP_VERSION = "7.4.16"
JAVA_VERSION = "openjdk@1.14"
```
[//]: # "not supported in EAP: PYTHON_VERSION= 3.8.10 NOVE_VERSION = 15.7.0 RUBY_VERSION = 2.6.0"

## Run as non-root

By default, the container is run as the `root` user so that Qodana can read any volumes bind-mounted with the project and write the results. As a result, files in the `results/` folder are owned by the `root` after the run.  
To avoid this, you can run the container as a regular user:

```shell
docker run -u $UID ...
# or
docker run -u $(id -u):$(id -g) ...
```

Note that in this case, the `results/` folder on host should already be created and owned by you. Otherwise, Docker will create it as `root` and Qodana will not be able to write to it.
