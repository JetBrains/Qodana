[//]: # (title: Qodana GitHub Action)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

Using the [Qodana Scan](https://github.com/marketplace/actions/qodana-scan) GitHub Action, you can run Qodana within 
your GitHub workflow to scan your Java, Kotlin, PHP, Python, JavaScript, and TypeScript projects and 
[other technologies supported by Qodana](https://www.jetbrains.com/help/qodana/supported-technologies.html).

## How to start
{id="how-to-start-github-action"}

To run Qodana with [GitHub Actions](https://github.com/features/actions), add `.github/workflows/code_scanning.yml` with the following contents:

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
We recommend you to have a separated workflow file for Qodana, because [different jobs run in parallel](https://help.github.com/en/actions/getting-started-with-github-actions/core-concepts-for-github-actions#job). 


With the above workflow, Qodana will run on the main branch, release branches and on the pull requests coming to your repository.
You will be able to see the results of the scan in the GitHub UI.

### Get a Qodana badge

To set up a badge with the workflow [![Qodana](https://github.com/JetBrains/qodana-action/actions/workflows/code_scanning.yml/badge.svg)](https://github.com/JetBrains/qodana-action/actions/workflows/code_scanning.yml), go to the workflow run you've just configured then click "Create status badge," copy the suggested Markdown text to your repository README file.

![create_status_badge](https://user-images.githubusercontent.com/13538286/148529278-5d585f1d-adc4-4b22-9a20-769901566924.png)


### GitHub Pages

If you want to see [the full Qodana report](https://www.jetbrains.com/help/qodana/html-report.html) right on GitHub, you can host it on your repository [GitHub Pages](https://docs.github.com/en/pages), using the following example workflow:
```yaml
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ${{ runner.temp }}/qodana/results/report
          destination_dir: ./
```
Note: It's not possible to host multiple reports on GitHub Pages in one repository.


### GitHub code scanning

You can set up [GitHub code scanning](https://docs.github.com/en/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/about-code-scanning) with Qodana for your project by adding the following lines after Qodana action to your workflow file:
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

For more configuration options, please refer to [Qodana Scan page](https://github.com/marketplace/actions/qodana-scan) in GitHub Marketplace.

<p><include src="lib_qd.xml" include-id="docker-options-tip"/></p>
