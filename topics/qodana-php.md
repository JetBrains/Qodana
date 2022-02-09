[//]: # (title: Qodana for PHP)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<note>
<p>
<include src="lib_qd.xml" include-id="eap-warning">
<var name="product" value="Qodana PHP"/>
</include>
</p>
</note>

<var name="linter" value="Qodana PHP"/>
<var name="ide" value="PhpStorm"/>
<var name="docker-image" value="jetbrains/qodana-php"/>

%linter% is based on [%ide%](https://www.jetbrains.com/phpstorm/) and provides static analysis for PHP projects. <include src="lib_qd.xml" include-id="linter-intro"/>

## Try it now

### Analyze a project locally

<p><include src="lib_qd.xml" include-id="qodana-cli-quickstart" filter="php-only,jvm-php,non-gs,other,empty"/></p>

## Next steps

- <a href="qodana-php-docker-readme.xml">Configure %linter% Docker image</a>
- <a href="qodana-github-action.md">Run %linter% on GitHub</a>
- <a href="qodana-github-application.md">Run %linter% as a GitHub App</a>
- <a href="service.md">Use %linter% as a Service</a>
- <a href="ci.md">Extend your CI/CD with %linter% plugins</a>
- <a href="qodana-php-language-upgrade.xml">See how migration between PHP versions will affect the code quality</a>