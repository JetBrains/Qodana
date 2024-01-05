[//]: # (title: Onboarding)

Onboarding is an essential step in preparing %instance% for working with your project, which lets you: 

- Connect your project repository to Qodana Cloud
- Create a Qodana Cloud [organization](cloud-organizations.topic), a [team](cloud-teams.topic), and a [project](cloud-projects.topic)
- Generate a [project token](project-token.md) required by the Ultimate and Ultimate Plus linters
- Set up code inspection

Onboarding uses information from your JetBrains account including licenses and companies. 

Below is the description of the steps.

<procedure>
<step>
<p>In the <ui-path>New company name</ui-path> field, provide either a new company name that will be stored in 
your JetBrains account. Alternatively, you can use the already existing company taken from your JetBrains account. </p>

<p>In the <ui-path>Name of your Qodana organization</ui-path> field, provide the name of the organization that will be 
used only in Qodana Cloud. In this case, multiple Qodana organizations can be created under a single JetBrains account.</p>

<p>In the <ui-path>Country</ui-path> field, select your country name.</p>

<img src="cloud-onboarding-step-1.png" dark-src="cloud-onboarding-step-1_dark.png" alt="The first step of the Qodana Cloud onboarding" width="706" border-effect="line"/>
</step>
<step>
<p>In the <ui-path>SSH URL</ui-path> field, provide the SSH URL to your project that can be accessible by Qodana Cloud.</p>

<img src="cloud-onboarding-step-2.png" dark-src="cloud-onboarding-step-2_dark.png" alt="The second step of the Qodana Cloud onboarding" width="706" border-effect="line"/>

<p>After connecting, Qodana Cloud provides a public key that will be identified by your Qodana Cloud account.</p>

<img src="cloud-onboarding-step-2-key.png" dark-src="cloud-onboarding-step-2-key_dark.png" alt="The public key generated during the second step of the Qodana Cloud onboarding" width="706" border-effect="line"/>

<p>Copy this public key and save it in your VCS on the project level. For example, read how to do it on: </p>

* [GitLab](https://docs.gitlab.com/ee/user/project/deploy_keys/#create-a-project-deploy-key)
* [GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/managing-deploy-keys#set-up-deploy-keys) - start from step 2, i.e. skip the SSH key generation step
* [JetBrains Space](https://www.jetbrains.com/help/space/git-keys-and-passwords.html#ssh-key) - start from step 2, i.e. skip the SSH key generation step 

<warning>Do not store the key on the account level, so that it cannot be shared by other repositories within your account.</warning>
</step>
<step>
<p>In the <ui-path>Your project name</ui-path> field, specify the name of the Qodana Cloud 
<a href="cloud-projects.topic">project</a>. In the field below it, specify the name of the <a href="cloud-teams.topic">team</a> 
that the project will be accessible for.</p>

<img src="cloud-onboarding-step-3.png" dark-src="cloud-onboarding-step-3_dark.png" alt="The third step of the Qodana Cloud onboarding" width="706" border-effect="line"/>
</step>
<step>
<p>Open your project locally using the JetBrains IDE, or learn how to configure %instance% for running in a CI/CD pipeline. 
This step also contains the <a href="cloud-projects.topic" anchor="cloud-manage-projects">project token</a> that you can 
copy and use for <a href="cloud-forward-reports.topic">uploading %instance% reports</a> to Qodana Cloud.</p>

<img src="cloud-onboarding-step-4.png" dark-src="cloud-onboarding-step-4_dark.png" alt="The fourth step of the Qodana Cloud onboarding" width="706" border-effect="line"/>
</step>

</procedure>






