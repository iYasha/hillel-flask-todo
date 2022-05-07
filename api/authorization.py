import flask
from flask import request
from core import config, utils

from crud.users import user_crud

auth_api = flask.Blueprint('auth_api', __name__)


@auth_api.route(config.API_ROUTE_PREFIX + 'register', methods=['POST'])
def register():
	data = request.json
	full_name = data.get('full_name')
	email = data.get('email')
	password = data.get('password')
	if email is None or email.find('@') == -1 or email.find('.') == -1:
		return utils.error(4, 'Некорректный email')
	if user_crud.get_by_email(email) is not None:
		return utils.error(2, 'Пользователь с таким email уже зарегистрирован')
	if password is None or len(password) < 6:
		return utils.error(5, 'Пароль должен быть не менее 6 символов')
	user = {
		'full_name': full_name,
		'email': email,
		'password': utils.hash_password(password),
		'access_token': utils.generate_access_token()
	}
	user_crud.create(user)
	return flask.jsonify({
			'code': 0,
			'message': 'User registered!',
			'user': user
		})


@auth_api.route(config.API_ROUTE_PREFIX + 'login', methods=['POST'])
def login():
	data = request.json
	email = data.get('email')
	password = data.get('password')

	user = user_crud.get_by_email(email)

	if user is None or not utils.check_password(password, user['password']):
		return utils.error(6, 'Неверный email или пароль')

	return flask.jsonify({
			'code': 0,
			'message': 'User logged in!',
			'access_token': user['access_token']
		})


@auth_api.route(config.API_ROUTE_PREFIX + 'user/me', methods=['GET'])
def get_user_info():
	"""
	Authorization: Bearer hV7g1pxCmWnJb3cY5KDY
	"""
	authorization_header = request.headers.get('Authorization')
	if authorization_header is None:
		return utils.error(7, 'Не передан заголовок Authorization')
	access_token = authorization_header.split()[1]

	user = user_crud.get_by_access_token(access_token)
	if user is None:
		return utils.error(8, 'Некорректный токен авторизации')

	return flask.jsonify({
			'code': 0,
			'message': 'User found',
			'user': user
		})
