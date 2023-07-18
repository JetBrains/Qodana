[//]: # (title: Project tokens)

Generally available [paid linters](pricing.md#linters-available-per-each-license) require that you use the 
`QODANA_TOKEN` variable to provide a [project token](cloud-projects.xml#cloud-manage-projects) while running %product%, 
for example: 

```shell
docker run \
   -v $(pwd):/data/project/ \
   -e QODANA_TOKEN="<qodana-cloud-token>" \
   jetbrains/qodana-<linter>
```

Below is the description of what `QODANA_TOKEN` does. 

## License verification

First of all, using `QODANA_TOKEN` Qodana Cloud verifies whether your [organization](cloud-organizations.xml) has a 
valid and compatible license. Each %product% [linter](linters.md) collects information about the license and the Qodana 
Cloud [organization](cloud-organizations.xml) that a specific license was issued for. Once collected, this information 
is then submitted to Qodana Cloud for verification. If verification fails, %product% returns an error meaning that 
you cannot run a specific linter under the current license.

For example, you cannot run the [Qodana for JVM](qodana-jvm.md) linter using the [Community license](pricing.md#linters-available-per-each-license). 
Instead, you should buy either the Ultimate or Ultimate Plus license if this was not done previously.

## Report collection

Second, the token binds your local %product% report with the report available in Qodana Cloud. This lets you
overview actual %product% reports in an aggregated and handy format.
