# Python

<var name="qp" value="Qodana for Python"/>
<var name="qp-co" value="Qodana Community for Python"/>
<var name="qp-linter" value="jetbrains/qodana-python:2024.1"/>
<var name="qp-co-linter" value="jetbrains/qodana-python-community:2024.1"/>
<var name="qd-image" value="jetbrains/qodana-python<-community>:2024.1"/>

<link-summary>You can inspect your code using the %qp% and %qp-co% linters.</link-summary>

You can inspect your code using the %qp% linter is based on PyCharm Professional and licensed under the Ultimate and 
Ultimate Plus licenses, and the %qp-co% linter is based on PyCharm Community and licensed under the Community license. 
To learn more about %product% licenses, navigate to the [](pricing.md) page.  

## Prerequisites

%qp% requires a [project token](project-token.md) generated in Qodana Cloud.

If your project has external `pip` dependencies, you can set them up using the [`bootstrap`](before-running-qodana.md) 
field in the `qodana.yaml` file. For example, if your project dependencies are specified by the `requirements.txt` file 
in your project root, add the following line to [`qodana.yaml`](qodana-yaml.md#Run+custom+commands) that will be 
executed before the analysis:

```yaml
bootstrap: pip install -r requirements.txt
```

## Basic use cases

### Local run

<note><include from="lib_qd.topic" element-id="docker-ram-note"/></note>

By default, you can run these linters using [Qodana CLI](https://github.com/JetBrains/qodana-cli). If necessary,
check the [installation page](https://github.com/JetBrains/qodana-cli/releases/latest) to install
Qodana CLI. Alternatively, you can use the Docker commands from the <ui-path>Docker image</ui-path> tab.

<include from="lib_qd.topic" element-id="root-and-non-root-users-info-bubble"></include>

<tabs>
    <tab id="qodana-cli-tab" title="Qodana CLI">
        <code-block prompt="$">
            qodana scan \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               -l %qd-image%
        </code-block>
        <p>Here, the <code>QODANA_TOKEN</code> variable refers to the <a href="project-token.md">project token</a>.</p>
        <p>If you omit the <code>-l</code> option, the %qp% linter will run by default.</p>
    </tab>
    <tab id="docker-image-tab" title="Docker image">
        <p>To start, pull the image from Docker Hub (only necessary to get the latest version):</p>
        <code-block lang="shell" prompt="$">
            docker pull %qd-image%
        </code-block>
        <p>Start local analysis with <code>source-directory</code> pointing to the root of your project and
            <code>QODANA_TOKEN</code> referring to the <a href="project-token.md">project token</a>:</p>
        <code-block lang="shell" prompt="$">
            docker run \
               -v &lt;source-directory&gt;/:/data/project/ \
               -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
               %qd-image%
        </code-block>
        <p>In your browser, open <a href="https://qodana.cloud">Qodana Cloud</a> to examine inspection results.
            Here, you can also reconfigure the analysis, see the <a href="ui-overview.md"/> section for
            details.</p>
    </tab>
</tabs>

### CI/CD pipelines



<!-- Short examples to provide here about each CI/CD -->


