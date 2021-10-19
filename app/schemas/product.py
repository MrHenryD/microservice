from typing import Optional

from pydantic import BaseModel


class ProductBase(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None


class ProductCreate(ProductBase):
    name: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None


class Product(ProductBase):
    name: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None
