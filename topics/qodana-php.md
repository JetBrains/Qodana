[//]: # (title: Qodana for PHP)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<img src="php-linter.png" dark-src="php-linter_dark.png" alt="Qodana for PHP linter languages" width="296"/>

<note>
<p>
<include src="lib_qd.xml" include-id="eap-warning">
<var name="product" value="Qodana PHP"/>
</include>
</p>
</note>

<var name="linter" value="Qodana PHP"/>
<var name="ide" value="PhpStorm"/>
<var name="docker-image" value="jetbrains/qodana-php:2023.1-eap"/>

%linter% is based on [%ide%](https://www.jetbrains.com/phpstorm/). <include src="lib_qd.xml" include-id="linter-intro"/>

%linter% provides inspections for PHP, JavaScript, and TypeScript.

## Try it now

### Analyze a project locally

<p><include src="lib_qd.xml" include-id="qodana-cli-quickstart" use-filter="php-only,jvm-php,non-gs,other,empty"/></p>

## Next steps

- <a href="qodana-php-docker-readme.xml">Configure %linter% Docker image</a>
- <a href="github.md">Run %linter% on GitHub</a>
- <a href="service.md">Use %linter% as a Service</a>
- <a href="ci.md">Extend your CI/CD with %linter% plugins</a>
- <a href="php-language-upgrade.xml">See how migration between PHP versions will affect the code quality</a>