from fastapi import APIRouter
from schemas.transcript import TranscriptResponse
from services.ai_service import AIService

router = APIRouter()
ai_service = AIService()

@router.post("/process-transcript", response_model=TranscriptResponse)
async def process_transcript(payload: dict):
    # Call the Langchain service to get the summary and flashcards
    return await ai_service.summarize(payload["transcriptText"])