[//]: # (title: Qodana IDE plugin)

The [Qodana IDE plugin](https://plugins.jetbrains.com/plugin/16938-qodana) is a plugin for JetBrains IDEs such as IntelliJ IDEA or PhpStorm. It provides a link between a Qodana report and your project opened in an IDE. With the plugin installed, you can navigate between the issues detected by the [](about-qodana-intellij.md) linter as well as use the **Open in IDE** functionality provided by the [Qodana UI](ui-overview.md).

## Quick start

1. Install the plugin for your IDE as described in the [IntelliJ IDEA Documentation](https://www.jetbrains.com/help/idea/?Managing_Plugins). IDE versions 2021.2 and later are supported. 
2. In the IDE, go to **Tools | Show Qodana Report | Open Qodana Report** and select a `qodana.sarif.json` report file generated after performing a Qodana run. See [](qodana-intellij-output.md) for details.
3. In the **Problems** tool window that opens, you can view the detected issues and jump to the corresponding line in the code editor.

    <img src="qd-ide-plugin-project-errors.png" alt="Project Errors view" width="740" border-effect="line"/>