from fastapi import APIRouter
from app.schemas.transcript import TranscriptResponse
from app.services.ai_service import AIService

router = APIRouter(prefix="/transcript", tags=["transcript"])
ai_service = AIService()

@router.post("/process-transcript", response_model=TranscriptResponse)
async def process_transcript(payload: dict):
    # Call the Langchain service to get the summary and flashcards
    return await ai_service.summarize(payload["transcriptText"])

@router.post("/process-youtube-transcript", response_model=TranscriptResponse)
async def process_youtube_transcript(url: dict):
    # Call the Langchain service to get the summary and flashcards
    return await ai_service.summarize_youtube_transcript(url["videoUrl"])