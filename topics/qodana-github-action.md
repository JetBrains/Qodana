[//]: # (title: Qodana GitHub Action)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

Using the [Qodana Scan](https://github.com/marketplace/actions/qodana-scan) GitHub Action, you can run Qodana within 
your GitHub workflow to scan your Java, Kotlin, PHP, Python, JavaScript, and TypeScript projects and 
[other technologies supported by Qodana](https://www.jetbrains.com/help/qodana/supported-technologies.html).

## How to start
{id="how-to-start-github-action"}

To run Qodana within your GitHub CI pipeline, just add the following lines to the workflow file:
```yaml
- uses: JetBrains/qodana-action@v4.2.0  # you can use @main if you want to use the latest version
  with:
    linter: jetbrains/qodana-jvm:2021.3  # Docker image full name with a tag
```

In case you have not created a workflow for your repository yet, you can save this sample to the 
`.github/workflows/code_scanning.yml` file:

```yaml
name: Code Scanning
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
        uses: JetBrains/qodana-action@v4.1.0
        with:
          linter: jetbrains/qodana-jvm
```

Using this workflow, Qodana will run on the main branch, release branches, and all incoming pull requests. 
You will be able to observe scan results in the GitHub UI.

### Configuration

For more configuration options, please refer to [Qodana Scan page](https://github.com/marketplace/actions/qodana-scan) in GitHub Marketplace.

### GitHub Pages

If you want to explore [Qodana reports](https://www.jetbrains.com/help/qodana/html-report.html) immediately on GitHub, 
you can enable this feature for your repository using [GitHub Pages](https://docs.github.com/en/pages):
```yaml
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ${{ runner.temp }}/qodana/results/report
          destination_dir: ./
```
> It is not possible to host multiple reports on GitHub Pages for a single repository.


### GitHub code scanning

You can set up [GitHub code scanning](https://docs.github.com/en/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/about-code-scanning) for your project using Qodana. To do it, append this to your workflow file 
after the lines specifying the Qodana action:
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

<p><include src="lib_qd.xml" include-id="docker-options-tip"/></p>
