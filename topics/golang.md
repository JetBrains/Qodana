# Golang

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<img src="golang.png" dark-src="golang_dark.png" alt="Golang" width="296"/>

<var name="linter" value="Qodana for Go"/>
<var name="ide" value="GoLand"/>
<var name="docker-image" value="jetbrains/qodana-go:2024.2-eap"/>
<var name="ide-url" value="https://www.jetbrains.com/go/"/>
<var name="config-file" value="qodana-go-docker-readme.topic"/>

<var name="linter-shell" value="qodana-go"/>
<var name="ide" value="GoLand"/>
<var name="code-inspection-ide-help-url" value="https://www.jetbrains.com/help/go/?Code_Inspection"/>
<var name="code-inspection-profiles-ide-help-url" value="https://www.jetbrains.com/help/go/?Customizing_Profiles"/>

<link-summary>%linter% is based on %ide% and provides static analysis for Go projects.</link-summary>

%linter% is based on [%ide%](%ide-url%) and provides static analysis for Go projects.

<note>This linter requires the Qodana Cloud <a href="project-token.md">project token</a>.</note>

## Supported technologies

%linter% provides inspections for the following technologies.

<table style="none">
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

## Try it now

### Analyze a project locally

<include from="lib_qd.topic" element-id="root-and-non-root-users-info-bubble"></include>

<p><include from="lib_qd.topic" element-id="qodana-cli-quickstart" use-filter="non-php,non-gs,other,empty"/></p>



<!--<include from="lib_qd.topic" element-id="linter-next-steps-footer" use-filter="empty"/>-->



<!--<p><img src="https://jb.gg/badges/official-flat-square.svg" alt="official JetBrains project"/>
    </p>
<include from="lib_qd.topic" element-id="linter-docker-image-intro"/>

<chapter id="quick-start-recommended-profile" title="Quick start with the recommended profile">
    <chapter id="Run+analysis+locally" title="Run analysis locally">
        <note>
            <p>
                <include from="lib_qd.topic" element-id="docker-ram-note"/>
            </p>
        </note>
        <include from="lib_qd.topic" element-id="docker-local-analysis" use-filter="empty"/>
    </chapter>
    <chapter id="Run+analysis+in+CI" title="Run analysis in CI">
        <include from="lib_qd.topic" element-id="docker-ci-analysis"/>
    </chapter>
</chapter>

<chapter id="Using+an+existing+profile" title="Using an existing profile">
    <include from="lib_qd.topic" element-id="docker-using-existing-profile"/>
</chapter>

<chapter id="Configure+via+qodana.yaml" title="Configure via qodana.yaml">
    <include from="lib_qd.topic" element-id="docker-configure-via-qodana-yaml" use-filter="empty,for-others"/>
</chapter>

<chapter id="Plugins+management" title="Plugins management">
    <include from="lib_qd.topic" element-id="docker-plugins-management"/>
</chapter>

<chapter id="Usage+statistics" title="Usage statistics">
    <p>
        <include from="lib_qd.topic" element-id="docker-usage-statistics"/>
    </p>
</chapter>-->