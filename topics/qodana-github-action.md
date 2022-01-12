[//]: # (title: Qodana GitHub Action)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

Using the [Qodana Scan](https://github.com/marketplace/actions/qodana-scan) GitHub Action, you can run Qodana within 
your GitHub workflow to scan your Java, Kotlin, PHP, Python, JavaScript, and TypeScript projects and 
[other technologies supported by Qodana](https://www.jetbrains.com/help/qodana/supported-technologies.html).

## How to start
{id="how-to-start-github-action"}

You can run Qodana with GitHub Actions using [Qodana Scan](https://github.com/marketplace/actions/qodana-scan). 
To do it, add `.github/workflows/code_scanning.yml` to your repository with the following contents:

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
      - uses: actions/checkout@v2
      - name: 'Qodana Scan'
        uses: JetBrains/qodana-action@v4.2.2
        with:
          linter: jetbrains/qodana-jvm  # pick the needed linter – https://www.jetbrains.com/help/qodana/docker-images.html
```
We recommend that you have a separate workflow file for Qodana because [different jobs run in parallel](https://help.github.com/en/actions/getting-started-with-github-actions/core-concepts-for-github-actions#job). 

Using this workflow, Qodana will run on the main branch, release branches, and on the pull requests coming to your 
repository. Inspection results will be available in the GitHub UI.

### Get a Qodana badge

You can set up a Qodana workflow badge in your repository: 

[![Qodana](https://github.com/JetBrains/qodana-action/actions/workflows/code_scanning.yml/badge.svg)](https://github.com/JetBrains/qodana-action/actions/workflows/code_scanning.yml) 

To do it, follow these steps:

1. Navigate to the workflow run that you previously configured.
2. On the workflow page, select **Create status badge**.  
3. Copy the Markdown text to your repository README file.

<img src="https://user-images.githubusercontent.com/13538286/148529278-5d585f1d-adc4-4b22-9a20-769901566924.png" alt="Creating status badge" width="706"/>

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
<note>Hosting of multiple Qodana reports in a single GitHub Pages repository is not supported.</note>

### GitHub code scanning

You can set up [GitHub code scanning](https://docs.github.com/en/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/about-code-scanning) for your project using Qodana. To do it, add these lines to the workflow file right after the `Qodana` 
action configuration:

```yaml
      - uses: github/codeql-action/upload-sarif@v1
        with:
          sarif_file: ${{ runner.temp }}/qodana/results/qodana.sarif.json
```

### Pull request quality gate

You can enforce GitHub to block the merge of pull requests if the Qodana quality gate has failed. To do it, create a 
branch protection rule as described below:

1. Create new or open an existing GitHub workflow with the Qodana Action specified.
2. Set the workflow to run on `pull_request` events that target the `main` branch.
```yaml
on:
  pull_request:
    branches:
    - main
```

Instead of `main`, you can specify your branch here. 

3. Set `1` for the Qodana Action `fail-threshold` option.
4. Under your repository name, click **Settings**. 
5. On the left menu, click **Branches**.
6. In the branch protection rules section, click **Add rule**.
7. Add `main` to **Branch name pattern**.
8. Select **Require status checks to pass before merging**. 
9. Search for the `Qodana` status check, then check it.
10. Click **Create**.

For more information about branch protection rules, refer to the original [GitHub Documentation](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/managing-a-branch-protection-rule).

### Configuration

For more configuration options, please refer to [Qodana Scan page](https://github.com/marketplace/actions/qodana-scan) 
on GitHub Marketplace.

<p><include src="lib_qd.xml" include-id="docker-options-tip"/></p>
