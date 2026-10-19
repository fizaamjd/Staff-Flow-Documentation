# Current implementation

Prepared on 2026-10-19 from [StaffFlow source revision be4981f](https://github.com/fizaamjd/StaffFlow/tree/be4981f6b0c487c14db5f6931be8862ff2f6d969). This is a maintenance summary, not a backdated sprint record.

The Next.js browser application uses the Express API and MongoDB. Manager and employee views cover shifts, scheduling, profile data and notifications; payroll/report endpoints aggregate stored application data. JWT and role middleware protect routes, but their presence does not establish a completed security review.

The pure recommendation module scores department fit, availability, preferred days, weekly-hour pressure, overtime, consecutive days, fairness and skill. Same-date overlap and inactive status exclude a candidate. Other inputs affect scores and are not hard guarantees. The generator greedily assigns candidates and updates its running state; it can leave unfilled slots.

Generating a proposal differs from publishing it. Publication can write assignments and send application notifications. A reviewer should inspect the proposal before publishing. Overnight work, statutory payroll, globally optimal allocation and time-zone correctness have not been established by this maintenance work.

For current setup, tests, configuration and known limitations, use the [application README](https://github.com/fizaamjd/StaffFlow). The [live demo video](../README.md#live-demo-video) contains illustrative data, not a production audit.
