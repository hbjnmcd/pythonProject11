# Лабораторная работа №11
## Нечаева Н.

* Создали проект в PyCharm
*  Создали текстовой файл
  [requirements.txt](https://github.com/hbjnmcd/pythonProject11/blob/master/requirements.txt),
в который поместили все необходимые для импортирования пакеты.
*  После чего в Терминале написали:
  ![Чтобы импортировать все необходимое](/pictures/Рисунок1.png),
*  и получили
  ![Вот это](/pictures/image2.png)
*  Создали файл "main.py", в котором:
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/home")
def get_home():
      return{"data": "Hello world"}
```
*  Запустили через терминал                
 ![Чтобы при внесении изменений обновлялось автоматически](/pictures/Рисунок3.png)
*  И теперь можно посмотреть как это выглядит:
![Ну пока не очень красиво](/pictures/Рисунок4.png)
*  
