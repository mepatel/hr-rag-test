# HR Assistant Access Control Policy

## Role-Based Access

| Role | Allowed Content | Restricted Content |
|---|---|---|
| employee | General HR policy | Salary, medical, investigation, legal, PIP records |
| manager | General HR policy and manager guidance | Individual salary, medical, investigation, legal records |
| hr_partner | General HR policy, limited case summaries | Legal privileged records |
| hr_leadership | Compensation and workforce planning | Legal privileged records unless authorized |
| legal | Legal hold, investigation, medical records as needed | None within approved matter scope |

## Required Behavior

- Apply role filtering before retrieval.
- Do not pass restricted documents to the LLM for unauthorized roles.
- Refuse restricted questions.
- Log restricted access attempts.
