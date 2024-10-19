from api.articles.repository import ArticleRepository
from api.articles.schemas import ArticleCreate, ArticleResponse
from api.articles.service import ArticleService
from api.database import get_async_session
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/articles", tags=["Articles"])


def get_article_service(session: AsyncSession = Depends(get_async_session)) -> ArticleService:
    repository = ArticleRepository(session)
    return ArticleService(repository)


@router.get("/", response_model=list[ArticleResponse])
async def get_articles(service: ArticleService = Depends(get_article_service)):
    articles = await service.get_all_articles()
    return [ArticleResponse.from_orm(article) for article in articles]


@router.post("/", response_model=ArticleResponse)
async def create_article(new_article: ArticleCreate, service: ArticleService = Depends(get_article_service)):
    article = await service.create_article(new_article)
    # Принудительно загрузим связанные объекты
    await service.load_related_objects(article)
    return ArticleResponse.from_orm(article)
