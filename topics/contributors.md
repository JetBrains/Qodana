[//]: # (title: Contributor counting)

<link-summary>Qodana license costs are comprised of the number of active contributors to your project. An active 
contributor is a person/bot who has committed to any number of Qodana Cloud projects within the past 90 days under a 
single Qodana license.</link-summary>

%instance% license costs are comprised of the number of active contributors to your project. An active contributor is a 
person/bot who has committed to any number of Qodana Cloud projects within the past 90 days under a single 
%instance% license. For example, on the 30th of June, %instance% will calculate and charge for the unique contributors 
detected within 30 days of June, 31 days of May, and 29 days of March. 

Active contributors are counted using SSH keys. The mechanism of key generation and contributor counting
is explained below.

> In case the email addresses of contributors to your GitHub project are set as private, please contact our support team at 
> <a href="mailto:qodana-support@jetbrains.com">qodana-support@jetbrains.com</a> for assistance with the contributor counting issue.
> {style="warning"}

## Key generation

During the [onboarding stage](cloud-onboarding.md), Qodana Cloud generates an SSH key pair for counting the number of 
active contributors to your project using this command:

```shell
ssh-keygen -t rsa -b 4096 -N "" -f id_rsa -C "qodana.cloud"
```
{prompt="$"}

Each key pair can be:

* Generated while creating a new organization
* Regenerated
* Encrypted using some secret stored in our database 

## Contributor counting

After you save the generated key in your VCS, %instance% will use the following command to clone the project metadata 
of your repository: 

```shell
git clone -n --filter=blob:none --shallow-since='90 days ago' <repo>
```
{prompt="$"}

After cloning, %instance% will extract the contributors from all commits made for the last 90 days: 

```shell
git log --all --since '90 days ago' --pretty=format:%ae||%an||%H||%ai
```
{prompt="$"}

To calculate the number of contributors in your repository, you can use 
[Qodana CLI](https://github.com/JetBrains/qodana-cli#contributors) with the `contributors` option invoked, for example:

```shell
qodana contributors -d 90
```
{prompt="$"}


