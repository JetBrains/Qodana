[//]: # (title: Linters)

<var name="image-version" value="2024.1"/>

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
* Upload inspection results to [Qodana Cloud](cloud-about.topic)

Currently, several linters provide inspections for several programming languages.

<table>
    <tr>
        <td>Project languages</td>
        <td>Supported in linters / linter name</td>
    </tr>
    <tr>
        <td>
            <img src="jvm.png" dark-src="jvm_dark.png" alt="Java, Kotlin, Groovy" width="296"/>
        </td>
        <td>
            <p><a href="qodana-jvm.md"/>&nbsp;/&nbsp;<code>jetbrains/qodana-jvm:%image-version%</code></p>
            <p><a href="qodana-jvm-community.md"/>&nbsp;/&nbsp;<code>jetbrains/qodana-jvm-community:%image-version%</code></p>
            <p><a href="qodana-jvm-android.md"/>&nbsp;/&nbsp;<code>jetbrains/qodana-jvm-android:%image-version%</code></p>
        </td>
    </tr>
    <tr>
        <td><img src="php.png" dark-src="php_dark.png" alt="PHP" width="296"/></td>
        <td><a href="qodana-php.md"/>&nbsp;/&nbsp;<code>jetbrains/qodana-php:%image-version%</code></td>
    </tr>
    <tr>
        <td><img src="js.png" dark-src="js_dark.png" alt="JavaScript and TypeScript" width="296"/></td>
        <td>
            <p><a href="qodana-js.md"/>&nbsp;/&nbsp;<code>jetbrains/qodana-js:%image-version%</code></p>
            <p><a href="qodana-php.md"/>&nbsp;/&nbsp;<code>jetbrains/qodana-php:%image-version%</code></p>
            <p><a href="qodana-dotnet.md"/>&nbsp;/&nbsp;<code>jetbrains/qodana-dotnet:%image-version%</code></p>
        </td>
    </tr>
    <tr>
        <td>
            <p><img src="dotnet.png" dark-src="dotnet_dark.png" alt="C, C++, C#, VB.NET" width="296"/></p>
            <p>C and C++ inspections are limited by projects containing <code>.sln</code> solution or <code>.csproj</code> project files.</p>
        </td>
        <td>
            <p><a href="qodana-dotnet.md"/>&nbsp;/&nbsp;<code>jetbrains/qodana-dotnet:%image-version%</code></p>
            <p><a href="qodana-dotnet-community.md"/>&nbsp;/&nbsp;<code>jetbrains/qodana-cdnet:%image-version%</code></p>
        </td>
    </tr>
    <tr>
        <td><img src="python.png" dark-src="python_dark.png" alt="Python" width="296"/></td>
        <td>
            <p><a href="qodana-python.md"/>&nbsp;/&nbsp;<code>jetbrains/qodana-python:%image-version%</code></p>
            <p><a href="qodana-python-community.md"/>&nbsp;/&nbsp;<code>jetbrains/qodana-python-community:%image-version%</code></p>
        </td>
    </tr>
    <tr>
        <td><img src="golang.png" dark-src="golang_dark.png" alt="Golang" width="296"/></td>
        <td><a href="qodana-go.md"/>&nbsp;/&nbsp;<code>jetbrains/qodana-go:%image-version%</code></td>
    </tr>
</table>