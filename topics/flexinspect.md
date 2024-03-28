# FlexInspect

<var name="feature" value="FlexInspect"/>

Starting from version 2024.1 of IntelliJ IDEA, you can employ the %feature% feature to develop your own inspections specific
to your project using IntelliJ IDEA and Kotlin, and run them instantly.

You can develop and run your inspections on the fly to inspect specific files,
execute them once for an entire project using the
[%product% functionality of the IDE](qodana-ide-plugin.md#ide-plugin-run-qodana), and inspect your code
in [CI pipelines](ci.md). Currently, %feature% supports the following languages: Java, Kotlin, JS, TypeScript, 
PHP, Go, Python, Ruby, SQL, XML, CSS, YAML, JSON, SHELL, DOCKERFILE, and MARKDOWN. 

## Prerequisites

Make sure that [IntelliJ IDEA](https://www.jetbrains.com/idea/) is installed on your machine.

If you need to develop inspections for other languages different from Java, in your IntelliJ IDEA you can install a plugin
that provides the language support. You can install plugins for [PHP](https://plugins.jetbrains.com/plugin/6610-php), [Go](https://plugins.jetbrains.com/plugin/9568-go), [Python](https://plugins.jetbrains.com/plugin/631-python) and other languages.

Because all inspections are developed using the Kotlin language, you probably need to learn the 
[basics of Kotlin](https://kotlinlang.org/docs/kotlin-tour-welcome.html).

## How it works

Using your inspections written in Kotlin, IntelliJ IDEA compiles them in runtime and then executes the inspections. 
The inspection code interacts with the [Program Structure Interface](https://plugins.jetbrains.com/docs/intellij/psi.html) 
or PSI. This interface provides the API for interacting with your codebase. In IntelliJ IDEA, PSI is available using the 
**PSI Viewer** tool.  

<img src="flexinspect-how-it-works.png" width="706" alt="PSI tree overview" border-effect="line" thumbnail="true"/>

PSI is an [AST](https://plugins.jetbrains.com/docs/intellij/uast.html) representation of your code corresponding to a 
source file's structure. In case of Java 
code, PSI reflects basic blocks of a Java file like package and import statements, class statements, method invocations, 
and other nodes. %feature% uses the PSI tree representation of your codebase to obtain the list of the codebase nodes 
that can be inspected using your inspections.

IntelliJ IDEA reads `inspection.kts` files from the `inspections` directory of your project, and each file
contains Kotlin code to check your codebase nodes using the API provided by the PSI.   

After you develop your inspections, you can run them over your code with IntelliJ IDEA and %product% right away.

## How to start

This section shows how to create an inspection example that will inspect whether a Java class has a constructor method.

### Create an inspection file

To create a new `inspection.kts` file, follow the procedure below.

<procedure>
<step>In your project, create the <code>inspections</code> directory.</step>
<step>
In the project navigator of IntelliJ IDEA, hover over the <code>inspections</code> directory, right-click the directory, navigate 
to <ui-path>New | Custom Inspection</ui-path>.
</step>
<step>
On the dialog that opens, you can select a template specific to your language, or create an empty 
<code>inspection.kts</code> file. Each file can contain multiple inspections. Camelcase is 
the preferable naming method for <code>inspection.kts</code> files.
</step>
</procedure>

Here is the animation showing how you can create an inspection.

<img src="flexinspect-create-template.gif" width="881" alt="Creating a template inspection" border-effect="line"/>

The created file already contains code examples and explanations, which lets you start to
develop your own inspection. 

### Study the PSI tree of your code

<procedure>
<step>In IntelliJ IDEA, open the file that you would like to inspect using your inspection. </step>
<step>Navigate to <ui-path>Tools | View PSI Structure of Current File</ui-path>. Here you can inspect the PSI tree of your file, APIs 
available for PSI nodes contained in the file, and come up with algorithms that would operate with this PSI tree. 
</step>
</procedure>

For example, to check whether a method is a constructor, you can use the `isConstructor()` PSI method available for 
each method of a class.

<img src="flexinspect-psi-tree.gif" width="881" alt="Studying a PSI tree of a file" border-effect="line"/>

### Create your inspection

You can develop the inspection in the file you have [already created](#Create+an+inspection+file). To check whether
a class has a constructor method, in this example you can iterate over all methods and use the `isConstructor()` method. 
If there is no constructor method, the inspection generate the error showing that a class has no constructor method.

Here is the Kotlin snippet for the `NoConstructor.inspection.kts` file containing inline comments.

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

All changes applied to the inspection are available on the fly for your entire project, so in your IDE you can 
see how your inspection highlights the code checked by the inspection. To see how the new inspection highlights 
results, open a file containing your code.

<img src="flexinspect-test-inspection.gif" width="881" alt="Testing the inspection in IDE" border-effect="line"/>

### Run your custom inspection using %product%

<note>
You need to select a suitable %product% <a href="linters.md">linter</a> to run your custom inspection. For example, for 
PHP it will be the <a href="qodana-php.md"/> linter.
</note>

<note>
If your custom inspection conflicts with a Qodana inspection, and you would still like to run it, you can 
<a href="qodana-yaml.md" anchor="exclude-inspection">disable</a> the Qodana inspection.
</note>

To inspect your entire project with the new inspection locally, run %product% as explained in the 
[](qodana-ide-plugin.md#ide-plugin-run-qodana) section.

<img src="flexinspect-run-qodana-locally.gif" width="881" alt="Running Qodana locally with a new inspection" border-effect="line"/>

To run your custom inspection in a CI pipeline, you can visit the [](ci.md) section and find the instructions for your
CI/CD solution. Because your inspection is already contained in the `inspections` section of your project, it is 
already available for inspecting your code.

You can use the inspection name from the `id` field of the [inspection file](#Create+an+inspection+file)
to [disable or enable](qodana-yaml.md#Example+of+different+configuration+options) your custom inspection in the 
[`qodana.yaml`](qodana-yaml.md) file.
