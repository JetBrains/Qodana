[//]: # (title: About Qodana Clone Finder)

[![official project](https://jb.gg/badges/official-flat-square.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

<note>

<include src="lib_qd.xml" include-id="supported-techs">
    <var name="linter" value="Qodana Clone Finder"/>
    </include>

</note>

Qodana Clone Finder compares a queried project against a number of reference projects and lists all duplicate functions ranked by their importance. 
In future, search by classes and files will be added.

The tool is designed to prevent problems rather than face the consequences down the line. By supporting CI integration, Clone Finder makes clone detection a routine check and reports borrowed code before it can lead to trouble.

## Features

Clone Finder uses a [block-based bag-of-tokens approach to clone detection](https://arxiv.org/pdf/2002.05204.pdf) that applies different similarity thresholds depending on the function size and token length, thus yielding diverse relevant results.

### Clone types and importance score calculation
{id="importance-score"}

Clone Finder uses a logistic regression model to estimate the importance score of clones based on features like the number of identifiers, entropy of the identifiers, and average length of the identifiers, finding the following types of clones:
* Identical code fragments with possible variations in whitespaces, layout, and comments
* Syntactically equivalent fragments with some variations in identifiers, literals, types, whitespaces, layout and comments
* Syntactically similar code with inserted, deleted, or updated statements.

You can see a sample report in [Clone Finder Output](clone-finder-output.md).

### Types of problems prevented

* Penalties for the unlicensed use of third-party code
* Excessive project maintenance costs due to overgrown codebases
* Increased security risks because fixing detected vulnerabilities across all instances of the copied code can be difficult

## Try it now

### Analyse a project locally

To start, pull the image from Docker Hub (only necessary to get the latest version):

```shell
docker pull jetbrains/qodana-clone-finder
```

and run the analysis locally:

```shell
   docker run --rm -it -p 8080:8080 \
      -v <queried-project-directory>/:/data/project/ \
      -v <reference-projects-directory>/:/data/versus/ \ 
      -v <output-directory>/:/data/results/ \
      jetbrains/qodana-clone-finder --show-report
   ```

where `<queried-project-directory>`, `<reference-projects-directory>`,  and `<output-directory>` are full local paths to the directories that contain, respectively, the project source code, one or more projects to compare against, and the analysis results.

Check the results in your browser at [`http://localhost:8080`](http://localhost:8080).

Read our [Docker guide](clone-finder-docker-readme.md) for more options and details related to the Clone Finder execution.
 
<seealso>
  <category ref="next_steps">
   <a href="clone-finder-docker-readme.md"/>
   <a href="clone-finder-github-action.md"/>
    <a href="clone-finder-teamcity-plugin.md"/>
  </category>
 </seealso>
