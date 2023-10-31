from typing import List, cast
import itertools

from todo_list.repositorys.database import todo_repo
from todo_list.dtos.todo_dto import TodoDto
from todo_list.models.todo import Todo

async def get_todo_tasks() -> List[TodoDto] | None:
    rows = await todo_repo.get_todo_tasks()
    todos = [TodoDto(id=row.id, description=row.description, name=row.name, executed=row.executed).__dictdto__() for row in rows]
    return todos


async def get_todo_tasks_by_id(id: int) -> TodoDto | None:
    todo = await todo_repo.get_todo_tasks_by_id(id)
    todo_dto = TodoDto(id=todo.id, description=todo.description, name=todo.name, executed=todo.executed).__dictdto__()
    return todo_dto

async def create_todo_task(name_task: str, description_task: str) -> TodoDto | None:
    todo = await todo_repo.create_todo(name=name_task, description=description_task)
    return todo

async def delete_todo_tasks_by_id(id: int) -> bool | None:
    delete_return = await todo_repo.delete_todo_tasks_by_id(id)
    return delete_return is not None

