[//]: # (title: Qodana for JS)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<note>
    <p>
<include src="lib_qd.xml" include-id="eap-warning">
<var name="product" value="Qodana JS"/>
</include>
</p>
</note>

<var name="linter" value="Qodana for JS"/>

<var name="linter" value="Qodana JS"/>
<var name="ide" value="WebStorm"/>
<var name="docker-image" value="jetbrains/qodana-js:2021.3-eap"/>

%linter% is based on [%ide%](https://www.jetbrains.com/webstorm/) and provides static analysis for JavaScript or TypeScript projects.

## Try it now

### Analyze a project locally

#### Install project dependencies

For a basic JavaScript project that has no external dependencies, no preliminary steps are required.

In case the project has external dependencies, you can set them up using the `bootstrap` field in the `qodana.yaml` file. 
For example, if your project dependencies are specified by the `yarn.lock` file in your project root, add the following 
line to `qodana.yaml`:

```yaml
bootstrap: yarn install
```

The command will be automatically executed before the analysis. You can use the `npm` or `yarn` commands to install dependencies.

#### Run analysis

<p><include src="lib_qd.xml" include-id="qodana-cli-quickstart" use-filter="js-py,js-only,non-gs,empty"/></p>

## Next steps

- <a href="qodana-js-docker-techs.xml">Configure %linter% Docker image</a>
- <a href="qodana-github-action.md">Run %linter% on GitHub</a>
- <a href="service.md">Use %linter% as a Service</a>
- <a href="ci.md">Extend your CI/CD with %linter% plugins</a>
