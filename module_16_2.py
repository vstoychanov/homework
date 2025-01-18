from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get('/')
async def main_page() -> dict:
    return {"message": "Главная страница"}

@app.get('/user/admin')
async def admin_page() -> dict:
    return {'message': 'Вы вошли как администратор'}

@app.get('/user/{user_id}')
async def user_page(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User id', example='55')]) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}

@app.get('/user/{username}/{age}')
async def user_info(username: Annotated[str, Path(min_length=5
                                                    , max_length=20
                                                    , description='Enter username'
                                                    , example='dede')]
                    , age: Annotated[int, Path(ge=18
                                                , le=120
                                                , description='Enter age'
                                                , example='54')]) -> dict:
    return {'message': f'Информация о пользователе. Имя: {username}, Возраст: {age}'}