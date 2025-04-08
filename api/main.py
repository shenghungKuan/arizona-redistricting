from typing import Union

from fastapi import FastAPI

from .routers.arizona import arizona_route as arizona

app = FastAPI()

app.include_router(arizona.router)