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

- Access the [PSI](https://plugins.jetbrains.com/docs/intellij/psi.html) representation of the source code.
- Debug new inspections on the fly.
- Observe your new custom inspections in action, including the highlighting of code fragments that don't behave as expected.

With %feature%, you get access to the same API that is used by all 
IntelliJ IDEA and %product% inspections. This allows you to run these inspections on your entire project using %product% 
to ensure that your entire team follows the standards defined by you.

You can develop local inspections that run within a file scope and global inspections that run within a project scope
as described in the [](qodana-ide-plugin.md#ide-plugin-run-qodana) section, and you can even inspect your code
in [CI pipelines](ci.md). Currently, %feature% supports any language covered by IntelliJ IDEA either natively or through 
additional plugins. For example, Java, Kotlin, JavaScript, TypeScript, PHP, Go, Python, Ruby, SQL, XML, CSS, YAML, JSON, Shell, 
and Dockerfile are supported. 

## Prerequisites

Start by verifying that [IntelliJ IDEA](https://www.jetbrains.com/idea/) is installed on your machine.

Then, ensure that your version of IntelliJ IDEA supports the language for which you want to develop an inspection. Out of the box, 
IntelliJ IDEA supports Java and [Kotlin](%kotlin%). The Ultimate edition of 
IntelliJ IDEA also provides default support for [JavaScript](%js%) and [TypeScript](%ts%). To get support for 
other languages like [PHP](https://plugins.jetbrains.com/plugin/6610-php), [Go](https://plugins.jetbrains.com/plugin/9568-go), and [Python](https://plugins.jetbrains.com/plugin/631-python), you can install plugins from 
[JetBrains Marketplace](https://plugins.jetbrains.com/). More detailed information about language support is available via the 
[IntelliJ IDEA](%idea-doc%) documentation portal.   

Since all inspections are developed using the Kotlin language, you'll need to know the 
[basics of Kotlin](https://kotlinlang.org/docs/kotlin-tour-welcome.html) before you can begin developing your own inspections.

## How it works

You write your inspections in Kotlin and store them in the `inspections` directory of your project as
`.inspection.kts` files. Each `.inspection.kts` file contains Kotlin code that is used to check your code using the API provided 
by the [Program Structure Interface](https://plugins.jetbrains.com/docs/intellij/psi.html)
or PSI. IntelliJ IDEA reads `.inspection.kts` files, compiles the inspection code on the fly, and then 
executes the compiled inspections. 

### Program Structure Interface (PSI)

The PSI is an [AST](https://plugins.jetbrains.com/docs/intellij/uast.html) representation of your code corresponding to a
source file's structure. In the case of Java code, the PSI reflects the basic blocks of a Java file like package and import
statements, class statements, method invocations, and other nodes. %feature% uses the PSI tree representation of your
code to obtain the list of the code nodes that can be inspected using your inspections.

In IntelliJ IDEA, you can navigate through the PSI using the **PSI Viewer** tool window. To do this, open a file that 
you would like to view with the **PSI Viewer**, and then navigate to **Tools | View PSI Structure of Current File**.

<img src="flexinspect-how-it-works.png" width="706" alt="PSI tree overview" border-effect="line" thumbnail="true"/>


## Inspection types

<link-summary>You can create local and global inspections to run them within file and project scopes respectively.</link-summary>

With IntelliJ IDEA, you can create both local and global inspections.

Local inspections operate on the file level and inspect each file of your project individually. 
Once you create a local inspection, IntelliJ IDEA will run it on any file opened in the editor.

Global inspections operate on the project level and use the project scope as a basis for inspection. For example, you can create 
inspections that can check whether specific files exist in your project. See the [](qodana-ide-plugin.md#ide-plugin-run-qodana) 
section of the documentation for more information about how to run global inspections.

## How to start

This section shows how to create an example inspection that will inspect whether a Java class has a constructor method.

### Create an inspection file

To create a new `.inspection.kts` template file, follow the procedure below.

<procedure>
<step>In your project, create an <code>inspections</code> directory.</step>
<step>
In the project navigator of IntelliJ IDEA, hover over the <code>inspections</code> directory, right-click on the directory, 
and then navigate to <ui-path>New | Custom Inspection</ui-path>.
</step>
<step>
<p>In the resultant dialog, you can choose from among various <a anchor="Inspection+types">local and global</a> inspection templates 
that you can use as a basis for your inspection. Empty local and global templates are universal for any language supported by %feature%,
while the local Java, Kotlin, JavaScript, and Typescript templates are language-specific.</p> 

<p>Note that each file can contain multiple inspections, and CamelCase is the preferred naming method for <code>.inspection.kts</code> 
files.</p>
</step>
</procedure>

Here's an animation showing you how to create an inspection following the above method.

<img src="flexinspect-create-template.gif" width="881" alt="Creating a template inspection" border-effect="line"/>

The created file already contains code examples and explanations, which you can then use to
develop your own inspection. 

### Study the PSI tree of your code

<procedure>
<step>In IntelliJ IDEA, open the file that you would like to analyze using your inspection. </step>
<step>Navigate to <ui-path>Tools | View PSI Structure of Current File</ui-path>. Here, you can explore the PSI tree of 
your file. APIs are available for PSI nodes contained in the file. These APIs can generate algorithms that would operate 
within the PSI tree. 
</step>
</procedure>

For example, to check whether a method is a constructor, you can use the `isConstructor()` PSI method, which is available 
for each method of a class.

<img src="flexinspect-psi-tree.gif" width="881" alt="Studying a PSI tree of a file" border-effect="line"/>

### Create your inspection

You can develop your inspection using the template that you've [already created](#Create+an+inspection+file). In this example, you can iterate 
over all methods and use the `isConstructor()` method to check whether a class has a constructor method. 
If there is no constructor method, the inspection generates an error showing that a class has no constructor method.

Here's the Kotlin snippet for the `NoConstructor.inspection.kts` file containing inline comments.

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
inspection code and view the resultant debug message in your IDE.

### Test your inspection in the IDE

After creating the inspection, you can see the compilation status on the toolbar in the upper part of the inspection file. 
When you change the inspection code, you need to explicitly recompile the inspection using the recompile button in the 
left part of the toolbar or use the <shortcut>Alt+Shift+Enter</shortcut> (Windows) or <shortcut>⌥⇧↩</shortcut> (macOS) shortcut.  
You can also open files using the **PSI Viewer** and study inspection examples.

<img src="flexinspect-test-your-inspection.png" width="706" alt="FlexInspect toolbar" border-effect="line"/>

To see how the new inspection functions on your code, open a file containing a problem the inspection is 
supposed to highlight.

<img src="flexinspect-test-inspection.gif" width="881" alt="Testing the inspection in IDE" border-effect="line"/>

### Run your custom inspection using %product%

<note>
Before you can run your inspection, you'll first need to select a suitable %product% <a href="linters.md">linter</a>. 
For example, for PHP, this will be the <a href="qodana-php.md"/> linter.
</note>

<note>
If your custom inspection conflicts with a %product% inspection, and you would still like to run it, you can 
<a href="qodana-yaml.md" anchor="exclude-inspection">disable</a> the relevant %product% inspection.
</note>

%feature% is supported by the [default inspection profiles](inspection-profiles.md#Default+profiles).

To inspect your entire project with the new inspection locally, run %product% as explained in the 
[](qodana-ide-plugin.md#ide-plugin-run-qodana) section.

<img src="flexinspect-run-qodana-locally.gif" width="881" alt="Running Qodana locally with a new inspection" border-effect="line"/>

To run your custom inspection in a CI pipeline, you can visit the [](ci.md) section and find the instructions for your
specific CI/CD solution. Because your inspection is already contained in the `inspections` directory of your project, it's 
already available for inspecting your code.

You can use the inspection name from the `id` field of the [inspection file](#Create+an+inspection+file)
to [disable or enable](qodana-yaml.md#Example+of+different+configuration+options) your custom inspection in the 
[`qodana.yaml`](qodana-yaml.md) file.
