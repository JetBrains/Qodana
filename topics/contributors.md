[//]: # (title: Contributor counting)

%product% license costs are comprised of the number of active contributors to your project. An active contributor is a 
person/bot who has committed to any number of Qodana Cloud projects at any point in the last 90 days under a single 
%product% license. Active contributors are counted using SSH keys as explained below.

## Key generation

During the [onboarding stage](cloud-onboarding.md) at Qodana Cloud, you can get a public SSH key that should be saved to 
your VCS. This key enables %product% to count the number of active contributors to your project, and the key pair is 
generated using this shell command: 

```shell
ssh-keygen -t rsa -b 4096 -N "" -f id_rsa -C "qodana.cloud"
```

In this case, each key pair can be:

* Generated each time a new organization is created, and one key pair is equivalent to one repository
* Regenerated when needed
* Encrypted using some secret stored in Amazon Secrets Manager and saved to our database 

## Contributor counting

After you save the generated key to your VCS, %product% will use this command to clone the project metadata of your repository: 

```shell
git clone -n --filter=blob:none --shallow-since='90 days ago' <repo>
```

After cloning, %product% will extract the contributors from all commits made for the last 90 days using this command: 

```shell
git log --since '90 days ago' --pretty=format:%ae||%an||%H||%ai
```

