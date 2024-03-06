[//]: # (title: Qodana for C/C++)

<var name="linter" value="Qodana for C/C++"/>
<var name="ide" value="CLion"/>
<var name="docker-image" value="jetbrains/qodana-clang:2023.3-eap"/>
<var name="config-file" value="qodana-clang-docker-readme.topic"/>
<var name="clang-tidy" value="https://clang.llvm.org/extra/clang-tidy"/>
<var name="clang-config" value="https://gist.github.com/fbaeuerlein/2895f889e451a817d7b2b36fd60e2873"/>
<var name="dockerfile" value="https://github.com/JetBrains/qodana-docker/blob/main/2023.3/base/cpp.Dockerfile"/>
<var name="dockerfile-internal" value="https://github.com/JetBrains/qodana-docker/blob/main/2023.3/cpp/internal.Dockerfile"/>
<var name="clang-website" value="https://clang.llvm.org/extra/clang-tidy/checks/list.html"/>
<var name="clion-inspections-general" value="https://www.jetbrains.com/help/clion/list-of-c-cpp-inspections.html#general"/>
<var name="misra-inspections" value="https://www.jetbrains.com/help/clion/list-of-c-cpp-inspections.html#stat-analysis-tools"/>
<var name="compdb-generate" value="https://www.jetbrains.com/help/clion/compilation-database.html#compdb_generate"/>

<note>
%linter% is currently in early access, which means it may be unreliable, not work as intended, and contain errors.
Any use of EAP products is entirely at your own risk. We welcome your feedback and encourage you to post it to our 
<a href="https://youtrack.jetbrains.com/newIssue?project=QD">issue tracker</a> or email it to us at
<a href="mailto:qodana-support@jetbrains.com">qodana-support@jetbrains.com</a>.
</note>

%linter% lets you inspect C and C++ projects containing [compilation databases](https://clang.llvm.org/docs/JSONCompilationDatabase.html). Based on the [Clang-Tidy](%clang-tidy%) 
linter, this linter operates on the AMD64 and ARM64 architectures.

%linter% extends standard [Clang-Tidy](%clang-website%) inspections by supplying CLion's 
[additional inspections](%clion-inspections-general%) and [`MISRA`](%misra-inspections%) checks. 

%linter% is open to users with Community, Ultimate, and Ultimate Plus subscriptions. However, the additional inspections 
and `MISRA` checks provided by CLion are only available to Ultimate and Ultimate Plus license holders.

## Supported features

The %linter% linter provides the following %product% features:

<table>
    <tr>
        <td>Feature</td>
        <td>Available with the license types</td>
    </tr>
    <tr>
        <td><a href="baseline.topic"/></td>
        <td>Community, Ultimate, and Ultimate Plus</td>
    </tr>
    <tr>
        <td><a href="quality-gate.topic"/></td>
        <td>Community, Ultimate, and Ultimate Plus</td>
    </tr>
</table>

## How it works

The Docker image of %linter% employs Clang 16.0.0 and LLVM 16. You can see the 
[`Dockerfile`](%dockerfile%) for the detailed description of all software employed by the linter.  

The linter searches for the compilation database file, `build/compile_commands.json`, in the build directory under the 
project root, reads this file, inspects the project, generates inspection reports, and saves them locally or 
uploads them to Qodana Cloud.

## Prepare the project

<procedure>
<step>Make sure that Clang-Tidy is deployed on your system. If necessary, install it using the 
<a href="https://releases.llvm.org/download.html">LLVM website</a>.
</step>
<step>
<p>Open the <a href="qodana-yaml.md" anchor="Example+of+different+configuration+options"><code>qodana.yaml</code></a> file 
and use the <code>include</code> and <code>exclude</code> configuration options to configure the list of 
inspections. Alternatively, you can configure inspections in the <code>.clang-tidy</code> file &mdash; see the configuration 
example on the <a href="%clang-config%">GitHub website</a> for more details. After configuring your inspections, save 
this file to the project root.</p>
<tip>
<p>For the full list of available Clang-Tidy inspections, use this command:</p>
<tabs group="clang-tidy-commands">
<tab id="qodana-clang-full-linux" title="Linux" group-key="clang-linux">
<code-block>clang-tidy -list-checks -checks="*"</code-block>
</tab>
<tab id="qodana-clang-full-windows" title="Windows" group-key="clang-windows">
<code-block>./clang-tidy.exe -list-checks -checks="*"</code-block>
</tab>
</tabs>
<p>To see a list of all the inspections that are enabled in Clang-Tidy by default, run this command:</p>
<tabs group="clang-tidy-commands">
<tab id="qodana-clang-enabled-linux" title="Linux" group-key="clang-linux">
<code-block>clang-tidy -list-checks</code-block>
</tab>
<tab id="qodana-clang-enabled-windows" title="Windows" group-key="clang-windows">
<code-block>./clang-tidy.exe -list-checks</code-block>
</tab>
</tabs>
</tip>
</step>
<step>
<p>Generate the <code>compile_commands.json</code> file, as explained in the <a href="%compdb-generate%">CLion documentation portal</a>, 
and save it to the <code>build</code> directory of the project root.</p>
<p>If you use CMake, you can also generate a compilation database by specifying the following 
<a href="before-running-qodana.md"><code>bootstrap</code></a> option in the <code>qodana.yaml</code> file as follows:</p>
<code-block lang="yaml">
bootstrap: mkdir -p build; cd build;cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=ON .. || true
</code-block>
</step>
<step>
<p>If your project requires specific packages not mentioned in the <a href="%dockerfile%"><code>Dockerfile</code></a>, 
then you can use the following <code>bootstrap</code> command in the your 
<code>qodana.yaml</code> file to install the required packages:</p>
<code-block lang="yaml">
bootstrap: sudo apt-get update; sudo apt-get install -y &lt;list of required packages&gt; |
&nbsp;&nbsp;rm -rf build;  mkdir -p build; cd build;cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=ON .. || true
</code-block>
</step>
</procedure>

## Run %linter%

Run the following Docker command:

```shell
docker run \
   -v $(pwd):/data/project/ \
   -v $(pwd)/results/:/data/results/ \
   -e QODANA_TOKEN="<cloud-project-token>" \
   %docker-image%
```

The linter will read the `build/compile_commands.json` file and run the Clang-Tidy tool.

In this command, the `QODANA_TOKEN` variable refers to the [project token](project-token.md) that lets you upload inspection results
to Qodana Cloud. If you omit the `QODANA_TOKEN` variable, the inspection results will be available in the 
`qodana.sarif.json` that is saved in the `/results` directory of your project root. 

You can also set a custom location for the compilation database file. For this, specify the path relative to the 
project root in the Docker command:

```shell
docker run \
   -v $(pwd):/data/project/ \
   -v $(pwd)/results/:/data/results/ \
   -e QODANA_TOKEN="<cloud-project-token>" \
   %docker-image% \
   --compile-commands <path-to-compile_commands.json>
```