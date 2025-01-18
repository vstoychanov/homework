from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def main_page() -> str:
    return f"Главная страница"

@app.get('/user/admin')
async def admin_page() -> str:
    return f'Вы вошли как администратор'

@app.get('/user/{user_id}')
async def user_page(user_id: str) -> str:
    return f'Вы вошли как пользователь № {user_id}'

@app.get('/user')
async def user_info(username: str, age: str) -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'
