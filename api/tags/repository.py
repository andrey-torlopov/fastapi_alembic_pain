from typing import Sequence

from api.tags.models import Tag
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class TagRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_tags(self) -> Sequence[Tag]:
        query = select(Tag)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def add_tag(self, tag: Tag) -> Tag:
        self.session.add(tag)
        await self.session.commit()
        await self.session.refresh(tag)
        return tag

    async def get_tag_by_id(self, tag_id: int) -> Tag | None:
        query = select(Tag).where(Tag.id == tag_id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def update_tag(self, tag: Tag) -> Tag:
        self.session.add(tag)
        await self.session.commit()
        await self.session.refresh(tag)
        return tag

    async def delete_tag(self, tag: Tag) -> None:
        await self.session.delete(tag)
        await self.session.commit()
