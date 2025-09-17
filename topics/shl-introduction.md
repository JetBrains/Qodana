# Introduction

%premlite% is a lightweight on-premises version of [%cloud%](cloud-use-cases.topic) designed for small development teams.

Using %premlite%, you can run %product% within your infrastructure ensuring that sensitive code and data remain secure and 
private, which is particularly useful for organizations that need powerful static analysis tools but must operate
within strict security or compliance standards. 

> %premlite% is still in the alpha development stage, which means that it may contain bugs or work not as intended.
{style="warning"}

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
