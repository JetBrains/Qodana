[//]: # (title: Docker Image Paths and Configuration Options)

## Docker image paths

- **/data/project**       -- root directory of the project to be analyzed
- **/data/versus**        -- the directory contains projects to compare against 
- **/data/results**       -- directory to store the analysis results, needs to be empty before the Qodana run

## Configuring

Available arguments:

```shell
$ docker run jetbrains/qodana-clone-finder

Usage:
  entrypoint [OPTIONS]

Application Options:
  -w, --show-report  Serve html report on port 8080
  -l, --language [PHP|Go|JavaScript|TypeScript|Java|Kotlin|Python]
        One or more languages to search clones in.
  --verbose Show logs and debugging info.

Help Options:
  --help         Show this help message
```

Examples of execution tuneup:

- Display a report in HTML. After the clone finder analysis is finished, the container will not exit and will listen to port `8080`. You can connect to [`http://localhost:8080`](http://localhost:8080) to see the results. When done, you can stop the web server by pressing `Ctrl-C` in the Docker console.

   ```shell
   docker run ... -p 8080:8080 <image-name> --show-report
   ```
  
- Specify languages explicitely
 ```shell
docker run ... <image-name> -l <language-name>
```
