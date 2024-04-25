# FlexInspect

<var name="feature" value="FlexInspect"/>
<var name="kotlin" value="https://www.jetbrains.com/help/idea/get-started-with-kotlin.html"/>
<var name="js" value="https://www.jetbrains.com/help/idea/javascript-specific-guidelines.html"/>
<var name="ts" value="https://www.jetbrains.com/help/idea/typescript-support.html"/>
<var name="idea-doc" value="https://www.jetbrains.com/help/idea/getting-started.html"/>

<link-summary>
Starting from version 2024.1 of IntelliJ IDEA, you can develop your own inspections specific to your project using the
IntelliJ API and Kotlin.
</link-summary>

Starting from version 2024.1 of IntelliJ IDEA, you can develop your own inspections specific to your project using the 
[IntelliJ API](https://plugins.jetbrains.com/docs/intellij/code-inspections.html#inspection-implementation-java-class) and Kotlin. You can:

- Access the [PSI](https://plugins.jetbrains.com/docs/intellij/psi.html) representation of the source code,
- Debug new inspections on the fly,
- Observe your new custom inspections in action including highlighting of the code fragments that do not meet expected behavior.

Using %feature%, you can get access to the same API that is used by all 
IntelliJ IDEA and %product% inspections, and run these inspections on your entire project using %product% to ensure that 
your entire team follows the standards defined by you.

You can develop local inspections that run within a file scope, global inspections that run within a project scope
as described in the [](qodana-ide-plugin.md#ide-plugin-run-qodana) section, and inspect your code
in [CI pipelines](ci.md). Currently, %feature% supports any language covered by IntelliJ IDEA either natively or through 
additional plugins. For example, Java, Kotlin, JS, TypeScript, PHP, Go, Python, Ruby, SQL, XML, CSS, YAML, JSON, SHELL, 
and DOCKERFILE are supported. 

## Prerequisites

Make sure that [IntelliJ IDEA](https://www.jetbrains.com/idea/) is installed on your machine.

Ensure that your version of IntelliJ IDEA supports the language you want to develop an inspection for. Out of the box, 
IntelliJ IDEA supports Java and [Kotlin](%kotlin%). The Ultimate edition of 
IntelliJ IDEA also provides the default support for [JavaScript](%js%) and [TypeScript](%ts%). To provide support for 
other languages like [PHP](https://plugins.jetbrains.com/plugin/6610-php), [Go](https://plugins.jetbrains.com/plugin/9568-go), and [Python](https://plugins.jetbrains.com/plugin/631-python), you can install plugins from 
[JetBrains Marketplace](https://plugins.jetbrains.com/). The detailed information is available on the 
[IntelliJ IDEA](%idea-doc%) documentation portal.   

Because all inspections are developed using the Kotlin language, you need to know the 
[basics of Kotlin](https://kotlinlang.org/docs/kotlin-tour-welcome.html).

## How it works

You write your inspections in Kotlin and store them in the `inspections` directory of your project as
`.inspection.kts` files. Each `.inspection.kts` file contains Kotlin code to check your code using the API provided 
by the [Program Structure Interface](https://plugins.jetbrains.com/docs/intellij/psi.html)
or PSI. IntelliJ IDEA reads `.inspection.kts` files, compiles the inspection code on the fly, and then 
it executes compiled inspections. 

### Program Structure Interface (PSI)

PSI is an [AST](https://plugins.jetbrains.com/docs/intellij/uast.html) representation of your code corresponding to a
source file's structure. In case of Java code, PSI reflects basic blocks of a Java file like package and import
statements, class statements, method invocations, and other nodes. %feature% uses the PSI tree representation of your
code to obtain the list of the code nodes that can be inspected using your inspections.

In IntelliJ IDEA, you can navigate through PSI via the **PSI Viewer** tool. To do it, in IntelliJ IDEA you can 
open a file that you would like to view with **PSI Viewer**, and then navigate to **Tools | View PSI Structure of Current File**.

<img src="flexinspect-how-it-works.png" width="706" alt="PSI tree overview" border-effect="line" thumbnail="true"/>


## Inspection types

<link-summary>You can create local and global inspections to run them within file and project scopes respectively.</link-summary>

You can create local and global inspections.

A local inspection operates on a file level and inspects each file of your project separately from 
others. Once you create a local inspection, IntelliJ IDEA will run it for an opened file in the editor.

A global inspection operates on a project level using the project scope for inspection. For example, you can create 
inspections that can check whether specific files exist in your project. You can run global inspections as described
in the [](qodana-ide-plugin.md#ide-plugin-run-qodana) section.

## How to start

This section shows how to create an inspection example that will inspect whether a Java class has a constructor method.

### Create an inspection file

To create a new `.inspection.kts` template file, follow the procedure below.

<procedure>
<step>In your project, create the <code>inspections</code> directory.</step>
<step>
In the project navigator of IntelliJ IDEA, hover over the <code>inspections</code> directory, right-click the directory, navigate 
to <ui-path>New | Custom Inspection</ui-path>.
</step>
<step>
<p>On the dialog that opens, you can choose among the <a anchor="Inspection+types">local and global</a> inspection templates 
that you can use for your inspection. Empty local and global templates are universal for any language supported by %feature%,
while local Java, Kotlin, JavaScript and Typescript templates are dedicated to these languages.</p> 

<p>Each file can contain multiple inspections. CamelCase is the preferable naming method for <code>.inspection.kts</code> 
files.</p>
</step>
</procedure>

Here is the animation showing how you can create an inspection.

<img src="flexinspect-create-template.gif" width="881" alt="Creating a template inspection" border-effect="line"/>

The created file already contains code examples and explanations, which lets you start to
develop your own inspection. 

### Study the PSI tree of your code

<procedure>
<step>In IntelliJ IDEA, open the file that you would like to analyze using your inspection. </step>
<step>Navigate to <ui-path>Tools | View PSI Structure of Current File</ui-path>. Here you can explore the PSI tree of 
your file, APIs available for PSI nodes contained in the file, and come up with algorithms that would operate with this 
PSI tree. 
</step>
</procedure>

For example, to check whether a method is a constructor, you can use the `isConstructor()` PSI method available for 
each method of a class.

<img src="flexinspect-psi-tree.gif" width="881" alt="Studying a PSI tree of a file" border-effect="line"/>

### Create your inspection

You can develop the inspection using the template that you have [already created](#Create+an+inspection+file). To check whether
a class has a constructor method, in this example you can iterate over all methods and use the `isConstructor()` method. 
If there is no constructor method, the inspection generates the error showing that a class has no constructor method.

Here is the Kotlin snippet for the `NoConstructor.inspection.kts` file containing inline comments.

```kotlin
import org.intellij.lang.annotations.Language
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

val noConstructor = localInspection { psiFile, inspection ->
    val classes = psiFile.descendantsOfType<PsiClass>()
    classes.forEach { clazz ->
        // Ignore interfaces
        if (clazz.isInterface) {
            return@forEach
        }

        // Iterate all methods of a class, check if there is a constructor
        val hasConstructor = clazz.methods.any { method -> method.isConstructor }
        if (hasConstructor) {
            return@forEach
        }

        val className = clazz.qualifiedName
        val message = "The class $className has no constructor"
        inspection.registerProblem(clazz, message)
    }
}

listOf(
        InspectionKts(
                id = "NoConstructor", // inspection id (used in qodana.yaml)
                localTool = noConstructor,
                name = "The class has no constructor", // Inspection name, displayed in UI
                htmlDescription = htmlDescription,
                level = HighlightDisplayLevel.WARNING,
        )
)
```
{collapsible="true"}

> To debug your inspections, you can add `inspection.registerProblem(<psi-element>, "<debug-message>")` to the 
inspection code and view a debug message in your IDE.

### Test your inspection in the IDE

After creating the inspection, you can see the compilation status on the toolbar in the upper part of the inspection file. 
When you change the inspection code, you need to explicitly recompile the inspection using the recompile button in the 
left part of the toolbar, or use the <shortcut>Alt+Shift+Enter</shortcut> / <shortcut>⌥⇧Enter</shortcut> shortcut.  
You can also open files using **PSI Viewer** and study inspection examples.

<img src="flexinspect-test-your-inspection.png" width="706" alt="FlexInspect toolbar" border-effect="line"/>

To see how the new inspection functions on your code, open a file containing a problem the inspection is 
supposed to highlight.

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

%feature% is supported by the [default inspection profiles](inspection-profiles.md#Default+profiles).

To inspect your entire project with the new inspection locally, run %product% as explained in the 
[](qodana-ide-plugin.md#ide-plugin-run-qodana) section.

<img src="flexinspect-run-qodana-locally.gif" width="881" alt="Running Qodana locally with a new inspection" border-effect="line"/>

To run your custom inspection in a CI pipeline, you can visit the [](ci.md) section and find the instructions for your
CI/CD solution. Because your inspection is already contained in the `inspections` directory of your project, it is 
already available for inspecting your code.

You can use the inspection name from the `id` field of the [inspection file](#Create+an+inspection+file)
to [disable or enable](qodana-yaml.md#Example+of+different+configuration+options) your custom inspection in the 
[`qodana.yaml`](qodana-yaml.md) file.
