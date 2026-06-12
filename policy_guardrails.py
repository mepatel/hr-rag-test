CONFIDENTIAL_TOPICS = {
    "compensation": ["salary", "bonus", "compensation", "pay", "raise", "equity"],
    "medical": ["medical", "diagnosis", "mental health", "stress leave", "accommodation", "doctor"],
    "investigation": ["investigation", "complaint", "harassment", "misconduct", "disciplinary"],
    "legal": ["legal hold", "lawsuit", "settlement", "privileged", "counsel"],
    "performance": ["performance improvement", "pip", "termination risk", "manager notes"],
}

AUTHORIZED_ROLES_BY_TOPIC = {
    "compensation": ["hr_leadership"],
    "medical": ["hr_partner", "legal"],
    "investigation": ["hr_partner", "legal"],
    "legal": ["legal"],
    "performance": ["hr_partner", "legal"],
}

def classify_request(question: str) -> list[str]:
    q = question.lower()
    flags = []

    for topic, keywords in CONFIDENTIAL_TOPICS.items():
        if any(keyword in q for keyword in keywords):
            flags.append(topic)

    return flags

def should_refuse(question: str, role: str) -> bool:
    flags = classify_request(question)

    for flag in flags:
        allowed_roles = AUTHORIZED_ROLES_BY_TOPIC.get(flag, [])
        if role not in allowed_roles:
            return True

    return False

def safe_refusal_message(risk_flags: list[str]) -> str:
    if not risk_flags:
        return "I cannot help with that request."

    return (
        "I cannot disclose confidential employee-specific information related to "
        + ", ".join(risk_flags)
        + ". I can help with general HR policy questions or direct you to HR."
    )
