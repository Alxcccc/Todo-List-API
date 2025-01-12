from fastapi import APIRouter

router = APIRouter(prefix="/api")

@router.get('/todo', summary='All tasks', tags=["CRUD todo list"],)
async def get_tasks():
    return {'message': 'hola mundo'}