from pydantic import BaseModel, ValidationError, validator
import uuid
from datetime import datetime


class Article(BaseModel):
	id: uuid.UUID = uuid.uuid4()
	title: str
	content: str
	author: str
	created_at: datetime = datetime.now()

	@validator('title')
	def title_length(cls, v):
		if len(v) < 2 or len(v) > 10:
			raise ValueError('Заголовок должен содержать от 2 до 10 символов')
		return v

	@validator('author')
	def validate_author(cls, v):
		if len(v) < 3 or len(v.split()) != 2:
			raise ValueError('Автор должен содержать Имя и Фамилия и длина должна быть больше 10 символов')
		return v

# data = {
# 	'id': uuid.uuid4(),
# 	'content': 'test',
# 	'created_at': datetime.now()
# }
# try:
# 	article_1 = Article(title='1123', content='Content', author='test test')
# 	print(article_1)
# 	print(article_1.json())
# 	print(article_1.dict())
# except ValidationError as e:
# 	print(e.errors())
# 	print(e.json())
# try:
# 	article_1 = Article.parse_obj(data)  # parse_obj - преобразует словарь в обьект PyDantic
# except ValidationError as e:
# 	print(e.json())
# print(article_1)


"""
Задание 1:
Создать сущность User с помощью PyDantic
У пользователя есть следующие поля:
id - заполняется автоматически (UUID)
name - заполняется вручную, длина должна быть от 2 до 20 символов
age - заполняется вручную, должен быть в диапазоне от 0 до 200
email - заполняется вручную, нужно сделать проверку на то, что пользователь ввел корректный email
created_at - заполняется автоматически (datetime.now())

Создать обьект User и вывести его в формате json
"""


class User(BaseModel):
	id: uuid.UUID = uuid.uuid4()
	name: str
	age: int
	email: str
	created_at: datetime = datetime.now()

	@validator('name')
	def name_length(cls, v):
		if len(v) < 2 or len(v) > 20:
			raise ValueError('Имя должно содержать от 2 до 20 символов')
		return v

	@validator('email')
	def validate_email(cls, v):
		if v.find('@') == -1 or v.find('.') == -1:
			raise ValueError('Введите корректный email')
		return v

	@validator('age')
	def validate_age(cls, value):
		if value < 0 or value > 200:
			raise ValueError('Возраст должен быть в диапазоне от 0 до 200')
		return value


user_1 = User(name='Вася', age=20, email='vasya@gmail.com')
print(user_1.dict())


