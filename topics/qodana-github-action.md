[//]: # (title: Qodana GitHub Action)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

Using [Qodana Scan](https://github.com/marketplace/actions/qodana-scan) GitHub Action, run Qodana with your GitHub workflow to scan your Java, Kotlin, PHP, Python, JavaScript, TypeScript projects and [other supported technologies by Qodana](https://www.jetbrains.com/help/qodana/supported-technologies.html).

## How to start
{id="how-to-start-github-action"}

To start running Qodana in your CI pipeline on GitHub all you need is to add the following lines to your workflow file:
```yaml
- uses: JetBrains/qodana-action@v4.1.0  # you can use @main if you want to use the latest version
  with:
    linter: jetbrains/qodana-jvm:2021.3  # Docker image full name with a tag
```

If you don't have any prepared workflow file in your repository, you can create a new one by using the example (store it
at `.github/workflows/code_scanning.yml`):

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

With the above workflow, Qodana will run on the main branch, release branches and on the pull requests coming to your repository. You will be able to see the results of the scan in the GitHub UI.

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

## Configuration

| Name                       | Description                                                                                                                        | Default Value                           |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| `linter`                   | [Official Qodana Docker image](https://www.jetbrains.com/help/qodana/docker-images.html). Required.                                | `jetbrains/qodana-jvm-community:latest` |
| `project-dir`              | The project's root directory to be analyzed. Optional                                                                              | `${{ github.workspace }}`               |
| `results-dir`              | Directory to store the analysis results. Optional.                                                                                 | `${{ runner.temp }}/qodana/results`     |
| `cache-dir`                | Directory to store Qodana caches. Optional.                                                                                        | `${{ runner.temp }}/qodana/caches`      |
| `idea-config-dir`          | IntelliJ IDEA configuration directory. Optional.                                                                                   | -                                       |
| `gradle-settings-path`     | Provide path to gradle.properties file. An example: "/your/custom/path/gradle.properties". Optional.                               | -                                       |
| `additional-volumes`       | Mount additional volumes to Docker container. Optional.                                                                            | -                                       |
| `additional-env-variables` | Pass additional environment variables to docker container. Optional.                                                               | -                                       |
| `fail-threshold`           | Set the number of problems that will serve as a quality gate. If this number is reached, the pipeline run is terminated. Optional. | -                                       |
| `inspected-dir`            | Directory to be inspected. If not specified, the whole project is inspected by default. Optional.                                  | -                                       |
| `baseline-path`            | Run in baseline mode. Provide the path to an existing SARIF report to be used in the baseline state calculation. Optional.         | -                                       |
| `baseline-include-absent`  | Include the results from the baseline absent in the current Qodana run in the output report. Optional.                             | `false`                                 |
| `changes`                  | Inspect uncommitted changes and report new problems. Optional.                                                                     | `false`                                 |
| `script`                   | Override the default docker scenario. Optional.                                                                                    | -                                       |
| `profile-name`             | Name of a profile defined in the project. Optional.                                                                                | -                                       |
| `profile-path`             | Absolute path to the profile file. Optional.                                                                                       | -                                       |
| `upload-result`            | Upload Qodana results as an artifact to the job. Optional.                                                                         | `true`                                  |
| `use-caches`               | Utilize GitHub caches for Qodana runs. Optional.                                                                                   | `true`                                  |
| `use-annotations`          | Use annotation to mark the results in the GitHub user interface. Optional.                                                         | `true`                                  |
| `github-token`             | GitHub token to be used for uploading results. Optional.                                                                           | `${{ github.token }}`                   |

<p><include src="lib_qd.xml" include-id="docker-options-tip"/></p>
