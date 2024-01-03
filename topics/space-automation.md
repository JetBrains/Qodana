[//]: # (title: Space Automation)

<var name="Space-cr-project" value="https://www.jetbrains.com/help/space/create-a-project.html"/>
<var name="Space-repo" value="https://www.jetbrains.com/help/space/repositories.html"/>
<var name="Space-config" value="https://www.jetbrains.com/help/space/automation-getting-started.html"/>
<var name="Space-secret" value="https://www.jetbrains.com/help/space/secrets-and-parameters.html#creating-secrets-and-parameters"/>
<var name="Space-starton" value="https://www.jetbrains.com/help/space/run-a-job-on-event-trigger.html#set-job-triggers"/>
<var name="Space-filter" value="https://www.jetbrains.com/help/space/run-a-job-on-event-trigger.html#filter-by-branch"/>
<var name="Space-creview" value="https://www.jetbrains.com/help/space/automation-dsl.html#codereviewopened"/>

[Space Automation](https://www.jetbrains.com/help/space/automation-concepts.html) is a CI/CD tool that helps you automate 
development workflows in the JetBrains Space environment. This section explains how you can configure and run %product% 
[Docker images](docker-images.md) within Space Automation jobs.

## Prepare your project

Assuming that your JetBrains Space account already has [a project](%Space-cr-project%) and 
[a repository](%Space-repo%), in the project root create the [`.space.kts`](%Space-config%) file. This 
file will contain configuration scripts written in [Kotlin](https://kotlinlang.org/) and mentioned in this section.

## Basic configuration

This is the basic configuration script for running %product% in JetBrains Automation jobs. 

```kotlin
job("Qodana") {
    container("jetbrains/qodana-<linter>") {
        env["QODANA_TOKEN"] = Secrets("qodana-token")
        shellScript {
            content = """
               qodana
               """.trimIndent()
        }
    }
}
```

The [`container`](https://www.jetbrains.com/help/space/run-a-step-in-a-container.html) block specifies which 
[Docker image](docker-images.md) of %product% to run.  

The `QODANA_TOKEN` variable refers to the [project token](project-token.md) generated in Qodana Cloud and contained in 
the `qodana-token` secret. This token is required by the paid %product% [linters](pricing.md#pricing-linters-licenses), 
and is optional for using with the Community linters. You can see these sections to learn how to generate the project token:

* The [](cloud-onboarding.md) section explains how to get the project token generated while first working with Qodana Cloud
* The [](cloud-projects.topic#cloud-manage-projects) section explains how to create a project in the existing Qodana Cloud organization

Once the project token is generated, in the **Settings** section of your JetBrains Space environment 
[create a secret](%Space-secret%) with the `qodana-token` name. Save the project token as the value for this secret.

The `shellScript` block contains the `qodana` command for running %product%, and it can also contain the 
[options](docker-image-configuration.topic) that can be used during the run like [quality gate](quality-gate.topic) or 
[baseline](baseline.topic).

## Inspect specific branches

The [`startOn`](%Space-starton%) block lets you specify the event that will trigger a job. This configuration 
uses the nested [`branchFilter`](%Space-filter%) block to override the default trigger and run the job only
after changes made in the `feature` branch. 

The [`codeReviewOpened`](%Space-creview%) trigger lets you inspect code reviews opened in the default branch of 
the project.

```kotlin
job("Qodana") {
   startOn {
      gitPush {
         branchFilter {
            +"refs/heads/feature"
         }
      }
      codeReviewOpened{}
   }
   container("jetbrains/qodana-<linter>") {
       env["QODANA_TOKEN"] = Secrets("qodana-token")
       shellScript {
           content = """
               qodana
               """.trimIndent()
      }
   }
}
```

## Quality gate and baseline

You can use the `--fail-threshold <number>` and `--baseline <path/to/qodana.sarif.json>` lines in the `shellScript` 
block to invoke the [quality gate](quality-gate.topic) and [baseline](baseline.topic) features.

```kotlin
job("Qodana") {
    container("jetbrains/qodana-<linter>") {
        env["QODANA_TOKEN"] = Secrets("qodana-token")
        shellScript {
            content = """
               qodana \
               --fail-threshold <number> \ 
               --baseline <path/to/qodana.sarif.json>
               """.trimIndent()
        }
    }
}
```
