# Qodana product roadmap Q2-Q3

## Core updates

- **Code coverage**: simplified setup, UI/UX improvements, artifact auto-discovery and IDE UI for incremental analysis.
- **License audit**: implementation of incremental analysis and R# API support.
- **Security analysis** including zero-configuration security analysis suitable for human and AI-generated code.
- **Code provenance** support for monorepo projects.
- **Automatic generation of new inspections** using the rule introspection functionalities.  
- **Code quality**:
    - LLM-based review agent
    - Updated quality metrics
- **Linter updates**:
    - Rider SafeCode EAP
    - Third-party linter onboarding
    - Multi-language analysis EAP
    - Two-phase analysis for the [%jvm%](jvm.md) and [%dotnet%](dotnet.md) linters
    - %product% CLI UX/UI improvements to make the user onboarding smoother 
    - Terraform inspections


<!--- **Rust**: implementation of license audit, vulnerability checker and code coverage for the [%rust%](rust.md) linter. -->
<!--    - %product% skill for Air -->
<!--    - Contributor counting mechanism -->
<!--    - Lua
    - SQL -->
<!--    - Code metrics insights -->

## Security updates

- **Opengrep plugin** available for %product%, in JetBrains Rider and JetBrains Marketplace and providing .NET and JavaScript security analysis capabilities.
- **Benchmarks** for security agent evaluation.
- **LLM-based linters** for agents like Codex, CC, Koog(ByOK) behind the ACP protocol.

## Qodana Cloud

- **UX/UI improvements** for onboarding, configuration, analysis reports and baseline making interaction with them easier and clearer.
- **Qodana Cloud API** supports configuration and managing of %product% entities like teams, projects, memberships, SSO and others.
- **Updated Insights metrics** includes duplication and cyclomatic complexity.
- **%premlite% documentation** update for covering all users' needs regarding deployment and usage. 

