[//]: # (title: Project tokens)

Generally available [paid linters](pricing.md#pricing-linters-licenses) require that you use the 
`QODANA_TOKEN` variable to provide a [project token](cloud-projects.xml#cloud-manage-projects) while running %product%, 
for example: 

<tabs>
    <tab title="Qodana CLI" id="project-token-cli-tab">
        <code style="block" lang="shell" prompt="$">
            qodana scan \
               -e QODANA_TOKEN="&lt;qodana-cloud-token&gt;"
        </code>
    </tab>
    <tab title="Docker image" id="project-token-docker">
        <code style="block" lang="shell" prompt="$">
            docker run \
               -v $(pwd):/data/project/ \
               -e QODANA_TOKEN="&lt;qodana-cloud-token&gt;" \
                jetbrains/qodana-&lt;linter&gt;        
        </code>
    </tab>
</tabs>

The `QODANA_TOKEN` variable contains information that %product% linters use for identification and verification.
Based on this, %product% establishes a connection with Qodana Cloud.

Below is the description of interaction between %product% and Qodana Cloud once the connection is established. 

## License verification

The paid %product% linters request and verify license information from a Qodana Cloud [organization](cloud-organizations.xml). 
If the verification step fails, %product% returns an error meaning that you cannot run a specific linter under the 
current license. 

For example, you will not be able to run %product% using an expired license, or a license issued for another Qodana Cloud 
organization. Nor can you use the full potential of the [Qodana for JVM](qodana-jvm.md) linter using the 
[Community license](pricing.md#pricing-linters-licenses) because this will significantly reduce the linter functionality.
To avoid this, you should obtain compatible and up-to-date licenses for each linter that you use.

## Report collection

Additionally, your local %product% report is bound with the project in [Qodana Cloud](cloud-projects.xml). After binding, 
you can overview actual %product% [reports](cloud-overview-reports.xml) in an aggregated and handy format, as well as 
keep historical overview of older Qodana reports. 

Once the project token is generated, you can regenerate or delete it as shown in the 
[](cloud-projects.xml#cloud-manage-projects) section of the Qodana Cloud documentation.