from pydantic import BaseModel, validator
import uuid
from datetime import datetime


class Article(BaseModel):
	id: str = str(uuid.uuid4())
	title: str
	content: str
	author: str
	file_name: str
	created_at: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	@validator('title')
	def check_title(cls, value):
		if len(value) < 3 or len(value) > 100:
			raise ValueError('Заголовок должен быть больше чем 3 символа и меньше чем 100')
		return value

	@validator('content')
	def check_content(cls, value):
		if len(value) < 3 or len(value) > 1000:
			raise ValueError('Содержимое должно быть больше чем 3 символа и меньше чем 1000')
		return value

	@validator('author')
	def check_author(cls, value):
		if len(value.split()) != 2:
			raise ValueError('Имя и фамилия автора должны быть разделены пробелом')
		return value
