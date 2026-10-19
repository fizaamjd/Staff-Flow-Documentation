# StaffFlow Documentation

![CI](https://github.com/fizaamjd/Staff-Flow-Documentation/actions/workflows/ci.yml/badge.svg?branch=main)

Planning, research and presentation records for StaffFlow, a workforce-management application with explainable, rules-based shift scheduling. This repository separates original sprint artifacts from current implementation notes.

[Application source](https://github.com/fizaamjd/StaffFlow) · [Open StaffFlow](https://staff-flow-silk.vercel.app/)

## Live demo video

https://github.com/user-attachments/assets/b07edb3f-dc78-4230-a0f3-2187874fa91e

This is the application's motion walkthrough using sample staff and payroll data. It illustrates workflows; it is not evidence of real employment records, benchmark results or statutory compliance.

## Current implementation

- [Implementation guide](docs/current-implementation.md) — maintained capabilities and source references.
- [Feature traceability](docs/traceability.md) — claims mapped to implementation and verification scope.
- [Architecture](docs/architecture.md) — how the repositories and records relate.
- [Archive caveats](docs/archive-notes.md) — missing notes, inconsistent dates and unverified historical claims.

## Historical archive

Three Markdown records and one presentation contain content. Eleven standup files are empty placeholders; they are preserved and explicitly indexed rather than filled with invented meeting notes.

| Artifact | Record status |
| --- | --- |
| [Sprint 01 Daily Standup 01](Sprint%2001%20Documentation/Sprint%2001%20Daily%20Standup%2001.md) | Historical notes; see archive caveats |
| [Sprint 01 Daily Standup 02](Sprint%2001%20Documentation/Sprint%2001%20Daily%20Standup%2002.md) | Placeholder — no historical notes supplied |
| [Sprint 01 Daily Standup 03](Sprint%2001%20Documentation/Sprint%2001%20Daily%20Standup%2003.md) | Placeholder — no historical notes supplied |
| [Sprint 01 Daily Standup 04](Sprint%2001%20Documentation/Sprint%2001%20Daily%20Standup%2004.md) | Placeholder — no historical notes supplied |
| [Sprint 01 Daily Standup 05](Sprint%2001%20Documentation/Sprint%2001%20Daily%20Standup%2005.md) | Placeholder — no historical notes supplied |
| [Sprint 01 Daily Standup 06](Sprint%2001%20Documentation/Sprint%2001%20Daily%20Standup%2006.md) | Placeholder — no historical notes supplied |
| [Sprint 01 Daily Standup 07](Sprint%2001%20Documentation/Sprint%2001%20Daily%20Standup%2007.md) | Placeholder — no historical notes supplied |
| [Sprint 01 Daily Standup 08](Sprint%2001%20Documentation/Sprint%2001%20Daily%20Standup%2008.md) | Placeholder — no historical notes supplied |
| [Sprint 01 Daily Standup 09](Sprint%2001%20Documentation/Sprint%2001%20Daily%20Standup%2009.md) | Placeholder — no historical notes supplied |
| [Sprint 01 Daily Standup 10](Sprint%2001%20Documentation/Sprint%2001%20Daily%20Standup%2010.md) | Placeholder — no historical notes supplied |
| [Sprint 01 Daily Standup 11](Sprint%2001%20Documentation/Sprint%2001%20Daily%20Standup%2011.md) | Placeholder — no historical notes supplied |
| [Sprint 01 Daily Standup 12](Sprint%2001%20Documentation/Sprint%2001%20Daily%20Standup%2012.md) | Placeholder — no historical notes supplied |
| [Sprint 01 Planning Meeting](Sprint%2001%20Documentation/Sprint%2001%20Planning%20Meeting.md) | Historical notes; see archive caveats |
| [Staff-Flow Market Research Report](Sprint%2001%20Documentation/Staff-Flow%20Market%20Research%20Report.md) | Historical notes; see archive caveats |
| [StaffFlow - AI-Powered Employee Shift & Workload Manager - Presentation](StaffFlow%20-%20AI-Powered%20Employee%20Shift%20%26%20Workload%20Manager%20-%20Presentation.pptx) | Original project presentation |

## Maintaining the documents

Use Python 3.11 or newer. No application credentials or database are needed.

```sh
python3 scripts/check-docs.py
python3 scripts/check-archive.py
# After an intentional artifact change:
python3 scripts/update-inventory.py
```

New retrospectives must use their real creation date and identify their source revision. Preserve original participant names, dates, research attribution and presentation authorship. Keep private employee information and credentials out of Git. See [contributing](CONTRIBUTING.md), [testing](docs/testing.md) and [verification](docs/verification.md).

## License and support

[MIT](LICENSE) covers authorized original contributions; historical team and third-party rights remain separate. See [license scope](docs/license-scope.md), [support](SUPPORT.md), [security](SECURITY.md), [code of conduct](CODE_OF_CONDUCT.md) and [changelog](CHANGELOG.md).
