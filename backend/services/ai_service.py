# Logic for summarizeing transcripts and generating flashcards
#from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from schemas.transcript import TranscriptResponse
from core.config import OPENAI_API_KEY, GEMINI_API_KEY
from pydantic import SecretStr

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