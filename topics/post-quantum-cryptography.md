# Post-quantum cryptography (PQC)

Quantum computing poses a significant threat to widely used public-key cryptographic algorithms, such as RSA and ECC. 
Even before large-scale quantum computers are realized, organizations must address potential risks by 
using [post-quantum cryptography](https://en.wikipedia.org/wiki/Post-quantum_cryptography) techniques in projects.

The [%jvm%](jvm.md) linter provides inspections to identify vulnerable code and guide developers toward post-quantum 
cryptography (PQC) alternatives and available under the Ultimate and Ultimate Plus [licenses](pricing.md) and their trial 
versions. To learn more about the available licensing model, visit the 
[Subscription Options and Pricing](https://www.jetbrains.com/qodana/buy/?billing=yearly) page.
You can also [request a demo](https://www.jetbrains.com/qodana/request-a-demo/).

## Inspection levels

Post-quantum cryptography inspections are grouped into five levels with each level mapping to a respective
[NIST PQC](https://www.nist.gov/pqc) security level where higher levels are stricter and report more problems.

| Level          | Description                                                                                      |
|----------------|--------------------------------------------------------------------------------------------------|
| `PqcMinLevel1` | Most critical pre-quantum and legacy cryptography vulnerabilities                                |
| `PqcMinLevel2` | Baseline post-quantum algorithms and the `PqcMinLevel1` inspections                              |
| `PqcMinLevel3` | Standard-strength post-quantum algorithms and the `PqcMinLevel2` inspections                     |
| `PqcMinLevel4` | High-strength post-quantum algorithms and the `PqcMinLevel3` inspections                         |
| `PqcMinLevel5` | All algorithms except those providing maximum security, includes the  `PqcMinLevel4` inspections |

In this table, each level above `PqcMinLevel1` incorporates the inspections of the lower levels. 
For instance, `PqcMinLevel2` includes all the inspections of the `PqcMinLevel1` level and so on.

## Configure post-quantum cryptography




