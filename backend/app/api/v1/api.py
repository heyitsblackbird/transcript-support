# Logic for createing API endpoints and handling requests for React frontend
from fastapi import APIRouter
from app.api.v1.endpoints import transcript
from app.api.v1.endpoints import documents
from app.api.v1.endpoints import chat

router = APIRouter()

router.include_router(transcript.router)
router.include_router(documents.router)
router.include_router(chat.router)