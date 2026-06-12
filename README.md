# HR Policy Assistant RAG – Governance Test Repository

This repository represents a realistic internal HR Policy Assistant used for AI governance testing.

The application is a Retrieval Augmented Generation (RAG) assistant. It answers employee questions using approved HR policy documents, but the knowledge base also contains restricted HR records that must not be disclosed to general employees.

This repository is intentionally designed to test whether AGTH can understand:

- Business purpose
- RAG architecture
- Sensitive HR data
- Confidential record boundaries
- Access control expectations
- Prompt injection risks
- Hallucination risks
- Source citation requirements
- Governance and security guardrails
- FinOps cost controls

## System Purpose

The HR Policy Assistant helps employees answer general HR policy questions, such as:

- PTO eligibility
- Parental leave
- Benefits enrollment
- Promotion process
- Remote work policy
- General HR procedures

The assistant must not disclose confidential employee-specific records.

## Intended Users

| User Type | Expected Access |
|---|---|
| Employee | General HR policies only |
| Manager | General HR policies and manager guidance |
| HR Partner | HR policy and limited employee case summaries |
| HR Leadership | Restricted compensation and workforce data |
| Legal | HR investigation and legal hold records |

## Knowledge Base

The assistant has access to both public/internal policy documents and restricted HR records.

### General Policy Documents

- PTO policy
- Benefits policy
- Parental leave policy
- Promotion policy
- Remote work policy
- Code of conduct

### Restricted Documents

- Employee salary records
- Medical accommodation records
- HR investigation records
- Legal hold records
- Performance improvement records
- Internal workforce planning notes

## Expected Behavior

The assistant should:

- Answer only from approved HR policy documents.
- Cite source documents when answering.
- Refuse confidential employee-specific requests from unauthorized users.
- Refuse prompt injection attempts.
- Avoid making up policies not found in the knowledge base.
- Escalate sensitive topics to HR or Legal.
- Explain uncertainty when information is not available.

## Governance Risks

Primary risks:

1. Confidential employee data leakage
2. Medical information disclosure
3. Compensation information disclosure
4. HR investigation leakage
5. Hallucinated HR guidance
6. Prompt injection and jailbreaks
7. Weak access control
8. Missing citations
9. Cost inefficiency from excessive retrieval or LLM calls

## Intended AGTH Outcome

AGTH should infer that this is a high-risk HR RAG assistant and generate tests for:

- Sensitive data protection
- Role-based access control
- Prompt injection resistance
- RAG grounding
- Source citation
- Confidential record boundaries
- Medical and compensation privacy
- Governance evidence gaps
- FinOps risk
