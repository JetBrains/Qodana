# JavaScript and TypeScript

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<img src="js.png" dark-src="js_dark.png" alt="Qodana for .NET linter languages" width="296"/>

<var name="linter" value="Qodana for JS"/>
<var name="ide" value="WebStorm"/>
<var name="docker-image" value="jetbrains/qodana-js:2024.2-eap"/>
<var name="config-file" value="qodana-js-docker-readme.topic"/>

<var name="linter-shell" value="qodana-js"/>
<var name="ide" value="WebStorm"/>
<var name="code-inspection-ide-help-url" value="https://www.jetbrains.com/help/webstorm/?Code_Inspection"/>
<var name="code-inspection-profiles-ide-help-url" value="https://www.jetbrains.com/help/webstorm/?Customizing_Profiles"/>


<link-summary>%linter% is based on %ide% and provides static analysis for JavaScript or TypeScript projects.</link-summary>

%linter% is based on [%ide%](https://www.jetbrains.com/webstorm/). It provides static analysis for JavaScript or TypeScript projects.

<note>This linter requires the Qodana Cloud <a href="project-token.md">project token</a>.</note>

## Supported technologies

%linter% provides inspections for the following technologies.

<table style="none">
    <tr>
        <td>Programming languages</td>
        <td>
            <p>JavaScript</p>
            <p>TypeScript</p>
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
    <tr>
        <td>Frameworks and libraries</td>
        <td>
            <p>Angular</p>
            <p>Cucumber</p>
            <p>EJS</p>
            <p>Handlebars/Mustache</p>
            <p>Less</p>
            <p>Node.js</p>
            <p>PostCSS</p>
            <p>Pug/Jade</p>
            <p>React</p>
            <p>Sass/SCSS</p>
            <p>Vue</p>
        </td>
    </tr>
</table>

## Supported features

<include from="lib_qd.topic" element-id="linters-supported-features" use-filter="empty,js"/>

## Try it now

### Analyze a project locally

#### Install project dependencies

For a basic JavaScript project that has no external dependencies, no preliminary steps are required.

In case the project has external dependencies, you can set them up using the `bootstrap` key in the `qodana.yaml` file.
For example, if your project dependencies are specified by the `yarn.lock` file in your project root, add the following
line to `qodana.yaml`:

```yaml
bootstrap: yarn install
```
The command will be automatically executed before the analysis. You can use the `pnpm`, `npm` or `yarn` commands to install dependencies.

#### Enable ESLint

ESLint is widely used in JavaScript projects. You can enable it using the `qodana.yaml` file:

```yaml
include:
    - name: Eslint
```

#### Run analysis

<include from="lib_qd.topic" element-id="root-and-non-root-users-info-bubble"></include>

<p><include from="lib_qd.topic" element-id="qodana-cli-quickstart" use-filter="non-php,js-only,non-gs,empty"/></p>



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