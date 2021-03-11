[//]: # (title: TeamCity Plugin)

The Qodana plugin for TeamCity lets you add static analysis to your build chain.

The plugin provides:
* Build runner
* Convenient UI
* Integration with TeamCity test support
* Smart and flexible build comparison
* Pliable build failure conditions

The plugin lets you add the code quality checks in the TeamCity pipeline or even start from scratch with static code analysis.

![Build Tab](tab.png)

## Quick Start Guide

Download and install the [Qodana plugin](https://plugins.jetbrains.com/plugin/15498-qodana) from JetBrains Marketplace on your TeamCity server or contact the server's administrator to do this.

With the plugin installed, add the Qodana runner to your build. If your project language is included in the list of 
fully [supported technologies](supported-technologies.md), no further preparation is needed. You can 
run your first analysis with the default settings right away.   

<img src="qodana-build-runner.png" width="641" alt="Qodana Build Runner"/>  

Make sure the **Code Inspections** option is enabled and start the build.

<img src="qodana-build-runner-settings.png" width="650" alt="Qodana Build Runner Settings"/>


If you use DSL to configure your build, add this section to your build configuration description:

```JSON
 steps {
    ...
    qodana {}
 }    
```

If your projects rely on technologies that are not fully supported, you may require additional steps in your build: for example, to download dependencies.

>Temporary limitation: only one Qodana build step can be added to the configuration. If you 
need to aggregate the analysis of several builds into one, use the TeamCity [Composite Build Configuration](https://www.jetbrains.com/help/teamcity/composite-build-configuration.html) feature.

After the build is finished, you will see the **Qodana** tab on the **Build Overview** page. Note that the tab 
can be hidden under the **More** section. To see it in all builds with this step, mark the **Qodana** tab with a star.

Almost all [UI features](ui-overview.md) of the **Qodana** tab are similar among all Qodana tools we provide. They are 
sufficient for exploring the results of a single run, but the tab in TeamCity offers even more. You can easily compare two 
builds and focus on the difference. Now, the comparison is limited to a single build configuration, but 
we are working on providing the cross-configuration option as well.

## Configuration

The main Qodana functionality comes from the 'engine' shaped into the Docker image. If you want to go beyond the 
boundaries of the default settings, refer to the [Docker image guide](docker-readme.md). Note that you don't need to write `docker run` on your own: the plugin will do it for you. You can just use all other options and provide them via the dedicated UI or DSL properties. 

### Advanced Configuration 

Advanced configuration allows you to report all found problems via the standard TeamCity tests mechanism. It means 
you can assign investigations, mute, see history, and do everything else you can do with regular tests in TeamCity. Qodana 
reports tests in four different ways:

- per problem
- per inspection type
- per inspection type/per module (if this information is available)
- per inspection type/per file

## License

By using the Qodana plugin, you agree to the [JetBrains EAP user agreement](https://www.jetbrains.com/legal/agreements/user_eap.html) and [JetBrains privacy policy](https://www.jetbrains.com/company/privacy.html).

## Contact

Contact us at [qodana-support@jetbrains.com](mailto:qodana-support@jetbrains.com) or via [our issue tracker](https://youtrack.jetbrains.com/newIssue?project=QD). We are eager to receive your feedback on the existing Qodana functionality and learn what other features you miss in it.