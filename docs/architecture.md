# Architecture Summary

User
↓
FastAPI `/chat` endpoint
↓
Role and request metadata
↓
Policy guardrails
↓
RAG retriever
↓
Knowledge base folders:
- policies/
- restricted/
↓
Vector database / ChromaDB
↓
LLM provider / Ollama llama3.2
↓
Response with sources and refusal flags

## Important Governance Boundary

Restricted documents must be filtered before retrieval results are sent to the LLM.

## Risk

If restricted documents are passed into the LLM context, the assistant may disclose confidential data even if the prompt says not to.
