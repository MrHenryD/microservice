from typing import Any, List

from fastapi import APIRouter, HTTPException

import schemas


router = APIRouter()


@router.get("/", response_model=List[schemas.Product])
def read_products(
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve users.
    """
    users = crud.user.get_multi(db, skip=skip, limit=limit)
    return users


@router.post("/", response_model=schemas.Product)
def create_products(
    product: schemas.Product,
) -> Any:
    """
    Create products.
    """
    users = crud.user.get_multi(db, skip=skip, limit=limit)
    return users
