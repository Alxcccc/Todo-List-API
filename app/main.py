from fastapi import FastAPI
from routes import todo, login, register

app = FastAPI()

# Routers
app.include_router(todo.router)
app.include_router(login.router)
app.include_router(register.router)

@app.get('/')
def main():
    return {'message': 'This is API for ToDo list'}