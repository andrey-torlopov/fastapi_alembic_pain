from datetime import datetime

from pydantic import BaseModel


class NoteCreate(BaseModel):
    content: str
    date: datetime
    type: str

class Tag(BaseModel):
    id: int
    name: str
    
class NoteResponse(BaseModel):
    id: int
    content: str
    date: datetime
    type: str

    class Config:
        orm_mode = True  # Для совместимости с ORM
        from_attributes = True  # Включаем поддержку from_orm в Pydantic 2.x
