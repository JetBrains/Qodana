# Post-quantum cryptography (PQC)

<link-summary>Quantum computing poses a significant threat to widely used public-key cryptographic algorithms, such as RSA and ECC.
The %jvm% linter provides inspections to identify vulnerable code and guide developers toward post-quantum 
cryptography (PQC) alternatives.</link-summary>

Quantum computing poses a significant threat to widely used public-key cryptographic algorithms, such as RSA and ECC. 
Even before large-scale quantum computers are realized, organizations must address potential risks by 
using [post-quantum cryptography](https://en.wikipedia.org/wiki/Post-quantum_cryptography) techniques in projects.

The [%jvm%](jvm.md) linter provides inspections to identify vulnerable code and guide developers toward post-quantum 
cryptography (PQC) alternatives and available under the Ultimate and Ultimate Plus [licenses](pricing.md) and their trial 
versions. To learn more about the available licensing model, visit the 
[Subscription Options and Pricing](https://www.jetbrains.com/qodana/buy/?billing=yearly) page.
You can also [request a demo](https://www.jetbrains.com/qodana/request-a-demo/).

## Inspection groups

<link-summary>Post-quantum cryptography inspections are divided into five groups, with each group mapping to a corresponding
NIST PQC security category, where higher groups are stricter and report more problems.</link-summary>

Post-quantum cryptography inspections are divided into five groups, with each group mapping to a corresponding
[NIST PQC](https://csrc.nist.gov/pubs/ir/8547/ipd) security category, where higher groups are stricter and report more problems.

| Inspection group / NIST PQC security category | Description                                                                 | Reference benchmark (defines the category)                   |
|-----------------------------------------------|-----------------------------------------------------------------------------|--------------------------------------------------------------|
| `PqcMinLevel1` / 1                            | Pre-quantum and legacy cryptography vulnerabilities                         | Key search on a block cipher with a 128-bit key (AES-128)    |
| `PqcMinLevel2` / 2                            | `PqcMinLevel1` + baseline post-quantum algorithms                           | Collision search on a 256-bit hash function (SHA-256)        |
| `PqcMinLevel3` / 3                            | `PqcMinLevel2` + standard-strength post-quantum algorithms                  | Key search on a block cipher with a 192-bit key (AES-192)    |
| `PqcMinLevel4` / 4                            | `PqcMinLevel3` + high-strength post-quantum algorithms                      | Collision search on a 384-bit hash function (SHA3-384)       |
| `PqcMinLevel5` / 5                            | `PqcMinLevel4` + all algorithms except those providing maximum security     | Key search on a block cipher with a 256-bit key (AES-256)    |

In this table, each group above `PqcMinLevel1` incorporates the inspections of the lower groups. 
For instance, `PqcMinLevel2` includes all the inspections of the `PqcMinLevel1` level and so on.

## Run post-quantum cryptography

<link-summary>You can enable one PQC level from 1 to 5 at a time using the 'inspections.group' key in your YAML configuration.</link-summary>

You can enable one PQC level from 1 to 5 at a time using the `inspections.group` key in your YAML configuration, for example: 

```yaml
version: "1.0"

profile:
  name: qodana.recommended
  inspections:
    - group: PqcMinLevel<number>
      enabled: true
```

Once configured, run the %jvm% linter as explained in the [](jvm.md#Run+Qodana) chapter of the %jvm% documentation.

