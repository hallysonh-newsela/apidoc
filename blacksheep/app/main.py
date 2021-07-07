from blacksheep.server.responses import text

from blacksheep.server import Application
from .config import Settings
from .docs import docs
from .routes import router, get

# Create app and get HTTP functions
app = Application(router=router)

# Register API Docs
docs.bind_app(app)

# Register services
app.services.add_instance(Settings())


@get("/")
async def root(settings: Settings):
    return text(f"Hello from BlackSheep App! (ENV: {settings.environment})")
