from typing import List, Optional
from datetime import datetime
from fastapi import HTTPException

from .models import UserIn, User

_users: List[User] = [
    User(id=1, username="hallyson.almeida", email="hallysonh@gmail.com", full_name="Hallyson Almeida",
         joined="2021-07-10 12:20:00"),
    User(id=2, username="mike.jonhson", email="mike.jonhson.test@gmail.com", full_name="Mike Jonhson",
         joined="2021-03-15 12:30:00"),
    User(id=3, username="john.rock", email="john.rock.test@gmail.com", full_name="John Rock",
         joined="2021-07-01 12:40:00"),
]


def list_users(q: Optional[str] = None, skip: int = 0, limit: int = 100):
    result = _users
    if q:
        result = [x for x in result if q.lower() in x.full_name.lower()]
    return result[skip:skip + limit]


def save_user(user_in: UserIn):
    user = User(**user_in.dict(), id=len(_users) + 1, joined=datetime.now())
    _users.append(user)
    return user


def find_user_by_id(user_id: int):
    user = next((x for x in _users if x.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def update_user(user_id: int, user_in: UserIn):
    user = find_user_by_id(user_id)
    update_data = user_in.dict(exclude_unset=True)
    updated_user = user.copy(update=update_data)

    user_index = _users.index(user)
    _users[user_index] = updated_user

    return updated_user
