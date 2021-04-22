[//]: # (title: Quick Start Guide)

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

> Temporary limitation: only one Qodana build step can be added to the configuration. If you
need to aggregate the analysis of several builds into one, use the TeamCity [Composite Build Configuration](https://www.jetbrains.com/help/teamcity/composite-build-configuration.html) feature.

After the build is finished, you will see the **Qodana** tab on the **Build Overview** page. Note that the tab
can be hidden under the **More** section. To see it in all builds with this step, mark the **Qodana** tab with a star.

Almost all [UI features](ui-overview.md) of the **Qodana** tab are similar among all Qodana tools we provide. They are
sufficient for exploring the results of a single run, but the tab in TeamCity offers even more. You can easily compare two
builds and focus on the difference. Now, the comparison is limited to a single build configuration, but
we are working on providing the cross-configuration option as well.
