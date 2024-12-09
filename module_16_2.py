from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Главная страница"}

@app.get("/user/admin")
async def admin_page():
    return {"Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def user_id_page(user_id: int = Path(gt=1, lt=100, description='Enter User ID', example='1')):
    return {f"Вы вошли как пользователь № {user_id}"}

@app.get('/user/{username}/{age}')
async def user_inform_page(username: Annotated[str, Path(gt=5, lt=20, description='Enter username', example='UrbanUser')],
                            age: Annotated[int,Path(gt=18, lt=120, description='Enter age', example='24')]):
    return {f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

## Запуск:
## 1. Переход в директорию: cd module_16/homework_16_2/
## 2. Сам запуск: uvicorn module_16_2:app --reload