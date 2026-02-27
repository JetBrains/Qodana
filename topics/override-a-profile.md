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

%product% inspection profiles configure the inspections that you are going to use. If you enable too few inspections, you may 
miss critical problems, which will affect your project overall. On the other hand, enabling too many inspections 
can negatively affect inspection performance and can result in using inspections that are irrelevant to your project. 

%product% provides the default `qodana.starter` and `qodana.recommended` [profiles](inspection-profiles.md#inspection-profiles-existing-profiles) that come in handy in most 
cases. You can override a default profile according to your needs, and this section provides basic recommendations 
taken from the [](inspection-profiles.md#inspection-profiles-custom-profiles) section.

## Initial configuration

<procedure>
   <step>
      <p>In your project root, create the YAML-formatted file. Save the following configuration, which 
    will contain the <a href="inspection-profiles.md" anchor="name"/> and <a href="inspection-profiles.md" anchor="base"/> 
blocks for naming your %product% profile and overriding the <code>qodana.recommended</code> profile:</p>
      <code-block lang="yaml">
      name: "Configuring Qodana" # Paste the name of your profile
      baseProfile: qodana.recommended # Override qodana.recommended
      </code-block>
   </step>
   <step>
      <p>In the <a href="qodana-yaml.md"><code>qodana.yaml</code></a> file, provide the path to the file configured in the previous step:</p> 
      <code-block lang="yaml">
      profile:
         path: &lt;relative-path-to-yaml-config-file&gt;
      </code-block>
   </step>
</procedure>

## Enable JavaScript and TypeScript inspections

Starting from version 2023.2 of %product%, all linters provide JavaScript and TypeScript inspections, but they are 
disabled by default. You can enable the `JavaScript and TypeScript` inspection category using the 
[`inspections`](inspection-profiles.md#inspections-group) block, so the configuration will look as follows:

```yaml
name: "Configuring Qodana" 
baseProfile: qodana.recommended

inspections:
   - group: "category:JavaScript and TypeScript" # Specify the inspection category
     enabled: true # Enable the JavaScript and TypeScript category
```

## Exclude a specific inspection

Suppose, before running the [%php%](php.md) linter, you would like to exclude the `PhpDeprecationInspection` 
inspection supported by the `qodana.recommended` profile. In this case, you can update your configuration as follows:

```yaml
name: "Configuring Qodana"
baseProfile: qodana.recommended

inspections:
   - group: "category:JavaScript and TypeScript"
     enabled: true
   - inspection: PhpDeprecationInspection # Specify an inspection
     enabled: false # Disable the inspection
```

## Specify inspection path(s)

You can tell %product% to ignore specific paths while inspecting your code. Suppose you would like to ignore the 
`vendor` directory in your project root. You can do this by using the [`ignore`](inspection-profiles.md#inspections-group) block. The final 
configuration would look like this:

```yaml
name: "Configuring Qodana"
baseProfile: qodana.recommended

inspections:
   - group: "category:JavaScript and TypeScript"
     enabled: true
     ignore:
       - "vendor/**" # Ignore the vendor directory
   - inspection: PhpDeprecationInspection
     enabled: false
```

## Specify SQL dialect

<p>To analyze SQL code, enabling SQL-related
    <a href="qodana-yaml.md" anchor="Include+an+inspection+in+the+analysis+scope">inspections</a> is not enough.
    In this case, you also have to specify an SQL dialect that you would like to analyze. To do this, in your
    project root save the <code>.idea/sqldialects.xml</code> containing the following contents:</p>
<code-block>
    &lt;?xml version="1.0" encoding="UTF-8"?&gt;
    &lt;project version="4"&gt;
        &lt;component name="SqlDialectMappings"&gt;
            &lt;file url="PROJECT" dialect="&lt;SQLDialectName&gt;" /&gt;
        &lt;/component&gt;
    &lt;/project&gt;
</code-block>
<p>To find a name of a concrete SQL dialect for this snippet, in your IDE navigate to
    <ui-path>Settings | Languages & Frameworks | SQL Dialects | Project SQL Dialect</ui-path>. In the upper part
of the <ui-path>Settings</ui-path>, expand either the <ui-path>Global SQL Dialect</ui-path> or
    <ui-path>Project SQL Dialect</ui-path> dropdown list.</p>

## Learn more

You can visit the [](inspection-profiles.md#inspection-profiles-custom-profiles) section to learn more about advanced configuration techniques, more configuration examples, 
and creating configurations from scratch.

Once you have configured %product%, you can run it using the recommendations from the [](Quick-start.topic) section.
