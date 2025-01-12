from fastapi import FastAPI
from routes import todo, login

app = FastAPI()

# Routers
app.include_router(todo.router)
app.include_router(login.router)

@app.get('/')
def main():
    return {'message': 'Hello word'}