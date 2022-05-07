from crud.base import BaseCRUD


class UserCRUD(BaseCRUD):
	_file_path = 'data/users.json'

	def get_by_email(self, email: str):
		for user in self._data:
			if user['email'] == email:
				return user
		return None

	def get_by_access_token(self, access_token: str):
		for user in self._data:
			if user['access_token'] == access_token:
				return user
		return None


user_crud = UserCRUD()
