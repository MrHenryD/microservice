from fastapi import APIRouter

from api.v1.endpoints import users, products

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(products.router, prefix="/product", tags=["product"])
