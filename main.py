from fastapi import FastAPI, status, HTTPException
from sqlalchemy.orm import Session



# Create the database
Base.metadata.create_all(engine)


    # return the id
    return tododb.id


    # get the todo item with the given id
    todo = crud_todo.delete_todo(session, id)

    # if todo item with given id exists, delete it from the database. Otherwise raise 404 error
    if not todo:
        raise HTTPException(status_code=404, detail=f"todo item with id {id} not found")

    return None


    return todo_list