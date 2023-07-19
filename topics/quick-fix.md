[//]: # (title: Quick-fixes)

**Quick-fixes** lets you improve development performance through fixing codebase problems automatically.

This feature is available starting from version 2023.2 of %product% and supported by all [linters](linters.md) except
Qodana for .NET under the Ultimate, and Ultimate Plus [licenses](pricing.md) and their trial versions.

## How it works

You can choose between several quick-fix strategies mentioned in this table. 

<table>
    <tr>
        <td>Quick-fixes strategy</td>
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

To apply either the `cleanup` or the `apply` quick-fix strategy, specify it using the `--fixes-strategy` 
[option](docker-image-configuration.xml): 

<tabs>
    <tab title="Docker image" id="quick-fix-docker">
        <code style="block" lang="shell" prompt="$">
            docker run \
               -v &lt;source-directory&gt;/:/data/project/  \
               jetbrains/qodana-&lt;linter&gt; \
               --fixes-strategy &lt;cleanup/apply&gt;
        </code>
    </tab>
    <tab title="Qodana CLI" id="quick-fix-cli">
        <code style="block" lang="shell" prompt="$">
            qodana scan \
               --apply-fixes/--cleanup
        </code>
    </tab>
</tabs>

Or specify it in the [`qodana.yaml` file](qodana-yaml.md):

```yaml
fixesStrategy: cleanup/apply
```

## CI integration

Currently, only GitHub Actions with GitHub repositories are supported.