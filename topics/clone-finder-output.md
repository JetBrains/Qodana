[//]: # (title: Clone Finder Output Formats)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

## Basic output

Full Clone Finder results are available in the file `report.json` located in the `results-dir` folder.

### UI-compatible output

In addition to programmatic output, you can generate human-readable output in the HTML format by using the `--save-report` argument.
See [HTML report](html-report.md) section for details.

```shell
├── asset-manifest.json  //UI
├── index.html //UI
├── preview.html //UI
├── results // folder with inspectiond descriptions
│   ├── descriptions
│   │   └── <inspection name>.json // Inspection description
│   ├── metaInformation.json // Metadata data about found problems
│   ├── projectStructure
│   │   └── <inspection name>.json // Inspection description
│   └── result-allProblems.json // All found probelms
└── versions // UI
```

### Command-line summary output

An example of the Clone Finder command-line summary output:
``` shell
┏━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━┓
┃ Repository ┃ Clones ┃ Functions ┃
┡━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━┩
│ buckwheat  │ 6      │ 72        │
│ http4k     │ 0      │ 3519      │
│ ideavim    │ 0      │ 4494      │
└────────────┴────────┴───────────┘
```

## UI-compatible output

In addition to programmatic output, you can generate human-readable output in the HTML format by using the `--save-report` argument.

### Learn more

* How to open a generated report in your browser: [HTML Report](html-report.md)

* Basic structure and configuration of Qodana HTML reports: [UI Overview](ui-overview.md)

* More information on command-line arguments for Clone Finder: [Docker Image Paths and Configuration Options](clone-finder-docker-techs.md)

### A sample decorated diff
In addition to the sunburst diagram and other features of Qodana's [web report](ui-overview.md), Clone Finder makes the analysis of code duplicates more helpful and convenient.
- The detected clones are prioritized and displayed in the order of their importance.
- When you expand an item, the duplicate code fragments are provided with decorated code diffs and are annotated with tags, licenses, languages, and file paths.

[//]: # "![](php-diff.png)"

Clone Finder highlights similar lines and presents the following information to help you investigate the problem:
1. Score

    Lists all detected duplicate functions ranked by their importance.
2. Tags

    Categorizes detected copies using 256 topics (see Figure 2 for a dendrogram of supported topics).
3. Licenses

    Lists licenses related to duplicate code fragments detected in the compared projects.
By the way, to supplement this feature, we are working on another tool that will list the licenses for third-party libraries used in the queried project and warn about incompatibilities between the queried project's license and third-party licenses. Stay tuned!
4. License mismatch warnings

    Displays a warning when the licenses in duplicate code fragments are different.
5. Language

    Displays the programming language of the clones. The EAP version of Clone Finder supports PHP, Java, and Kotlin.
