from fastapi import FastAPI

from notes.router import router as notes_router

app = FastAPI(title="Demo Fast API")
app.include_router(notes_router)


@app.get('/')
def hello():
    return "Hello world!"


if __name__ == "__main__":
    print("main!")
