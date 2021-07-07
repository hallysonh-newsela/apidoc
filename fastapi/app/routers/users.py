from fastapi import APIRouter, status
from typing import List, Optional
from ..internal import fakedb as db, models

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[models.User], response_model_exclude={"joined"})
async def get_user_list(q: Optional[str] = None, skip: int = 0, limit: int = 100):
    return db.list_users(q, skip, limit)


@router.get("/{user_id}", response_model=models.User)
async def get_user_by_id(user_id: int):
    return db.find_user_by_id(user_id)


@router.post(
    "/",
    response_model=models.User,
    status_code=status.HTTP_201_CREATED,
    summary="Create an user",
    description="Create an user with with the username, email, full_name and password provided",
)
async def create_user(user: models.UserIn):
    return db.save_user(user)


@router.put("/{user_id}", response_model=models.User)
async def update_user(user_id: int, user: models.UserIn):
    return db.update_user(user_id, user)
