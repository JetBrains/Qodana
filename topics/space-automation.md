[//]: # (title: Space Automation)

<var name="Space-cr-project" value="www.jetbrains.com/help/space/create-a-project.html"/>
<var name="Space-repo" value="www.jetbrains.com/help/space/repositories.html"/>
<var name="Space-config" value="www.jetbrains.com/help/space/automation-getting-started.html"/>
<var name="Space-secret" value="www.jetbrains.com/help/space/secrets-and-parameters.html#creating-secrets-and-parameters"/>
<var name="Space-starton" value="www.jetbrains.com/help/space/run-a-job-on-event-trigger.html#set-job-triggers"/>
<var name="Space-filter" value="www.jetbrains.com/help/space/run-a-job-on-event-trigger.html#filter-by-branch"/>

[Space Automation](https://www.jetbrains.com/help/space/automation-concepts.html) is a CI/CD tool that helps you automate 
development workflows in the JetBrains Space environment. This section explains how you can run %product% 
[Docker images](docker-images.md) within Space Automation jobs.

## Prepare your project

Assuming that your JetBrains Space account already has [a project](https://%Space-cr-project%) and 
[a repository](https://%Space-repo%), in the project root create the [`.space.kts`](https://%Space-config%) file. This 
file will contain configuration scripts written in [Kotlin](https://kotlinlang.org/) and mentioned in this section.

## Basic configuration

This is the basic configuration script for running %product% in JetBrains Automation. 

```kotlin
job("Qodana") {
   container("jetbrains/qodana-<linter>") {
      shellScript {
         content = """qodana"""
      }
   }
}
```

The [`container`](https://www.jetbrains.com/help/space/run-a-step-in-a-container.html) block specifies the invoked 
[Docker image](docker-images.md), and the `shellScript` block contains the script for running %product%.

Using the `shellScript` block, you can configure the [linter](docker-image-configuration.xml). 
For example, there can be the `--fail-threshold` and `--profile-name` options.

```kotlin
job("Qodana") {
   container("jetbrains/qodana-<linter>") {
      shellScript {
         content = """
                   qodana 
                   --fail-threshold <number> 
                   --profile-name <profile-name>
                   """.trimIndent()
      }
   }
}
```

## Inspect specific branches

The [`startOn`](https://%Space-starton%) block lets you specify the event that will trigger a job. This configuration 
uses the nested [`branchFilter`](https://%Space-filter%) block to override the default trigger and inspect the `feature` 
branch only.

```kotlin
job("Qodana") {
   startOn {
      gitPush {
         branchFilter {
            +"refs/heads/feature"
         }
      }
   }
   container("jetbrains/qodana-<linter>") {
      shellScript {
         content = """qodana"""
      }
   }
}

```

## Forward report to Qodana Cloud

Once you generated a [project token](cloud-projects.xml) in Qodana Cloud, in the **Settings** section of your JetBrains 
Space environment you can [create a secret](https://%Space-secret%). Save the copied project token as the value for this 
secret.

Here is the script that lets you forward inspection reports to Qodana Cloud. This script specifies the `QODANA_TOKEN` 
variable that refers to the `qodana-token` secret. 

```kotlin
job("Qodana") {
   container("jetbrains/qodana-<linter>") {
      env["QODANA_TOKEN"] = Secrets("qodana-token")
      shellScript {
         content = """qodana"""
      }
   }
}
```

To provide Qodana Cloud with additional data, such as the branch name or commit hash, you can add several variables to 
the configuration script.

```kotlin
job("Qodana") {
   container("jetbrains/qodana-<linter>") {
      env["QODANA_TOKEN"] = Secrets("qodana-token")
      shellScript {
         content = """
            QODANA_REPO_URL="${'$'}JB_SPACE_API_URL/p/${'$'}JB_SPACE_PROJECT_KEY/repositories/${'$'}JB_SPACE_GIT_REPOSITORY_NAME" \
            QODANA_REMOTE_URL="ssh://git@git.${'$'}JB_SPACE_API_URL/${'$'}JB_SPACE_PROJECT_KEY/${'$'}JB_SPACE_GIT_REPOSITORY_NAME.git" \
            QODANA_BRANCH=${'$'}JB_SPACE_GIT_BRANCH \
            QODANA_REVISION=${'$'}JB_SPACE_GIT_REVISION \
            qodana
         """.trimIndent()
      }
   }
}
```

<note>The <code>QODANA_BRANCH</code> and <code>QODANA_REVISION</code> variables are dependent on the 
<code>QODANA_REMOTE_URL</code> value, so presence of the <code>QODANA_REMOTE_URL</code> variable is required in this 
case. </note>

## Combined configuration

This configuration script combines everything mentioned in this section.

```kotlin
job("Qodana") {
   startOn {
      gitPush {
         branchFilter {
            +"refs/heads/feature"
         }
      }
   }
   container("jetbrains/qodana-<linter>") {
      env["QODANA_TOKEN"] = Secrets("qodana-token")
      shellScript {
         content = """
            QODANA_REPO_URL="${'$'}JB_SPACE_API_URL/p/${'$'}JB_SPACE_PROJECT_KEY/repositories/${'$'}JB_SPACE_GIT_REPOSITORY_NAME" \
            QODANA_REMOTE_URL="ssh://git@git.${'$'}JB_SPACE_API_URL/${'$'}JB_SPACE_PROJECT_KEY/${'$'}JB_SPACE_GIT_REPOSITORY_NAME.git" \
            QODANA_BRANCH=${'$'}JB_SPACE_GIT_BRANCH \
            QODANA_REVISION=${'$'}JB_SPACE_GIT_REVISION \
            qodana
         """.trimIndent()
      }
   }
}
```