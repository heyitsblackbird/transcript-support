from pydantic import BaseModel

class ChatRequest(BaseModel):
    question: str
    top_k: int = 5

class Citation(BaseModel):
    source_id: str
    source: str | None
    chunk_index: int | None
    text: str | None

class ChatResponse(BaseModel):
    answer: str
    citations: list[Citation]