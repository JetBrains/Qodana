[//]: # (title: About Qodana Clone Finder)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

Qodana Clone Finder lets you check a queried project against a number of reference projects and lists all duplicate functions ranked by their importance. It is aimed to prevent problems rather than face them. By supporting CI integration, Clone Finder makes clone detection a routine check and allows finding borrowed code as early as possible.

The current version [supports PHP, Java, and Kotlin for Server Side](supported-technologies.md); support for more languages and technologies is on its way.

## Features

Clone Finder uses a [block-based bag-of-tokens approach to clone detection](https://arxiv.org/pdf/2002.05204.pdf) that applies different similarity thresholds depending on the function size and token length, thus yielding diverse relevant results.

### Types of clones detected
* Identical code fragments with possible variations in whitespaces, layout, and comments
* Syntactically equivalent fragments with some variations in identifiers, literals, types, whitespaces, layout and comments
* Syntactically similar code with inserted, deleted, or updated statements.

You can see a sample report in [Clone Finder Output](clone-finder-output.md).

### Helps to avoid the following problems
<!---update!--->
* Penalties for unlicensed use of third-party code
* Excessive project maintenance costs
* Not fixing vulnerabilities in all instances of copied code.

## Distribution

We provide the Clone Finder linter in a number of formats---.

Clone Finder is packed into a ready-to-use [Docker image](clone-finder-docker-readme.md) which supports different usage scenarios:
- Running the analysis on a regular basis as part of your continuous integration (*CI-based execution*)
- Single-shot analysis (for example, performed *locally*)
- - --[GitHub Action](clone-finder-github-action.md)

If you don't have any CI for your project, we encourage you to try a free version of JetBrains [TeamCity](https://www.jetbrains.com/teamcity/), either in-cloud (currently in Beta) or on-premise. In this case, you can switch to our [TeamCity plugin](clone-finder-teamcity-plugin.md) as it gives more options.









