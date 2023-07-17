[//]: # (title: Onboarding)

The onboarding stage is an essential step in preparing your project for %product%, namely: 

- Connect your project to Qodana Cloud
- Generate the license for %product%
- Create a Qodana Cloud organization and project
- If necessary, create a JetBrains account organization

Onboarding is available while creating your account at Qodana, as well as while creating an [](cloud-organizations.xml), and 
consists of several steps as described below. Because logging in to Qodana Cloud is carried out using your 
[JetBrains account](cloud-get-access.xml), 

<img src="cloud-onboarding-step-1.png" alt="The first step of the Qodana Cloud onboarding" width="706" border-effect="line"/>

During the first step, in the **New company name** field provide either a new company name that will be stored in 
your JetBrains account. Alternatively, you can use the already existing company taken from your JetBrains account. 

In the **Name of your Qodana organization** field, provide the name of the organization that will be used only in Qodana 
Cloud. In this case, multiple Qodana organizations can be created under a single JetBrains account.

The **Country** field should contain your country name. 

<img src="cloud-onboarding-step-2.png" alt="The second step of the Qodana Cloud onboarding" width="706" border-effect="line"/>

During the second step, in the **SSH** field provide the SSH URL to your project that can be accessible by Qodana Cloud.
After connecting, Qodana Cloud provides a public key that will be identified by your Qodana Cloud account. 

<img src="cloud-onboarding-step-2-key.png" alt="The public key generated during the second step of the Qodana Cloud onboarding" width="706" border-effect="line"/>

Copy this public key and save it in your VCS on the project level. For example, you can read how to do it on: 

* [GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/managing-deploy-keys#deploy-keys),
* [GitLab](https://docs.gitlab.com/ee/user/project/settings/project_access_tokens.html) 
* [JetBrains Space](https://www.jetbrains.com/help/space/git-keys-and-passwords.html)

<warning>Do not store the key on the account level, so that it cannot be shared by other repositories within your account.</warning>

<img src="cloud-onboarding-step-3.png" alt="The third step of the Qodana Cloud onboarding" width="706" border-effect="line"/>

During the third onboarding step, in the **Your project name** specify the name of the [project](cloud-projects.xml) in 
Qodana Cloud. In the field below, specify the name of the [team](cloud-teams.xml) that the project will be accessible for.

<img src="cloud-onboarding-step-4.png" alt="The fourth step of the Qodana Cloud onboarding" width="706" border-effect="line"/>

During the final onboarding step, you can open your project locally using the JetBrains IDE, or learn how to configure
%product% for running Qodana over it in a CI/CD pipeline. This page also contains the 
[project token](cloud-projects.xml#cloud-manage-projects) that you can copy and use for 
[uploading %product% reports](cloud-forward-reports.xml) to Qodana Cloud.