from fastapi import  Header, HTTPException, status
from main import BaseModel
from . import models


# this function will get all the todos
async def get_all_todo():
    todos = db.query (models.ToDo).all ()
    print (todos)
    return todos


# this function will get a todos
async def get_a_todo(id: int):
    todo = db.query (models.ToDo).filter (models.ToDo.id == id).first ()

    return todo


# this function created a new todo from the data sent as input
async def create_a_todo(todo: ToDo):
    db_todo = db.query (models.ToDo).filter (models.ToDo.name == todo.name).first ()
    if db_todo is not None:
        raise HTTPException (status_code=status.HTTP_201_CREATED, detail="Todo already exist")

    new_todo = models.ToDo (
        id=todo.id,
        name=todo.name,
        description=todo.description,
    )

    db.add (new_todo)
    db.commit ()
    return new_todo


# this function will update the todo
async def update_todo(id: int, todo: ToDo):
    update_a_todo = db.query (models.ToDo).filter (models.ToDo.id == id).first ()
    update_a_todo.id = todo.id
    update_a_todo.name = todo.name
    update_a_todo.description = todo.description

    db.commit ()
    return update_a_todo


# this function will delete the todo
async def delete_todo(id: int):
    delete_a_todo = db.query (models.ToDo).filter (models.ToDo.id == id).first ()
    if delete_a_todo is None:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail="Resource not Found")

    db.delete (delete_a_todo)
    db.commit ()

    return delete_a_todo
