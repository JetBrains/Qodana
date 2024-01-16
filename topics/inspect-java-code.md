[//]: # (title: Inspect Java code)

<var name="JenkinsCred" value="https://www.jenkins.io/doc/book/using/using-credentials/#adding-new-global-credentials"/>
<var name="docker-image" value="jetbrains/qodana-jvm&lt;-community/android&gt;:2023.3"/>

To inspect your Java codebase, depending on your %product% [license](pricing.md) you can employ the following linters: 

<tabs>
<tab id="inspect-java-code-linters" title="Linters">

| Linter name                | Suitable %product% licenses |
|----------------------------|-----------------------------|
| [](qodana-jvm.md)          | Ultimate and Ultimate Plus  |
| [](qodana-jvm-community.md)| Community                   |
| [](qodana-jvm-android.md)  | Community                   |

</tab>
<tab id="inspect-java-code-techs" title="Supported technologies and features">
<p>Here is the list of technologies and features supported by all linters.</p>
<tabs>
<tab id="inspect-java-code-techs-features" title="Features">

| Supported feature            | [](qodana-jvm.md) | [](qodana-jvm-community.md) | [](qodana-jvm-android.md) |
|------------------------------|-------------------|-----------------------------|---------------------------|
| [](baseline.xml)             | &#x2714;          | &#x2714;                    | &#x2714;                  |
| [](quality-gate.xml)         | &#x2714;          | &#x2714;                    | &#x2714;                  |
| [](code-coverage.md)         | &#x2714;          | &#x274c;                    | &#x274c;                  |
| [](license-audit.xml)        | &#x2714;          | &#x274c;                    | &#x274c;                  |
| [](quick-fix.md)             | &#x2714;          | &#x274c;                    | &#x274c;                  |
| [](vulnerability-checker.md) | &#x2714;          | &#x274c;                    | &#x274c;                  |

</tab>
<tab id="inspect-java-code-techs-pls" title="Programming languages">

| Linter name                | Supported languages           |
|----------------------------|-------------------------------|
| [](qodana-jvm.md)          | Java, Kotlin, Groovy          |
| [](qodana-jvm-community.md)| Java, Kotlin, Groovy          |
| [](qodana-jvm-android.md)  | Android, Java, Kotlin, Groovy |

</tab>
<tab id="inspect-java-code-techs-pls" title="Markup languages">

| Linter name                | Supported languages                                                                       |
|----------------------------|-------------------------------------------------------------------------------------------|
| [](qodana-jvm.md)          | CSS, FreeMarker Template Language, HTML, JSON and JSON5, RELAX NG, XML, XPath, XSLT, YAML |
| [](qodana-jvm-community.md)| HTML, JSON and JSON5, RELAX NG, XML, XPath, XSLT                                          |
| [](qodana-jvm-android.md)  | HTML, JSON and JSON5, RELAX NG, TOML, XML, XPath, XSLT, YAML                              |

</tab>
<tab id="inspect-java-code-techs-pls" title="Scripting languages">

| Linter name                | Supported languages                    |
|----------------------------|----------------------------------------|
| [](qodana-jvm.md)          | Expression Language (EL), Shell script |
| [](qodana-jvm-community.md)| None                                   |
| [](qodana-jvm-android.md)  | Shell script                           |

</tab>
<tab id="inspect-java-code-techs-pls" title="Databases and ORM">

| Linter name                  | Supported technologies                                             |
|------------------------------|--------------------------------------------------------------------|
| [](qodana-jvm.md)            | Hibernate ORM, MongoJS, Oracle, MySQL, PostgreSQL, SQL, SQL server |
| [](qodana-jvm-community.md)  | None                                                               |
| [](qodana-jvm-android.md)    | None                                                               |

</tab>
<tab id="inspect-java-code-techs-pls" title="Build management">

| Linter name                | Supported technologies |
|----------------------------|------------------------|
| [](qodana-jvm.md)          | Ant, Gradle, Maven     |
| [](qodana-jvm-community.md)| Ant, Gradle, Maven     |
| [](qodana-jvm-android.md)  | Ant, Gradle, Maven     |

</tab>
<tab id="inspect-java-code-techs-pls" title="Frameworks and libraries">

| Linter name                   | Supported technologies                                                                              |
|-------------------------------|-----------------------------------------------------------------------------------------------------|
| [](qodana-jvm.md)             | Jakarta EE, Java EE, JavaBeans, JAX-RS, JPA, JSP, JUnit, Lombok, Reactive Streams, Spring, TestNG   |
| [](qodana-jvm-community.md)   | JavaBeans, JPA, JUnit, Lombok, Reactive Streams, TestNG                                             |
| [](qodana-jvm-android.md)     | JavaBeans, JavaFX, JUnit, Lombok, TestNG                                                            |

</tab>
</tabs>
</tab>
</tabs>


Here are several configuration snippets showing how you can inspect Java code.

<!-- I need to modify all these tabs accordingly -->

<tabs>
<tab id="inspect-java-code-github" title="GitHub Actions">
    <include src="lib_qd.xml" include-id="github-basic-configuration"/>
</tab>
<tab id="inspect-java-code-jenkins" title="Jenkins">

Here is the Jenkins Pipeline configuration.

```groovy
pipeline {
    environment {
        QODANA_TOKEN=credentials('qodana-token')
    }
    agent {
        docker {
            args '''
              -v "${WORKSPACE}":/data/project
              --entrypoint=""
              '''
            image 'jetbrains/qodana-jvm<-community/android>:2023.3'
        }
    }
    stages {
        stage('Qodana') {
            steps {
                sh '''qodana'''
            }
        }
    }
}
```

In this configuration, the `environment` block defines the `QODANA_TOKEN` variable to invoke the
[project token](project-token.md) generated in Qodana Cloud and contained in
the `qodana-token` [global credentials](%JenkinsCred%). The project token is required by the paid %product%
[linters](pricing.md#pricing-linters-licenses), and is optional for using with the Community linters.

</tab>
<tab id="inspect-python-code-local" title="Run locally">
<include src="lib_qd.xml" include-id="qodana-cli-quickstart" use-filter="jvm-only,empty"/>
</tab>
</tabs>



