# Introduction

<!-- Exact name of the product -->
<!-- If the utility name is not used anywhere, can it be omitted at all? -->

%premlite% is an on-premises version of [%cloud%](cloud-use-cases.topic).

Using %premlite%, you can run %product% within your infrastructure ensuring that sensitive code and data remain secure and 
private, which is particularly useful for organizations that need powerful static analysis tools but must operate
within strict security or compliance standards. 

This documentation guides you through the installation, product configuration, and initialization stages. 

## %premlite% features

Data privacy lets you store sensitive code within your organization's infrastructure.
Scalability lets you scale %premlite% to meet the needs of larger teams or organizations with extensive codebases.
Customizability lets you configure %product% to match their specific code quality requirements.
%premlite% lets you use local hosting on your infrastructure to ensure code and data privacy. 

> %premlite% supports a single server installation meaning that a Docker Swarm cluster should have one node.
{style="note"}

`qodana-installer-cli` is a command-line utility that offers you a one-line installer for %premlite%. The utility requires a
server running Linux with the Docker Engine and Docker Swarm as a container orchestrator. It is compatible with
automation and Infrastructure as a Code (IaC) frameworks.

## Requirements

### %product% license

Reach out to our support team to request a licence that can be used by `qodana-installer-cli` and %premlite%.

### System and network requirements

Below are the requirements grouped in categories.

<tabs>
    <tab title="Hardware and software">
        <table>
            <tr>
                <td>Attribute</td>
                <td>Value</td>
            </tr>
            <tr>
                <td>CPU Architecture</td>
                <td>AMD64_86, ARM64</td>
            </tr>
            <tr>
                <td>Number of cores</td>
                <td>>= 4</td>
            </tr>
            <tr>
                <td>RAM</td>
                <td>>= 16GB</td>
            </tr>
            <tr>
                <td>HDD</td>
                <td>>= 100GB</td>
            </tr>
            <tr>
                <td>Operating system</td>
                <td>Any Linux distribution that supports a compatible CPU Architecture</td>
            </tr>
            <tr>
                <td>Docker version</td>
                <td>20.10.23 or later</td>
            </tr>
        </table>
    </tab>
    <tab title="Network">
        <p><code>qodana-installer-cli</code> references container images from the <code>quay.io</code> Docker registry. Make sure that 
            <code>quay.io</code> is a trusted address in the network. For offline installations, mirror 
            to an internal trusted Docker registry the tags available in the 
            <code>https://quay.io/repository/jetbrains/qodana-installer-cli-dependencies</code> Docker registry.
        </p>
        <p>For usage statistics dynamic configuration, download the configuration from the 
            <a href="https://resources.jetbrains.com/storage/fus/config/v4/QD/QDCLD.json">JetBrains website</a>. 
           Also, the following FQDNs must be accessible if you wish to share analytics with the %product% team:</p>
            <list>
                <li><code>https://analytics.services.jetbrains.com</code></li>
                <li><code>https://resources.jetbrains.com</code></li>
            </list>
    </tab>
    <tab title="S3-compliant storage">
        <p>%premlite% supports S3 directly in AWS, as well as Minio starting 
            from version <code>RELEASE.2025-01-20T14-49-07Z</code> onwards.</p>
    </tab>
</tabs>

