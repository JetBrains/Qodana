[//]: # (title: Qodana for Python)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<note>
    <p>
<include src="lib_qd.xml" include-id="eap-warning">
<var name="product" value="Qodana Python"/>
</include>
</p>
</note>

<var name="linter" value="Qodana Python"/>
<var name="ide" value="PyCharm Professional"/>
<var name="docker-image" value="jetbrains/qodana-python"/>

%linter% is based on [%ide%](https://www.jetbrains.com/pycharm/) and provides static analysis for Python projects.

## Try it now

### Analyze a project locally

<p><include src="lib_qd.xml" include-id="qodana-cli-quickstart" filter="py-only,empty"/></p>

## Next steps

- <a href="qodana-python-docker-readme.xml">Configure %linter% Docker image</a>
- <a href="qodana-github-action.md">Run %linter% on GitHub</a>
- <a href="qodana-github-application.md">Run %linter% as a GitHub App</a>
- <a href="service.md">Use %linter% as a Service</a>
- <a href="ci.md">Extend your CI/CD with %linter% plugins</a>