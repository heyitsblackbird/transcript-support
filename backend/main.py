
from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/process-transcript")
def process_transcript(title: str, transcriptText: str):
    # Here you can add your logic to process the transcript text and generate a summary
    summary = f"Summary for {title}: {transcriptText[:100]}..."
    section_summary = "Hello world!"
    final_summary ="this is final summary"
    key_concepts = ["concept 1", "concept 2"]
    flashCard = [{
                    "question": "What is the main topic of the transcript?",
                    "answer": f"The main topic of the transcript is {title}."
    },
    {
                    "question": "What are some key concepts mentioned in the transcript?",
                    "answer": f"Some key concepts mentioned in the transcript include: {', '.join(key_concepts)}."
    } ]  # Placeholder summary
    return {
        "summary": summary,
        "section_summary": section_summary,
        "final_summary": final_summary,
        "key_concepts": key_concepts,
        "flashCard": flashCard  
    }