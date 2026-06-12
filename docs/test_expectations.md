# Expected AGTH Test Interpretation

AGTH should detect:

## System Type

RAG assistant

## Domain

HR / employment

## Sensitive Data

- Compensation
- Medical leave
- HR investigations
- Legal holds
- Performance improvement plans
- Workforce planning notes

## Primary Tests Expected

- Confidential data protection
- Role-based access control
- Prompt injection resistance
- Hallucination / unsupported HR policy
- Source citation behavior
- Bias / protected characteristic handling
- FinOps risk due to no caching and multiple model calls

## Expected Report Style

The report should explain findings in plain language:

- What was tested
- What happened
- Why it matters
- What to fix
- How to retest
