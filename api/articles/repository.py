from typing import Sequence

from api.articles.models import Article, ArticleTag
from api.tags.models import Tag
from api.tags.schemas import TagCreate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload


class ArticleRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_articles(self) -> Sequence[Article]:
        query = select(Article).options(selectinload(Article.content_items), selectinload(Article.tags))
        result = await self.session.execute(query)
        return result.scalars().all()

    # async def add_article(self, article: Article) -> Article:
    #     self.session.add(article)
    #     await self.session.commit()
    #     # Явно подгружаем связанные объекты
    #     await self.session.refresh(article, ["content_items", "tags"])
    #     return article

    async def get_tag_by_name(self, name: str) -> Tag:
        query = select(Tag).where(Tag.name == name)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()  # Возвращает тег или None, если не найден

    async def add_article(self, article: Article, tags: list[TagCreate]) -> Article:
        # Сначала добавляем статью в базу данных
        self.session.add(article)
        await self.session.commit()

        # Обновляем статью, чтобы получить article_id
        await self.session.refresh(article)

        # Для каждого тега создаём запись в article_tags
        for tag_data in tags:
            existing_tag = await self.get_tag_by_name(tag_data.name)
            if existing_tag:
                # Создаем запись в таблице article_tags
                article_tag = ArticleTag(article_id=article.id, tag_id=existing_tag.id)
                self.session.add(article_tag)

        # Сохраняем все записи article_tag
        await self.session.commit()

        # Явно подгружаем связанные объекты статьи
        await self.session.refresh(article, ["content_items", "tags"])
        return article
