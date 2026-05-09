# Logic for createing API endpoints and handling requests for React frontend
from fastapi import APIRouter
from backend.app.api.v1.endpoints import transcript

router = APIRouter()
router.include_router(transcript.router, prefix="/transcript", tags=["transcript"])