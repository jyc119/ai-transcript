import io
import os
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))


async def transcribe_audio(file_bytes: bytes, filename: str) -> str:
    audio_file = io.BytesIO(file_bytes)
    audio_file.name = filename

    transcription = await client.audio.transcriptions.create(
        model="gpt-4o-mini-transcribe",
        file=audio_file
    )

    return transcription.text
