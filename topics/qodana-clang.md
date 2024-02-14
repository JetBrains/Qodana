[//]: # (title: Qodana for C/C++ \(CMake\))

<var name="linter" value="Qodana for C/C++ (CMake)"/>
<var name="ide" value="Clion"/>
<var name="docker-image" value="jetbrains/qodana-clang:2023.3-eap"/>
<var name="config-file" value="qodana-clang-docker-readme.xml"/>
<var name="clang-tidy" value="https://clang.llvm.org/extra/clang-tidy"/>
<var name="clang-config" value="https://gist.github.com/fbaeuerlein/2895f889e451a817d7b2b36fd60e2873"/>
<var name="dockerfile" value="https://github.com/JetBrains/qodana-docker/blob/main/2023.3/base/cpp.Dockerfile"/>
<var name="dockerfile-internal" value="https://github.com/JetBrains/qodana-docker/blob/main/2023.3/cpp/internal.Dockerfile"/>
<var name="clang-website" value="https://clang.llvm.org/extra/clang-tidy/checks/list.html"/>
<var name="clion-inspections-general" value="https://www.jetbrains.com/help/clion/list-of-c-cpp-inspections.html#general"/>
<var name="misra-inspections" value="https://www.jetbrains.com/help/clion/list-of-c-cpp-inspections.html#stat-analysis-tools"/>

<note>
%linter% is currently in the Early Access, which means it may be not reliable, work not as intended, and contain errors.
Any use of the EAP product is at your own risk. Your feedback is very welcome in our 
<a href="https://youtrack.jetbrains.com/newIssue?project=QD">issue tracker</a> or at
<a href="mailto:qodana-support@jetbrains.com">qodana-support@jetbrains.com</a>.
</note>

%linter% lets you inspect your C and C++ projects. This linter is based on the [Clang Tidy](%clang-tidy%) linter, 
operates on the AMD64 and ARM64 architectures, and lets you inspect only projects compiled with 
[CMake](https://cmake.org/). It extends the existing Clang Tidy inspections by supplying the `Clang-Tidy` and 
`MISRA checks` inspections provided by CLion. 

%linter% is available under the Community, Ultimate, and Ultimate Plus licenses. However, the `Clang-Tidy` and
`MISRA checks` inspections from CLion are available only under the Ultimate and Ultimate Plus licenses.

The list of the standard Clang Tidy inspections is available on the [Clang website](%clang-website%). The list of the 
CLion `Clang-Tidy` inspections is available in the [General](%clion-inspections-general%) section on the 
CLion documentation website. Information about the `MISRA checks` inspections is available in the 
[Static Analysis Tools](%misra-inspections%) section of the Clion documentation website.

## Supported technologies

<table header-style="none">
    <tr>
        <td>Programming languages</td>
        <td>
            <p>C</p>
            <p>C++</p>
            <p>Android</p>
            <p>Objective-C</p>
        </td>
    </tr>
    <tr>
        <td>Frameworks and libraries</td>
        <td>
            <p>Abseil</p>
            <p>Altera</p>
            <p>Boost</p>
            <p>MPI</p>
            <p>OpenMP</p>
        </td>
    </tr>
</table>

## Supported features

The %linter% linter provides the following %product% features:

<table>
    <tr>
        <td>Feature</td>
        <td>Available under licenses</td>
    </tr>
    <tr>
        <td><a href="baseline.xml"/></td>
        <td>Community, Ultimate and Ultimate Plus</td>
    </tr>
    <tr>
        <td><a href="quality-gate.xml"/></td>
        <td>Community, Ultimate and Ultimate Plus</td>
    </tr>
</table>

## How it works

The Docker image of %linter% employs Clang 16.0.0 and LLVM 16. You can see the 
[`Dockerfile`](%dockerfile%) for the detailed description of all software employed by the linter.  

The linter runs CMake to compile project files, generates a compilation command database, and saves it to the 
`build/compile_commands.json` file of the project directory. The linter reads the compilation command database, inspects 
the project, generates inspection reports, and saves them locally or uploads to Qodana Cloud.

## Prepare the project

Make sure that the Clang Tidy and CMake tools are installed on your system.

In the [`qodana.yaml`](qodana-yaml.md#Example+of+different+configuration+options) file, you can enable or disable inspections using the `include` and `exclude` configuration 
options. Alternatively, you can configure inspections in the `.clang-tidy` file, see the configuration example on the 
[GitHub website](%clang-config%). After configuring, save this file to the project root. 

<tip>
<p>You can get the list of all available Clang Tidy inspections using this command:</p>
<tabs>
<tab id="qodana-clang-full-linux" title="Linux" group-key="clang-linux">
<code>clang-tidy -list-checks -checks="*"</code>
</tab>
<tab id="qodana-clang-full-windows" title="Windows" group-key="clang-windows">
<code>./clang-tidy.exe -list-checks -checks="*"</code>
</tab>
</tabs>
<p>To obtain the list of all inspections enabled in Clang Tidy by default, you can run this command:</p>
<tabs>
<tab id="qodana-clang-enabled-linux" title="Linux" group-key="clang-linux">
<code>clang-tidy -list-checks</code>
</tab>
<tab id="qodana-clang-enabled-windows" title="Windows" group-key="clang-windows">
<code>./clang-tidy.exe -list-checks</code>
</tab>
</tabs>
</tip>

In the `qodana.yaml` file, use the [`bootstrap`](before-running-qodana.md) option to specify a command for generating 
a compilation command database contained in the `build/compile_commands.json` file, for example:

```yaml
bootstrap: mkdir -p build; cd build;cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=ON .. || true
```

Here, `cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=ON` generates and saves the `compile_commands.json` file to the `build` directory
inside your project.

If your project requires specific packages not mentioned in the [`Dockerfile`](%dockerfile%), then in the `qodana.yaml` 
file you can use the following `bootstrap` command that will install the required packages:

```yaml
bootstrap: sudo apt-get update; sudo apt-get install -y <list of required packages>; |
  rm -rf build;  mkdir -p build; cd build;cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=ON .. || true
```

## Run %linter%

%linter% reads a compilation command database contained in the `build/compile_commands.json` file and runs the `Clang Tidy` 
tool using this database.

Here is the Docker command for running the %linter% linter:

```shell
docker run \
   -v $(pwd):/data/project/ \
   -v $(pwd)/results/:/data/results/ \
   -e QODANA_TOKEN="<cloud-project-token>" \
   %docker-image%
```

Here, the `QODANA_TOKEN` variable refers to the [project token](project-token.md) that lets you upload inspection results
to Qodana Cloud. If you omit the `QODANA_TOKEN` variable, the inspection results will be available in the 
`qodana.sarif.json` saved in the `/results` directory of your project root. 

To override the location of a compilation command database, you can specify the location for the 
`compile_commands.json` file relatively to the project root, so the Docker command will look like:

```shell
docker run \
   -v $(pwd):/data/project/ \
   -v $(pwd)/results/:/data/results/ \
   -e QODANA_TOKEN="<cloud-project-token>" \
   %docker-image% \
   --compile-commands <path-to-compile_commands.json>
```