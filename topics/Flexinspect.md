# Flexinspect

Starting from version 2024.1 of %product%, you can use the flexInspect feature to develop your own inspections using the API of 
JetBrains IDEs. This feature provides you a flexible way for developing your own inspections, and you don't have to develop
a complete plugin anymore.

## Before you start

Because all inspections should be developed using Kotlin, make sure that you have a IntelliJ IDEA installed on your machine. 
In addition to the %product% license, you will need to buy an IntelliJ IDEA license.

In IntelliJ IDEA, you may need to install the `PsiViewer` plugin.

## How it works

Using a PSI tree of your codebase, you can develop your own inspections using Kotlin.

A PSI tree is a structure of a file with your code containing basic blocks of the file like package and import statements,
class statements, and other entities. A PSI tree works as a tool for developing your inspections.

## How to start

Open a file that you would like to inspect with your new inspection.

To start working with a PSI tree, you need to open a PSI viewer. To do it, 

In your IDE, create a new template inspection, a file with the `inspection.kts` extension that will contain the 
code of your inspection that will interact with the IntelliJ IDEA API. 
Save this file to the `inspections` directory of your project.

<!-- PsiViewer is the plugin name -->

After opening the file, open the PSI tree of that file that will describe your codebase. Learn how your codebase will
be inspected.

After you checked the PSI tree and inspection you developed for inspecting your file, you can run the developed inspection
using %product%.

<!-- How can I run a new inspection using Qodana? -->

### What a PSI tree contains

<!-- Need to describe what a PSI tree contains -->

<!-- Example of a codebase and inspection for it are required, with explanations. -->

<!-- Explanation of how to develop an inspection using a specific example needs to be provided -->

<!-- Where can I take template inspections? Where can I take it? This needs to be added here -->



Through the API the user works with the PSI tree. PSI tree is a structure of a file containing code, and it contains
basic blocks of the file like package and import statements, class statement and so on.
And inspection code interacts with the PSI tree of specific code. Using Kotlin.
The inspection code will be run on each node of the file's PSI tree if a specific PSI entity type suits the inspection criterion.
This is specified with the expression in brackets.
Using the PSI tree, I can see which methods to invoke. And how to develop the inspection.
The idea is to iterate over a PSI tree and do something useful there.

### Add a new inspection to your CI pipelines

<!-- How can this be added to CI pipelines? -->

### 