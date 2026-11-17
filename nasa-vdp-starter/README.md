# NASA VDP Research Starter

> Independent learning and responsible disclosure workspace. **Not affiliated with or endorsed by NASA.**

Goal: develop practical web security skills, keep accurate records, and prepare high-quality reports if a genuine, authorized vulnerability is discovered. This is not a certificate, proof of discovery, or guarantee of a Letter of Recognition.

## Official references (verified 2026-11-18)
- NASA Vulnerability Disclosure Policy v1.6.2 (2026-04-30): https://www.nasa.gov/vulnerability-disclosure-policy/
- NASA Bugcrowd engagement (official report channel): https://bugcrowd.com/engagements/nasa-vdp
- PortSwigger Web Security Academy labs: https://portswigger.net/web-security
- OWASP Juice Shop: https://owasp.org/www-project-juice-shop/

## Before any real-world research
1. Re-read the current NASA policy **and the live Bugcrowd scope and testing restrictions**.
2. Testing is allowed **only on specifically listed in-scope targets**. Never infer that every NASA domain/subdomain is allowed.
3. Do not perform denial of service, spam, social engineering, credential attacks, uncontrolled automated scanning, data exfiltration, persistence, or production-disruptive testing.
4. Prefer intentionally vulnerable local labs. Stop immediately upon identifying a vulnerability or sensitive data, and notify NASA as directed in its policy.
5. Keep vulnerability details and evidence private. **Do not commit live findings, PII, secrets, screenshots, exploit payloads, or raw requests/responses to this public repository.**
6. Submit actual NASA findings through Bugcrowd, not public GitHub issues.

NASA notes that qualifying Letters of Recognition are for P1-P4 reports that are valid, accepted, and confirmed fixed, excluding duplicates/known issues. No monetary bounty is promised.

## Starter kit
- `docs/scope-and-safety.md`: rules, authorization gate, and stop conditions
- `docs/report-template.md`: sanitized report structure (store actual reports **privately** off public GitHub)
- `docs/learning-plan.md`: practical roadmap with authorized labs
- `tools/scope_guard.py`: **offline only**, exact-host allowlist verification
- `scope.txt`: initially empty. No targets are presumed authorized.
- `tests/test_scope_guard.py`: local unit tests

## Run offline checks
```bash
cd nasa-vdp-starter
python -m unittest discover -s tests -v
python tools/scope_guard.py https://example.org
```
With the default empty scope file, the URL is **DENIED**. This script does **not** scan or connect to anything.

When ready, manually add *exact* hosts verified against the current official in-scope list to `scope.txt`; this is just a local reminder and does not confer permission.

## Progress
- [x] GitHub starter workspace created on an isolated branch
- [x] Official policy reviewed
- [ ] Finish Web Security Academy labs
- [ ] Validate Bugcrowd registration and in-scope target selection
- [ ] Perform authorized research and privately document any findings
- [ ] Submit a genuine, reproducible vulnerability only if found
- [ ] Record acceptance/remediation/recognition only after independent confirmation
