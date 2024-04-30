[//]: # (title: Inspect Python code)

<link-summary>A use case explaining how you can Qodana to inspect your Python code.</link-summary>

<var name="JenkinsCred" value="https://www.jenkins.io/doc/book/using/using-credentials/#adding-new-global-credentials"/>
<var name="docker-image" value="jetbrains/qodana-python&lt;-community&gt;:2024.1"/>

To inspect your Python codebase, depending on your %product% [license](pricing.md), you can employ the following linters: 

<tabs>
<tab id="inspect-python-code-linters" title="Linters">

| Linter name                    | Suitable %product% licenses |
|--------------------------------|-----------------------------|
| [](qodana-python.md)           | Ultimate and Ultimate Plus  |
| [](qodana-python-community.md) | Community                   |

</tab>
<tab id="inspect-python-code-techs" title="Supported technologies and features">

Here is the list of technologies and features supported by both linters.

| Supported technologies and features                                                                                                                                     | [](qodana-python.md) | [](qodana-python-community.md) |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|--------------------------------|
| Python, CSS, HTML, JSON and JSON5, RELAX NG, XML, YAML, shell scripts, MongoJS, MySQL, Oracle, PostgreSQL, SQL, SQL Server, Django, Google App Engine, Jupyter, Pyramid | &#x2714;             | &#x2714;                       |
| [](baseline.topic)                                                                                                                                                      | &#x2714;             | &#x2714;                       |
| [](quality-gate.topic)                                                                                                                                                  | &#x2714;             | &#x2714;                       |
| [](license-audit.topic)                                                                                                                                                    | &#x2714;             | &#x274c;                       |
| [](quick-fix.md)                                                                                                                                                        | &#x2714;             | &#x274c;                       |
| [](vulnerability-checker.md)                                                                                                                                            | &#x2714;             | &#x274c;                       |

</tab>
</tabs>

## Install project dependencies

You can install project dependencies using the [`bootstrap`](before-running-qodana.md) key, for example:

```yaml
bootstrap: |
  pip install -r requirements.txt
```

## Inspect your code

Here are several configuration snippets showing how you can inspect Python code.

<tabs>
<tab id="inspect-python-code-github" title="GitHub Actions">
<include from="lib_qd.topic" element-id="github-basic-configuration"/>

</tab>
<tab id="inspect-python-code-jenkins" title="Jenkins">

Here is the Jenkins Pipeline configuration.

```groovy
pipeline {
    environment {
        QODANA_TOKEN=credentials('qodana-token')
    }
    agent {
        docker {
            args '''
              -v "${WORKSPACE}":/data/project
              --entrypoint=""
              '''
            image '%docker-image%'
        }
    }
    stages {
        stage('Qodana') {
            steps {
                sh '''qodana'''
            }
        }
    }
}
```

In this configuration, the `environment` block defines the `QODANA_TOKEN` variable to invoke the
[project token](project-token.md) generated in Qodana Cloud and contained in
the `qodana-token` [global credentials](%JenkinsCred%). The project token is required by paid %product%
[linters](pricing.md#pricing-linters-licenses), and is optional for using the Community linters.

</tab>
<tab id="inspect-python-code-local" title="Local run">
<p>Qodana provides two options for local analysis of your code.
    <a href="https://github.com/JetBrains/qodana-cli">Qodana CLI</a> is the easiest option to start.
    Alternatively, you can use the Docker command from the <ui-path>Docker image</ui-path> tab.</p>
<tabs>
    <tab id="qodana-cli-tab" title="Qodana CLI">
        <p>Assuming that you have already
            <a href="https://github.com/JetBrains/qodana-cli/releases/latest">installed</a> Qodana CLI on your
            machine, you can run this command in the project root directory:</p>
        <code-block prompt="$">
            qodana scan \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               -l %docker-image%
        </code-block>
        <p>Here, the <code>QODANA_TOKEN</code> variable refers to the <a href="project-token.md">project token</a>.</p>
    </tab>
    <tab id="docker-image-tab" title="Docker image">
        <p>To start, pull the image from Docker Hub (only necessary to get the latest version):</p>
        <code-block lang="shell" prompt="$">
            docker pull %docker-image%
        </code-block>
        <p>Start local analysis with <code>source-directory</code>
            pointing to the root of your project and
            <code>QODANA_TOKEN</code> referring to the <a href="project-token.md">project token</a>:</p>
        <code-block lang="shell" prompt="$">
            docker run \
               -v &lt;source-directory&gt;/:/data/project/ \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               %docker-image%
        </code-block>
    </tab>
</tabs>

</tab>
</tabs>



