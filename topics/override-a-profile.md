[//]: # (title: Configure Qodana your way)

<var name="wiki-glob" value="https://en.wikipedia.org/wiki/Glob_(programming)"/>
<var name="idea-scopes" value="https://www.jetbrains.com/help/idea/scope-language-syntax-reference.html"/>

<link-summary>A use case explaining how you can configure Qodana for various tasks.</link-summary>

%product% inspection profiles configure the inspections that you are going to use. If you enable too few inspections, you may 
miss critical problems, which will affect your project overall. On the other hand, enabling too many inspections 
can negatively affect inspection performance and can result in using inspections that are irrelevant to your project. 

%product% provides the default `qodana.starter` and `qodana.recommended` [profiles](inspection-profiles.md#Default+profiles) that come in handy in most 
cases. You can override a default profile according to your needs, and this section provides basic recommendations 
taken from the [](custom-profiles.md) section.

## Initial configuration

<procedure>
   <step>
      <p>In your project root, create the YAML-formatted file. Save the following configuration, which 
    will contain the <a href="custom-profiles.md" anchor="name"/> and <a href="custom-profiles.md" anchor="baseProfile"/> 
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
[`inspections`](custom-profiles.md#inspections-group) block, so the configuration will look as follows:

```yaml
name: "Configuring Qodana" 
baseProfile: qodana.recommended

inspections:
   - group: "category:JavaScript and TypeScript" # Specify the inspection category
     enabled: true # Enable the JavaScript and TypeScript category
```

## Exclude a specific inspection

Suppose, before running the [Qodana for PHP](qodana-php.md) linter, you would like to exclude the `PhpDeprecationInspection` 
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
`vendor` directory in your project root. You can do this by using the [`ignore`](custom-profiles.md#inspections-group) block. The final 
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

## Learn more

You can visit the [](custom-profiles.md) section to learn more about advanced configuration techniques, more configuration examples, 
and creating configurations from scratch.

Once you have configured %product%, you can run it using the recommendations from the [](Quick-start.topic) section.
