![](https://jb.gg/badges/official-flat-square.svg)  
![](resources/eap-alert.png) 
![](resources/banner-main.png)

**Qodana** is a code quality monitoring tool to identify and suggest fixes for bugs, security vulnerabilities, duplications, and imperfections. 
It brings all the smart features you love in the JetBrains IDEs into your project pipelines. 
It takes different shapes: [Docker for any CI](Docker/README.md), [GitHub actions & application](GitHub/README.md), [TeamCity plugin](TeamCity/README.md), or a separate [cloud service](Service/README.md), but has a common goal: guiding users towards more robust, more maintainable, and healthier code.

It works with PHP, Java and Kotlin projects today, and eventually will support [languages and technologies](General/supported-technologies.md) covered by JetBrains IDEs.

### Analyse project locally

Pull the image from Docker hub
```
docker pull jetbrains/qodana
```
and run the analysis locally

```
docker run -v <source-folder>/:/data/project/ -p 8080:8080 jetbrains/qodana --show-report 
```

The `source-folder` should point to the root of your project. 
Check the results in your browser at http://localhost:8080.
 
Please read [Docker guide](/Docker/README.md) for more options and details related to the execution.

### Run at GitHub

You can setup a workflow in your GitHub repository using the GitHub action we published. 

### License
Using Qodana you agree to [JetBrains EAP user agreement](https://www.jetbrains.com/legal/agreements/user_eap.html) and [JetBrains privacy policy](https://www.jetbrains.com/company/privacy.html).

## Contact
Contact us at [qodana-support@jetbrains.com](mailto:qodana-support@jetbrains.com) or via [our issue tracker](https://youtrack.jetbrains.com/newIssue?project=QD). We eagerly want your feedback on what's already there and if there are any features that we miss.
