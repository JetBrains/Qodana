# FlexInspect

<var name="feature" value="FlexInspect"/>

Starting from version 2024.1 of %product%, you can employ the %feature% feature to develop your own inspections specific
to your project using IntelliJ IDEA and Kotlin, and run them instantly.

You can run your inspections using the [](qodana-jvm.md), [](qodana-jvm-community.md), and 
[](qodana-jvm-android.md) linters.

## Prerequisites

Make sure that IntelliJ IDEA and Kotlin are installed on your machine.

Depending on your plans, you probably need to learn the [basics of Kotlin](https://kotlinlang.org/docs/kotlin-tour-welcome.html).

## How it works

The [Program Structure Interface](https://plugins.jetbrains.com/docs/intellij/psi.html) or PSI provides the API for interacting with your codebase.
In IntelliJ IDEA, PSI is available using the **PSI Viewer** tool.  

<img src="flexinspect-how-it-works.png" width="706" alt="PSI tree overview" border-effect="line" thumbnail="true"/>

PSI is a tree representation of the source code elements corresponding to a source file's structure. In case of Java 
code, PSI reflects basic blocks of a Java file like package and import statements, class statements, method invocations, 
and other nodes. %feature% uses the PSI tree representation of your codebase to obtain the list of the codebase nodes 
that can be inspected using your inspections.

%feature% reads `inspection.kts` files from the `inspections` directory in your project, and each `inspection.kts` file
contains Kotlin code to check your codebase nodes using the API provided by the PSI.   

After you develop your inspections, you can run %product% using them right away, without any additional configuration.

## How to start

This section shows how to create an inspection example that will inspect whether a Java class has a constructor method.

### Create an inspection template

To create a new `inspection.kts` template, follow the procedure below.

<procedure>
<step>In your project, create the <code>inspections</code> directory.</step>
<step>
In the project navigator of IntelliJ IDEA, hover over the <code>inspections</code> directory, right-click the directory, navigate 
to <ui-path>New | Custom Inspection</ui-path>.
</step>
<step>
On the dialog that opens, select the inspection type and specify the inspection name.
</step>
</procedure>

Here is the animation showing how to create an inspection template.

<img src="flexinspect-create-template.gif" width="881" alt="Creating a template inspection" border-effect="line"/>

A created template already contains code examples and explanations, which lets you start to
develop your own inspection. 

### Study the list of items to inspect

In your IDE, open a Java file that you would like to develop an inspection for, and then navigate
to **Tools | View PSI Structure of Current File**. 

<img src="flexinspect-psi-tree.gif" width="881" alt="Studying a PSI tree of a file" border-effect="line"/>

To check whether a method is a constructor, you can use the `isConstructor()` PSI method available for each method of 
a class. 

### Modify the inspection template to your needs

You can modify the inspection template that you have [already created](#Create+an+inspection+template). To check whether
a class has a constructor method, you can iterate over all methods and use the `isConstructor()` method. If there is no
constructor method, the inspection generate the error showing that a class has no constructor method.

Here is the Kotlin snippet for the `noConstructor.inspection.kts` file containing inline comments.

```kotlin
import org.intellij.lang.annotations.Language
import com.intellij.psi.JavaElementVisitor
import com.intellij.psi.PsiClass

/**
 * Full HTML description of inspection: Describe here motivation, examples, etc.
 */
@Language("HTML")
val htmlDescription = """
    <html>
    <body>
        A class has no constructor
    </body>
    </html>
""".trimIndent()

val noConstructorInspection = localInspectionKts { inspection ->
    object : JavaElementVisitor() {
        override fun visitClass(aClass: PsiClass) {
            super.visitClass(aClass)

            // Ignore interfaces
            if (aClass.isInterface) {
                return
            }
            // Iterate all methods of a class
            for (method in aClass.methods) {
                if (method.isConstructor) {
                    return
                }
            }
            // Class method for the error message
            val className = aClass.getQualifiedName()
            // Generate the error message
            val message = "The class $className has no constructor"
            inspection.registerProblem(aClass, message)
        }
    }
}

listOf(
        InspectionKts(
                id = "NoConstructorInClass", // Inspection id (used in qodana.yaml)
                localTool = noConstructorInspection,
                name = "The class has no constructor", // Inspection name, displayed in UI
                htmlDescription = htmlDescription,
                level = HighlightDisplayLevel.WARNING, // Inspection severity
        )
)

```
{collapsible="true"}

### Test your inspection in the IDE

All changes applied to the inspection template are available on the fly for your entire project, so in your IDE you can 
see how your inspection outlines the code fragment checked by the inspection.

<img src="flexinspect-test-inspection.gif" width="881" alt="Testing the inspection in IDE" border-effect="line"/>

### Run your custom inspection using %product%

To inspect your code with the new inspection locally, run %product% as explained in the 
[](qodana-ide-plugin.md#ide-plugin-run-qodana) section.

<img src="flexinspect-run-qodana-locally.gif" width="881" alt="Running Qodana locally with a new inspection" border-effect="line"/>

To run your custom inspection in a CI pipeline, you can visit the [](ci.md) section and find the description for your
CI/CD solution. Because your inspection is already contained in the `inspections` section of your project, it is 
already available for inspecting your code. 

To configure your inspection in the `qodana.yaml` file, you can use the inspection name from 
the `id` field of the [inspection template](#Modify+the+inspection+template+to+your+needs) as shown in the [](qodana-yaml.md#exclude-paths) and 
[](qodana-yaml.md#Include+an+inspection+into+the+analysis+scope) sections.

<!-- Is flexInspect FAQ required here? -->