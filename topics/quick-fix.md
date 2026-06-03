[//]: # (title: Quick-Fix)

**Quick-Fix** lets you improve development performance through fixing codebase problems automatically.

Quick-Fix is available on the Ultimate and Ultimate Plus [licenses](pricing.md), visit 
the [Subscription Options and Pricing](https://www.jetbrains.com/qodana/buy/?billing=yearly) page to learn more about available %product% licenses.
You can also [request a demo](https://www.jetbrains.com/qodana/request-a-demo/).

This feature is supported by the following linters and their trial versions:

* [%jvm%](jvm.md)
* [%python%](python.md)
* [%php%](php.md)
* [%js%](js.md)
* [%go%](golang.md)
* [%dotnet%](dotnet.md)

## How Quick-Fix works

<link-summary>Learn how you can configure Quick-Fix strategies. </link-summary>

<link-summary>Learn more about available Quick-Fix strategies and running Qodana with the Quick-Fix feature enabled.</link-summary>

You can choose between several Quick-Fix strategies mentioned in this table. 

<table>
    <tr>
        <td>Quick-Fix strategy</td>
        <td>Description</td>
    </tr>
    <tr>
        <td><code>NONE</code></td>
        <td>The default strategy that requires no configuration and implies that no Quick-Fixes are applied to your project</td>
    </tr>
    <tr>
        <td><code>CLEANUP</code></td>
        <td>Automatic application of the minor and safe cleanup inspections that do not affect the project logic and behavior</td>
    </tr>
    <tr>
        <td><code>APPLY</code></td>
        <td>
            <p>%instance% attempts to evaluate and fix all problems detected in the codebase.</p>
            <p>This approach may lead to serious code modifications that can affect the project logic and behavior. These changes
should be reviewed before submitting</p>
        </td>
    </tr>
</table>

You can apply Quick-Fix strategies using the following available options:

<tabs>
    <tab title="Docker and Qodana CLI" id="quick-fix-cli-docker">
        <p>Depending on the Quick-Fix strategy, run %instance% using either the <code>--apply-fixes</code> or the <code>--cleanup</code> option. The <code>QODANA_TOKEN</code> variable 
            refers to the <a href="project-token.md">project token</a> required by the 
            <a href="pricing.md" anchor="pricing-linters-licenses">Ultimate and Ultimate Plus</a> linters. </p>
        <tabs>
            <tab title="Docker">
                <code-block lang="shell" prompt="$">
                    docker run \
                       -v &lt;source-directory&gt;/:/data/project/  \
                       -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                       jetbrains/qodana-&lt;image&gt; \
                       &lt;--apply-fixes/--cleanup&gt;
                </code-block>
            </tab>
            <tab title="Qodana CLI">
                <code-block lang="shell" prompt="$">
                qodana scan \
                   -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                   &lt;--apply-fixes/--cleanup&gt;
                </code-block>
            </tab>
        </tabs>
    </tab>
    <tab title="qodana.yaml" id="quick-fix-qodana-yaml">
        <p>You can use the <code>fixesStrategy</code> option in the <a href="qodana-yaml.md"><code>qodana.yaml</code></a> file:</p>
        <code-block lang="yaml">
            fixesStrategy: cleanup/apply
        </code-block>
    </tab>
    <tab title="GitHub Actions" id="quick-fix-ci-pipeline">
        <p>Learn the <a href="github.md"/> section for details.</p>
    </tab>
</tabs>