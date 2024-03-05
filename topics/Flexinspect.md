# Flexinspect

Starting from version 2024.1 of %product%, you can use the flexInspect feature to develop your own inspections in 
IntelliJ IDEA using the API of JetBrains IDEs. This feature provides a flexible way for developing your own inspections, 
and you don't have to develop a complete plugin anymore.

You can develop new inspections using Kotlin.

## Prerequisites

Make sure that you have a IntelliJ IDEA and Kotlin installed on your machine.

You may also need to install the `PsiViewer` plugin.

## How it works

### PSI tree

You can develop your inspections using information provided by a [PSI](https://plugins.jetbrains.com/docs/intellij/psi.html) tree.
The Program Structure Interface, commonly referred to as just PSI, is the layer in the IntelliJ Platform responsible for 
parsing files and creating the syntactic and semantic code model that powers so many of the platform's features.
In this case, it reflects basic blocks of the file like package and import statements,
class statements, and other entities that let you interact with the IntelliJ IDEA API. Using the PSI tree, for example, 
you can see which methods to invoke, and iterate over a PSI tree.
A PSI tree works as a tool for developing your inspections.

A PSI (Program Structure Interface) file represents a hierarchy of PSI elements (so-called PSI trees).

### Inspection file

To run your inspection, you need to save an inspection file in the `inspections` directory of your project. %product%
will use this file to inspect your code locally or 

## How to start

In your project, create the `inspections` directory. 

In the project navigator in your IDE, right-click the `inspections` directory, navigate to **New | Custom Inspection**
to create an inspection template. This template already contains all information required for developing your own
inspection. 

In your IDE, open a file that you would like to inspect, and navigate to the PSI Viewer to see the nodes of it.

After you checked the PSI tree and inspection you developed for inspecting your file, you can run the developed inspection
using %product%. In this case, the inspection code will interact with the PSI tree nodes of specific code. 

After you finish editing your inspection template, the new inspection becomes available for the entire project. 
All you need in this case it to contain the inspection file in the `inspections` directory, and everything will be 
applied on the fly. The inspection code will be run on each node of the file's PSI tree if a specific PSI entity type 
suits the inspection criterion.

### Run your custom inspection in %product%

To inspect your code with the new inspection locally, run %product% as explained in the 
[](qodana-ide-plugin.md#ide-plugin-run-qodana) section.

To run your custom inspection in a CI pipeline, 
<!-- How does this work ?-->

<!-- Link to the examples on GitHub needs to be provided -->