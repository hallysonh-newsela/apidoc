from fastapi import FastAPI
from typing import List
from app.internal import models, fakedb as db

app = FastAPI()


@app.get("/users", response_model=List[models.User])
async def get_user_list():
    return db.list_users()
