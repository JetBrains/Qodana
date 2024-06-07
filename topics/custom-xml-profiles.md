[//]: # (title: Custom XML profiles)

You can create XML-formatted inspection profiles using your IDE. For example, for IntelliJ IDEA this is explained
on the [Configure profiles](https://www.jetbrains.com/help/idea/customizing-profiles.html) page.  After you create a 
profile, you can [export](https://www.jetbrains.com/help/idea/customizing-profiles.html#export-and-import-a-profile) it 
to file.

To run %instance% with the custom profile, you can follow the recommendations from the 
[](inspection-profiles.md#inspection-profiles-setup-a-profile) section. In this case, the profile name does not necessarily 
match the name of the containing file. The actual name is stored as the `%\profileName%` value in the profile file.

