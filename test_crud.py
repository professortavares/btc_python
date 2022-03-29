import pytest
from urllib import response
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from main import app, get_session
from database import Base

# Create a sqlite engine instance
engine = create_engine("sqlite:///todo_test.db")

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        db.begin()
        yield db
    finally:
        db.rollback()
        db.close()

app.dependency_overrides[get_session] = override_get_db

client = TestClient(app)


def test_root():
    #https://docs.python-requests.org/en/v0.6.2/api/
    response = client.get("/")
    assert response.status_code == 200    
    assert response.json() == {'message': 'Hello world!!!'}

def limpar_banco():
    Base.metadata.drop_all(bind=engine)
    return "ok"

def test_crud_api():
    json = {
        "task":"Uma task qualquer"
    }
    # testa a criação de uma task
    response = client.post("/todo",
                json=json)

    assert response.status_code == 201    
    task_id = response.json()
    assert task_id is not None

    # testa a recuperacao de uma task criada    
    response = client.get(f"/todo/{task_id}")
    assert response.status_code == 200
    json = response.json()
    assert json['task'] == "Uma task qualquer"
    assert json['id'] == task_id

    # testa a alteração de uma task criada
    json = {
        "task":"alterando a task"
    }
    response = client.put(f"/todo/{task_id}",
        json=json)
    retorno_id = response.json()
    assert retorno_id == task_id

    # testa a recuperação de uma task criada    
    response = client.get(f"/todo/{task_id}")
    assert response.status_code == 200
    json = response.json()
    assert json['task'] == "alterando a task"
    assert json['id'] == task_id

    # testa a remoção de uma tarefa    
    response = client.delete(f"/todo/{task_id}")
    assert response.status_code == 200

    # testa a recuperação de uma task criada    
    response = client.get(f"/todo/{task_id}")
    assert response.status_code == 404


    limpar_banco()
