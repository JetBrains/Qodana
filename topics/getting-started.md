[//]: # (title: Getting started)

<var name="linter" value="Qodana"/>

The current version of %product% (%product-version%) lets you analyze 
<a href="supported-technologies.md">Java, Kotlin, PHP, Python, JavaScript, and TypeScript</a> projects. Eventually, all 
languages and technologies covered by JetBrains IDEs will be added.

## Analyze a project locally

Start with any of the [provided linters](supported-technologies.md). For all linters the procedure is basically the same.

```shell
docker run --rm -it -v <source-directory>/:/data/project/ \ 
  -p 8080:8080 jetbrains/qodana-<linter> --show-report
```

with `source-directory` pointing to the root of your project.

You can [check results in your browser](html-report.md) at `http://localhost:8080`.


## Next steps

 - <a href="docker-images.md">Configure %linter% Docker images</a>
 - <a href="github-actions.md">Run %linter% on GitHub</a>
 - <a href="qodana-github-application.md">Run %linter% as a GitHub App</a>
 - <a href="service.md">Use %linter% as a Service</a>
 - <a href="ci.md">Extend your CI/CD with %linter% plugins</a>

 