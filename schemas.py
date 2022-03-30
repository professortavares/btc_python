from pydantic import BaseModel, constr

# Create ToDo Schema (Pydantic Model)
class ToDoCreate(BaseModel):
    #task: constr(max_length=2)    
    task: str    

# Complete ToDo Schema (Pydantic Model)
class ToDo(BaseModel):
    id: int
    task: str  
    
    class Config:
        orm_mode = True