[//]: # (title: Qodana IntelliJ GitHub Action)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

While the [Qodana IntelliJ GitHub app](qodana-intellij-github-application.md) supports only public repositories, for private repositories use the Qodana IntelliJ GitHub action.

The **Qodana IntelliJ GitHub action** is a more general tool for easier continuous code inspection.
Anyone with the write permission to a repository can set up a continuous code inspection with Qodana using GitHub actions.

## How to start
{id="how-to-start-github-action"}

Example GitHub Workflow (`.github/workflows/qodana.yml`):

```yaml
  jobs:
    qodana:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v2
        - uses: actions/cache@v2
          with:
            path: ~/work/_temp/_github_home/cache
            key: ${{ runner.os }}-qodana-${{ github.ref }}
            restore-keys: |
              ${{ runner.os }}-qodana-${{ github.ref }}
              ${{ runner.os }}-qodana-   
        - uses: docker://jetbrains/qodana-<linter>
          with:
            args: --cache-dir=/github/home/cache --results-dir=/github/workspace/qodana --save-report --report-dir=/github/workspace/qodana/report
        - uses: actions/upload-artifact@v2
          with:
            path: qodana
  ```

<p><include src="lib_qd.xml" include-id="docker-options-tip"/></p>

For detailed instructions, see the [Qodana IntelliJ GitHub action](https://github.com/marketplace/actions/qodana-code-inspection) on GitHub Marketplace.