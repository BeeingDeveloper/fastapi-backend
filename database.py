from model import Todo

import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient
('mongodb+srv://officialakhter007:AKHTERX2000@fastapi.uw2wzfj.mongodb.net/')
database = client.TodoList
collection = database.todo




async def fetchSingleTodo(title):
    document = await collection.find_one({"title": title})
    return document


async def fetchAllTodo():
    todos = collection.find()
    return todos


async def createNewTodo(todo):
    document = todo
    result = collection.insert_one(document)
    return result


async def updateTodo(title, desc):
    await collection.update_one({"title": title}, {"$set": {"description": desc}})

    documnet = await collection.find_one({"title": title})
    return documnet


async def deleteTodo(title):
    await collection.delete_one({"title": title})
    return True