from sqlalchemy import INTEGER, VARCHAR, BOOLEAN, Column

from todo_list.infra.mariadb import Base


class Todo(Base):
    __tablename__ = "todo"

    id = Column(INTEGER, nullable=False, primary_key=True)
    name = Column(VARCHAR(200), nullable=False)
    description = Column(VARCHAR(200), nullable=False)
    executed = Column(BOOLEAN, nullable=False)
