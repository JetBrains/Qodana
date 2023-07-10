[//]: # (title: Package checking)

Relying on third-party software in your projects can become a source of vulnerability. To prevent security issues arising
from third-party packages, you can inspect your project using the Package checker tool available in the 
[Qodana for JVM](qodana-jvm.md) linter. This tool is powered by Checkmarx (c) and lets you check Gradle and Maven 
dependencies for known vulnerabilities and let you manage such cases by getting the information about vulnerable 
dependencies.  

## How it works

To inspect your code using Package Checker, in the [`qodana.yaml`](qodana-yaml.md) file, enable 
the `VulnerableLibrariesGlobal` inspection: 

<chunk id="package-checking-enable">

```yaml
include:
  - name: VulnerableLibrariesGlobal
```

</chunk>

After your project is inspected, you can update the packages containing vulnerabilities to versions where such 
vulnerabilities are fixed, or switch to alternative packages.