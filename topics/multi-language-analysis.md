# Multi-language analysis

<link-summary>This manual provides instructions and guidance on using Multi-language analysis within Qodana, 
including troubleshooting and configuration tips based on known behaviors.</link-summary>

Multi-language analysis is a powerful, fast, and reliable static analysis engine integrated into Qodana. 
It supports multiple languages and is designed for high-performance analysis, including taint analysis (DFA).

## Key Features

### Multi-Language Support
Multi-language analysis supports analysis for various languages, including Java, .NET, JavaScript, TypeScript, and others. 
    It performs deep analysis using Taint Analysis (DFA)
to detect security vulnerabilities and code quality issues.

### Configurability
You can control Multi-language analysis behavior by configuring which rules are applied:
*   **Disabling Built-in Rules**: If Multi-language analysis is consuming excessive resources or reporting irrelevant issues,
    you can disable default rules using configuration options.

## Performance and Troubleshooting

### Performance Tuning
While Multi-language analysis is optimized for speed, analysis of very large codebases or complex rules (like PQC rules) might take longer.
*   **Recommendation**: If analysis times are high, ensure your project is properly scoped.
*   **Note**: Some PQC rules may be computationally expensive.

### .NET and Docker Environments
When using Multi-language analysis in .NET or Docker environments:
*   Ensure Multi-language analysis is initialized correctly. If analysis hangs or fails, verify the environment setup.
*   In Rider, if syntax highlighting seems unresponsive, minor edits or a file refresh may trigger re-analysis.

### Troubleshooting Known Issues
*   **Analysis Hangs**: If analysis seems to hang, check the logs. This can occasionally occur during binary initialization or verification failures.
*   **Rule Clashes**: Ensure that any forked versions of Multi-language analysis do not clash with upstream installations on your system (`~/.cache/opengrep`, `~/.opengrep`).
*   **Syntax Highlighting (Rider)**: If highlighting issues occur, selecting all content and pasting it back into the file can sometimes force an update.

## Project Roadmap and Development

### Security Analysis (EAP)
Multi-language analysis integrates Security analysis capabilities powered by OpenGrep inspections, addressing the need for automated security vulnerability checks in modern, AI-generated code.

*   **Roadmap**: Current
*   **Focus**: Supporting automated security checks for .NET and JavaScript, competing with similar market solutions.
*   **Implementation**: Based on OpenGrep and Taint Analysis plugins, potentially moving towards a dedicated `qodana-security` linter.
*   **Configuration**: Uses a dedicated linter (`qodana-security`) and inspection profile (`qodana.security-analysis`).

### Multi-language Analysis (EAP)
This initiative aims to support third-party linters via a generic OpenGrep-based linter, expanding support to languages not covered by JetBrains IDEs.

*   **Roadmap**: Next
*   **Capabilities**:
    - Support for multiple languages, including .NET, JavaScript, and TypeScript.
    - Improved scan times and ability to analyze multiple languages in a single scan.
    - Compatibility with third-party OpenGrep rules.
*   **Configuration**: Uses a generic linter (`qodana-multi-language`) and supports language-specific inspection profiles.
