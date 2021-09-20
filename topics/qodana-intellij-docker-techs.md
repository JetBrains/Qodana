[//]: # (title: Docker image configuration)

## Docker image paths

| Path | Description |
|--|--|
| `/data/project` | Root directory of the project to be analyzed |
| `/data/results` | Directory to store the analysis results, needs to be empty before running Qodana IntelliJ | 
| `/root/.config/idea` | IntelliJ IDEA configuration directory |
| `/opt/idea` | Directory of the IntelliJ IDEA distributive |
| `/data/profile.xml` | Used if a profile wasn't configured by run options or via `qodana.yaml`. See [Order of resolving a  profile](#Order+of+resolving+a+profile). |

## Configuration options

The following arguments are available for the `docker run jetbrains/qodana` command:

| Option | Description |
|--|--|
| `-i`, `--project-dir=` | Project root folder (default: current working directory `/data/project`) |
| `-o`, `--results-dir=` | Save results to folder (default: `/data/results`) |
| `-r`, `--report-dir=`  | Save HTML report to folder (default: `/data/results/report`) |
| `--cache-dir=`         | Set cache folder (default: `/data/cache`) |
| `-s`, `--save-report`  | Generate HTML report |
| `-w`, `--show-report`  | Serve HTML report on port 8080 |
| `-b`, `--baseline` | Run [in baseline mode](#Run+in+baseline+mode). Provide the path to an exisitng SARIF report to be used in the baseline state calculation. |
| `--baseline-include-absent` | Include in the output report the results from the baseline run that are absent in the current run |
| `--fail-threshold`     | Set the number of problems that will serve as a quality gate. If this number is reached, the inspection run is terminated. |
| `-d`                   | Directory to be inspected. If not specified, the whole project is inspected by default |
| `-n`, `--profile-name`         | Name of a profile defined the in project |
| `-p`, `--profile-path`         | Absolute path to the profile file |
| `-changes`             | Inspect uncommitted changes and report new problems |

## Examples of execution tuneup
{id="qodana-execution-tuneup"}

### Override the default inspection profile

  ```shell
   docker run ... -v <inspection-profile.xml>:/data/profile.xml <image-name>
   ```

If no profile is specified, the default `qodana.recommended` profile is used. For more options of how to specify a profile, see [Order of resolving a profile](#Order+of+resolving+a+profile).
For more about available profiles, see [Set up a profile](qodana-yaml.md#Set+up+a+profile).

### Save a report as HTML

  ```shell
   docker run ... <image-name> --save-report
   ```

By default, the HTML report is stored in a separate `report/` subdirectory under the `results` directory. This location could be configured with `--report-dir`.

### Display a report in HTML

```shell
docker run ... -p 8080:8080 <image-name> --show-report
```

After the inspection is finished, the container will not exit and will listen on port `8080`. You can connect to `http://localhost:8080` to see the results. To stop the web server, press `Ctrl-C` in the Docker console.


### Change the Heap size

  ```shell
docker run ... -e _JAVA_OPTIONS=-Xmx6g <image-name>
  ```

By default, Heap size is set to 80% of the host RAM.

### Log INFO messages to STDOUT

  ```shell
docker run ... -e IDE_PROPERTIES_PROPERTY='-Didea.log.config.file=info.xml' <image-name>
  ```

The default log level for STDOUT is `WARN`.

### Provide different Gradle settings

  ```shell
   docker run ... -v <source-directory>/gradle.properties:/root/.gradle/gradle.properties <image-name>
   ```

### Use a different 'idea.properties' file

  ```shell
   docker run ... -e IDEA_PROPERTIES=/data/project/idea.properties <image-name>
   ```

### Turn off user statistics

To disable the [reporting of usage statistics](qodana-intellij-docker-readme.md#Usage+statistics), adjust the `idea.headless.enable.statistics` value:

```shell
docker run ... -e IDE_PROPERTIES_PROPERTY="-Didea.headless.enable.statistics=false" <image-name> 
```

### Manage plugins

The Qodana IntelliJ image contains selected IDEA Ultimate plugins + a PHP plugin.

Paid plugins are not yet supported. Each vendor must clarify licensing terms for CI usage and collaborate with us to make it work.

You can add any free IntellJ platform plugins or your custom plugin by using the following command:

```shell
docker run ... -v /your/custom/path/%pluginName%:/opt/idea/plugins/%pluginName% <image-name>
```

To optimize the most common cases, some bundled plugins are disabled by default. You can check the whole list of disabled plugins in `/root/.config/idea/disabled_plugins.txt`.

Java, Kotlin for Server Side, PHP, and their libraries'/frameworks' plugins are enabled by default. Gradle and Maven plugins are also enabled.

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

### Analyze changes

Qodana IntelliJ lets you check only changed files:

```shell
docker run  -e IDE_PROPERTIES_PROPERTY='-Didea.required.plugins.id=Git4Idea,Subversion,hg4idea' <image-name> -changes
```

You can adjust the `idea.required.plugins.id` value and keep only the VCS plugin suitable for your project.

### Run in baseline mode

<note>

Displaying Qodana IntelliJ baseline run results via [Qodana UI](ui-overview.md) is currently in development.

</note>

In baseline run mode, each new Qodana IntelliJ run is compared to some initial run selected as a "baseline". This can help in situations when you have no possibility to fix old problems and rather want to prevent the appearance of new ones.

```shell
   docker run ... <image-name> --baseline <baseline-path> [--baseline-include-absent]
```

where `<baseline-path>` is the path to a `qodana.sarif.json` file from an earlier run. If the `--baseline-include-absent` option is provided, the inspection results will include _absent_ problems, that is the problems detected only in the baseline run but not in the current run.

After the inspection is finished, Qodana IntelliJ displays the summary of the current project state compared to the baseline.

```shell
Baseline comparison result - UNCHANGED: 10, NEW: 5, ABSENT: 3
```

where the detected problems are aggregated as follows:

- `new`: The problem was detected only in the current run but not in the baseline run.
- `absent`: The problem was detected only in the baseline run but not in the current run.
- `unchanged`: The problem was detected both in the current run and in the baseline run.

The [SARIF output report](qodana-intellij-docker-sarif.md) will contain the per-problem information on the baseline state.

### Set a quality gate

Qodana IntelliJ lets you configure a "quality gate", that is, the number of problems that will act as a threshold. If the threshold number is reached, the inspection run is terminated. 

```shell
   docker run ... <image-name> --fail-threshold <number>
```

When running in [baseline mode](#Run+in+baseline+mode), a threshold is calculated as the sum of _new_ and _absent_ problems. _Unchanged_ results are ignored.

<note>

You can also specify the threshold by adding the `failThreshold: <number>` node to [qodana.yaml](qodana-yaml.md). The value specified as the `docker run` option will override the one specified in `qodana.yaml`.  

</note>

### Run as non-root

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

By default, Qodana IntelliJ would save caches to folder `/data/cache` inside container. This location could be changed via `--cache-dir` cli argument. The data inside is per-repository, so you can pass cache from `branch-a` to build checking `branch-b`. In this case, only new dependencies would be downloaded, if they were added.

Example for **local** run:

 ```shell
 docker run --rm -it -p 8080:8080 \
    -v <source-directory>/:/data/project/ \
    -v <output-directory>/:/data/results/ \
    -v <cache-directory>/:/data/cache/ \
    jetbrains/qodana --show-report
 ```

In this case mapping the same `<cache-directory>` would speed up the second run.

In **GitHub** workflow you can utilise [actions/cache](https://docs.github.com/en/actions/guides/caching-dependencies-to-speed-up-workflows), see [full example](qodana-intellij-docker-readme.md#Run+analysis+in+CI).

**GitLab** CI also has [cache](https://docs.gitlab.com/ee/ci/caching/) which can be stored [only inside](https://docs.gitlab.com/ee/ci/yaml/README.html#cachepaths) the project directory. In this case, we recommend excluding the cache folder from inspection via [qodana.yaml](qodana-yaml.md#exclude-paths).

## Order of resolving a profile

Qodana IntelliJ checks the configuration parameters for resolving the inspection profile in this order:
1. Profile with the name `%name%` from the command-line option `--profile-name %name%`.
2. Profile by the path `%path%` from the command-line option `--profile-path %path%`.
3. Profile with the name `%name%` from `qodana.yaml`.
4. Profile by the path `%path%` from `qodana.yaml`.
5. Profile mounted to `/data/profile.xml`.
6. Fall back to using the default `qodana.recommended` profile.
