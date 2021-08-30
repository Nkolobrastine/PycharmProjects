from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List
import uvicorn
import models
from Database import SessionLocal, engine, Base


class ToDo (BaseModel):
    id: int
    name: str
    description: str


app = FastAPI (title="ToDo App")
db = SessionLocal ()
Base.metadata.create_all (bind=engine)


@app.get ("/todo", response_model=List[ToDo], status_code=200)
async def get_all_todo():
    todos = db.query (models.ToDo).all ()
    print (todos)
    return todos


@app.get ("/todo/{id}", response_model=ToDo, status_code=status.HTTP_200_OK)
async def get_a_todo(id: int):
    todo = db.query (models.ToDo).filter (models.ToDo.id == id).first ()

    return todo


@app.post ("/todo", response_model=ToDo, status_code=status.HTTP_201_CREATED)
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


@app.put ("/todo/{id}", response_model=ToDo, status_code=status.HTTP_200_OK)
async def update_todo(id: int, todo: ToDo):
    update_a_todo = db.query (models.ToDo).filter (models.ToDo.id == id).first ()
    update_a_todo.id = todo.id
    update_a_todo.name = todo.name
    update_a_todo.description = todo.description

    db.commit ()
    return update_a_todo


@app.delete ("/todo/{id}")
async def delete_todo(id: int):
    delete_a_todo = db.query (models.ToDo).filter (models.ToDo.id == id).first ()
    if delete_a_todo is None:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND, detail="Resource not Found")

    db.delete (delete_a_todo)
    db.commit ()

    return delete_a_todo


if __name__ == "__main__":
    uvicorn.run ("main:app", host="127.0.0.1", port=8000, reload=True)
