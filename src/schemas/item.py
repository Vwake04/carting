from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    is_active: bool = True


class ItemCreate(ItemBase):
    pass


class ItemUpdate(ItemBase):
    name: Optional[str] = None
    is_active: Optional[bool] = None


class ItemInDB(ItemBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    owner_id: Optional[int] = None

    class Config:
        from_attributes = True


class Item(ItemInDB):
    pass
