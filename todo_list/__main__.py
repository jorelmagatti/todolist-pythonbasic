from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

from todo_list.api.api import router as v1router
from todo_list.config import settings

app = FastAPI(
    root_path=settings.root_path,
    title="Todo List API",
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redoc",
)

Instrumentator().instrument(app).expose(app)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(v1router, prefix="/api/v1")
