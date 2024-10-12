from api.notes.router import router as notes_router
from fastapi import FastAPI

app = FastAPI(title="Demo Fast API")
app.include_router(notes_router)


@app.get('/')
def hello():
    return "Hello world!"
