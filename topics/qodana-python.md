[//]: # (title: Qodana for Python)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<note>
    <p>
<include src="lib_qd.xml" include-id="eap-warning">
<var name="product" value="Qodana Python"/>
</include>
</p>
</note>

<var name="linter" value="Qodana Python"/>
<var name="ide" value="PyCharm Professional"/>

%linter% is based on [%ide%](https://www.jetbrains.com/pycharm/) and provides static analysis for Python projects.

## Try it now

### Analyze a project locally

To start, pull the image from Docker Hub (only necessary to get the latest version):

<var name="docker-image" value="jetbrains/qodana-python"/>

<code style="block" lang="shell">
  docker pull %docker-image%
</code>

For a basic Python project, which only uses `stdlib`, no preliminary steps are required.

In case a project has external `pypi` dependencies, use any of the following  options:
- Create `virtualenv` as a subfolder in your project and exclude it in [qodana.yaml](qodana-yaml.md#exclude-paths) to skip analysis of vendor code.
- Mount a separate `virtualenv` as [cache](qodana-python-docker-techs.xml#Cache+dependencies).

  When you create the `virtualenv` folder, no actual `python` binary is copied into it. Instead, a symlink is created to `python` binary used to create virtualenv. This could lead to incorrect paths when your `virtualenv` is being read inside the Qodana container, since `python` location there could be different. To fix this, create `virtualenv` using the Qodana container's `python`:

  ```shell
  docker run --rm \
        -v <source-directory>/:/data/project/ \
        -v <cache-directory>/:/data/cache/ \
        --entrypoint=bash \
        %docker-image% -c '
          python3 -m venv /data/cache/venv
          source /data/cache/venv/bin/activate
          pip3 install -r /data/project/requirements.txt
        '
  ```

The project dependencies are now stored in `<cache-directory>`. This folder could be preserved between builds to speed them up. 

Start local analysis with cache mounted and with `source-directory` pointing to the root of your project, and it would automatically look for `virtualenv` in `/data/cache/venv`:

   ```shell
   docker run --rm -it -p 8080:8080 \
      -v <source-directory>/:/data/project/ \
      -v <output-directory>/:/data/results/ \
      -v <cache-directory>/:/data/cache/ \
      %docker-image% --show-report
   ```

<p>
<include src="lib_qd.xml" include-id="show-report-command-explanation"/>
</p>

## Next steps

- <a href="qodana-python-docker-techs.xml">Configure %linter% Docker image</a>
- <a href="qodana-github-action.md">Run %linter% on GitHub</a>
- <a href="qodana-github-application.md">Run %linter% as a GitHub App</a>
- <a href="service.md">Use %linter% as a Service</a>
- <a href="ci.md">Extend your CI/CD with %linter% plugins</a>