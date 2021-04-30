[//]: # (title: About Qodana Clone Finder)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

Qodana Clone Finder detects duplicates in code repositories. While static analysis within IntelliJ IDEs allows to find copied code within one project on an individual workstation, the new linter allows to search for code copies across multiple repositories, helping to avoid
* Penalties for unlicensed use of third-party code
* Excessive project maintenance costs
* Not fixing vulnerabilities in all instances of copied code.

<!---Qodana Clone Finder allows to find code clones on the function level in six different languages: Java, Kotlin, Python, JavaScript, TypeScript, and Go.
It uses a [block-based bag-of-tokens approach to clone detection](https://arxiv.org/pdf/2002.05204.pdf) that applies different similarity thresholds depending on the function size and token length, thus yielding diverse relevant results.
Clone Finder uses a logistic regression model trained on a dataset of 200 pairs of clones using three metrics: number of identifiers, entropy of the identifiers, and average length of the identifiers. Types of clones detected:
Clone Finder uses a logistic regression model trained on a dataset of 200 pairs of clones using three metrics: number of identifiers, entropy of the identifiers, and average length of the identifiers, finding the following types of clones:...

Clone Finder workflow
1. Identifies the programming language.
2. Parses code, extracts ASTs and then the following information for each function:
* path to the file
* identifier names
* path to the function
* all lines of code for the function.
3. Searches for similar sets of identifiers taking into account the function size and the identifier frequency.
As a result, Clone Finder lists per each component of the queried project:
* clones
* language
* score
* topic
* license.!--->

Qodana Clone Finder finds the following types of clones between a queried project and selected reference projects:
* Identical code fragments but may have some variations in whitespace, layout, and comments
* Syntactically equivalent fragments with some variations in identifiers, literals, types, whitespace, layout and comments
* Syntactically similar code with inserted, deleted, or updated statements.
