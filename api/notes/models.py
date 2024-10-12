from datetime import datetime

from api.database import Base
from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column


class Tag(Base):
    __tablename__ = "tags"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

class Note(Base):
    __tablename__ = "notes"
    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str]
    date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)  # Включаем поддержку временных зон
    type: Mapped[str]
