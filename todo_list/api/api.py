from fastapi import APIRouter

from todo_list.infra.health_check import router as routeh
from todo_list.infra.routers import router as routes

router = APIRouter()
router.include_router(routes, tags=["todo"])
router.include_router(routeh, tags=["health-check"])
