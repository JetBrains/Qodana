[//]: # (title: Qodana IDE plugin)

The [Qodana IDE plugin](https://plugins.jetbrains.com/plugin/16938-qodana) is a plugin for JetBrains IDEs such as IntelliJ IDEA or PhpStorm. It provides a link between a Qodana report and your project opened in an IDE. With the plugin installed, you can navigate between the issues detected by a linter as well as use the **Open file in \<IDE\>** functionality provided by the [Qodana UI](ui-overview.md).

## Before you start

1. Make sure your preferred IDE is installed via [JetBrains Toolbox App](https://www.jetbrains.com/toolbox-app/).
2. Install the plugin for the IDE as described in the [IntelliJ IDEA Documentation](https://www.jetbrains.com/help/idea/?Managing_Plugins). IDE versions 2021.2 and later are supported.
3. Make sure that you previously opened the project by the IDE at least one time. This action establishes the link 
between the %product% report and your IDE.    

Now you can run %product% to inspect your code, see the [Qodana linters](linters.md) section for details.

## Open a file from the Qodana UI 

1. In the Qodana HTML report, choose a problem to navigate to and click **Open file in \<IDE\>**.

   <img src="qd-report-open-in-ide.png" dark-src="qd-report-open-in-ide_dark.png" alt="The Open in IDE button" width="706" border-effect="line"/>

## Open a Qodana report in the IDE

1. In the IDE, go to **Tools | Show Qodana Analysis Report | Open Qodana Analysis Report** and select the 
`qodana.sarif.json` report file generated after a Qodana run. See [](qodana-inspection-output.md) for details.
2. In the **Problems** tool window that opens, you can view the detected issues and jump to the corresponding line in the code editor.

    <img src="qd-ide-plugin-project-errors.png" alt="Project Errors view" width="740" border-effect="line"/>