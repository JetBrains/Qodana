[//]: # (title: Contributor counting)

%product% license costs are comprised of the number of active contributors present in your project. An active contributor is a 
person/bot who has committed to any number of Qodana Cloud projects at any point in the last 90 days under a single 
%product% license. Active contributors are counted using SSH keys. The mechanism of key generation and contributor counting
is explained below.

## Key generation

During the [onboarding stage](cloud-onboarding.md), Qodana Cloud generates a public SSH key for saving in your VCS. 
This key lets %product% count the number of active contributors to your project. 

Qodana Cloud generates the key pair using this shell command: 

```shell
ssh-keygen -t rsa -b 4096 -N "" -f id_rsa -C "qodana.cloud"
```
{prompt="$"}

Each key pair can be:

* Generated each time a new organization is created, and one key pair is equivalent to one repository
* Regenerated when needed
* Encrypted using some secret stored in our database 

## Contributor counting

After you save the generated key in your VCS, %product% will use the following command to clone the project metadata 
of your repository: 

```shell
git clone -n --filter=blob:none --shallow-since='90 days ago' <repo>
```
{prompt="$"}

After cloning, using this command %product% will extract the contributors from all commits made for the last 90 days: 

```shell
git log --since '90 days ago' --pretty=format:%ae||%an||%H||%ai
```
{prompt="$"}
