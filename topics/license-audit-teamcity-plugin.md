[//]: # (title: License Audit TeamCity Plugin)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

The Qodana License Audit plugin for TeamCity lets you extend Qodana static analysis with the [License Audit](about-license-audit.md) functionality.

## Quick start

* Ensure you have the [Qodana](https://www.jetbrains.com/help/qodana/qodana-teamcity-plugin.html) plugin for IntelliJ Inspection installed
* Install the Qodana License Audit plugin from [JetBrains Marketplace](https://plugins.jetbrains.com/plugin/15498-qodana)

[//]: # "TODO: update the plugin link"

Use [TeamCity VCS roots](https://www.jetbrains.com/help/teamcity/vcs-root.html) to add all required project source to the build.

With the plugin installed, [add the Qodana runner to your build](teamcity-plugin-configuration.md).

<img src="qodana-build-runner.png" width="641" alt="Qodana Build Runner"/>  

**Specify the build settings**

1. Select the checkbox next to **License Audit**. 
   
2. For **Additional arguments for 'docker run'**, specify:

    - (Optional) [Your project's tools versions](license-audit-docker-techs.md#Configuration), for example, `-e PYTHON_VERSION=3.7.10`
    - (Optional) Using verbose License Audit build output with `-e QODANA_VERBOSE=true` 

[//]: # "TODO: discuss the variable QODANA_VERBOSE naming"

Also use qodana.yaml and qodana.license.rules.json in your project to configure the tool.

3. If you use DSL to configure your build, add this section to your build configuration description:

```JSON
 steps {
    ...
    qodana {
    ...
          param("licenseaudit-custom-docker-image", "jetbrains/qodana-license-audit")
          param("licenseaudit-enable", "true")
    }
 }    
```

4. For **Docker image name**, specify an image name (and optionally tag).

   **Public Image (Latest)** points to the default `jetbrains/qodana-license-audit:latest`.

   **Custom** allows to specify your own value in the field that appears below.

5. Click **Save**. Now you can run a build with new inspection parameters you specified.

<note>
 
Temporary limitation: only one Qodana build step can be added to the configuration. If you
need to aggregate the analysis of several builds into one, use the TeamCity [Composite Build Configuration](https://www.jetbrains.com/help/teamcity/composite-build-configuration.html) feature.

</note>

> After the build is finished, you will see the **Qodana** tab on the **Build Overview** page. Note that the tab can be hidden under the **More** section. To see it in all builds with this step, mark the **Qodana** tab with a star.

Almost all [UI features](results.md) of the **Qodana** tab are similar across all Qodana tools we provide. They are sufficient for exploring the results of a single run, but the tab in TeamCity offers even more. You can easily compare two builds and focus on the difference. Now, the comparison is limited to a single build configuration, but
we are working on providing the cross-configuration option as well.

In the [inspection profile](ui-overview.md#Adjust+your+inspection+profile), you will find six inspections provided by License Audit:
* Unrecognized project license
* Unrecognized dependency license
* No project licenses
* No dependency licenses
* Prohibited dependency license
* Uncategorized dependency license


Check the chapter about [Qodana Inspection Results](results.md) to see all features available in the UI.


## License

<include src="lib_qd.xml" include-id="license-info">
    <var name="product" value="Qodana Clone Finder TeamCity plugin"/>
</include>