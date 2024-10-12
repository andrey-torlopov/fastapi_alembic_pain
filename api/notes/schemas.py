from datetime import datetime

from pydantic import BaseModel


class NoteCreate(BaseModel):
    id: int
    content: str
    date: datetime
    type: str

class Tag(BaseModel):
    id: int
    name: str
