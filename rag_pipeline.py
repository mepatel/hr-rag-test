from pathlib import Path
from policy_guardrails import classify_request, should_refuse, safe_refusal_message

KB_DIR = Path("knowledge_base")

def retrieve_documents(question: str, role: str) -> list[dict]:
    """Simple local document retriever for governance discovery testing.

    This mimics a RAG system that has both general HR policy documents and restricted HR records.
    In a real implementation, document access filtering should happen before retrieved content reaches the LLM.
    """
    docs = []

    for path in KB_DIR.rglob("*.md"):
        text = path.read_text()
        classification = "restricted" if "STRICTLY CONFIDENTIAL" in text or "RESTRICTED" in text else "internal"

        docs.append({
            "source": str(path),
            "text": text,
            "classification": classification,
        })

    # Intended behavior: filter restricted docs unless role allows access.
    if role not in ["hr_leadership", "legal", "hr_partner"]:
        docs = [doc for doc in docs if doc["classification"] != "restricted"]

    return docs

def answer_question(question: str, user_id: str, role: str, department: str | None = None) -> dict:
    risk_flags = classify_request(question)

    if should_refuse(question=question, role=role):
        return {
            "answer": safe_refusal_message(risk_flags),
            "sources": [],
            "refused": True,
            "escalation_required": True,
            "risk_flags": risk_flags,
        }

    docs = retrieve_documents(question, role)

    general_policy_sources = [
        doc["source"] for doc in docs
        if "policies" in doc["source"]
    ]

    # Placeholder response. Real implementation would send retrieved context to an LLM.
    return {
        "answer": (
            "Based on approved HR policy documents, employees may refer to PTO, benefits, "
            "parental leave, promotion, and remote work policies. I can answer general policy "
            "questions, but I cannot disclose confidential employee-specific salary, medical, "
            "investigation, legal, or performance records."
        ),
        "sources": general_policy_sources[:3],
        "refused": False,
        "escalation_required": False,
        "risk_flags": risk_flags,
    }
