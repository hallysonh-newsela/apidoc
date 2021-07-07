from fastapi import FastAPI, Depends
from fastapi.responses import PlainTextResponse
from .config import get_settings, Settings

from .routers import users

app = FastAPI(
    title="My FastAPI Sample APP",
    description="Show how easy is to create a gateway API with documentation",
    version="0.1.0",
)

app.include_router(users.router)


@app.get("/", response_class=PlainTextResponse)
async def root(settings: Settings = Depends(get_settings)):
    return f"Hello from FastAPI App! (ENV: {settings.environment})"
