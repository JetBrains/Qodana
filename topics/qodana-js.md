[//]: # (title: Qodana for JS)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<note>
    <p>
<include src="lib_qd.xml" include-id="eap-warning">
<var name="product" value="Qodana JS"/>
</include>
</p>
</note>

<var name="linter" value="Qodana for JS"/>

<var name="linter" value="Qodana JS"/>
<var name="ide" value="WebStorm"/>
<var name="docker-image" value="jetbrains/qodana-js"/>

%linter% is based on [%ide%](https://www.jetbrains.com/webstorm/) and provides static analysis for JavaScript or TypeScript projects.

## Try it now

### Analyze a project locally

<p><include src="lib_qd.xml" include-id="qodana-cli-quickstart" filter="js-only,non-gs,empty"/></p>

## Next steps

- <a href="qodana-js-docker-readme.xml">Configure %linter% Docker image</a>
- <a href="qodana-github-action.md">Run %linter% on GitHub</a>
- <a href="qodana-github-application.md">Run %linter% as a GitHub App</a>
- <a href="service.md">Use %linter% as a Service</a>
- <a href="ci.md">Extend your CI/CD with %linter% plugins</a>
