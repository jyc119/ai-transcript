from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


#accepts audio file and returns a transcript
# @app.get("/tasks", response_model=List[Task])
def get_tasks():
    pass