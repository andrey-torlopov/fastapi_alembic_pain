from api.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Tag(Base):
    __tablename__ = "tags"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

    articles: Mapped[list["Article"]] = relationship(
        "Article", secondary="article_tags", back_populates="tags"
    )
