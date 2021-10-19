from typing import Any, List

from fastapi import APIRouter, HTTPException

import schemas


router = APIRouter()


@router.get("/", response_model=List[schemas.User])
def read_users(
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve users.
    """
    users = crud.user.get_multi(db, skip=skip, limit=limit)
    return users


@router.post("/", response_model=schemas.User)
def create_users(
    user: schemas.User,
) -> Any:
    """
    Create users.
    """
    users = crud.user.get_multi(db, skip=skip, limit=limit)
    return users
