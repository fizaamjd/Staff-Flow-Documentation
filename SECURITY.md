# Security policy

## Reporting

Use [GitHub private reporting](https://github.com/fizaamjd/Staff-Flow-Documentation/security/advisories/new). Include the affected branch/commit, reproduction with synthetic data, impact and suggested mitigation. Do not post credentials, customer data, private repository contents, or real email in an issue. If a credential was exposed, revoke it through its provider; removing a file does not invalidate a token or erase earlier commits.

The maintained branch is `main`; there is no separate security support promise for old phase branches or tags. Dependency updates and CI checks do not establish a completed security audit.

## Known boundaries

- This repository contains public project records, not a private HR system. Never commit employee records, payroll information, passwords, tokens or customer data.
- Historical market research includes unverified pricing, product comparisons, performance and compliance statements. It is not current product evidence, legal guidance or a verified benchmark.
- The application lives in the separate StaffFlow repository and has its own security policy. Documentation CI validates links and artifact integrity, not the application's access control or deployment security.

Use dedicated development services and explicit secrets. Review provider permissions, public network exposure, data retention, and deployment access before using private data. No penetration test or production-readiness certification is claimed.
