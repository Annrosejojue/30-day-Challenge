from fastapi import FastAPI

app = FastAPI()

todos = []

@app.post("/add")
def add_task(task: str):
    todos.append(task)
    return {"message": "Task added", "todos": todos}

@app.get("/list")
def list_tasks():
    return {"todos": todos}

@app.delete("/delete")
def delete_task(task: str):
    if task in todos:
        todos.remove(task)
        return {"message": "Task deleted", "todos": todos}
    return {"error": "Task not found"}
