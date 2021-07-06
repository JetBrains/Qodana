[//]: # (title: Docker Image Paths and Configuration Options)

## Docker image paths

- **/data/project**       &mdash; root directory of the project to be analyzed
- **/data/results**       &mdash; directory to store the analysis results, needs to be empty before running Qodana IntelliJ
- **/root/.config/idea**  &mdash; idea configuration directory
- **/opt/idea**           &mdash; directory of the idea distributive
- **/data/profile.xml**   &mdash; used if a profile wasn't configured by run options or via `qodana.yaml`. See [Order of resolving a profile](#Order+of+resolving+a+profile).

## Configuration

Available arguments:

```shell
$ docker run jetbrains/qodana

Usage:
  entrypoint [OPTIONS]

Application Options:
  -i, --project-dir= Project folder to inspect  (default: current work dir
                     /data/project)
  -o, --results-dir= Save results to folder (default: /data/results)
  -r, --report-dir=  Save html report to folder (default: /data/results/report)
      --cache-dir=   Set cache folder (default: /data/cache)
  -s, --save-report  Generate html report
  -w, --show-report  Serve html report on port 8080

Help Options:
  -h, --help         Show this help message

IDEA Inspect Options:
  -d                 Directory to be inspected. Otherwise, the whole project is inspected by default
  -profileName       Name of a profile defined in project
  -profilePath       Absolute path to the profile file
  -changes           Inspect uncommitted changes and report new problems
```

[//]: # "Why uncommitted changes? I heard that -changes allows to see changes only "

### Examples of execution tuneup
{id="qodana-execution-tuneup"}

- Override the default inspection profile:

  ```shell
   docker run ... -v <inspection-profile.xml>:/data/profile.xml <image-name>
   ```
Do not specify any profile to use the default `qodana.recommended`. For more options of how to specify a profile, see [Order of resolving a profile](#Order+of+resolving+a+profile).
For more about profiles available, see [Set up a profile](qodana-yaml.md#Set+up+a+profile).

- Save a report in HTML. By default, the HTML report will be stored in a separate `report/` subdirectory under the `results` directory. This location could be configured with `--report-dir`.

  ```shell
   docker run ... <image-name> --save-report
   ```

- Display a report in HTML. After the inspection is finished, the container will not exit and will listen to port `8080`. You can connect to [`http://localhost:8080`](http://localhost:8080) to see the results. When done, you can stop the web server by pressing `Ctrl-C` in the Docker console.

   ```shell
   docker run ... -p 8080:8080 <image-name> --show-report
   ```

- Extra Gradle settings:

  ```shell
   docker run ... -v <source-directory>/gradle.properties:/root/.gradle/gradle.properties <image-name>
   ```

- Change the Heap size (default is 80% of host RAM):

  ```shell
   docker run ... -e _JAVA_OPTIONS=-Xmx6g <image-name>
   ```

- Log INFO messages to STDOUT. By default, the log level for STDOUT is WARN.

  ```shell
   docker run ... -e IDE_PROPERTIES_PROPERTY='-Didea.log.config.file=info.xml' <image-name>
   ```

- Use own `idea.properties` file:

  ```shell
   docker run ... -e IDEA_PROPERTIES=/data/project/idea.properties <image-name>
   ```


## Order of resolving a profile

Qodana IntelliJ checks the configuration parameters for resolving the inspection profile in this order:
1. Profile with the name `%name%` from the command line option `-profileName %name%`.
2. Profile by the path `%path%` from the command line option `-profilePath %path%`.
3. Profile with the name `%name%` from `qodana.yaml`.
4. Profile by the path `%path%` from `qodana.yaml`.
5. Profile mounted to `/data/profile.xml`.
6. Fall back to using the default `qodana.recommended` profile.

## Plugins management

The Qodana IntelliJ image contains selected IDEA Ultimate plugins + a PHP plugin.

Paid plugins are not yet supported. Each vendor must clarify licensing terms for CI usage and collaborate with us to make it work.

You can add any free IntellJ platform plugins or your custom plugin using the following command:

```shell
docker run ... -v /your/custom/path/%pluginName%:/opt/idea/plugins/%pluginName% <image-name>
```

To optimize the most common cases, some bundled plugins are disabled by default. You can check the whole list of disabled plugins in `/root/.config/idea/disabled_plugins.txt`.

By default are enabled: Java, Kotlin for Server Side, PHP, and their libraries/frameworks' plugins. Gradle and Maven plugins are also enabled.

To change the plugins list, do any of the following:
- Override `disabled_plugins.txt` by mounting your own file:

  ```shell
        docker run ... -v $empty_file$:/root/.config/idea/disabled_plugins.txt <image-name>
    ```
- Use IDE properties `idea.required.plugins.id` and `idea.suppressed.plugins.id`:

  ```shell
    docker run ... -e IDE_PROPERTIES_PROPERTY='-Didea.required.plugins.id=JavaScript,org.intellij.grails' <image-name> 
    ```
  or

    ```shell
        docker run ... -e IDE_PROPERTIES_PROPERTY='-Didea.suppressed.plugins.id=com.intellij.spring.security' <image-name> 
    ```

## Analyze changes

Qodana IntelliJ allows you to check only changed files:

```shell
docker run  -e IDE_PROPERTIES_PROPERTY='-Didea.required.plugins.id=Git4Idea,Subversion,hg4idea' <image-name> -changes
```

You can adjust the `idea.required.plugins.id` value and keep only the CVS plugin suitable for your project.

[//]: # "todo: describe  problem with useMirrors in the VCS - a TeamCity problem"

## Run as non-root

By default, the container is run as the `root` user so that Qodana IntelliJ can read any volumes bind-mounted with the project and write the results. As a result, files in the `results/` folder are owned by the `root` after the run.  
To avoid this, you can run the container as a regular user:

```shell
docker run -u $UID ...
# or
docker run -u $(id -u):$(id -g) ...
```

Note that in this case the `results/` folder on host should already be created and owned by you. Otherwise, Docker will create it as `root` and Qodana IntelliJ will not be able to write to it.

### Cache dependencies

You can decrease the time for a Qodana IntelliJ run by persisting cache from one run to another. For example, package and dependency management tools such as Maven, Gradle, npm, and Yarn keep a local cache of downloaded dependencies.

By default, Qodana IntelliJ  would save caches to folder `/data/cache` inside container. This location could be changed via `--cache-dir` cli argument. The data inside is per-repository, so you can pass cache from `branch-a` to build checking `branch-b`. In this case, only new dependencies would be downloaded, if they were added. The cache feature is available starting from `2021.1-eap` image.

Example for **local** run:
   ```
   docker run --rm -it -p 8080:8080 \
      -v <source-directory>/:/data/project/ \
      -v <output-directory>/:/data/results/ \
      -v <cache-directory>/:/data/cache/ \
      jetbrains/qodana --show-report
   ```
In this case mapping the same `<cache-directory>` would speed up the second run.

In **GitHub** workflow you can utilise [actions/cache](https://docs.github.com/en/actions/guides/caching-dependencies-to-speed-up-workflows), see [full example](qodana-intellij-docker-readme.md#Run+analysis+in+CI).

**GitLab** CI also has [cache](https://docs.gitlab.com/ee/ci/caching/) which can be stored [only inside](https://docs.gitlab.com/ee/ci/yaml/README.html#cachepaths) the project directory. In this case, we recommend excluding the cache folder from inspection via [qodana.yaml](qodana-yaml.md#exclude-paths).

## Turn off user statistics

To disable the [reporting of usage statistics](qodana-intellij-docker-readme.md#Usage+statistics), adjust the `idea.headless.enable.statistics` value:

```shell
docker run  -e IDE_PROPERTIES_PROPERTY="-Didea.headless.enable.statistics=false" <image-name> 
```
