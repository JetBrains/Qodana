# Requirements

## Qodana license

Reach out to our support team to request a license that can be used by %premlite%.

## System and network requirements

### Kubernetes version

<link-summary>See the requirements for a Kubernetes cluster of %premlite%.</link-summary>

Below are the requirements grouped in categories.

<tabs>
    <tab title="Kubernetes cluster">
        <table>
            <tr>
                <td>Environment</td>
                <td>CPU (cores)</td>
                <td>RAM (GB)</td>
                <td>Storage (GB)</td>
                <td>Notes</td>
            </tr>
            <tr>
                <td>Demo/PoC (small team)</td>
                <td>6-8</td>
                <td>8</td>
                <td>40-60</td>
                <td>Single-node possible, not HA</td>
            </tr>
            <tr>
                <td>Small prod</td>
                <td>8-16</td>
                <td>16-32</td>
                <td>100-200</td>
                <td>3+ nodes, HA with only multi nodes</td>
            </tr>
            <tr>
                <td>Medium-to-large prod</td>
                <td>16+</td>
                <td>32+</td>
                <td>200+</td>
                <td>Scale per workload, more for large codebases</td>
            </tr>
        </table>
<!--What are pods? This needs to be explained or simplified  -->
<!--This is probably related to the configuration step, not description of requirements  -->
<!--SH pods is nonsense, needs to be moved to the configuration stage as a note  -->
        <p>In case of a single-node configuration, limited resources are not sufficient for the Kubernetes Scheduler and 
           Kubelet for deployments that mutate the configuration state of Self-Hosted (SH) pods. In such a case, 
           proceed with two-step deployment: with the first step apply the configuration change and set the replicaCount 
           of SH pods to 0, wait for the deployment to succeed and proceed with the second step where you set the 
           <code>replicaCount</code> from 0 to 1. Another alternative that avoids this is to provision a multi-node 
           Kubernetes cluster such that pods are distributed cross nodes and are not limited by the limitation of a one node cluster.
        </p>
</tab>
<!--Kubernetes requirements need to be referenced to the Kubernetes website  -->
    <tab title="Kubernetes software">
        <table>
            <tr>
                <td>Attribute</td>
                <td>Value(s)</td>
            </tr>
            <tr>
                <td>Operating system</td>
                <td>Any Linux distribution that satisfies Kubernetes requirements</td>
            </tr>
            <tr>
<!-- Add that in the examples Containerd will be used  -->
                <td>Container runtime</td>
                <td>Any container runtime that satisfies Kubernetes requirements</td>
            </tr>
            <tr>
<!-- Add here that NGINX will be used  -->
                <td>Ingress controller</td>
                <td>Any Ingress Controller that is deployed in the Kubernetes cluster as a cluster service and can resolve service URLs</td>
            </tr>
            <tr>
<!-- Needs to be referenced, but a bit later  -->
                <td>Storage controller</td>
                <td>Any Storage Controller that allows volumes to migrate cross nodes based on pod locations</td>
            </tr>
        </table>
        <p>
<!-- This should be moved to the configuration stage, around Ingress  -->
            For any ingress controller, you must configure redirect behavior, client identity propagation, 
            and size/buffering limits.</p>
            <p>First, decide where TLS terminates and who performs HTTP to HTTPS redirects; if 
            your edge LB/CDN already enforces HTTPS, disable redirects at the ingress to avoid loops and double hops.</p> 
            <p>Second, ensure your apps see the real client IP, scheme, and host: choose the appropriate mechanism your 
            controller supports (X-Forwarded-* headers, Forwarded header, or PROXY protocol) and restrict trust to 
            known upstream CIDRs so users can’t spoof IPs.</p> 
            <p>
            Third, right-size limits for request headers, request bodies, 
            and response buffering to match your workloads (SSO cookies, many Set-Cookie headers, file uploads, streaming). </p> 
            <p>Each controller exposes different knobs and names for these concepts, but they map to the same concerns: header 
            buffer sizes, large-header buffers, max body size, proxy buffer sizes, forwarded header handling, and optional 
            proxy protocol. Review your controller’s documentation for the exact settings, mirror the intent of the 
            examples shown for NGINX, and validate under load tests to confirm no 400/413 responses, no misreported 
            client IPs, and consistent redirect behavior.</p>
        <p>Below is an example configuration for Kubernetes nginx ingress controller.</p>
<!-- This needs to be moved out of here  -->
        <code-block block="yaml" collapsible="true">
            #  Disabling avoids double redirects, redirect loops, and unnecessary hops during health checks or internal service calls over HTTP. Services with external URLs expose the same URL internally for intra cluster communication.
            force-ssl-redirect: "false"
            &nbsp;            
            #  Disabling avoids double redirects, redirect loops, and unnecessary hops during health checks or internal service calls over HTTP. Services with external URLs expose the same URL internally for intra cluster communication.
            ssl-redirect: "false"
            &nbsp;
            # Supports larger-than-default request lines and headers (e.g., long cookies, SSO tokens, or complex auth headers) without immediate resort to the “large” buffers. Reduces 400 Bad Request (Request header too large) errors at modest memory cost.
            client-header-buffer-size: "32k"
            &nbsp;            
            # Accommodates bursts of large headers (multiple cookies, SAML/OIDC headers, complex reverse-proxy chains). Prevents header truncation and 494/400 errors under peak conditions.
            large-client-header-buffers: "4 32k"
            &nbsp;            
            # Handles large response headers (e.g., many Set-Cookie directives or big metadata) without spilling to disk or triggering buffer-related errors. Useful with SSO gateways or multi-cookie apps.
            proxy-buffer-size: "128k"
            &nbsp;            
            # Provides 1 MB of in-memory buffering per connection for smoother delivery of medium responses and to absorb backend send bursts. Reduces client-facing latency jitter and backend backpressure.
            proxy-buffers: "4 256k"
            &nbsp;            
            # Balances memory usage and throughput. Prevents excessive memory pressure while still allowing efficient streaming to slower clients.
            proxy-busy-buffers-size: "256k"
            &nbsp;
            # Supports larger uploads (files, form posts, GraphQL multipart, large JSON) without 413 Request Entity Too Large. Choose a value aligned with app limits and upstream timeouts; higher values increase memory/disk usage risk if many concurrent uploads.
            proxy-body-size: "100m"
            &nbsp;            
            # Necessary when TLS terminates upstream (LB/CDN) so apps see correct scheme (https), host, and client IP. Prevents generating incorrect redirects (http instead of https) and preserves accurate logs and security rules.
            use-forwarded-headers: "true"
            &nbsp;             
            # Matches the de-facto standard used by most LBs and CDNs. Ensures consistent client IP extraction across components.
            forwarded-for-header: "X-Forwarded-For"
            &nbsp;
            # Use only if your external load balancer is explicitly configured for PROXY protocol and your entire chain supports it. Keeping it false avoids handshake mismatches and connection failures. If you rely on HTTP headers instead, this should remain disabled.
            use-proxy-protocol: "false"
        </code-block>
    </tab>
    <tab title="Tools">
        <table>
            <tr>
                <td>Name</td>
                <td>Value(s)</td>
            </tr>
            <tr>
                <td><code>helm</code></td>
                <td>Helm CLI installed latest version</td>
            </tr>
            <tr>
                <td><code>kubectl</code></td>
                <td>Kubernetes CLI (kubectl) installed and configured</td>
            </tr>
            <tr>
                <td><code>openssl</code></td>
                <td>OpenSSL CLI for generating secret</td>
            </tr>
        </table>
    </tab>
    <tab title="Network">
        <table>
            <tr>
                <td>Attribute</td>
                <td>Value(s)</td>
            </tr>
            <tr>
                <td>DNS top-level domain</td>
                <td>Allocate a DNS zone for %premlite% so that it can identify assets on the network starting from the zone name. Example: <code>qodana.local</code></td>
            </tr>
            <tr>
                <td>Base URLs</td>
                <td>
                    <p>Qodana Self-Hosted is composed of several components. Almost each of these components requires a 
                        dedicated base URL. Example: given that the top-level domain is <code>qodana.local</code>:</p> 
                        <list>
                            <li>UI: <code>qodana.local</code></li>
                            <li>Backend: <code>api.qodana.local</code></li>
                            <li>Linters API: <code>lintersapi.qodana.local</code></li>
                            <li>Built-in file storage: <code>files.qodana.local</code></li>
                            <li>Built-in SSO provider: <code>login.qodana.local</code></li>
                            <li>Built-in ingress controller: <code>ingress.qodana.local</code></li>
                        </list>
                </td>
            </tr>
            <tr>
                <td>Docker registry</td>
                <td>The Helm Chart and Docker images are hosted at <code>https://jetbrains.team</code></td>
            </tr>
            <tr>
                <td>Other URLs</td>
                <td><p>JetBrains resources:</p> 
                    <list>
                        <li><code>analytics.services.jetbrains.com</code></li>
                        <li><code>vulnerability-search.jetbrains.com</code></li>
                        <li><code>resources.jetbrains.com</code></li>
                        <li><code>www.jetbrains.com</code></li>
                        <li><code>account.jetbrains.com</code></li>
                    </list>
                    <p>Third-party resources:</p>
                        <list>
                            <li><code>dl.min.io</code></li>
                        </list>
                </td>
            </tr>
        </table>
    </tab>
    <tab title="Other">
    <p>%premlite% supports S3 in AWS or Minio starting from version <code>RELEASE.2025-01-20T14-49-07Z</code> onwards.</p>
</tab>
</tabs>

### Docker version

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
                <td>20.10.23 or later with the Swarm mode available</td>
            </tr>
        </table>
    </tab>
    <tab title="Network">
        <p><code>qodana-installer-cli</code> references container images from the <code>quay.io</code> Docker registry. Make sure that 
            <code>quay.io</code> is a trusted address in the network. For offline deployment, mirror 
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


