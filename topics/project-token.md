[//]: # (title: Project and organization tokens)

<link-summary>A project token contains information that Qodana linters use for identification and verification. </link-summary>

Generally available [paid linters](pricing.md#pricing-linters-licenses) require that you identify and verify your %product% usage by means of tokens. This is necessary for
establishing a connection with %cloud% and subsequent [license verification](#License+verification) and [report collection](#Report+collection). 

Depending on your needs, you can use either a project or an organization token:

| Token type | Description |
|---|--|
| [Project token](#Project+token) | You generate and use each separate token for each separate project. <br> Working with multiple projects requires generating and managing multiple project tokens. |
| [Organization token](#Organization+token) | A single organization-level token lets you get access to all projects in the organization. <br> Compared to project tokens, this requires more configuration. | 

## Project token

While creating a [project in %cloud%](cloud-projects.topic#cloud-manage-projects), you get a project token generated. 
After then, use the `QODANA_TOKEN` variable to provide a reference to its value in your %product% configuration, 
for example: 

<tabs group="token-tabs">
    <tab title="Qodana CLI" group-key="token-cli-tab" id="project-token-cli-tab">
        <code-block lang="shell" prompt="$">
            qodana scan \
               -e QODANA_TOKEN="&lt;qodana-cloud-token&gt;"
        </code-block>
    </tab>
    <tab title="Docker image" group-key="token-docker-tab" id="project-token-docker-tab">
        <code-block lang="shell" prompt="$">
            docker run \
               -v $(pwd):/data/project/ \
               -e QODANA_TOKEN="&lt;qodana-cloud-token&gt;" \
                jetbrains/qodana-&lt;image&gt;        
        </code-block>
    </tab>
</tabs>

## Organization token

<link-summary>
A single organization-level token lets you generate tokens for all projects in the organization.  
</link-summary>

An organization token gives you access to a [%cloud% organization](cloud-organizations.topic). To identify a specific project within it, you need 
team and project slugs as shown in the steps below:

<procedure>
<step>Generate an organization token in %cloud%.</step>
<step>Get the team slug using either the %cloud% URL like <code>AbCdE</code> from <code>https://qodana.cloud/teams/AbCdE</code>, or the API method described in the <a href="experimental-api.md" anchor="Create+teams"/> chapter. </step> 
<step>Using the %cloud% URL, get the project slug. For example, this will be <code>AbCde</code> from <code>https://qodana.cloud/projects/AbCde/</code>.</step>
<step><p>Use the the <code>QODANA_ORG_TOKEN</code> variable to refer to the organization token. 
Also, use the <code>QODANA_PROJECT_SLUG</code> variable or the <code>projectSlug</code> key in your YAML configuration to refer to the team and project slugs in the <code>[team-slug]:[project-slug]</code> format. For example:</p>
<tabs group="token-tabs">
    <tab title="Qodana CLI" group-key="token-cli-tab" id="org-token-cli-tab">
        <code-block lang="shell" prompt="$"><![CDATA[
            qodana scan \
               -e QODANA_ORG_TOKEN="<qodana-organization-token>" \
               -e QODANA_PROJECT_SLUG="<team-slug>:<project-slug>" \
        ]]>
        </code-block>
    </tab>
    <tab title="Docker image" group-key="token-docker-tab" id="org-token-docker-tab">
        <code-block lang="shell" prompt="$"><![CDATA[
            docker run \
               -v $(pwd):/data/project/ \
               -e QODANA_ORG_TOKEN="<qodana-organization-token>" \
               -e QODANA_PROJECT_SLUG="<team-slug>:<project-slug>" \
                jetbrains/qodana-<image>        
        ]]>
</code-block>
    </tab>
</tabs>
</step>
</procedure>

## License verification

<link-summary>
The paid %instance% linters request and verify license information from a %cloud% organization. 
If the verification step fails, the linter returns an error meaning that you cannot run it using the current license.
</link-summary>

The paid %instance% linters request and verify license information from a %cloud% [organization](cloud-organizations.topic). 
If the verification step fails, the linter returns an error meaning that you cannot run it using the current license.

For example, you cannot run %instance% using an expired license. Nor can you run the 
[%jvm%](jvm.md) linter using the [Community license](pricing.md#pricing-linters-licenses).
To avoid this, you should get compatible and valid licenses for each linter that you use.

## Report collection

<link-summary>
You can view actual %instance% reports in an aggregated and handy format, as well as 
keep a historical overview of older %product% reports. 
</link-summary>

Your local %instance% report is bound with the project in [%cloud%](cloud-projects.topic). After binding, 
you can view actual %instance% [reports](cloud-overview-reports.topic) in an aggregated and handy format, as well as 
keep a historical overview of older %product% reports. 
