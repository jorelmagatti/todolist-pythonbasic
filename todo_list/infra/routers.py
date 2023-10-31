from fastapi import APIRouter, Query
import json
from starlette.responses import JSONResponse
from todo_list.services.todo_services import (get_todo_tasks, get_todo_tasks_by_id, create_todo_task, delete_todo_tasks_by_id)
router = APIRouter()

@router.get("/tasks")
async def bulk_import():
    return JSONResponse({"success": True, "tasks": await get_todo_tasks()}, status_code=200)

@router.get("/task")
async def bulk_import(task_id: int):
    return JSONResponse({"success": True, "task": await get_todo_tasks_by_id(task_id)}, status_code=200)

@router.post("/task")
async def bulk_import(task_name: str, task_description: str):
    return JSONResponse({"success": True, "task": await create_todo_task(task_name, task_description)}, status_code=200)

@router.put("/task")
async def bulk_import(task_id: int, new_task_name: str):
    return JSONResponse({"success": True, "task": new_task_name}, status_code=200)

@router.delete("/task")
async def bulk_import(task_id: int):
    return JSONResponse({"success": True, "action": json.dumps(await delete_todo_tasks_by_id(task_id))}, status_code=200)