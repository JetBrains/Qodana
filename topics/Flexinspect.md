# Flexinspect

Starting from version 2024.1 of %product%, you can use the flexInspect feature to develop your own inspections in 
IntelliJ IDEA using the API of JetBrains IDEs. This feature provides a flexible way for developing your own inspections, 
and you don't have to develop a complete plugin anymore.

You can develop new inspections using Kotlin.

## Prerequisites

Make sure that you have a IntelliJ IDEA and Kotlin installed on your machine.

You may also need to install the `PsiViewer` plugin.

## How it works

To develop your custom inspection, you may need to use a PSI representation while developing a file containing the code of the inspection.

The [PSI](https://plugins.jetbrains.com/docs/intellij/psi.html) or Program Structure Interface creates a representation 
of the source code as a tree of elements corresponding to a source file's structure. In case of Java code, this reflects 
basic blocks of a Java file like package and import statements, class statements, and method invocations. In 
IntelliJ IDEA, PSI is implemented in form of a PSI tree available via the **PSI Viewer** tool.

To run custom inspections, %product% uses files saved in the `inspections` directory of your project.

## How to start

In your project, create the `inspections` directory. 

In the project navigator in your IDE, right-click the `inspections` directory, navigate to **New | Custom Inspection**
to create an inspection template. This template already contains code examples and explanations, which lets you start 
developing your own inspection. All inspection files have the `inspection.kts` extension.

In your IDE, open a Java file in your project that you would like to inspect with your custom inspection, and then open 
the PSI Viewer. You will be able to see the PSI elements contained in the file. 

All changes made to the inspection template are available on the fly, so you can see how your inspection already works.

After you finish inspection development, it becomes available for the entire project. The inspection code will be run 
on each element of the file's PSI tree if a specific PSI entity type suits the inspection criterion.

### Run your custom inspection in %product%

To inspect your code with the new inspection locally, run %product% as explained in the 
[](qodana-ide-plugin.md#ide-plugin-run-qodana) section.

To run your custom inspection in a CI pipeline, 
<!-- How does this work ?-->

<!-- Link to the examples on GitHub needs to be provided -->