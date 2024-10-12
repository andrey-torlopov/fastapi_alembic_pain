from api.database import get_async_session
from api.notes.models import Note
from api.notes.schemas import NoteCreate, NoteResponse
from fastapi import APIRouter, Depends
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

# Через сервис ходим в базу

router = APIRouter(
    prefix="/notes",
    tags=["Notes"]
)


@router.get("/")
async def get_specific_notes(note_type: str, session: AsyncSession = Depends(get_async_session)):
    query = select(Note).where(Note.type == note_type)  # обращение к полю напрямую
    result = await session.execute(query)

    # Преобразование результатов в список словарей
    notes_dicts = [row._asdict() for row in result.all()]
    return {"result": notes_dicts}


@router.post("/", response_model=NoteResponse)
async def add_note(new_note: NoteCreate, session: AsyncSession = Depends(get_async_session)):
    # Создаем объект Note
    note = Note(
        content=new_note.content,
        date=new_note.date,
        type=new_note.type
    )
    
    # Добавляем объект в сессию
    session.add(note)
    await session.commit()
    await session.refresh(note)  # Обновляем объект, чтобы получить id

    # Преобразуем ORM объект в Pydantic-схему для возврата
    return NoteResponse.from_orm(note)
