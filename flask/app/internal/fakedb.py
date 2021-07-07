from datetime import datetime
from typing import List, Optional

from flask_restful import abort

from .models import UserIn, User

_datetime_format = "%Y-%m-%d %H:%M:%S"
_user_fields = [k for k in User.__annotations__]
_users: List[User] = [
    User(id=1, username="hallyson.almeida", email="hallysonh@gmail.com", full_name="Hallyson Almeida",
         joined=datetime.strptime("2021-07-10 12:20:00", _datetime_format)),
    User(id=2, username="mike.jonhson", email="mike.jonhson.test@gmail.com", full_name="Mike Jonhson",
         joined=datetime.strptime("2021-03-15 12:30:00", _datetime_format)),
    User(id=3, username="john.rock", email="john.rock.test@gmail.com", full_name="John Rock",
         joined=datetime.strptime("2021-07-01 12:40:00", _datetime_format)),
]


def abort_if_user_doesnt_exist(user_id):
    for x in _users:
        if x.id == user_id:
            break
    else:
        abort(404, message="User not found")


def list_users(q: Optional[str] = None, skip: int = 0, limit: int = 100):
    result = _users
    if q:
        result = [x for x in result if q.lower() in x.full_name.lower()]
    return result[skip:skip + limit]


def save_user(user_in: UserIn):
    create_data = {k: v for k, v  in user_in.__dict__.items() if k in _user_fields}
    user = User(**create_data, id=len(_users) + 1, joined=datetime.now())
    _users.append(user)
    return user


def find_user_by_id(user_id: int):
    abort_if_user_doesnt_exist(user_id)
    user = next((x for x in _users if x.id == user_id), None)
    return user


def update_user(user_id: int, user_in: UserIn):
    abort_if_user_doesnt_exist(user_id)
    user = find_user_by_id(user_id)
    update_data = {k: v for k, v in user_in.__dict__.items() if v and k in _user_fields}

    for k, v in update_data.items():
        setattr(user, k, v)

    return user
