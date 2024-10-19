from datetime import datetime
from typing import List, Optional

from api.tags.schemas import TagCreate, TagResponse
from pydantic import BaseModel


# Схема для создания контентного элемента
class ContentItemCreate(BaseModel):
    content_type: str
    content_order: int
    text: Optional[str] = None
    media_url: Optional[str] = None
    media_metadata: Optional[dict] = None


# Схема для ответа контентного элемента
class ContentItemResponse(BaseModel):
    id: int
    article_id: int
    content_type: str
    content_order: int
    text: Optional[str] = None
    media_url: Optional[str] = None
    media_metadata: Optional[dict] = None

    class Config:
        from_attributes = True


# Схема для создания статьи
class ArticleCreate(BaseModel):
    title: str
    status: str
    user_id: int
    content_items: list[ContentItemCreate] = []
    tags: list[TagCreate] = []


# Схема для ответа статьи
class ArticleResponse(BaseModel):
    id: int
    title: str
    status: str
    created: datetime
    updated_at: Optional[datetime]
    user_id: int
    content_items: list[ContentItemResponse] = []
    tags: list[TagResponse] = []

    class Config:
        from_attributes = True
