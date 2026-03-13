[//]: # (title: Inspections)

<var name="wiki-glob" value="https://en.wikipedia.org/wiki/Glob_(programming)"/>
<var name="idea-scopes" value="https://www.jetbrains.com/help/idea/scope-language-syntax-reference.html"/>


<link-summary>Each inspection is a set of conditions to analyze the code, detect and correct abnormal fragments in it. Qodana
    inspections can find and highlight various problems, locate dead code, find probable bugs, spelling problems,
    and thus facilitate improving the overall code structure.</link-summary>

Each inspection is a set of conditions to analyze the code, detect and correct abnormal fragments in it. Qodana
    inspections can find and highlight various problems, locate dead code, find probable bugs, spelling problems,
    and thus facilitate improving the overall code structure. Using inspections, Qodana implements its
    [static analysis](static-analysis.topic) mechanism. 


All inspections are highly configurable, so you can configure:

* What inspections to run for your codebase. There are lots of various inspections, so you can enable or
  disable them for some reason.
* What directories and files to include in your code analysis. If you feel that you do not need to analyze
  any file or group of files, you can exclude them from code analysis.
* How you can configure and use [inspection profiles](#Inspection+profiles). You can use the preset combinations
  of inspections specified by inspection profiles aimed at solving specific tasks or create your custom profile
  that would meet your unique needs.

You can explore available %product% inspections using the [Inspectopedia](https://www.jetbrains.com/help/inspectopedia/) website.
This website provides details about inspections: descriptions, severity levels, languages covered, etc.

You can use the table of contents to explore all available inspections:

<img src="inspectopedia-toc.png" alt="Table of contents on the Inspectopedia website" width="296" border-effect="line"/>

Alternatively, you can search for the concrete inspections by their names, or identifiers:

<img src="inspectopedia-search.png" alt="Searching for an inspection" width="706" border-effect="line"/>

## Inspection profiles

Inspection profiles let you combine and configure inspections that you would like %product% to use. The detailed description
of inspection profiles is available in the [](inspection-profiles.md) section.

