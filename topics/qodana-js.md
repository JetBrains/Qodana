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

%linter% is based on [%ide%](https://www.jetbrains.com/webstorm/) and provides static analysis for JavaScript or TypeScript projects.

## Try it now

### Analyze a project locally

To start, pull the image from Docker Hub (only necessary to get the latest version):

<var name="docker-image" value="jetbrains/qodana-js"/>

<code style="block" lang="shell">
  docker pull %docker-image%
</code>

For a basic JavaScript project, which does not have dependencies, no preliminary steps are required.


In case a project has external `npm` dependencies, add the following step before you run the analysis:

   ```shell
  docker run --rm -v <source-directory>:/usr/src/app -w /usr/src/app node:lts npm install
   ```

You can use any Node version your project requires or use yarn or other package managers to install the project dependencies.

The project dependencies are now stored in `<source-directory>/node_modules`. This folder could be preserved between builds to speed them up. 

Start local analysis with cache mounted and with `source-directory` pointing to the root of your project, and it would automatically look for `node_modules` in `/data/project/node_modules`:

   ```shell
   docker run --rm -it -p 8080:8080 \
      -v <source-directory>/:/data/project/ \
      -v <output-directory>/:/data/results/ \
      %docker-image% --show-report
   ```

<p>
<include src="lib_qd.xml" include-id="show-report-command-explanation"/>
</p>

## Next steps

- <a href="qodana-js-docker-techs.xml">Configure %linter% Docker image</a>
- <a href="qodana-github-action.md">Run %linter% on GitHub</a>
- <a href="service.md">Use %linter% as a Service</a>
- <a href="ci.md">Extend your CI/CD with %linter% plugins</a>
