from fastapi import FastAPI

# A criação do objeto app, que é um objeto da
# classe FastAPI
app = FastAPI()

@app.get("/")
def root(nome:str = "world!!!"):
    return {"message": f"Hello {nome}"}


@app.post("/todo")
def criar_tarefa():
    pass

@app.get("/todo/{id}")
def ler_tarefa_por_id(id:int):
    pass

@app.put("/todo/{id}")
def atualizar_tarefa_por_id(id:int):
    pass

@app.delete("/todo/{id}")
def excluir_tarefa_por_id(id:int):
    pass

@app.get("/todo")
def ler_todas_tarefas():
    pass
