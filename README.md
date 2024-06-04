# Лабораторная работа №11
## Нечаева Н.

* Создали проект в PyCharm
*  Создали текстовой файл [requirements.txt](https://github.com/hbjnmcd/pythonProject11/blob/master/requirements.txt),
в который поместили все необходимые для импортирования пакеты.
*  После чего в Терминале написали:
* ![Чтобы импортировать все необходимое](/pictures/Рисунок1.png),
*  и получили
* ![Вот это](/pictures/image2.png)
*  Создали файл "main.py", в котором:
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/home")
def get_home():
      return{"data": "Hello world"}
```
*  Запустили через терминал
*  ![Чтобы при внесении изменений обновлялось автоматически](/pictures/Рисунок3.png)
*  И теперь можно посмотреть как это выглядит:
*  ![Ну пока не очень красиво](/pictures/Рисунок4.png)
*  "Наращиваем" функционал "main.py":
``` python
from typing import Optional, Annotated

from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI()


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None
class STask(STaskAdd):
    id: int
tasks = []
@app.post("/tasks")
async def add_task(
        task: Annotated[STaskAdd, Depends()],
):
    tasks.append(task)
    return {"ok": True}
```
*  Можно также посмотреть адрес "/docs":
*  ![Ну пока не очень красиво](/pictures/Рисунок5.png)
* Создаем новый файл, в котором будут основные функции для развертывания базы данных [database.py](https://github.com/hbjnmcd/pythonProject11/blob/master/database.py)
* Потом создаем еще очень много файлов, куда размещаем различные функции, и все для того, чтобы "main" выглядел красиво и незамусоренно. Например, все, относящееся к открываемым страницам, переносим в [router.py](https://github.com/hbjnmcd/pythonProject11/blob/master/router.py), а все, что относится к добавлению/удалению из БД, в [repo.py](https://github.com/hbjnmcd/pythonProject11/blob/master/repo.py), все что еще осталось выносим в  [schemas.py](https://github.com/hbjnmcd/pythonProject11/blob/master/schemas.py). Главное - не забыть везде выставить и поправить импорты, чтобы все работало корректно.
# 
По итогу я все сломала, и база данных создается, локально ее можно посмотреть, если понадобавлять всего-разного вот так:
  * ![Бывает](/pictures/Снимок_послений.JPG)
  * ![Бывает](/pictures/Снимок33.JPG)

Но в самом приложении все ломается. Надо разбираться.
