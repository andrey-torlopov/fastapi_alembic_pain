from api.database import get_async_session
from api.tags.repository import TagRepository
from api.tags.schemas import TagCreate, TagResponse, TagUpdate
from api.tags.service import TagService
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/tags", tags=["Tags"])


def get_tag_service(session: AsyncSession = Depends(get_async_session)) -> TagService:
    repository = TagRepository(session)
    return TagService(repository)


@router.get("/", response_model=list[TagResponse])
async def get_tags(service: TagService = Depends(get_tag_service)) -> list[TagResponse]:
    tags = await service.get_all_tags()
    return [TagResponse.from_orm(tag) for tag in tags]


@router.post("/", response_model=TagResponse)
async def create_tag(tag: TagCreate, service: TagService = Depends(get_tag_service)) -> TagResponse:
    tag = await service.create_tag(tag)
    return TagResponse.from_orm(tag)


@router.put("/{tag_id}", response_model=TagResponse)
async def update_tag(tag_id: int, tag: TagUpdate, service: TagService = Depends(get_tag_service)) -> TagResponse:
    tag = await service.update_tag(tag_id, tag)
    return TagResponse.from_orm(tag)


@router.delete("/{tag_id}", status_code=204)
async def delete_tag(tag_id: int, service: TagService = Depends(get_tag_service)) -> None:
    await service.delete_tag(tag_id)
