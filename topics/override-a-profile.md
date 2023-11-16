[//]: # (title: Override a profile)

%product% inspection profile configures the inspections to scan your code. If you enable too few
inspections, you may miss the crucial problems. On the other hand, enabling too many inspections can negatively affect
inspection performance while your code is scanned using inspections irrelevant to your project. 

%product% provides the default `qodana.starter` and `qodana.recommended` 
[default profiles](inspection-profiles.md#Default+profiles) that come in handy in most cases. If you wish to 
override a default profile, this page contains basic recommendations taken from the [](custom-profiles.md) section. 

## Before you start

1. Create the YAML file that will contain the profile configuration and be accessible by %product%. Suppose it will override
the `qodana.recommended` profile, in this case save this configuration to the profile configuration file:

    ```yaml
    name: "My custom profile" # Paste here the name of your profile
    
    baseProfile: qodana.recommended # Override qodana.recommended
    ```

2. In the [`qodana.yaml`](qodana-yaml.md) file, specify the path to the profile configuration file as explained on the 
[Inspection profiles](inspection-profiles.md#Profile+path) page.

<tip>The detailed profile configuration guide is available in the <a href="custom-profiles.md"/> section.</tip>

## Enable the JavaScript and TypeScript inspections

Starting from 2023.2, all %product% linters provide JavaScript and TypeScript inspections that are disabled by default. 
To enable them, you need to enable the `JavaScript and TypeScript` inspection category, your configuration file look like:

```yaml
name: "My custom profile" # Paste here the name of your profile
    
baseProfile: qodana.recommended # Override qodana.recommended

inspections:
   - group: "category:JavaScript and TypeScript"
     enabled: true
```

## Exclude a specific inspection

Suppose, before running the [Qodana for PHP](qodana-php.md) linter you need to exclude the `PhpDeprecationInspection` 
inspection from the `qodana.recommended` profile. Here is the configuration for this:

```yaml
name: "My custom profile" # Paste here the name of your profile
    
baseProfile: qodana.recommended # Override qodana.recommended

inspections:
   - inspection: PhpDeprecationInspection
     enabled: false
```

## Exclude a path

<include src="custom-profiles.md" include-id="custom-profiles-exclude-paths"/>

