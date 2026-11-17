# Private vulnerability report template

> **TEMPLATE ONLY.** Do not publish a live, unpatched vulnerability or sensitive evidence in a GitHub repository. Store completed drafts privately and submit NASA reports only through its official Bugcrowd engagement.

## Summary
- Title: [clear vulnerability + affected component]
- Target: [exact authorized in-scope host and path]
- Discovery date (UTC): [date]
- Policy checked (UTC) and scope reference: [live Bugcrowd brief]
- Category: [e.g., access control, XSS, injection]
- Suggested severity: [justify with actual impact; final decision belongs to NASA/Bugcrowd]

## What is vulnerable?
[Concise technical explanation in English if possible. Avoid unsubstantiated claims.]

## Reproduction (minimum impact)
1. [Starting state, using only your own test account/data]
2. [Exact permitted request or user action]
3. [Observed result]
4. [Expected secure result]

## Verified impact
[Show why this matters, using dummy/test data where possible. No exfiltration or further exploitation.]

## Evidence
[Reference to secure private screenshots or redacted requests; never put tokens/PII in repo.]

## Suggested remediation
[Smallest actionable fix and/or developer guidance.]

## Responsible disclosure
- Test stopped on confirmation: [yes/no]
- Date submitted on Bugcrowd: [not yet]
- Bugcrowd report ID: [private]
- NASA/Bugcrowd status: [not submitted / triaged / accepted / fixed]
- Publication authorization: [none unless explicitly received]
