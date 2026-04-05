# Transcript Summarizer

A full-stack web app that turns long transcript text into a concise AI-generated summary and a set of study flashcards.

The project combines a FastAPI backend with a React + Vite frontend. The backend sends transcript text to Google Gemini through LangChain, asks for a structured response, and returns both a summary and flashcards that the frontend renders interactively.

## Features

- AI-powered transcript summarization.
- Automatic generation of 7 to 8 flashcards from the source transcript.
- Structured API response with predictable `summary` and `flashcards` fields.
- Modern React UI for reviewing the summary and flipping flashcards.
- FastAPI backend with CORS configured for local frontend development.

## Tech Stack

- Backend: FastAPI, Pydantic, LangChain, Google Gemini.
- Frontend: React, Vite, React Router, Axios, Tailwind CSS, shadcn/ui.
- Tooling: Python environment managed through `uv`-generated requirements, npm for the frontend.

## How It Works

1. The user enters transcript text in the frontend.
2. The frontend sends the text to the FastAPI endpoint `/api/v1/transcript/process-transcript`.
3. The backend builds an LLM prompt and requests a structured response from Gemini.
4. The API returns a summary plus a flashcard list.
5. The frontend displays the result in the summary panel and interactive flashcards.

## Project Structure

```text
backend/
  main.py                # FastAPI app entry point
  api/v1/                # API router and endpoints
  core/config.py         # Environment configuration
  schemas/transcript.py  # Response schema for summary + flashcards
  services/ai_service.py # LangChain / Gemini summarization logic

frontend/
  src/
    pages/Home.jsx       # Main page layout
    components/          # Input, summary, and flashcard UI
    lib/api.js           # Frontend API client
```

## Getting Started

### Prerequisites

- Python 3.13 or newer.
- Node.js 18 or newer.
- A Google Gemini API key.

### 1. Backend Setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file inside `backend/`:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Run the API:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

FastAPI docs will be available at `http://localhost:8000/docs`.

### 2. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

By default, the frontend expects the backend to be running at `http://localhost:8000`.

## API Reference

### `GET /`

Returns a simple health-style welcome message.

### `POST /api/v1/transcript/process-transcript`

Request body:

```json
{
  "transcriptText": "Your transcript text here"
}
```

Response shape:

```json
{
  "summary": "...",
  "flashcards": [
    {
      "question": "...",
      "answer": "..."
    }
  ]
}
```

## Notes

- The current frontend UI includes tabs for YouTube URL, pasted text, and file upload, but the active backend workflow currently processes pasted transcript text.
- If you change the backend host or port, update the Axios base URL in `frontend/src/lib/api.js`.

## Future Improvements

- Support file uploads end to end.
- Add export funtionality to save generated flashcards.