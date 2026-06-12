# Overview of self-hosting

%premlite% is a lightweight on-premises version of [%cloud%](cloud-use-cases.topic) designed for small development teams.

Using %premlite%, you can run %product% within your infrastructure ensuring that sensitive code and data remain secure and 
private, which is particularly useful for organizations that need powerful static analysis tools but must operate
within strict security or compliance standards. 

> %premlite% is still in the alpha development stage, which means that it may contain bugs or work not as intended.
{style="warning"}

Visit the [Subscription Options and Pricing](https://www.jetbrains.com/qodana/buy/?billing=yearly) page to learn more about available
subscription options for %premlite%. You can also [request a demo](https://www.jetbrains.com/qodana/request-a-demo/).

This documentation guides you through deployment, product configuration, and initialization stages of the dockerized
and cluster versions of %premlite%.

## %premlite% features

Data privacy lets you store sensitive code within your organization's infrastructure.
Scalability lets you scale %premlite% to meet the needs of larger teams or organizations with extensive codebases.
Customizability lets you configure %product% to match their specific code quality requirements.
%premlite% lets you use local hosting on your infrastructure to ensure code and data privacy. 

> For the Docker version, %premlite% supports a single server deployment meaning that a Docker Swarm cluster should have one node.
{style="note"}

## Deployment options

You can deploy %premlite% using two options:

* The Kubernetes version of %premlite% is a Helm-based deployment for Kubernetes that sets up all the necessary Qodana
  services and their dependencies as Kubernetes resources. It uses Helm to distribute the product as a Helm Chart.
  You can customize it through an ad-hoc `values.yaml` file. By default, the package is configured to run in demo/PoC mode.
* The Dockerized version is the alternative that uses the `qodana-installer-cli` command-line utility to offer you a one-line 
installer. The utility requires a server running Linux with the Docker Engine and Docker Swarm as a container orchestrator. 
It is compatible with automation and Infrastructure as a Code (IaC) frameworks.

<!-- The word deployment needs to be linked to the K8s documentation -->

<!--The values.yaml file can be probably deleted from here because it's irrelevant here  -->

