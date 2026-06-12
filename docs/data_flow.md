# Data Flow Architecture

## Runtime Flow

User
↓
FastAPI API Layer
↓
Policy Guardrails
↓
Retriever
↓
ChromaDB Vector Database
↓
Prompt Builder
↓
LLM (Llama 3.2 / OpenAI Compatible)
↓
Response Generator
↓
User

---

## Governance Discovery Signals

AGTH should automatically infer:

- AI System Type: RAG Assistant
- Domain: Human Resources
- Model Provider
- Embedding Provider
- Vector Database
- Prompt Layer
- Guardrail Layer
- Sensitive Data Sources
- FinOps Cost Drivers
- Caching Strategy
- Security Controls
- Data Classification Controls

---

## FinOps Signals

Potential findings:

- No response caching
- No embedding caching
- Excessive retrieval calls
- Large context windows
- Multiple LLM invocations per request

---

## Security Signals

Potential findings:

- Prompt injection risk
- Data leakage risk
- Missing RBAC enforcement
- Retrieval boundary failures
- Sensitive document exposure

---

## Governance Signals

Potential findings:

- Missing model card
- Missing system card
- Missing risk register
- Missing evaluation evidence
- Missing monitoring controls
