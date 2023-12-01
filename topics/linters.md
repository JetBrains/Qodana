[//]: # (title: Linters)

A linter is a software tool that analyzes codebase for bugs, errors, and other mistakes that impact its quality and 
can cause problems. Basically, each Qodana linter is associated with a specific programming language and helps you:

* Detect anomalous code and probable bugs
* Eliminate dead code
* Highlight spelling problems
* Improve overall code structure
* Introduce coding best practices
* Check third-party license compatibility. This feature is available in [several linters](license-audit.xml)
* Upload inspection results to [Qodana Cloud](cloud-about.xml)

Currently, several linters provide inspections for several programming languages.

<table>
    <tr>
        <td>Project languages</td>
        <td>Supported in linters</td>
    </tr>
    <tr>
        <td>
            <img src="jvm.png" dark-src="jvm_dark.png" alt="Java, Kotlin, Groovy" width="296"/>
        </td>
        <td>
            <p><a href="qodana-jvm.md"/></p>
            <p><a href="qodana-jvm-community.md"/></p>
            <p><a href="qodana-jvm-android.md"/></p>
        </td>
    </tr>
    <tr>
        <td><img src="php.png" dark-src="php_dark.png" alt="PHP" width="296"/></td>
        <td><a href="qodana-php.md"/></td>
    </tr>
    <tr>
        <td><img src="js.png" dark-src="js_dark.png" alt="JavaScript and TypeScript" width="296"/></td>
        <td>
            <p><a href="qodana-js.md"/></p>
            <p><a href="qodana-php.md"/></p>
            <p><a href="qodana-dotnet.md"/></p>
        </td>
    </tr>
    <tr>
        <td>
            <p><img src="dotnet.png" dark-src="dotnet_dark.png" alt="C, C++, C#, VB.NET" width="296"/></p>
            <p>C and C++ inspections are limited by projects containing <code>.sln</code> files. </p>
        </td>
        <td>
            <p><a href="qodana-dotnet.md"/></p>
            <p><a href="qodana-dotnet-community.md"/></p>
        </td>
    </tr>
    <tr>
        <td><img src="python.png" dark-src="python_dark.png" alt="Python" width="296"/></td>
        <td>
            <p><a href="qodana-python.md"/></p>
            <p><a href="qodana-python-community.md"/></p>
        </td>
    </tr>
    <tr>
        <td><img src="golang.png" dark-src="golang_dark.png" alt="Golang" width="296"/></td>
        <td><a href="qodana-go.md"/></td>
    </tr>
</table>