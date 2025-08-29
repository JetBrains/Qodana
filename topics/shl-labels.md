# Labels

This section describes labels that you can use to better explore and monitor %premlite% resources.
Information about Docker labels is available on the [Docker](https://docs.docker.com/engine/manage-resources/labels/) 
website. 

## Global labels

%premlite% uses several global labels to mark the resources it owns and manages. You can use these labels to operate 
%premlite%:

| Label and value                                                                  | Description                                                                                                                                 |
|----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| `qodana.jetbrains.self-hosted.lite.select=true`                                  | Identify all resources that are part of the %premlite% installation                                                                         |
| `qodana.jetbrains.self-hosted.lite.version=${APP_QODANA_SELF_HOSTED_IMAGE_TAG}`  | Display at runtime a %premlite% version that a specific resouce is related to. Dependent on the `APP_QODANA_SELF_HOSTED_IMAGE_TAG` variable |


## Component-specific labels

%premlite% is operated by several services. To simplify administration, they are combined into the following groups:

| Group name           | Description                                                |
|----------------------|------------------------------------------------------------|
| `local-dependencies` | Stateful components                                        |
| `application`        | %product% API, %product% Git API, linter API and others    |
| `supporting-tools`   | Ingress and garbage collection of Docker images and others |

Here, each group identifies a specific Docker Swarm stack.

### Labels related to local dependencies

The `qodana.jetbrains.self-hosted.lite.dependencies.local=true` and `qodana.jetbrains.self-hosted.lite.service-type=local-dependencies` 
labels identify resources related to the `qodana_self_hosted_local_dependencies` stack or group.

The `qodana.jetbrains.self-hosted.lite.database.volume.name` label defines the internal name of a volume that will be 
mapped to a related stateful service that is part of a certain Docker stack.

You can find out the volume name for a given container using this Docker CLI command:

```Bash
docker inspect <containerid> \
  --format "{{ range .HostConfig.Mounts }}{{ json .VolumeOptions.Labels }}{{end}}"
```
{prompt="$"}

To understand the mount point of a specific Docker volume, you can use the 
`qodana.jetbrains.self-hosted.lite.database.volume.path` label.

### Label related to %premlite%

The `qodana.jetbrains.self-hosted.lite.service-type=application` label identifies the resources related to the 
`qodana_self_hosted_local_service_tools` stack.

<!-- What are the supporting tools here ? -->

### Label related to supporting tools

The `qodana.jetbrains.self-hosted.lite.service-type=supporting-tools` label identifies the resources related to the
`qodana_self_hosted_local_service_tools` stack.





