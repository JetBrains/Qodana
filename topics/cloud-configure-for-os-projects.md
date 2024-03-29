[//]: # (title: Inspect open-source projects)

<var name="cloud" value="Qodana Cloud"/>
<var name="feature" value="License audit"/>
<var name="github-secret" value="https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository"/>
<var name="branch-protection-rule" value="https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/managing-a-branch-protection-rule"/>
<!-- I need to mention here more about OS projects -->

This section explains how you can inspect your open-source projects using %instance%, and how you can use %cloud% to 
view %instance% inspection results in a convenient form and free for open-source projects. 

## Before you start 

<link-summary>Learn more about the preparation steps before you inspect your open-source project by %product%.</link-summary>

Depending on your needs, it may be useful to know how to:

* [Inspect your code](inspect-your-code.topic) using %instance%
* Configure %instance% using [`qodana.yaml`](qodana-yaml.md) and [](docker-image-configuration.topic)
* Run %instance% either [locally](Quick-start.topic) on in your [CI/CD pipelines](ci.md)
* [Forward reports](cloud-forward-reports.topic) to %cloud%

## Prepare %cloud%

<link-summary>Learn how to prepare Qodana Cloud before inspecting your open-source project using %product%.</link-summary>

If you plan to create a separate team and project in your Qodana Cloud account, follow the steps below.

<procedure>
<step>
In the %cloud% UI, navigate to your organization.

<img src="qc-settings-organization-navigate-between.png" dark-src="qc-settings-organization-navigate-between_dark.png" width="706" alt="Creating an organization" border-effect="line" animated="true"/>
</step>
<step>
In your organization, create a <a href="cloud-teams.topic">team</a>.
</step>
<step>
In your team, create a <a href="cloud-projects.topic">project</a>. 
</step>
<step>
In the project, click <ui-path>Generate token</ui-path> to generate a project token.

<img src="qc-generate-token.png" dark-src="qc-generate-token_dark.png" alt="Generate the project token" width="706" border-effect="line"/>
</step>
</procedure>

<tip>To learn more about using project tokens, see the <a href="cloud-forward-reports.topic"/> section.</tip>

## Inspect your projects

<link-summary>Depending on the %instance% license, you can configure various features.</link-summary>

You can inspect your codebase using methods described in the [](inspect-your-code.topic) section. 

Depending on the %instance% [license](pricing.md#pricing-linters-licenses), you can configure various features, for example:

* [Baseline](#Configure+baseline) for monitoring current and new problems
* [Inspections](#Configure+inspections) that you would like to use
* [License audit](#configure-license-audit) for checking license compatibility
* [Quality gate](#configure-quality-gate) for restricting the number of problems

Here are the links to the sections that describe other available features: 

* [](code-coverage.md)
* [](php-language-upgrade.topic)
* [](quick-fix.md)
* [](taint-analysis.md)
* [](vulnerability-checker.md)

### Configure inspections

<link-summary>By default, %instance% inspects your code using the `qodana.starter` profile. You can use additional 
inspections by specifying the `qodana.recommended` profile.</link-summary>

By default, %instance% inspects your code using the `qodana.starter` profile. You can use additional inspections by 
specifying the `qodana.recommended` profile in the [`qodana.yaml`](qodana-yaml.md) file contained in your project root: 

```yaml
profile:
    name: qodana.recommended  
```

To check the overall configuration of your project, you can employ the `qodana.sanity` profile:

```yaml
profile:
    name: qodana.sanity  
```

### Configure license audit
{id="configure-license-audit"}

<link-summary>A license audit lets you track compatibility of dependency licenses with your open-source project license.</link-summary>

[License audit](license-audit.topic) lets you track compatibility of dependency licenses with your project license.

To enable the license audit, use the `include` option of the [`qodana.yaml`](qodana-yaml.md) file in your project root:

```yaml
include:
  - name: CheckDependencyLicenses
```

### Configure baseline

<link-summary>A baseline lets you create a snapshot of your project that will be used as a basis for subsequent 
analysis.</link-summary>

[Baseline](baseline.topic) lets you create a snapshot of your project that will be used as a basis for 
subsequent analysis. To enable it, select inspections and download the `qodana.sarif.json` file. 

You can run %instance% with the baseline enabled using the `--baseline` option:

```shell
--baseline <path-to-qodana.sarif.json>
```

### Configure the quality gate
{id="configure-quality-gate"}

<link-summary>A quality gate lets you configure the ultimate number of problems that will cause a CI/CD pipeline failure.</link-summary>

[](quality-gate.topic) lets you configure the ultimate number of problems that will cause a CI/CD pipeline failure.

Once configured, a quality gate will make your CI/CD system:

* Build the project only if the number of problems contained in it is below the configured threshold
* Accept only the pull requests containing problems below the configured threshold  

To enable the quality gate, you can use the `fail-threshold <number>` option.

### Types of Qodana reports

<link-summary>%instance% can generate several types of inspection reports.</link-summary>

%instance% can generate the following types of inspection reports: 

* Reports containing inspection results over a specific branch of your project
* Pull or merge request inspection reports generated by [GitHub Actions](#GitHub+Actions) and [GitLab CI/CD](#GitLab+CI%2FCD)

#### GitHub Actions

<link-summary>You can configure GitHub for forwarding inspection results to %cloud% and block the merge of pull
requests if a quality gate has failed.</link-summary>

Using this example, you can configure GitHub for:

* Forwarding inspection results to %cloud%
* Blocking the merge of pull requests if a quality gate has failed

Follow these steps:

1. Create an [encrypted secret](%github-secret%) with the `QODANA_TOKEN` name.
2. Create a new or open an existing GitHub workflow that invokes the Qodana Scan action.
3. Set the workflow to run on `pull_request` events that target the `main` branch, and forward reports to Qodana Cloud 
based on the `QODANA_TOKEN` value. Instead of `main`, you can specify your branch here.

```yaml
name: Qodana
on:
  workflow_dispatch:
  pull_request:
    branches:
      - main
  push:
    branches:
      - main
      - 'releases/*'

jobs:
  qodana:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
      - name: 'Qodana Scan'
        uses: JetBrains/qodana-action@v2022.2.3
        env:
          QODANA_TOKEN: ${{ secrets.QODANA_TOKEN }}
```

4. Set the number of problems (integer) for the Qodana action [`fail-threshold`](#configure-quality-gate) option.
5. Under your repository name, click **Settings**.
6. On the left menu, click **Branches**.
7. In the branch protection rules section, click **Add rule**.
8. Add `main` to **Branch name pattern**.
9. Select **Require status checks to pass before merging**.
10. Search for the `Qodana` status check, then check it.
11. Click **Create**.

#### GitLab CI/CD

<link-summary>You can configure GitLab CI/CD for inspecting a specific branch and all merge requests, block merge requests
if a quality gate has failed, and forward inspection results to Qodana Cloud.</link-summary>

Using this example, you can configure GitLab CI/CD for:

* Inspecting the `main` branch and all merge requests
* Blocking merge requests if a quality gate has failed
* Forwarding inspection results to %cloud%

Follow these steps to add a %instance% runner to a GitLab CI/CD pipeline:

1. Create the [`QODANA_TOKEN`](https://docs.gitlab.com/ee/ci/variables/) variable and save the %cloud% project token value in it 
2. Paste this sample to the `.gitlab-ci.yml` file: 

```yaml
stages:
  - qodana

qodana:
  stage: qodana
  only:
    - main
    - merge_requests
  image:
    name: jetbrains/qodana-<linter>
    entrypoint: [""]
  script:
    - qodana --save-report --results-dir=$CI_PROJECT_DIR/qodana 
     --report-dir=$CI_PROJECT_DIR/qodana/report
     --fail-threshold <number>
  artifacts:
    paths:
      - qodana
```
In this sample, specify the %instance% linter and the quality gate using `--fail-threshold` option. 
Using this configuration, %instance% will inspect the main branch and all merge requests coming to your repository.

## Inspection result overview

<link-summary>After your project is inspected and inspection results are uploaded to %cloud%, you can view results.</link-summary>

After your project is inspected and inspection results are uploaded to %cloud%, you can view results as shown 
[on this page](cloud-overview-reports.topic).