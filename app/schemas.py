from pydantic import BaseModel


class ToDoBase (BaseModel):
    name: str
    description: str


class TodoCreate (ToDoBase):
   pass

class ToDo (ToDoBase):
    id: int

    class Config:
        orm_mode = True
