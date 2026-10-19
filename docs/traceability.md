# Feature traceability

This table maps the maintained implementation rather than declaring every historical proposal complete.

| Area | Source | Verification boundary |
| --- | --- | --- |
| Candidate scoring and explanations | server/src/services/recommendation.js | Offline regressions cover hard exclusions, ranking, penalties and score bounds |
| Greedy scheduling and slot generation | server/src/services/recommendation.js | Offline regressions cover assignment conflicts, unfilled slots, date ranges and coverage |
| Accounts and roles | server/src/middleware/auth.js, routes/auth.js | Source inspected; live authentication/tenant behavior not exercised here |
| Shifts and employees | server/src/routes/shifts.js, employees.js | Source inspected; database integration not tested by offline scheduler tests |
| Payroll and reports | server/src/controllers/payrollController.js, reportController.js | Application estimates; no payroll certification or legal test |
| UI | app/, components/, lib/ | Type checking/build; no claim that every browser workflow is end-to-end tested |
| Sprint artifacts | Sprint 01 Documentation/ | Link/integrity checks; historical claims and missing notes remain unresolved |

Paths above are relative to [StaffFlow](https://github.com/fizaamjd/StaffFlow). Test results and dependency findings are recorded in that repository's maintained verification notes.
