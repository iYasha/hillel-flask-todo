from flask import Flask
from api.authorization import auth_api
from pages.authorization import auth_pages
from api.articles import article_api

app = Flask(__name__)
app.register_blueprint(auth_api)
app.register_blueprint(article_api)
app.register_blueprint(auth_pages)

"""
Вопросы:
1) Создание пользователя
"""

"""
Запрос на сервер:
 * путь
 * метод
 * данные
 
 
GET: (Params)
localhost:5000/user?username=Vasya&password=qwerty123&full_name=Vasya Pupkin

POST/PUT/PATCH: (Body)
localhost:5000/user
{
	"username": "Vasya",
	"password": "qwerty123",
	"full_name": "Vasya Pupkin"
}
"""

"""
Задачи: 
* Редактирование пользователя
* Удаление пользователя по id
"""

"""
Идентификация
email = vasya@gmail.com

Аутентификация
password = qwerty123

Авторизация
secret_word = asfhjasfkjaslfk1243124
"""


if __name__ == '__main__':
	app.run(debug=True)
