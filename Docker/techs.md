# Qodana. Docker Image Paths and Configuration Options

### Docker image paths
- **/data/project**       -- root directory of the project to be analyzed
- **/data/results**       -- directory to store the analysis results, needs to be empty before the Qodana run
- **/root/.config/idea**  -- idea configuration directory
- **/opt/idea**           -- directory of the idea distributive
- **/data/profile.xml**   -- used if a profile wasn't configured by run options or via `qodana.yaml`. See [Order of resolving profile](#Order-of-resolving-profile).

### Configuring

Examples of execution tuneup:

- Override the default inspection profile:
   ```
   docker run ... -v <inspection-profile.xml>:/data/profile.xml <image-name>
   ```

- Save a report in HTML. The HTML report will be stored in a separate `report/` subdirectory under the `results` directory.
   ```
   docker run ... <image-name> --save-report
   ```

- Display a report in HTML. After the inspection is finished, the container will not exit and will listen to port `8080`. You can connect to [`http://localhost:8080`](http://localhost:8080) to see the results.
   ```
   docker run ... -p 8080:8080 <image-name> --show-report
   ```

- Extra Gradle settings:
   ```
   docker run ... -v <source-directory>/gradle.properties:/root/.gradle/gradle.properties <image-name>
   ```

- Change the Heap size (default is 80% of host RAM):
   ```
   docker run ... -e _JAVA_OPTIONS=-Xmx6g <image-name>
   ```

- Log INFO messages to STDOUT. By default, the log level for STDOUT is WARN.
   ```
   docker run ... -e IDE_PROPERTIES_PROPERTY='-Didea.log.config.file=info.xml' <image-name>
   ```

- Use own `idea.properties` file:
   ```
   docker run ... -e IDEA_PROPERTIES=/data/project/idea.properties <image-name>
   ```


### Order of resolving profile

Qodana checks the configuration parameters for resolving the inspection profile in this order:
1. Profile with the name `%name%` from the command line option `-profileName %name%`.
2. Profile by the path `%path%` from the command line option `-profilePath %path%`.
3. Profile with the name `%name%` from `qodana.yaml`.
4. Profile by the path `%path%` from `qodana.yaml`.
5. Profile mounted to `/data/profile.xml`.
6. Fall back to using the embedded `qodana.recommended` profile.

### Plugins management

The Qodana image contains all bundled Idea Ultimate plugins. A significant number of plugins is disabled by default; the list of disabled plugins is stored in `/root/.config/idea/disabled_plugins.txt`.  
Enabled plugins: Java, Kotlin, PHP, and their libraries/frameworks' plugins. Gradle and Maven plugins are also enabled.

To change the plugins list, do any of the following:
- Override `disabled_plugins.txt` by mounting your own file:
    ```
        docker run ... -v $empty_file$:/root/.config/idea/disabled_plugins.txt <image-name>
    ```
- Use IDE properties `idea.required.plugins.id` and `idea.suppressed.plugins.id`:
    ```
    docker run ... -e IDE_PROPERTIES_PROPERTY='-Didea.required.plugins.id=JavaScript,org.intellij.grails' <image-name> 
    ```
or
    ```
    docker run ... -e IDE_PROPERTIES_PROPERTY=' -Didea.suppressed.plugins.id=com.intellij.spring.security' <image-name> 
    ```

Any custom plugin can be added to the IDEA instance by mounting it to the plugins' directory.
If your plugin's `%pluginName%` directory is ```/your/custom/path/%pluginName%```, this plugin can be mounted with:
```
docker run ... -v /your/custom/path/%pluginName%:/opt/idea/plugins/%pluginName% <image-name>
```

### Analyze changes

Qodana allows checking only changed files:
```
docker run  -e IDE_PROPERTIES_PROPERTY='-Didea.required.plugins.id=Git4Idea,Subversion,hg4idea' <image-name> -changes
```
You can adjust the `idea.required.plugins.id` value and keep only the CVS plugin suitable for your project.

### Turn off user statistics

To disable the [reporting of usage statistics](README.md#usage-statistics), adjust the `idea.headless.enable.statistics` value: 
```
docker run  -e IDE_PROPERTIES_PROPERTY="-Didea.headless.enable.statistics=false" <image-name> 
```