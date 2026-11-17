# Authorization, scope, and safety checklist

Source of truth: [NASA VDP](https://www.nasa.gov/vulnerability-disclosure-policy/) and [live NASA Bugcrowd brief](https://bugcrowd.com/engagements/nasa-vdp). This summary is **not a scope grant**.

- [ ] Read the latest VDP and Bugcrowd brief immediately before testing.
- [ ] Identify the exact host, asset and environment explicitly listed in the live scope; connected third-party services are excluded unless explicitly authorized.
- [ ] Check prohibited test types, limitations, and reporting instructions.
- [ ] Confirm production vs non-production; use a non-production or public test environment when available.
- [ ] Verify that my testing could not impact availability, other people's data, or NASA operations.
- [ ] Ensure no automated scanner/tool is used unless explicitly allowed and compliant with program rules.
- [ ] Use own accounts and minimum proof necessary; no credential attacks or exfiltration.
- [ ] If vulnerable behavior or sensitive data appears: **STOP**, record only the minimum necessary private evidence and notify NASA promptly.
- [ ] Keep the finding confidential; do not post public GitHub issues or proof of concept prior to disclosure permission.

## Prohibited/unsupported examples in NASA's policy

- Denial-of-service and spamming
- Social engineering
- Unauthorized access, modification or transfer of data
- Automated-tool output with no evidence of real-world exploitability
- Reports that only note missing headers, TLS configuration or versions without clear exploitability
- Any asset outside the live in-scope targets

## Disclosure
Use Bugcrowd to report NASA findings: https://bugcrowd.com/engagements/nasa-vdp

Avoid public disclosure while NASA mitigates; current policy requests no sharing for 90 days after initial submission unless otherwise coordinated.

## Private research note fields
Date (UTC), exact scoped hostname, official source confirming scope, policy checked at (UTC), permitted test category, observation, minimal private reproduction evidence, impact, stop condition, reporting status.

Never store passwords, tokens, personal data, production raw responses, or an unpatched finding in GitHub.
