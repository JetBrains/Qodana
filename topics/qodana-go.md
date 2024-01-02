[//]: # (title: Qodana for Go)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<img src="golang.png" dark-src="golang_dark.png" alt="Golang" width="296"/>

<var name="linter" value="Qodana for Go"/>
<var name="ide" value="GoLand"/>
<var name="docker-image" value="jetbrains/qodana-go:2023.3"/>
<var name="ide-url" value="https://www.jetbrains.com/go/"/>
<var name="config-file" value="qodana-go-docker-readme.topic"/>

%linter% is based on [%ide%](%ide-url%) and provides static analysis for Go projects.

## Supported technologies

%linter% provides inspections for the following technologies.

<table header-style="none">
    <tr>
        <td>Programming languages</td>
        <td>
            <p>Golang</p>
        </td>
    </tr>
    <tr>
        <td>Markup languages</td>
        <td>
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
</table>

## Supported features

<include from="lib_qd.topic" element-id="linters-supported-features" use-filter="empty,non-jvm"/>

## Analyze a project locally

<include from="lib_qd.topic" element-id="qodana-cli-quickstart" use-filter="non-php,non-gs,other,empty"/>

## Next steps

<include from="lib_qd.topic" element-id="linter-next-steps-footer" use-filter="empty"/>