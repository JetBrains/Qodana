<no-index/>

# Backend

<warning>This section is in progress, so we do not recommend to use it.</warning>

## 1.8.0

Release date: 16 July 2024

### Fixes
{id="180-fixes"}

* GitHub automatic setup in Qodana Cloud was adapted to custom Qodana Cloud URLs
* The `AdminServiceTest` service was extended with sleep time between generating new tokens and calling the API
* Distinguishing among Ktor HTTP clients was implemented using the `user-agent` string of request senders
* Version endpoints of Qodana Cloud return correct version data
* The `analysisId` parameter is escaped while uploading %product% reports

## 1.9.0

Release date: 25 July 2024

### Features
{id="190-features"}

* The backend can generate dummy values for the frontend API
* The endpoint `organizations/:organizationId/vcs/:vcsId/` returns the type of Qodana Cloud account
* Pagination for the `teams/:id/users` when listing team users
* The `/linters/v1/linters/license-key` endpoint returns organization IDs in a hashed form
* GitHub automatic project setup can accept various %product% Cloud APIs
* Version endpoints return the correct version
* The Qodana Cloud profile was refactored
* Test cases for organization API tokens
* Code coverage measurement for integration tests using JaCoCo

### Fixes
{id="190-fixes"}

* Incorrect status return for the [license audit](license-audit.topic) feature between the backend and frontend parts of Qodana Cloud
* The `/organizations/{id}/vcs/{vcs_id}/accounts` endpoint now returns responses about linking to %product% in the `isLinkedToQodana` object
* The `/repositories` endpoint was fixed to fetch the list of repositories in GitHub
* Repeated creating a team and project with the same name after deletion was enabled
* Running %product% while merging changes was recovered

## 1.10.0

Release date: 14 August 2024

### Features
{id="1100-features"}

* The endpoint for creating teams and projects automatically from users' build pipelines
* Code coverage for TeamCity pipelines
* The random initialization vector for SSH key generation
* The types of %product% analysis are distinguished between a full repository or files modified by some commits
* Extracting a linter name and version into %product% reports
* CodeHorizon API with dummy responses

### Fixes
{id="1100-fixes"}

* Improved project filtering in the `projects/search` request based on network protocols
* Unified error messaging in case of an invalid or deleted organization token
* Timestamps implemented for all deletion actions for teams and projects
* For the `users/me` endpoint, e-mail addresses are now used for binding user accounts between Qodana Cloud and JetBrains IDEs
* License audit status was fixed for uploading reports of projects without dependencies
* Unit tests were implemented for FUS events
* Integration test parallel execution was assigned to jUnit
* Vulnerable dependencies were updated for the `guava`, `bouncycastle` and `jsch` libraries
* The Ktor version was updated from 2.2.4 to 2.3.12
* The report cleaner was fixed to exit correctly
* The functionality of moving projects between teams was implemented

## 1.11.0

Release date: 29 August 2024

### Features
{id="1110-features"}

* Report processing logic extracts information about severity, baseline, and reports that contain no problems
* Soft deletion of organizations leads to complete deletion after 30 days
* The CodeHorizon API contract
* The `AgreementTest` tests

### Fixes
{id="1110-fixes"}

* Eliminated organization update using empty parameters
* Deletion of unknown branches was implemented
* The `projectCount` and `teamCount` endpoints were upgraded for ignoring deleted entities
* The flaky unit test for scheduled FUS statistics was fixed

## 1.11.1

Release date: 23 September 2024

### Features
{id="1111-features"}

* The v.1 of the `inspectopedia` client retrieves information about inspections in JSON format
* The JaCoCo code coverage Gradle plugin was replaced with IntelliJ coverage agent (Kover)
* The project token validation and checking for existence in a Qodana Cloud database
* Tests for hard entity deletion
* Performance tests for TeamCity configurations with the JBA approach

### Fixes
{id="1111-fixes"}

* Slow database queries for team and organization endpoints were fixed
* Updated `user_invited` event log entry description in Qodana Cloud log
* Sequential scan query was updated to consume less CPU resources
* The `PaginatedList` class was rewritten to become a class with explicit type to check for its usage
* The response 500 was fixed while inviting new team members
* Invalidation mechanism for old [project tokens](project-token.md) was implemented
* The `Request` class was tested using the Allure Framework
* Code coverage inspections were removed from separate modules and the quality gate was set for Qodana

## 1.12.0

Release date: 14 October 2024

### Features
{id="1120-features"}

* All state check endpoints were unified across all Qodana Cloud entities
* Storage mechanism for inspection metadata using Postgres
* JetBrains IDE tests for a new Qodana Cloud client
* Request methods for VCS Integration in the Integration Tests suite

### Fixes
{id="1120-fixes"}

* Qodana Cloud routes are trimmed according to the requirements of the Prometheus monitoring platform
