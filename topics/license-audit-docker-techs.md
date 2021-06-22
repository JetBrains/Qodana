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
```

The command structure:
```shell
docker run <docker-options> <image-name:tag> <audit-options>
````

### License Audit options: Examples of execution tuneup

- Display a report in HTML. After the Clone Finder analysis is finished, the container will not exit and will listen to port `8080`. You can connect to [`http://localhost:8080`](http://localhost:8080) to see the results. When done, you can stop the web server by pressing `Ctrl-C` in the Docker console.

   ```shell
   docker run ... -p 8080:8080 <image-name> --show-report
   ```

### Docker options: Specify a different language version

The default installed versions of languages in the License Audit image:
```shell
PYTHON_VERSION = "3.8.10"
PHP_VERSION = "7.4.16"
NODE_VERSION = "15.7.0"
RUBY_VERSION = "2.6.0"
JAVA_VERSION = "openjdk@1.14"
```

If your project requires another version, pass the environment variable of the language version with other Docker options to `docker run`:

```shell
docker run --rm -it -p 8080:8080 \
-v /project/:/data/project \
-v /results/:/data/results/ \
-e PYTHON_VERSION=3.7.10 jetbrains/qodana-license-audit:latest --show-report
```

Then it will be installed on the container launch and used to obtain dependencies.

[//]: # "todo: change to Install language version + You need to do it one time (when implemented)"

## Run as non-root

By default, the container is run as the `root` user so that Qodana can read any volumes bind-mounted with the project and write the results. As a result, files in the `results/` folder are owned by the `root` after the run.  
To avoid this, you can run the container as a regular user:

```shell
docker run -u $UID ...
# or
docker run -u $(id -u):$(id -g) ...
```

Note that in this case, the `results/` folder on host should already be created and owned by you. Otherwise, Docker will create it as `root` and Qodana will not be able to write to it.
