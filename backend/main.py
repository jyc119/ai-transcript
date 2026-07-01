from fastapi import FastAPI
from router.transcription import router
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

app.include_router(router)