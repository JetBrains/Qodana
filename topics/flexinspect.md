# FlexInspect

<var name="feature" value="FlexInspect"/>

Starting from version 2024.1 of %product%, you can employ the %feature% feature to develop your own inspections using 
IntelliJ IDEA and Kotlin. Each inspection is a Kotlin file contained in your project and available on the fly.

You can run your inspections using the [](qodana-jvm.md), [](qodana-jvm-community.md), and 
[](qodana-jvm-android.md) linters.

## Prerequisites

Make sure that IntelliJ IDEA and Kotlin are installed on your machine.

## How it works

The [PSI](https://plugins.jetbrains.com/docs/intellij/psi.html) or Program Structure Interface is a tree representation of the source code elements corresponding to a 
source file's structure. In case of Java code, this reflects basic blocks of a Java file like package and import 
statements, class statements, method invocations, and other nodes. %feature% uses the PSI tree representation of your 
codebase to obtain the list of the codebase nodes that can be inspected using your inspections.

%feature% reads `inspection.kts` files contained in the `inspections` directory of your project. Each inspection file 
in this directory uses the existing PSI tree representation of your codebase to inspect various nodes of it.  

Once ready, you can run %product% using your inspections right away, without any additional configuration.

## How to start

### Create an inspection template

To create a new inspection draft, follow the procedure below.

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

Here is the video showing how to create an inspection template.

<img src="flexinspect-intro.gif" width="706" alt="Creating a template inspection" border-effect="line"/>

This template already contains code examples and explanations, which lets you start 
developing your own inspection. All inspection files have the `inspection.kts` extension.

### Study the list of items to inspect

In your IDE, open a Java file in your project that you would like to develop your inspection for, and then navigate
to **Tools | View PSI Structure of Current File**. 

<!-- I can probably adapt this section to the next subsection -->

<img src="flexinspect-psi-tree.gif" width="881" alt="Studying a PSI tree of a file" border-effect="line"/>

Here, you can see the PSI elements contained in the file and choose the nodes you would like to inspect. 

### Modify the inspection template to your needs

After you create an inspection template and study the elements of your codebase, you can develop your 
inspections that invoke these elements and check them against specific conditions. 

All changes made to the inspection template are available on the fly, so you can see how your inspection already working.

After you finish inspection development, it becomes available for the entire project. The inspection code will be run 
on each element of the file's PSI tree if a specific PSI entity type suits the inspection criterion.

### Run your custom inspection in %product%

To inspect your code with the new inspection locally, run %product% as explained in the 
[](qodana-ide-plugin.md#ide-plugin-run-qodana) section.

To run your custom inspection in a CI pipeline, you can visit the [](ci.md) section and find the description for your
CI/CD solution. Because your inspection is already contained in the `inspections` section of your project, it is 
available for inspecting your code. 

To be able to configure your inspection in the `qodana.yaml` file, you can use the inspection name from 
the inspection template as shown in the [](qodana-yaml.md#exclude-paths) and 
[](qodana-yaml.md#Include+an+inspection+into+the+analysis+scope) sections.


<!-- Link to the examples on GitHub needs to be provided -->