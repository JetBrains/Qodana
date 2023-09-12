[//]: # (title: Quick-fix)

**Quick-fix** lets you improve development performance through fixing codebase problems automatically.

This feature is available starting from version 2023.2 of %product% and supported by all [linters](linters.md) except
Qodana for .NET under the Ultimate, and Ultimate Plus [licenses](pricing.md) and their trial versions.

## How it works

You can choose between several quick-fix strategies mentioned in this table. 

<table>
    <tr>
        <td>Quick-fix strategy</td>
        <td>Description</td>
    </tr>
    <tr>
        <td><code>NONE</code></td>
        <td>The default strategy that requires no configuration and implies that no quick-fixes are applied to your project</td>
    </tr>
    <tr>
        <td><code>CLEANUP</code></td>
        <td>Automatic application of the minor and safe cleanup inspections that do not affect the project logic and behavior</td>
    </tr>
    <tr>
        <td><code>APPLY</code></td>
        <td>
            <p>%product% attempts to evaluate and fix all problems detected in the codebase.</p>
            <p>This approach may lead to serious code modifications that can affect the project logic and behavior. These changes
should be reviewed before submitting</p>
        </td>
    </tr>
</table>

You can apply quick-fix strategies using the following available options:

<tabs>
    <tab title="Docker and Qodana CLI" id="quick-fix-cli-docker">
        <p>Run %product% with the <code>--fixes-strategy</code> option invoked. The <code>QODANA_TOKEN</code> variable 
            refers to the <a href="project-token.md">project token</a> required by the 
            <a href="pricing.md" anchor="pricing-linters-licenses">Ultimate and Ultimate Plus</a> linters. </p>
        <tabs>
            <tab title="Docker">
                <code style="block" lang="shell" prompt="$">
                    docker run \
                       -v &lt;source-directory&gt;/:/data/project/  \
                       -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                       jetbrains/qodana-&lt;linter&gt; \
                       --fixes-strategy &lt;cleanup/apply&gt;
                </code>
            </tab>
            <tab title="Qodana CLI">
                <code style="block" lang="shell" prompt="$">
                qodana scan \
                   -e QODANA_TOKEN="&lt;cloud-project-token&gt;" \
                   &lt;--apply-fixes/--cleanup&gt;
                </code>
            </tab>
        </tabs>
    </tab>
    <tab title="qodana.yaml" id="quick-fix-qodana-yaml">
        <p>You can use the <code>fixesStrategy</code> option in the <a href="qodana-yaml.md"><code>qodana.yaml</code></a> file:</p>
        <code style="block" lang="yaml">
            fixesStrategy: cleanup/apply
        </code>
    </tab>
    <tab title="CI pipeline" id="quick-fix-ci-pipeline">
        <p>Learn the <a href="github.md"/> and <a href="bitbucket.md"/> sections for details.</p>
    </tab>
</tabs>