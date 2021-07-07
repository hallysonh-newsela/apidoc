from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from marshmallow import Schema, fields


# MODELS #####

@dataclass
class UserIn:
    username: str
    email: str
    full_name: Optional[str] = None
    password: str = field(default="", repr=False)


@dataclass
class User:
    id: int
    username: str
    email: str
    full_name: Optional[str] = None
    joined: datetime = field(default=datetime.now())


# SCHEMAS #####

class UserInSchema(Schema):
    username = fields.String(required=True)
    email = fields.String(required=True)
    fullName = fields.String(required=False, default=None, attribute="full_name")
    password = fields.String(required=True)


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    fullName = fields.Str(required=False, default=None, attribute="full_name")
    joined = fields.DateTime(format="iso8601", default=datetime.now())


class PageRequestSchema(Schema):
    q = fields.Str(default=None)
    skip = fields.Int(default=0)
    limit = fields.Int(default=100)

