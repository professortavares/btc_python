from fastapi import FastAPI, status, HTTPException
from sqlalchemy.orm import Session
from task import Tarefa
from database import Base, engine, ToDo


app = FastAPI()


# Create the database
Base.metadata.create_all(engine)

@app.post("/todo",status_code = status.HTTP_201_CREATED)
def create_task(tarefa: Tarefa):
   # create a new database session
    session = Session(bind=engine, expire_on_commit=False)
    # create an instance of the ToDo database model
    tododb = ToDo(tarefa = tarefa.task)
    session.add(tododb)
    session.commit()
    # grab the id given to the object from the database
    id = tododb.id
    # close the session
    session.close()
    # return the id
    return f"created todo item with id {id}"


#Take All task
@app.get("/todo/{id}")
def read_task_by_id(id:int):
    # create a new database session
    session = Session(bind = engine,expire_on_commit = False)
    # get the todo item with the given id
    todo = session.query(ToDo).get(id)
    session.close()
    # check if todo item with given id exists. If not, raise exception and return 404 not found response
    if not todo:
        raise HTTPException(status_code = 404, detail = f"todo item with id {id} not found")
    return todo


#Update  task by ID
@app.put("/todo/{id}")
def update_task_by_id(id:int,task:str):
    session = Session(bind = engine, expire_on_commit = False)

    todo = session.query(ToDo).get(id)
    if todo:
        todo.tarefa = task
        session.commit()

    session.close()

    # check if todo item with given id exists. If not, raise exception and return 404 not found response
    if not todo:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")

    return todo
   

#Delete  task by ID
@app.delete("/todo/{id}")
def delete_task_by_id(id:int):
    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # get the todo item with the given id
    todo = session.query(ToDo).get(id)

    # if todo item with given id exists, delete it from the database. Otherwise raise 404 error
    if todo:
        session.delete(todo)
        session.commit()
        session.close()
    else:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")


@app.get("/todo")
def read_all_tasks():
    # create a new database session
    session = Session(bind = engine, expire_on_commit = False)

    # get all todo items
    todo_list = session.query(ToDo).all()

    # close the session
    session.close()

    return todo_list