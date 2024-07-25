# PHP

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<img src="php-linter.png" dark-src="php-linter_dark.png" alt="Qodana for PHP linter languages" width="296"/>

<var name="linter" value="Qodana for PHP"/>
<var name="ide" value="PhpStorm"/>
<var name="docker-image" value="jetbrains/qodana-php:2024.2-eap"/>
<var name="config-file" value="qodana-php-docker-readme.topic"/>
<var name="linter-shell" value="qodana-php"/>
<var name="code-inspection-ide-help-url" value="https://www.jetbrains.com/help/phpstorm/?Code_Inspection"/>
<var name="code-inspection-profiles-ide-help-url" value="https://www.jetbrains.com/help/phpstorm/?Customizing_Profiles"/>

<link-summary>%linter% is based on %ide% and provides inspections for PHP, JavaScript, and TypeScript.</link-summary>

%linter% is based on [%ide%](https://www.jetbrains.com/phpstorm/). <include from="lib_qd.topic" element-id="linter-intro"/>

<note>This linter requires the Qodana Cloud <a href="project-token.md">project token</a>.</note>

## Supported technologies

%linter% provides inspections for the following technologies.

<table style="none">
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
            <p>MongoDB</p>
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

<include from="lib_qd.topic" element-id="root-and-non-root-users-info-bubble"></include>

<p><include from="lib_qd.topic" element-id="qodana-cli-quickstart" use-filter="php-only,jvm-php,non-gs,other,empty"/></p>



<!--<include from="lib_qd.topic" element-id="linter-next-steps-footer" use-filter="empty,for-php-linter"/>-->





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
