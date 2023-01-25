[//]: # (title: Taint analysis)

Taint analysis is the process of assessing the flow of untrusted user input throughout the body of a function or a method.
If you have a taint in your code, hackers can execute these code fragments to cause SQL injection, arithmetic overflow, 
cross-site scripting, path traversal, etc.

The core goal of taint analysis is to determine if unanticipated input can affect program execution in malicious ways.

Currently, taint analysis is supported by the [Qodana for PHP](qodana-php.md) linter.

<!-- Here, I also need a redrawn image illustrating how taint analysis works -->
<!-- I also need to add this to the quick start guide in the doc -->

## How it works

Tainted data is called a Source, while a vulnerable function where this data shouldn’t be is a Sink. And tainted data 
goes from sources to sinks via propagators, such as function calls or assignments.

<!-- Here, I also need a redrawn image illustrating how taint analysis works -->

To prevent taint propagation, the following approaches can be applied:

* Sanitize the data, i.e. transform data to the safe state. In the example below, we removed tags to resolve the taint.
* Validate the data, i.e. checking that the added data conforms with a required pattern. In the example below, we enable validation for the $email variable.

The Qodana for PHP supports both methods of taint prevention. 