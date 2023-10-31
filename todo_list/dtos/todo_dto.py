from pydantic import BaseModel

class TodoDto(BaseModel):
    id: int
    name: str
    description: str
    executed: bool | None

    def __dictdto__(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'executed': self.executed,
        }