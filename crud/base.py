import json
import os
import uuid


class BaseCRUD:
	_file_path = None

	def __init__(self):
		if self._file_path is None:
			raise ValueError('_file_path не заполнено')
		if not os.path.exists(self._file_path):  # Проверяем существует ли файл
			with open(self._file_path, 'w') as f:
				f.write('[]')  # Если файла нет, то мы записываем в файл пустой список, чтобы при парсинге json не было ошибки
		with open(self._file_path, 'r') as f:  # Считываем данные из файла
			self._data = json.loads(f.read())

	def save(self):
		with open(self._file_path, 'w') as f:
			f.write(json.dumps(self._data))

	def create(self, data: dict):
		data['id'] = str(uuid.uuid4())
		self._data.append(data)
		self.save()
		return data

	def get_one(self, obj_id: int):
		for data in self._data:
			if data['id'] == obj_id:
				return data
		return None

	def get_all(self):
		return self._data

	def update(self, new_data: dict, obj_id: int):
		for data in self._data:
			if data['id'] == obj_id:
				data.update(new_data)
				self.save()

	def delete(self, obj_id: int) -> bool:
		data = self.get_one(obj_id)
		if data:
			self._data.remove(data)
			self.save()
			return True
		return False

