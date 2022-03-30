
from sqlalchemy.orm import Session
import schemas
import models

def create_todo(session:Session, todo: schemas.ToDoCreate):
    # create an instance of the ToDo database model
    tododb = models.ToDo(task = todo.task)

    # add it to the session and commit it
    session.add(tododb)
    session.commit()
    session.refresh(tododb)

    return tododb

def get_todo_by_id(session:Session, id:int):
    # get the todo item with the given id
    todo = session.query(models.ToDo).get(id)

    return todo

def update_todo(session:Session, id: int, task: str):

    # get the todo item with the given id
    todo = session.query(models.ToDo).get(id)
    
    # update todo item with the given task (if an item with the given id was found)
    if todo:
        todo.task = task
        session.commit()

    return todo

def delete_todo(session:Session, id: int):
    # get the todo item with the given id
    todo = session.query(models.ToDo).get(id)

    # if todo item with given id exists, delete it from the database. Otherwise raise 404 error
    if todo:
        session.delete(todo)
        session.commit()
        return todo
    else: return None

def read_todo_list(session):
    # get all todo items
    todo_list = session.query(models.ToDo).all()
    
    return todo_list