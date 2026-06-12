from fastapi import FastAPI
from pydantic import BaseModel
from rag_pipeline import answer_question

app = FastAPI(
    title="HR Policy Assistant RAG API",
    description="Internal HR assistant using RAG over general HR policies and restricted HR records.",
    version="0.2.0",
)

class ChatRequest(BaseModel):
    user_id: str
    role: str = "employee"
    department: str | None = None
    question: str

class ChatResponse(BaseModel):
    answer: str
    sources: list[str]
    refused: bool = False
    escalation_required: bool = False
    risk_flags: list[str] = []

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    result = answer_question(
        question=request.question,
        user_id=request.user_id,
        role=request.role,
        department=request.department,
    )
    return ChatResponse(**result)

@app.get("/health")
def health():
    return {"status": "ok"}
