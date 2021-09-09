[//]: # (title: Clone Finder TeamCity plugin)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

The Qodana Clone Finder plugin for TeamCity lets you extend Qodana static analysis with the [Clone Finder](https://www.jetbrains.com/help/qodana/about-clone-finder.html) functionality.

## Quick start

* Ensure you have the [Qodana](https://www.jetbrains.com/help/qodana/qodana-teamcity-plugin.html) plugin for IntelliJ Inspection installed
* Install the Qodana Clone Finder plugin from [JetBrains Marketplace](https://plugins.jetbrains.com/plugin/15498-qodana)

Use [TeamCity VCS roots](https://www.jetbrains.com/help/teamcity/vcs-root.html) to add all required project source to the build.  

With the plugin installed, add the Qodana runner to your build. 

<img src="qodana-build-runner.png" width="641" alt="Qodana Build Runner" border-effect="line"/>  

Make sure the **Clone Finder** option is enabled and provide the following required parameters:

* Queried project: the project source code
* Referenced project directories: one or more projects to compare against
* Languages: languages to perform search

<img src="clone-finder-runner-settings.png" width="650" alt="Qodana Clone Finder Build Runner Settings" border-effect="line"/>

The example above shows that the project ```phpunit``` will be compared to the project ```pest``` and the analysis will be performed for the PHP language.

In this example, VCS roots are configured with the following mappings:
* ```phpunit``` sources will be checked out to the ```phpunit``` folder (=>phpunit)
* ```pest``` sources will be checked out to the ```pest``` folder (=>pest)

If you use DSL to configure your build, add this section to your build configuration description:

```JSON
 steps {
    ...
    qodana {
    ...
          param("clonefinder-languages", "PHP")
          param("clonefinder-languages-container", "PHP")
          param("clonefinder-docker-image", "custom")
          param("clonefinder-queried-project", "phpunit")
          param("clonefinder-custom-docker-image", "jetbrains/qodana-clone-finder")
          param("clonefinder-enable", "true")
          param("clonefinder-reference-projects", "pest")        
    }
 }    
```

> Temporary limitation: only one Qodana build step can be added to the configuration. If you
need to aggregate the analysis of several builds into one, use the TeamCity [Composite Build Configuration](https://www.jetbrains.com/help/teamcity/composite-build-configuration.html) feature.

After the build is finished, you will see the **Qodana** tab on the **Build Overview** page. Note that the tab
can be hidden under the **More** section. To see it in all builds with this step, mark the **Qodana** tab with a star.

Almost all [UI features](https://www.jetbrains.com/help/qodana/ui-overview.html) of the **Qodana** tab are similar among all Qodana tools we provide. They are
sufficient for exploring the results of a single run, but the tab in TeamCity offers even more. You can easily compare two
builds and focus on the difference. Now, the comparison is limited to a single build configuration, but
we are working on providing the cross-configuration option as well.

In the [inspection profile](https://www.jetbrains.com/help/qodana/ui-overview.html#Adjust+your+inspection+profile), you will find two inspections provided by Clone Finder:
* Code Fragments/Clone 
* Code Fragments/Clone with license mismatch

[//]: # "![Build Tab](tab.png) - irrelevant"

Check the [Qodana UI](https://www.jetbrains.com/help/qodana/ui-overview.html) to see all features available in the UI.

## License

<include src="lib_qd.xml" include-id="license-info">
    <var name="product" value="Qodana Clone Finder TeamCity plugin"/>
</include>