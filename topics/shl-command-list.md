# Docker commands

This section lists %premlite% commands executed in the `quay.io/jetbrains/qodana-installer-cli:latest` Docker image.

<!-- Do we really need to mention qodana-installer-cli name here? -->

## help

Help for the `qodana-installer-cli` tool:

```Bash
docker run \
  -v /var/run/docker.sock:/var/run/docker.sock \ 
  quay.io/jetbrains/qodana-installer-cli:latest \
  help
```
{prompt="$"}

## environment

Display all active configurations passed or used by the `qodana-installer-cli` tool: 

```Bash
docker run \
  -v /var/run/docker.sock:/var/run/docker.sock \ 
  quay.io/jetbrains/qodana-installer-cli:latest \
  environment
```
{prompt="$"}

## install-app

> Detailed deployment guide is available in the [](shl-deployment.md) section.

Deploy %premlite% on your machine:

```Bash
docker run \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -e API_ORGANIZATION_NAME="<Specify the name of your organization>" \
  -e COMMON_LICENSE_KEY_SECRET="<Specify a valid license key>" \ 
  quay.io/jetbrains/qodana-installer-cli:latest \
  install-app
```
{prompt="$"}

## uninstall

Uninstall %premlite% from your machine:

```Bash
docker run \
  -v /var/run/docker.sock:/var/run/docker.sock \ 
  quay.io/jetbrains/qodana-installer-cli:latest \
  uninstall
```
{prompt="$"}

To remove Docker volumes of %premlite%, run the following command:

```Bash
echo "[INFO] Cleaning the Docker volumes" && docker volume ls \
  --filter "label=qodana.jetbrains.self-hosted.lite.dependencies.local=true" \
  --quiet | xargs -r docker volume rm
```
{prompt="$"}

To delete persisting secrets from your machine located in the `${PWD}/secrets` directory, run this command:

```Bash
echo "[INFO] Cleaning the local secrets directory" && rm -rf ${PWD}/secrets
```
{prompt="$"}

## logs

Print logs related to %premlite% to the standard output:

```Bash
docker run \
  -v /var/run/docker.sock:/var/run/docker.sock \ 
  quay.io/jetbrains/qodana-installer-cli:latest 
  logs
```
{prompt="$"}

You can filter log output using the `--filters ` parameter and labels described in the [](shl-labels.md) section and 
separated by a space character, for example:

```Bash
docker run \ 
  -v /var/run/docker.sock:/var/run/docker.sock \ 
  quay.io/jetbrains/qodana-installer-cli:latest \ 
  logs \
  --filters "label=com.docker.stack.namespace=qodana_self_hosted_services label=qodana.jetbrains.self-hosted.lite.service-type=application"
```
{prompt="$"}



