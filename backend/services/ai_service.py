# Logic for summarizeing transcripts and generating flashcards
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from backend.schemas.transcript import TranscriptResponse, Flashcard

class AIService:
    def __init__(self):
        self.model = ChatOpenAI(model="gpt-4", temperature=0)

    async def summarize(self, transcriptText: str) -> TranscriptResponse:
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are an expert educator that summarizes transcripts and generates 7-8 high quality flashcards from the provided transcript. The flashcards should cover the most important concepts and information from the transcript. "),
            ("user", f"Summarize the following transcript and generate flashcards:\n\n{transcriptText}")
        ])

        # Logic to follow the schema 
        struct__llm = self.model.with_structured_output(TranscriptResponse)

        # Execute the prompt and get the structured response
        chain = struct__llm | prompt
        result = await chain.ainvoke({"transcriptText": transcriptText}) #type: ignore
        return result # type: ignore