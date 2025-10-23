# Analyze code using Roslyn analyzers

<var name="roslyn-link" value="https://learn.microsoft.com/en-us/visualstudio/code-quality/roslyn-analyzers-overview?view=vs-2022"/>
<var name="ide" value="JetBrains Rider"/>
<var name="roslyn-template" value="https://www.jetbrains.com/help/rider/Creating_and_Opening_Projects_and_Solutions.html"/>

<link-summary>
You can create and run your custom Roslyn analyzers using the %dotnet% linter of %product%
</link-summary>


<show-structure for="chapter" depth="3"/>

You can create and run your custom [Roslyn analyzers](%roslyn-link%) using the [%dotnet%](dotnet.md) linter of %product% 
as explained in this section.

## Prerequisites

This section uses [JetBrains Rider](https://www.jetbrains.com/help/rider/Introduction.html) for creating analyzer 
templates.

## Create a template

In the **New Project** [dialog](%roslyn-template%) of %ide%, create a new solution using the **Roslyn** template. The created solution
will also contain three separate projects. For example, for the `MyCustomAnalyzer` solution, this will
contain the following projects: 
* `MyCustomAnalyzer` is designed for implementation of the analyzer logic
* `MyCustomAnalyzer.Sample` lets you see how your analyzer interacts with real-world code examples, helping you fine-tune its behavior
* `MyCustomAnalyzer.Tests` lets you write unit tests to verify the correctness of your analyzer

Using the Explorer window of your %ide%, expand the logic implementation project (`MyCustomAnalyzer` in the example above) and make sure that it contains the following classes:  

* `SampleCodeFixProvider.cs` provides code fixes or suggestions to address the issues identified by your analyzer
* `SampleSemanticAnalyzer.cs` uses semantic information like symbol tables and type information to identify more complex issues
* `SampleSyntaxAnalyzer.cs` focuses on the code syntax looking for patterns or structures that might indicate potential problems

In the logic implementation project, open the `SampleSyntaxAnalyzer.cs` file and paste the following code into it: 

```c#
// 1. Define constants for identification

public const string CompanyName = "company";
public const string DiagnosticId = "BreakStatementInspection";

// 2. Create the DiagnosticDescriptor class

private static readonly DiagnosticDescriptor Rule = new(
    DiagnosticId,
    "Avoid 'break' statements outside 'switch'",
    "'break' statement found outside of a 'switch' statement",
    "Control Flow",
    DiagnosticSeverity.Warning,
    isEnabledByDefault: true,
    description: "This inspection enforces to use break statements only in switch cases.");

// 3. Specify the SupportedDiagnostics variable

public override ImmutableArray<DiagnosticDescriptor> SupportedDiagnostics => ImmutableArray.Create(Rule);

// 4. Implement the Initialize method

public override void Initialize(AnalysisContext context)
    {       context.ConfigureGeneratedCodeAnalysis(GeneratedCodeAnalysisFlags.None);
        context.EnableConcurrentExecution();
        context.RegisterSyntaxNodeAction(AnalyzeBreakStatement, SyntaxKind.BreakStatement);
    }

// 5. Implement the Core Logic in AnalyzeBreakStatement

private void AnalyzeBreakStatement(SyntaxNodeAnalysisContext context)
{
    var breakStatement = (BreakStatementSyntax)context.Node;
    var switchStatement = breakStatement.Ancestors().OfType<SwitchStatementSyntax>().FirstOrDefault();

    if (switchStatement == null) // Not within a switch
    {
        var diagnostic = Diagnostic.Create(Rule, breakStatement.BreakKeyword.GetLocation());
        context.ReportDiagnostic(diagnostic);
    }
}
```

## Package and run your Roslyn analyzer

To package your analyzer in a NuGet package, use the `dotnet pack` utility.

Before running %product%, make sure that the following prerequisites are met: 

1. The %dotnet% linter is going to be executed in the [native mode](deploy-qodana.md#deploy-qodana-native-mode) or provide credentials within the `nuget.config` file
2. Your project is built as described in the [](dotnet.md#dotnet-build-project) chapter of the %dotnet% section

To run your Roslyn analyzer using %product%, in your %ide% install the NuGet package containing your analyzer using
the IDE built-in package or the `dotnet add package` command. 



