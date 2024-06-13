from ast import Dict
from datetime import datetime
from typing import List
from sqlalchemy import JSON, create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column


def get_utc_now():
    return datetime.utcnow()


SQLALCHEMY_DATABASE_URL = "postgresql://ales_user:1yvzuHdq5sDTjQZZixRegojOfaiM4vJp@dpg-cplltajgbbvc738qls8g-a.oregon-postgres.render.com/ales"
engine = create_engine(SQLALCHEMY_DATABASE_URL)


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, index=True, unique=True)


class Product(Base):
    __tablename__ = "products"

    name: Mapped[str]
    slug: Mapped[str]
    description: Mapped[str]
    price: Mapped[int]
    images: Mapped[List[str]] = mapped_column(JSON, insert_default=[])
    quantity: Mapped[int]
    typeId: Mapped[int]
    categoryIds: Mapped[List[int]] = mapped_column(JSON, insert_default=[])
    socialLinks: Mapped[Dict] = mapped_column(JSON, insert_default={})
    created_at: Mapped[datetime] = mapped_column(insert_default=get_utc_now())
    updated_at: Mapped[datetime] = mapped_column(
        insert_default=get_utc_now(), onupdate=get_utc_now()
    )


SessionLocal = sessionmaker(autoflush=False, bind=engine)
