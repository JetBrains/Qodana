[//]: # (title: Configure Qodana your own way)

<var name="wiki-glob" value="https://en.wikipedia.org/wiki/Glob_(programming)"/>
<var name="idea-scopes" value="https://www.jetbrains.com/help/idea/scope-language-syntax-reference.html"/>

%product% inspection profile configures the inspections to scan your code. If you enable too few inspections, you may 
miss the crucial problems, which will affect your project in overall. On the other hand, enabling too many inspections 
can negatively affect inspection performance while your code is scanned using inspections irrelevant to your project. 

%product% provides the default `qodana.starter` and `qodana.recommended` [profiles](inspection-profiles.md#Default+profiles) that come in handy in most 
cases. If you also override a default profile according to your needs, and this page contains basic recommendations 
taken from the [](custom-profiles.md) section.

## Prepare configuration

<procedure>
   <step>
      <p>In your project root, create the YAML file that will configure and be accessible by %product%. This sample show 
      how to override the <code>qodana.recommended</code> profile, and you can save the following configuration to it:</p>
      <code style="block" lang="yaml">
      name: "Configuring Qodana" # Paste here the name of your profile
      baseProfile: qodana.recommended # Override qodana.recommended
      </code>
      <p>This configuration employs the <a href="custom-profiles.md" anchor="name"/> and 
         <a href="custom-profiles.md" anchor="baseProfile"/> blocks.</p>
   </step>
   <step>
      <p>In the <a href="qodana-yaml.md"><code>qodana.yaml</code></a> file, provide the path to your profile configuration file:</p> 
      <code style="block" lang="yaml">
      profile:
         path: &lt;relative-path-to-custom-configuration&gt;
      </code>
      <tip>The detailed profile configuration guide is available in the <a href="custom-profiles.md"/> section.</tip>
   </step>
</procedure>

## Enable JavaScript and TypeScript inspections

Starting from version 2023.2 of %product%, all linters provide JavaScript and TypeScript inspections that are disabled 
by default. You can enable the `JavaScript and TypeScript` inspection category using the 
[`inspections`](custom-profiles.md#inspections-group) block, so the configuration will look as follows:

```yaml
name: "Configuring Qodana" 
    
baseProfile: qodana.recommended

inspections:
   - group: "category:JavaScript and TypeScript" # Specify the inspection category
     enabled: true # Enable the JavaScript and TypeScript category
```

## Exclude a specific inspection

Suppose, before running the [Qodana for PHP](qodana-php.md) linter, you need to exclude the `PhpDeprecationInspection` 
inspection contained in the `qodana.recommended` profile. Here is the updated configuration:

```yaml
name: "Configuring Qodana"
    
baseProfile: qodana.recommended

inspections:
   - group: "category:JavaScript and TypeScript"
     enabled: true
   - inspection: PhpDeprecationInspection # Specify an inspection
     enabled: false # Disable the inspection
```

## Exclude a path

You can tell %product% ignoring specific paths while inspecting your code. Suppose, you would like to ignore the 
`vendor` directory in your project root using the [`ignore`](custom-profiles.md#inspections-group) block, so the final 
configuration is shown below:

```yaml
name: "Configuring Qodana"

baseProfile: qodana.recommended

groups:

inspections:
   - group: "category:JavaScript and TypeScript"
     enabled: true
     ignore:
       - "vendor/**" # Ignore the vendor directory
   - inspection: PhpDeprecationInspection
     enabled: false
```

## Learn more

This use case showed how to configure inspections and inspection paths. To learn more about advanced configuration
techniques, more configuration examples and creating configurations from scratch, you can visit the [](custom-profiles.md) section.

Once you have configured %product%, you can run it using recommendations from the [](Quick-start.xml) section.
