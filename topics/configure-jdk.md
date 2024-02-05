[//]: # (title: Configure the JDK)

## Default versions

This table shows the JDK versions that are by default used by %instance%:

|---------|-----------|
|[Linter](linters.md) | JDK version |
|[](qodana-jvm.md)|[JBR SDK 17](https://github.com/JetBrains/JetBrainsRuntime/tree/jbr17) |
|[](qodana-jvm-community.md)|[JBR SDK 17](https://github.com/JetBrains/JetBrainsRuntime/tree/jbr17) |
|[](qodana-jvm-android.md)|[Amazon Corretto 11](https://docs.aws.amazon.com/corretto/latest/corretto-11-ug/what-is-corretto-11.html) |

Using the default version of the JDK does not require any special configuration.

## Available versions

<anchor name="configure-jdk-available-versions"/>

Apart from the versions available [by default](#Default+versions), %instance% can automatically download and use these versions of JBR SDK 
for all JVM linters: 8, 11, 13, 15, 16, 17, 18, 19.

Otherwise, you can download the required JDK version, and [mount it](#Mount+JDK) to %instance%.

## Configure Qodana

<include from="lib_qd.topic" element-id="configure-jdk-qodana-yaml" use-filter="configure-jdk,empty"/>

If you specify here any JDK from the [list of available versions](#Available+versions), it will be automatically 
downloaded by %instance%. If you would like to use the JDK beyond this list, you will have to download it and then 
[mount it](#Mount+JDK) to %instance%.  

## Gradle

Gradle runs scripts based on the [Compatibility Matrix](https://docs.gradle.org/current/userguide/compatibility.html)
meaning that the latest supported and downloadable version of the JDK will be set up as the Gradle JDK. Using the 
Compatibility Matrix in combination with the list of [available JDK versions](#Available+versions), 
you can find the JDK that will be used by %instance%. For example, in case of Gradle 6.6, %instance% will 
download and employ JDK 13.

## Maven

In Maven, you can configure the [source and target](https://maven.apache.org/plugins/maven-compiler-plugin/examples/set-compiler-source-and-target.html) versions of the Java compiler. %instance% compares these values and selects the latest version. This version of the JDK is
then searched in the [list of available versions](#Available+versions). If found, %instance% will download and use it. 
Otherwise, %instance% will download the subsequent version from this list.  

## Mount JDK

You can mount JDK from your local filesystem to the `/root/.jdks` folder of the %instance% Docker image:

```shell
$ docker run -v /path/to/jdk:/root/.jdks/jdk \
jetbrains/qodana-<linter>
```