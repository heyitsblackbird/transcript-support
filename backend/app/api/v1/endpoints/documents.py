from pathlib import Path
from fastapi import APIRouter, UploadFile, File, HTTPException

from app.services.ingestion_service import ingest_document
from app.services.chunking_service import chunk__document
from app.services.embedding_service import store_embeddings

router = APIRouter(prefix="/documents", tags=["documents"])
UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file uploaded")
    
    file_path = UPLOAD_DIR / file.filename
    with open(file_path, "wb") as f:
        f.write(await file.read())
    
    doc = ingest_document(str(file_path))

    chunks = chunk__document(text = doc['text'], source_name=doc['source'])
    total_embeddings = store_embeddings(chunks)

    return {
        "message": f"File uploaded and processed successfully.",
        "source": doc['source'],
        "total_chunks": total_embeddings
    }

