[//]: # (title: Gradle plugin)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

The [Gradle Qodana plugin](https://plugins.gradle.org/plugin/org.jetbrains.qodana) provides the Gradle interface for running 
code inspections provided by %instance%. To start, apply the Gradle plugin `org.jetbrains.qodana` in the Gradle 
configuration file.

 <tabs group="languages">
  <tab title="Groovy" group-key="groovy">

Add the following to the `build.gradle` configuration file.

  ```groovy
  plugins {
      id "org.jetbrains.qodana" version "<plugin-version>"
  }
  ```

  </tab>
  <tab title="Kotlin DSL" group-key="kotlin-dsl">

Add the following to the `build.gradle.kts` configuration file:

  ```kotlin
  plugins {
      id("org.jetbrains.qodana") version "<plugin-version>"
  }
  ```

  </tab>
 </tabs>

<var name="qodana-label">Gradle Plugin Portal</var>
<note>

The latest version is: [![](https://img.shields.io/gradle-plugin-portal/v/org.jetbrains.qodana?color=green&label=%qodana-label%&logo=gradle)](https://plugins.gradle.org/plugin/org.jetbrains.qodana)

</note>


<tip>

For details on working with Gradle in IntelliJ IDEA, see the [IntelliJ IDEA Gradle documentation](https://www.jetbrains.com/help/idea/?Gradle).

</tip>

### `qodana { }` extension configuration
Properties available for configuration in the `qodana { }` top-level configuration closure:

| Name             | Description                                          | Type      | Default Value                           |
|------------------|------------------------------------------------------|-----------|-----------------------------------------|
| `projectPath`    | Path to the project folder to inspect.               | `String`  | `project.projectDir`                    |
| `resultsPath`    | Path to the directory to store task results.         | `String`  | `"${projectPath}/build/qodana/results"` |
| `cachePath`      | Path to the directory to store the generated report. | `String`  | `"${projectPath}/build/qodana/cache/"`  |

## Gradle Qodana Tasks

### `qodanaScan`

Start Qodana in the project directory.

The task relies on the `qodana { }` extension configuration. However, it is also controlled by provided `arguments`.


### Example

Add this to your Gradle configuration file:

- Groovy – `build.gradle`

  ```groovy
  plugins {
      // applies Gradle Qodana plugin to use it in project
      id "org.jetbrains.qodana" version "..."
  }
  
  qodana {
      // by default result path is $projectPath/build/results
      resultsPath = "some/output/path"
  }
  
  qodanaScan {
      arguments = ["--fail-threshold", "0"]
  }
  ```

- Kotlin – `build.gradle.kts`

  ```kotlin
  plugins {
      // applies Gradle Qodana plugin to use it in project
      id("org.jetbrains.qodana") version "..."
  }
  
  qodana {
      // by default result path is $projectPath/build/results
      resultsPath.set("some/output/path")
  }
  
  qodanaScan {
      resultsPath.set("some/output/path")
      arguments.set(listOf("--fail-threshold", "0"))
  }
  ```

> **Note:** Docker requires at least 4GB of memory. Set it in the Docker `Preferences > Resources > Memory` section.

Now you can run inspections with `qodanaScan` Gradle task:

```bash
gradle qodanaScan 
// or
./gradlew qodanaScan
```

A complete guide for options and configuration of `arguments` parameters can be found on [Qodana CLI docs page](https://github.com/JetBrains/qodana-cli#scan).
