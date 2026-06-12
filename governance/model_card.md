# Model Card

## Model

llama3.2:latest running through Ollama for local testing.

## Intended Use

Internal HR policy question answering.

## Not Intended For

- Legal advice
- Medical advice
- Employment decision automation
- Compensation decisioning
- Investigation summaries
- Employee monitoring

## Known Risks

- RAG retrieval may surface restricted documents.
- Model may hallucinate policy if grounding is weak.
- Prompt injection may attempt to override confidentiality rules.
- Source citations may be incomplete.

## Evaluation Coverage Needed

- Confidential data leakage
- Prompt injection resistance
- Grounding accuracy
- Source attribution
- Protected characteristic bias
