[//]: # (title: Qodana IntelliJ)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<var name="linter" value="Qodana IntelliJ"/>

<note>

<include src="lib_qd.xml" include-id="supported-techs">
    <var name="linter" value="Qodana IntelliJ"/>
    </include>

</note>

The Qodana IntelliJ linters let you perform [static analysis](https://en.wikipedia.org/wiki/Static_program_analysis) of your codebase. It brings all the smarts from IntelliJ IDEs, which help you: 

- detect anomalous code and probable bugs
- eliminate dead code 
- highlight spelling problems
- improve overall code structure
- introduce coding best practices

Each linter covers the technologies supported by the corresponding IntelliJ IDE. Currently, the following linters are available:
- [](qodana-jvm.md)
- [](qodana-jvm-community.md)
- [](qodana-android.md)
- [](qodana-php.md)
- [](qodana-python.md)
- [](qodana-go.md)


<tip>

<include src="lib_qd.xml" include-id="qodana-playground-tip">
    <var name="qodana-playground-url" value="https://qodana.teamcity.com/project/Hosted_Root_Java?mode=builds#all-projects"/>
    <var name="linter" value="Qodana IntelliJ linters"/>
</include>

</tip>

## Next steps

- <a href="qodana-intellij-docker-readme.md">Configure %linter% Docker image</a>
- <a href="qodana-intellij-github-action.md">Run %linter% on GitHub</a>
- <a href="qodana-intellij-github-application.md">Run %linter% as a GitHub App</a>
- <a href="service.md">Use %linter% as a Service</a>
- <a href="ci.md">Extend your CI/CD with %linter% plugins</a>
