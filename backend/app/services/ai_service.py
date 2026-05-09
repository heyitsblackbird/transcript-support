# Logic for summarizeing transcripts and generating flashcards
#from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from backend.app.schemas.transcript import TranscriptResponse
from backend.app.core.config import OPENAI_API_KEY, GEMINI_API_KEY
from pydantic import SecretStr
from youtube_transcript_api import YouTubeTranscriptApi

class AIService:
    def __init__(self):
        if not GEMINI_API_KEY:
            raise ValueError("Gemini API key is not set. Please set the GEMINI_API_KEY environment variable.")
        
        self.model = ChatGoogleGenerativeAI(api_key= SecretStr(GEMINI_API_KEY), model="gemini-3-flash-preview", temperature=0)

    async def summarize(self, transcriptText: str) -> TranscriptResponse:
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are an expert educator that summarizes transcripts and generates 7-8 high quality flashcards from the provided transcript. The flashcards should cover the most important concepts and information from the transcript. "),
            ("user", f"Summarize the following transcript and generate flashcards:\n\n{transcriptText}")
        ])

        # Logic to follow the schema 
        struct__llm = self.model.with_structured_output(TranscriptResponse)

        # Execute the prompt and get the structured response
        chain = prompt  | struct__llm
        result = await chain.ainvoke({"transcriptText": transcriptText}) #type: ignore
        return result # type: ignore

    async def summarize_youtube_transcript(self, url: str) -> TranscriptResponse:

        # get video id from url
        youtube_api = YouTubeTranscriptApi()
        
        video_id = url.split("v=")[-1]
        # get transcript using youtube_transcript_api
        transcript = youtube_api.fetch(video_id)
        # print(f"Type of transcript: {type(transcript)}")
        transcriptText = " ".join([snippet.text for snippet in transcript])

        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are an expert educator that summarizes transcripts and generates 7-8 high quality flashcards from the provided transcript. The flashcards should cover the most important concepts and information from the transcript. "),
            ("user", f"Summarize the following transcript and generate flashcards:\n\n{transcriptText}")
        ])

        # Logic to follow the schema 
        struct__llm = self.model.with_structured_output(TranscriptResponse)

        # Execute the prompt and get the structured response
        chain = prompt  | struct__llm
        result = await chain.ainvoke({"transcriptText": transcriptText}) #type: ignore
        return result # type: ignore