from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import Base, engine, ToDo

# A criação do objeto app, que é um objeto da
# classe FastAPI
app = FastAPI()

# Create the database
Base.metadata.create_all(engine)


class Tarefa(BaseModel):
    task:str

@app.get("/")
def root(nome:str = "world!!!"):
    return {"message": f"Hello {nome}"}


@app.post("/todo", status_code=status.HTTP_201_CREATED)
def criar_tarefa(tarefa:Tarefa):
    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # create an instance of the ToDo database model
    tododb = ToDo(tarefa = tarefa.task)

    # add it to the session and commit it
    session.add(tododb)
    session.commit()

    # grab the id given to the object from the database
    id = tododb.id

    # close the session
    session.close()

    # return the id
    return f"created todo item with id {id}"

@app.get("/todo/{id}")
def ler_tarefa_por_id(id:int):
    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # get the todo item with the given id
    todo = session.query(ToDo).get(id)

    # close the session
    session.close()

    # check if todo item with given id exists. If not, raise exception and return 404 not found response
    if not todo:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")

    return todo

@app.put("/todo/{id}")
def atualizar_tarefa_por_id(id:int, task:str):
    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # get the todo item with the given id
    todo = session.query(ToDo).get(id)

    # update todo item with the given task (if an item with the given id was found)
    if todo:
        todo.tarefa = task
        session.commit()

    # close the session
    session.close()

    # check if todo item with given id exists. If not, raise exception and return 404 not found response
    if not todo:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")

    return todo

@app.delete("/todo/{id}")
def excluir_tarefa_por_id(id:int):
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
def ler_todas_tarefas():
    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # get all todo items
    todo_list = session.query(ToDo).all()

    # close the session
    session.close()

    return todo_list