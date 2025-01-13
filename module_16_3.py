from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Name: Example, Age:18'}

@app.get('/users')
async def get_users() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def add_user(username: str, age: int) -> str:
    new_id = str(int(max(users, key=int)) + 1)
    users[new_id] = f'Имя: {username}, возраст: {age}'
    return f'User {new_id} is registered'

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str, username: str, age: int) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is updated'

@app.delete('/user/{user_id}')
async def delete_user(user_id: str) -> str:
    users.pop(user_id)
    return f'User {user_id} is deleted'
