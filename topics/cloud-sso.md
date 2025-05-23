# Single Sign-on

<show-structure for="chapter" depth="3"/>

<link-summary>Single Sign-On (SSO) functionality of %cloud% lets you use third-party identity providers for 
authentication in %cloud%.</link-summary>

<var name="hub-link" value="https://www.jetbrains.com/help/hub/introduction-to-hub.html"/>
<var name="hub-user-acc" value="https://www.jetbrains.com/help/hub/creating-user-accounts.html#CreatingNewAccount"/>
<var name="hub-user-invite" value="https://www.jetbrains.com/help/hub/creating-user-accounts.html#InvitingNewUsers"/>
<var name="hub-access-management" value="https://www.jetbrains.com/help/hub/access-management.html"/>
<var name="hub-user-roles" value="https://www.jetbrains.com/help/hub/configuring-access-for-a-user-account.html#GrantingAccessToAccount"/>
<var name="hub-auth-modules" value="https://www.jetbrains.com/help/hub/managing-auth-modules.html"/>

Single Sign-On (SSO) functionality of %cloud% lets you use third-party identity providers for authentication in %cloud%.
This functionality is available only under Ultimate Plus [licenses](pricing.md) purchased for a minimum of ten users.

This section explains how you can manage users and authentication modules for authentication in %cloud% and guides 
you through the SSO configuration process. 

## Configure SSO

### Create a subdomain
{id="sso-create-a-subdomain"}

Only users with the [Admin](cloud-user-roles.md#cloud-user-org-roles-admin) and
[Owner](cloud-user-roles.md#cloud-user-org-roles-owner) organization roles can configure the single sign-on functionality
in %cloud%.

User authentication is carried out using a subdomain of %cloud%, which you can create as explained below.

<procedure>
    <step>In your %cloud% organization, navigate to the 
        <a href="cloud-organizations.topic" anchor="cloud-organizations-overview">settings page</a>.</step>
    <step>
        <p>On the settings page, click the <ui-path>SSO</ui-path> tab.</p>
    </step>
    <step><p>On the <ui-path>SSO</ui-path> tab, enter the name of the subdomain that you would like to use for authentication, and then
            click the <ui-path>Set up SSO</ui-path> button.</p> 
        <img src="qc-sso-sso-tab.png" width="706" alt="The SSO tab of the organization settings" border-effect="line"/>
    </step>
    <step><p>On the <ui-path>SSO</ui-path> tab, copy and save the generated URL that you will be using for authentication, and then click the <ui-path>Configure SSO</ui-path> link to proceed to the next configuration stage.</p>
          <img src="qc-sso-configure-sso.png" width="706" alt="The generated URL and the Configure SSO link" border-effect="line"/>
    </step>
</procedure>

### Manage users and authentication modules
{id="sso-manage-users-auth-modules"}

Based on the latest step of [the previous action](#sso-create-a-subdomain), you should be redirected to a 
[JetBrains Hub](%hub-link%) instance. 

Using the [**Access Management**](%hub-access-management%) section of the **Administration** menu, navigate to the 
[**Auth Modules**](%hub-auth-modules%) page. On this page, perform the following actions: 

* Select and configure the authentication modules that you would like to use. 
* Import users and groups, as well as assign them to [%product% user roles](cloud-user-roles.md). Each imported user should be granted a 
  %product% role, which can be achieved by granting a role explicitly using the **Roles** tab or by creating user groups
  with %product% roles and assigning users to those groups.

## Authenticate in %cloud%

Once you configured users and authentication modules, you can navigate to %cloud% using the URL that was generated
during the [subdomain creation](#sso-create-a-subdomain) stage. On the page that opens, click the **Login with SSO** button.

<img src="qc-login-with-sso-start-page.png" width="706" alt="%cloud% start page with SSO" border-effect="line"/>

This will redirect you to the authentication page containing configured providers.

<img src="qc-sso-authentication-page.png" width="706" alt="%cloud% SSO authentication page" border-effect="line"/>