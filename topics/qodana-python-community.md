[//]: # (title: Qodana Community for Python)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<img src="python.png" dark-src="python_dark.png" alt="Python" width="296"/>

<note>
    <p>
<include src="lib_qd.xml" include-id="eap-warning">
<var name="product" value="Qodana Community Python"/>
</include>
</p>
</note>

<var name="linter" value="Qodana Community Python"/>
<var name="ide" value="PyCharm Community"/>
<var name="docker-image" value="jetbrains/qodana-python-community:2023.2-eap"/>

%linter% is based on [%ide%](https://www.jetbrains.com/pycharm/) and provides static analysis for Python projects.

## Try it now

### Analyze a project locally

#### Install project dependencies

For a basic Python project that has no external dependencies, no preliminary steps are required. 

In case the project has external `pip` dependencies, you can set them up using the `bootstrap` field in the `qodana.yaml` file.  
For example, if your project dependencies are specified by the `requirements.txt` file in your project root, add the following line to `qodana.yaml`:

```yaml
bootstrap: pip install -r requirements.txt
```

The command will be automatically executed before the analysis.

#### Run analysis

<p><include src="lib_qd.xml" include-id="qodana-cli-quickstart" use-filter="non-php,py-only,non-gs,empty"/></p>

## Next steps

- <a href="qodana-python-docker-readme.xml">Configure %linter% Docker image</a>
- <a href="github.md">Run %linter% on GitHub</a>
- <a href="service.md">Use %linter% as a Service</a>
- <a href="ci.md">Extend your CI/CD with %linter% plugins</a>
