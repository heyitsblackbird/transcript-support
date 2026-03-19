# Logic for createing API endpoints and handling requests for React frontend
from fastapi import APIRouter
from api.v1.endpoints import transcript

router = APIRouter()

# @router.post("/process-transcript", response_model=TranscriptResponse)
# def process_transcript(transcriptText: str):
#     # Here you can add your logic to process the transcript text and generate a summary
#     # call your AI service to get the summary and flashcards
#     return {
#         "summary": "This is a summary of the transcript.",
#         "flashcards": [
#             {
#                 "question": "What is the main topic of the transcript?",
#                 "answer": "The main topic of the transcript is AI and its applications."
#             },
#             {
#                 "question": "What are some key concepts mentioned in the transcript?",
#                 "answer": "Some key concepts mentioned in the transcript include machine learning, natural language processing, and deep learning."
#             }
#         ]
#     }

router.include_router(transcript.router, prefix="/transcript", tags=["transcript"])
