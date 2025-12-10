# Customize inspections

<var name="export-profile" value="https://www.jetbrains.com/help/idea/customizing-profiles.html#export-and-import-a-profile"/>
<var name="ruby-inspection" value="https://www.jetbrains.com/help/inspectopedia/RubyParameterNamingConvention.html#inspection-options"/>
<var name="jvmcoverageinspection" value="https://www.jetbrains.com/help/inspectopedia/JvmCoverageInspection.html#inspection-options"/>

<link-summary>Specific inspections offer configurable options, which lets you customize them for use with %product%. </link-summary>

Specific [inspections](https://jetbrains.com/help/inspectopedia) provide configurable options, which lets you customize 
them for use with %product%. 

> For several inspections, Inspectopedia provides detailed descriptions of available options. For example, see
> the [`RubyParameterNamingConvention`](%ruby-inspection%) inspection description.

To discover configurable options, in IntelliJ IDEA configure the inspection and then [export the profile](%export-profile%).
For example, the [`JvmCoverageInspection`](%jvmcoverageinspection%) inspection offers the `classThreshold`, `methodThreshold`, 
and `warnMissingCoverage` options, which you can see from the profile configuration: 

```xml
<component name="InspectionProjectProfileManager">
    <profile version="1.0">
        <option name="myName" value="Project Default" />
        <inspection_tool class="JvmCoverageInspection" enabled="true" level="WARNING" enabled_by_default="true">
            <option name="classThreshold" value="51" />
            <option name="methodThreshold" value="51" />
            <option name="warnMissingCoverage" value="true" />
        </inspection_tool>
    </profile>
</component>
```

You can use the option names in the [YAML](qodana-yaml.md) configuration of %product%, for example:

```yaml
name: "Customizing the JvmCoverageInspection inspection" # Profile name

baseProfile: qodana.recommended

inspections:
  - inspection: JvmCoverageInspection
    options:
      classThreshold: 51
      methodThreshold: 51
      warnMissingCoverage: true
```

> The detailed description of profile configuration is available in the [](inspection-profiles.md#inspection-profiles-custom-profiles) section.