# Requirements

## %product% license

Reach out to our support team to request a license that can be used by `qodana-installer-cli` and %premlite%.

## System and network requirements

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
    <tab title="Object storage">
        <p>%premlite% supports MinIO starting from version <code>RELEASE.2025-01-20T14-49-07Z</code> onwards.</p>
    </tab>
</tabs>

