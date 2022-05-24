import asyncio

from typing import Union
from fastapi import FastAPI

from fiscal import models
from fiscal.crud import crud
from fiscal.schemas import schema
from fiscal.routers import router
from fiscal.db import sync_engine


models.Base.metadata.create_all(bind=sync_engine)

app = FastAPI()

app.include_router(router.router)

@app.get("/")
async def root():
    return {"Info": "This is fiscal service"}
