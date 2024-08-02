# Detect hard-coded passwords

<var name="hc-passwords" value="https://owasp.org/www-community/vulnerabilities/Use_of_hard-coded_password"/>

[Hard-coded passwords](%hc-passwords%) are a critical security issue. When exposed, the attacker can leak data and
access sensitive information.

Starting from version 2024.2,  %product% provides the `HardcodedPasswords` inspection that detects hard-coded passwords 
and covers the following languages: [](js.md), [](jvm.md), [](php.md), [](golang.md), [](python.md), [C#](dotnet.md),
JSON, YAML, and XML.

> The `HardcodedPasswords` inspection analyzes files tracked in git with the “unchanged” status.
{style="note"}

#### How it works

By default, the `HardcodedPasswords` inspection reports variables with values matching built-in regex rules for
hard-coded passwords. To report any variable with a suspicious name like `token` or `password` and a constant string value,
add the following configuration in the [`qodana.yaml`](qodana-yaml.md) file:

```yaml
hardcodedPasswords:
  reportDefaultSuspiciousVariableNames: true
```

You can specify your own regex rules to detect hard-coded passwords by saving them in the [`qodana.yaml`](qodana-yaml.md)
file, for example:

```yaml
hardcodedPasswords:
	# regex rules for variable values to report as hardcoded password
	variableValues:
	  - "[0-9a-z\\-_\\t.]{0,20}(?:[\\s|']|[\\s|\"]){0,3}(?:=|>|:=|\\|\\|:|<=|=>|:)(?:'|@\"|\"|\\s|=|\\x60){0,5}(?!([a-z]+\\.[a-zA-Z]+)|.*(\\d{4}-\\d{2}-\\d{2}|[a-z]+-[a-z]+.*)|:*(?!([\"']))[0-9A-Za-z]+\\.[0-9A-Za-z]+,|[A-Z]+_[A-Z]+_)(?<CONTENT>[0-9a-z\\-_.=~]{10,150})(?:['|\"\\n\\r\\s\\x60;]|$)"
	  - "perm:(?<clearSecret>[a-zA-Z=.0-9]{96}|[a-zA-Z=.0-9]{64})"
	
	# regex rules for variable names to report as hardcoded password
	variableNames:
		- "password"
	 
	# regex rules for variable values to ignore (not report) as hardcoded password
  ignoreVariableValues:
    - "do-not-report-this-value"
    
  # regex rules for variable names to ignore (not report) as hardcoded password
  ignoreVariableNames:
	  - "^(?=.*\bteamcity\b)(?=.*\bkey\b).*$"
```

To enable your custom hard-coded password setup, save the `HardcodedPasswords` configuration in the
[`qodana.yaml`](qodana-yaml.md) file:

```yaml
include:
  - name: "HardcodedPasswords"
```