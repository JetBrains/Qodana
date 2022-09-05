[//]: # (title: Linters)

A linter is a software tool that analyzes codebase for bugs, errors, and other mistakes that impact its quality and 
can cause problems. Basically, each Qodana linter associated with a specific programming language 
helps:

* Detect anomalous code and probable bugs
* Eliminate dead code
* Highlight spelling problems
* Improve overall code structure
* Introduce coding best practices

Starting from version 2022.3, Qodana reads `.gitignore` files of your project and defines the files and folders to be 
ignored during inspections.

Here is an overview of %product% linters for inspecting your projects.

## JVM-based languages

%product% provides several linters for inspecting JVM-based projects.

<table>
    <tr>
    <td><a href="qodana-jvm-community.md"/></td>
    <td><a href="qodana-jvm-android.md"/></td>
    <td><a href="qodana-jvm.md"/></td>
    </tr>
    <tr>
        <td>Based on IntelliJ IDEA Community with support for:
            <list>
            <li>Java and Kotlin inspections</li>
            <li>Maven and Gradle</li>
            </list>
        </td>
        <td>Based on IntelliJ IDEA Community with support for:
            <list>
            <li>Java and Kotlin inspections</li>
            <li>Maven and Gradle</li>
            <li>Android-specific code inspections</li>
            </list>
        </td>
        <td>Based on IntelliJ IDEA Ultimate with support for:
            <list>
            <li>Java and Kotlin inspections</li>
            <li>Maven and Gradle</li>
            <li>IntelliJ IDEA Ultimate code inspections</li>
            <li>Spring, Jakarta EE, Java EE, Micronaut, Quarkus, Helidon frameworks</li>
            <li>Third-party license verification using <a href="license-audit.xml">License audit</a></li>
            </list>
        </td>
    </tr>
</table>

## PHP

The [](qodana-php.md) linter is based on [PhpStorm](https://www.jetbrains.com/phpstorm) and supports:

* PHP language inspections from PhpStorm
* Third-party license verification using <a href="license-audit.xml">License audit</a>
* Code inspection while migrating to a new [language version](qodana-php-language-upgrade.xml)

## Python

The [](qodana-python.md) linter is based on [PyCharm Professional](https://www.jetbrains.com/pycharm) and supports:

* Python language inspections from PyCharm Professional
* Third-party license verification using <a href="license-audit.xml">License audit</a>

## JavaScript and TypeScript

The [](qodana-js.md) linter is based on [WebStorm](https://www.jetbrains.com/webstorm) and supports:

* JavaScript and TypeScript language inspections from WebStorm
* Third-party license verification using <a href="license-audit.xml">License audit</a>

## Clone detection

The [Qodana Clone Finder](about-clone-finder.md) linter lets you detect code duplicates across different projects.
