
from api.articles.models import Article, ContentItem, Tag
from api.articles.repository import ArticleRepository
from api.articles.schemas import ArticleCreate


class ArticleService:
    def __init__(self, repository: ArticleRepository) -> None:
        self.repository = repository

    async def load_related_objects(self, article: Article) -> None:
        # Используем сессию из репозитория для явной загрузки связанных объектов
        await self.repository.session.refresh(article, ["content_items", "tags"])

    async def get_all_articles(self) -> list[Article]:
        return await self.repository.get_articles()

    async def create_article(self, article_data: ArticleCreate) -> Article:
        tags = []
        for tag_data in article_data.tags:
            # Проверяем, существует ли тег в базе данных
            existing_tag = await self.repository.get_tag_by_name(tag_data.name)
            if existing_tag:
                tags.append(existing_tag)
            else:
                # Если тега нет, создаём новый
                new_tag = Tag(name=tag_data.name)
                self.repository.session.add(new_tag)
                await self.repository.session.commit()  # Сохраняем новый тег
                await self.repository.session.refresh(new_tag)  # Обновляем, чтобы получить id
                tags.append(new_tag)

        # Создание статьи и добавление тегов
        content_items = [ContentItem(**item.dict()) for item in article_data.content_items]

        article = Article(
            title=article_data.title,
            status=article_data.status,
            user_id=article_data.user_id,
            content_items=content_items,
            tags=tags  # Используем либо существующие, либо новые теги
        )

        # Добавляем статью через репозиторий
        return await self.repository.add_article(article, tags=tags)
