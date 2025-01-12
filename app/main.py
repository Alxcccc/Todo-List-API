from fastapi import FastAPI
from routes import todo

app = FastAPI()

# Routers
app.include_router(todo.router)

@app.get('/')
def main():
    return {'message': 'Hello word'}