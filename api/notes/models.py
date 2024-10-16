from datetime import datetime

from sqlalchemy import JSON, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from api.database import Base


class Tag(Base):
    __tablename__ = "tags"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)


class ContentItem(Base):
    __tablename__ = 'content_items'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    article_id: Mapped[int] = mapped_column(ForeignKey('articles.id'), nullable=False)
    content_type: Mapped[str] = mapped_column(nullable=False)  # Например: "text", "image", "video"
    content_order: Mapped[int] = mapped_column(nullable=False)  # Порядок отображения контента
    text: Mapped[str] = mapped_column(nullable=True)  # Текст для текстового контента
    media_url: Mapped[str] = mapped_column(nullable=True)  # URL для изображений или видео
    media_metadata: Mapped[dict] = mapped_column(JSON, nullable=True)  # Метаданные для медиа (например, разрешение, описание)

    article: Mapped["Article"] = relationship("Article", back_populates="content_items")


class Article(Base):
    __tablename__ = 'articles'
    STATUS = ("draft", "published", "archived")  # Перечисление статусов как кортеж
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False)
    created: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    user_id: Mapped[int] = mapped_column(Integer, nullable=False)

    tags: Mapped[list[Tag]] = relationship("Tag", secondary="article_tags", back_populates="articles")
    content_items: Mapped[list[ContentItem]] = relationship("ContentItem", back_populates="article")


class ArticleTag(Base):
    __tablename__ = 'article_tags'
    id: Mapped[int] = mapped_column(primary_key=True)
    article_id: Mapped[int] = mapped_column(ForeignKey('articles.id'), primary_key=True)
    tag_id: Mapped[int] = mapped_column(ForeignKey('tags.id'), primary_key=True)

    article: Mapped["Article"] = relationship("Article", back_populates="tags")
    tag: Mapped["Tag"] = relationship("Tag", back_populates="articles")
