from crud.base import BaseCRUD


class TaskCRUD(BaseCRUD):
	_file_path = 'data/tasks.json'


task_crud = TaskCRUD()

