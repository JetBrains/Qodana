[//]: # (title: Overview of linters)

<link-summary>A linter is a software tool that analyzes codebase for bugs, errors, and other mistakes that impact its 
quality and can cause problems. Basically, each Qodana linter is associated with a specific programming language.</link-summary>

A linter is a software tool that analyzes codebase for bugs, errors, and other mistakes that impact its quality and 
can cause problems. Basically, each Qodana linter is associated with a specific programming language and helps you:

* Detect anomalous code and probable bugs
* Eliminate dead code
* Highlight spelling problems
* Improve overall code structure
* Introduce coding best practices
* Check third-party license compatibility. This feature is available in [several linters](license-audit.topic)
* Upload analysis reports to [%cloud%](https://qodana.cloud)

> You can find out which linters are available under the Community, Ultimate and Ultimate Plus licenses in the [Pricing Model](pricing.md#pricing-linters-licenses) section.
{style="tip"}

Currently, several linters provide inspections for several programming languages.

<table>
    <tr>
        <td>Project languages</td>
        <td>Supported by linters / linter name *</td>
    </tr>
    <tr>
        <td>
            <img src="jvm.png" dark-src="jvm_dark.png" alt="Java, Kotlin, Groovy" width="296"/>
        </td>
        <td>
            <p><a href="jvm.md">%jvm%</a>&nbsp;/&nbsp;<code>%jvm-linter%</code></p>
            <p><a href="jvm.md">%jvm-co%</a>&nbsp;/&nbsp;<code>%jvm-co-linter%</code></p>
            <p><a href="jvm.md">%jvm-co-a%</a>&nbsp;/&nbsp;<code>%jvm-co-a-linter%</code></p>
            <p><a href="jvm.md">%jvm-a%</a>&nbsp;/&nbsp;<code>%jvm-a-linter%</code></p>
        </td>
    </tr>
    <tr>
        <td><img src="php.png" dark-src="php_dark.png" alt="PHP" width="296"/></td>
        <td><a href="php.md">%php%</a>&nbsp;/&nbsp;<code>%php-linter%</code></td>
    </tr>
    <tr>
        <td><img src="js.png" dark-src="js_dark.png" alt="JavaScript and TypeScript" width="296"/></td>
        <td>
            <p><a href="js.md">%js%</a>&nbsp;/&nbsp;<code>%js-linter%</code></p>
            <p><a href="php.md">%php%</a>&nbsp;/&nbsp;<code>%php-linter%</code></p>
            <p><a href="dotnet.md">%dotnet%</a>&nbsp;/&nbsp;<code>%dotnet-linter%</code></p>
            <p><a href="jvm.md">%jvm%</a>&nbsp;/&nbsp;<code>%jvm-linter%</code></p>
            <p><a href="jvm.md">%jvm-a%</a>&nbsp;/&nbsp;<code>%jvm-a-linter%</code></p>
            <p><a href="python.md">%python%</a>&nbsp;/&nbsp;<code>%python-linter%</code></p>
            <p><a href="golang.md">%go%</a>&nbsp;/&nbsp;<code>%go-linter%</code></p>
            <p><a href="ruby.md">%ruby%</a>&nbsp;/&nbsp;<code>%ruby-linter%</code></p>
        </td>
    </tr>
    <tr>
        <td>
            <p><img src="dotnet.png" dark-src="dotnet_dark.png" alt="C, C++, C#, VB.NET" width="296"/></p>
        </td>
        <td>
            <p><a href="dotnet.md">%dotnet%</a>&nbsp;/&nbsp;<code>%dotnet-linter%</code></p>
            <p><a href="dotnet.md">%dotnet-co%</a>&nbsp;/&nbsp;<code>%dotnet-co-linter%</code></p>
            <p><a href="clang.md">%clang%</a>&nbsp;/&nbsp;<code>%clang-linter%</code></p>
            <p><a href="clang.md">%cpp%</a>&nbsp;/&nbsp;<code>%cpp-linter%</code></p>
        </td>
    </tr>
    <tr>
        <td><img src="python.png" dark-src="python_dark.png" alt="Python" width="296"/></td>
        <td>
            <p><a href="python.md">%python%</a>&nbsp;/&nbsp;<code>%python-linter%</code></p>
            <p><a href="python.md">%python-co%</a>&nbsp;/&nbsp;<code>%python-co-linter%</code></p>
        </td>
    </tr>
    <tr>
        <td><img src="golang.png" dark-src="golang_dark.png" alt="Golang" width="296"/></td>
        <td><a href="golang.md">%go%</a>&nbsp;/&nbsp;<code>%go-linter%</code></td>
    </tr>
    <tr>
        <td><img src="ruby.png" dark-src="ruby_dark.png" alt="Ruby" width="296"/></td>
        <td><a href="ruby.md">%ruby%</a>&nbsp;/&nbsp;<code>%ruby-linter%</code></td>
    </tr>
</table>

\* Each linter from this table can be invoked using the `--linter` option, see the 
[](docker-image-configuration.topic#docker-config-reference-qodana-scan) for details.