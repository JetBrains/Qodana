# Deployment

Assuming that requirements from the [](shl-introduction.md) and [](shl-prepare-project.md) sections are satisfied, pull the 
`quay.io/jetbrains/qodana-installer-cli:latest` Docker image. All commands running this image require the 
`/var/run/docker.sock` Docker socket file for communicating with the Docker engine and Docker Swarm.

> The command list is available in the [](shl-command-list.md) section.

## Basic use case

Follow the steps below for installing %premlite% on your machine:

<procedure>
    <step>
        <p>On your local Linux machine, configure the <code>/etc/hosts</code> file as shown below:</p>
        <code-block lang="text">
            # Added for Qodana Self-Hosted Lite Version
            127.0.0.1 qodana.local
            127.0.0.1 files.qodana.local
            127.0.0.1 api.qodana.local
            127.0.0.1 ingress.qodana.local
            127.0.0.1 login.qodana.local
            127.0.0.1 lintersapi.qodana.local
        </code-block>
    </step>
    <step>
        <p>On your local machine, run the following Docker command:</p>
        <code-block lang="Bash" prompt="$">
            docker run \
                -v /var/run/docker.sock:/var/run/docker.sock \
                -e API_ORGANIZATION_NAME="&lt;Specify the name of your organization&gt;" \
                -e COMMON_LICENSE_KEY_SECRET="&lt;Specify a valid license key&gt;" \ 
                quay.io/jetbrains/qodana-installer-cli:latest \
                install-app
        </code-block>
    </step>
</procedure>

In your browser, navigate to `http://qodana.local` to receive access to %premlite%.

By default, %premlite% comes configured with local dependencies for quick Proofs Of Concepts (PoCs) or Proofs of Value (PoV). 
The credentials for a built-in administrator test user are as follows:

|Credential | Value               |
|-----------|---------------------|
|Username | `tser@qodana.local` |
|Password | `@wesomeQodana`     |

You can update these credentials by navigating to the `http://login.qodana.local` page.

## Use configuration from file

Run the following Docker command to use a configuration contained in a file:

```Bash
docker run 
    -v /var/run/docker.sock:/var/run/docker.sock \ 
    -e API_ORGANIZATION_NAME="<Specify the name of your organization>" \
    -e COMMON_LICENSE_KEY_SECRET="<Specify a valid license key>" \ 
    --env-file qodana-self-hosted.env \
    quay.io/jetbrains/qodana-installer-cli:latest 
    install-app
```
{prompt="$"}

This command uses the `--env-file` option to specify the path to the configuration file, in this case this is the
`qodana-self-hosted.env` file.

## Persist secrets

This command lets you export and persist secrets created during installation in the `${PWD}/secrets` directory:

```Bash
docker run \
    -v /var/run/docker.sock:/var/run/docker.sock \ 
    -v ${PWD}/secrets:/app/qodana-installer/secrets \
    -e API_ORGANIZATION_NAME="<Specify the name of your organization>" \
    -e COMMON_LICENSE_KEY_SECRET="<Specify a valid license key>" \ 
    quay.io/jetbrains/qodana-installer-cli:latest \
    install-app
```
{prompt="$"}

To make the secret idempotent, this command mounts the `/app/qodana-installer/secrets` directory for storing secrets.
