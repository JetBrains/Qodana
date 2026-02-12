# Create and run Roslyn analyzers

<var name="roslyn-link" value="https://learn.microsoft.com/en-us/visualstudio/code-quality/roslyn-analyzers-overview?view=vs-2022"/>
<var name="ide" value="JetBrains Rider"/>
<var name="roslyn-template" value="https://www.jetbrains.com/help/rider/Creating_and_Opening_Projects_and_Solutions.html"/>

<link-summary>
You can create and run your custom Roslyn analyzers using the %dotnet% linter of %product%
</link-summary>


<show-structure for="chapter" depth="3"/>

You can create and run your custom [Roslyn analyzers](%roslyn-link%) using the [%dotnet%](dotnet.md) linter 
as explained in this section.

## Prerequisites

This section uses [JetBrains Rider](https://www.jetbrains.com/help/rider/Introduction.html) for creating an analyzer template.

## Create a template

In the **New Project** [dialog](%roslyn-template%) of %ide%, create a new solution using the **Roslyn** template of the **Analyzers** type. The created solution
will also contain three separate projects. For example, for the `MyCustomAnalyzer` solution, this will
contain the following projects: 
* `MyCustomAnalyzer` is designed for implementation of the analyzer logic
* `MyCustomAnalyzer.Sample` lets you see how your analyzer operates in real time
* `MyCustomAnalyzer.Tests` lets you write unit tests to verify the correctness of your analyzer

Using the **Solution Explorer** window of %ide%, expand the logic implementation project (`MyCustomAnalyzer` in the example above) 
and make sure that it contains implementations of the `DiagnosticAnalyzer` and `CodeFixProvider` classes. 

<!--
* `SampleSyntaxAnalyzer.cs` focuses on the code syntax looking for patterns or structures that might indicate potential problems
* `SampleSemanticAnalyzer.cs` uses semantic information like symbol tables and type information to identify more complex issues
* `SampleCodeFixProvider.cs` provides code fixes or suggestions to address the issues identified by your analyzer
-->

In the logic implementation project, open the analyzer class derived from the `DiagnosticAnalyzer` class 
(often named as `SampleSyntaxAnalyzer.cs`) and replace its contents with the following sample code that will catch 
empty `catch` statements in your code: 

```c#
using System.Collections.Immutable;
using System.Linq;
using Microsoft.CodeAnalysis;
using Microsoft.CodeAnalysis.CSharp;
using Microsoft.CodeAnalysis.CSharp.Syntax;
using Microsoft.CodeAnalysis.Diagnostics;

namespace MyCustomAnalyzer
{
    [DiagnosticAnalyzer(LanguageNames.CSharp)]
    public sealed class EmptyCatchBlockAnalyzer : DiagnosticAnalyzer
    {
        public const string DiagnosticId = "MCA0001";

        private static readonly DiagnosticDescriptor Rule = new(
            id: DiagnosticId,
            title: "Avoid empty catch blocks",
            messageFormat: "Empty catch block should be avoided",
            category: "Reliability",
            defaultSeverity: DiagnosticSeverity.Warning,
            isEnabledByDefault: true,
            description: "Reports catch clauses with an empty block. Empty catches can hide failures and make debugging harder."
        );

        public override ImmutableArray<DiagnosticDescriptor> SupportedDiagnostics
            => ImmutableArray.Create(Rule);

        public override void Initialize(AnalysisContext context)
        {
            context.ConfigureGeneratedCodeAnalysis(GeneratedCodeAnalysisFlags.None);
            context.EnableConcurrentExecution();

            context.RegisterSyntaxNodeAction(AnalyzeCatchClause, SyntaxKind.CatchClause);
        }

        private static void AnalyzeCatchClause(SyntaxNodeAnalysisContext context)
        {
            var catchClause = (CatchClauseSyntax)context.Node;

            // catch { } or catch (Exception) { }
            var block = catchClause.Block;
            if (block is null)
                return;

            // Ignore non-empty catches
            if (block.Statements.Count != 0)
                return;

            // Ignore catches that have comments inside (often intentionally empty)
            if (block.DescendantTrivia().Any(t => t.IsKind(SyntaxKind.SingleLineCommentTrivia) ||
                                                 t.IsKind(SyntaxKind.MultiLineCommentTrivia)))
                return;

            context.ReportDiagnostic(Diagnostic.Create(Rule, catchClause.CatchKeyword.GetLocation()));
        }
    }
}
```
{collapsible="true"}



## Configure the analyzer project

In the project configuration file, add the following configuration:

```xml
    <PropertyGroup>
    <!-- NuGet Package Configuration -->
    <IsPackable>true</IsPackable>
    <GeneratePackageOnBuild>true</GeneratePackageOnBuild>

    <!-- Prevent the analyzer from being added as a lib reference -->
    <IncludeBuildOutput>false</IncludeBuildOutput>
    <SuppressDependenciesWhenPacking>true</SuppressDependenciesWhenPacking>

  </PropertyGroup>
  
  <!-- Locate the analyzer DLL in the correct package directory -->
  <ItemGroup>
    <None Include="$(OutputPath)\$(AssemblyName).dll" Pack="true" PackagePath="analyzers/dotnet/cs" Visible="false"/>
  </ItemGroup>
```

## Package and run your Roslyn analyzer

Package your analyzer by running the `dotnet pack` utility.

%dotnet% runs Roslyn analyzers under the following conditions: 
* The analyzer is referenced in a solution or project configuration of an analyzed project, for example:
    ```XML
    <ItemGroup>
       <PackageReference Include="MyCustomAnalyzer" Version="1.0.0" />
     </ItemGroup>
     ```
* The analyzer is reachable by build/restore and executed 
* The `nuget.config` file provides access to the package
* Your project is built as described in the [](dotnet.md#dotnet-build-project) chapter
* The %dotnet% linter is going to be executed in the [native mode](deploy-qodana.md#deploy-qodana-native-mode)

Below is a sample %product% configuration:

```yaml
version: 1.0

# Configuring native mode
linter: qodana-dotnet
withinDocker: false  

# Restoring, building and referencing package
bootstrap: |+
  dotnet restore
  dotnet build
  dotnet add package MyCustomAnalyzer --version 1.0.0

dotnet:
  solution: MyProjectSolutionFile.csproj

```

To run your Roslyn analyzer using %product% in %ide%, install your analyzer package by navigating **View | Tool Windows | NuGet**. 



