<no-index/>

# Frontend

<warning>This section is in progress, so we do not recommend to use it.</warning>

## 5.0.0

Release date: 08 July 2024

### Features
{id="500-features"}

* Configuration steps for various CI/CD solutions in the project setup including GitHub Actions
* The component of `ChooseRepositoryPage` was updated with a notification including private repositories and links to the documentation
* Step-by-step instructions for configuring CI/CD solutions
* The **Copy config** button was redesigned in the project setup
* The step back button in the project setup
* The English language review for the project setup texts
* In the project setup, options for configuring Jenkins, TeamCity, and GitHub Actions. This includes saving
  the state between configuration steps
* Update in Qodana Cloud UI icons and buttons
* Navigation to the first screen of the project setup wizard. Now, a user can choose a CI/CD solution they would like to use

### Fixes
{id="500-fixes"}

* Project setup card texts were updated for the case when no permissions are granted to obtain a project token
* Fix in Qodana Cloud report URLs while clicking the **Open in IDE** button
* The **$** character copying was fixed while copying code snippets from the project setup wizard
* Fixed console output args and unused variables from the `ChooseRepositoryPage` tests
  the **Choose VCS** page of the project setup wizard
* No redirection rule was set to the project setup wizard after clicking **Manage permissions**
* The MD5 library was moved to the `qodana-cloud` package
* `QueryableList` was added to the list of repositories

## 5.1.0

Release date: 02 August 2024

### Features
{id="510-features"}

* Statistics for the project setup stage
* The **Authorization pending** modal window is now part of the project setup wizard
* Error log tracking for the project setup stage
* A filter and pagination were added on the organization users page
* The list of validation rules was updated to allow characters like `_` to be present in Qodana Cloud entities
* Page navigation between various setup options in the project setup wizard
* The mechanism for generating random project names for default projects was developed for the project setup to handle name collisions
* The %product% logo in %product% Cloud UI was replaced with the new one

### Fixes
{id="510-fixes"}

* Manage permissions functionality for GitHub repositories in Qodana Cloud was fixed for private repository analysis
* The list of organization administrators was hidden from external users
* Proper redirection from the last step of the project setup was configured
* The UI for managing permissions in GitHub was developed
* Project card redirection is available to VCS options
* Improved config code snippets that propagate variable names for a Qodana [project token](project-token.md) are in use

## 5.2.0

Release date: 20 August 2024

### Features
{id="520-features"}

* Large widget container in the Qodana Cloud UI
* Navigation to the dashboard in Qodana Cloud
* Redirection logic while creating a new organization in Qodana Cloud

### Fixes
{id="520-fixes"}

* Information about a Qodana Cloud organization was removed from the Qodana Cloud team URL
* Error handling after unsuccessful newsletter subscription was implemented
* Update in the team dashboard design
* Improved validation messages in the Qodana Cloud UI

## 6.0.0

Release date: 30 August 2024

### Features
{id="600-features"}

* A chart pop-over component for Qodana reports
* A donut chart widget for Qodana reports
* A dashboard page layout in Qodana Cloud
* Collecting statistics about IDs of projects, users and organizations
* Collecting information about project IDs in the hashed form

### Fixes
{id="600-fixes"}

* Simplified E-mail verification was implemented on the frontend side

## 6.1.0

Release date: 23 September 2024

### Features
{id="610-features"}

* A donut chart widget on the **Insights** page
* A timeline chart component in the Qodana Cloud UI

### Fixes
{id="610-fixes"}

* An error message if a user cannot get information was developed
* Keyboard navigation for the `MoreActions` component was implemented
* Sending reports about expired invitations to the frontend Sentry was disabled

## 6.2.0

Release date: 08 October 2024

### Features
{id="620-features"}

* The **Scans** widget in the Qodana Cloud UI
* A modal window containing a table in the Qodana Cloud UI
* A timeline chart widget in the Qodana Cloud UI
* A tracking provider for pages containing now organization ID in the URL

### Fixes
{id="620-fixes"}

* Report scaling in Qodana reports was fixed
* List of accounts update in case of a repository request error was fixed
