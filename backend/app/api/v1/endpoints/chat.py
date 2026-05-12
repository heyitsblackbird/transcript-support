from fastapi import APIRouter, UploadFile, File, HTTPException
from app.schemas.chat import ChatRequest, ChatResponse

from app.services.retrieval_service import retrieve_relevant_chunks
from app.services.generation_service import generate_answer

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("/query", response_model=ChatResponse)
async def query_chat(chat_request: ChatRequest):
    if not chat_request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    
    chunks = retrieve_relevant_chunks(question=chat_request.question, top_k=3)

    result = await generate_answer(question=chat_request.question, chunks=chunks)

    return result
