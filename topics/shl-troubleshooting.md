# Troubleshooting (Docker)

To troubleshoot the issues that may arise during deployment, configuration or operation
of %premlite%, use the following command to extract log entries:

```bash
docker run -v /var/run/docker.sock:/var/run/docker.sock \ quay.io/jetbrains/qodana-installer-cli:latest logs > all.troubleshooting.logs
```
{prompt="$"}

Study log entries and also try to:

* Look for the message related to a specific issue
* Review the possible causes of the issue
* Find the trace and debug the issue

If you cannot debug the issue or if the issue persists, navigate to the [JetBrains website](https://qodana-support.jetbrains.com/hc/en-us) and 
create a request containing the following information:

| Information item | Description                                                                                                                |
|------------------|----------------------------------------------------------------------------------------------------------------------------|
| Summary          | Short and self-contained description of the issue                                                                          |
| Description      | Additional information to outline the issue better                                                                         |
| Attachments      | Any log files and screenshots, if available                                                                                |
| Tags             | Specify the version                                                                                                        |
| Type             | Try to categorize the title and the description of your case. This will be refined after the maintainers analyze the issue |
| Priority         | Set the priority to the issue. Apply common sense for the definition of the urgency level                                  |
