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

<link-summary>Post-quantum cryptography inspections are categorized into several groups, with some groups corresponding to specific NIST PQC security categories. Each higher category imposes stricter requirements and identifies a broader range of vulnerabilities.</link-summary>

Post-quantum cryptography inspections are categorized into several groups, with some groups corresponding to specific
[NIST PQC](https://csrc.nist.gov/pubs/ir/8547/ipd) security categories. Each higher category imposes stricter 
requirements and identifies a broader range of vulnerabilities.

| Inspection group / NIST PQC security category | Description                                                                 | Reference benchmark (defines the category)                   |
|-----------------------------------------------|-----------------------------------------------------------------------------|--------------------------------------------------------------|
| `PqcMinLevel1` / non-compliant with NIST PQC                             | Pre-quantum and legacy cryptography vulnerabilities                         | Key search on a block cipher with a 128-bit key (AES-128)    |
| `PqcMinLevel2` / 1                            | `PqcMinLevel1` + baseline post-quantum algorithms                           | Collision search on a 256-bit hash function (SHA-256)        |
| `PqcMinLevel3` / 2                            | `PqcMinLevel2` + standard-strength post-quantum algorithms                  | Key search on a block cipher with a 192-bit key (AES-192)    |
| `PqcMinLevel4` / 3                            | `PqcMinLevel3` + high-strength post-quantum algorithms                      | Collision search on a 384-bit hash function (SHA3-384)       |
| `PqcMinLevel5` / 4                            | `PqcMinLevel4` + all algorithms except those providing maximum security     | Key search on a block cipher with a 256-bit key (AES-256)    |
| `AllPqcInspections` / 5                              | Every PQC inspection at any level     | Every case at every level    |

In this table, each group above `PqcMinLevel1` incorporates the inspections of the lower groups. 
For instance, `PqcMinLevel2` includes all the inspections of the `PqcMinLevel1` level and so on.

## Run post-quantum cryptography

<link-summary>You can enable any inspection group using the 'inspections.group' key in your YAML configuration.</link-summary>

You can enable any inspection group using the `inspections.group` key in your YAML configuration, for example: 

```yaml
version: "1.0"

profile:
  name: qodana.recommended
  inspections:
    - group: PqcMinLevel<number> / AllPqcInspections
      enabled: true
```

Once configured, run the %jvm% linter as explained in the [](jvm.md#Run+Qodana) chapter of the %jvm% documentation.

