[//]: # (title: GitHub Actions)

## Usage

The [Qodana Scan GitHub action](https://github.com/marketplace/actions/qodana-scan)
allows you to run Qodana on a GitHub repository.

<anchor name="basic-configuration"></anchor>

### Basic configuration

To configure Qodana Scan, save the `.github/workflows/code_quality.yml` file containing the workflow configuration:

```yaml
name: Qodana
on:
  workflow_dispatch:
  pull_request:
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
        uses: JetBrains/qodana-action@v2022.3.0
```

Using this workflow, Qodana will run on the main branch, release branches, and on the pull requests coming to your
repository.

Note: `fetch-depth: 0` is required for checkout in case Qodana works in pull request mode (reports issues that appeared only in that pull request).

We recommend that you have a separate workflow file for Qodana
because [different jobs run in parallel](https://help.github.com/en/actions/getting-started-with-github-actions/core-concepts-for-github-actions#job)
.

### GitHub code scanning

You can set
up [GitHub code scanning](https://docs.github.com/en/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/about-code-scanning)
for your project using Qodana. To do it, add these lines to the `code_quality.yml` workflow file right below
[the basic configuration](#basic-configuration) of Qodana Scan:

```yaml
      - uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: ${{ runner.temp }}/qodana/results/qodana.sarif.json
```

This sample invokes `codeql-action` for uploading a SARIF-formatted Qodana report to GitHub and specifies the report
file using the `sarif_file` key.

> GitHub code scanning does not export inspection results to third-party tools, which means you cannot use this data for further processing by Qodana. In this case, you must set up baseline and quality gate processing on the Qodana side before submitting inspection results to GitHub code scanning. See the
[Quality gate and baseline](#quality-gate-and-baseline) section for details.

### Pull request quality gate

You can enforce GitHub to block the merge of pull requests if the Qodana quality gate has failed. To do it, create a
[branch protection rule](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/managing-a-branch-protection-rule)
as described below:

1. Create a new or open an existing GitHub workflow that invokes the Qodana Scan action.
2. Set the workflow to run on `pull_request` events that target the `main` branch.

```yaml
on:
  pull_request:
    branches:
      - main
```

Instead of `main`, you can specify your branch here.

3. Set the number of problems (integer) for the Qodana action `fail-threshold` option.
4. Under your repository name, click **Settings**.
5. On the left menu, click **Branches**.
6. In the branch protection rules section, click **Add rule**.
7. Add `main` to **Branch name pattern**.
8. Select **Require status checks to pass before merging**.
9. Search for the `Qodana` status check, then check it.
10. Click **Create**.

<anchor name="quality-gate-and-baseline"></anchor>

### Quality gate and baseline

You can combine the [quality gate](https://www.jetbrains.com/help/qodana/quality-gate.html), and [baseline](https://www.jetbrains.com/help/qodana/qodana-baseline.html) features to manage your
technical debt, report only new problems, and block pull requests that contain too many issues.

Follow these steps to establish a baseline for your project:

1. Run Qodana [locally](https://www.jetbrains.com/help/qodana/getting-started.html#Analyze+a+project+locally) over your project:

```shell
cd <source-directory>
qodana scan --show-report
```

2. Open your report at `http://localhost:8080/`, [add detected problems](https://www.jetbrains.com/help/qodana/ui-overview.html#Technical+debt) to the baseline,
   and download the `qodana.sarif.json` file.

3. Upload the `qodana.sarif.json` file to your project root folder on GitHub.

4. Append `--baseline,qodana.sarif.json` argument to the Qodana Scan action configuration `args` parameter in the `code_quality.yml` file:

```yaml
- name: Qodana Scan
  uses: JetBrains/qodana-action@v2022.3.0
  with:
    args: --baseline,qodana.sarif.json
```

If you want to update the baseline, you must repeat these steps.

After that, the Qodana Scan GitHub action will generate alerts only for the problems that were not added to the baseline as new.

To establish a quality gate additionally to the baseline, add this line to `qodana.yaml` in the root of your repository:

```yaml
failThreshold: <number-of-accepted-problems>
```

Based on this, you will be able to detect only new problems in pull requests that fall beyond the baseline. At the same
time, pull requests with **new** problems exceeding the `fail-threshold` limit will be blocked, and the workflow will fail.

### GitHub Pages

If you wish to study [Qodana reports](https://www.jetbrains.com/help/qodana/html-report.html) directly on GitHub, you
can host them on your [GitHub Pages](https://docs.github.com/en/pages) repository using this example workflow:

```yaml
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ${{ runner.temp }}/qodana/results/report
          destination_dir: ./
```

> Hosting multiple Qodana reports in a single GitHub Pages repository is not supported.

### Get a Qodana badge

You can set up a Qodana workflow badge in your repository. To do it, follow these steps:

1. Navigate to the workflow run that you previously configured.
2. On the workflow page, select **Create status badge**.
3. Copy the Markdown text to your repository README file.

<img src="https://user-images.githubusercontent.com/13538286/148529278-5d585f1d-adc4-4b22-9a20-769901566924.png" alt="Creating status badge" width="706"/>

## Configuration

Most likely, you won't need other options than `args`: all other options can be helpful if you are configuring multiple Qodana Scan jobs in one workflow. 

Use [`with`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstepswith) to define any action parameters:

```yaml
with:
  args: --baseline,qodana.sarif.json
```

| Name                    | Description                                                                                                                                                                                  | Default Value                       |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|
| `args`                  | Additional [Qodana CLI `scan` command](https://github.com/jetbrains/qodana-cli#scan) arguments, split the arguments with commas (`,`), for example `-i,frontend,--print-problems`. Optional. | -                                   |
| `results-dir`           | Directory to store the analysis results. Optional.                                                                                                                                           | `${{ runner.temp }}/qodana/results` |
| `upload-result`         | Upload Qodana results as an artifact to the job. Optional.                                                                                                                                   | `true`                              |
| `artifact-name`         | Specify Qodana results artifact name, used for results uploading. Optional.                                                                                                                  | `qodana-report`                     |
| `cache-dir`             | Directory to store Qodana cache. Optional.                                                                                                                                                   | `${{ runner.temp }}/qodana/caches`  |
| `use-caches`            | Utilize GitHub caches for Qodana runs. Optional.                                                                                                                                             | `true`                              |
| `additional-cache-hash` | Allows customizing the generated cache hash. Optional.                                                                                                                                       | `${{ github.sha }}`                 |
| `use-annotations`       | Use annotation to mark the results in the GitHub user interface. Optional.                                                                                                                   | `true`                              |
| `pr-mode`               | Analyze only changed files in a pull request. Optional.                                                                                                                                      | `true`                              |

[gh:qodana]: https://github.com/JetBrains/qodana-action/actions/workflows/code_scanning.yml
[youtrack]: https://youtrack.jetbrains.com/issues/QD
[youtrack-new-issue]: https://youtrack.jetbrains.com/newIssue?project=QD&c=Platform%20GitHub%20action
[jb:confluence-on-gh]: https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub
[jb:discussions]: https://jb.gg/qodana-discussions
[jb:twitter]: https://twitter.com/Qodana
[jb:docker]: https://hub.docker.com/r/jetbrains/qodana
