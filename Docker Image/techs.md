# Qodana. Docker Image Paths and Configuration Options

### Docker image paths
- **/data/project**       -- root folder of project to be analyzed
- **/data/results**       -- root folder of stored analysis results, have to be clear before qodana run.
- **/root/.config/idea**  -- idea configuration folder
- **/opt/idea**           -- folder of idea distributive
- **/data/profile.xml**   -- used if profile wasn't configured by run options or qodana.yaml. See [Order of resolving profile](#Order_of_resolving_profile)

### Configuring
Examples of execution tuning:
- Override default inspection profile
   ```
   docker run ... -v <inspection-profile.xml>:/data/profile.xml <image-name>
   ```

- Save html report. Results folder would have additional `report/` folder with html report.
   ```
   docker run ... <image-name> --save-report
   ```

- Display html report. After inspection finished container would not exit and listen on port 8080. You can connect to http://localhost:8080 to see the results.
   ```
   docker run ... -p 8080:8080 <image-name> --show-report
   ```

- Gradle extra settings
   ```
   docker run ... -v <project-folder>/gradle.properties:/root/.gradle/gradle.properties <image-name>
   ```

- Change Heap size (default is 80% of host RAM)
   ```
   docker run ... -e _JAVA_OPTIONS=-Xmx6g <image-name>
   ```

- Log INFO messages to STDOUT. By default log level for STDOUT is WARN.
   ```
   docker run ... -e IDE_PROPERTIES_PROPERTY='-Didea.log.config.file=info.xml' <image-name>
   ```

- Use own idea.properties
   ```
   docker run ... -e IDEA_PROPERTIES=/data/project/idea.properties <image-name>
   ```


### Order of resolving profile
Qodana checks configuration parameters for resolving inspection profile in this order:
- Profile with the name %name% from command line option ```-profileName %name%```
- Profile by the path %path% from command line option ```-profilePath %path%```
- Profile with the name %name% from [qodana.yaml](#Qodana.yaml)
- Profile by the path %path% from [qodana.yaml](#Qodana.yaml)
- Profile mounted to ```/data/profile.xml```
- Fallback to using of embedded ```qodana.recommended``` profile

### Plugins management
Qodana image contains all bundled Idea Ultimate plugins. Significant part of plugins is disabled by default, list of disabled plugins is stored in /root/.config/idea/disabled_plugins.txt.  
Enabled plugins: Java, Kotlin, PHP and their libraries/frameworks plugins. Gradle and Maven plugins are also enabled.
Ways to change plugins list:
- Override disabled_plugins.txt by mounting your own file.
```
    docker run ... -v $empty_file$:/root/.config/idea/disabled_plugins.txt <image-name>
```
- Use ide properties ```idea.required.plugins.id``` and ```idea.suppressed.plugins.id```
```
docker run ... -e IDE_PROPERTIES_PROPERTY='-Didea.required.plugins.id=JavaScript,org.intellij.grails' <image-name> 
```
or
```
docker run ... -e IDE_PROPERTIES_PROPERTY=' -Didea.suppressed.plugins.id=com.intellij.spring.security' <image-name> 
```
Any custom plugin could be added to Idea instance with mounting it to plugins directory.
If you have your plugin %pluginName% directory is ```/your/custom/path/%pluginName%``` this plugin could be mounted with
```
    docker run ... -v /your/custom/path/%pluginName%:/opt/idea/plugins/%pluginName% <image-name>
```

### Analyze changes
Qodana allows checking only changed files.
```
docker run  -e IDE_PROPERTIES_PROPERTY='-Didea.required.plugins.id=Git4Idea,Subversion,hg4idea' <image-name> -changes
```
You can adjust ```idea.required.plugins.id``` value and keep only suitable for your project cvs plugin.
