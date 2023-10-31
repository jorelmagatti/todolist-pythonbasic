from typing import List, cast

from sqlalchemy import insert, select, delete

from todo_list.infra.mariadb import get_db
from todo_list.models.todo import Todo

class TodoRepository:
    async def create_todo(self, name: str, description: str):
        async with get_db() as session:
            query = insert(Todo).values(name=name,description=description,executed=False)
            await session.execute(query)
            await session.commit()

    async def get_todo_tasks(self) -> List[Todo]:
        async with get_db() as session:
            query = select(Todo).where(Todo is not None)
            return (await session.execute(query)).scalars()

    async def get_todo_tasks_by_id(self, id: int) -> Todo:
        async with get_db() as session:
            query = select(Todo).where(Todo.id==id)
            return (await session.execute(query)).scalar()

    async def delete_todo_tasks_by_id(self, id: int):
        async with get_db() as session:
            query = delete(Todo).where(id=id)
            return (await session.execute(query))

todo_repo = TodoRepository()
