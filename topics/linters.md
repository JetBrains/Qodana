[//]: # (title: Overview of linters)

<var name="image-version" value="2025.1"/>
<var name="image-version-clang" value="2024.3"/>


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
* Upload analysis reports to [Qodana Cloud](https://qodana.cloud)

> You can find out which linters are available under the Community, Ultimate and Ultimate Plus licenses in the [Pricing Model](pricing.md#pricing-linters-licenses) section.
{style="tip"}

Currently, several linters provide inspections for several programming languages.

<table>
    <tr>
        <td>Project languages</td>
        <td>Supported by linters / linter name</td>
    </tr>
    <tr>
        <td>
            <img src="jvm.png" dark-src="jvm_dark.png" alt="Java, Kotlin, Groovy" width="296"/>
        </td>
        <td>
            <p><a href="jvm.md">%jvm%</a>&nbsp;/&nbsp;<code>jetbrains/qodana-jvm:%image-version%</code></p>
            <p><a href="jvm.md">%jvm-co%</a>&nbsp;/&nbsp;<code>jetbrains/qodana-jvm-community:%image-version%</code></p>
            <p><a href="jvm.md">%jvm-co-a%</a>&nbsp;/&nbsp;<code>jetbrains/qodana-jvm-android:%image-version%</code></p>
            <p><a href="jvm.md">%jvm-a%</a>&nbsp;/&nbsp;<code>jetbrains/qodana-android:%image-version%</code></p>
        </td>
    </tr>
    <tr>
        <td><img src="php.png" dark-src="php_dark.png" alt="PHP" width="296"/></td>
        <td><a href="php.md">%php%</a>&nbsp;/&nbsp;<code>jetbrains/qodana-php:%image-version%</code></td>
    </tr>
    <tr>
        <td><img src="js.png" dark-src="js_dark.png" alt="JavaScript and TypeScript" width="296"/></td>
        <td>
            <p><a href="js.md">%js%</a>&nbsp;/&nbsp;<code>jetbrains/qodana-js:%image-version%</code></p>
            <p><a href="php.md">%php%</a>&nbsp;/&nbsp;<code>jetbrains/qodana-php:%image-version%</code></p>
            <p><a href="dotnet.md">%dotnet%</a>&nbsp;/&nbsp;<code>jetbrains/qodana-dotnet:%image-version%</code></p>
            <p><a href="jvm.md">%jvm%</a>&nbsp;/&nbsp;<code>jetbrains/qodana-jvm:%image-version%</code></p>
            <p><a href="jvm.md">%jvm-a%</a>&nbsp;/&nbsp;<code>jetbrains/qodana-android:%image-version%</code></p>
            <p><a href="python.md">%python%</a>&nbsp;/&nbsp;<code>jetbrains/qodana-python:%image-version%</code></p>
            <p><a href="golang.md">%go%</a>&nbsp;/&nbsp;<code>jetbrains/qodana-go:%image-version%</code></p>
        </td>
    </tr>
    <tr>
        <td>
            <p><img src="dotnet.png" dark-src="dotnet_dark.png" alt="C, C++, C#, VB.NET" width="296"/></p>
        </td>
        <td>
            <p><a href="dotnet.md">%dotnet%</a>&nbsp;/&nbsp;<code>jetbrains/qodana-dotnet:%image-version%&lt;-privileged&gt;</code>*</p>
            <p><a href="dotnet.md">%dotnet-co%</a>&nbsp;/&nbsp;<code>jetbrains/qodana-cdnet:%image-version%-eap&lt;-privileged&gt;</code>*</p><!-- Add -eap after release -->
            <p><a href="clang.md">%clang%</a>&nbsp;/&nbsp;<code>jetbrains/qodana-clang:%image-version-clang%-eap</code></p><!-- Add -eap after release -->
            <p><a href="clang.md">%cpp%</a>&nbsp;/&nbsp;<code>jetbrains/qodana-cpp:%image-version%-eap&lt;-clangXX&gt;&lt;-privileged&gt;</code>**</p><!-- Add -eap after release -->
        </td>
    </tr>
    <tr>
        <td><img src="python.png" dark-src="python_dark.png" alt="Python" width="296"/></td>
        <td>
            <p><a href="python.md">%python%</a>&nbsp;/&nbsp;<code>jetbrains/qodana-python:%image-version%</code></p>
            <p><a href="python.md">%python-co%</a>&nbsp;/&nbsp;<code>jetbrains/qodana-python-community:%image-version%</code></p>
        </td>
    </tr>
    <tr>
        <td><img src="golang.png" dark-src="golang_dark.png" alt="Golang" width="296"/></td>
        <td><a href="golang.md">%go%</a>&nbsp;/&nbsp;<code>jetbrains/qodana-go:%image-version%</code></td>
    </tr>
</table>

\* The privileged mode lets you execute commands that need root access because in this case %product% comes with a 
default `qodana` user that possesses root privileges and does not require a password. To do it, in the linter name 
specify the `-privileged` tag.

\** You can run the %cpp% linter in the privileged mode to execute commands that need root access because in this case
%product% comes with a default `qodana` user that possesses root privileges and does not require a password. To do it,
in the `-clangXX` tag of the linter name specify the [Clang-Tidy](https://clang.llvm.org/extra/clang-tidy) version from 
15 to 18, and also specify the `-privileged` tag. 
