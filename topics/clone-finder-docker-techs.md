[//]: # (title: Docker Image Paths and Configuration Options)

## Docker image paths

- **/data/project**&mdash;root directory of the project to be analyzed
- **/data/versus**&mdash;directory containing projects to compare against 
- **/data/results**&mdash;directory to store the analysis results, needs to be empty before each Qodana run

## Configuration

Available arguments:

```shell
$ docker run jetbrains/qodana-clone-finder

Usage:
  entrypoint [OPTIONS]

Application & help options:
  -i, --project-dir DIRECTORY     Queried project
  -o, --results-dir PATH          Save results to the folder
  -v, --versus-dir DIRECTORY      Reference projects to compare the queried project with
  -s, --save-report               Generate an HTML report
  -w, --show-report               Serve an HTML report on port 8080
  -l, --language [PHP|Java|Kotlin]
                                  One or more languages to search clones in
  --verbose                       Show logs and debugging info
  --help                          Show this message and exit
```

Examples of execution tuneup:

- Display a report in HTML. After the Clone Finder analysis is finished, the container will not exit and will listen to port `8080`. You can connect to [`http://localhost:8080`](http://localhost:8080) to see the results. When done, you can stop the web server by pressing `Ctrl-C` in the Docker console.

   ```shell
   docker run ... -p 8080:8080 <image-name> --show-report
   ```
  
- Specify languages explicitly
   ```shell
  docker run ... <image-name> -l <language-name>
  ```

## Run as non-root

By default, the container runs as `root` user, so Qodana would be able to read any bind-mounted volumes with the project and write the results. Which also leads to files in `results/` folder owned by `root` after the run.  
To avoid this, you can run container as a current user:

```shell
docker run -u $UID ...
# or
docker run -u $(id -u):$(id -g) ...
```