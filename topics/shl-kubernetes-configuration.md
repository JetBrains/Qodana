# Kubernetes configuration

<show-structure for="chapter" depth="3"/>

## Prepare your project

The Kubernetes version of %premlite% is deployed on a [Kubernetes cluster](https://kubernetes.io/docs/concepts/overview/components/).

<!-- The storage should be mentioned here as well -->

### Kubernetes cluster

All requirements to a cluster are described in the [](shl-requirements.md#Kubernetes+version) chapter. For resilience, 
we recommend deploying your cluster on at least three nodes.

Make sure that all nodes of your cluster have unique hostnames.

Below are the links to the Kubernetes documentation that you can use to deploy a cluster:

* [Cluster concepts](https://kubernetes.io/docs/setup/production-environment/)
* [Node components](https://kubernetes.io/docs/concepts/architecture/#node-components)

This is the minimum list of tools that should be deployed and configured on your cluster: 

| Tool                                                                                                                     | Description                                                  | Control plane nodes | Worker nodes |
|--------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|---------------------|--------------|
| [Container runtime](https://kubernetes.io/docs/setup/production-environment/container-runtimes/)                         | Run pods of your cluster                                     | Required            | Required     |
| [kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/)                                    | Delegate tasks to the container runtime                      | Required            | Required     |
| [kubectl](https://kubernetes.io/docs/reference/kubectl/)                                                                 | Interact with the cluster API using a command line interface | Required            | Not required |
| [kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/) or other similar tools | Bootstrap and manage Kubernetes clusters                     | Required            | Not required |
| CNI or container network interface plugin ([flannel](https://github.com/flannel-io/flannel) or other) \*                 | Assign IP addresses to pods                                  | Required            | Required     |

\* You need to select a Pod Network CIDR that does not overlap with your host network. For example, for 
[flannel](https://github.com/flannel-io/flannel) this can be `10.244.0.0/16`.

After deployment, make sure that all these components are running and healthy.

### Helm Chart

In the Kubernetes version of %premlite%, the deployment is configurable via a [Helm](https://helm.sh/) Chart deployed on 
an up-and-running Kubernetes cluster. To install Helm on your control plane node, run the following command: 

```bash
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```
{prompt="$"}

Once installed, Helm needs a Chart contained in the `values.yaml` file.
This file lets you customize endpoints, resources, secrets, integrations, and security policies.

The actual version of the %product% Helm Chart is 1.0.3. Run the following command to pull the actual version of the product:

```bash
helm pull oci://registry.jetbrains.team/p/helm/alpha/qodana --version 1.0.3 
```
{prompt="$"}

Navigate to the directory where the `values.yaml` file is located and run the following command to install the product, for example:

```bash
helm install --generate-name -f values.yaml ./qodana
```
{prompt="$"}

After deploying a cluster, run the `kubectl get svc` command to see the list of services deployed.

### Ingress controller

You can use any ingress controller to expose %premlite% to the internet. Examples include: NGINX, Traefik, 
Kong, AWS ALB, GKE, etc. For each type of ingress controller, you have to configure the following aspects: 

* Redirect behavior
* Client identity propagation
* Size/buffering limits

Also, decide where TLS terminates and what performs HTTP to HTTPS redirects; if your edge LB/CDN already enforces HTTPS, 
then disable redirects at the ingress to avoid loops and double hops. 

Besides that, ensure that your applications see the real client IP, scheme, and host: 
choose the appropriate mechanism your controller supports (X-Forwarded-* headers, Forwarded header, or 
PROXY protocol) and restrict trust to known upstream CIDRs so users can’t spoof IPs. 

Finally, right-size limits for request headers, request bodies, and response buffering to match your workloads like SSO 
cookies, many Set-Cookie headers, file uploads, and streaming. 

Each controller exposes different knobs and names for these concepts, but they map to the same 
concerns: header buffer sizes, large-header buffers, max body size, proxy buffer sizes, forwarded header handling, 
and optional proxy protocol. Review your controller’s documentation for the exact settings, mirror the intent of the 
examples shown for NGINX, and validate under load tests to confirm no `400/413` responses, no misreported client IPs, 
and consistent redirect behavior.

Here is an example of the NGINX configuration: 

```yaml
#  Disabling avoids double redirects, redirect loops, and unnecessary hops during health checks or internal service calls over HTTP. Services with external URLs expose the same URL internally for intra cluster communication.
force-ssl-redirect: "false"

#  Disabling avoids double redirects, redirect loops, and unnecessary hops during health checks or internal service calls over HTTP. Services with external URLs expose the same URL internally for intra cluster communication. 
ssl-redirect: "false" 

# Supports larger-than-default request lines and headers (e.g., long cookies, SSO tokens, or complex auth headers) without immediate resort to the “large” buffers. Reduces 400 Bad Request (Request header too large) errors at modest memory cost.
client-header-buffer-size: "32k"

# Accommodates bursts of large headers (multiple cookies, SAML/OIDC headers, complex reverse-proxy chains). Prevents header truncation and 494/400 errors under peak conditions. 
large-client-header-buffers: "4 32k"

# Handles large response headers (e.g., many Set-Cookie directives or big metadata) without spilling to disk or triggering buffer-related errors. Useful with SSO gateways or multi-cookie apps.
proxy-buffer-size: "128k"

# Provides 1 MB of in-memory buffering per connection for smoother delivery of medium responses and to absorb backend send bursts. Reduces client-facing latency jitter and backend backpressure. 
proxy-buffers: "4 256k" 

# Balances memory usage and throughput. Prevents excessive memory pressure while still allowing efficient streaming to slower clients.
proxy-busy-buffers-size: "256k" 

# Supports larger uploads (files, form posts, GraphQL multipart, large JSON) without 413 Request Entity Too Large. Choose a value aligned with app limits and upstream timeouts; higher values increase memory/disk usage risk if many concurrent uploads.
proxy-body-size: "100m" 

# Necessary when TLS terminates upstream (LB/CDN) so apps see correct scheme (https), host, and client IP. Prevents generating incorrect redirects (http instead of https) and preserves accurate logs and security rules.
use-forwarded-headers: "true" 

# Matches the de-facto standard used by most LBs and CDNs. Ensures consistent client IP extraction across components.
forwarded-for-header: "X-Forwarded-For" 

# Use only if your external load balancer is explicitly configured for PROXY protocol and your entire chain supports it. Keeping it false avoids handshake mismatches and connection failures. If you rely on HTTP headers instead, this should remain disabled.
use-proxy-protocol: "false"
```
{collapsible="true"}

## Configure your project

All configuration snippets here are provided for the `values.yaml` file.

### Prerequisites

This guide explains how to configure %premlite% URLs when switching from `qodana.local` to a new domain.

Before you start, make sure that the following requirements are met:

* The new domain is registered, and DNS records for %premlite% are configured to point to your Kubernetes ingress controller.
  For example, it can be `externalurls.local`.
  The DNS records that point (CNAME) to the DNS record of your ingress controller are the following:
    * `externalurls.local`
    * `api.externalurls.local`
    * `lintersapi.externalurls.local`
    * `files.externalurls.local`
    * `login.externalurls.local`

* The API, UI, Linters API, Object Storage, and Identity Provider Helm Chart services must be updated for a new domain.
* Internal URL of your Ingress Controller Load Balancer. Example: `ingress-nginx-controller.kube-ingress.svc.cluster.local`.
* Sufficient permissions are provided to modify the namespace where %product% is deployed.

### Update URLs

Update URLs for the following services:

<tabs>
    <tab title="API service">
    <code-block lang="yaml">
        global:
          services:
            api: 
              url:
               host: &api_hostname "api.externalurls.local" 
    </code-block>
    </tab>
    <tab title="UI service">
    <code-block lang="yaml">
        global:
          services:
            ui: 
              url:
               host: &ui_hostname “externalurls.local" 
    </code-block>
    </tab>
    <tab title="LInter API service">
    <code-block lang="yaml">
        global:
          services:
            linters: 
              url:
               host: &linters_hostname “lintersapi.externalurls.local" 
    </code-block>
    </tab>
    <tab title="Object storage service">
    <code-block lang="yaml">
        global:
          dependencies:
            buckets: 
               host: &file_server_hostname “files.externalurls.local" 
    </code-block>
    </tab>
    <tab title="Identity provider service">
    <code-block lang="yaml">
        global:
          dependencies:
            oidc: 
               host: &identity_server “login.externalurls.local" 
    </code-block>
    </tab>
</tabs>

### Update ingress hostnames

Ensure that ingress hostnames match the updated URLs by using YAML pointers (`*`) for consistency.
Modify the following sections:

<tabs>
    <tab title="API Ingress">
    <code-block lang="yaml">
        api:
          ingress:
            hostname: *api_hostname
    </code-block>
    </tab>
    <tab title="UI Ingress">
    <code-block lang="yaml">
        ui:
          ingress:
            hostname: *ui_hostname
    </code-block>
    </tab>
    <tab title="Linters Ingress">
    <code-block lang="yaml">
        linters:
          ingress:
            hostname: *linters_hostname
    </code-block>
    </tab>
    <tab title="Object storage ingress">
    <code-block lang="yaml">
        dependencies:
          file-server:
            ingress:
               hostname: *file_server_hostname
    </code-block>
    </tab>
    <tab title="Identity provider ingress">
    <code-block lang="yaml">
        identity-server:
            extraEnvVars:
              - name: KC_HOSTNAME
                value: *identity_server
            ingress:
              extraHosts:
                - name: *identity_server
    </code-block>
    </tab>
</tabs>

### Update organization name and memory settings

Update the organization name as follows:

```yaml
global:
  organizationName: "StaticAnalysisHeroes"
```

Memory settings for the API service can be configured as follows:

```yaml
api: 
  resources: 
       requests: 
           memory: 2048Mi 
       limits: 
           memory: 2048Mi
```

### Configuration example

Here is an example of the `values.yaml` file containing these modifications:

```yaml
global:
  organizationName: "ExternalURLS"
  license: "gAv9P3X3Se+xIVtJzQsk8QrB/w52IB3FKiAKl/a"
  services:
    api:
      url:
        host: &api_hostname "api.externalurls.local"
    ui:
      url:
        host: &ui_hostname "externalurls.local"
    linters:
      url:
        host: &linters_hostname "linters.externalurls.local"
  dependencies:
    kubernetesIngress:
      internalFQDN: "ingress-nginx-controller.kube-ingress.svc.cluster.local"
    buckets:
      host: &file_server_hostname "fileserver.externalurls.local"
    oidc:
      host: &identity_server "identity.externalurls.local"

api:
  resources:
    requests:
      memory: 2048Mi
    limits:
      memory: 2048Mi
  ingress:
    hostname: *api_hostname

ui:
  ingress:
    hostname: *ui_hostname

linters:
  ingress:
    hostname: *linters_hostname

dependencies:
  file-server:
    ingress:
      hostname: *file_server_hostname
  identity-server:
    extraEnvVars:
      - name: KC_HOSTNAME
        value: *identity_server
    ingress:
      extraHosts:
        - name: *identity_server
```
{collapsible="true"}

### Configure via CLI

<!-- Helm commands from a text file should be moved here as well -->

You can override the existing %premlite% Helm Chart settings, here is an example of a memory limit override:

```Bash
helm template --namespace kube-public oci://registry.jetbrains.team/p/helm/alpha/qodana \
  --version 1.0.3 \
  --set global.license='<YOUR_LICENSE_KEY>' \
  –-set api.resources.limits.memory=2048Mi" > installation.bundle.yaml
```
{prompt="$"}

Apply the generated manifests to your cluster using `kubectl`:

```bash
kubectl apply -f installation.bundle.yaml
```
{prompt="$"}

