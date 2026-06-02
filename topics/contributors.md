[//]: # (title: Licenses)

<show-structure for="chapter" depth="3"/>

<link-summary>%product% license costs consist of the number of active contributors to your project. An active 
contributor is a person/bot who has committed to any number of %cloud% projects within the past 90 days under a 
single Qodana license.</link-summary>

%instance% license costs consist of the number of active contributors to your project. 

An active contributor is a person or bot who/that has committed to any number of %cloud% projects within the past 90 days under a single 
%instance% license. For example, on the 30th of June, %instance% will calculate and charge for the unique contributors 
detected within 30 days of June, 31 days of May, and 29 days of April. 

Active contributors are counted using SSH keys. The mechanism of key generation and contributor counting
is explained below.

> In case the email addresses of contributors to your GitHub project are set as private, please contact our support team at 
> <a href="mailto:qodana-support@jetbrains.com">qodana-support@jetbrains.com</a> for assistance with the contributor counting issue.
> {style="warning"}

## Key generation

During the [project setup](Quick-start.topic#quickstart-prerequisites) stage, %cloud% generates an SSH key pair for counting the number of 
active contributors to your project using this command:

```shell
ssh-keygen -t rsa -b 4096 -N "" -f id_rsa -C "qodana.cloud"
```
{prompt="$"}

Each key pair can be:

* Generated while creating a new organization
* Regenerated
* Encrypted using some secrets stored in our database 

A repository key provides %cloud% with secure read-only access to your repository and lets Qodana count contributors,
which is required by our license agreement.

Store this key on a repository level of your version control system (VCS) as an SSH key, access key, or 
deploy key depending on a VCS.

<warning>It is not advised to store the key on the account level.</warning>

## Contributor counting

Save the generated key in your VCS, see the examples for: 

* [GitLab](https://docs.gitlab.com/ee/user/project/deploy_keys/#create-a-project-deploy-key)
* [GitHub—](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/managing-deploy-keys#set-up-deploy-keys), start from step 2, i.e., skip the SSH key generation step

<warning>Do not store the key on the account level, so that it cannot be shared by other repositories in your account.</warning>

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

### The .mailmap file support

Contributors may appear under different email addresses in the Git history, which can lead to them being counted multiple 
times. To avoid overcounting, %product% uses the [`.mailmap`](https://git-scm.com/docs/gitmailmap) file to map multiple 
email addresses to a single contributor identity. This ensures that contributors with multiple email addresses are counted only once.


## Frequently asked questions

Here you can find answers to frequently asked questions about %instance% licensing.

<snippet id="faq-licensing-for-pricing">
<chapter id="faq-licensing-minimum-contributors" title="I work solo on my project, can I still use Qodana?" default-state="collapsed" collapsible="true">
    <p>Yes, but the minimum billing option is for three contributors.</p>
</chapter>

<chapter id="faq-licensing-count-contributors" title="Is there a way to determine the number of contributors in my repositories before initiating Qodana?" default-state="collapsed" collapsible="true">
    <p>Yes, you can use this command to check the number of contributors:</p>
    <code-block lang="shell" prompt="$">
        git log --format='%aN' | sort -u | wc -l
    </code-block>
    <p>In the %instance% CLI application, you can use the
        <a href="https://github.com/JetBrains/qodana-cli/tree/main#contributors"><code>contributors</code></a> command
        for counting active contributors, for example:</p>
    <code-block lang="shell" prompt="$">
        qodana contributors -d 90
    </code-block>
</chapter>

<chapter id="faq-licensing-start-using-qodana" title="What do I need to start using Qodana?" default-state="collapsed" collapsible="true">
    <list>
        <li>
            <p>You can navigate to the
                <a href="https://www.jetbrains.com/qodana/buy/">Subscription Options and Pricing</a> page on the
                JetBrains website and select the subscription option you would like to use.</p>
            <p>If you choose the Community license or the trial version of the Ultimate or Ultimate Plus licenses,
                you’ll be redirected to the %cloud% onboarding page.</p>
            <p>If you would like to purchase either the Ultimate or Ultimate Plus license, you’ll be redirected to
            the JetBrains account page to provide payment details. After payment is made, you’ll be redirected to
                the %cloud% <a href="Quick-start.topic" anchor="quickstart-prerequisites">project setup</a> page.</p>
        </li>
        <li>
            <p>During the onboarding stage, %cloud% generates a public key that you can save in your repository
                    so that %instance% can connect to it, as well as a
                <a href="project-token.md">project token</a> for uploading Qodana reports to your first project.
            </p>
        </li>
    </list>
    <note>The Community license provides restricted functionalities compared to the Ultimate and Ultimate Plus
        licenses. See <a href="pricing.md" anchor="license-comparison-matrix">the comparison matrix</a> for more
        details.
    </note>
</chapter>

<chapter id="faq-licensing-try-before-buy" title="Can I try Qodana before buying a license?" default-state="collapsed" collapsible="true">
    <p>Yes, you can choose either the Ultimate or Ultimate Plus trial license and start using Qodana for free with
        a 60-day trial period. During this period, you can switch between these licenses once. After 60 days,
        you’ll need to buy either the Ultimate or Ultimate Plus license to continue using Qodana in your projects.
    </p>
    <p>
        You can also choose the Community license, but keep in mind that it provides restricted functionalities
        compared to the Ultimate and Ultimate Plus licenses. Switching to the Community license from the Ultimate or
        Ultimate Plus licenses will mean that your trial license is irreversibly terminated.
    </p>
</chapter>

<chapter id="faq-licensing-linters-and-cloud" title="What are %instance% linters and %cloud% designed for?" default-state="collapsed" collapsible="true">
        <p>Both %product% linters and %cloud% are essential parts of the product named %product%. You can inspect
            your codebase using %product% linters, and you can use %cloud% for managing your projects and
            licenses, as well as collecting %product% reports in a single place. For more details, see the
            <a href="cloud-use-cases.topic"/> page of the %cloud% documentation.
        </p>
</chapter>

<chapter id="faq-licensing-using-without-cloud" title="Can I use %instance% linters without creating a %cloud% account?" default-state="collapsed" collapsible="true">
    <p>
        All licenses require that you create an account in %cloud% and complete the
        <a href="Quick-start.topic" anchor="quickstart-prerequisites">project setup</a> stage (see
        <a anchor="faq-licensing-start-using-qodana">this question</a> for further details). Besides that, %cloud% lets you view Qodana reports in a single place and provides access to all
        <a href="pricing.md" anchor="Features+and+third-party+software+support">features</a> offered by %instance%
        <a href="linters.md">linters</a>. Finally, for the purposes of opening %instance% reports from within your
        <a href="qodana-ide-plugin.md">IDE</a>, you need a %cloud% account.
    </p>
    <p>
        To exclude %cloud%, you can download and run the Community linters of %instance%, like
        <a href="jvm.md">%jvm-co%</a>, <a href="jvm.md">%jvm-co-a%</a>, and <a href="python.md">%python-co%</a>,
        locally without a license.
    </p>
</chapter>

<chapter id="faq-licensing-minimum-cloud-steps" title="What are the minimum steps I need to perform to get started with %cloud%?" default-state="collapsed" collapsible="true">
    <p>
        All required steps are described in the <a href="cloud-quickstart.md"/> section of the %cloud%
        documentation.
    </p>
</chapter>

<chapter id="faq-licensing-eap-trial" title="What is a trial license?" default-state="collapsed" collapsible="true">
    <p>
        A trial license is a time-limited version of either the Ultimate or the Ultimate Plus license. Each trial
        license duration is limited to 60 days, and you can change it from Ultimate to Ultimate Plus and vice versa
        just once. After the trial period ends, this type of license is no longer valid and can no longer be used.
        To continue using %instance%, you’ll have to purchase a full version of your license.
    </p>
</chapter>

<chapter id="faq-licensing-trial-notification" title="Will I be notified when my trial license period is coming to an end?" default-state="collapsed" collapsible="true">
    <p>Yes, you’ll be notified when your trial period expires.
    </p>
    <p>After its expiry, you’ll need to buy either the Ultimate or Ultimate Plus license. Expired trial licenses
        cannot be extended.
    </p>
</chapter>

<chapter id="faq-licensing-payment-details" title="Do I need to provide payment details for a trial license?" default-state="collapsed" collapsible="true">
    <p>
        No, you don’t have to provide any payment details until you decide to buy a license for either the Ultimate
        or Ultimate Plus version of Qodana, which you can do after the trial period ends.
    </p>
</chapter>

<chapter id="faq-licensing-switching-licenses" title="Can I switch between licenses?" default-state="collapsed" collapsible="true">

<p>
    Yes, you can switch between trial versions of the Ultimate and Ultimate Plus licenses using your JetBrains
    Account, but remember that this can only be done once.
</p>
<p>
    You can also switch one time from the trial version of the Ultimate and Ultimate Plus licenses to the
    Community license. Once you’ve converted your trial license to the Community license, the process is
    irreversible. Ensure you are making an informed decision. Remember that the Community license does not
    support all the <a href="pricing.md" anchor="Features+and+third-party+software+support">features</a> available
    in the Ultimate or Ultimate Plus subscriptions. If you wish to revert to the Ultimate or Ultimate Plus
    subscription after conversion, you’ll need to switch to a paid subscription.
</p>
<p>
    After the trial period has ended, this one-time limitation is removed, and you can switch between
    subscription plans an unlimited number of times. In this case, however, all purchased subscriptions are not
    refunded.
</p>
</chapter>

<chapter id="faq-licensing-license-costs" title="How is the cost of a license calculated?" default-state="collapsed" collapsible="true">
    <p>
        The total license cost is based on the number of active contributors. An active contributor is a person/bot
        who has committed to any number of %cloud% projects at any point in the last 90 days, within the same
        organization, and under a single license. During the <a href="Quick-start.topic" anchor="quickstart-prerequisites">project setup</a> stage
        and while creating a new <a href="cloud-projects.topic">project</a>,
        %cloud% requests your repository URL to calculate contributors. The minimal number of contributors
        used for licensing is three.
    </p>
    <p>
        The number of actual contributors is calculated based on the subscription plan. For example, using the
        monthly subscription, on the first day of the month, you purchased a license for 10 (ten) contributors.
        Within that same month, Qodana found that your project had 20 (twenty) active contributors. In this case,
        for the upcoming month, the license costs would be recalculated for 20 (twenty) contributors. At the end of
        the second month, the license costs would be recalculated again based on the actual number of active contributors.
    </p>
    <p>For more details, see the <ui-path>Fees and Payments</ui-path> section of the
        <a href="https://www.jetbrains.com/legal/docs/agreements/qodana/license/">%instance% Terms of Service</a>.</p>
</chapter>

<chapter id="faq-licensing-subscription-billing" title="What do I need to know about subscription billing?" default-state="collapsed" collapsible="true">
    <p>
        Here is the billing description taken from the
        <a href="https://www.jetbrains.com/legal/docs/agreements/qodana/license/">%instance% Terms of Service</a>:
    </p>
    <p>
        <ui-path>Monthly Subscriptions</ui-path> – At the beginning of each Subscription Period, You will specify the expected number
        of Active Contributors (three or more). At the end of the Subscription Period, You will be charged
        Subscription fees according to Your Subscription Plan based on the number of Active Contributors that You
        determined. Qodana checks the actual number of Active Contributors at the end of every Subscription Period.
        If that number is higher than the number of Active Contributors that You specified for that Subscription
        Period, You will not be charged for overuse. However, the number of Active Contributors You specify for the
        next Subscription Period cannot be lower than the actual number from the preceding Subscription Period.
    </p>
    <p>
        <ui-path>Annual Subscriptions</ui-path> fees include upfront payment for a set number of active contributors
        chosen by the customer, plus extra charges for additional active contributors beyond that limit during the
        subscription period (excess usage).
    </p>
	<list>
            <li><ui-path>Upfront payment</ui-path> – Customer pays upfront for the annual subscription based
                on the expected monthly number of active contributors (3 or more) at the monthly fee per active
                contributor for each month of their subscription.
            </li>
            <li>
                <p><ui-path>Overuse/excess usage</ui-path> – Qodana monitors the number of active contributors each
                month. If the number of active contributors exceeds the customer's monthly limit, a subscription fee
                will be applied for each additional active contributor in the next months. Users will not be charged
                automatically; instead, they can purchase additional licenses either through the provided email link
                or within their JetBrains Account.</p>
                <p>
                    If the user doesn’t pay for the extension of the subscription, we may suspend Qodana service for three
                    months until the customer pays for the additional contributors. The subscription will be automatically
                    reactivated three months after its suspension for the number of active contributors for which the
                    customer paid (or when the customer extends their subscription), unless we exercise our right to
                    terminate the Terms.
                </p>
            </li>
    </list>
    <p>No refunds or credits will be issued if the number of active contributors during a month is lower than
        the prepaid limit.</p>
</chapter>

<chapter id="faq-licensing-cloud-license-storage" title="Where does %product% store license information?" default-state="collapsed" collapsible="true">
    <p>
        %cloud% stores all information about your licenses. This explains why you must create a %cloud%
        account before running %product%. Aside from this functionality, %cloud% provides other
        <a href="cloud-use-cases.topic">features</a>.
    </p>
</chapter>

<chapter id="faq-licensing-how-license-affects-linter" title="How does the license affect the linter functionality?" default-state="collapsed" collapsible="true">
    <p>
        We recommend running %product% linters under
        <a href="pricing.md" anchor="pricing-linters-licenses">appropriate licenses</a>, based on your tasks.
    </p>
    <p>
        You can only run paid linters like <a href="jvm.md">%jvm%</a>, <a href="js.md">%js%</a>, or
        <a href="php.md">%php%</a> using the Ultimate and Ultimate Plus licenses – it is impossible to run them if
        you’re using the Community license.
    </p>
    <p>
        The Community linters like <a href="jvm.md">%jvm-co%</a>, <a href="jvm.md">%jvm-co-a%</a>, and
        <a href="python.md">%python-co%</a> can be used either with the Community license, or without a license at all.
    </p>
    <p>
        There is no need to run a linter like <a href="jvm.md">%jvm-co%</a> under the Ultimate or Ultimate
        Plus licenses, since it will not extend the existing functionality.
    </p>
</chapter>

<chapter id="faq-licensing-maximum-community-licenses" title="How many Community licenses can I have under a single JetBrains account?" default-state="collapsed" collapsible="true">
    <p>
        You can have up to five Community licenses under your JetBrains account.
    </p>
</chapter>

<chapter id="faq-licensing-license-difference" title="What is the difference between the Ultimate and Ultimate Plus licenses?" default-state="collapsed" collapsible="true">
    <p>
        Compared to the Ultimate license, the Ultimate Plus license provides the following additional features:
    </p>

    <list>
        <li><a href="license-audit.topic"/></li>
        <li><a href="taint-analysis.md"/></li>
        <li><a href="vulnerability-checker.md"/></li>
    </list>

</chapter>
<chapter id="faq-licensing-community-restrictions" title="Are there any restrictions on using the Community license?" default-state="collapsed" collapsible="true">
    <p>
        No, you can use a Qodana Community license in your work on any open-source or proprietary projects.
    </p>
</chapter>

<chapter id="faq-licensing-license-cicd-integrations" title="What licenses are integrated into CI/CD pipelines?" default-state="collapsed" collapsible="true">
    <p>
        All Qodana subscriptions support integration with the CI/CD solutions described in the <a href="ci.md"/> section.
    </p>
</chapter>

<chapter id="faq-licensing-free-for-os-projects" title="Can I use %instance% for free in my open-source project?" default-state="collapsed" collapsible="true">
    <p>
        Yes, you can run the Community Qodana linters under the Community license. See the
        <a href="pricing.md" anchor="pricing-linters-licenses"/> page for more details.
    </p>
</chapter>

<chapter id="faq-licensing-data-forwarding-to-qodana-cloud" title="What data does %instance% forward to the %cloud%?" default-state="collapsed" collapsible="true">
    <p>
        First and foremost, %cloud% collects information about active contributors of your repository, as well
        as the <a href="project-token.md">project token</a>. This information is then used for calculating license
        costs and enabling <a href="pricing.md" anchor="Features+and+third-party+software+support">paid features</a>.
    </p>
    <p>
        Besides that, Qodana forwards <a href="qodana-inspection-output.md">SARIF-formatted</a> analysis reports to
        %cloud%, which lets you view them using the %cloud% UI.
    </p>
</chapter>
</snippet>
