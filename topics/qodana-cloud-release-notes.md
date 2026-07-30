# Qodana Cloud release notes

<show-structure for="chapter" depth="3"/>

## July 2026

Here are highlights of what shipped in Qodana Cloud since our last update. As always, this covers user-facing features, 
UI improvements, bug fixes, and stability improvements that affect your experience.

### Security
{id="july-2026-security"}

* **Critical AWS ECR vulnerabilities resolved**. Upgraded components to address critical container image vulnerabilities.
* **VCS link domain allowlist bypass fixed**. The button that links out to your VCS host validated domains using a 
  pattern that could be spoofed; it now checks properly.


### New features
{id="july-2026-new-features"}

#### Cloud API
{id="july-2026-new-features-cloud-api"}

**Set team visibility on project creation**. The `/api/v1/public/organizations/projects` endpoint now accepts an 
`isPublicTeam` parameter, so you can create a private team via the API instead of only public ones. Existing teams are unaffected.

#### UI improvements
{id="july-2026-new-features-ui-improvements"}

* **Switch controls replace dropdowns**. The timeline graph filter and the problems/files switcher in the TeamCity plugin 
now use direct toggle controls instead of dropdowns.
* **Smaller visual clean-up**. Removed unnecessary drop shadows and made various small text and hover-state improvements across the app.
* **Copy- and loading-state updates**. Refreshed the sanity inspection warning banner, the VCS set-up step, and 
the "Qodana is getting ready" loading screen text. Replaced free-text filter inputs with selectable snippets and added a progress bar to the set-up flow.

#### Bug fixes
{id="july-2026-new-features-bug-fixes"}

* **SSO page showed the wrong message for expired plans**. Fixed incorrect messaging and call-to-action shown on the SSO page for expired Ultimate Plus plans. 
* **"Report not found" error appeared incorrectly**. This is now fixed.
* **Report page loader got stuck after manual CI/CD set-up**. Fixed the loader persisting after a manually configured CI/CD scan finished.
* **Reassigned projects stayed on their old page**. Fixed a Global Project Configuration bug where a project remained listed on its original page after reassignment until a manual refresh.
* **Collapsing inspection groups was broken on the report inspections tab**. This is now fixed.
* **"Copy link" button on problems was broken**. This is now fixed.
* **Report processing failures from date/time formatting**. Fixed report processing failures caused by unexpected date/time formats in scan data.
* **False "malicious dependency" flag for `ngx-bootstrap`**. This is now fixed.
* **Uploads with invalid licenses now blocked**. Previously these proceeded silently; they're now stopped as expected.

## June 2026

Here's a summary of everything that has been shipped in Qodana Cloud this month. As always, this covers
user-facing features, UI improvements, bug fixes, and stability work that affects your experience.

### Security
{id="june-2026-security"}

**Rate limiting added to the organizations API**. The `/api/v1/organizations`
endpoint now has proper rate limiting in place, closing a potential denial-of-service attack
vector.

### New features
{id="june-2026-new-features"}

#### Insights
{id="june-2026-new-features-insights"}

- **Code coverage trends over time**. The code coverage view in Insights now shows a
historical trend chart for the selected time period, so you can see how coverage has
evolved across your projects — not just the current snapshot.
- **Checks filter in Insights**. You can now filter Insights data by specific inspections, giving you
  more precise control over the data you're analyzing.

#### Settings & tokens
{id="june-2026-new-features-settings-and-tokens"}

- **Token list sortable in settings**. Organization project tokens can now be sorted by team
  name, project name, last used date, and expiration date, making it easier to manage
  tokens at scale.

#### Global configuration
{id="june-2026-new-features-global-configuration"}

- **Alerts when global configuration changes affect projects**. When a global
  configuration is modified in a way that disconnects or overrides connected projects, you
  now see an explicit in-app alert, instead of the change happening silently.

### UI improvements
{id="june-2026-ui-improvements"}

- **Redesigned report filters**. The filter panel has been overhauled with improved
  grouping and severity-based sorting, making it faster to zero in on the problems that
  matter.

### Bug fixes
{id="june-2026-bug-fixes"}

- **Token refresh button clipped for long names in Settings**. In the **Settings | Tokens**
  tab, the refresh action button was partially hidden when team or project names were
  long. This is now fixed.
- **"Open in GitHub" project button was unresponsive**. Fixed an issue where the button
  did not respond to clicks in certain states.

## January-May 2026

Starting today, the %product% team will publish a monthly summary of everything that has shipped in Qodana Cloud. 
Whether it’s a new feature, a bug fix, or a behind-the-scenes improvement that makes the platform faster or more reliable, you'll find it here.

We’ll publish each edition on a dedicated page in the Qodana documentation, so you'll always have a 
single place to check what's new. 

This first edition covers several months of accumulated changes to bring you fully up to date. 
Expect future posts to be considerably shorter.

### Security

The %product% team always prioritizes security updates. Here's what we addressed:

* **Stored XSS vulnerability fixed**. We patched a vulnerability that could allow malicious scripts to execute in a user’s browser via crafted links in Qodana Cloud.
* **Report sharing access controls hardened**. We tightened the access rules on report sharing endpoints to ensure only authorized users can access shared reports.
* **Session cookie now correctly expires on logout**. Previously, Self-Hosted deployments could leave a valid session cookie behind after logout. This has been fixed — logging out now fully invalidates the session.
* **OAuth PKCE parameters secured**. PKCE parameters are now passed inside the OAuth state parameter rather than as plain query parameters, closing a potential attack vector.
* **Critical dependency vulnerabilities patched**. Multiple critical and high-severity vulnerabilities in underlying dependencies — including the Go standard library, Netty, and OpenSSL — were addressed in our Docker images.

### New features

#### Language support

* **Ruby, C, and C++ linters** are now available in the onboarding flow, so you can get started with these languages directly from the UI.

#### Insights

* **Saved filter bookmarks in Insights**. You can now save your [Insights filter](insights.md#Dashboard+filters) combinations as named bookmarks and come back to them any time. No more reconfiguring the same filters after every visit.
* **Scan frequency in Insights**. Insights now show how frequently each project is being analyzed over a chosen look-back period, with the ability to view projects sorted by scan activity.

#### Project tokens

* **Token expiration dates**. When creating a [project token](project-token.md), you can now set an optional expiration date. Expired tokens are automatically rejected, giving you tighter control over long-lived credentials.
* **Organization token validity management**. In addition to per-project token expiration (already live), you’ll soon be able to configure validity timeframes for organization-level tokens as well, giving you consistent access control across the board.

#### Public API expansions

* **SSH public keys** for projects are now accessible via the Cloud API, enabling automated key management workflows.
* **Organization settings** can now be read and updated through the Cloud API.
* **Project insights and Insights data** are now exposed via the Cloud API.
* **List all inspections** via the Cloud API — useful for building custom integrations or tooling around your %product% reports.
* **The GET `/projects/{id}` endpoint** now returns additional fields: last report ID, last state, and last license key request timestamp.

#### Organization & team management

* **Bulk team invitations**. You can now invite multiple team members at once instead of adding them one by one.
* **Team invitations** now accept email arrays, consistent with the organization invitation API.
* **Reworked organization creation flow** for a smoother set-up experience.

#### Onboarding

* **SSO is now generally available**. The beta label has been removed, and the [feature](cloud-sso.md) is fully supported.
* **A ‘Wait for results’ step** with a dedicated loading indicator has been added to the project setup flow, so you always know what’s happening while your first report processes.

#### Report viewer

* **‘Open in Cursor’ support**. In addition to existing IDE support options, you can now open a problem directly in Cursor.
* **‘Open in VCS’ action** now adapts to the repository type (GitHub, GitLab, etc.) for each problem.
* **SARIF download improvements**. SARIF file handling in the [report](ui-overview.md) viewer has been overhauled, with better download support.
* **‘Expand/Collapse all’ button added** to the issue list in the report viewer for faster navigation of large reports.
* **Filters from Insights now carry over to the report** — when you navigate from Insights into a specific report, your active filters follow you.
* **Report tabs** have been refreshed with updated colors and more visually distinct styling.
* **Redesigned report filters** with improved grouping and severity sorting for faster navigation.

#### UI improvements

* **Global search on the organization page**. Find teams and projects from a single search bar without navigating.

### Performance and stability

* **Large repository contributor counts no longer cause memory errors**. We’ve optimized the contributor counting logic to handle repositories with very high contributor numbers gracefully.
* **License audit now streams large S3 objects** instead of loading them fully into memory, preventing out-of-memory failures on projects with large metadata files.
* **Report viewer handles large reports (300 MB+) without crashing**. A guard was added for oversized report loading so the app degrades gracefully rather than failing.
* **The license agreement is now checked before rendering any page**, eliminating a brief flash of content for users with pending agreements.

### Notable bug fixes

* **License activation is now case-insensitive**. Users whose JetBrains Account email contains uppercase letters could previously not activate licenses. This is now fixed.
* **API-created projects** now correctly support VCS settings (SSH/HTTPS) updates, which previously failed due to a missing internal repository record.
* **Switching repository URL type** from SSH to HTTPS no longer crashes the UI.
* **Expanded problems in the report** now render at the correct height when clicking "show more."
* **The "Choose a linter" dropdown** now shows explicit language support in brackets, e.g., JVM (Java, Kotlin, Groovy, JavaScript, TypeScript) and is now full-width, preventing content from being cut off.


That’s everything for this edition. If you have feedback or run into anything unexpected, please let us know through the in-app feedback button.