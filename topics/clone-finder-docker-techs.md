[//]: # (title: Docker Image Paths and Configuration Options)

## Docker image paths

- **/data/project**&mdash;root directory of the project to be analyzed
- **/data/versus**&mdash;directory containing projects to compare against 
- **/data/results**&mdash;directory to store the analysis results, needs to be empty before each Qodana run

## Configuring

Available arguments:

```shell
$ docker run jetbrains/qodana-clone-finder

Usage:
  entrypoint [OPTIONS]

Application options:
  -w, --show-report  Serve an HTML report on port 8080
  -l, --language [PHP|Java|Kotlin]
        One or more languages to search clones in.
  --verbose Show logs and debugging info.

Help options:
  --help         Show this help message
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

