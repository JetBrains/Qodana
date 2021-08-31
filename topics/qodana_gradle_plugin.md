[//]: # (title: Gradle Plugin)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

The [Gradle Qodana plugin](https://github.com/JetBrains/gradle-qodana-plugin) provides the Gradle interface to run code inspections from Intellij IDEA. To get started, apply the Gradle plugin `org.jetbrains.qodana` in the Gradle configuration file.

 <tabs>
  <tab title="Groovy">

Add the following to the `build.gradle` configuration file:

  ```groovy
  plugins {
      id "org.jetbrains.qodana" version "0.1.5"
  }
  ```

  </tab>
  <tab title="Kotlin DSL">

Add the following to the `build.gradle.kts` configuration file:

  ```kotlin
  plugins {
      id("org.jetbrains.qodana") version "0.1.5"
  }
  ```

  </tab>
 </tabs>


<tip>

For details on working with Gradle in IntelliJ IDEA, see the [IntelliJ IDEA Gradle documentation](https://www.jetbrains.com/help/idea/?Gradle).

</tip>

## Gradle Qodana tasks

After the Gradle Qodana plugin is applied, you can run the provided tasks. 

| Task | Description |
|--|--|
| `runInspections` | starts Qodana inspections in a Docker container |
| `stopInspections` | stops the Qodana Docker container |
| `cleanInspections` | cleans up the Qodana output directory |

## Gradle plugin configuration

To configure the plugin, use the following options in the top level `qodana { }` configuration node:

| Option | Description |
|--|--|
| `projectPath` | path to the project on local machine |
| `resultsPath` | path to the directory to store the analysis results |
| `profilePath` | path to the profile file |
| `disabledPluginsPath` | path to file that describes disabled IDEA plugins |
| `jvmParameters` | JVM parameters to start IDEA JVM |
| `bind(local port, docker port)` | binds the ports between the local machine and the Docker container |
| `mount(local path, docker path)` | mounts a directory between the local machine and the Docker container |
| `env(name, value)` | defines an environment variable |
| `dockerImageName` | name of the Qodana Docker image |
| `dockerContainerName` | Docker container name to identify the Qodana container |
| `dockerPortBindings` | bounded Docker and local ports |
| `dockerVolumeBindings` | mounted Docker and local directories |
| `dockerEnvParameters` | defined environment variables |
| `dockerArguments` | custom Docker arguments to start a Qodana Docker container |

<tip>

For the detailed description of the Qodana IntelliJ Docker image configuration, see [Docker Image Configuration](qodana-intellij-docker-techs.md).

</tip>


### Example

<tabs>
  <tab title="Groovy"> 

Add the following to the `build.gradle` configuration file:

  ```groovy
  plugins {
      // applies the Gradle Qodana plugin to use it in the project
      id "org.jetbrains.qodana" version "0.1.5"
  }
  
  qodana {
      // by default, qodana.recommended will be used
      profilePath = "./someExternallyStoredProfile.xml"

      // by default, the results path is $projectPath/build/results
      resultsPath = "some/output/path"
  }
  ```
  </tab>

  <tab title="Kotlin DSL">

Add the following to the `build.gradle.kts` configuration file:

  ```kotlin
  plugins {
      // applies the Gradle Qodana plugin to use it in the project
      id("org.jetbrains.qodana") version "0.1.5"
  }
  
  qodana {
      // by default, qodana.recommended will be used
      profilePath.set("./someExternallyStoredProfile.xml")

      // by default, the results path is $projectPath/build/results
      resultsPath.set("some/output/path")
  }
  ```
  </tab>
</tabs>

To run the inspections, start the `runInspections` Gradle task:

```shell
gradle runInspections 
// or
./gradlew runInspections
```