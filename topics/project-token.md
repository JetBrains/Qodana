[//]: # (title: Project tokens)

<link-summary>A project token contains information that Qodana linters use for identification and verification. </link-summary>

Generally available [paid linters](pricing.md#pricing-linters-licenses) require that you use the 
`QODANA_TOKEN` variable to provide a [project token](cloud-projects.topic#cloud-manage-projects) while running %instance%, 
for example: 

<tabs>
    <tab title="Qodana CLI" id="project-token-cli-tab">
        <code-block lang="shell" prompt="$">
            qodana scan \
               -e QODANA_TOKEN="&lt;qodana-cloud-token&gt;"
        </code-block>
    </tab>
    <tab title="Docker image" id="project-token-docker">
        <code-block lang="shell" prompt="$">
            docker run \
               -v $(pwd):/data/project/ \
               -e QODANA_TOKEN="&lt;qodana-cloud-token&gt;" \
                jetbrains/qodana-&lt;linter&gt;        
        </code-block>
    </tab>
</tabs>

The `QODANA_TOKEN` variable contains information that %instance% linters use for identification and verification.
Based on this, %instance% establishes a connection with Qodana Cloud.

Below is the description of interaction between %instance% and Qodana Cloud once the connection is established. 

## License verification

The paid %instance% linters request and verify license information from a Qodana Cloud [organization](cloud-organizations.topic). 
If the verification step fails, the linter returns an error meaning that you cannot run it using the current license.

For example, you cannot run %instance% using an expired license. Nor can you run the 
[Qodana for JVM](qodana-jvm.md) linter using the [Community license](pricing.md#pricing-linters-licenses).
To avoid this, you should obtain compatible and up-to-date licenses for each linter that you use.

## Report collection

Additionally, your local %instance% report is bound with the project in [Qodana Cloud](cloud-projects.topic). After binding, 
you can view actual %instance% [reports](cloud-overview-reports.topic) in an aggregated and handy format, as well as 
keep a historical overview of older Qodana reports. 

Once the project token is generated, you can regenerate or delete it as shown in the 
[](cloud-projects.topic#cloud-manage-projects) section of the Qodana Cloud documentation.

## Linters that require project tokens

Here is the list of linters that require project tokens: 

* [](qodana-jvm.md)
* [](qodana-php.md)
* [](qodana-python.md)
* [](qodana-js.md)
* [](qodana-go.md)
* [](qodana-dotnet.md)
* [](qodana-dotnet-community.md)

This is the list of linters where project token usage is optional: 

* [](qodana-jvm-community.md)
* [](qodana-jvm-android.md)
* [](qodana-python-community.md)

Without a project token, you will not be able to upload and study analysis reports in [Qodana Cloud](cloud-about.topic). 