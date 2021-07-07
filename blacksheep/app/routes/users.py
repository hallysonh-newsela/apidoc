from blacksheep.server.bindings import FromJSON, FromQuery

from .router import get, post, put
from ..docs import docs
from ..domain import UserIn
from ..internal import fakedb as db


@docs(tags=["users"])
@get("/users")
async def get_user_list(
        q: FromQuery[str] = FromQuery(""),
        skip: FromQuery[int] = FromQuery(0),
        limit: FromQuery[int] = FromQuery(100)):
    return db.list_users(q.value, skip.value, limit.value)


@docs(tags=["users"])
@get("/users/{user_id}")
async def get_user_by_id(user_id: int):
    return db.find_user_by_id(user_id)


@docs(
    summary="Create an user",
    description="Create an user with with the username, email, full_name and password provided",
    tags=["users"]
)
@post("/users")
async def create_user(user: FromJSON[UserIn]):
    return db.save_user(user.value)


@docs(tags=["users"])
@put("/users/{user_id}")
async def update_user(user_id: int, user: FromJSON[UserIn]):
    return db.update_user(user_id, user.value)
