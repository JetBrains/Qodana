[//]: # (title: Qodana for PHP)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<img src="php-linter.png" dark-src="php-linter_dark.png" alt="Qodana for PHP linter languages" width="296"/>

<var name="linter" value="Qodana for PHP"/>
<var name="ide" value="PhpStorm"/>
<var name="docker-image" value="jetbrains/qodana-php:2023.3"/>
<var name="config-file" value="qodana-php-docker-readme.xml"/>

%linter% is based on [%ide%](https://www.jetbrains.com/phpstorm/). 

<include from="lib_qd.topic" element-id="linter-intro"/>

## Supported technologies

%linter% provides inspections for the following technologies.

<table header-style="none">
    <tr>
        <td>Programming languages</td>
        <td>
            <p>PHP</p>
            <p>JavaScript</p>
            <p>TypeScript</p>
        </td>
    </tr>
    <tr>
        <td>Markup languages</td>
        <td>
            <p>Blade</p>
            <p>CSS</p>
            <p>HTML</p>
            <p>JSON and JSON5</p>
            <p>RELAX NG</p>
            <p>XML</p>
            <p>YAML</p>
        </td>
    </tr>
    <tr>
        <td>Scripting languages</td>
        <td>
            <p>Shell script</p>
        </td>
    </tr>
    <tr>
        <td>Databases and ORM</td>
        <td>
            <p>MongoJS</p>
            <p>MySQL</p>
            <p>Oracle</p>
            <p>PostgreSQL</p>
            <p>SQL</p>
            <p>SQL Server</p>
        </td>
    </tr>
    <tr>
        <td>Dependency management</td>
        <td>
            <p>Composer</p>
        </td>
    </tr>
    <tr>
        <td>Frameworks and libraries</td>
        <td>
            <p>Cucumber</p>
            <p>Joomla!</p>
            <p>PHPUnit</p>
            <p>Psalm</p>
        </td>
    </tr>
</table>

## Supported features

<include from="lib_qd.topic" element-id="linters-supported-features" use-filter="empty,php"/>

## Try it now

### Analyze a project locally

<include from="lib_qd.topic" element-id="qodana-cli-quickstart" use-filter="php-only,jvm-php,non-gs,other,empty"/>

## Next steps

<include from="lib_qd.topic" element-id="linter-next-steps-footer" use-filter="empty,for-php-linter"/>
