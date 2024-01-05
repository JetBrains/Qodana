[//]: # (title: Taint analysis)

Taint analysis is the process of assessing the flow of untrusted user input throughout the body of a function or a method.
If you have a taint in your code, hackers can execute these code fragments to cause SQL injection, arithmetic overflow, 
cross-site scripting, path traversal, etc.

The core goal of the taint analysis is to determine if unanticipated input can affect program execution in malicious ways.

Taint analysis is supported only by the [Qodana for PHP](qodana-php.md) linter starting from version 2023.1 of %instance%.
This feature is available under the Ultimate Plus [license](pricing.md).

## How it works

Tainted data are called a **Source**, while a vulnerable function that may contain such data is a **Sink**.
In this case, tainted data travel from sources to Sinks via propagators, such as function calls or assignments.

<img src="taint-analysis.png" dark-src="taint-analysis_dark.png" width="706" alt="Taint analysis diagram" border-effect="line"/>

To prevent such propagation, the following approaches are applied by the Qodana for PHP inspections:

* Data sanitization, i.e. data transformation to the safe state. Here, tags are removed to resolve the taint:
    ```PHP
    <?php
    $taint = $_GET['some_key'];
    $taint = strip_tags($taint);
   ```
* Data validation, i.e. checking the data conforms with a required pattern. In this sample, validation for the `$email` variable is enabled:
    ```PHP
    <?php
    $email = $_GET['email'];
    if (filter_var($email, FILTER_VALIDATE_EMAIL)) {
      echo $email;
    }
    ```

## Running the taint analysis

<chunk id="running-taint-analysis">

  <p>In the <code>qodana.yaml</code> file,
  <a href="qodana-yaml.md" anchor="Include+an+inspection+into+the+analysis+scope">include</a> the 
  <code>PhpVulnerablePathsInspection</code> inspection into the analysis scope:</p>
  
  <code style="block" lang="yaml">
  include:
    - name: PhpVulnerablePathsInspection
  </code>
  
  <p>Alternatively, you can use the <code>inspections</code> section of <code>qodana.yaml</code>:</p>
  
  <code style="block" lang="yaml">
  inspections:
    - inspection: PhpVulnerablePathsInspection
      enabled: true
  </code>

</chunk>