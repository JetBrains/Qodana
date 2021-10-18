[//]: # (title: TeamCity plugins)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

## List of Qodana plugins available
Qodana plugins for TeamCity are an example of how fine-tuned our linters’ integration into a CI workflow can be.

If you have your own installation of TeamCity, you can install the following Qodana plugins from JetBrains Marketplace:

* [Qodana plugin](https://plugins.jetbrains.com/plugin/15498-qodana): provides the Qodana IntelliJ linter, Qodana UI and extension point for other linters support
* [Clone Finder plugin](https://plugins.jetbrains.com/plugin/16784-qodana-clone-finder): adds the Qodana Clone Finder linter support
* [License Audit plugin](https://plugins.jetbrains.com/plugin/17283-qodana-license-audit):  adds the Qodana License Audit linter support

## Qodana reporting features in TeamCity

After extending your build with Qodana, you’ll get the following capabilities:

- View an interactive report in a separate build tab
- Compare problems and checks applied between builds
- Report discovered problems as standard TeamCity tests so that you can assign investigations to the responsible team members
- Use flexible build failure conditions
- View aggregate statistics for static code analysis metrics

![](tc-plugin.png)

The screenshot above shows a report for failed inspections grouped by type. In this example, 17 problems related to *PhpHierarchyChecksInspections* were grouped together. You can also choose grouping by file or module, or create a separate assignable failed “test” for every problem that is found.

For more about Qodana HTML reports, see the [Qodana Inspection Results](results.md) chapter.
