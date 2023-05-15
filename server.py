from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import Todo

app = FastAPI()

origins = ['https://localhost:3000']

from database import(
    deleteTodo,
    fetchAllTodo,
    updateTodo,
    createNewTodo,
    fetchSingleTodo
)



app.add_middleware(
    CORSMiddleware,
    # allow_orgins = origins,
    # allow_credentials = True,
    # allow_methods = ["*"],
    # allow_headers=["*"],
)

@app.get("/")
def checkConnection():
    return {"Connection": "Connected to server..."}




@app.get("/api/all-todo")
async def getTodo():
    response = await fetchAllTodo()
    return response


@app.get("/api/todo/{title}", response_model=Todo)
async def fetchOneTodo(title):
    response = await fetchSingleTodo(title)
    if response:
        return response
    raise HTTPException(501, "There is no todo item with this title")




@app.post("/api/create-todo", response_model= Todo)
async def createTodo(todo: Todo):
    response = await createNewTodo(todo.dict())
    if response:
        return response
    raise HTTPException(501, "Unable to create todo")



@app.put("/api/update-todo/{title}", response_model=Todo)
async def updateTodoByTitle(title: str, desc: str):
    response = await updateTodo(title, desc)

    if response:
        return response
    
    raise HTTPException(501, "Unable to update todo")



@app.delete("/api/delete/{title}")
async def deleteTodoByTitle(title):
    response = await deleteTodo(title)

    if response:
        return response
    
    raise HTTPException(501, "Failed to delete Todo")