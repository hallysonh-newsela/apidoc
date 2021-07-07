from blacksheep.server import Application
from blacksheep.server.openapi.v3 import OpenAPIHandler
from openapidocs.v3 import Info

from typing import List
from app.internal import fakedb as db
from blacksheep.app import domain

app = Application()

# Create Documentation handler
docs = OpenAPIHandler(
    info=Info(
        title="My BlackSheep Simple APP",
        description="Show how easy is to create a gateway API with documentation",
        version="0.1.0",
    ),
)
docs.bind_app(app)


@docs(tags=["users"])
@app.router.get("/users")
async def get_user_list() -> List[domain.User]:
    return db.list_users()
