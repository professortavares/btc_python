from fastapi import FastAPI

# A criação do objeto app, que é um objeto da
# classe FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello Leonardo"}