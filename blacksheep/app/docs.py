from blacksheep.server.openapi.v3 import OpenAPIHandler
from openapidocs.v3 import Info

# Create Documentation handler
docs = OpenAPIHandler(
    info=Info(
        title="My BlackSheep Sample APP",
        description="Show how easy is to create a gateway API with documentation",
        version="0.1.0",
    ),
)
