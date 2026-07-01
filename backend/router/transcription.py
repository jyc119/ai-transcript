from fastapi import APIRouter, UploadFile, File, HTTPException
from services.transcription import transcribe_audio

router = APIRouter()

ALLOWED_TYPES = {"audio/webm", "audio/wav", "audio/mpeg"}
MAX_SIZE_MB = 25


@router.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(415, f"Unsupported file type: {file.content_type}")

    contents = await file.read()
    if len(contents) > MAX_SIZE_MB * 1024 * 1024:
        raise HTTPException(413, "File too large")

    try:
        text = await transcribe_audio(contents, filename=file.filename)
    except Exception as e:
        raise HTTPException(502, f"Transcription failed: {e}")

    return {"transcription": text}
