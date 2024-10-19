from pydantic import BaseModel


# Схема для создания тега
class TagCreate(BaseModel):
    name: str


# Схема для ответа тега
class TagResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class TagUpdate(BaseModel):
    name: str
