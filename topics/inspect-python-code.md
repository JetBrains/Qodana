[//]: # (title: Inspect Python code)

To inspect your Python codebase, depending on your %product% [license](pricing.md) you can employ the  following linters: 

<tabs>
<tab id="inspect-python-code-linters" title="Linters">

| Linter name                    | Suitable %product% licenses |
|--------------------------------|-----------------------------|
| [](qodana-python.md)           | Ultimate and Ultimate Plus  |
| [](qodana-python-community.md) | Community                   |


</tab>
<tab id="inspect-python-code-techs" title="Supported technologies and features">

Here is the list of technologies and features supported by both linters.

| Supported technologies and features                                                                                                                                      | [](qodana-python.md) | [](qodana-python-community.md) |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|--------------------------------|
| Python, CSS, HTML, JSON and JSON5, RELAX NG, XML, YAML, Shell script, MongoJS, MySQL, Oracle, PostgreSQL, SQL, SQL Server, Django, Google App Engine, Jupyter, Pyramid   | &#x2714;             | &#x2714;                       |
| [](baseline.xml)                                                                                                                                                         | &#x2714;             | &#x2714;                       |
| [](quality-gate.xml)                                                                                                                                                     | &#x2714;             | &#x2714;                       |
| [](license-audit.xml)                                                                                                                                                    | &#x2714;             | &#x274c;                       |
| [](quick-fix.md)                                                                                                                                                         | &#x2714;             | &#x274c;                       |
| [](vulnerability-checker.md)                                                                                                                                             | &#x2714;             | &#x274c;                       |

</tab>
</tabs>

Here are several configuration snippets showing how you can inspect Python code.

<!-- I need to modify all these tabs accordingly -->

<tabs>
<tab id="inspect-python-code-github" title="GitHub Actions">
    <include src="lib_qd.xml" include-id="github-basic-configuration"/>
</tab>
<tab id="inspect-python-code-jenkins" title="Jenkins">
    <include src="jenkins.md" include-id="jenkins-basic-config"/>
</tab>
<tab id="inspect-python-code-local" title="Run locally">
<include src="lib_qd.xml" include-id="qodana-cli-quickstart" use-filter="non-php,py-only,non-gs,empty"/>
</tab>
</tabs>



