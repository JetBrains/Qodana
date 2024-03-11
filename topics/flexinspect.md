# FlexInspect

<var name="feature" value="FlexInspect"/>

Starting from version 2024.1 of %product%, you can use the %feature% feature to develop your own inspections in 
IntelliJ IDEA. %feature% uses the API of JetBrains IDEs and provides a flexible way for developing your own inspections 
and seeing results on the fly.

You can develop your inspections using Kotlin and run your solutions using the [](qodana-jvm.md), [](qodana-jvm-community.md), and 
[](qodana-jvm-android.md) linters.

## Prerequisites

Make sure that you have IntelliJ IDEA and Kotlin installed on your machine.

## How it works

While developing your inspections, you can use the [PSI](https://plugins.jetbrains.com/docs/intellij/psi.html) or Program Structure Interface representation of the source 
code as a tree of elements corresponding to a source file's structure. In case of Java code, this reflects 
basic blocks of a Java file like package and import statements, class statements, method invocations, and others. In 
IntelliJ IDEA, PSI is implemented in form of a PSI tree available via the **PSI Viewer** tool.

%product% uses the inspection files with the `inspection.kts` extension saved in the `inspections` directory of your 
project.

## How to start

<procedure>
<step>In your project, create the <code>inspections</code> directory.</step>
<step>
In the project navigator of IntelliJ IDEA, hover over the <code>inspections</code> directory, right-click the directory, navigate 
to <ui-path>New | Custom Inspection</ui-path>.
</step>
<step>
On the dialog that opens, click <ui-path>Java local inspection</ui-path> and specify the inspection name.
</step>
</procedure>

<img src="flexinspect-intro.gif" width="706" alt="Creating a template inspection" border-effect="line"/>

This template already contains code examples and explanations, which lets you start 
developing your own inspection. All inspection files have the `inspection.kts` extension.

In your IDE, open a Java file in your project that you would like to inspect with your custom inspection, and then navigate
to **Tools | View PSI Structure of Current File**. You will be able to see the PSI elements contained in the file. 

<!-- Here a short video needs to be created -->

All changes made to the inspection template are available on the fly, so you can see how your inspection already works.

After you finish inspection development, it becomes available for the entire project. The inspection code will be run 
on each element of the file's PSI tree if a specific PSI entity type suits the inspection criterion.

### Run your custom inspection in %product%

To inspect your code with the new inspection locally, run %product% as explained in the 
[](qodana-ide-plugin.md#ide-plugin-run-qodana) section.

To run your custom inspection in a CI pipeline, 
<!-- How does this work ?-->

<!-- Link to the examples on GitHub needs to be provided -->