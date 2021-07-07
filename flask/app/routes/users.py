from flask_apispec import marshal_with, doc, use_kwargs
from flask_apispec.views import MethodResource

from ..internal import fakedb as db
from ..internal.models import UserIn, UserInSchema, UserSchema, PageRequestSchema


# noinspection PyMethodMayBeStatic
@doc(tags=["users"])
@marshal_with(UserSchema)
class UsersRoot(MethodResource):

    @marshal_with(UserSchema(many=True))
    @use_kwargs(PageRequestSchema, location="query")
    def get(self, **kwargs):
        return db.list_users(**kwargs)

    @doc(description="Create an user with with the username, email, full_name and password provided")
    @use_kwargs(UserInSchema, location='json')
    def post(self, **kwargs):
        user_in = UserIn(**kwargs)
        return db.save_user(user_in), 201


# noinspection PyMethodMayBeStatic
@doc(tags=["users"])
@marshal_with(UserSchema)
class UsersById(MethodResource):

    def get(self, user_id: int):
        return db.find_user_by_id(user_id)

    @use_kwargs(UserInSchema, location='json')
    def put(self, user_id: int, **kwargs):
        user_in = UserIn(**kwargs)
        return db.update_user(user_id, user_in)
