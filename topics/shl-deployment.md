# Kubernetes configuration

<show-structure for="chapter" depth="3"/>

In the Kubernetes version of %premlite%, the deployment is configurable via the `values.yaml` file, which lets you 
customize endpoints, resources, secrets, integrations, and security policies.

Once installed, Helm Chart reads the contents of the `values.yaml` file.

The actual version of the %product% Helm Chart is 1.0.3. Run the following command to pull the actual version of the product:

```bash
helm pull oci://registry.jetbrains.team/p/helm/alpha/qodana --version 1.0.3 
```

## Set up a new domain

This guide explains how you can configure %premlite% URLs when switching from `qodana.local` to a new domain. 
This involves updating the ingress and service URLs to reflect the new domain.

### Prerequisites

Before you start, make sure that the following requirements are met:

* The new domain is registered and DNS records for %premlite% are configured to point to your Kubernetes ingress controller. 
For example, it can be `externalurls.local`. 
The DNS records that point (CNAME) to the DNS record of your ingress controller are the following: 
    * `externalurls.local` 
    * `api.externalurls.local` 
    * `lintersapi.externalurls.local` 
    * `files.externalurls.local`
    * `login.externalurls.local`

* The API, UI, Linters API, Object Storage, and Identity Provider Helm Chart services must be updated for a new domain.
* Internal URL of your Ingress Controller Load Balancer. Example: `ingress-nginx-controller.kube-ingress.svc.cluster.local`.
* Access to a Kubernetes cluster:
  * Kubernetes CLI (`kubectl`) and Helm are installed and configured
  * Sufficient permissions to modify the namespace where %product% is deployed

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

### Full configuration example

Here is an example that contains these modifications:

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


## Example settings and commands

The `values.yaml` provides configurable settings. For example, you can configure the organization name:

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

Generate a new configuration file:

```bash
helm template --namespace kube-public oci://registry.jetbrains.team/p/helm/alpha/qodana \
  --version 1.0.3 \
  --set global.license='<YOUR_LICENSE_KEY>' > installation.bundle.yaml"
```

Override the existing settings, for example:

```Bash
helm template --namespace kube-public oci://registry.jetbrains.team/p/helm/alpha/qodana \
  --version 1.0.3 \
  --set global.license='<YOUR_LICENSE_KEY>'
  –-set api.resources.limits.memory=2048Mi"
```




