from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List 

from fastapi import Depends
from database import Base, engine, SessionLocal

import models
import schemas
import crud_todo


# seguir o passo a passo que está em:
# https://www.gormanalysis.com/blog/building-a-simple-crud-application-with-fastapi/

# Create the database
Base.metadata.create_all(engine)

def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()

@app.get("/")
def root(nome:str = "world!!!"):
    return {"message": f"Hello {nome}"}

@app.post("/todo", status_code=status.HTTP_201_CREATED)
def create_todo(todo: schemas.ToDoCreate, session:Session = Depends(get_session)):
    # create an instance of the ToDo database model
    tododb = crud_todo.create_todo(session, todo)

    # return the id
    return tododb.id

@app.get("/todo/{id}")
def read_todo(id: int, session:Session = Depends(get_session)):

    todo = crud_todo.get_todo_by_id(session, id)

    # check if todo item with given id exists. If not, raise exception and return 404 not found response
    if not todo:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")

    return todo

@app.put("/todo/{id}")
def update_todo(id: int, todo: schemas.ToDoCreate, session:Session = Depends(get_session)) :

    todo_atualizado = crud_todo.update_todo(session, id, todo.task)
    # check if todo item with given id exists. If not, raise exception and return 404 not found response
    if not todo_atualizado:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")
    return todo_atualizado.id

@app.delete("/todo/{id}")
def delete_todo(id: int, session:Session = Depends(get_session)):
    # get the todo item with the given id
    todo = crud_todo.delete_todo(session, id)

    # if todo item with given id exists, delete it from the database. Otherwise raise 404 error
    if not todo:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")

    return None

@app.get("/todo", response_model=List[schemas.ToDo])
def read_todo_list(session:Session = Depends(get_session)):
    todo_list = crud_todo.read_todo_list(session)

    return todo_list