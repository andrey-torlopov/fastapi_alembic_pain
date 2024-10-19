from api.tags.models import Tag
from api.tags.repository import TagRepository
from api.tags.schemas import TagCreate, TagUpdate
from fastapi import HTTPException


class TagService:
    def __init__(self, repository: TagRepository) -> None:
        self.repository = repository

    async def get_all_tags(self) -> list[Tag]:
        return await self.repository.get_tags()

    async def create_tag(self, tag_data: TagCreate) -> Tag:
        tag = Tag(name=tag_data.name)
        return await self.repository.add_tag(tag)

    async def update_tag(self, tag_id: int, tag_data: TagUpdate) -> Tag:
        tag = await self.repository.get_tag_by_id(tag_id)
        if not tag:
            raise HTTPException(status_code=404, detail="Tag not found")
        tag.name = tag_data.name
        return await self.repository.update_tag(tag)

    async def delete_tag(self, tag_id: int) -> None:
        tag = await self.repository.get_tag_by_id(tag_id)
        if not tag:
            raise HTTPException(status_code=404, detail="Tag not found")
        await self.repository.delete_tag(tag)
