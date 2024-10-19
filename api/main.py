from typing import Literal

from api.articles.router import router as article_router
from api.tags.router import router as tags_router
from fastapi import FastAPI

app = FastAPI(title="Demo Fast API")
app.include_router(article_router)
app.include_router(tags_router)


@app.get('/')
def hello() -> Literal['Article API!']:
    return "Article API!"
