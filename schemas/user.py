from datetime import datetime

from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    slug: str
    description: str
    price: int
    images: list[str] = []
    quantity: int
    typeId: int
    categoryIds: list[int] = []
    socialLinks: dict = {}


class ProductGet(ProductCreate):
    id: int
    created_at: datetime
    updated_at: datetime

    class config:
        orm_mode = True
